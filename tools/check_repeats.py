#!/usr/bin/env python3
"""Pre-scheduling repeat guard (Mack, Oct 19). RUN BEFORE SCHEDULING, MOVING OR SWAPPING ANY POST.
Exit code 0 = clean, 1 = violations (do not schedule), 2 = could not verify (unknown media etc.).

RULES CHECKED (Mack's FINAL rule, Oct 19 evening — replaces every earlier version)
 R2 MAIN-ACCOUNT POOL, 7 DAYS: the pool is Instagram @mackygolfs + @mackthegolfer ONLY. A reel — any version of it
    (original, re-edit, Mack's own post) — must not post on either account within 7 days (168 h) of any version of
    it posting on either of them. Same source = same Dropbox video (/Golf Captions + /golfclips; twins and alt takes
    merged). Compilations and shorties are EXEMPT. TikTok, @moremackygolfs, X and Facebook do NOT count toward the pool
    and are not restricted by it.
 R1 EXACT DUPLICATE, PER ACCOUNT: the same media file (same bytes, any commit/caption) never posts twice on the same
    account (any account, incl. @moremackygolfs, FB, X). Different accounts are not an R1 problem.
 Mack's own posts (not made through Zernio) count for R2: they are fingerprinted (state/fp/posts in the
 mackygolfs-mackthegolfer repo) and matched against every source fingerprint.

INPUT: raw saved outputs of Zernio `posts_list_posts` (call_tool; from_date ~14 days back, to_date ~21
days ahead, limit 100, every page) and `analytics_get_analytics` per IG account (Mack's own posts):
    python3 tools/check_repeats.py --zernio p1.txt p2.txt --analytics an_*.txt [--plan plan.json]
                                   [--days 14] [--all] [--json out.json]
 --candidates FILE: REVIEW-PAGE GATE. JSON list of {"label", "account", "media": "repo:path", "time"?}.
         Each candidate is checked against every pool post (published, scheduled, Mack's own) within
         7 days either side of its time (no time = it could post tomorrow morning). Prints PASS/FAIL per
         candidate and, for a FAIL, the earliest date it clears. NOTHING goes on the Trial Reels Review
         page (and no draft is created) unless its candidate check PASSES. Exit 1 if any FAIL.
 --plan: extra planned posts not yet in Zernio, JSON list of
         {"account": "ig:mackygolfs", "time": "2026-10-21T18:44:00-06:00", "media": "repo:path", "label": "..."}
 Default output lists only violations that involve a post that has NOT published yet (fixable).
 --all also prints past ones (history).
Media -> sources comes from state/media_sources.json (tools/build_media_map.py). A future post whose
media isn't in that map is an error (exit 2): add it to the map first.
"""
import argparse, ast, json, os, subprocess, sys, urllib.parse, datetime as dt

# Works from either repo (a copy lives in mack-fitz/clips and mack-fitz/mackygolfs-mackthegolfer); both repos
# must be cloned side by side (default /home/claude/clips + /home/claude/mackygolfs-mackthegolfer), or set
# CLIPS_REPO / MG_REPO.
_HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_UP = os.path.dirname(_HERE)
CLIPS = os.environ.get("CLIPS_REPO") or (_HERE if os.path.basename(_HERE) == "clips" else os.path.join(_UP, "clips"))
MG = os.environ.get("MG_REPO") or (_HERE if os.path.basename(_HERE) == "mackygolfs-mackthegolfer" else os.path.join(_UP, "mackygolfs-mackthegolfer"))
REPOS = {"clips": CLIPS, "mackygolfs-mackthegolfer": MG}
WEEK = dt.timedelta(hours=168)
ACCOUNTS = {  # zernio account id -> pool key
    "6acce837f3bd55021dad245f": "ig:mackygolfs", "6accea22c485191e985aa1cb": "ig:mackthegolfer",
    "6acc2885bac230e9d1133105": "ig:moremackygolfs", "6ad052a5a442d9968f306c31": "fb:macky.golfs",
    "6acc3edbda858fbeab423c5a": "x:mackygolfs", "6acc3fd31ce18dfecf0a2249": "tiktok:mackygolfs",
}
POOL = {"ig:mackygolfs", "ig:mackthegolfer"}  # Mack, Oct 19 final: main accounts only
APPROVAL = {"ig:mackygolfs", "ig:mackthegolfer"}


def load_tool(path):
    raw = json.load(open(path))
    r = raw.get("result", raw) if isinstance(raw, dict) else raw
    if isinstance(r, str):
        try:
            return json.loads(r)
        except Exception:
            return ast.literal_eval(r)
    return r


def parse_t(s):
    return dt.datetime.fromisoformat(s.replace("Z", "+00:00"))


def mt(t):
    off = 6 if t < dt.datetime(2026, 11, 1, 8, tzinfo=dt.timezone.utc) else 7
    return (t - dt.timedelta(hours=off)).strftime("%a %b %d %H:%M MT")


_blob_cache = {}


def media_key(url):
    """raw.githubusercontent URL -> ('repo:path', blob sha or None)"""
    if "raw.githubusercontent.com/mack-fitz/" not in (url or ""):
        return None, None
    repo, ref, path = url.split("raw.githubusercontent.com/mack-fitz/")[1].split("/", 2)
    path = urllib.parse.unquote(path.split("?")[0])
    d = REPOS.get(repo)
    blob = None
    if d:
        ref = "origin/main" if ref == "main" else ref
        k = (d, ref, path)
        if k not in _blob_cache:
            r = subprocess.run(["git", "-C", d, "rev-parse", f"{ref}:{path}"], capture_output=True, text=True)
            _blob_cache[k] = r.stdout.strip() or None
        blob = _blob_cache[k]
    return f"{repo}:{path}", blob


class Use:
    def __init__(self, **kw):
        self.__dict__.update(kw)

    def label(self):
        st = "" if self.status in ("published",) else f" [{self.status}]"
        who = "Mack's own post" if self.external else f"zernio {self.post_id}"
        return f"{self.account} {mt(self.t)}{st} \"{(self.caption or '')[:45]}\" ({who}; {self.media or self.url})"


def zernio_uses(paths, mmap):
    uses, unknown = [], []
    for p in paths:
        d = load_tool(p)
        for post in d["posts"]:
            if post.get("status") in ("cancelled",):
                continue
            for pl in post["platforms"]:
                acc = pl["accountId"]["_id"] if isinstance(pl["accountId"], dict) else pl["accountId"]
                key = ACCOUNTS.get(acc)
                if not key:
                    continue  # not a golf account (e.g. heyymackyy)
                psd = pl.get("platformSpecificData") or {}
                if psd.get("contentType") == "story":
                    continue
                media = (pl.get("customMedia") or post.get("mediaItems") or [{}])[0]
                mk, blob = media_key(media.get("url", ""))
                t = parse_t(pl.get("publishedAt") or pl.get("scheduledFor") or post["scheduledFor"])
                status = pl.get("status") or post["status"]
                if post.get("isDraft") or post["status"] == "draft":
                    status = "draft"
                if status == "failed":
                    continue
                info = mmap.get(mk) if mk else None
                u = Use(account=key, t=t, status=status, post_id=post["_id"], caption=post.get("content"),
                        media=mk, url=media.get("url"), blob=blob, external=False,
                        sources=(info or {}).get("sources", []), main=(info or {}).get("main"),
                        kind=(info or {}).get("kind", "unknown"))
                if info is None and key in POOL and status != "published":
                    unknown.append(u)
                uses.append(u)
    # same post id + same account listed twice (pagination overlap) -> keep one
    seen, out = set(), []
    for u in uses:
        k = (u.post_id, u.account)
        if k not in seen:
            seen.add(k)
            out.append(u)
    return out, unknown


def external_uses(paths, since):
    """Mack's own IG posts (no Zernio late id) -> sources by fingerprint."""
    sys.path.insert(0, os.path.join(MG, "tools"))
    import match_fp as M
    cache_f = os.path.join(CLIPS, "state", "external_sources.json")
    cache = json.load(open(cache_f)) if os.path.exists(cache_f) else {}
    srcfp = None
    sys.path.insert(0, os.path.join(CLIPS, "tools"))
    from build_media_map import canon_map
    cmap = canon_map()
    uses, missing = [], []
    for p in paths:
        d = load_tool(p)
        for post in d["posts"]:
            if post.get("latePostId"):
                continue  # ours, already counted from Zernio
            pl = post["platforms"][0]
            key = ACCOUNTS.get(pl.get("accountId"))
            if key not in POOL:
                continue
            t = parse_t(post["publishedAt"])
            if t < since:
                continue
            url = post.get("platformPostUrl")
            ig = pl.get("platformPostId")
            if url not in cache:
                fpf = os.path.join(MG, "state", "fp", "posts", f"{key.split(':')[1]}_{ig}.json")
                if not os.path.exists(fpf):
                    missing.append(url)
                    continue
                if srcfp is None:
                    srcfp = {}
                    base = os.path.join(MG, "state", "fp", "sources")
                    for root, _, files in os.walk(base):
                        for f in files:
                            name = f[:-5]
                            if name in cmap:
                                srcfp[name] = json.load(open(os.path.join(root, f)))
                pf = json.load(open(fpf))
                hits = []
                for name, sf in srcfp.items():
                    r = M.overlap(pf, sf)
                    if M.is_match(r):
                        amt = max(r.get("audio_s") or 0, r.get("audio_total_s") or 0, r.get("frames_s") or 0)
                        hits.append((amt, cmap[name]))
                hits.sort(reverse=True)
                srcs = []
                for _, s in hits:
                    if s not in srcs:
                        srcs.append(s)
                cache[url] = {"account": key, "date": post["publishedAt"], "caption": post.get("content"), "sources": srcs}
            c = cache[url]
            uses.append(Use(account=key, t=t, status="published", post_id=url, caption=c["caption"], media=None,
                            url=url, blob=None, external=True, sources=c["sources"],
                            main=c["sources"][0] if c["sources"] else None,
                            kind="comp" if len(c["sources"]) > 2 else "original"))
    json.dump(cache, open(cache_f, "w"), indent=1)
    return uses, missing


def plan_uses(path, mmap):
    out, unknown = [], []
    for e in json.load(open(path)):
        info = mmap.get(e["media"])
        u = Use(account=e["account"], t=parse_t(e["time"]), status="planned", post_id=e.get("label", "plan"),
                caption=e.get("caption", e.get("label")), media=e["media"], url=None, blob=None, external=False,
                sources=(info or {}).get("sources", []), main=(info or {}).get("main"), kind=(info or {}).get("kind", "unknown"))
        (unknown if info is None else out).append(u)
    return out, unknown


def conflict(a, b):
    """shared source footage that counts under R2, or None. Compilations and shorties are exempt (Mack, Oct 19 final)."""
    if a.kind in ("shorty", "story", "comp") or b.kind in ("shorty", "story", "comp"):
        return None
    hit = set(a.sources) & set(b.sources)
    hit.discard(None)
    return hit or None


def candidate_report(cands, uses, mmap, now):
    """review-page gate: returns list of (label, ok, reasons, earliest_clear)"""
    out = []
    for c in cands:
        info = mmap.get(c["media"])
        if info is None:
            out.append((c["label"], False, ["UNKNOWN MEDIA - add it to the map first"], None))
            continue
        t = C_parse(c.get("time")) if c.get("time") else (now + dt.timedelta(hours=14))
        u = Use(account=c["account"], t=t, status="candidate", post_id=c["label"], caption=c["label"], media=c["media"],
                url=None, blob=None, external=False, sources=info["sources"], main=info["main"], kind=info["kind"])
        if c["media"].startswith("mackygolfs-mackthegolfer:"):
            _, u.blob = media_key("https://raw.githubusercontent.com/mack-fitz/mackygolfs-mackthegolfer/main/" + c["media"].split(":", 1)[1])
        reasons, block_until = [], t
        for o in uses:
            if o.status == "draft" or o.post_id == c["label"]:
                continue
            if u.blob and o.blob == u.blob and o.account == u.account:
                reasons.append(f"same file already on {o.account} {mt(o.t)}")
            if o.account in POOL and u.account in POOL and abs(o.t - t) < WEEK:
                hit = conflict(u, o)
                if hit:
                    reasons.append(f"{', '.join(sorted(hit))} on {o.label()}")
                    block_until = max(block_until, o.t + WEEK)
        out.append((c["label"], not reasons, reasons, None if not reasons else block_until))
    return out


def C_parse(s):
    return parse_t(s)


def check(uses, now, show_all=False):
    v = []
    uses = sorted(uses, key=lambda u: u.t)
    for i, a in enumerate(uses):
        for b in uses[i + 1:]:
            pending = a.status != "published" or b.status != "published"
            if not (pending or show_all):
                continue
            if a.status == "draft" or b.status == "draft":
                continue  # drafts don't post; they are checked when approved/scheduled
            # R1 exact duplicate (same file, same account)
            if a.blob and a.blob == b.blob and a.account == b.account and a.account != "tiktok:mackygolfs":
                v.append(("R1 exact duplicate file on one account", a, b, a.media))
                continue
            # R2 same footage
            if a.account in POOL and b.account in POOL and b.t - a.t < WEEK:
                hit = conflict(a, b)
                if hit:
                    v.append(("R2 same reel on @mackygolfs/@mackthegolfer < 7 days", a, b, ", ".join(sorted(hit))))
    return v


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--zernio", nargs="+", required=True)
    ap.add_argument("--analytics", nargs="*", default=[])
    ap.add_argument("--plan")
    ap.add_argument("--candidates")
    ap.add_argument("--days", type=int, default=14, help="look-back for published posts")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--json")
    ap.add_argument("--now")
    a = ap.parse_args()
    now = parse_t(a.now) if a.now else dt.datetime.now(dt.timezone.utc)
    mmap = json.load(open(os.path.join(CLIPS, "state", "media_sources.json")))["media"]
    since = now - dt.timedelta(days=a.days)
    uses, unknown = zernio_uses(a.zernio, mmap)
    uses = [u for u in uses if u.t >= since]
    ext, missing = external_uses(a.analytics, since) if a.analytics else ([], [])
    uses += ext
    if a.plan:
        pu, pun = plan_uses(a.plan, mmap)
        uses += pu
        unknown += pun
    if a.candidates:
        rep = candidate_report(json.load(open(a.candidates)), uses, mmap, now)
        bad = 0
        for label, ok, reasons, until in rep:
            print(("PASS " if ok else "FAIL ") + label)
            for r in reasons:
                print("   - " + r)
            if not ok:
                bad += 1
                if until:
                    print(f"   earliest clear: {mt(until)} (and re-check then)")
        sys.exit(1 if bad else 0)
    v = check(uses, now, a.all)
    print(f"checked {len(uses)} posts ({len(ext)} of Mack's own) from {mt(since)}; now {mt(now)}")
    for kind, x, y, what in v:
        fix = y if y.status != "published" else x
        gate = " (APPROVAL ACCOUNT: unschedule to draft, never swap without Mack)" if fix.account in APPROVAL else ""
        print(f"\nVIOLATION {kind}: {what}\n  earlier: {x.label()}\n  later:   {y.label()}\n  fix:     {fix.account} {mt(fix.t)}{gate}")
    for u in unknown:
        print(f"\nUNKNOWN MEDIA (add to state/media_sources.json): {u.label()}")
    for m in missing:
        print(f"\nNO FINGERPRINT for Mack's own post {m} (push fp/want_posts.tsv in mackygolfs-mackthegolfer)")
    if a.json:
        json.dump([{"rule": k, "what": w, "earlier": x.label(), "later": y.label(),
                    "fix_post": (y if y.status != "published" else x).post_id,
                    "fix_account": (y if y.status != "published" else x).account} for k, x, y, w in v],
                  open(a.json, "w"), indent=1)
    if v:
        print(f"\nFAIL: {len(v)} violation(s)")
        sys.exit(1)
    if unknown or missing:
        print("\nCANNOT VERIFY (see above)")
        sys.exit(2)
    print("\nOK: no repeats")


if __name__ == "__main__":
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    main()
