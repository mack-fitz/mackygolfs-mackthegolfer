# comp13 r2: Mack's note "sounds way closer together, multiple per second" -> 54 hits at 0.40 s each (12 frames: 0.13 s before contact, 0.27 s after) + the cup drop. Same per-bit gain/fades/limiter as r1, ONE crf 17 encode.
import subprocess,numpy as np,sys,json
sys.path.insert(0,'.')
from src import sources
S=sources(); out=sys.argv[1]; TXT=2.0; PRE,POST=0.13,0.27
seq=json.load(open('seq.json'))
B=[(b['src'],round(b['t']-PRE,3),round(b['t']+POST,3),b['g'],b['type'],b['t']) for b in seq]
B.append(('Video Oct 12 2026, 7 33 50 AM.mov',26.2,27.15,'LB','cup drop',26.76))
json.dump([dict(src=a,**{'in':b,'out':c},group=g,type=t,contact=k) for a,b,c,g,t,k in B],open('comp13_r2_bits.json','w'),indent=1)
ins=[];vf=[];af=[];lab=[];gains=[]
for i,(k,a,b,g,typ,t) in enumerate(B):
    raw=subprocess.run(['ffmpeg','-v','error','-ss',f'{a}','-t',f'{b-a:.3f}','-i',S[k],'-ac','1','-ar','48000','-af','highpass=f=80','-f','f32le','-'],capture_output=True).stdout
    x=np.frombuffer(raw,np.float32);W=480
    e=10*np.log10(np.add.reduceat(x[:len(x)//W*W]**2,np.arange(0,len(x)//W*W,W))/W+1e-12)
    gn=min(24,-5-e.max()); gains.append(round(float(gn),1))
    d=round((b-a)*30)/30
    ins+=['-ss',f'{a:.3f}','-t',f'{d+0.5:.3f}','-i',S[k]]
    vf.append(f'[{i}:v]trim=duration={d:.4f},setpts=PTS-STARTPTS,scale=1080:1920:flags=lanczos,fps=30,format=yuv420p,setsar=1[v{i}]')
    af.append(f'[{i}:a]atrim=duration={d:.4f},asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo,highpass=f=80,volume={gn:.2f}dB,afade=t=in:d=0.006,afade=t=out:st={d-0.02:.3f}:d=0.02[a{i}]')
    lab.append(f'[v{i}][a{i}]')
n=len(B)
fg=';'.join(vf+af)+';'+''.join(lab)+f'concat=n={n}:v=1:a=1[cv0][ca0];[ca0]alimiter=limit=0.7:level=false,aresample=48000[ca];'
fg+=f'[{n}:v]format=rgba,fade=t=out:st={TXT-0.2}:d=0.2:alpha=1[ov];[cv0][ov]overlay=0:0:eof_action=pass,format=yuv420p[cv]'
cmd=['ffmpeg','-nostdin','-v','error','-y']+ins+['-loop','1','-t',str(TXT),'-framerate','30','-i','ovl.png','-filter_complex',fg,'-map','[cv]','-map','[ca]','-c:v','libx264','-preset','slow','-crf','17','-profile:v','high','-pix_fmt','yuv420p','-r','30','-color_primaries','bt709','-color_trc','bt709','-colorspace','bt709','-c:a','aac','-b:a','192k','-ar','48000','-movflags','+faststart',out]
subprocess.run(cmd,check=True); print('gains',gains)
