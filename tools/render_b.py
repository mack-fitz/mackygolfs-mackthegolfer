#!/usr/bin/env python3
"""B re-edit renderer (single encode, no burned-in text).
usage: render_b.py src segs.json out.mp4 [crf]
segs: [[start, end, zoom], ...]  zoom 1 = ~15% center punch-in.
Keeps the source resolution, libx264 crf 18 (default), maxrate 9M so files stay under GitHub's 100 MB limit, AAC 192k 48 kHz.
3 ms-ish audio fades only where the cut jumps in time (no clicks)."""
import json, subprocess, sys

src, segs_path, out = sys.argv[1:4]
crf = sys.argv[4] if len(sys.argv) > 4 else "18"
segs = json.load(open(segs_path))
w, h = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                       "stream=width,height", "-of", "csv=p=0", src],
                      capture_output=True, text=True).stdout.strip().split(",")[:2]
w, h = int(w), int(h)
import os, tempfile
tmp = tempfile.mkdtemp()
lst = open(os.path.join(tmp, "list.txt"), "w")
for i, (a, b, z) in enumerate(segs):
    jin = i > 0 and abs(segs[i - 1][1] - a) > 0.01
    jout = i < len(segs) - 1 and abs(segs[i + 1][0] - b) > 0.01
    d = b - a
    vf = (f"crop=iw/1.15:ih/1.15,scale={w}:{h}:flags=lanczos," if z else "") + "setsar=1,fps=30"
    af = ["anull"]
    if jin:
        af.append("afade=t=in:d=0.03")
    if jout:
        af.append(f"afade=t=out:st={max(0, d - 0.03):.3f}:d=0.03")
    seg = os.path.join(tmp, f"s{i}.mkv")
    # lossless intermediate (crf 0) so the final export is the only lossy encode
    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-ss", str(a), "-i", src, "-t", f"{d:.3f}",
                    "-vf", vf, "-af", ",".join(af), "-c:v", "libx264", "-preset", "ultrafast", "-crf", "0",
                    "-pix_fmt", "yuv420p", "-c:a", "pcm_s16le", "-ar", "48000", seg], check=True)
    lst.write(f"file '{seg}'\n")
lst.close()
cmd = ["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst.name,
       "-c:v", "libx264", "-preset", "slow", "-crf", crf, "-profile:v", "high", "-pix_fmt", "yuv420p",
       "-maxrate", "9M", "-bufsize", "18M", "-g", "60", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart", out]
subprocess.run(cmd, check=True)
subprocess.run(["rm", "-rf", tmp])
print(out, round(sum(b - a for a, b, _ in segs), 2))
