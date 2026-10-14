# usage: python3 render_wipes.py comps.json comp2 out.mp4
import json,sys,subprocess,numpy as np
d=json.load(open(sys.argv[1]))[sys.argv[2]]; out=sys.argv[3]; S="/home/claude/src/"
def lvl(src,n):
    b=subprocess.run(["ffmpeg","-v","error","-t",f"{n/30:.4f}","-i",S+src,"-ac","1","-ar","48000","-f","s16le","-"],capture_output=True).stdout
    x=np.frombuffer(b,np.int16).astype(float)/32768; w=2400
    r=np.array([np.sqrt(np.mean(x[i:i+w]**2)) for i in range(0,len(x)-w+1,w)])
    r=np.sort(r)[len(r)//2:]  # louder half
    return 20*np.log10(np.sqrt(np.mean(r**2))+1e-9)
ins=[];vf=[];af=[];lab=[]
for i,(src,n,_,_) in enumerate(d):
    L=lvl(src,n); g=max(-12,min(12,-30-L)); print(f"{src[:40]:40s} {n/30:.3f}s lvl {L:.1f} gain {g:+.1f}")
    ins+=["-t",f"{n/30+0.5:.3f}","-i",S+src]
    vf.append(f"[{i}:v]fps=30,trim=end_frame={n},setpts=PTS-STARTPTS,scale=1080:1920:flags=lanczos,setsar=1,format=yuv420p[v{i}]")
    fa=[f"volume={g:.2f}dB"]
    if i>0: fa.append("afade=t=in:d=0.02")
    if i<len(d)-1: fa.append(f"afade=t=out:st={n/30-0.03:.4f}:d=0.03")
    af.append(f"[{i}:a]aresample=48000,aformat=channel_layouts=stereo,atrim=end={n/30:.5f},asetpts=PTS-STARTPTS,{','.join(fa)}[a{i}]")
    lab.append(f"[v{i}][a{i}]")
k=len(d)
base=";".join(vf+af)+";"+"".join(lab)+f"concat=n={k}:v=1:a=1[cv][ca0];[ca0]volume=11dB,alimiter=limit=0.45:level=false[ca1]"
r=subprocess.run(["ffmpeg","-nostdin","-hide_banner"]+ins+["-filter_complex",base+";[cv]nullsink;[ca1]loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json[ca]","-map","[ca]","-f","null","-"],capture_output=True,text=True).stderr
m=json.loads(r[r.rfind("{"):r.rfind("}")+1])
ln=f"loudnorm=I=-16:TP=-1.5:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true"
cmd=["ffmpeg","-nostdin","-v","error","-y"]+ins+["-filter_complex",base+f";[ca1]{ln},aresample=48000[ca]","-map","[cv]","-map","[ca]","-c:v","libx264","-preset","slow","-crf","17","-profile:v","high","-pix_fmt","yuv420p","-r","30","-color_primaries","bt709","-color_trc","bt709","-colorspace","bt709","-c:a","aac","-b:a","192k","-ar","48000","-movflags","+faststart",out]
subprocess.run(cmd,check=True); print("measured",m["input_i"],m["normalization_type"] if "normalization_type" in m else "")
