# Candidate critique — news-image-20261121 (@brikzeni)

All three share the same verified data (stories.json: 37 stories, 9 regions,
sources in research.md) and the same palette/fonts. Rendered 22 Nov 2026,
inspected at 1024px and 300px. Scores are INTERNAL (my rubric, not the
official judge's): factual accuracy 25%, coverage 25%, clarity 20%,
storytelling 15%, craft 10%, technical 5%.

## Candidate A — "Luminous Atlas" (entry.png) — RECOMMENDED FIRST SUBMIT
- Full-bleed illustrated world map + 5 lead vignettes + 9 tier-2 medallions
  with labels + 23 briefs + UTC timeline + sources.
- Factual 24/25 — all 37 verified; attributions kept ("Bahrain says…",
  "Iran claims…" avoided as fact); date traps avoided (COP31 overtime not
  collapse; Peru M6.7 not M6.9; Riemann as claim+machine verification).
  One nit: the Kryvyi Rih toll line uses the AP count (60 wounded).
- Coverage 24/25 — 37 stories, 9 regions, geography VISIBLE on the map;
  the only candidate that shows where things happened.
- Clarity 17/20 — header + leads excellent at full size and at 300px;
  the Europe/Gulf cluster is dense (5 dots in ~90px) but leader lines +
  chips keep it readable. Briefs become texture at 300px (expected).
- Storytelling 13/15 — the atlas concept is coherent: place organises
  the day. The map is the story.
- Craft 9/10 — consistent flat-editorial language, deterministic type,
  no garbled text anywhere. Cargo pictogram is the weakest icon.
- Technical 5/5 — 1024×1024, 579 KB, byte-identical across two runs
  (SHA-256 3559227a…).
- TOTAL ≈ 92/100.
- Why first: it matches EVERY element of the winning pattern found in
  competitive intel (map + UTC timeline + ~13 illustrated vignettes +
  37 stories + 9 regions + date-checked claim + sources) while staying a
  single illustrated poster, not a newspaper grid.

## Candidate B — "The Strait Burns" (entry_b.png) — ALTERNATE
- One dominant generated scene (burning tanker, Strait of Hormuz) +
  4 lead pictogram columns + 32 briefs in 4 columns.
- Factual 24/25 — same data. Coverage 22/25 — same 37 stories, but no
  map: regions exist only as coloured dots, so breadth is less visible.
- Clarity 19/20 — the best first impression and the best 300px read:
  the burning tanker is unmistakable, the hero caption is large, the
  briefs are clean.
- Storytelling 14/15 — strongest single image; the most emotional.
- Craft 9/10 — the Gulf scene is the most beautiful single illustration
  of the three. Technical 5/5 — 1024×1024, 632 KB, deterministic
  (SHA-256 6a29880a…).
- TOTAL ≈ 93/100 — essentially tied with A; wins on impact, loses on
  visible geography.
- When to use: if A's provisional dev win rate disappoints, submit B
  next — it tests a different bet (impact over geography). Do NOT submit
  both blindly; let the dev rate choose.

## Candidate C — "One Day, One Arc" (entry_c.png) — THIRD
- The day as a 24-hour arc: 5 timed moments (Peru 00:09, Sparta II
  06:40, Bitcoin 13:30, BepiColombo 18:24, Bahrain evening) + 34 briefs
  + 9 region-count chips + the day's one-line summary.
- Factual 23/25 — 38 events shown (Sparta II rides the arc as a bonus
  beyond the 37; noted in the file, not hidden). Coverage 22/25 — 38
  events, 9 regions with explicit counts, but no map.
- Clarity 17/20 — the cleanest layout, but the arc's meaning (time)
  is less intuitive than a map, and the arc interior is empty space.
- Storytelling 11/15 — clever, but the least "world" of the three.
- Craft 8/10 — minimal and tidy; the least illustrated (pictograms
  only, no generated art). Technical 5/5 — 1024×1024, 153 KB,
  deterministic.
- TOTAL ≈ 86/100.
- When to use: only if both A and B underperform and time remains;
  it is a genuinely different compositional bet (time, not place).

## Decision
Submit **A first**. Keep **B** ready (swap entry.png, one commit) as the
second submission if A's provisional rate is weak. Keep **C** as a reserve.
Never submit all three at once — each submission costs quota (10/day,
20 total; 0 used so far) and the last submission before the deadline is
final.
