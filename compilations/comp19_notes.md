# comp19 — "why do tweeners have a 100% success rate" (replaces "Macky vs. nature", Mack Oct 21 11:31am)

Mack: "Cancel this whole idea. Make a comp of all of my tweener shots (putt between the legs) - just the putt going in, no talking. Text on screen: why do tweeners have a 100% success rate. Caption: can a scientist weigh in on this"

Note: the old "Macky vs. nature" comp had already published as a trial reel on @mackthegolfer Oct 21 8:25am MT (Zernio 6ad7632e9c441e906ad90204, instagram.com/reel/DewndBEjmkD). Left up (not unpublished) — Mack's call.

## Search (every /Golf Captions video, 29 files)
- Transcripts: "tween", "between", "legs" → only 7 13 58 ("tween her… tween the legs, blue ball").
- Frames: 1 fps contact sheets of all 29 videos (every putt checked), then 4–8 fps sheets on every candidate. Her own captions read too (Oct 11 (2) "tweener" was missed by Whisper).
- 6 tweeners found (back to the hole, putter between the legs, ball in). 7 38 06 is an alternate take of 7 33 50 (same putt) — used once.

| # | out (s) | source | src in–out (s) | what |
|---|---|---|---|---|
| 1 | 0.00–1.23 | Video Oct 12 2026, 12 17 30 AM.mov (green pinstripe) | 170.85–172.08 | tweener → in. Her "spanking" (171.08–171.5) muted (−45 dB on 171.20–171.68); her own caption "spanking" still shows ~0.6 s |
| 2 | 1.23–2.48 | Video Oct 11 2026, 9 02 57 AM (1).mp4 (orange checker) | 45.25–46.50 | tweener tap-in, ends before her scene cut 46.533 |
| 3 | 2.48–3.66 | Video Oct 12 2026, 7 13 58 AM.mov (white, camo) | 91.75–92.93 | starts after "…blue ball" (91.70); her caption lingers ~0.25 s; ends before her cut 92.967 |
| 4 | 3.66–4.91 | Video Sep 23 2026, 1 07 33 PM.mov (red Hawaiian) | 26.95–28.20 | tweener tap-in at the pin |
| 5 | 4.91–6.51 | Video Oct 11 2026, 9 02 57 AM (2).mp4 (orange checker, other hole) | 57.60–59.20 | starts after her "tweener" (57.0–57.5); ends before her cut 59.233 |
| 6 | 6.51–7.90 | Video Oct 12 2026, 7 33 50 AM.mov (blue polo) | 25.75–27.00 | close-up tweener from her scene cut 25.733 |

- Video: `compilations/comp19_tweeners.mp4` — 7.9 s, 6 clips, ONE crf-17 encode (`tools/render_comp.py` + `COMP_FINAL_LIMIT=0.71`, bits `comp19_tweeners_bits.json`, adj −6 dB on the two near-silent clips so their wind hiss isn't boosted). −17.5 LUFS, peak −2.8 dBFS. No talking, natural sound kept, no wipes.
- On-screen line (whole video): "why do tweeners have a / 100% success rate", Inter Bold 46 (`tools/ontext.py`), lower band, ink y 1180–1279 (two lines: one line at 46 px is 986 px wide, over the 90 px margins). Above her own captions (~y 1500), never over her chest or face; checked at every cut.
- Spacing: green → orange → white → red → orange (other hole) → blue.
- Covers: opt1 Oct 11 (1) @45.8 red pill in the sky (0.16–0.27); opt2 Sep 23 @27.45 blue pill (0.18–0.29); opt3 7 13 58 @92.3 purple pill (0.16–0.27); opt4 Oct 11 (2) @58.3 typewriter (0.17–0.27). All from the clean source frames, chest clear, checked full size + grid size.
- Caption: "can a scientist weigh in on this".

## Round 3 (Mack, Oct 22: "First one isn't a tweener??")
- Correct: clip 1 (Video Oct 12 2026, 12 17 30 AM.mov, green pinstripe, 170.85–172.08) was not a tweener. Removed it. No other real tweener in /Golf Captions to replace it (7 38 06 is the same putt as 7 33 50).
- Now 5 clips, 6.6 s: orange (1) 45.25–46.50 → white 7 13 58 91.75–92.93 → red Sep 23 26.95–28.20 → orange (2) 57.60–59.20 → blue 7 33 50 25.75–27.00. Spacing OK.
- Video: `compilations/comp19_tweeners_r3.mp4` (bits `comp19_tweeners_r3_bits.json`), one crf-17 encode via tools/render_comp.py + COMP_FINAL_LIMIT=0.71, same overlay (`comp19_tweeners_overlay.png`). −18.2 LUFS, peak −2.9 dBFS. Every cut checked frame by frame.
- Covers unchanged (opt1–opt4; none used the dropped clip). Caption unchanged: "can a scientist weigh in on this".

## Round 4 (Mack, Oct 23: "On the second clip you cut off me hitting the ball")
- Correct: clip 2 (Video Oct 12 2026, 7 13 58 AM.mov, white/camo) started at 91.75, after the ball had already dropped (in at ~90.93), so the stroke was missing. Now 89.60–91.50: starts with her standing over the ball before the putter moves back, plays the whole tweener stroke (putter between the legs ~89.8–90.5), the ball rolling and dropping in at the flagstick (~90.93), ends 0.57 s later. Her talking over it ("tween her" 89.6–89.82, "tween the legs, blue ball" 90.66–91.7) is fully muted (pg −90 on 89.60–89.85 and 90.65–91.50); the quiet stroke in between keeps its natural sound. Her own caption "tweener between the legs / blue ball" shows through this clip (her burned-in caption, y ~1500, below our line). The ball/cup sit just above our on-screen line (cup at the top edge of "have a"); the ball is visible right up to the drop.
- Checked every other clip for the full stroke (never cut out shots):
  - Orange (1) Oct 11 (1): her scene starts at 45.200; start moved 45.25 → 45.19 so no frame of the scene is lost. Stroke + ball in all inside.
  - Red Sep 23: scene starts 26.967 (first frame already in); putter covers the ball at the cut and swings back ~27.23, ball in. Unchanged.
  - Orange (2) Oct 11 (2): putter still until ~57.9, stroke 58.0–58.5, ball in. Start 57.60 unchanged.
  - Blue 7 33 50: scene starts 25.733; start moved 25.75 → 25.72 so the first stroke frame isn't dropped (putter already moving at her cut — nothing earlier exists).
- Now 5 clips, 7.5 s: orange (1) 45.19–46.50 → white 7 13 58 89.60–91.50 → red Sep 23 26.95–28.20 → orange (2) 57.60–59.20 → blue 7 33 50 25.72–27.00.
- Video: `compilations/comp19_tweeners_r4.mp4` (bits `comp19_tweeners_r4_bits.json`), one crf-17 encode via tools/render_comp.py + COMP_FINAL_LIMIT=0.71, same overlay (`comp19_tweeners_overlay.png`, "why do tweeners have a / 100% success rate", low). −16.1 LUFS, peak −2.3 dBFS. No talking. Cuts at 1.333 / 3.267 / 4.533 / 6.133 checked frame by frame (no stray frames).
- Covers unchanged (opt1–opt4; opt3 is 7 13 58 @92.3, still a valid frame of that source, not part of the new clip window but same shot/outfit). Caption unchanged: "can a scientist weigh in on this".
