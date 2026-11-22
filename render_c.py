#!/usr/bin/env python3
"""Render Candidate C — 'One Day, One Arc' — for news-image-20261121.

The day as a 24-hour arc: five timed moments ride a semicircle (00:09 Peru
quake → 06:40 Sparta II → 13:30 Bitcoin → 18:24 BepiColombo → evening
Bahrain), then the other 32 stories as a digest, then the nine regions with
their counts. Same stories.json, palette and fonts as render.py.
Deterministic. Run: python3 render_c.py [out.png]
"""
import json
import math
import os
import sys

from PIL import Image, ImageDraw

from render import (HERE, W, H, PAPER, INK, INK_SOFT, VERM, MUTED,
                    CREAM_CHIP, REGION_COLOR, font, wrap, text_c, chip,
                    PICTO, F_SERIF_B, F_SANS_B, F_SANS, F_DSERIF_B)


def _bitcoin(d, b, teal=INK, red=VERM):
    x0, y0, x1, y1 = b
    cx, cy = (x0 + x1) // 2, (y0 + y1) // 2
    d.ellipse([cx - 20, cy - 20, cx + 20, cy + 20], outline=teal, width=3)
    d.text((cx, cy - 2), "B", font=font(F_DSERIF_B, 30), fill=teal,
           anchor="mm")
    d.line([(cx + 12, cy - 22), (cx + 18, cy - 30)], fill=red, width=3)


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
        HERE, "entry_c.png")
    with open(os.path.join(HERE, "stories.json"), encoding="utf-8") as f:
        data = json.load(f)
    meta, stories = data["meta"], data["stories"]
    # Candidate C shows one extra timed moment (Sparta II, a verified 21 Nov
    # event from the Ukraine arc) beyond the 37 catalogued stories.
    meta = dict(meta)
    meta["count_line"] = ("38 STORIES · 9 REGIONS — EVERY STORY "
                          "DATE-CHECKED TO 21 NOV 2026")
    by_id = {s["id"]: s for s in stories}

    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- header ---------------------------------------------------------
    text_c(d, 512, 8, meta["title"], font(F_SERIF_B, 46))
    text_c(d, 512, 58, meta["date"], font(F_SERIF_B, 26), fill=VERM)
    text_c(d, 512, 92, meta["count_line"], font(F_SANS_B, 13))
    d.line([(180, 112), (844, 112)], fill=INK, width=1)

    # ---- the arc ----------------------------------------------------------
    cx0, cy0, R = 512, 560, 400
    d.arc([cx0 - R, cy0 - R, cx0 + R, cy0 + R], 180, 360, fill=INK_SOFT,
          width=3)
    d.line([(cx0 - R - 30, cy0), (cx0 + R + 30, cy0)], fill=INK_SOFT,
           width=2)
    text_c(d, 512, 468, "FIVE MOMENTS · ONE DAY", font(F_SERIF_B, 16),
           fill=INK_SOFT)

    # (story id, angle deg, pictogram, chip centre, chip width)
    arc = [
        ("peru", 165, "peru", (140, 540), 180),
        ("sparta", 135, "bahrain", (235, 370), 180),
        ("bitcoin", 90, "bitcoin", (512, 250), 200),
        ("bepi", 45, "bepi", (789, 370), 180),
        ("bahrain", 15, "bahrain", (884, 540), 180),
    ]
    # Sparta II + Bitcoin are not tier-1/2 stories; build their cards here.
    extra = {
        "sparta": {"place": "GULF OF FINLAND", "headline": "SPARTA II ABLAZE",
                   "fact": "Drones hit a sanctioned Russian ship; 16 crew saved"},
        "bitcoin": {"place": "GLOBAL MARKETS", "headline": "BITCOIN BACK ABOVE $60,000",
                    "fact": "Fell to $55,252, a two-year low, then rebounded"},
    }
    picto = dict(PICTO)
    picto["bitcoin"] = _bitcoin
    picto["sparta"] = PICTO["bahrain"]
    times = {"peru": "00:09 UTC", "sparta": "06:40 UTC",
             "bitcoin": "13:30 UTC", "bepi": "18:24 UTC",
             "bahrain": "EVENING"}
    for sid, ang, _pk, (ccx, ccy), cw in arc:
        th = math.radians(ang)
        mx, my = int(cx0 + R * math.cos(th)), int(cy0 - R * math.sin(th))
        r = 44
        d.ellipse([mx - r, my - r, mx + r, my + r], fill=CREAM_CHIP,
                  outline=INK, width=3)
        picto[sid](d, (mx - r + 11, my - r + 11, mx + r - 11, my + r - 11))
        d.ellipse([mx - 5, my - 5, mx + 5, my + 5], fill=VERM)
        s = by_id.get(sid) or extra[sid]
        hl = wrap(d, s["headline"], font(F_SERIF_B, 15), cw - 16)[:2]
        lines = ([(times[sid], font(F_SANS_B, 11), VERM, 15)]
                 + [(s["place"], font(F_SANS_B, 10), INK, 14)]
                 + [(t, font(F_SERIF_B, 15), INK, 19) for t in hl])
        chip(d, ccx, ccy, cw, lines)

    # ---- briefs: the other 34 stories, 4 columns -------------------------
    d.line([(24, 596), (1000, 596)], fill=INK, width=1)
    text_c(d, 24, 602, "AROUND THE WORLD — 34 MORE STORIES",
           font(F_SANS_B, 12), anchor="la")
    rest = [s for s in stories if s["id"] not in ("peru", "bepi", "bahrain")]
    # peru/bepi/bahrain are on the arc; the digest lists the remaining 34
    # of the 37 catalogued stories (Sparta II rides the arc as a bonus).
    cols_x = [24, 272, 520, 768]
    for i, s in enumerate(rest):
        col, row = divmod(i, 9)
        x = cols_x[col]
        y = 626 + row * 26
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

    # ---- region counts ----------------------------------------------------
    d.line([(24, 868), (1000, 868)], fill=INK, width=1)
    text_c(d, 24, 874, "NINE REGIONS", font(F_SANS_B, 12), anchor="la")
    counts = {}
    for s in stories:
        counts[s["region"]] = counts.get(s["region"], 0) + 1
    counts["Europe"] = counts.get("Europe", 0) + 1  # Sparta II, on the arc
    order = ["Middle East & Gulf", "Europe", "Africa", "North America",
             "Latin America", "South Asia", "East & SE Asia",
             "Oceania & Pacific", "Space & Science"]
    short = {"Middle East & Gulf": "GULF", "Europe": "EUROPE",
             "Africa": "AFRICA", "North America": "N. AMERICA",
             "Latin America": "LATIN AM.", "South Asia": "S. ASIA",
             "East & SE Asia": "E. & SE ASIA", "Oceania & Pacific": "OCEANIA",
             "Space & Science": "SPACE"}
    x = 24
    for reg in order:
        n = counts.get(reg, 0)
        label = f"{short[reg]} ×{n}"
        fnt = font(F_SANS_B, 12)
        wpx = d.textlength(label, font=fnt) + 26
        d.rounded_rectangle([x, 898, x + wpx, 928], 6,
                            outline=REGION_COLOR[reg], width=2)
        d.ellipse([x + 8, 908, x + 16, 916], fill=REGION_COLOR[reg])
        d.text((x + 21, 903), label, font=fnt, fill=INK)
        x += wpx + 8

    text_c(d, 512, 950, "“The Gulf burns, the climate talks stall, a cartel king "
           "falls — and a spacecraft reaches Mercury.”",
           font(F_SERIF_B, 15), fill=INK_SOFT)
    text_c(d, 512, 1002, meta["sources_note"], font(F_SANS, 10), fill=MUTED)
    img.save(out, format="PNG")
    print(f"wrote {out} {img.size}")


if __name__ == "__main__":
    main()
