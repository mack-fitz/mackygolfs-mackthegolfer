# Compilation 2 — "what it's like being delusional" (FOR REVIEW, not posted)

- Video: `compilations/comp2_delusional.mp4` — 37.5 s, 1080x1920, 30 fps, H.264 crf 17 preset slow, AAC 192k 48 kHz, +faststart
- SOURCE QUALITY: every bit is cut from Mack's true originals (inbox/videos, Dropbox /Golf Captions, rejoined from .partNN with sha256 OK). Source video bitrates: 7 13 58 AM.mov 10.3 Mbps, 7 16 02 AM.mov 11.1 Mbps, 12 03 20 AM.mov 10.8 Mbps, Oct 11 9 02 57 AM (3).mp4 7.7 Mbps (that's the Dropbox original itself — her phone export of that clip is 7.7 Mbps; nothing better exists). Nothing from clips/queue or trial edits.
- Covers (white Poppins Bold on a rounded box, mid-frame, same layout as comp 1):
  - `comp2_delusional_cover.jpg` — main: "and yet now I'm in the sand" deadpan close-up (Video Oct 12 2026, 12 03 20 AM.mov @ 54.0 s), orange #F7931E
  - `comp2_delusional_cover_alt1.jpg` — the confidence: "I'm normally pretty good with a pitching wedge" (Video Oct 11 2026, 9 02 57 AM (3).mp4 @ 32.8 s), blue #1E90FF
  - `comp2_delusional_cover_alt2.jpg` — "so as it turns out I'm pissed" close-up (Video Oct 12 2026, 7 16 02 AM.mov @ 120.7 s), orange #F7931E
- Audio: per-bit gain to even levels (bit 1 −1.9, 2 +11, 3 −2.2, 4 −0.6 dB), soft limiter, then loudnorm I=-16 (linear, measured 2-pass) → −15.9 LUFS integrated, peak −2.2 dBFS
- No text added to the video; Mack's own captions untouched. No shirt wipes. No swearing cut. Every bit keeps her confident line + the full shot + the result/reaction. Cuts only at measured quiet gaps (0.1 s windows at 48 kHz / asetnsamples=4800, checked at 20 ms), and moved off scene changes so no stray frames.
- Moments found by OCR of Mack's burned-in captions (tesseract, fps 3) across all inbox originals + clips/queue + trials (clips/trials only used to find moments, then located in the originals by audio cross-correlation).
- Bits run 7–13 s (longer than comp 1's 2–7 s) because each one has to carry the shot and the ball flight, not just a reaction.
- Punch-ins (1.15): on the reaction in bit 1, on the setup line in bits 2 and 3, on the reaction in bit 4.
- None of comp 1's bits reused. Two bits end on "and yet" (open + close), on purpose.

## Suggested caption
confidence is free

## Bits (in order)
| # | out (s) | source (mackygolfs-mackthegolfer/inbox/videos, originals) | source in–out (s) | framing | confident line → result (her captions) |
|---|---|---|---|---|---|
| 1 | 0.00–7.95 | Video Oct 12 2026, 7 13 58 AM.mov | 39.35–47.30 | full, punch-in 1.15 from 46.0 | "alright we've got literally no excuse not to be on the green in three" → shanks it right (tracer) → "and yet" |
| 2 | 7.95–15.39 | Video Oct 11 2026, 9 02 57 AM (3).mp4 | 32.47–36.10 + 40.50–44.31 | punch-in on setup, then full | "I'm normally pretty good with a pitching wedge / should be able to get us pretty close" → pitch → "no f*cking way" (cut: "and then hopefully just a little bump and roll") |
| 3 | 15.39–24.11 | Video Oct 12 2026, 7 16 02 AM.mov | 110.59–117.48 + 120.07–121.90 | punch-in on setup to 113.51, then full | "I'm actually gonna be pissed if we're not on in 4 to be honest" → chip → "so as it turns out I'm pissed" (cut: picking up the camera) |
| 4 | 24.11–37.48 | Video Oct 12 2026, 12 03 20 AM.mov | 21.03–29.40 + 50.00–55.00 | full, then punch-in 1.15 | "anyway let's drive the green why not" → drive (tracer to landing) → "I thought it was like one of the best drives of my life / and yet now I'm in the sand" (cut: walk-up + heat talk) |

## Cut from this version (good swaps if she wants one)
- Galaxy putter: Video Oct 12 2026, 12 05 56 AM.mov ~102.3–107.9 "it's fortunate that I'm one of the best putters that this galaxy has ever seen, so actually won't be a problem" → putt ~120.7 → "[didn't] get all the way there" ~126.5 (adds ~11 s; dropped to stay under 45 s)
- Skull: "as long as I don't skull this across the green" → "and yet that's exactly what I did" (clips/queue/012_great-drive_full.mp4 20.95–30.97) — no Dropbox original for it, so not usable under the true-originals rule
- 12 03 20 AM.mov 30.7–32.3 "genuinely almost drove the green" (right after bit 4's drive); 85.0 "I've got to pop it over this tree" → 94.3 "well it technically did go over the tree but then it fell down the right side"; 155.3 "get a double get a double" → 159.0 "oh it lipped / freaking lipped"

## Other delusional moments found (not used, for swaps)
- 015_hole-in-one-attempt_full 1.4–3.0 "watch this hole in one" → shot 21–23 → 31.0–34.3 "well wasn't quite a hole in one but maybe next time" (needs the 3.0→20.8 setup trimmed; practice swing joke at 11.5–15 "that wasn't the hole in one / glad I got it out of my system")
- 003_guess-my-score_full 36.0–47.3 putt → "that's gonna be good x3 / real freaking good" → "I might have blocked that entire shot but just know that it was perfect"
- 009_six-months-par-5 (trials _a) 119.0–134.9 "so if I bog this hopefully you'll say I'm a good golfer" → miss → "I'm six months into this getting a double bogey, surely that feels pretty good right"
- 006_hole-in-one-loading_b 2.3 "I'm getting a hole in one on this" … 30.3 "you ready for this" → 38.7 "it's gonna be a little left" / "about 40 yards past it"
- 007_found-the-trees_b 119.0 "you're about to see the lag MASTA at work" → 125.0 "maybe the lag mister took the day off after all"
- 009_new-shirt_full 27.0 "lag her up there and get a nice par tap in" → 40.3 "let's try this again"
- Video Oct 12 2026, 12 22 39 AM.mov 61.4–69.9 "don't hit this tree above you Mack" → "well I hit the tree"
- Video Oct 12 2026, 12 17 30 AM.mov 9.3–33 "it's literally such a straight shot" → "I'm about as straight as it gets / that was a joke by the way"
- 013_cliff-par-5_full 22.7 "just gotta get this up and over this bunker" → 29.7 "truly terrible"
