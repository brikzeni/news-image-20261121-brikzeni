#!/usr/bin/env python3
"""Render Candidate A — 'Luminous Atlas' — for news-image-20261121 (@brikzeni).

Deterministic Pillow compositor: generated base world-map art (no text inside
it) + coded flat pictograms + ALL typography typeset here, so every word is
sharp and factually exact. No network, no clock, no randomness:
same stories.json + same base art = same bytes.

Run:  python3 render.py            -> writes entry.png (1024x1024)
       python3 render.py out2.png  -> writes out2.png (for determinism check)
"""
import json
import os
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
W, H = 1024, 1024
PAPER = (246, 234, 215)
INK = (20, 66, 74)          # deep ink-teal
INK_SOFT = (62, 107, 122)
VERM = (200, 67, 43)        # vermilion accent
OCHRE = (176, 122, 42)
MUTED = (110, 100, 82)
CREAM_CHIP = (250, 242, 226)

F_SERIF_B = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
F_SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
F_SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
F_SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
F_SANS_I = "/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf"
F_DSERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"

REGION_COLOR = {
    "Middle East & Gulf": (200, 67, 43),
    "Europe": (20, 66, 74),
    "Africa": (176, 122, 42),
    "North America": (62, 107, 122),
    "Latin America": (74, 122, 62),
    "South Asia": (122, 74, 107),
    "East & SE Asia": (138, 109, 27),
    "Oceania & Pacific": (46, 74, 122),
    "Space & Science": (34, 34, 34),
}


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap to max_w pixels; returns list of lines."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w or not cur:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_c(draw, cx, y, s, fnt, fill=INK, anchor="ma"):
    draw.text((cx, y), s, font=fnt, fill=fill, anchor=anchor)


def lonlat_to_art(lon, lat):
    """Approx equirectangular fit to the generated base art (1920x1280)."""
    x = 875 + 5.3 * lon
    if lat >= 0:
        y = 360 + (51.5 - lat) * 7.86
    else:
        y = 765 + (-lat) * 5.0
    return x, y


def art_to_canvas(ax, ay):
    """Base art is cropped (0,100,1920,1160) and resized to (1024,554),
    pasted at y=118."""
    return ax * (1024 / 1920), 118 + (ay - 100) * (554 / 1060)


# ---------------------------------------------------------------- pictograms
# Each draws a flat icon inside a square box (x0,y0,x1,y1) in teal + vermilion.

def _ship(d, b, teal=INK, red=VERM):
    x0, y0, x1, y1 = b
    cx = (x0 + x1) // 2
    d.polygon([(x0 + 6, y1 - 22), (x1 - 6, y1 - 22), (x1 - 14, y1 - 8),
               (x0 + 14, y1 - 8)], fill=teal)
    d.rectangle([cx - 16, y0 + 16, cx + 16, y1 - 22], fill=teal)
    d.rectangle([cx - 8, y0 + 8, cx + 8, y0 + 16], fill=teal)
    d.polygon([(x1 - 26, y0 + 2), (x1 - 18, y0 + 12), (x1 - 12, y0 + 12),
               (x1 - 20, y0 + 2)], fill=red)  # flame
    for i, wx in enumerate((x0 + 8, cx - 2, cx + 14)):
        d.arc([wx, y1 - 6, wx + 22, y1 + 6], 0, 180, fill=INK_SOFT, width=2)


def _globe_thermo(d, b, teal=INK, red=VERM):
    x0, y0, x1, y1 = b
    cx, cy = (x0 + x1) // 2 - 8, (y0 + y1) // 2 + 2
    r = 20
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=teal, width=3)
    d.arc([cx - r, cy - r, cx + r, cy + r], 200, 340, fill=teal, width=2)
    d.line([(cx, cy - r), (cx, cy + r)], fill=teal, width=2)
    d.line([(cx - r, cy), (cx + r, cy)], fill=teal, width=2)
    # thermometer
    tx = x1 - 14
    d.rounded_rectangle([tx - 4, y0 + 8, tx + 4, y1 - 14], 4,
                        outline=teal, width=3)
    d.ellipse([tx - 7, y1 - 20, tx + 7, y1 - 6], fill=red)
    d.rectangle([tx - 2, y0 + 18, tx + 2, y1 - 14], fill=red)


def _building_crack(d, b, teal=INK, red=VERM):
    x0, y0, x1, y1 = b
    d.rectangle([x0 + 10, y0 + 14, x1 - 10, y1 - 8], outline=teal, width=3)
    for wx in (x0 + 18, (x0 + x1) // 2, x1 - 26):
        for wy in (y0 + 22, y0 + 36):
            d.rectangle([wx, wy, wx + 8, wy + 8], fill=teal)
    d.line([(x0 + 26, y0 + 14), (x0 + 20, y0 + 30), (x0 + 30, y0 + 44),
            (x0 + 22, y1 - 8)], fill=red, width=3)
    d.line([(x1 - 14, y0 + 6), (x1 - 20, y0 + 16)], fill=red, width=3)


def _handcuffs(d, b, teal=INK, red=VERM):
    x0, y0, x1, y1 = b
    cy = (y0 + y1) // 2
    d.ellipse([x0 + 4, cy - 13, x0 + 30, cy + 13], outline=teal, width=4)
    d.ellipse([x1 - 30, cy - 13, x1 - 4, cy + 13], outline=teal, width=4)
    d.line([(x0 + 30, cy), (x1 - 30, cy)], fill=teal, width=3)
    d.line([(x0 + 12, cy - 13), (x0 + 22, cy - 20)], fill=red, width=3)
    d.line([(x1 - 22, cy - 13), (x1 - 12, cy - 20)], fill=red, width=3)


def _spacecraft(d, b, teal=INK, red=VERM):
    x0, y0, x1, y1 = b
    cx, cy = (x0 + x1) // 2, (y0 + y1) // 2
    d.arc([x0 + 2, y0 + 2, x1 - 2, y1 - 2], 200, 340, fill=INK_SOFT, width=2)
    d.rectangle([cx - 18, cy - 8, cx - 2, cy + 8], fill=teal)
    d.rectangle([cx + 2, cy - 8, cx + 18, cy + 8], fill=teal)
    d.rectangle([cx - 5, cy - 5, cx + 5, cy + 5], fill=red)
    d.ellipse([x1 - 22, y0 + 4, x1 - 6, y0 + 20], fill=VERM)
    d.ellipse([x1 - 20, y0 + 6, x1 - 8, y0 + 18], fill=(230, 150, 110))


def _zeta(d, b, teal=INK, red=VERM):
    x0, y0, x1, y1 = b
    f = font(F_DSERIF_B, 34)
    d.text(((x0 + x1) // 2 - 12, (y0 + y1) // 2 - 8), "ζ", font=f, fill=teal,
           anchor="mm")
    d.line([(x1 - 22, y1 - 16), (x1 - 14, y1 - 8), (x1 - 4, y1 - 20)],
           fill=red, width=4)


def _chart_down(d, b, teal=INK, red=VERM):
    x0, y0, x1, y1 = b
    d.line([(x0 + 8, y1 - 10), (x0 + 8, y0 + 8)], fill=teal, width=3)
    d.line([(x0 + 8, y1 - 10), (x1 - 6, y1 - 10)], fill=teal, width=3)
    pts = [(x0 + 12, y0 + 14), (x0 + 26, y0 + 22), (x0 + 36, y0 + 18),
           (x0 + 48, y0 + 32), (x0 + 60, y1 - 18)]
    d.line(pts, fill=red, width=4, joint="curve")
    d.polygon([(x0 + 60, y1 - 18), (x0 + 50, y1 - 20), (x0 + 58, y1 - 8)],
              fill=red)


def _factory_fire(d, b, teal=INK, red=VERM):
    x0, y0, x1, y1 = b
    d.rectangle([x0 + 8, y0 + 26, x1 - 8, y1 - 8], outline=teal, width=3)
    d.polygon([(x0 + 8, y0 + 26), (x0 + 18, y0 + 16), (x0 + 28, y0 + 26),
               (x0 + 38, y0 + 16), (x0 + 48, y0 + 26)], fill=teal)
    d.rectangle([x1 - 18, y0 + 6, x1 - 10, y0 + 26], fill=teal)
    d.polygon([(x1 - 16, y0 - 2), (x1 - 8, y0 + 8), (x1 - 20, y0 + 10)],
              fill=red)


def _shield(d, b, teal=INK, red=VERM):
    x0, y0, x1, y1 = b
    cx = (x0 + x1) // 2
    d.arc([x0 + 6, y0 + 22, x1 - 6, y1 - 2], 180, 360, fill=teal, width=3)
    for dx, dy in ((-16, 2), (0, -2), (16, 4)):
        d.ellipse([cx + dx - 3, y0 + dy + 2, cx + dx + 3, y0 + dy + 8],
                  fill=red)
    d.line([(cx - 16, y0 + 12), (cx - 6, y0 + 26)], fill=red, width=2)
    d.line([(cx, y0 + 8), (cx, y0 + 26)], fill=red, width=2)
    d.line([(cx + 16, y0 + 12), (cx + 6, y0 + 26)], fill=red, width=2)


def _seismo(d, b, teal=INK, red=VERM):
    x0, y0, x1, y1 = b
    cy = (y0 + y1) // 2
    pts = [(x0 + 4, cy), (x0 + 16, cy), (x0 + 22, cy - 14), (x0 + 28, cy + 12),
           (x0 + 34, cy - 20), (x0 + 40, cy + 16), (x0 + 46, cy),
           (x1 - 4, cy)]
    d.line(pts, fill=red, width=3, joint="curve")
    d.line([(x0 + 4, y1 - 8), (x0 + 20, y1 - 14), (x0 + 34, y1 - 8),
            (x1 - 4, y1 - 12)], fill=teal, width=3)


def _cargo(d, b, teal=INK, red=VERM):
    x0, y0, x1, y1 = b
    cx = (x0 + x1) // 2
    d.polygon([(x0 + 6, y1 - 20), (x1 - 6, y1 - 20), (x1 - 14, y1 - 6),
               (x0 + 14, y1 - 6)], fill=teal)
    d.rectangle([cx - 18, y0 + 14, cx - 2, y0 + 26], fill=red)
    d.rectangle([cx + 2, y0 + 14, cx + 18, y0 + 26], fill=teal)
    d.rectangle([cx - 10, y0 + 28, cx + 10, y0 + 38], fill=INK_SOFT)
    for wx in (x0 + 8, cx - 2, cx + 14):
        d.arc([wx, y1 - 4, wx + 22, y1 + 8], 0, 180, fill=INK_SOFT, width=2)


def _capsized(d, b, teal=INK, red=VERM):
    x0, y0, x1, y1 = b
    cx, cy = (x0 + x1) // 2, (y0 + y1) // 2
    d.arc([x0 + 6, cy - 14, x1 - 6, cy + 14], 180, 360, fill=teal, width=4)
    d.line([(x0 + 14, cy - 6), (x1 - 14, cy - 6)], fill=teal, width=3)
    for wx in (x0 + 8, cx - 2, cx + 14):
        d.arc([wx, y1 - 12, wx + 22, y1], 0, 180, fill=INK_SOFT, width=2)
    d.ellipse([cx - 4, y0 + 8, cx + 4, y0 + 16], fill=red)


def _truck(d, b, teal=INK, red=VERM):
    x0, y0, x1, y1 = b
    d.rectangle([x0 + 8, y0 + 16, x1 - 18, y1 - 16], outline=teal, width=3)
    d.rectangle([x1 - 18, y0 + 24, x1 - 6, y1 - 16], fill=teal)
    d.ellipse([x0 + 16, y1 - 16, x0 + 28, y1 - 4], fill=teal)
    d.ellipse([x1 - 26, y1 - 16, x1 - 14, y1 - 4], fill=teal)
    d.line([(x0 + 20, y0 + 22), (x0 + 26, y0 + 30), (x0 + 32, y0 + 22)],
           fill=red, width=2)


def _placard(d, b, teal=INK, red=VERM):
    x0, y0, x1, y1 = b
    cx = (x0 + x1) // 2
    d.rectangle([x0 + 10, y0 + 8, x1 - 10, y0 + 34], outline=teal, width=3)
    d.line([(cx, y0 + 8), (cx - 8, y0 + 18), (cx + 8, y0 + 28)], fill=red,
           width=3)
    d.line([(cx, y0 + 34), (cx, y1 - 6)], fill=teal, width=3)
    for dx in (-18, -6, 6, 18):
        d.ellipse([cx + dx - 3, y1 - 12, cx + dx + 3, y1 - 6], fill=teal)


PICTO = {
    "bahrain": _ship, "cop31": _globe_thermo, "kryvyi": _building_crack,
    "chapo": _handcuffs, "bepi": _spacecraft, "riemann": _zeta,
    "markets": _chart_down, "indonesia": _factory_fire, "riyadh": _shield,
    "peru": _seismo, "eu-indo": _cargo, "nigeria": _capsized,
    "gaza": _truck, "france": _placard,
}

# --- layout overrides (canvas coords; map band y=118..672) -----------------
MED_OVERRIDE = {
    "bepi": (730, 175), "eu-indo": (400, 180), "france": (335, 285),
    "peru": (230, 580), "riyadh": (700, 470), "bahrain": (712, 330),
    "kryvyi": (580, 235), "markets": (310, 410), "riemann": (165, 230),
}
# tier-1 chips: (cx, cy, width)
CHIP1 = {
    "bahrain": (712, 414, 210), "cop31": (320, 345, 190),
    "kryvyi": (520, 155, 200), "chapo": (150, 510, 200),
    "bepi": (730, 250, 200),
}
# tier-2 one-line labels: (cx, cy, width)
LABEL2 = {
    "riemann": (165, 180, 150), "markets": (310, 456, 150),
    "indonesia": (820, 566, 150), "riyadh": (700, 516, 150),
    "peru": (230, 626, 150), "eu-indo": (400, 228, 180),
    "nigeria": (420, 526, 150), "gaza": (540, 466, 150),
    "france": (230, 285, 150),
}

BASE_ART = os.path.join(
    HERE, "illustrations",
    "media-generation-world-atlas-base-0-f15917d0-ab2c-4df2-8f38-2e71c8c22bd9.png")


def clean_base():
    """Load base art, erase the generator's random vermilion dots, crop and
    resize to the map band. Deterministic."""
    im = Image.open(BASE_ART).convert("RGB")
    a = np.array(im).astype(int)
    red = (a[:, :, 0] > 150) & (a[:, :, 1] < 120) & (a[:, :, 2] < 100) \
        & ((a[:, :, 0] - a[:, :, 1]) > 60)
    a[red] = [246, 234, 215]
    im = Image.fromarray(a.astype("uint8"), "RGB")
    return im.crop((0, 100, 1920, 1160)).resize((1024, 554), Image.LANCZOS)


def chip(draw, cx, cy, w, lines):
    """Cream chip with centred lines [(text, font, fill, leading)]."""
    heights = [fnt.size + 4 for _, fnt, _, _ in lines]
    # recompute per wrapped line below; caller passes already-wrapped lines
    total = sum(h for _, h in zip(lines, heights)) + 14
    y0 = cy - total // 2
    draw.rounded_rectangle([cx - w // 2, y0, cx + w // 2, y0 + total],
                           6, fill=CREAM_CHIP, outline=INK, width=1)
    y = y0 + 8
    for (txt, fnt, fill, _lead) in lines:
        draw.text((cx, y), txt, font=fnt, fill=fill, anchor="ma")
        y += fnt.size + 4
    return y0 + total


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "entry.png")
    with open(os.path.join(HERE, "stories.json"), encoding="utf-8") as f:
        data = json.load(f)
    meta = data["meta"]
    stories = data["stories"]
    by_id = {s["id"]: s for s in stories}

    img = Image.new("RGB", (W, H), PAPER)
    img.paste(clean_base(), (0, 118))
    d = ImageDraw.Draw(img)

    # ---- header ---------------------------------------------------------
    text_c(d, 512, 8, meta["title"], font(F_SERIF_B, 46))
    text_c(d, 512, 58, meta["date"], font(F_SERIF_B, 26), fill=VERM)
    text_c(d, 512, 92, meta["count_line"], font(F_SANS_B, 13))
    d.line([(180, 112), (844, 112)], fill=INK, width=1)

    # ---- map: dots, leaders, medallions, chips -------------------------
    for s in stories:
        if s["tier"] not in (1, 2):
            continue
        mx, my = MED_OVERRIDE.get(s["id"], tuple(s["med"]))
        r = 46 if s["tier"] == 1 else 30
        ax, ay = lonlat_to_art(s["lon"], s["lat"])
        dx, dy = art_to_canvas(ax, ay)
        # leader line (from medallion edge toward dot)
        d.line([(mx, my), (dx, dy)], fill=INK_SOFT, width=2)
        # geo dot
        d.ellipse([dx - 6, dy - 6, dx + 6, dy + 6], fill=VERM,
                  outline=(255, 255, 255), width=2)
        # medallion
        d.ellipse([mx - r, my - r, mx + r, my + r], fill=CREAM_CHIP,
                  outline=INK, width=3)
        pad = 12 if s["tier"] == 1 else 8
        PICTO[s["id"]](d, (mx - r + pad, my - r + pad, mx + r - pad,
                           my + r - pad))

    # tier-1 chips (place + headline + fact)
    for sid, (cx, cy, w) in CHIP1.items():
        s = by_id[sid]
        hl = wrap(d, s["headline"], font(F_SERIF_B, 16), w - 16)[:2]
        fc = wrap(d, s["fact"], font(F_SANS, 11), w - 16)[:2]
        lines = ([(s["place"], font(F_SANS_B, 10), VERM, 14)]
                 + [(t, font(F_SERIF_B, 16), INK, 20) for t in hl]
                 + [(t, font(F_SANS, 11), MUTED, 14) for t in fc])
        chip(d, cx, cy, w, lines)

    # tier-2 labels (place + headline, inline)
    for sid, (cx, cy, w) in LABEL2.items():
        s = by_id[sid]
        hl = wrap(d, f"{s['place']} — {s['headline']}",
                  font(F_SANS_B, 11), w - 8)[:2]
        lines = [(t, font(F_SANS_B, 11), INK, 14) for t in hl]
        chip(d, cx, cy, w, lines)

    # ---- briefs band ----------------------------------------------------
    d.line([(24, 684), (1000, 684)], fill=INK, width=1)
    text_c(d, 24, 690, "THE REST OF THE DAY — 23 MORE STORIES",
           font(F_SANS_B, 12), anchor="la")
    t3 = [s for s in stories if s["tier"] == 3]
    cols_x = [24, 352, 680]
    for i, s in enumerate(t3):
        col, row = divmod(i, 8)
        x = cols_x[col]
        y = 712 + row * 27
        rc = REGION_COLOR[s["region"]]
        d.ellipse([x, y + 4, x + 8, y + 12], fill=rc)
        txt = f"{s['place']} — {s['headline']}. {s['fact']}"
        f12 = font(F_SANS, 12)
        lines = wrap(d, txt, f12, 312)
        if len(lines) > 2:
            f12 = font(F_SANS, 11)
            lines = wrap(d, txt, f12, 312)
        if len(lines) > 2:
            lines = lines[:2]
            lines[1] = lines[1][:54].rsplit(" ", 1)[0] + "…"
        # bold the place prefix on the first line
        d.text((x + 13, y), lines[0], font=f12, fill=INK)
        if len(lines) > 1:
            d.text((x + 13, y + 13), lines[1], font=f12, fill=INK)

    # ---- footer: UTC timeline + sources ---------------------------------
    d.line([(24, 928), (1000, 928)], fill=INK, width=1)
    tl = data["timeline"]
    tl_x = [130, 320, 520, 700, 880]
    d.line([(60, 956), (964, 956)], fill=INK_SOFT, width=2)
    for (ev, ex) in zip(tl, tl_x):
        d.ellipse([ex - 5, 951, ex + 5, 961], fill=VERM)
        text_c(d, ex, 930, ev["t"], font(F_SANS_B, 11))
        lab = wrap(d, ev["label"], font(F_SANS, 10), 150)
        ly = 966
        for ln in lab[:2]:
            text_c(d, ex, ly, ln, font(F_SANS, 10), fill=MUTED)
            ly += 12
    text_c(d, 512, 1002, meta["sources_note"], font(F_SANS, 10), fill=MUTED)

    img.save(out, format="PNG")
    print(f"wrote {out} {img.size}")


if __name__ == "__main__":
    main()
