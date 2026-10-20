# Compilation "Macky vs. your approval" — me begging the internet to tell me I'm good at golf (new idea, Oct 20; FOR REVIEW, not posted) — id comp-validation

- Why this idea: no past comp is about her asking viewers to rate her / tell her she's good. Every bit is her fishing for approval ("I want to be a better golfer, please let me know what I'm doing wrong", "do you think I'm better or worse than an average six month old golfer?", "what am I doing wrong? please help me out", "if I bog this hopefully you'll say I'm a good golfer… well, I didn't… surely that feels pretty good, right? you let me know"). Different from guess-my-score (comp11, dropped: guessing a number) and from the other session's comp22 (invites to play): no invite lines and no guess-my-score lines are used.
- Account: **@mackygolfs** (proposed). Opens on her shirt wipe (A rule: wipe stays on @mackygolfs pieces).
- Caption: **please help, this is getting embarrassing** was used before (chipping-tip, cancelled) — so: **be honest. but also be nice** (asks for help, Oct 16 rule). Alt: "rate me. not too low".
- Video: `compilations/comp-validation_your-approval.mp4` — ~46.6 s, 4 bits, 1080x1920 30 fps, H.264 High crf 17 slow, AAC 192k 48 kHz, +faststart. ONE encode from the true originals with `tools/render_comp.py` + `COMP_FINAL_LIMIT=0.71` (bits in `comp-validation_bits.json`).
- Sources: /Golf Captions originals only, byte-for-byte relay copies (.partNN rejoined, sha256 verified; 7 34 47 single file). All already posted: 7 30 44 = @mackygolfs 2026-10-15 "fr are they poisonous" https://www.instagram.com/reel/DehF8YylZTQ/ ; 7 26 20 = @mackygolfs 2026-10-16 "six months of golf. rate me" https://www.instagram.com/reel/Dek2epXEhPv/ ; 7 34 47 = @mackthegolfer 2026-10-02 "idk something about that bandana made me…" https://www.instagram.com/reel/Dd_2QCYxGiQ/ (Mack's own). Comps are exempt from the 30-day pool rule.
- Every shot whole: bit 4 is one stretch (118.95–148.60, her own cut at 130.567 inside) — the bogey putt → miss → "Well, I didn't" → her talk over the next putt → the tap-in → "I almost missed that. But I didn't." Cuts only in quiet gaps (word timestamps + 20 ms RMS) or on her own scene cuts (7 30 44 at 5.033, 7 26 20 at 10.4, 7 34 47 at 5.767).
- Removed after the first render: the 2.7 s "surely I'm a much better girl now that I had that little impromptu lesson" line (12 11 12) — Mack said Oct 19 the San Angelo lesson footage had been posted too many times.
- No text added, no music, no speed changes.
- SPACING: green polo, cactus day (San Angelo) → white shirt + camo hat (Amarillo) → black print + white hat (Colorado) → white shirt + camo hat (same video as bit 2, different hole moment; never back to back).

## Bits (in order)
| # | out (s) | source | src in–out (s) | what |
|---|---|---|---|---|
| 1 | 0.00–4.95 | Video Oct 12 2026, 7 30 44 AM.mov | 0.00–4.95 | shirt wipe → "I'm glad I got your attention, I want to be a better golfer, please let me know what I'm doing wrong." |
| 2 | 4.95–12.49 | Video Oct 12 2026, 7 26 20 AM.mov | 2.76–10.30 | "I've been golfing for about six months now. Watch me play this par five and let me know, do you think I'm better or worse than an average six month old golfer?" |
| 3 | 12.49–16.96 | Video Oct 12 2026, 7 34 47 AM.mov | 1.15–5.62 | "I want to consistently be breaking a hundred. So what am I doing wrong? Please help me out." |
| 4 | 16.96–46.61 | Video Oct 12 2026, 7 26 20 AM.mov | 118.95–148.60 | "So if I bog this, hopefully you'll say I'm a good golfer." → putt misses → "Well, I didn't. But like I said, I'm six months into this, getting a double bogey. Surely that feels pretty good, right? Maybe, I don't know, you let me know." → tap-in → "I almost missed that. But I didn't." |

## Reuse check (every compilations/*bits*.json + notes, shorty notes, Reviewer DB)
- Not in any posted / scheduled / waiting comp or shorty. Bit 4's 119.35–139.35 was in comp7 round 1 (rebuilt from scratch; the posted comp7 r5 doesn't have it). Bit 1's wipe (0–1.1 s of 7 30 44) is wipe 13 of comp_wipes (posted on @mackygolfs Oct 13) — unavoidable, every /Golf Captions wipe is already in a wipe comp, and A pieces keep the wipe.
- The other session's comp23 uses 7 26 20 12.20–27.80 (finger wiggles); bit 2 here ends at 10.30, before it.

## Covers (3 options; text off her chest and face, inside the grid crop; checked full + grid size)
1. `comp-validation_your-approval_cover_opt1.jpg` — @0.4 s shirt-wipe frame in the cart, red pill "Macky vs. your approval" over her hair/cart roof, above the face (0.14–0.19)
2. `comp-validation_your-approval_cover_opt2.jpg` — @13.5 s big grin "I wanna consistently be breaking 100", typewriter "please tell me i'm good at golf" above her cap (0.13–0.19)
3. `comp-validation_your-approval_cover_opt3.jpg` — @44.85 s picking the ball out of the cup, purple pill in the trees (0.22–0.27)
