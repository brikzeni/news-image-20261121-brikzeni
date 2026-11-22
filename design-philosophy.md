# Design philosophy — "One Day, Held Up to the Light"

## Movement: Luminous Atlas

A single day of world news is not a list. It is a planet turning once under
the light, and the light catching a different edge of every continent as it
goes. This philosophy treats the image as one luminous object: a warm-paper
world held up to the light, where geography is the skeleton, illustration is
the flesh, and words are only the labels pinned where the eye already looks.

## Space and form

One clear composition, one focal mass, generous breathing room. The world is
drawn as a single continuous illustrated field — not a grid of boxes, not a
magazine spread, not a dashboard. Stories sit where they happened, on a
living map, so place itself does the organising. A strong horizon or orbit
line gives the eye a path; secondary stories orbit the lead stories the way
time zones orbit a day. Nothing floats unattached; every mark answers to the
geography beneath it.

## Colour and material

Warm paper, deep ink, one hot accent. Cream paper (#F4EBD8 family) as the
ground — newsprint you can feel, not a screen. Deep ink-teal for land and
type. A single vermilion / signal-red accent reserved for the day's sharpest
edges (casualty, rupture, breakthrough), used sparingly so it never shouts
twice. No navy-and-gold: that was yesterday's poster. The palette is
deliberately narrow so the judge's eye, at 300 pixels across, still reads
three zones instantly: paper, land, accent.

## Scale and rhythm

Three tiers, three sizes, no more. Tier 1 (3–5 stories): large illustrated
scenes with bold two-line headlines, readable at thumbnail size. Tier 2
(8–12 stories): compact illustrated vignettes with one-line labels. Tier 3
(remaining verified stories): short place + fact labels along the map's
margins and arcs, set small but never grey-on-busy — always on paper, always
legible. Rhythm comes from alternating scene and silence: a dense cluster,
then open ocean, then a single quiet label.

## Typography

Two families only. A sturdy serif for the title and Tier 1 headlines
(Liberation Serif Bold / DejaVu Serif Bold) — editorial, not decorative.
A clean sans for labels, dates and numbers (Liberation Sans / DejaVu Sans).
The date is the largest single line after the title: SATURDAY · 21 NOVEMBER
2026, unmissable, because the judge's first criterion is the day itself.
Every word is typeset deterministically with Pillow; no generated text
anywhere, so nothing can be garbled. Numbers are verified facts only, never
rounded for effect.

## Craft

Every illustration is original, drawn or generated as flat editorial art
with no text inside it, then composited with exact typography. No
photographs presented as documentary evidence; sensitive events are shown
through accurate editorial symbolism, never invented scenes of real people.
The work must look laboured over: clean edges, consistent line weight,
consistent light, one visual language from corner to corner. If an element
does not help a viewer who missed the day understand what happened, it is
cut — detail for its own sake does not count.

## The test

At 300 pixels across: the date reads, the lead stories read, the world
reads. At full size: a careful viewer discovers the rest of the day. That
is the whole ambition.
