#!/usr/bin/env python3
"""Full never-posted count across ALL Dropbox source folders (PLAYBOOK: "Source folders for new videos").

  python3 tools/full_count.py match <shard> <nshards> <out.json>
      every fingerprinted source (state/fp/sources/**.json, one per unique Dropbox content; byte-identical
      copies share one, see state/fp/full_manifest.json) x every posted reel (state/fp/posts/*.json),
      and every source x source pair. Writes overlap seconds for the pairs that overlap at all.
      (runs in the fpfull workflow, 8 shards x 4 processes)
  python3 tools/full_count.py merge <dir> <out.json>
Rules applied later (state/never_posted.json builder): DUP CHECK FIX = ALREADY POSTED only if ONE post
holds >= 15 s of the source (audio or frames); same video = files whose fingerprints overlap for most of
the shorter one.
"""
import glob, json, os, sys
from multiprocessing import Pool
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import match_fp as M

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FP = os.path.join(ROOT, "state", "fp")

def sources():
    out = {}
    for p in sorted(glob.glob(os.path.join(FP, "sources", "**", "*.json"), recursive=True)):
        out[os.path.relpath(p, os.path.join(FP, "sources"))[:-5]] = p
    return out

def posts():
    return {os.path.basename(p)[:-5]: p for p in sorted(glob.glob(os.path.join(FP, "posts", "*.json")))}

_cache = {}
def load(p):
    if p not in _cache:
        _cache[p] = json.load(open(p))
    return _cache[p]

def work(job):
    kind, a, b, pa, pb = job
    try:
        r = M.overlap(load(pa), load(pb))
    except Exception as e:
        return [kind, a, b, {"error": str(e)}]
    if not (r["audio_s"] or r["audio_total_s"] or r["frames_s"] or r["thumb_dist"] is not None):
        return None
    return [kind, a, b, r]

def match(shard, n, out):
    S, P = sources(), posts()
    names = sorted(S)
    jobs = []
    for i, s in enumerate(names):
        for k in sorted(P):
            jobs.append(("post", k, s, P[k], S[s]))          # a = posted reel, b = source (dense)
        for s2 in names[i + 1:]:
            jobs.append(("src", s, s2, S[s], S[s2]))
    mine = jobs[shard::n]
    with Pool(4) as pool:
        res = [r for r in pool.imap_unordered(work, mine, chunksize=20) if r]
    json.dump({"shard": shard, "pairs_checked": len(mine), "pairs": res}, open(out, "w"))
    print(f"shard {shard}: {len(mine)} pairs, {len(res)} overlapping")

def merge(d, out):
    allp, checked = [], 0
    for f in sorted(glob.glob(os.path.join(d, "*.json"))):
        x = json.load(open(f)); allp += x["pairs"]; checked += x["pairs_checked"]
    json.dump({"pairs_checked": checked, "sources": sorted(sources()), "posts": len(posts()), "pairs": allp},
              open(out, "w"), separators=(",", ":"))
    print("merged", checked, len(allp))

if __name__ == "__main__":
    if sys.argv[1] == "match":
        match(int(sys.argv[2]), int(sys.argv[3]), sys.argv[4])
    else:
        merge(sys.argv[2], sys.argv[3])
