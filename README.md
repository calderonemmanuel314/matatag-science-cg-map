# DepEd Science Curriculum Knowledge Graph — Source Code

## What's here

### `kg_pipeline/` — Python data pipeline
Generates the knowledge graph JSON (nodes + edges) from the raw MATATAG
Science CG text. Run in order (or just run `assemble.py`, which imports
the others):

1. `curriculum_data.py` — hand-transcribed raw CS/LC data for Grades 3-10,
   structured as `GRADES[grade] = [quarters...]`. Edit this file if you
   spot a transcription error against the official CG PDF.
2. `build_nodes.py` — turns raw data into Content Standard and Learning
   Competency nodes, auto-generates IDs (`G{grade}-Q{quarter}-{CS|LC}{n}-{STRAND}`),
   and tags each LC with a Bloom's Taxonomy level via a lead-verb lookup
   table (with a small manual-override dict for ambiguous cases).
3. `build_edges.py` — generates three edge types via keyword-overlap
   matching:
   - **horizontal**: within the same grade+quarter (same-CS siblings →
     `complements`/`applies_to`; cross-CS → `shares_context`)
   - **vertical**: same strand, later grade, best keyword match at the
     nearest grade that has one (auto-flags `grade_skip: true` when the
     match isn't in the immediately next grade)
   - **cross_strand**: different strand entirely, any grade — uses a
     higher overlap threshold (3 vs 2) since cross-strand false positives
     are easier to generate from incidental shared words
4. `assemble.py` — runs the full pipeline, validates referential integrity
   (no dangling edges, no orphan parents, no duplicate IDs, no self-loops),
   prints stats, and writes:
   - `deped_science_kg_full.json` — everything, all 8 grades
   - `grade{3..10}_kg_v2.json` — per-grade splits (nodes for that grade +
     any edge touching them)

**To run:**
```bash
cd kg_pipeline
python3 assemble.py
```
Output files are written to `/mnt/user-data/outputs/` — change the paths
at the bottom of `assemble.py` if you're running this outside that
environment.

**Tuning knobs**, if you want to regenerate with different sensitivity:
- `build_edges.py` → `STOPWORDS` set and `MIN_KEYWORD_LEN` control what
  counts as a "real" keyword vs. generic curriculum filler
- `generate_horizontal_edges(lcs, min_overlap=2)` — cross-CS threshold
- `generate_vertical_edges(lcs, min_overlap=2, max_grade_gap=4)` —
  cross-grade threshold and how far forward to search
- `generate_cross_strand_edges(lcs, min_overlap=3)` — cross-strand
  threshold

### `kg_visualization_template.html` — the visualization, pre-data-injection
This is the actual page source: D3 force-directed graph, grade/quarter
timeline layout, strand color-coding, side panel, filters. It contains a
placeholder, `__DATA_PLACEHOLDER__`, where the graph JSON gets substituted
in before publishing — the file as published to you (`deped_science_kg.html`)
has the full ~325-node dataset already embedded in place of that
placeholder, which is why it's a much larger file.

**To rebuild the final page yourself** after regenerating the data:
```python
import json
data = json.load(open("deped_science_kg_full.json"))
html = open("kg_visualization_template.html").read()
html = html.replace("__DATA_PLACEHOLDER__", json.dumps(data, ensure_ascii=False))
open("deped_science_kg.html", "w").write(html)
```

**Structure of the template**, roughly top to bottom:
- CSS custom properties for the color system (strand colors: amber for
  Matter, green for Living Things, blue for Force/Motion/Energy, rust for
  Earth/Space)
- Header, strand legend, grade timeline strip (all vanilla JS, no
  framework)
- `RAW_DATA` — where the placeholder lives
- D3 setup: SVG, zoom/pan, force simulation (`forceX`/`forceY` position by
  grade+quarter and strand lane, `forceLink` handles the three edge types
  with different distance/strength, `forceCollide` prevents overlap)
- Render functions for links, nodes, axis backdrop (grade/quarter labels)
- Side panel logic: click a node → shows full competency text, Bloom's
  level, and clickable lists of vertical/horizontal/cross-strand
  connections

## Known limitations (worth knowing if you keep extending this)
- Keyword-overlap matching is blunt — it finds edges that share
  vocabulary, not necessarily edges that share deep conceptual structure.
  It correctly caught things like "transverse waves" (G6) → "electromagnetic
  radiation as transverse waves" (G9), but it can also miss real
  conceptual links that use different wording, or catch coincidental
  overlaps that aren't meaningful.
- All curriculum text in `curriculum_data.py` was manually transcribed
  from the CG PDF — worth spot-checking against the source if precision
  matters for your use case.
- No automated tests beyond the referential-integrity validation in
  `assemble.py`.
