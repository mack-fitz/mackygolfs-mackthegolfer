#!/usr/bin/env python3
"""Shorty renderer (Oct 20): ONE continuous clip from the TRUE original + the on-reel line, ONE encode.
usage: python3 tools/render_shorty.py src a b overlay.png fade_out_at out.mp4
  src: file name in tools/src/ (true original, rejoined/sha-checked)
  a,b: clip window (s) inside one of her own clips (no cuts inside; trim at quiet gaps)
  overlay.png: 1080x1920 RGBA from tools/ontext.py (Oct 17 ON-REEL TEXT spec)
  fade_out_at: output time (s) where the line starts a 0.3 s fade-out (keep it off her face/head); 0 = stays
Her own sound: only 30/40 ms edge fades + one linear 2-pass loudnorm to -14 LUFS / TP -1.5 (so every shorty plays at the same level and nothing clips; no compression); 1080x1920 30 fps libx264 crf 17 slow, AAC 192k 48 kHz, +faststart."""
import subprocess, sys, os
S = os.path.dirname(os.path.abspath(__file__)) + '/src/'
src, a, b, ovl, fo, out = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), sys.argv[4], float(sys.argv[5]), sys.argv[6]
d = b - a
import json, re
def _ln(extra):
    return (f"[0:a]asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo,afade=t=in:d=0.03,afade=t=out:st={d-0.04:.3f}:d=0.04,"
            f"loudnorm=I=-14:TP=-1.5:LRA=11{extra}")
r = subprocess.run(['ffmpeg', '-nostdin', '-hide_banner', '-ss', f'{a:.3f}', '-t', f'{d:.3f}', '-i', S + src, '-filter_complex', _ln(':print_format=json') + '[o]',
                    '-map', '[o]', '-f', 'null', '-'], capture_output=True, text=True).stderr
m = json.loads(r[r.rfind('{'):r.rfind('}') + 1])
LN = _ln(f":measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true") + ",aresample=48000[ca]"
of = f",fade=t=out:st={fo:.3f}:d=0.3:alpha=1" if fo > 0 else ""
fg = (f"[0:v]setpts=PTS-STARTPTS,scale=1080:1920:flags=lanczos,fps=30,format=yuv420p,setsar=1[v];"
      f"[1:v]format=rgba{of}[t];[v][t]overlay=0:0:shortest=1,format=yuv420p[cv];"
      + LN)
cmd = ['ffmpeg', '-nostdin', '-v', 'error', '-y', '-ss', f'{a:.3f}', '-t', f'{d:.3f}', '-i', S + src,
       '-loop', '1', '-t', f'{d:.3f}', '-i', ovl, '-filter_complex', fg, '-map', '[cv]', '-map', '[ca]',
       '-c:v', 'libx264', '-preset', 'slow', '-crf', '17', '-profile:v', 'high', '-pix_fmt', 'yuv420p', '-r', '30',
       '-color_primaries', 'bt709', '-color_trc', 'bt709', '-colorspace', 'bt709',
       '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-movflags', '+faststart', out]
subprocess.run(cmd, check=True)
print('done', out, round(d, 2))
