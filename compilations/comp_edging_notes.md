# Compilation — "is this edging?" (@mackygolfs, FOR REVIEW, not posted)

- Account: **@mackygolfs** (A, Zernio account 6acce837f3bd55021dad245f). NOT for @mackthegolfer (B stays clean).
- Video: `compilations/comp_edging_mackygolfs.mp4` — 47.5 s, 6 bits, 1080x1920, 30 fps, H.264 High crf 17 preset slow (10.4 Mbps), AAC 192k 48 kHz, +faststart (moov first). One encode straight from the originals with `tools/render_comp.py` (bits in `comp_edging_bits.json`).
- Topic: her putts that get REALLY close — lip-out, inches short at the cup, putts that slide by, "blue ball lagged right on up to the edge of the hole… not quite going in yet".
- Cover text: **is this edging?** (white Poppins Bold on one rounded color box, mid-frame ~57% down, like comp4 / her grid). 4 options.
- Caption: **it definitely makes things last longer**
- Proposed slot: **Mon Oct 19, 6:47pm MT (7:47pm CT), @mackygolfs evening trial slot.** First A slot that is 3+ days clear of the same footage elsewhere (B posts the orange-checker "perfect perfect bogey" re-edit = `9 02 57 AM (1)` on Oct 15 pm; A/B Oct 14–16 reels use 7 13 58 / 7 38 06 footage earlier in the week). Waiting on Mack's approval; nothing created in Zernio.
- Review page: https://claude.ai/artifact/KFJoqNkDr6kpxYDkpniAZ7 → collection `compilations`, doc `comp_edging` (round 1).

## Method
- Sources: ONLY Mack's true originals from Dropbox `/Golf Captions`, already relayed byte-for-byte into `inbox/videos/` (.partNN rejoined with `cat`, sha256 verified against the relay `.sha256`). Oct 11 `.mp4`s are the Dropbox files themselves (7.0–7.6 Mbps landscape-tagged, rotated); `7 38 06` is the untouched 6 Mbps Dropbox original (no re-encoded copies used).
- Finding the putts: OCR of her burned-in captions over all 24 originals (2 fps, white-text + dark-outline mask, tesseract) searched for putt words (lip, edge, get in, break, lag, short, putt…), then 2–6 fps contact sheets of every candidate and 0.1 s / 20 ms loudness maps for her reactions and cut points.
- Every bit keeps the whole putt from the stroke until the ball stops (or, in bit 6, until she turns away from it — her camera never follows the ball there), plus her reaction. No putt or shot is cut. No swearing cut ("doesn't freaking matter" kept). Cuts at measured quiet points and on her own scene cuts (frame-diff checked; one stray frame at the 7 38 06 join found and fixed by ending 2 frames earlier).
- Punch-ins (1.15): lip-out reaction, the putter-kick, the "that is why she's blue boys" putt (also hides the one internal cut in bit 6).
- Audio: per-bit gain to −18 LUFS (far-camera bits 2 and 5 lifted +5 dB more so "get in there" is clear; the windy no-talk low-angle bit 3 pulled down 10 dB), 20/30 ms fades at jumps, alimiter, loudnorm 2-pass linear → **−16.1 LUFS, peak −1.3 dBFS**. Each clip keeps its own sound; no music (no earlier comp used music).
- No text burned in (her own captions untouched). No speed changes. No shirt wipes.
- Outfits alternate: green pinstripe → orange checker → light blue print → dark green → orange checker → white shirt/camo hat (no same shirt back to back).
- No bits from comp1–4 reused (comp4's driver putt and "break in break in", comp2's galaxy putt all skipped).

## Bits (in order)
| # | out (s) | source (Golf Captions original) | src in–out (s) | what happens |
|---|---|---|---|---|
| 1 | 0.00–6.47 | Video Oct 12 2026, 12 03 20 AM.mov (green pinstripe) | 155.45–161.92 (punch-in from 157.10) | "get a double, get a double" → putt → hand over mouth → "oh it lipped… freaking lipped" |
| 2 | 6.47–13.41 | Video Oct 11 2026, 9 02 57 AM.mp4 (orange checker) | 29.40–36.34 | long putt from the far camera, "get in there" → stops a few feet short → tap, "get in" |
| 3 | 13.41–21.72 | Video Oct 12 2026, 7 38 06 AM.mov (light blue print) | 18.17–26.48 | long putt, body-English lean → low camera at the cup: ball rolls up and stops inches from the hole while she crouches in the background |
| 4 | 21.72–29.07 | Video Oct 12 2026, 12 05 56 AM.mov (dark green) | 141.60–148.95 (punch-in from 145.00) | "…at this bogey / should not speak while putt— oh" → slides by → kicks her leg and drops the putter → "doesn't freaking matter" |
| 5 | 29.07–36.82 | Video Oct 11 2026, 9 02 57 AM (1).mp4 (orange checker) | 41.70–49.45 (her own cut to selfie at 46.53) | short putt, "get in there" → misses, frozen squat by the flag → "that is a tough bog after two incredibly perfect shots" |
| 6 | 36.82–47.35 | Video Oct 12 2026, 7 13 58 AM.mov (white shirt, camo hat) | 62.42–66.45 + 69.00–75.50 (punch-in) | "blue ball lagged right on up to the edge of the hole / not quite going in yet" → the lag → watches it → "and that is why she's blue boys" (cut: the pre-putt "that's why she's blue" so the line lands once, after the putt) |

Length note: 47.5 s, a little over the 45 s aim — six bits was the floor and none of them can lose more without cutting a putt or a reaction. To get under 45: drop bit 5 (→ 39.8 s).

## Covers ("is this / edging?", white Poppins Bold, one rounded box, mid-frame)
1. `comp_edging_cover_opt1.jpg` — comp @ 2.3 s, hand over mouth after the lip-out, red #E8101A
2. `comp_edging_cover_opt2.jpg` — comp @ 21.4 s, ball sitting inches from the cup (low angle), purple #A21CAF
3. `comp_edging_cover_opt3.jpg` — comp @ 26.4 s, the putter-kick, blue #1E90FF
4. `comp_edging_cover_opt4.jpg` — comp @ 34.8 s, orange-checker grin, orange #F7931E

## Other near-misses found (swaps / later)
- Video Oct 12 2026, 12 11 12 AM.mov 160.85–173.3 "you're about to see the lag putt of the century" → lag → "you ever seen a lag putt that good, don't think so" → ball inches from the cup, tap "boom" (12.5 s; cut for length; same footage as B's Lucy Goosey re-edit Oct 15)
- Video Oct 12 2026, 7 17 58 AM.mov 75.5–95 lag → "that's gonna break right" → "that's why they call me the motherf*cking lag master" → "nothing but a tap in bog" (A posts this footage Oct 15)
- Video Oct 12 2026, 7 16 02 AM.mov 122–140.5 "lag MASTA at work" → "took the day off after all" → second lag "now that was a lag" → "lunch break" → tap "boom"
- Video Oct 11 2026, 9 02 57 AM (2).mp4 29.5–40 lag "get up there get up there" → stops short → crouch → "let's try this again"
- Video Oct 12 2026, 7 13 58 AM.mov 76–92 the blue-ball tap-in ("let's just tap this in and call it a day boys", "tweener between the legs")
- Used elsewhere, skipped: 7 19 40 "break in break in" (comp4), 9 02 57 AM (3) driver putt (comp4), 12 05 56 galaxy putt (comp2), 12 14 03 8-footer (it went in).


## Round notes IN PROGRESS (Oct 14, 17:02–, still working at 17:31 UTC, :47 review-check run) — another run: skip this one
