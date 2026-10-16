from PIL import Image,ImageDraw,ImageFont,ImageFilter
W,H=1080,1920; txt="asmr but it's golf"
f=ImageFont.truetype('/usr/share/fonts/opentype/inter/Inter-SemiBold.otf',72)
im=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(im)
bb=d.textbbox((0,0),txt,font=f); tw=bb[2]-bb[0]; x=(W-tw)//2; y=330
sh=Image.new('RGBA',(W,H),(0,0,0,0)); ds=ImageDraw.Draw(sh)
ds.text((x+3,y+4),txt,font=f,fill=(0,0,0,200)); sh=sh.filter(ImageFilter.GaussianBlur(6))
im=Image.alpha_composite(sh,im); d=ImageDraw.Draw(im); d.text((x,y),txt,font=f,fill=(255,255,255,255))
im.save('ovl.png'); print(x,y,tw)
