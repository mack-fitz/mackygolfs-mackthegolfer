#!/usr/bin/env python3
"""Build the JSON files the two trial dashboards read.

  python3 tools/dash_trials.py trials A out/trials_a.json    # from state/trials.json
  python3 tools/dash_trials.py trials B out/trials_b.json
  python3 tools/dash_trials.py upnext A zernio_posts.txt out/upnext_a.json
  python3 tools/dash_trials.py upnext B zernio_posts.txt out/upnext_b.json

`zernio_posts.txt` is the raw answer of Zernio posts_list_posts for that account's profile
(profile_id, limit 50, sort_by "scheduled-asc"), saved as-is (JSON or Python-dict text).
"""
import ast
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent.parent
MT = ZoneInfo("America/Denver")
ACCOUNTS = {
    "A": {"handle": "mackygolfs", "account": "6acce837f3bd55021dad245f", "profile": "6acce3f0662265cf261fca4a"},
    "B": {"handle": "mackthegolfer", "account": "6accea22c485191e985aa1cb", "profile": "6acce6402daf1733722343d0"},
}


def cover_test(v):
    if v is None:
        return "not recorded"
    if isinstance(v, str):
        return "no words" if v.strip().lower() in ("", "none", "no", "false") else "words"
    return "words" if v else "no words"


def opening_test(v):
    if not v:
        return "not recorded"
    s = str(v).lower()
    if s.startswith("teaser") or "teaser" in s.split(" then ")[0]:
        return "teaser-first"
    if s.startswith("talk") or "spoken" in s or "first line" in s:
        return "talk-first"
    return "not recorded"


def trials(arm, out):
    data = json.loads((ROOT / "state/trials.json").read_text())
    rows = []
    for fid, reel in data.get("reels", {}).items():
        v = reel.get(arm)
        if not v or not v.get("zernio"):
            continue
        row = {
            "zernio_post_id": v["zernio"],
            "slug": reel.get("slug", ""),
            "caption": v.get("caption", ""),
            "posted_mt": v.get("posted", ""),
            "version": v.get("version", ""),
        }
        if arm == "A":
            row["cover_words"] = v.get("cover_words") if isinstance(v.get("cover_words"), str) else ""
            row["cover_test"] = cover_test(v.get("cover_words"))
        else:
            row["opening"] = v.get("opening", "")
            row["opening_test"] = opening_test(v.get("opening"))
        rows.append(row)
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    Path(out).write_text(json.dumps(rows, indent=1))
    print(f"{len(rows)} trial rows -> {out}")


def parse(text):
    text = text.strip()
    try:
        a = json.loads(text)
    except ValueError:
        a = ast.literal_eval(text)
    if isinstance(a, dict) and isinstance(a.get("result"), str):
        return parse(a["result"])
    return a


def upnext(arm, src, out):
    acc = ACCOUNTS[arm]
    a = parse(Path(src).read_text())
    now = datetime.now(timezone.utc)
    rows = []
    for p in a.get("posts", []):
        if p.get("status") != "scheduled":
            continue
        for pl in p.get("platforms", []):
            aid = pl.get("accountId")
            aid = aid.get("_id") if isinstance(aid, dict) else aid
            if aid != acc["account"]:
                continue
            when = datetime.fromisoformat(str(pl.get("scheduledFor") or p["scheduledFor"]).replace("Z", "+00:00"))
            if when <= now:
                continue
            mt = when.astimezone(MT)
            media = (p.get("mediaItems") or [{}])[0]
            rows.append({
                "when": when.strftime("%Y-%m-%dT%H:%M:%SZ"),
                "when_mt": mt.strftime("%a %b %-d · %-I:%M") + mt.strftime("%p").lower(),
                "slot": "morning" if mt.hour < 12 else "midday" if mt.hour < 17 else "evening",
                "clip": p["_id"],
                "caption": p.get("content", ""),
                "hook": "",
                "where": "IG trial reel · @" + acc["handle"],
                "thumb": "",
                "ig_url": media.get("url", ""),
                "full_url": "",
                "note": "" if media.get("instagramThumbnail") else "no custom cover",
            })
    rows.sort(key=lambda r: r["when"])
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    Path(out).write_text(json.dumps(rows, indent=1, ensure_ascii=False))
    print(f"{len(rows)} scheduled -> {out}")


if __name__ == "__main__":
    kind, arm = sys.argv[1], sys.argv[2].upper()
    if kind == "trials":
        trials(arm, sys.argv[3])
    else:
        upnext(arm, sys.argv[3], sys.argv[4])
