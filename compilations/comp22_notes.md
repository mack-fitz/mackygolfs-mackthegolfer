# Compilation 22 — "Macky vs. finding a golf buddy" (new idea, Oct 20; FOR REVIEW, not posted)

- Why this idea: the idea list (1–12 + asmr + golf lingo) is used up; comp15–21 were new patterns. New pattern from the transcripts: almost every one of her videos opens with her inviting you to play ("let's play a par 3 together", "you, me, par 4?", "I'm literally begging you, come play this par 5 with me"). 11 of those lines back to back, escalating to "literally begging you". Every bit IS the theme.
- Account: @mackthegolfer trial (default). Caption: **please i'm running out of ways to ask** (asks for help, Oct 16 caption rule). Alt: "it's free and i'll drive the cart".
- Video: `compilations/comp22_play-with-me.mp4` — 37.7 s, 11 bits, 1080x1920 30 fps, H.264 High crf 17 slow (~11.5 Mbps), AAC 192k 48 kHz, +faststart. ONE encode from the true originals with `tools/render_comp.py` + `COMP_FINAL_LIMIT=0.71` (bits in `comp22_bits.json`). Loudness −16.2 LUFS integrated, true peak −2.5 dBFS.
- Sources: /Golf Captions originals only (HARD RULE 12, no /golfclips). Single files symlinked from inbox/videos; 12 11 12 / 12 17 30 / 12 22 39 rejoined from .partNN, sha256 verified. 7 37 01 / 7 38 06 are naturally 5–6 Mbps and the Oct 11 .mp4s 7–8 Mbps (untouched Dropbox files, same as comp_wipes noted). No never-posted video used (7 09 34, 7 31 40, 1 07 33 avoided).
- NO SHIRT WIPES: every intro opens with her wipe; each bit starts AFTER it — on the quiet 20 ms window right before her first word (RMS check), with the shirt already down (frame-checked). comp_wipes (posted) is the wipes only (0 s → just before her first word), so no frame is shared with it.
- Each bit ends in the quiet after her line and before her own scene cut to the tee shot (scdet), so no shot is touched. No text added, no music, no speed changes. Nothing to swear in these lines.
- SPACING: orange checker (Oct 11) → red Hawaiian (Sep 21) → dark green tee (TX) → black print/white hat → red (Sep 21, other hole) → pinstripe (San Angelo) → light blue print → red (Sep 23) → orange checker (other hole) → red (Sep 21, par 5) → green polo (TX). Never the same shirt twice in a row.

## Bits (in order)
| # | out (s) | source | src in–out (s) | line |
|---|---|---|---|---|
| 1 | 0.00–4.50 | Video Oct 11 2026, 9 02 57 AM (2).mp4 | 1.60–6.10 | "Guess what? I got a new shirt. Isn't it cute? Let's play a par 3 together." |
| 2 | 4.50–6.67 | Video Sep 21 2026, 7 12 01 PM.mov | 1.45–3.62 | "Whoo, let's go play a par 3 together." |
| 3 | 6.67–10.19 | Video Oct 12 2026, 12 17 30 AM.mov | 2.08–5.60 | "Hey man, uh, you, me, par 4?" |
| 4 | 10.19–13.35 | Video Oct 12 2026, 7 37 01 AM.mov | 1.62–4.78 | "Hey, my name is Mack. Should we play a par 3 together?" |
| 5 | 13.35–16.41 | Video Sep 21 2026, 7 28 37 PM.mov | 2.36–5.42 | "Is it just me, or should we play a par 5 together?" |
| 6 | 16.41–21.13 | Video Oct 12 2026, 12 11 12 AM.mov | 1.40–6.12 | "I'm in San Angelo, Texas for some reason, the only thing that would make that better is if you played a par 4 with me." |
| 7 | 21.13–24.77 | Video Oct 12 2026, 7 38 06 AM.mov | 1.50–5.14 | "Hey, my name's Mack. Would you want to play a par 5 with me?" |
| 8 | 24.77–27.45 | Video Sep 23 2026, 1 04 53 PM.mov | 1.92–4.60 | "Hey, my name is Mack, why don't you play par 4 with me?" |
| 9 | 27.45–31.97 | Video Oct 11 2026, 9 02 57 AM.mp4 | 2.14–6.66 | "Glad I got your attention. My name is Mack. Let's play a par 4 together." |
| 10 | 31.97–34.49 | Video Sep 21 2026, 7 24 34 PM.mov | 1.78–4.30 | "Hey, it's Mack. Should we play a par 5 together?" |
| 11 | 34.49–37.53 | Video Oct 12 2026, 12 22 39 AM.mov | 1.46–4.50 | "Hey, I'm literally begging you, come play this par 5 with me." |

- Note: bit 3's burned-in caption already shows "four first things first" for the last second (her own caption runs both lines together); the audio stops after "par 4?".

## Reuse
- No window overlaps any posted / scheduled / waiting comp or shorty (checked every compilations/*bits*.json). Nearest: comp_wipes (posted) ends each of these sources right where these bits start; comp20 r2 uses 12 22 39 from 4.55 (after bit 11's 4.50). All bits < 15 s → no never-posted video used up.

## Covers (text above her head, off her chest, inside the grid crop; checked full + grid size)
1. `comp22_play-with-me_cover_opt1.jpg` — @1.5 orange checker grin, orange pill "Macky vs. finding a golf buddy" (0.13–0.24)
2. `comp22_play-with-me_cover_opt2.jpg` — @14.0 red Hawaiian half-smile, blue pill (0.14–0.25)
3. `comp22_play-with-me_cover_opt3.jpg` — @32.2 red Hawaiian big laugh, typewriter "me asking you to play golf with me" (0.15–0.25)
4. `comp22_play-with-me_cover_opt4.jpg` — @11.0 white hat, purple pill (0.13–0.24)

## Spares (not used)
- 12 03 20 1.2–5.0 "Guys, I'm in San Angelo, Texas for some reason. Please keep me company on this par 4." (too close to bit 6)
- 7 13 58 1.5–4.9 "Glad I got your attention. I need someone to play this par 4 with me."
- 7 19 40 18.2–21.2 "Since you're already here, you might as well watch the rest of this par 4."
