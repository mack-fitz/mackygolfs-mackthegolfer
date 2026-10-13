#!/usr/bin/env python3
"""A cover in Mack's grid styles (covers/grid-reference.png).
usage: cover_a.py video.mp4 t_seconds out.jpg STYLE "text" [color]
STYLE: pill (Macky vs. ___ box; color orange|red|yellow|purple|blue),
       type (lowercase typewriter note on white), none (plain frame).
Text sits mid-frame (~55-62% down), inside the center square so the grid crop keeps it."""
import subprocess, sys, tempfile, textwrap
from PIL import Image, ImageDraw, ImageFont

video, t, out, style = sys.argv[1:5]
text = sys.argv[5] if len(sys.argv) > 5 else ""
color = sys.argv[6] if len(sys.argv) > 6 else "orange"
COLORS = {"orange": "#F7931E", "red": "#E8101A", "yellow": "#F5C518", "purple": "#A21CAF", "blue": "#1E90FF"}
tmp = tempfile.mktemp(suffix=".png")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", t, "-i", video, "-frames:v", "1", tmp], check=True)
im = Image.open(tmp).convert("RGB")
W, H = im.size
d = ImageDraw.Draw(im)
if style == "pill":
    f = ImageFont.truetype("/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf", int(W * 0.075))
    lines = textwrap.wrap(text, 20)
    lh = int(W * 0.095)
    y = int(H * 0.57) - lh * len(lines) // 2
    for ln in lines:
        bw = d.textlength(ln, font=f)
        x = (W - bw) / 2
        d.rounded_rectangle([x - 34, y - 8, x + bw + 34, y + lh - 4], radius=22, fill=COLORS[color])
        d.text((x, y - 4), ln, font=f, fill="white")
        y += lh
elif style == "type":
    f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", int(W * 0.05))
    lines = textwrap.wrap(text.lower(), 22)
    lh = int(W * 0.068)
    tw = max(d.textlength(l, font=f) for l in lines)
    x0 = (W - tw) / 2
    y0 = int(H * 0.58) - lh * len(lines) // 2
    d.rectangle([x0 - 36, y0 - 26, x0 + tw + 36, y0 + lh * len(lines) + 18], fill="white")
    for i, l in enumerate(lines):
        d.text(((W - d.textlength(l, font=f)) / 2, y0 + i * lh), l, font=f, fill="black")
im.save(out, quality=92)
print(out, W, H, style, repr(text))
