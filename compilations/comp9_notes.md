# Compilation 9 — "Macky vs. putting" (idea #9 "me vs. putting", FOR REVIEW, not posted)

- Account: @mackthegolfer trial (default for compilations). Clean: no innuendo in cover or caption.
- Video: `compilations/comp9_me-vs-putting.mp4` — 43.3 s, 4 bits, 1080x1920, 30 fps, H.264 High crf 17 preset slow (~11.8 Mbps), AAC 192k 48 kHz, +faststart. ONE encode straight from the true originals with `tools/render_comp.py` (bits in `comp9_bits.json`).
- Theme (kept simple so every bit reads on its own): a putt that should go in → it doesn't → her reaction. Every putt kept whole (stroke → roll → result).
- Cover text: **Macky vs. putting** (her "Macky vs." pill, Poppins Bold, kept off her face). 4 options.
- Caption: **who made the hole this small**
- Review page: https://claude.ai/artifact/KFJoqNkDr6kpxYDkpniAZ7 → collection `compilations`, doc `comp9` (round 1).
- Idea #8 (almost moments) skipped: it draws on the same near-miss pool as the on-hold "edging" comp (only 2 putts within ~2 in), so it can't be made to Mack's standard yet.

## Method
- Sources: Mack's true originals from Dropbox /Golf Captions in `inbox/videos/` (.partNN rejoined with `cat`, sha256 OK; Oct 11 (2) .mp4 = the Dropbox file itself, 7.8 Mbps, rotation tag honoured). Bitrates: 12 03 20 10.8, 7 19 40 9.5, 12 05 56 10.5 Mbps.
- None of the 9 never-posted sources used (state/never_posted.json).
- Cut points from word-timestamped transcripts (state/transcripts) + 20 ms RMS maps + frame-diff scene cuts: every cut sits in a measured gap between words; D starts exactly on her own scene cut (66.067) and G on hers (59.233). No swearing in the kept bits was cut ("shit", "freaking" kept). No shirt wipes, no text added, no speed changes.
- Punch-ins (1.15) alternate: lip-out reaction (A), the selfie verdict (D), the putter kick (B).
- Audio: per-bit gain to −18 LUFS (G selfie quiet: +11.6 dB), fades at jumps, alimiter, loudnorm 2-pass linear → −16 LUFS.
- Spacing: olive/green San Angelo (12 03 20) → white shirt/camo hat Amarillo → dark green San Angelo, different hole/day file (12 05 56) → orange checker Colorado. No two same-shirt bits back to back.
- Reuse: A and B were in the on-hold, never-posted "edging" comp only; D's putt was in dropped comp4 only. Nothing from comp1, comp2 r6, comp3 r5, comp7 r4, wipes or any shorty.

## Bits (in order)
| # | out (s) | source (Golf Captions original) | src in–out (s) | what happens |
|---|---|---|---|---|
| A | 0.0–9.0 | Video Oct 12 2026, 12 03 20 AM.mov (olive, San Angelo) | 153.9–157.1 + 157.1–162.9 (punch-in) | putt → "get a double, get a double" → lips out, hand over mouth → "oh it lipped… freaking lipped" |
| D | 9.0–23.5 | Video Oct 12 2026, 7 19 40 AM.mov (white shirt, camo hat) | 66.1–74.433 + 74.433–77.767 (punch-in) + 77.767–80.55 | "this is for par" → putt → "break in, break in" → misses → "there's really nothing worse than having a perfect drive and then being shit the rest of the time, but here we are for bogey" |
| B | 23.5–38.2 | Video Oct 12 2026, 12 05 56 AM.mov (dark green) | 134.3–145.0 + 145.0–149.0 (punch-in) | "there's a lot riding on this, and you better not delete your comment because you're so embarrassed at this bogey" → putt → "I should not speak while I putt— oh" → misses, kicks, drops the putter → "doesn't freaking matter" |
| G | 38.2–43.3 | Video Oct 11 2026, 9 02 57 AM (2).mp4 (orange checker, Colorado) | 59.25–64.3 | "that was a tough four putt, but at least I look so cute in my new shirt" |

## Covers ("Macky vs. putting", one rounded pill, off her face)
1. `comp9_me-vs-putting_cover_opt1.jpg` — comp @ 3.8 s, hand over mouth after the lip-out, red
2. `comp9_me-vs-putting_cover_opt2.jpg` — comp @ 35.33 s, the putter kick, blue
3. `comp9_me-vs-putting_cover_opt3.jpg` — comp @ 39.33 s, orange-checker grin ("tough four putt"), purple
4. `comp9_me-vs-putting_cover_opt4.jpg` — comp @ 18.5 s, camo-hat selfie ("nothing worse than a perfect drive"), orange

## Swaps (if she wants changes)
- Video Oct 11 2026, 9 02 57 AM (1).mp4 32.85–50.7 (orange checker): "I've got two shots to sink this baby" → long putt → "get in there" misses → frozen squat → "that is a tough bog after two incredibly perfect shots, so" (17.8 s — cut for length; same shirt as G, so it would replace G or sit apart from it)
- Video Oct 11 2026, 9 02 57 AM (3).mp4 78.8–99.6 driver-putting: "imagine I was better at putting with my driver than my putter" → "get in there" → "honestly a four putt is pretty standard"
