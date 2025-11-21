#!/usr/bin/env python3
from inky.auto import auto
from PIL import Image, ImageOps, ImageFilter

SCREENSHOT_PATH = "/home/pi/inky-weather/data/screenshot.png"

ASSUME_HIRES_INPUT = False

INKY_COLORS = [
    (255, 255, 255),  # 0: white
    (0,   0,   0),    # 1: black
    (255, 0,   0),    # 2: red
    (255, 255, 0),    # 3: yellow
    (0,   255, 0),    # 4: green
    (0,   0,   255),  # 5: blue
    (255, 128, 0),    # 6: orange
]

def build_inky_palette_image():
    """Build a small 'P' image with the Inky palette."""
    palette_img = Image.new("P", (1, 1))
    palette_data = []

    for r, g, b in INKY_COLORS:
        palette_data.extend([r, g, b])
    palette_data.extend([0] * (256 * 3 - len(palette_data)))
    palette_img.putpalette(palette_data)
    return palette_img

def main():
    inky = auto()
    inky.set_border(inky.BLACK)
    target_w, target_h = inky.resolution

    img = Image.open(SCREENSHOT_PATH)

    img = img.convert("RGB")

    if ASSUME_HIRES_INPUT or img.size != (target_w, target_h):
        img = ImageOps.fit(
            img,
            (target_w, target_h),
            method=Image.Resampling.LANCZOS
        )

    img = img.filter(ImageFilter.UnsharpMask(
        radius=1.0,
        percent=180,
        threshold=3
    ))

    palette_img = build_inky_palette_image()
    img = img.quantize(
        palette=palette_img,
        dither=Image.FLOYDSTEINBERG
    )

    img = img.resize((target_w, target_h), Image.Resampling.NEAREST)

    inky.set_image(img)
    inky.show()

if __name__ == "__main__":
    main()
