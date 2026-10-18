# On-reel text in a bubble (Mack, Oct 18 comp14 note: "put bubble around the letters so it doesn't look like the captions").
# Inter Bold 46 px, black text on a white rounded bubble (one bubble per line, IG "text background" style), soft shadow.
# usage: python3 tools/ontext_bubble.py '["line 1","line 2"]' <bubble top y> out.png   -> prints the bubble box
from PIL import Image,ImageDraw,ImageFont,ImageFilter
FONT='/usr/share/fonts/opentype/inter/Inter-Bold.otf'; SIZE=46; W,H=1080,1920; PADX=22; PADY=12; GAP=0; R=22
def make(lines,top,out,fill=(255,255,255,245),ink=(0,0,0,255)):
    f=ImageFont.truetype(FONT,SIZE); d0=ImageDraw.Draw(Image.new('RGBA',(W,H)))
    asc,desc=f.getmetrics(); lh=asc+desc
    bub=Image.new('RGBA',(W,H),(0,0,0,0)); db=ImageDraw.Draw(bub)
    sh=Image.new('RGBA',(W,H),(0,0,0,0)); ds=ImageDraw.Draw(sh)
    txt=Image.new('RGBA',(W,H),(0,0,0,0)); dt=ImageDraw.Draw(txt)
    y=top; box=[W,H,0,0]
    for t in lines:
        tw=d0.textlength(t,font=f); bw=tw+2*PADX; bh=lh+2*PADY
        x0=(W-bw)/2; assert x0>=90,(t,tw)
        r=[x0,y,x0+bw,y+bh]
        ds.rounded_rectangle([r[0]+2,r[1]+4,r[2]+2,r[3]+4],R,fill=(0,0,0,110))
        db.rounded_rectangle(r,R,fill=fill)
        dt.text((x0+PADX,y+PADY),t,font=f,fill=ink)
        box=[min(box[0],r[0]),min(box[1],r[1]),max(box[2],r[2]),max(box[3],r[3])]
        y+=bh+GAP
    sh=sh.filter(ImageFilter.GaussianBlur(6))
    im=Image.alpha_composite(Image.alpha_composite(sh,bub),txt); im.save(out); return [int(v) for v in box]
if __name__=='__main__':
    import sys,json; print(make(json.loads(sys.argv[1]),int(sys.argv[2]),sys.argv[3]))
