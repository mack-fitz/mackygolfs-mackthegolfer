# On-reel meme text, Mack Oct 17 rule: Inter Bold 46, white, 3 px black stroke @85%, soft drop shadow, centered, >=90 px side margins.
from PIL import Image,ImageDraw,ImageFont,ImageFilter
FONT='/usr/share/fonts/opentype/inter/Inter-Bold.otf'; SIZE=46; STROKE=3; W,H=1080,1920; LEAD=12
def make(lines,top,out):
    f=ImageFont.truetype(FONT,SIZE); d0=ImageDraw.Draw(Image.new('RGBA',(W,H)))
    boxes=[d0.textbbox((0,0),t,font=f,stroke_width=STROKE) for t in lines]
    asc=f.getmetrics()[0]; lh=SIZE+LEAD
    # ink top of first line (incl. stroke) lands exactly on `top`
    y0=top-boxes[0][1]
    txt=Image.new('RGBA',(W,H),(0,0,0,0)); sh=Image.new('RGBA',(W,H),(0,0,0,0))
    dt=ImageDraw.Draw(txt); ds=ImageDraw.Draw(sh); ink=[W,H,0,0]
    for i,(t,b) in enumerate(zip(lines,boxes)):
        tw=b[2]-b[0]; x=(W-tw)//2-b[0]; y=y0+i*lh
        assert (W-tw)//2>=90, (t,tw)
        ds.text((x+3,y+4),t,font=f,fill=(0,0,0,200),stroke_width=STROKE,stroke_fill=(0,0,0,200))
        dt.text((x,y),t,font=f,fill=(255,255,255,255),stroke_width=STROKE,stroke_fill=(0,0,0,217))
        bb=dt.textbbox((x,y),t,font=f,stroke_width=STROKE); ink=[min(ink[0],bb[0]),min(ink[1],bb[1]),max(ink[2],bb[2]),max(ink[3],bb[3])]
    sh=sh.filter(ImageFilter.GaussianBlur(6))
    im=Image.alpha_composite(sh,txt); im.save(out); return ink
if __name__=='__main__':
    import sys,json; print(make(json.loads(sys.argv[1]),int(sys.argv[2]),sys.argv[3]))
