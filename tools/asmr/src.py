import glob,os
R='/home/claude/mackygolfs-mackthegolfer/inbox/videos/'
def sources():
    out={}
    for f in sorted(glob.glob(R+'*')):
        b=os.path.basename(f)
        if b.endswith('.sha256'): continue
        if '.part' in b:
            n=b.split('.part')[0]
            out.setdefault(n,[]).append(f)
        else: out[b]=[f]
    return {n:(v[0] if len(v)==1 else 'concat:'+'|'.join(sorted(v))) for n,v in out.items()}
