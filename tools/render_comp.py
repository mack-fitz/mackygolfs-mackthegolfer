# Compilation renderer (comp4+). usage: python3 render_comp.py bits.json out.mp4 [overlay.png]
# optional overlay.png (1080x1920 RGBA) is laid over the whole video in the same single encode (only when Mack asks for on-reel text).
# bits.json: [{src, parts:[[in,out,zoom]], adj?: dB, pg?: [dB per part]}]; sources are read from <this script dir>/src/
# (symlink/rejoin the true originals there). Per-bit gain to -18 LUFS, 20/30 ms fades at jumps, alimiter,
# 2-pass linear loudnorm -16 LUFS; ONE libx264 crf 17 slow encode, 1080x1920 30 fps, AAC 192k.
# env COMP_FINAL_LIMIT=0.71 adds a true-peak safety limiter after loudnorm (only touches transients like club impacts).
# parts may carry a 4th value vlead: video starts that many s later (first frame held) so audio can start just before her own scene cut.
import json,sys,subprocess,re,os
S=os.path.dirname(os.path.abspath(sys.argv[0]))
bits=json.load(open(sys.argv[1])); out=sys.argv[2]; srcdir=S+'/src/'
ovl=sys.argv[3] if len(sys.argv)>3 else None
def loud(src,parts):
    # integrated loudness of a bit
    ins=[];fl=[]
    for i,pp in enumerate(parts):
        a,b=pp[0],pp[1]
        ins+=['-ss',str(a),'-t',f'{b-a:.3f}','-i',srcdir+src]; fl.append(f'[{i}:a]')
    fg=''.join(fl)+f'concat=n={len(parts)}:v=0:a=1,ebur128[o]'
    r=subprocess.run(['ffmpeg','-nostdin','-hide_banner']+ins+['-filter_complex',fg,'-map','[o]','-f','null','-'],capture_output=True,text=True).stderr
    return float(re.findall(r'I:\s+(-?[\d.]+) LUFS',r)[-1])
gains=[]
for bt in bits:
    L=loud(bt['src'],bt['parts']); g=max(-12,min(15,-18-L+bt.get('adj',0))); gains.append(g); print(bt['src'][:30],'L',L,'gain',round(g,1))
ins=[];vf=[];af=[];labels=[];k=0
allparts=[]
for bi,bt in enumerate(bits):
    for pi,part in enumerate(bt['parts']):
        a,b,z=part[:3]; vl=part[3] if len(part)>3 else 0
        ins+=['-ss',f'{a:.3f}','-t',f'{b-a:.3f}','-i',srcdir+bt['src']]
        d=b-a
        inidx=len(ins)//6-1
        if vl:
            ins+=['-ss',f'{a+vl:.3f}','-t',f'{b-a-vl:.3f}','-i',srcdir+bt['src']]
        contig_in = pi>0 and abs(bt['parts'][pi-1][1]-a)<0.01
        contig_out = pi<len(bt['parts'])-1 and abs(bt['parts'][pi+1][0]-b)<0.01
        zv=',crop=iw/1.15:ih/1.15,scale=1080:1920:flags=lanczos' if z else ''
        vsrc=f'[{len(ins)//6-1}:v]' if vl else f'[{inidx}:v]'
        tp=f',tpad=start_duration={vl:.3f}:start_mode=clone' if vl else ''
        vf.append(f'{vsrc}setpts=PTS-STARTPTS,scale=1080:1920:flags=lanczos{zv},fps=30{tp},format=yuv420p,setsar=1[v{k}]')
        pg=bt.get('pg',[0]*len(bt['parts']))[pi]
        fa=[f'volume={gains[bi]+pg:.2f}dB']
        if not contig_in and k>0: fa.append('afade=t=in:d=0.02')
        if not contig_out and k< sum(len(x['parts']) for x in bits)-1: fa.append(f'afade=t=out:st={max(0,d-0.03):.3f}:d=0.03')
        af.append(f'[{inidx}:a]asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo,{",".join(fa)}[a{k}]')
        labels.append(f'[v{k}][a{k}]'); k+=1
base=';'.join(vf+af)+';'+''.join(labels)+f'concat=n={k}:v=1:a=1[cv][ca0];[ca0]alimiter=limit=0.89:level=false[ca1]'
# pass 1: measure
r=subprocess.run(['ffmpeg','-nostdin','-hide_banner']+ins+['-filter_complex',base+';[cv]nullsink;[ca1]loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json[ca]','-map','[ca]','-f','null','-'],capture_output=True,text=True).stderr
j=r[r.rfind("{"):r.rfind("}")+1]
if not j.strip().startswith("{\n") and "input_i" not in j: print(r[-2000:]); sys.exit(1)
m=json.loads(j)
ln=f"loudnorm=I=-16:TP=-1.5:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true"
post=f",alimiter=limit={os.environ['COMP_FINAL_LIMIT']}:level=false:attack=1:release=50" if os.environ.get('COMP_FINAL_LIMIT') else ''  # opt-in (comp20): catch club-impact overs after linear loudnorm
fg=base+f';[ca1]{ln}{post},aresample=48000[ca]'
extra=[]
if ovl:
    extra=['-loop','1','-i',ovl]; fg=fg.replace('[cv]','[cv0]',1)+f';[cv0][{len(ins)//6}:v]overlay=0:0:shortest=1,format=yuv420p[cv]'
cmd=['ffmpeg','-nostdin','-v','error','-y']+ins+extra+['-filter_complex',fg,'-map','[cv]','-map','[ca]','-c:v','libx264','-preset','slow','-crf','17','-profile:v','high','-pix_fmt','yuv420p','-r','30','-color_primaries','bt709','-color_trc','bt709','-colorspace','bt709','-c:a','aac','-b:a','192k','-ar','48000','-movflags','+faststart',out]
subprocess.run(cmd,check=True)
print('done',m['input_i'])
