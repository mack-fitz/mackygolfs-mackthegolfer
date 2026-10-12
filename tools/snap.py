import array,math,sys,json
d=array.array('h',open(sys.argv[1],'rb').read());sr=16000;n=320
rms=[20*math.log10(math.sqrt(sum(x*x for x in d[i:i+n])/n)+1e-9)-90.3 for i in range(0,len(d)-n,n)]
def snap(t,w=0.25):
    a=max(0,int((t-w)*sr/n));b=min(len(rms)-1,int((t+w)*sr/n))
    k=min(range(a,b+1),key=lambda j:rms[j]);return round(k*n/sr+0.01,2),round(rms[k],1)
segs=json.loads(sys.argv[2]);out=[]
for a,b,z in segs:
    sa,da=snap(a) if a>0 else (0,0); sb,db=snap(b)
    out.append([sa,sb,z]); print(a,'->',sa,da,'|',b,'->',sb,db,file=sys.stderr)
print(json.dumps(out))
