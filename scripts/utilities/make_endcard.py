#!/usr/bin/env python3
"""Build the social CTA end card for the Baby Batter shorts.

All lettering is drawn with Pillow (DejaVu Sans Bold) at exactly 1080x1920 --
no AI-generated text, per project guardrails. Font sizes auto-fit the frame.

Usage: python scripts/utilities/make_endcard.py
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "project-files/graphics/ENDCARD_social_v001.png"

W, H = 1080, 1920
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

CREAM = (240, 226, 199)
GOLD = (233, 205, 160)
TAN = (205, 172, 130)
DIM = (170, 140, 105)
DARK = (150, 122, 92)
RED = (178, 32, 34)
RIM = (230, 200, 160)


def fit_font(draw: ImageDraw.ImageDraw, text: str, max_w: float, start: int) -> ImageFont.FreeTypeFont:
    size = start
    while size > 20:
        font = ImageFont.truetype(FONT, size)
        bbox = draw.textbbox((0, 0), text, font=font)
        if bbox[2] - bbox[0] <= max_w:
            return font
        size -= 4
    return ImageFont.truetype(FONT, 20)


def center(draw: ImageDraw.ImageDraw, text: str, font, y: int, fill) -> None:
    bbox = draw.textbbox((0, 0), text, font=font)
    w = bbox[2] - bbox[0]
    draw.text(((W - w) / 2, y), text, font=font, fill=fill)


def main() -> None:
    img = Image.new("RGB", (W, H), (58, 37, 24))
    d = ImageDraw.Draw(img)

    # warm vertical gradient
    for y in range(H):
        t = y / H
        r = int(58 + (24 - 58) * t)
        g = int(37 + (22 - 37) * t)
        b = int(24 + (18 - 24) * t)
        d.line([(0, y), (W, y)], fill=(r, g, b))

    # subtle gingham grid
    grid = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(grid)
    for x in range(0, W, 60):
        gd.line([(x, 0), (x, H)], fill=(150, 55, 40, 55), width=2)
    for y in range(0, H, 60):
        gd.line([(0, y), (W, y)], fill=(150, 55, 40, 55), width=2)
    img = Image.alpha_composite(img.convert("RGBA"), grid).convert("RGB")
    d = ImageDraw.Draw(img)

    margin = 70
    max_w = W - 2 * margin

    font_wordmark = fit_font(d, "BABY BATTER", max_w - 40, 96)
    font_sub = fit_font(d, "FOR BREAKFAST", max_w - 120, 46)
    font_cta = fit_font(d, "COME SEE MORE", max_w - 160, 72)
    font_handle = fit_font(d, "@plaguedr.online", max_w - 140, 110)
    font_line = fit_font(d, "FULL MUSIC VIDEO · NEW DROPS · WAFFLES", max_w, 44)

    # wordmark
    center(d, "BABY BATTER", font_wordmark, 170, GOLD)
    center(d, "FOR BREAKFAST", font_sub, 310, TAN)

    # rule
    d.line([(W / 2 - 260, 740), (W / 2 + 260, 740)], fill=(210, 170, 120), width=4)

    # CTA
    center(d, "COME SEE", font_cta, 820, CREAM)
    center(d, "MORE", font_cta, 930, CREAM)

    # handle plate
    handle = "@plaguedr.online"
    bbox = d.textbbox((0, 0), handle, font=font_handle)
    tw = bbox[2] - bbox[0]
    pad_x, pad_y = 50, 34
    x0 = (W - tw) / 2 - pad_x
    y0 = 1110
    x1 = (W + tw) / 2 + pad_x
    y1 = y0 + (bbox[3] - bbox[1]) + pad_y * 2
    d.rounded_rectangle([x0, y0, x1, y1], radius=26, fill=RED, outline=RIM, width=5)
    d.text(((W - tw) / 2, y0 + pad_y - bbox[1]), handle, font=font_handle, fill=(255, 244, 220))

    # footer
    center(d, "FULL MUSIC VIDEO · NEW DROPS · WAFFLES", font_line, 1520, TAN)
    center(d, "no syrup required", fit_font(d, "no syrup required", max_w - 200, 40), 1600, DIM)
    center(d, "waffles, biscuits or pie", fit_font(d, "waffles, biscuits or pie", max_w - 200, 40), 1680, DARK)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT)
    print(f"saved {OUT} ({img.size[0]}x{img.size[1]})")


if __name__ == "__main__":
    main()
