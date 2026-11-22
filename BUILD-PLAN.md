# Build plan — news-image-20261121 (updated with competitive intel)

## Target (from intel, verified 22 Nov ~15:35 UTC)
- **35–39 stories, 7–9 regions.** Mode top-50 = 35; #1 won with 37/9.
  Write the count visibly on the image ("37 STORIES · 9 REGIONS").
- **Leads (consensus, in order):** (1) Iran–Bahrain strikes,
  (2) COP31 overtime Antalya, (3) Peru quake M6.7 — then El Chapo Isidro
  capture, Riyadh missile intercepts, Kryvyi Rih strike, BepiColombo at
  Mercury, Hormuz tankers.
- **Format:** one illustrated world atlas (single composition) + ~13
  illustrated vignettes at their real locations + remaining stories as
  short region-labelled briefs + UTC timeline strip + big date.
  NO newspaper-card grid, NO navy+gold, NO boxed article summaries.
- **Date discipline (traps):** COP31 COLLAPSED on 22 Nov — 21 Nov is
  overtime/deadlock only. Peru quake M6.7 (not M6.9), event Fri night
  20 Nov local, reported 21 Nov; 1 killed, 16 injured, 853 displaced.
  Iran–Bahrain: attribute ("Bahrain says…", "Iran claims…") — casualties
  and Patriot-radar claims differ by source. Kryvyi Rih: 7yo + 20yo woman
  killed, 60+ injured. Russian ship = Sparta II, 2 drones, 16 crew
  evacuated. El Chapo Isidro: US reward $5M.
- **Route:** hybrid A+B — Route A content (37 stories) inside a Route B
  single editorial illustration. Iterate 2–3 variants; let dev win rate
  choose (parent submits only with user approval).

## Pipeline (proven news-19 v4 pattern)
1. `research.md` (subagent) → verified story list with sources.
2. `stories.json` — the 37 selected stories: id, region, place, lat/lon
   (approx, for map placement), tier (1/2/3), headline (short, verified),
   fact (one number or detail), source.
3. Generated base art (no text inside): `illustrations/world-atlas-base.png`.
4. `render.py` — deterministic Pillow compositor: base art + coded
   pictograms for tier-2 vignettes + ALL typography (Liberation/DejaVu).
   Writes `entry.png` (1024×1024, RGB, <1 MiB).
5. `main.ts` — starter copy program (stdlib only), copies entry.png to
   /output/entry.png. `main.py` NOT used as entrypoint (Pillow is not
   stdlib; grader installs nothing).
6. Validate: run render twice → SHA-256 identical; check 1024×1024,
   bytes ≤ 1048576, PNG decodes, offline.
7. GitHub repo (gh, brikzeni) + LICENSE + README (make.fun template) +
   bundle --dry-run → report to parent (no submit without approval).

## Candidates (3, to render and compare)
- A — "Luminous Atlas": full-bleed illustrated world map, vignettes on
  location, timeline strip at bottom. (primary)
- B — "One Day, Many Fronts": panoramic band composition — Gulf lead
  scene large left, COP31 + Peru + Mexico scenes right, briefs below.
- C — "The Day in One Picture": single dominant illustrated scene
  (Shenzhen summit table / three powers) with the rest of the world as
  labelled orbit ring.

## Open items / risks
- research.md still pending (subagent running) — final story list, numbers,
  and sources depend on it.
- Transcript eligibility: Muse sessions need --muse-usage rows; no
  muse-usage-news-image-20261121.jsonl exists yet. Parent to create from
  real usage data; handed-over sessions take NO paid place (handed_over_places=none).
  Flag honestly in final report.
- Quota: 10/day, 20 total; 0 used so far for this competition by @brikzeni.
