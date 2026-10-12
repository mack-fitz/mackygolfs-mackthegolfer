#!/bin/bash
# usage: render.sh src segs.json "hook1" "hook2" out.mp4
set -e
SRC="$1"; SEGS="$2"; H1="$3"; H2="$4"; OUT="$5"
FONT=/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf
W=$(mktemp -d)
python3 -I - "$SEGS" > $W/plan.txt <<'PY'
import json,sys
s=json.load(open(sys.argv[1]))
for i,(a,b,z) in enumerate(s):
    fin = i>0 and abs(s[i-1][1]-a)>0.01
    fout = i<len(s)-1 and abs(s[i+1][0]-b)>0.01
    print(a,b,z,int(fin),int(fout))
PY
i=0; : > $W/list.txt
while read a b z fin fout; do
  d=$(python3 -c "print(round($b-$a,3))"); fo=$(python3 -c "print(round($b-$a-0.03,3))")
  V=""; [ "$z" = 1 ] && V="crop=iw/1.15:ih/1.15,"
  AF="anull"; [ "$fin" = 1 ] && AF="afade=t=in:d=0.03"; [ "$fout" = 1 ] && AF="$AF,afade=t=out:st=$fo:d=0.03"
  ffmpeg -nostdin -v error -y -ss $a -i "$SRC" -t $d -vf "${V}scale=1080:1920,setsar=1" -af "$AF" -c:v libx264 -preset veryfast -crf 16 -pix_fmt yuv420p -r 30 -c:a aac -b:a 192k -ar 48000 $W/s$i.mp4
  echo "file 's$i.mp4'" >> $W/list.txt; i=$((i+1))
done < $W/plan.txt
# No hook text (trial accounts): pass "" "" and nothing is drawn on the video.
if [ -z "$H1$H2" ]; then VF="null"; else VF="drawtext=fontfile=$FONT:text='$H1':fontsize=68:fontcolor=white:box=1:boxcolor=black@0.75:boxborderw=22:x=(w-text_w)/2:y=300,drawtext=fontfile=$FONT:text='$H2':fontsize=68:fontcolor=white:box=1:boxcolor=black@0.75:boxborderw=22:x=(w-text_w)/2:y=410"; fi
ffmpeg -v error -y -f concat -safe 0 -i $W/list.txt -vf "$VF" -c:v libx264 -preset medium -b:v 4.5M -maxrate 6M -bufsize 10M -profile:v high -pix_fmt yuv420p -r 30 -g 60 -c:a aac -b:a 128k -ar 48000 -movflags +faststart "$OUT"
rm -rf $W
