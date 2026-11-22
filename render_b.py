#!/usr/bin/env python3
"""Render Candidate B — 'The Strait Burns' — for news-image-20261121.

One dominant generated scene (burning tanker, Strait of Hormuz) + the four
other leads as pictogram columns + all 32 remaining stories as a digest.
Same stories.json, same palette/fonts as render.py. Deterministic.
Run: python3 render_b.py [out.png]
"""
import json
import os
import sys

import numpy as np
from PIL import Image, ImageDraw

from render import (HERE, W, H, PAPER, INK, INK_SOFT, VERM, MUTED,
                    CREAM_CHIP, REGION_COLOR, font, wrap, text_c, chip,
                    PICTO, F_SERIF_B, F_SERIF, F_SANS_B, F_SANS)

GULF_ART = os.path.join(
    HERE, "illustrations",
    "media-generation-gulf-scene-0-5e15f1f3-67e9-4887-8cc4-53233ed80707.png")


def clean_gulf():
    """Crop the generator's paper border, resize to the hero band."""
    im = Image.open(GULF_ART).convert("RGB")
    a = np.array(im).astype(int)
    paper = np.array([246, 234, 215])
    mask = (np.abs(a - paper).sum(axis=2) > 45)
    ys, xs = np.where(mask)
    im = im.crop((int(xs.min()), int(ys.min()), int(xs.max()) + 1,
                  int(ys.max()) + 1))
    return im.resize((1024, 442), Image.LANCZOS)


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
        HERE, "entry_b.png")
    with open(os.path.join(HERE, "stories.json"), encoding="utf-8") as f:
        data = json.load(f)
    meta, stories = data["meta"], data["stories"]
    by_id = {s["id"]: s for s in stories}

    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    img.paste(clean_gulf(), (0, 118))

    # ---- header ---------------------------------------------------------
    text_c(d, 512, 8, meta["title"], font(F_SERIF_B, 46))
    text_c(d, 512, 58, meta["date"], font(F_SERIF_B, 26), fill=VERM)
    text_c(d, 512, 92, meta["count_line"], font(F_SANS_B, 13))
    d.line([(180, 112), (844, 112)], fill=INK, width=1)

    # ---- hero caption chip (lead story, over the dark sea) --------------
    s = by_id["bahrain"]
    lines = ([(s["place"], font(F_SANS_B, 11), VERM, 15)]
             + [(t, font(F_SERIF_B, 20), INK, 24)
                for t in wrap(d, s["headline"], font(F_SERIF_B, 20), 380)]
             + [(t, font(F_SANS, 12), MUTED, 15)
                for t in wrap(d, s["fact"], font(F_SANS, 12), 380)][:2])
    # chip() centres text; draw it manually left-aligned instead
    w, x0, y0 = 420, 24, 452
    total = sum(fnt.size + 4 for _, fnt, _, _ in lines) + 16
    d.rounded_rectangle([x0, y0, x0 + w, y0 + total], 6,
                        fill=CREAM_CHIP, outline=INK, width=1)
    y = y0 + 9
    for (txt, fnt, fill, _l) in lines:
        d.text((x0 + 14, y), txt, font=fnt, fill=fill, anchor="la")
        y += fnt.size + 4

    # ---- four other leads ------------------------------------------------
    for i, sid in enumerate(["cop31", "kryvyi", "chapo", "bepi"]):
        s = by_id[sid]
        cx = 128 + 256 * i
        my = 598
        r = 36
        d.ellipse([cx - r, my - r, cx + r, my + r], fill=CREAM_CHIP,
                  outline=INK, width=3)
        PICTO[sid](d, (cx - r + 10, my - r + 10, cx + r - 10, my + r - 10))
        y = my + r + 6
        text_c(d, cx, y, s["place"], font(F_SANS_B, 10), fill=VERM)
        y += 15
        for t in wrap(d, s["headline"], font(F_SERIF_B, 15), 236)[:2]:
            text_c(d, cx, y, t, font(F_SERIF_B, 15))
            y += 19
        for t in wrap(d, s["fact"], font(F_SANS, 11), 236)[:2]:
            text_c(d, cx, y, t, font(F_SANS, 11), fill=MUTED)
            y += 14

    # ---- briefs: the other 32 stories, 4 columns -------------------------
    d.line([(24, 728), (1000, 728)], fill=INK, width=1)
    text_c(d, 24, 734, "THE REST OF THE DAY — 32 MORE STORIES",
           font(F_SANS_B, 12), anchor="la")
    rest = [s for s in stories if s["tier"] in (2, 3)]
    cols_x = [24, 272, 520, 768]
    for i, s in enumerate(rest):
        col, row = divmod(i, 8)
        x = cols_x[col]
        y = 758 + row * 28
        rc = REGION_COLOR[s["region"]]
        d.ellipse([x, y + 4, x + 8, y + 12], fill=rc)
        txt = f"{s['place']} — {s['headline']}"
        f12 = font(F_SANS, 12)
        lines = wrap(d, txt, f12, 219)
        if len(lines) > 2:
            f12 = font(F_SANS, 11)
            lines = wrap(d, txt, f12, 219)
        if len(lines) > 2:
            lines = lines[:2]
            lines[1] = lines[1][:38].rsplit(" ", 1)[0] + "…"
        d.text((x + 13, y), lines[0], font=f12, fill=INK)
        if len(lines) > 1:
            d.text((x + 13, y + 13), lines[1], font=f12, fill=INK)

    text_c(d, 512, 1002, meta["sources_note"], font(F_SANS, 10), fill=MUTED)
    img.save(out, format="PNG")
    print(f"wrote {out} {img.size}")


if __name__ == "__main__":
    main()
