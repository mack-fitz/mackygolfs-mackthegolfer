#!/bin/bash
# usage: render.sh src segs.json "hook1" "hook2" out.mp4
# segs: [[start, end, zoom], ...]  zoom 1 = ~15% center punch-in.
# Trial accounts: pass "" "" (no text drawn on the video).
# SINGLE high-quality encode (Mack, Oct 13): all cuts/punch-ins are done in one filtergraph
# straight from the source file, then one libx264 -crf 17 -preset slow pass at the source
# resolution and frame rate, AAC 192k 48 kHz. No intermediate encodes, no -b:v cap, no -r 30.
set -e
SRC="$1"; SEGS="$2"; H1="$3"; H2="$4"; OUT="$5"
FONT=/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf
read W H FPS < <(ffprobe -v error -select_streams v:0 -show_entries stream=width,height,r_frame_rate -of csv=p=0 "$SRC" | tr ',' ' ')
# phone .mp4s carry a -90/90 rotation tag; ffmpeg auto-rotates, so swap W/H to match the upright frames
ROT=$(ffprobe -v error -select_streams v:0 -show_entries stream_side_data=rotation -of csv=p=0 "$SRC" | tr -d '\r\n ,')
case "$ROT" in 90|-90|270|-270) T=$W; W=$H; H=$T;; esac
FG=$(python3 -I - "$SEGS" "$W" "$H" "$FONT" "$H1" "$H2" <<'PY'
import json, sys
segs = json.load(open(sys.argv[1])); w, h = int(sys.argv[2]), int(sys.argv[3])
font, h1, h2 = sys.argv[4], sys.argv[5], sys.argv[6]
parts, labels = [], []
for i, (a, b, z) in enumerate(segs):
    jin = i > 0 and abs(segs[i-1][1] - a) > 0.01
    jout = i < len(segs) - 1 and abs(segs[i+1][0] - b) > 0.01
    d = b - a
    zv = f",crop=iw/1.15:ih/1.15,scale={w}:{h}:flags=lanczos" if z else ""
    parts.append(f"[{i}:v]setpts=PTS-STARTPTS{zv},setsar=1[v{i}]")
    af = ["anull"]
    if jin: af.append("afade=t=in:d=0.03")
    if jout: af.append(f"afade=t=out:st={max(0, d-0.03):.3f}:d=0.03")
    parts.append(f"[{i}:a]asetpts=PTS-STARTPTS,aresample=48000,{','.join(af)}[a{i}]")
    labels.append(f"[v{i}][a{i}]")
vf = "null"
if h1 or h2:
    vf = (f"drawtext=fontfile={font}:text='{h1}':fontsize=68:fontcolor=white:box=1:boxcolor=black@0.75:boxborderw=22:x=(w-text_w)/2:y=300,"
          f"drawtext=fontfile={font}:text='{h2}':fontsize=68:fontcolor=white:box=1:boxcolor=black@0.75:boxborderw=22:x=(w-text_w)/2:y=410")
parts.append(f"{''.join(labels)}concat=n={len(segs)}:v=1:a=1[cv][ca]")
parts.append(f"[cv]{vf}[ov]")
print(";".join(parts))
PY
)
# one input per segment (accurate -ss/-t seek, decoded once each) so long edits don't buffer
# the whole source in memory; still a single encode.
# GitHub rejects files over 100 MB (media is served from raw.githubusercontent). For a long edit
# that would exceed that, set MAXRATE (e.g. MAXRATE=12M) to cap peaks only; still crf 17, one encode.
VBV=""; [ -n "$MAXRATE" ] && VBV="-maxrate $MAXRATE -bufsize $(( ${MAXRATE%M} * 2 ))M"
INS=()
while read a d; do INS+=(-ss "$a" -t "$d" -i "$SRC"); done < <(python3 -I -c "import json,sys;[print(a, round(b-a,3)) for a,b,z in json.load(open(sys.argv[1]))]" "$SEGS")
ffmpeg -nostdin -v error -y "${INS[@]}" -filter_complex "$FG" -map "[ov]" -map "[ca]" \
  -c:v libx264 -preset slow -crf 17 $VBV -profile:v high -pix_fmt yuv420p -r "$FPS" \
  -c:a aac -b:a 192k -ar 48000 -movflags +faststart "$OUT"
