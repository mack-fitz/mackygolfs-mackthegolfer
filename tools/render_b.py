#!/usr/bin/env python3
"""B re-edit renderer: thin wrapper around tools/render.sh (single crf 17 / preset slow encode,
source resolution + fps, AAC 192k 48 kHz, no burned-in text).
usage: render_b.py src segs.json out.mp4"""
import os, subprocess, sys
src, segs, out = sys.argv[1:4]
subprocess.run([os.path.join(os.path.dirname(os.path.abspath(__file__)), "render.sh"), src, segs, "", "", out], check=True)
