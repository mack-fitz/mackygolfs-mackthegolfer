import sys,json,subprocess,numpy as np
from src import sources
S=sources(); T='/home/claude/mackygolfs-mackthegolfer/state/transcripts/'
res={}
for n,p in S.items():
    raw=subprocess.run(['ffmpeg','-v','error','-i',p,'-ac','1','-ar','48000','-af','highpass=f=1500','-f','f32le','-'],capture_output=True).stdout
    x=np.frombuffer(raw,np.float32); W=240  # 5ms
    e=10*np.log10(np.add.reduceat(x[:len(x)//W*W]**2,np.arange(0,len(x)//W*W,W))/W+1e-12)
    words=[]
    try:
        for s in json.load(open(T+n+'.json'))['segments']:
            words+= [(w[0],w[1]) for w in s.get('words',[])]
    except Exception as ex: print('no tr',n)
    c=[]
    for i in range(20,len(e)-10):
        pre=np.median(e[i-20:i-2]); pk=e[i:i+3].max()
        if pk-pre>18 and pk>-45 and e[i]-e[i-1]>8:
            t=i*W/48000
            if c and t-c[-1][0]<0.4: continue
            near=min([min(abs(t-a),abs(t-b)) if not(a<=t<=b) else 0 for a,b in words] or [9])
            c.append((round(float(t),3),round(float(pk-pre),1),round(float(pk),1),round(float(near),2)))
    res[n]=c; print(n,len(x)/48000,len(c),[cc for cc in c if cc[3]>0.3][:40])
json.dump(res,open('onsets.json','w'))
