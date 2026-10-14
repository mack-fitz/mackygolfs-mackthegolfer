#!/usr/bin/env python3
"""Build the "already posted" index (DUPLICATE CHECK V2 in PLAYBOOK.md).

Refresh (morning run, when state/posted_index.json is over 24 h old):
 1. Zernio analytics_get_analytics for each of the 3 IG accounts (source "all", limit 100, every page,
    366-day windows back to the account's first post). Save the posts as a JSON list of
    {account, zid, late_id, ig_id, url, published, caption, duration, media_type, product,
     video_url, thumb_url}  (copy URLs exactly; easiest is ast.literal_eval on the raw tool text).
 2. python3 tools/posted_index.py want <posts.json>
      -> writes fp/want_posts.tsv for reels with no fingerprint yet (plus fp/want_sources.txt for
         Golf Captions files with no fingerprint, from state/fp/sources_meta.json). Commit + push;
         wait for the "Fingerprints" commit of the fingerprint workflow; pull.
 3. python3 tools/posted_index.py build <posts.json>
      -> state/posted_index.json (every post + every source with its matches)
      -> state/never_posted.json  (ONLY sources with no fingerprint overlap on any account)
 Check a rendered file or queue item against the index / against another video:
    python3 tools/posted_index.py check <fp.json>        (which posts does it overlap?)
    python3 tools/match_fp.py pair <a.json> <b.json>
"""
import json, os, sys, glob, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import match_fp as M

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FP = os.path.join(ROOT, "state", "fp")
ACCOUNTS = {"mackygolfs": "6acce837f3bd55021dad245f", "mackthegolfer": "6accea22c485191e985aa1cb",
            "moremackygolfs": "6acc2885bac230e9d1133105"}

def key(p):
    return f"{p['account']}_{p['ig_id']}"

def load(path):
    return json.load(open(path))

def want(posts_path):
    posts = load(posts_path)
    rows = []
    for p in posts:
        if p.get("media_type") != "video":
            continue
        if os.path.exists(os.path.join(FP, "posts", key(p) + ".json")):
            continue
        rows.append("\t".join([key(p), p.get("url") or "", p.get("video_url") or "", p.get("thumb_url") or ""]))
    os.makedirs(os.path.join(ROOT, "fp"), exist_ok=True)
    if rows:
        open(os.path.join(ROOT, "fp", "want_posts.tsv"), "w").write("\n".join(rows) + "\n")
    meta = load(os.path.join(FP, "sources_meta.json"))["files"]
    missing = [n for n in meta if not os.path.exists(os.path.join(FP, "sources", n + ".json"))]
    if missing:
        open(os.path.join(ROOT, "fp", "want_sources.txt"), "w").write("\n".join(missing) + "\n")
    print(f"want_posts: {len(rows)}  want_sources: {len(missing)}")

def mt(iso):
    t = datetime.datetime.fromisoformat(iso.replace("Z", "+00:00"))
    return (t - datetime.timedelta(hours=6)).strftime("%Y-%m-%d %H:%M MT")  # MDT (until Nov 1)

def build(posts_path):
    posts = load(posts_path)
    meta = load(os.path.join(FP, "sources_meta.json"))["files"]
    sources = {n: load(os.path.join(FP, "sources", n + ".json")) for n in meta
               if os.path.exists(os.path.join(FP, "sources", n + ".json"))}
    out_posts, pfp = [], {}
    for p in sorted(posts, key=lambda x: x["published"]):
        f = os.path.join(FP, "posts", key(p) + ".json")
        rec = {"account": p["account"], "platformPostUrl": p.get("url"), "date": p["published"],
               "date_mt": mt(p["published"]), "caption": p.get("caption"), "duration": p.get("duration"),
               "zernio_id": p.get("zid"), "late_post_id": p.get("late_id"), "media_type": p.get("media_type")}
        if os.path.exists(f):
            d = load(f)
            pfp[key(p)] = d
            rec["fingerprint"] = os.path.relpath(f, ROOT)
            rec["fp_kind"] = d["kind"]; rec["fp_from"] = d.get("meta", {}).get("got")
            if d.get("duration"): rec["duration"] = rec["duration"] or round(d["duration"])
        else:
            rec["fingerprint"] = None; rec["fp_kind"] = None
        rec["sources"] = []
        out_posts.append(rec)
    by_key = {key(p): r for p, r in zip(sorted(posts, key=lambda x: x["published"]), out_posts)}
    mp_path = os.path.join(FP, "manual_posts.json")
    manual = load(mp_path)["posts"] if os.path.exists(mp_path) else []
    out_sources = []
    for name, s in sorted(sources.items()):
        matches = []
        for k, d in pfp.items():
            r = M.overlap(d, s)
            if M.is_match(r):
                pr = by_key[k]
                aud = r["audio_s"] > M.THRESH_S or r.get("audio_total_s", 0) >= M.TOTAL_THRESH_S
                fr = r["frames_s"] >= M.FRAME_THRESH_S
                how = "thumbnail" if r["thumb_dist"] is not None else ("audio+frames" if aud and fr else ("audio" if aud else "frames"))
                matches.append({"account": pr["account"], "platformPostUrl": pr["platformPostUrl"],
                                "date_mt": pr["date_mt"], "caption": (pr["caption"] or "")[:120],
                                "audio_overlap_s": r["audio_s"], "audio_total_s": r.get("audio_total_s"), "frame_overlap_s": r["frames_s"],
                                "thumb_dist": r["thumb_dist"], "how": how})
                pr["sources"].append(name)
        # posts no longer on Instagram (deleted) but known to have gone out: state/fp/manual_posts.json
        for mp in manual:
            if mp["source"] == name:
                matches.append({"account": mp["account"], "platformPostUrl": None, "date_mt": mp["date_mt"],
                                "caption": mp.get("caption", ""), "how": "manual", "note": mp.get("note", "")})
        matches.sort(key=lambda m: m["date_mt"])
        out_sources.append({"name": name, "dropbox_id": meta[name], "duration": s.get("duration"),
                            "status": "ALREADY POSTED" if matches else "never posted",
                            "first_posted": matches[0] if matches else None, "matches": matches})
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
    n_fp = sum(1 for r in out_posts if r["fingerprint"])
    idx = {"updated": now,
           "rule": "PLAYBOOK DUPLICATE CHECK V2: a source is ALREADY POSTED if its audio fingerprint lines up with a posted reel for > 5 s in one stretch (or >= 12 s across several >= 3 s stretches, for re-edits) or its 2-s frame hashes line up for >= 8 s of changing picture (or, for posts where only the cover image could be fetched, the cover matches a source frame). Never judge by length or caption.",
           "accounts": ACCOUNTS,
           "coverage": {"posts": len(out_posts), "fingerprinted": n_fp,
                        "video_fp": sum(1 for r in out_posts if r["fp_kind"] == "video"),
                        "thumbnail_only": sum(1 for r in out_posts if r["fp_kind"] == "thumbnail"),
                        "missing": [r["platformPostUrl"] for r in out_posts if not r["fingerprint"]]},
           "sources": out_sources, "posts": out_posts}
    json.dump(idx, open(os.path.join(ROOT, "state", "posted_index.json"), "w"), indent=1, ensure_ascii=False)
    # keep hand-kept fields (lined_up / used) from the previous never_posted.json
    np_path = os.path.join(ROOT, "state", "never_posted.json")
    prev = {v["name"]: v for v in load(np_path).get("videos", [])} if os.path.exists(np_path) else {}
    keep = lambda n: {k: v for k, v in prev.get(n, {}).items() if k in ("lined_up", "used", "subfolder")}
    never = {"updated": now, "from": "state/posted_index.json (fingerprint-checked against every post on @mackygolfs, @mackthegolfer, @moremackygolfs)",
             "note": "Never-posted status comes ONLY from this file (PLAYBOOK DUPLICATE CHECK V2). 'lined_up' = already on the review page / scheduled; once it posts, the next refresh drops it (it matches its own post).",
             "videos": [dict({"name": s["name"], "dropbox_id": s["dropbox_id"], "duration": s["duration"]}, **keep(s["name"]))
                        for s in out_sources if not s["matches"]]}
    json.dump(never, open(os.path.join(ROOT, "state", "never_posted.json"), "w"), indent=1, ensure_ascii=False)
    print(f"posts {len(out_posts)} (fp {n_fp}); sources {len(out_sources)}; never posted {len(never['videos'])}")
    for s in out_sources:
        print(f"  {s['status']:15} {s['name']}  " + "; ".join(f"{m['account']} {m['date_mt'][:10]} ({m['how']} {m.get('audio_overlap_s')}/{m.get('audio_total_s')}/{m.get('frame_overlap_s')})" for m in s["matches"][:4]))

def check(fp_path):
    d = load(fp_path)
    idx = load(os.path.join(ROOT, "state", "posted_index.json"))
    for p in idx["posts"]:
        if not p.get("fingerprint"):
            continue
        r = M.overlap(load(os.path.join(ROOT, p["fingerprint"])), d)
        if M.is_match(r):
            print(p["account"], p["date_mt"], p["platformPostUrl"], json.dumps(r), (p["caption"] or "")[:60])

if __name__ == "__main__":
    {"want": want, "build": build, "check": check}[sys.argv[1]](sys.argv[2])
