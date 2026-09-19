# -*- coding: utf-8 -*-
"""
Edge generation: horizontal (within-grade-quarter) and vertical (cross-grade)
edges, built programmatically from node text similarity + strand continuity.
Lean output: no notes/rationale text, per user preference.
"""
import re
from collections import defaultdict
from build_nodes import build_nodes

BLOOM_ORDER = ["remember", "understand", "apply", "analyze", "evaluate", "create"]
BLOOM_RANK = {b: i for i, b in enumerate(BLOOM_ORDER)}

# Stopwords to ignore in keyword overlap matching — expanded to catch
# generic curriculum scaffolding language that isn't a real concept link.
STOPWORDS = set("""
a an the of to in on and or with for from by as is are that this these those it its their
they such using use used describe explain identify demonstrate participate guided
activities secondary sources information how what when where
learners local school home community everyday simple science process processes
things people objects ways make different various common examples example including
observe observed observation record recording show shows including relation relative
based than able need needs needed help helps important explain explained explains
class group groups discuss discussion recognize identify identifying appropriate
around some several every each other another same over into during after before
scientific investigation investigations carry terms structure state states changes change
cause causes valid reliable steps
""".split())

MIN_KEYWORD_LEN = 5  # ignore short generic words like "area", "type"

def keywords(text):
    words = re.findall(r"[a-zA-Z']+", text.lower())
    return set(w for w in words if w not in STOPWORDS and len(w) >= MIN_KEYWORD_LEN)

def overlap_score(a_kw, b_kw):
    if not a_kw or not b_kw:
        return 0
    inter = a_kw & b_kw
    return len(inter)

def build_keyword_index(lcs):
    for n in lcs:
        n["_kw"] = keywords(n["full_text"] + " " + n["label"])
    return lcs


# ---------------------------------------------------------------- HORIZONTAL
def generate_horizontal_edges(lcs, min_overlap=2):
    """Within the same grade+quarter, link LC pairs with keyword overlap.
    Same-CS pairs (siblings) get 'complements' if adjacent in sequence,
    else 'applies_to'. Cross-CS pairs within the same quarter get
    'shares_context' if overlap found."""
    edges = []
    by_gq = defaultdict(list)
    for n in lcs:
        by_gq[(n["grade"], n["quarter"])].append(n)

    for (grade, q), group in by_gq.items():
        group_sorted = sorted(group, key=lambda n: int(n["id"].split("-LC")[1].split("-")[0]))
        for i, a in enumerate(group_sorted):
            for b in group_sorted[i+1:]:
                same_cs = a["parent"] == b["parent"]
                score = overlap_score(a["_kw"], b["_kw"])
                is_adjacent = same_cs and (
                    int(a["id"].split("-LC")[1].split("-")[0]) + 1
                    == int(b["id"].split("-LC")[1].split("-")[0])
                )
                if same_cs and is_adjacent:
                    rel = "complements"
                elif same_cs and score >= 1:
                    rel = "applies_to"
                elif (not same_cs) and score >= min_overlap:
                    rel = "shares_context"
                else:
                    continue
                edges.append({
                    "source": a["id"],
                    "target": b["id"],
                    "connection_type": "horizontal",
                    "relationship": rel,
                })
    return edges


# ------------------------------------------------------------------ VERTICAL
def generate_vertical_edges(lcs, min_overlap=2, max_grade_gap=4):
    """For every LC, look at LCs in LATER grades within the same strand,
    and link to the best-scoring match in the nearest grade that has one
    (so we don't fan out to every later grade redundantly)."""
    edges = []
    by_strand_grade = defaultdict(list)
    for n in lcs:
        by_strand_grade[(n["strand_code"], n["grade"])].append(n)

    strand_codes = set(n["strand_code"] for n in lcs)
    grades = sorted(set(n["grade"] for n in lcs))

    for strand in strand_codes:
        for src_grade in grades:
            sources = by_strand_grade.get((strand, src_grade), [])
            if not sources:
                continue
            for src in sources:
                best_match = None
                best_score = 0
                best_target_grade = None
                for gap in range(1, max_grade_gap + 1):
                    tgt_grade = src_grade + gap
                    if tgt_grade not in grades:
                        continue
                    targets = by_strand_grade.get((strand, tgt_grade), [])
                    if not targets:
                        continue
                    for tgt in targets:
                        score = overlap_score(src["_kw"], tgt["_kw"])
                        if score > best_score:
                            best_score = score
                            best_match = tgt
                            best_target_grade = tgt_grade
                    if best_match:
                        # found a match at nearest available grade gap; stop searching further grades
                        break
                if best_match and best_score >= min_overlap:
                    src_bloom = BLOOM_RANK.get(src.get("bloom_level"), 1)
                    tgt_bloom = BLOOM_RANK.get(best_match.get("bloom_level"), 1)
                    if tgt_bloom > src_bloom:
                        rel = "extends"
                    elif tgt_bloom == src_bloom:
                        rel = "builds_on"
                    else:
                        rel = "applies_to"
                    edges.append({
                        "source": src["id"],
                        "target": best_match["id"],
                        "connection_type": "vertical",
                        "relationship": rel,
                        "bloom_shift": f"{src.get('bloom_level')} -> {best_match.get('bloom_level')}",
                        "grade_skip": (best_target_grade - src_grade) > 1,
                    })
    return edges


# ----------------------------------------------------------------- CROSS-STRAND
def generate_cross_strand_edges(lcs, min_overlap=3):
    """Find LC pairs in DIFFERENT strands (any grade/quarter) that share
    enough real vocabulary to represent a genuine cross-cutting topic
    (e.g. process skills reused across strands, water/carbon/oxygen
    cycles spanning Matter and Living Things). Uses a higher threshold
    than same-strand matching since cross-strand false positives are
    more likely (different subject areas share fewer *real* concepts,
    so any overlap needs to be more deliberate)."""
    edges = []
    for i, a in enumerate(lcs):
        for b in lcs[i+1:]:
            if a["strand_code"] == b["strand_code"]:
                continue
            score = overlap_score(a["_kw"], b["_kw"])
            if score >= min_overlap:
                edges.append({
                    "source": a["id"],
                    "target": b["id"],
                    "connection_type": "cross_strand",
                    "relationship": "shares_context",
                })
    return edges


def dedupe_edges(edges):
    seen = set()
    out = []
    for e in edges:
        key = (e["source"], e["target"], e["connection_type"])
        if key in seen:
            continue
        seen.add(key)
        out.append(e)
    return out


if __name__ == "__main__":
    nodes = build_nodes()
    lcs = [n for n in nodes if n["type"] == "learning_competency"]
    for n in lcs:
        n["strand_code"] = n["id"].split("-")[-1]
    build_keyword_index(lcs)

    h_edges = generate_horizontal_edges(lcs)
    v_edges = generate_vertical_edges(lcs)
    h_edges = dedupe_edges(h_edges)
    v_edges = dedupe_edges(v_edges)

    print("Horizontal edges:", len(h_edges))
    print("Vertical edges:", len(v_edges))
    print("\nSample horizontal:")
    for e in h_edges[:5]:
        print(" ", e)
    print("\nSample vertical:")
    for e in v_edges[:5]:
        print(" ", e)

    grade_skips = [e for e in v_edges if e["grade_skip"]]
    print(f"\nGrade-skip vertical edges: {len(grade_skips)}")
