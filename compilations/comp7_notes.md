# Compilation 7 — "that's not bad" (idea #7, FOR REVIEW, not posted)

- Account: @mackthegolfer trial (default for compilations). Clean: no innuendo in cover or caption.
- Video: `compilations/comp7_not-bad.mp4` — 44.2 s, 4 bits, 1080x1920, 30 fps, H.264 High crf 17 preset slow, AAC 192k 48 kHz, +faststart. ONE encode straight from the true originals with `tools/render_comp.py` (bits in `comp7_bits.json`).
- Theme: a bad shot, then Mack rating it generously. Every bit = the shot (whole) → her verdict.
- Cover text: **that's not bad** (pill, 3 colors) + one typewriter option "my golf shots, rated by me". 4 options.
- Caption: **i'm my biggest fan**
- Review page: https://claude.ai/artifact/KFJoqNkDr6kpxYDkpniAZ7 → collection `compilations`, doc `comp7` (round 1).

## Method
- Sources: Mack's true originals from Dropbox `/Golf Captions` in `inbox/videos/` (.partNN rejoined with `cat`, sha256 verified). Rotated Oct 11 .mp4 used as-is (Dropbox file).
- Finding bits: OCR of her burned-in captions over all 22 originals (2 fps, white-text mask, tesseract), searched for generous self-ratings ("not bad", "perfect", "standard", "pretty good"...), then contact sheets for the shot result, 0.04–0.2 s loudness maps for cut points, frame-diff for her own scene cuts.
- Every bit starts after her previous caption has cleared and ends before her next line starts. Shots kept whole (swing → tracer/roll → reaction). No swearing in these bits (nothing cut). No shirt wipes. No text added. Punch-ins (1.15) on the four-putt verdict, "but that was gonna be a perfect shot", "surely that feels pretty good right".
- Audio: per-bit gain to −18 LUFS (windy Colorado putt +6.6 dB), fades at jumps, alimiter, loudnorm 2-pass linear → −16.0 LUFS.
- Spacing: white shirt/camo hat (Amarillo) → orange checker (Colorado) → green (San Angelo) → white/camo (different hole, different day's video). No two same-shirt bits back to back.
- Nothing reused from comp1, comp2 (r3), comp3 (r4), edging or wipes. (9 02 57 (3) 83–89 and 7 19 40 66–73 were in comp4, which was dropped; this uses different seconds anyway.)

## Bits (in order)
| # | out (s) | source (Golf Captions original) | src in–out (s) | what happens |
|---|---|---|---|---|
| 1 | 0.00–13.20 | Video Oct 12 2026, 7 19 40 AM.mov (white shirt, camo hat) | 46.25–59.45 | "let's get on the green, might as well right" → approach (tracer) comes up short → "absolutely perfect / little short but absolutely perfect / in the sense that little short is absolutely perfect" |
| 2 | 13.20–18.32 | Video Oct 11 2026, 9 02 57 AM (3).mp4 (orange checker) | 90.833–94.333 + 94.333–95.95 (punch-in) | putt slides by → tap-in → "honestly a four putt is pretty standard" |
| 3 | 18.32–24.08 | Video Oct 12 2026, 12 11 12 AM.mov (green, San Angelo) | 75.50–79.60 + 79.60–81.26 (punch-in) | swing → pulled into the tree → "oh I pulled that and it hit the tree / but that was gonna be a perfect shot" |
| 4 | 24.08–44.2 | Video Oct 12 2026, 7 26 20 AM.mov (white shirt, camo hat) | 119.35–133.00 + 133.00–139.35 (punch-in) | "so if I bog this, hopefully you'll say I'm a good golfer" → bogey putt misses → "well… I didn't, like I said" → "I'm six months into this getting a double bogey / surely that feels pretty good right… maybe" |

## Covers
1. `comp7_not-bad_cover_opt1.jpg` — comp @ 12.0 s, camo-hat close-up ("little short is absolutely perfect"), red pill "that's not bad"
2. `comp7_not-bad_cover_opt2.jpg` — comp @ 17.5 s, orange checker grin at the flag, blue pill
3. `comp7_not-bad_cover_opt3.jpg` — comp @ 17.75 s, orange checker, typewriter note "my golf shots, rated by me"
4. `comp7_not-bad_cover_opt4.jpg` — comp @ 12.5 s, camo-hat close-up, purple pill

## Other generous-rating moments (swaps / later)
- Video Oct 12 2026, 7 13 58 AM.mov 21–39.2 "I don't think I've got the power to get her there" → shot → "holy shit couldn't have been more perfect / still not on the green but absolutely pured the hell out of that" (white/camo)
- Video Oct 12 2026, 7 26 20 AM.mov 53.3–67 shot → "would have liked to see a little more distance / but otherwise pure like butter"; 110–118 "well that wasn't great / I do believe we're putting for bogey now / which is actually pretty good"
- Video Oct 12 2026, 7 17 58 AM.mov 24.5–37 "into the hole" → 8 iron → "not bad not bad" (was comp4's ender); ~100–107 "bump bump / I'll take a bog"
- Video Oct 12 2026, 12 03 20 AM.mov ~89–101 "well it technically did go over the tree / … at least I'm in the shade now"
- Video Oct 12 2026, 12 11 12 AM.mov 155–171 ball across the green → "that's okay, still feeling absolutely electric" → "lag putt of the century"
