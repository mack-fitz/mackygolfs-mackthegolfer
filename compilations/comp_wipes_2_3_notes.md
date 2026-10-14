# Shirt-wipe compilations 2 and 3 (@mackygolfs, for Mack to upload herself; NOT posted, NOT scheduled, NOT in The Reviewer)

- Videos (public download, mack-fitz/clips `downloads/`):
  - `shirt-wipe-comp-2.mp4` — 15.67 s, 10 shirt wipes, cover `shirt-wipe-comp-2_cover.jpg`
  - `shirt-wipe-comp-3.mp4` — 16.70 s, 10 shirt wipes, cover `shirt-wipe-comp-3_cover.jpg`
  - Both 1080x1920, 30 fps, H.264 High crf 17 preset slow, AAC 192k 48 kHz, +faststart. Comp 2: −15.9 LUFS, peak −1.3 dBFS. Comp 3: −16.0 LUFS, peak −1.4 dBFS.
- Covers: clean frames, no text. Comp 2 = wipe 1 (copy_2A97DD30…) @ 0.70 s, eyes over the shirt, blue sky. Comp 3 = wipe 1 (copy_6FFD8A7C…) @ 0.70 s, eyes over the shirt, pines.
- Built by copying `comp_wipes_notes.md` exactly (method below). Renderer: `tools/render_wipes.py` + `compilations/comp_wipes_2_3.json`.

## Clip pool / no-overlap rule
- Excluded: all 14 sources of `comp_wipes_mackygolfs.mp4`, plus their byte-identical copies in `/golfclips` (`Video Aug 27 2026, 5 43 32 PM.MP4` = 9 02 57 AM (2).mp4, `5 49 54 PM.MP4` = (3).mp4). `5 51 18 PM.MP4` is the same file as Golf Captions `9 02 57 AM.mp4`, so it counts once (used in comp 2 under its Golf Captions name).
- Remaining distinct clips: 8 in `/Golf Captions` + 12 in `/golfclips` = 20. All 20 open on the shirt wipe (fps-4 contact sheets of the first 3.5 s), so each comp got 10 and they share nothing. Frame-fingerprint check (27x48 gray MSE at 2/4/6 s, all ≥1790 vs <100 for a true duplicate) confirmed none of the 20 is a re-export of a comp_wipes source or of each other.
- That is every wipe clip available, so 10 per comp (~16–17 s) is the maximum without reusing a clip; the 10–14 / 20–30 s target can't be met until more wipe clips land in Dropbox.

## Method (same as comp_wipes)
- Sources: ONLY Mack's true originals. Golf Captions files from the existing `inbox/videos` relay copies (.partNN rejoined, sha256 verified); golfclips files relayed via clips `inbox/want.txt` (clips@40aae52 → eb5a2ab), rejoined with `tools/rejoin.sh`, sha256 ok, byte sizes match Dropbox; raw files then removed from the public inbox (clips@05a140b).
- Each wipe starts at 0.0 s of the original and ends just before her first spoken word: onset from speech-band (250–3500 Hz) 20 ms energy plus the frame where her own caption first appears; cut at a quiet 20 ms window before onset, frame-aligned, and before her caption shows, so no words are clipped and no caption text appears in either comp (checked frame by frame).
- Audio: each clip keeps its own sound; per-clip gain to a common level (louder half of 50 ms windows → −30 dBFS, ±12 dB cap), 20/30 ms fades at every cut, then +11 dB, limiter (0.45), loudnorm I=−16 linear 2-pass.
- No text burned in, no speed changes, no music. Outfits/places alternate; no outfit twice in a row.

## Comp 2 — wipes (in order)
| # | out (s) | source (original) | src in–out (s) | outfit / place |
|---|---|---|---|---|
| 1 | 0.00–1.60 | copy_2A97DD30-DDC0-49D9-8870-4C269E760E1D.MOV (golfclips) | 0.000–1.600 | green striped polo, red top, standing on fairway, blue sky (opener, big smile) |
| 2 | 1.60–3.67 | IMG_6394.MP4 (golfclips) | 0.000–2.067 | orange checker, cloudy sky, mountains |
| 3 | 3.67–5.07 | copy_0B6BFBE5-2F81-487A-9544-B2C587E0EE74.MOV (golfclips) | 0.000–1.400 | green striped polo, orange top, pines + mountains |
| 4 | 5.07–6.37 | Video Oct 12 2026, 7 17 58 AM.mov (Golf Captions) | 0.000–1.300 | white shirt, camo hat, cloudy |
| 5 | 6.37–7.80 | copy_99A28E54-DA4E-4AD6-956C-A4CC7A3C4FC1.MOV (golfclips) | 0.000–1.433 | green striped polo, red top, standing by a pond (windy) |
| 6 | 7.80–8.83 | 0cef0458001241e4b2c974c97174e51f.MOV (golfclips) | 0.000–1.033 | palm-print shirt, Birdie Birdie hat |
| 7 | 8.83–10.10 | Video Oct 12 2026, 12 03 20 AM.mov (Golf Captions) | 0.000–1.267 | sage green polo, San Angelo |
| 8 | 10.10–12.20 | Video Oct 11 2026, 9 02 57 AM.mp4 (Golf Captions) | 0.000–2.100 | orange checker, dry field |
| 9 | 12.20–13.43 | Video Oct 12 2026, 7 33 50 AM.mov (Golf Captions) | 0.000–1.233 | light blue print, navy hat (windy) |
| 10 | 13.43–15.67 | copy_A526847D-927A-4E66-BA6A-83EF27833CEC.MOV (golfclips) | 0.000–2.233 | green striped polo, red top, cart, mountains (closer, smile) |

## Comp 3 — wipes (in order)
| # | out (s) | source (original) | src in–out (s) | outfit / place |
|---|---|---|---|---|
| 1 | 0.00–1.57 | copy_6FFD8A7C-C1C6-458D-A2EE-21B81C660A11.MOV (golfclips) | 0.000–1.567 | green striped polo, red top, pines (opener, big smile) |
| 2 | 1.57–3.23 | Video Oct 11 2026, 9 02 57 AM (1).mp4 (Golf Captions) | 0.000–1.667 | orange checker, tee in mouth, Colorado |
| 3 | 3.23–4.47 | Video Oct 12 2026, 12 05 56 AM.mov (Golf Captions) | 0.000–1.233 | sage green polo, sunny |
| 4 | 4.47–6.77 | IMG_6391.MP4 (golfclips) | 0.000–2.300 | black print shirt, white/red hat |
| 5 | 6.77–9.20 | copy_4E5F508B-EA57-40DF-AC16-CF253290B923.MOV (golfclips) | 0.000–2.433 | green striped polo, red top, tee in mouth, cart |
| 6 | 9.20–10.80 | Video Oct 12 2026, 7 26 20 AM.mov (Golf Captions) | 0.000–1.600 | white shirt, camo hat, sunny |
| 7 | 10.80–12.30 | copy_292850AB-28FF-4896-87F6-BAE3D3750515.MOV (golfclips) | 0.000–1.500 | green striped polo, red top, cart, bright sun |
| 8 | 12.30–13.97 | 17ad39c4cb414ab3a7e6618492d7c7a3.MOV (golfclips) | 0.000–1.667 | blue rainbow-stripe polo, after rain |
| 9 | 13.97–15.43 | Video Oct 12 2026, 12 22 39 AM.mov (Golf Captions) | 0.000–1.467 | sage green polo, shade |
| 10 | 15.43–16.70 | copy_2CC073A6-0417-450E-A364-BDCE638A2D66.MOV (golfclips) | 0.000–1.267 | green striped polo, orange top, blue sky (closer, smile) |
