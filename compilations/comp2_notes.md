# Compilation 2 — "what it's like being delusional" (FOR REVIEW, not posted)

- Video: `compilations/comp2_delusional.mp4` — 45.5 s (container 45.6 s), 1080x1920, 30 fps, H.264 crf 17 preset slow, AAC 192k 48 kHz, +faststart
- Covers (white Poppins Bold on a rounded box, mid-frame, same layout as comp 1):
  - `comp2_delusional_cover.jpg` — main: wide-eyed "as long as I don't skull this across the green" (012_great-drive_full.mp4 @ 21.8 s), orange #F7931E
  - `comp2_delusional_cover_alt1.jpg` — the regret: crouched grin, "and yet that's exactly what I did" (012_great-drive_full.mp4 @ 29.2 s), blue #1E90FF
  - `comp2_delusional_cover_alt2.jpg` — "so as it turns out I'm pissed" close-up (trials/007_found-the-trees_b.mp4 @ 117.5 s), orange #F7931E
- Audio: per-bit gain to even levels (bit 1 −1.9, 2 +11, 3 −5.1, 4 −2.2, 5 +10 dB), soft limiter, then loudnorm I=-16 (linear, measured 2-pass) → −15.8 LUFS integrated, peak −2.0 dBFS
- No text added to the video; Mack's own captions untouched. No shirt wipes. No swearing cut. Every bit keeps her confident line + the full shot + the result/reaction. Cuts only at measured quiet gaps (0.1 s windows at 48 kHz / asetnsamples=4800, checked at 20 ms), and moved off scene changes so no stray frames.
- Moments found by OCR of Mack's burned-in captions (tesseract, fps 3) across clips/queue/*_full.mp4, inbox/videos (rejoined .partNN, sha256 OK) and trials/.
- Punch-ins (1.15) alternate: on the reaction in bits 1, 3, 5; on the setup line in bits 2, 4.
- None of comp 1's bits reused.

## Suggested caption
confidence is free

## Bits (in order)
| # | out (s) | source | source in–out (s) | framing | confident line → result (her captions) |
|---|---|---|---|---|---|
| 1 | 0.00–7.95 | mackygolfs-mackthegolfer/inbox/videos/Video Oct 12 2026, 7 13 58 AM.mov (rejoined) | 39.35–47.30 | full, punch-in 1.15 from 46.0 | "alright we've got literally no excuse not to be on the green in three" → shanks it right (tracer) → "and yet" |
| 2 | 7.95–15.39 | clips/queue/010_wrong-clubs_full.mp4 | 32.47–36.10 + 40.50–44.31 | punch-in on setup, then full | "I'm normally pretty good with a pitching wedge / should be able to get us pretty close" → pitch → "no f*cking way" (cut: "and then hopefully a little bump and roll") |
| 3 | 15.39–26.80 | mackygolfs-mackthegolfer/trials/002_guess-my-score_b.mp4 | 103.33–108.69 + 121.75–127.80 | full, punch-in 1.15 from 124.2 | "it's fortunate that I'm one of the best putters that this galaxy has ever seen, so actually won't be a problem" → putt → "[didn't] get all the way there" (cut: dragonfly + "you're about to see…") |
| 4 | 26.80–35.52 | mackygolfs-mackthegolfer/trials/007_found-the-trees_b.mp4 | 107.38–114.27 + 116.86–118.69 | punch-in on setup to 110.3, then full | "I'm actually gonna be pissed if we're not on in 4 to be honest" → chip → "so as it turns out I'm pissed" (cut: picking up the camera) |
| 5 | 35.52–45.54 | clips/queue/012_great-drive_full.mp4 | 20.95–30.97 | full, punch-in 1.15 from 28.0 | "as long as I don't skull this across the green, we should be in a pretty OK position" → skulls it → "and yet that's exactly what I did" |

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
