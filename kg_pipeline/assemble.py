# -*- coding: utf-8 -*-
"""
Final assembly: builds all nodes + edges, validates referential integrity,
writes deped_science_kg_full.json (all grades) and per-grade split files.
"""
import json
from collections import defaultdict
from build_nodes import build_nodes
from build_edges import build_keyword_index, generate_horizontal_edges, generate_vertical_edges, generate_cross_strand_edges, dedupe_edges

def main():
    nodes = build_nodes()
    lcs = [n for n in nodes if n["type"] == "learning_competency"]
    for n in lcs:
        n["strand_code"] = n["id"].split("-")[-1]
    build_keyword_index(lcs)

    h_edges = dedupe_edges(generate_horizontal_edges(lcs))
    v_edges = dedupe_edges(generate_vertical_edges(lcs))
    x_edges = dedupe_edges(generate_cross_strand_edges(lcs))
    all_edges = h_edges + v_edges + x_edges

    # strip internal helper fields before output
    clean_nodes = []
    for n in nodes:
        n2 = {k: v for k, v in n.items() if not k.startswith("_") and k != "strand_code"}
        clean_nodes.append(n2)

    # ---- VALIDATION ----
    node_ids = set(n["id"] for n in clean_nodes)
    errors = []

    # 1. every edge references existing nodes
    for e in all_edges:
        if e["source"] not in node_ids:
            errors.append(f"Edge source not found: {e['source']}")
        if e["target"] not in node_ids:
            errors.append(f"Edge target not found: {e['target']}")

    # 2. every LC has a valid parent CS
    for n in clean_nodes:
        if n["type"] == "learning_competency":
            if n["parent"] not in node_ids:
                errors.append(f"LC {n['id']} has orphan parent {n['parent']}")

    # 3. no duplicate node IDs
    id_counts = defaultdict(int)
    for n in clean_nodes:
        id_counts[n["id"]] += 1
    dupes = [i for i, c in id_counts.items() if c > 1]
    if dupes:
        errors.append(f"Duplicate node IDs: {dupes}")

    # 4. no self-loop edges
    self_loops = [e for e in all_edges if e["source"] == e["target"]]
    if self_loops:
        errors.append(f"Self-loop edges: {len(self_loops)}")

    print("=" * 60)
    print("VALIDATION")
    print("=" * 60)
    if errors:
        print(f"FAILED - {len(errors)} error(s):")
        for e in errors[:20]:
            print(" -", e)
    else:
        print("PASSED - no dangling references, no orphan parents, no dupes, no self-loops.")

    # ---- STATS ----
    cs_count = sum(1 for n in clean_nodes if n["type"] == "content_standard")
    lc_count = sum(1 for n in clean_nodes if n["type"] == "learning_competency")
    print("\n" + "=" * 60)
    print("STATS")
    print("=" * 60)
    print(f"Total nodes: {len(clean_nodes)}  (CS: {cs_count}, LC: {lc_count})")
    print(f"Total edges: {len(all_edges)}  (horizontal: {len(h_edges)}, vertical: {len(v_edges)}, cross-strand: {len(x_edges)})")
    grade_skips = [e for e in v_edges if e.get("grade_skip")]
    print(f"Grade-skip vertical edges: {len(grade_skips)}")

    per_grade = defaultdict(lambda: {"cs": 0, "lc": 0})
    for n in clean_nodes:
        per_grade[n["grade"]][{"content_standard": "cs", "learning_competency": "lc"}[n["type"]]] += 1
    print("\nPer-grade node counts:")
    for g in sorted(per_grade):
        print(f"  Grade {g}: CS={per_grade[g]['cs']}, LC={per_grade[g]['lc']}")

    # ---- OUTPUT: full combined file ----
    output = {"nodes": clean_nodes, "edges": all_edges}
    with open("../deped_science_kg_full.json", "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    # ---- OUTPUT: per-grade split files (nodes for that grade + edges touching them) ----
    for grade in range(3, 11):
        g_node_ids = set(n["id"] for n in clean_nodes if n["grade"] == grade)
        g_nodes = [n for n in clean_nodes if n["grade"] == grade]
        g_edges = [e for e in all_edges if e["source"] in g_node_ids or e["target"] in g_node_ids]
        g_output = {"nodes": g_nodes, "edges": g_edges}
        with open(f"/mnt/user-data/outputs/grade{grade}_kg_v2.json", "w") as f:
            json.dump(g_output, f, indent=2, ensure_ascii=False)

    print("\nWrote deped_science_kg_full.json and grade3_kg_v2.json ... grade10_kg_v2.json")
    return errors

if __name__ == "__main__":
    errors = main()
