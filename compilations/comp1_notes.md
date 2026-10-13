# Compilation 1 — "what it's like playing with me" (FOR REVIEW, not posted)

- Video: `compilations/comp1_playing-with-me.mp4` — 38.2 s (container 38.3 s), 1080x1920, 30 fps, H.264 crf 17 preset slow, AAC 192k, +faststart
- Cover: `compilations/comp1_playing-with-me_cover.jpg` — "another stupid bounce" face frame (007_ugly-bounce_full.mp4 @ 39.0 s), red #E8101A rounded box, white Poppins Bold, mid-frame
- Audio: per-bit gain to even levels, soft limiter, then loudnorm I=-16 (linear, measured 2-pass) → −15.9 LUFS integrated
- No text added to the video; Mack's own captions untouched. No shirt wipes. No swearing cut (all cuts at measured quiet gaps, 20 ms RMS check).
- Moments found by OCR of Mack's burned-in captions (tesseract, fps 3) + 0.1 s loudness windows (48 kHz, 4800 samples).

## Suggested caption
golf is so relaxing guys

## Bits (in order)
| # | out (s) | source | source in–out (s) | framing | what she says (her caption) |
|---|---|---|---|---|---|
| 1 | 0.00–6.84 | clips/queue/007_ugly-bounce_full.mp4 | 18.36–25.20 | full frame, punch-in 1.15 | ugly ugly ugly bounce, no / cause i'm actually so pissed about this damage control i have to do because of that f*cking bounce |
| 2 | 6.84–11.53 | clips/queue/002_beach-day_full.mp4 | 46.40–51.09 | full frame | stop stop stop stop ... motherf*cker. alright |
| 3 | 11.53–13.38 | mackygolfs-mackthegolfer/inbox/videos/Video Oct 12 2026, 12 22 39 AM.mov (rejoined from .partNN) | 109.95–111.80 | punch-in 1.15 | and f*ck that marshall by the way |
| 4 | 13.38–18.61 | mackygolfs-mackthegolfer/inbox/videos/Video Oct 12 2026, 12 17 30 AM.mov (rejoined from .partNN) | 154.62–159.85 | full frame | triple dipper motherf*cker / guess i'm not getting a trip dip / don't even care anymore actually |
| 5 | 18.61–20.76 | clips/queue/002_beach-day_full.mp4 | 62.10–64.25 | punch-in 1.15 | motherf*cking christ |
| 6 | 20.76–26.96 | mackygolfs-mackthegolfer/inbox/videos/Video Oct 12 2026, 12 22 39 AM.mov (rejoined from .partNN) | 33.10–39.30 | full frame, punch-in 1.15 | what was that / gotta stop talking or thinking or breathing while i hit the ball |
| 7 | 26.96–29.31 | clips/queue/016_help-my-swing_full.mp4 | 52.85–55.20 | full frame | f*ck the texas wedge |
| 8 | 29.31–31.66 | clips/queue/007_ugly-bounce_full.mp4 | 37.85–40.20 | punch-in 1.15 | another stupid bounce |
| 9 | 31.66–34.46 | mackygolfs-mackthegolfer/inbox/videos/Video Oct 12 2026, 12 17 30 AM.mov (rejoined from .partNN) | 162.30–165.10 | full frame | genuinely this is actually getting so embarrassing |
| 10 | 34.46–38.24 | clips/queue/003_guess-my-score_full.mp4 | 81.22–85.00 | punch-in 1.15 | and if any of you guessed higher than par you are my enemy |

Inbox file `Video Oct 12 2026, 12 17 30 AM.mov` / `12 22 39 AM.mov` are originals rejoined with `cat .partNN` (sha256 verified).

## Other angry moments found (not used, for swaps)
- 001_perfect-perfect-bogey_full 6.7–8.3 "let's hope i don't f*ck it up"; 20.0–24.3 "you can either send it or you can be a p*ssy"
- 002_beach-day_full 77.3–79.0 "and that's what pisses me off"
- 007_ugly-bounce_full 26.3–28.0 "who put those rocks there"
- 010_wrong-clubs_full 42.3–43.7 "no f*cking way" (quiet mutter)
- 012_great-drive_full 44.3–47.3 "hate to see a great drive turn into a triple"
- Video Oct 12 2026, 12 22 39 AM.mov 4.7–6.3 "i know i'm gonna be pissed with this yellow box"; 159.0–161.3 "and f*ck that marshall"
- Video Oct 12 2026, 7 17 58 AM.mov 14.3–19.7 "anybody who guesses above one looks like an absolute asshole"; 88.7–92.3 "the motherf*cking lag master"
- Video Oct 12 2026, 12 17 30 AM.mov 165.3–169.8 "have to get this in or... somebody's in big trouble"

## Round 2 (Oct 13) — Mack: "Give me more cover photo options. The text is fine. Change caption to: why do I like this sport"
- Caption → **why do I like this sport**
- Cover options (same red box/text pasted pixel-exact from option 1; frames taken from the compilation itself):
  1. `comp1_playing-with-me_cover.jpg` — "another stupid bounce" (original)
  2. `comp1_cover_opt2.jpg` — comp @ 5.97 s, snarl on "that f*cking bounce" (bit 1)
  3. `comp1_cover_opt3.jpg` — comp @ 28.00 s, exasperated selfie on "f*ck the texas wedge" (bit 7)
  4. `comp1_cover_opt4.jpg` — comp @ 37.17 s, pointing at camera, "you are my enemy" (bit 10)
  5. `comp1_cover_opt5.jpg` — comp @ 35.17 s, glare into camera, "if any of you guessed higher than par" (bit 10)

## Full-quality rebuild (Oct 13) — sources swapped to Mack's true originals, edit unchanged
- Bits 1, 2, 5, 7, 8, 10 were cut from clips/queue/*_full.mp4 (~4–6 Mbps re-encodes). Now cut from the byte-exact Dropbox /golfclips originals (sha256 verified against relay .sha256 / Dropbox size):
  - 007_ugly-bounce → IMG_6391.MP4 (H.264, 8.5 Mbps; relayed in clips@654e995)
  - 002_beach-day → copy_2CC073A6-0417-450E-A364-BDCE638A2D66.MOV (HEVC, 11.2 Mbps; clips@f36a504)
  - 016_help-my-swing → copy_A526847D-927A-4E66-BA6A-83EF27833CEC.MOV (HEVC, 11.1 Mbps; clips@654e995)
  - 003_guess-my-score → copy_0B6BFBE5-2F81-487A-9544-B2C587E0EE74.MOV (HEVC, 11.2 Mbps, slight VFR; clips@f36a504)
  - Bits 3, 4, 6, 9 unchanged (inbox .mov originals rejoined, 10.7 Mbps).
- Alignment: every comp frame matched to its source frame (54x96 gray MSE, full + 1.15 punch-in candidates); originals share the _full timeline exactly (0-frame offset, audio x-corr offsets identical), so in/out times above stand. Frame-exact source windows used (first/last source frame per bit; punch-in switches at src 21.40 s in bit 1 and 34.367 s in bit 6).
- Audio: same per-bit gains (fitted to the old mix, corr 0.996–0.9999 per bit), alimiter, loudnorm 2-pass linear → −16.0 LUFS, TP −5.0, LRA 4.2 (old: −15.97 / −4.98 / 4.20). Whole mix sits 3 ms earlier than the old file (inaudible).
- Check vs previous file: 1149/1149 frames, per-frame MSE max 1.65 (encode noise only); contact sheets identical. New file: 1080x1920, 30 fps, H.264 High crf 17 slow, 12.9 Mbps, AAC 192k, +faststart, 38.32 s. Covers unchanged.
