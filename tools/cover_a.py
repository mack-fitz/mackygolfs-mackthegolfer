#!/usr/bin/env python3
"""A cover in Mack's grid styles (covers/grid-reference.png).
usage: COVER_Y=<0.15-0.85> cover_a.py video.mp4 t_seconds out.jpg STYLE "text" [color]
       cover_a.py --guide video.mp4 t_seconds guide.jpg   (frame with % lines, to pick COVER_Y)
STYLE: pill (Macky vs. ___ box; color orange|red|yellow|purple|blue),
       type (lowercase typewriter note on white), none (plain frame).

TEXT NEVER GOES OVER HER CHEST (Mack, Oct 17: "You've been putting the text over my cleavage
a lot"). Her chest / cleavage / bra must stay visible on every cover. There is NO default
position: COVER_Y (the text block's center, as a fraction of the height) is required for any
cover with words. How to choose it, per frame:
  1. Run --guide on the exact frame and LOOK at it: find where her chest/bra/cleavage starts
     and ends (it moves from video to video, so never reuse a y from another cover).
  2. Put the words over the shirt-over-face / head area ABOVE the chest (usually 0.18-0.40), or
     BELOW the chest over the stomach/waist (usually 0.75-0.85), whichever is clear. The whole
     block must sit inside the grid crop (Instagram's profile grid shows the middle 1080x1440
     of a 1080x1920 cover = 0.125-0.875) and below Instagram's top bar, so COVER_Y must be
     0.15-0.85 and the block edges are checked against that.
  3. If no clear spot exists on that frame, pick a nearby frame of the wipe.
  4. View the finished cover at grid-thumbnail size (center 3:4 crop, ~360 px wide) AND full
     size before using it.
Other env: COVER_FS font scale (long text in tight spots), COVER_WRAP wrap width,
COVER_KEEPCASE keep case for type."""
import subprocess, sys, tempfile, textwrap, os
from PIL import Image, ImageDraw, ImageFont


def frame(video, t):
    tmp = tempfile.mktemp(suffix=".png")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", t, "-i", video, "-frames:v", "1", tmp], check=True)
    im = Image.open(tmp).convert("RGB")
    os.remove(tmp)
    return im


if sys.argv[1] == "--guide":
    video, t, out = sys.argv[2:5]
    im = frame(video, t)
    W, H = im.size
    d = ImageDraw.Draw(im)
    f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", int(W * 0.03))
    for p in range(5, 100, 5):
        y = int(H * p / 100)
        d.line([(0, y), (W, y)], fill="yellow", width=2)
        d.text((10, y - int(W * 0.035)), f"{p/100:.2f}", font=f, fill="yellow")
    for p in (0.125, 0.875):  # grid crop edges
        d.line([(0, int(H * p)), (W, int(H * p))], fill="cyan", width=6)
    im.save(out, quality=90)
    print(out, "yellow = COVER_Y fractions, cyan = grid crop edges")
    sys.exit(0)

video, t, out, style = sys.argv[1:5]
text = sys.argv[5] if len(sys.argv) > 5 else ""
color = sys.argv[6] if len(sys.argv) > 6 else "orange"
FS = float(os.environ.get("COVER_FS", "1"))
if style != "none":
    if "COVER_Y" not in os.environ:
        sys.exit("COVER_Y is required: run --guide on this frame, find her chest, and put the words "
                 "above it (shirt-over-face/head) or below it (stomach), never over it. See the docstring.")
    YF = float(os.environ["COVER_Y"])
    if not 0.15 <= YF <= 0.85:
        sys.exit("COVER_Y must be 0.15-0.85 (inside the 3:4 grid crop, below Instagram's top bar)")
COLORS = {"orange": "#F7931E", "red": "#E8101A", "yellow": "#F5C518", "purple": "#A21CAF", "blue": "#1E90FF"}
im = frame(video, t)
W, H = im.size
d = ImageDraw.Draw(im)
top = bot = None
if style == "pill":
    f = ImageFont.truetype("/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf", int(W * 0.075 * FS))
    lines = textwrap.wrap(text, int(os.environ.get("COVER_WRAP", "20")))
    lh = int(W * 0.095 * FS)
    y = int(H * YF) - lh * len(lines) // 2
    top = y - 8
    for ln in lines:
        bw = d.textlength(ln, font=f)
        x = (W - bw) / 2
        d.rounded_rectangle([x - 34, y - 8, x + bw + 34, y + lh - 4], radius=22, fill=COLORS[color])
        d.text((x, y - 4), ln, font=f, fill="white")
        y += lh
    bot = y - 4
elif style == "type":
    f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", int(W * 0.05 * FS))
    lines = textwrap.wrap(text if os.environ.get("COVER_KEEPCASE") else text.lower(), int(os.environ.get("COVER_WRAP", "22")))
    lh = int(W * 0.068 * FS)
    tw = max(d.textlength(l, font=f) for l in lines)
    x0 = (W - tw) / 2
    y0 = int(H * YF) - lh * len(lines) // 2
    top, bot = y0 - 26, y0 + lh * len(lines) + 18
    d.rectangle([x0 - 36, top, x0 + tw + 36, bot], fill="white")
    for i, l in enumerate(lines):
        d.text(((W - d.textlength(l, font=f)) / 2, y0 + i * lh), l, font=f, fill="black")
if top is not None and (top < H * 0.13 or bot > H * 0.87):
    sys.exit(f"text block {top/H:.2f}-{bot/H:.2f} leaves the grid crop / hits the top bar; move COVER_Y")
im.save(out, quality=95, subsampling=0)  # Mack, Oct 23: full-res JPEG q95
print(out, W, H, style, repr(text), "" if top is None else f"text block {top/H:.2f}-{bot/H:.2f} of height")
