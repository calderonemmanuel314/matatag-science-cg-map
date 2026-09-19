# -*- coding: utf-8 -*-
"""
Node generation: builds CS and LC nodes from raw curriculum data,
auto-assigns IDs, strand metadata, and Bloom's level via lead-verb lookup.
"""
import re
from curriculum_data import GRADES, STRAND_CODE

# ---- Bloom's verb lookup table -------------------------------------------
# Ordered by specificity; first match wins. Keys are lead verbs/phrases
# commonly used in DepEd LC text.
BLOOM_VERB_MAP = [
    # Create (highest)
    (["design", "construct", "develop", "formulate", "plan and carry out", "propose"], "create"),
    # Evaluate
    (["evaluate", "assess", "critique", "justify", "debate", "recognize the advantages and limitations", "predict the position"], "evaluate"),
    # Analyze
    (["analyze", "differentiate", "compare", "classify", "investigate", "examine", "distinguish",
      "relate", "explore the school grounds", "interpret"], "analyze"),
    # Apply
    (["demonstrate", "apply", "measure", "use", "calculate", "carry out", "assemble", "draw a",
      "construct and annotate", "make a", "make models", "make drawings", "trace", "express quantitatively",
      "write the chemical", "write equations", "create a scale drawing"], "apply"),
    # Understand
    (["describe", "explain", "discuss", "summarize", "identify and explain", "predict and explain",
      "gather information", "explain why", "explain how", "explain that", "explain the"], "understand"),
    # Remember (lowest / most literal)
    (["identify", "recognize", "list", "name", "define", "state"], "remember"),
]

def bloom_level(lc_text: str) -> str:
    """Infer Bloom's level from the lead verb / phrase of an LC statement."""
    text = lc_text.strip().lower()
    # Strip common lead-in scaffolding like "participate in guided activities to..."
    scaffolds = [
        "participate in guided activities to ",
        "participate in a guided investigation to ",
        "participate in guided science activities to ",
        "carry out guided investigations to ",
        "use information from secondary sources to ",
        "use information from secondary resources to ",
        "gather information from secondary sources to ",
        "use models and labeled diagrams to ",
    ]
    for s in scaffolds:
        if text.startswith(s):
            text = text[len(s):]
            break

    for verbs, level in BLOOM_VERB_MAP:
        for v in verbs:
            if text.startswith(v):
                return level
    # fallback: search anywhere in first 6 words if no prefix match
    head = " ".join(text.split()[:6])
    for verbs, level in BLOOM_VERB_MAP:
        for v in verbs:
            if v in head:
                return level
    return "understand"  # safe default

# ---- Manual overrides for genuinely ambiguous LCs -------------------------
# Keyed by (grade, quarter, lc_number)
BLOOM_OVERRIDES = {
    (3, 2, 8): "understand",   # "recognize that there is a need to protect..." - attitude/value, not pure recall
    (6, 1, 9): "understand",   # "recognize the features of a fair test..." - conceptual, not rote
    (9, 1, 6): "understand",   # "identify that electricity is a flow..." + "show appreciation" - conceptual
}

def get_bloom(grade, q, n, text):
    if (grade, q, n) in BLOOM_OVERRIDES:
        return BLOOM_OVERRIDES[(grade, q, n)]
    return bloom_level(text)


def short_label(text: str, max_words=9) -> str:
    """Generate a short label from full LC/CS text."""
    t = text.strip().rstrip(".")
    t = t[0].upper() + t[1:] if t else t
    words = t.split()
    if len(words) > max_words:
        t = " ".join(words[:max_words]) + "..."
    return t


def build_nodes():
    nodes = []
    for grade, quarters in GRADES.items():
        for quarter in quarters:
            q = quarter["q"]
            strand_label = quarter["strand"]
            strand_code = STRAND_CODE[strand_label]
            # CS nodes
            for cs in quarter["cs"]:
                cs_id = f"G{grade}-Q{q}-CS{cs['n']}-{strand_code}"
                nodes.append({
                    "id": cs_id,
                    "type": "content_standard",
                    "grade": grade,
                    "quarter": q,
                    "strand": strand_label,
                    "parent": None,
                    "label": cs["topic"],
                    "full_text": cs["text"],
                })
            # LC nodes
            for lc in quarter["lc"]:
                lc_id = f"G{grade}-Q{q}-LC{lc['n']}-{strand_code}"
                cs_id = f"G{grade}-Q{q}-CS{lc['cs_n']}-{strand_code}"
                nodes.append({
                    "id": lc_id,
                    "type": "learning_competency",
                    "grade": grade,
                    "quarter": q,
                    "strand": strand_label,
                    "parent": cs_id,
                    "label": short_label(lc["text"]),
                    "full_text": lc["text"],
                    "bloom_level": get_bloom(grade, q, lc["n"], lc["text"]),
                })
    return nodes


if __name__ == "__main__":
    nodes = build_nodes()
    cs_count = sum(1 for n in nodes if n["type"] == "content_standard")
    lc_count = sum(1 for n in nodes if n["type"] == "learning_competency")
    print(f"Total nodes: {len(nodes)} (CS: {cs_count}, LC: {lc_count})")

    # Bloom distribution sanity check
    from collections import Counter
    bloom_dist = Counter(n["bloom_level"] for n in nodes if n["type"] == "learning_competency")
    print("Bloom's distribution:", dict(bloom_dist))

    # spot check a few
    for n in nodes[:5]:
        print(n["id"], "|", n.get("bloom_level", "-"), "|", n["label"])
