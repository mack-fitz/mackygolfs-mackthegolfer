# comp13 r3 (Mack, Oct 17): same cut as r2 (bits from compilations/comp13_r2_bits.json), only the on-reel text changes:
# "asmr but it's golf" Inter Bold 46, white, 3 px black stroke @85% + soft shadow, ink top y 1180 (lower band), first 2.0 s, fades out 1.8-2.0 s.
# usage: python3 render_r3.py <src dir> <overlay.png> <out.mp4>   (overlay from the Oct 17 text helper, 1080x1920 RGBA)
import subprocess,numpy as np,sys,json,os
SRC,OVL,out=sys.argv[1],sys.argv[2],sys.argv[3]; TXT=2.0
B=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'../../compilations/comp13_r2_bits.json')))
ins=[];vf=[];af=[];lab=[];gains=[]
for i,bt in enumerate(B):
    k,a,b=os.path.join(SRC,bt['src']),bt['in'],bt['out']
    raw=subprocess.run(['ffmpeg','-v','error','-ss',f'{a}','-t',f'{b-a:.3f}','-i',k,'-ac','1','-ar','48000','-af','highpass=f=80','-f','f32le','-'],capture_output=True).stdout
    x=np.frombuffer(raw,np.float32);W=480
    e=10*np.log10(np.add.reduceat(x[:len(x)//W*W]**2,np.arange(0,len(x)//W*W,W))/W+1e-12)
    gn=min(24,-5-e.max()); gains.append(round(float(gn),1))
    d=round((b-a)*30)/30
    ins+=['-ss',f'{a:.3f}','-t',f'{d+0.5:.3f}','-i',k]
    vf.append(f'[{i}:v]trim=duration={d:.4f},setpts=PTS-STARTPTS,scale=1080:1920:flags=lanczos,fps=30,format=yuv420p,setsar=1[v{i}]')
    af.append(f'[{i}:a]atrim=duration={d:.4f},asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo,highpass=f=80,volume={gn:.2f}dB,afade=t=in:d=0.006,afade=t=out:st={d-0.02:.3f}:d=0.02[a{i}]')
    lab.append(f'[v{i}][a{i}]')
n=len(B)
fg=';'.join(vf+af)+';'+''.join(lab)+f'concat=n={n}:v=1:a=1[cv0][ca0];[ca0]alimiter=limit=0.7:level=false,aresample=48000[ca];'
fg+=f'[{n}:v]format=rgba,fade=t=out:st={TXT-0.2}:d=0.2:alpha=1[ov];[cv0][ov]overlay=0:0:eof_action=pass,format=yuv420p[cv]'
cmd=['ffmpeg','-nostdin','-v','error','-y']+ins+['-loop','1','-t',str(TXT),'-framerate','30','-i',OVL,'-filter_complex',fg,'-map','[cv]','-map','[ca]','-c:v','libx264','-preset','slow','-crf','17','-profile:v','high','-pix_fmt','yuv420p','-r','30','-color_primaries','bt709','-color_trc','bt709','-colorspace','bt709','-c:a','aac','-b:a','192k','-ar','48000','-movflags','+faststart',out]
subprocess.run(cmd,check=True); print('gains',gains)
