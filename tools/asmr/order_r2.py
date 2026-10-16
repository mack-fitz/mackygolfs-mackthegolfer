import json,random
P=[b for b in json.load(open('pool_ok.json')) if b['i'] not in (152,144,166)]
random.seed(13)
first=[b for b in P if b['i']==43][0]  # driver over the water
seq=[first]; rest=[b for b in P if b is not first]
while rest:
    random.shuffle(rest)
    def ok(b):
        if b['g']==seq[-1]['g']: return False
        if len(seq)>=2 and b['type']==seq[-1]['type']==seq[-2]['type']: return False
        if any(x['src']==b['src'] for x in seq[-4:]): return False
        return True
    c=[b for b in rest if ok(b)] or [b for b in rest if b['g']!=seq[-1]['g']] or rest
    # prefer the group with most remaining to avoid stranding
    from collections import Counter
    cnt=Counter(b['g'] for b in rest); c.sort(key=lambda b:-cnt[b['g']])
    seq.append(c[0]); rest.remove(c[0])
for k in range(1,len(seq)):
    if seq[k]['g']==seq[k-1]['g']: print('ADJ',k)
print(len(seq),[ (b['g'],b['type'][0]) for b in seq])
json.dump(seq,open('seq.json','w'),indent=0)
