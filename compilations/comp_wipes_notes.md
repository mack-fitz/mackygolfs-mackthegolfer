# Compilation — "what it's like golfing with me in the summer" (@mackygolfs, FOR REVIEW, not posted)

- Account: **@mackygolfs** (the shirt-wipe compilation, per PLAYBOOK idea #5)
- Video: `compilations/comp_wipes_mackygolfs.mp4` — 22.4 s, 14 shirt wipes, 1080x1920, 30 fps, H.264 crf 17 preset slow, AAC 192k, +faststart
- Cover text: "what it's like golfing with me in the summer" (white Poppins Bold on a rounded box, mid-frame, like comp1 / her grid)
- Caption: sorry I'm so wet
- Review page: https://claude.ai/artifact/KFJoqNkDr6kpxYDkpniAZ7 → collection `compilations`, doc `comp_wipes` (round 1)

## Method
- Sources: ONLY Mack's true originals from Dropbox `/Golf Captions` (byte sizes match Dropbox; .partNN pieces rejoined with `cat`, sha256 verified). 11 fetched via the relay (`inbox/want.txt`) for this job. No clips-repo queue copies.
  Some originals are naturally under 8 Mbps (7 33 50–7 38 06, Oct 11 .mp4s at 7–8 Mbps landscape-tagged with −90° rotation) — they are the untouched Dropbox files, not shrunk copies.
- Each wipe starts at 0.0 s of the original (her videos open mid-lift) and ends just before her first spoken word (cut at the quietest 20 ms window near speech onset, frame-aligned), so no words are clipped. Picked from fps-4 contact sheets of the first 3.5 s.
- Audio: each clip keeps its own sound; per-clip gain to a common level (louder half of 50 ms windows → −30 dBFS, ±12 dB cap), 20/30 ms fades at every cut, then +11 dB, limiter (0.45), loudnorm I=−16 linear 2-pass → −15.9 LUFS integrated.
- No text burned in (her own captions appear in a few clips), no speed changes, no music.

## Wipes (in order)
| # | out (s) | source (Golf Captions original) | src in–out (s) | outfit / place |
|---|---|---|---|---|
| 1 | 0.00–1.63 | Video Oct 11 2026, 9 02 57 AM (2).mp4 | 0.000–1.633 | orange checker, storm sky (opener, big smile) |
| 2 | 1.63–3.70 | Video Oct 12 2026, 12 17 30 AM.mov | 0.000–2.067 | green polo, sunny trees |
| 3 | 3.70–5.67 | Video Oct 12 2026, 7 13 58 AM.mov | 0.000–1.967 | white shirt, camo hat, golden field |
| 4 | 5.67–7.17 | Video Oct 12 2026, 7 38 06 AM.mov | 0.000–1.500 | light blue print, navy hat |
| 5 | 7.17–8.93 | Video Oct 12 2026, 7 35 57 AM.mov | 0.000–1.767 | black print, white hat |
| 6 | 8.93–10.10 | Video Oct 12 2026, 12 00 30 AM.mov | 0.000–1.167 | blue striped polo, rainy |
| 7 | 10.10–11.53 | Video Oct 12 2026, 12 11 12 AM.mov | 0.000–1.433 | green polo, San Angelo |
| 8 | 11.53–13.50 | Video Oct 12 2026, 7 19 40 AM.mov | 0.000–1.967 | white shirt, camo hat |
| 9 | 13.50–15.23 | Video Oct 11 2026, 9 02 57 AM (3).mp4 | 0.000–1.733 | orange checker, dry field |
| 10 | 15.23–16.70 | Video Oct 12 2026, 12 14 03 AM.mov | 0.000–1.467 | green polo |
| 11 | 16.70–18.33 | Video Oct 12 2026, 7 37 01 AM.mov | 0.000–1.633 | black print, white hat |
| 12 | 18.33–19.83 | Video Oct 12 2026, 7 16 02 AM.mov | 0.000–1.500 | white shirt, camo hat |
| 13 | 19.83–20.93 | Video Oct 12 2026, 7 30 44 AM.mov | 0.000–1.100 | green polo |
| 14 | 20.93–22.43 | Video Oct 12 2026, 7 34 47 AM.mov | 0.000–1.500 | black print, white hat (closer, smile) |

Not used (spares for swaps): 9 02 57 AM.mp4 and (1).mp4 (orange checker again), 12 03 20, 12 05 56, 12 22 39 (green polo), 7 17 58, 7 26 20 (white/camo), 7 33 50 (light blue; windy audio).

## Covers (3 options, all shirt-wipe frames)
1. `comp_wipes_cover_opt1.jpg` — (2).mp4 @ 0.7 s, eyes over the orange checker shirt, blue #1E90FF box
2. `comp_wipes_cover_opt2.jpg` — 7 13 58 AM.mov @ 0.9 s, white shirt + camo hat, orange #F7931E box
3. `comp_wipes_cover_opt3.jpg` — 12 17 30 AM.mov @ 1.0 s, green polo, orange #F7931E box
