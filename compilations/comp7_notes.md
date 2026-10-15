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

## Round 2 (Oct 14) — Mack: "This doesn't make sense go back to the drawing board"
Rebuilt from scratch. Problem with r1: bits mixed themes (a "if I bog this" setup = delusional, "that was gonna be a perfect shot" = excuse) and some verdicts needed context. New rule for every bit: ONE shot that clearly goes wrong → her immediately rating it way too kindly. No setups that need explaining.
- Video: `compilations/comp7_not-bad_r2.mp4` — 46.3 s, 4 bits, single crf-17 encode from the true originals (`comp7_r2_bits.json`, `tools/render_comp.py`).
| # | out (s) | source | src in–out (s) | what happens |
|---|---|---|---|---|
| 1 | 0.0–14.3 | Video Oct 12 2026, 12 03 20 AM.mov (green, San Angelo) | 84.70–86.15 + 89.60–102.45 | "I've got to pop it over this tree" → shot (tracer) → "well it technically did go over the tree / but then it fell down the right side of the green so / hate to see that, at least I'm in the shade now / that's genuinely the only good news" |
| 2 | 14.3–22.7 | Video Oct 12 2026, 7 13 58 AM.mov (white/camo, Amarillo) | 28.30–33.85 + 36.45–39.30 (punch-in) | shot → "holy shit couldn't have been more perfect" → "still not on the green but absolutely pured the hell out of that" |
| 3 | 22.7–35.7 | Video Oct 11 2026, 9 02 57 AM (3).mp4 (orange checker, Colorado) | 84.90–89.30 + 90.80–99.40 | long putt "get in there get in there" slides by → tap-in → "honestly a four putt is pretty standard / but that long putt incredible" |
| 4 | 35.7–46.3 | Video Oct 12 2026, 7 26 20 AM.mov (white/camo) | 55.20–60.90 + 63.20–67.95 (punch-in) | shot pops up and comes down short (tracer) → "would have liked to see a little more distance / but otherwise pure like butter" |
- Every shot kept whole; cuts only in silent address/walking (0.1 s RMS maps); her own scene cut used at 90.80 in bit 3. No swearing in kept bits was cut. No text added. Outfits alternate green → white/camo → orange → white/camo.
- Not reused from comp1, comp2, comp3, edging, wipes (bit 4 seconds overlap dropped comp6's tree shot window edge only: comp6 ended at 53.44, this starts 55.20).
- Covers (r2): opt1 shade face @11.0 red pill "that's not bad"; opt2 orange checker grin @33.0 blue pill; opt3 camo close-up "pure like butter" @44.6 purple pill; opt4 typewriter "my golf shots, rated by me" @12.4.
- Caption unchanged: "i'm my biggest fan".

## Round 3 (Oct 15 03:16Z) — Mack: "Redo this whole thing. Text says the sh*t I be saying while shooting a 115. Do clips of me talking about how good I am. Open with best putter in the galaxy. Other stuff like that. The more the better I'll tell you what to cut"
- Rebuilt: 11 self-hype lines, opens on the galaxy line, no shots on screen, outfits alternate green/white/orange. `comp7_hype_r3.mp4` (render_comp.py, comp7_r3_bits.json), 44 s.
  galaxy (12 05 56 101.9–109.3) → "as you know if you watch my content I'm an expert read greener" (7 17 58 72.05–75.0) → "you're about to see the lag putt of the century" (12 11 12 161.05–163.1) → "we could actually be alright here, I'm normally pretty good with a pitching wedge" (Oct 11 (3) 30.9–34.45) → "you're about to see one of the best putts you've ever seen in your entire life" (12 05 56 113.5–116.3) → "now you're about to see the lag master do her thang… you're going to eat this right up, that's something I know for sure" (7 13 58 52.6–61.45, cut before the stroke) → "have you ever seen a shot better than that?" (12 05 56 54.05–55.95) → "I'm basically gonna whack it with my 8 iron straight into the hole" (7 17 58 8.75–13.55) → "you ever seen a lag putt that good? I don't think so" (12 11 12 169.0–171.05) → "and that's why they call me the motherf*cking lag master" (7 17 58 88.5–92.15) → "so I really just have to hit this perfectly, shouldn't be too hard" (12 05 56 72.36–76.5).
- No bit shared with comp2 r6 except the galaxy line. 7 17 58 (lock-it-in par 3) is never-posted: full original posts on @mackygolfs Oct 15 6:52pm MT — comp7 must not post before that.
- Cover text "the sh*t I be saying while shooting a 115", 4 options. Caption unchanged ("i'm my biggest fan").

## Round 4 file (rebuilt Oct 15 ~12Z) — the earlier Oct 15 run couldn't push
- `comp7_hype_r4.mp4` (40.7 s) rendered from `comp7_r4_bits.json` (= comp7_r3_bits.json minus the Oct 11 (3) pitching-wedge bit) with render_comp.py, single crf-17 encode from the true originals. Matches the round-4 preview on the review page.
- `comp7_hype_r4_cover_opt1..3.jpg` regenerated per the build note (1.0 s orange 62%, 8.0 s red 50%, 33.5 s purple 60%); the page's cover blobs are the ones she sees.

## Round 5 (Oct 15 ~21:50Z) — Mack: "Take out every comment that isn't about putting and then make the text 'the sh*t I be saying while 4 putting every hole'. Keep that text on the reel throughout"
- Cut the 3 non-putting lines: "have you ever seen a shot better than that?" (approach, 12 05 56 54.05), "I'm basically gonna whack it with my 8 iron straight into the hole" (7 17 58 8.75), "so I really just have to hit this perfectly" (approach over the bunker, 12 05 56 72.36). Kept 7 putting lines in the same order: galaxy best putter → expert read greener → lag putt of the century → one of the best putts → lag master do her thang → you ever seen a lag putt that good → motherf*cking lag master.
- `comp7_putting_r5.mp4` (29.9 s) from `comp7_r5_bits.json`, render_comp.py with the new optional overlay arg: `comp7_r5_overlay.png` = "the sh*t I be saying while / 4 putting every hole" (white Poppins Bold, black outline + soft shadow) at the top (y 130–280 of 1920) for the whole reel — Mack asked for on-reel text, so this is the exception to no-burned-in-text. Checked every 1.5 s: never over her face (only over the hat in close-ups). Still one crf-17 encode from the true originals.
- Covers (r5): pill with the new text over her shirt, below her face: opt1 galaxy close-up orange (12 05 56 @104.6), opt2 expert read greener red (7 17 58 @74.3), opt3 lag master purple (7 17 58 @90.3).
- Still can't post before the lock-it-in full (7 17 58) — that posted Thu Oct 15 6:52pm MT.
