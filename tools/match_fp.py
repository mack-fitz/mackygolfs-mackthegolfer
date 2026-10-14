#!/usr/bin/env python3
"""Match fingerprints (DUPLICATE CHECK V2). Library + CLI.

  python3 tools/match_fp.py pair a.json b.json        -> overlap seconds (audio, frames)

overlap(a, b) returns {"audio_s", "audio_off_s", "frames_s", "frames_off_s", "thumb_dist"}:
  audio_s   longest run where the two chromaprints line up (bit error <= ~1/3, smoothed),
            ignoring near-constant stretches (silence / steady wind) that match anything.
  frames_s  longest run of 2-s frames whose phash is within FRAME_MAX of the other video's
            frame at one consistent time offset (+-1 s).
  thumb_dist  for thumbnail-only fingerprints: best phash distance to any frame of the other.
A source counts as ALREADY POSTED when one aligned audio stretch is > 5 s, or aligned >=3 s audio
stretches add up to >= 12 s (re-edits), or >= 8 s of changing frames line up (see PLAYBOOK).
Calibration (22 Golf Captions sources, all pairs): unrelated videos max 3.6 s single audio stretch,
9.4 s audio total, 6 s frames; every trial render matched its own source (min 11 s total).
"""
import json, sys
import numpy as np

ITEM = 0.1238
AUD_BER = 10      # mean differing bits (of 32) allowed per item, smoothed
AUD_WIN = 8
SEG_MIN = 24       # ~3 s: shortest aligned stretch counted toward the total
FRAME_MAX = 8     # phash hamming (of 64)
THRESH_S = 5.0
TOTAL_THRESH_S = 12.0  # sum of >=3 s aligned audio stretches (catches heavy re-edits); unrelated pairs max 9.4
FRAME_THRESH_S = 8.0   # 4 consecutive 2-s frames; 3 frames (6 s) false-matched two different
                       # green-polo reels from the same day in calibration

_POP = np.array([bin(i).count("1") for i in range(256)], dtype=np.uint8)

def popcount32(x):
    x = x.astype(np.uint32)
    return (_POP[x & 255] + _POP[(x >> 8) & 255] + _POP[(x >> 16) & 255] + _POP[(x >> 24) & 255]).astype(np.int16)

def _longest(mask):
    best = cur = 0; end = -1
    for i, m in enumerate(mask):
        cur = cur + 1 if m else 0
        if cur > best: best, end = cur, i
    return best, end

def audio_overlap(fa, fb):
    a = np.array(fa, dtype=np.uint64).astype(np.uint32)
    b = np.array(fb, dtype=np.uint64).astype(np.uint32)
    if len(a) < 40 or len(b) < 40:
        return 0.0, None, 0.0
    # "busy" items: the fingerprint changes from item to item (real sound, speech, impacts)
    # (smoothed: consecutive items of real audio often differ by only 1-3 bits, so a per-item
    #  test broke true matches into short runs)
    def busy(x):
        d = np.zeros(len(x), dtype=np.float32)
        d[1:] = popcount32(x[1:] ^ x[:-1])
        return np.convolve(d, np.ones(16) / 16, mode="same") >= 2.0
    ba, bb = busy(a), busy(b)
    best, best_off, segs = 0, None, []
    kern = np.ones(AUD_WIN) / AUD_WIN
    for off in range(-(len(b) - 40), len(a) - 40):
        i0, j0 = max(0, off), max(0, -off)
        n = min(len(a) - i0, len(b) - j0)
        if n < 40:
            continue
        e = popcount32(a[i0:i0 + n] ^ b[j0:j0 + n]).astype(np.float32)
        if n >= AUD_WIN:
            e = np.convolve(e, kern, mode="same")
        m = (e <= AUD_BER) & (ba[i0:i0 + n] | bb[j0:j0 + n])
        if m.sum() < SEG_MIN:
            continue
        # every aligned stretch >= SEG_MIN items at this offset (re-edits = many short segments)
        cur = 0
        for k, v in enumerate(np.append(m, False)):
            if v:
                cur += 1
            else:
                if cur >= SEG_MIN:
                    segs.append((cur, i0 + k - cur, i0 + k))
                    if cur > best:
                        best, best_off = cur, off
                cur = 0
    # total = non-overlapping (in a's timeline) aligned segments, longest first
    taken, total = [], 0
    for ln, s0, s1 in sorted(segs, reverse=True):
        if all(s1 <= t0 or s0 >= t1 for t0, t1 in taken):
            taken.append((s0, s1)); total += ln
    return (round(best * ITEM, 1), (round(best_off * ITEM, 1) if best_off is not None else None),
            round(total * ITEM, 1))

def _h(x):
    return int(x, 16)

def _ham(x, y):
    return bin(x ^ y).count("1")

def frames_overlap(fa, fb):
    """fa: list of [t, hex] (2 s step); fb: list of [t, hex] (any step, dense preferred)."""
    if len(fa) < 2 or len(fb) < 1:
        return 0.0, None
    A = [(t, _h(h)) for t, h in fa]
    B = [(t, _h(h)) for t, h in fb]
    # offsets (rounded to 1 s) at which each A frame has a close B frame
    offs = []
    for t, h in A:
        s = set()
        for tb, hb in B:
            if _ham(h, hb) <= FRAME_MAX:
                s.add(round(tb - t))
        offs.append(s)
    cand = set().union(*offs) if offs else set()
    best, best_off = 0, None
    for o in cand:
        mask = [any(abs(x - o) <= 1 for x in s) for s in offs]
        run, end = _longest(mask)
        if run <= best:
            continue
        # a static shot (sky, green, cart floor) matches itself at many offsets: only count a run
        # whose frames actually change (>= 2 visible changes between consecutive frames)
        seg = [A[i][1] for i in range(end - run + 1, end + 1)]
        changes = sum(1 for x, y in zip(seg, seg[1:]) if _ham(x, y) > 10)
        if changes < 2:
            continue
        best, best_off = run, o
    step = (A[1][0] - A[0][0]) if len(A) > 1 else 2.0
    return round(best * step, 1), best_off

def thumb_dist(thumb, fb):
    h = _h(thumb[0][1])
    return min((_ham(h, _h(x)) for _, x in fb), default=64)

def overlap(a, b):
    """a: posted reel fp; b: source fp (uses b's dense frames when present)."""
    res = {"audio_s": 0.0, "audio_off_s": None, "audio_total_s": 0.0, "frames_s": 0.0, "frames_off_s": None, "thumb_dist": None}
    fb = b.get("frames_dense") or b.get("frames") or []
    if a.get("kind") == "thumbnail":
        res["thumb_dist"] = thumb_dist(a["frames"], fb)
        return res
    if a.get("audio") and b.get("audio"):
        res["audio_s"], res["audio_off_s"], res["audio_total_s"] = audio_overlap(a["audio"]["fp"], b["audio"]["fp"])
    res["frames_s"], res["frames_off_s"] = frames_overlap(a.get("frames") or [], fb)
    return res

def is_match(r, thumb_max=4):
    if r.get("thumb_dist") is not None:
        return r["thumb_dist"] <= thumb_max
    return r["audio_s"] > THRESH_S or r.get("audio_total_s", 0) >= TOTAL_THRESH_S or r["frames_s"] >= FRAME_THRESH_S

if __name__ == "__main__":
    if sys.argv[1] == "pair":
        a, b = (json.load(open(p)) for p in sys.argv[2:4])
        r = overlap(a, b); print(json.dumps(r), "MATCH" if is_match(r) else "no")
