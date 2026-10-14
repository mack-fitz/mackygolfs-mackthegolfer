# Compilation 6 — "the course hates me" (idea #6, FOR REVIEW, not posted)

- Account: @mackthegolfer trial (default for compilations). Clean: no innuendo in cover or caption.
- Video: `compilations/comp6_course-hates-me.mp4` — 47.0 s, 5 bits, 1080x1920, 30 fps, H.264 High crf 17 preset slow (~15.7 Mbps), AAC 192k 48 kHz, +faststart. One encode straight from the originals with `tools/render_comp.py` (bits in `comp6_bits.json`).
- Topic: the course doing her dirty — "best drive of my life" into the sand, a drive that ends up on the cart path behind a forest, a drive into a cactus (she gets poked, twice), mosquitoes, and a tree she was worried about and hit anyway.
- Cover text: **the course hates me** (white Poppins Bold on one rounded color box, mid-frame ~57% down). 5 options.
- Caption: **it's personal**
- Review page: https://claude.ai/artifact/KFJoqNkDr6kpxYDkpniAZ7 → collection `compilations`, doc `comp6` (round 1).

## Method
- Sources: ONLY Mack's true originals from Dropbox `/Golf Captions`, relayed byte-for-byte into `inbox/videos/` (.partNN rejoined with `cat`, sha256 verified against the relay `.sha256`; Oct 11 `.mp4` = the Dropbox file itself). Source bitrates: 12 03 20 10.8 Mbps, 7 16 02 11.1, 7 30 44 11.2, 9 02 57 AM 7.0 (Dropbox original, landscape-tagged/rotated), 7 26 20 9.7.
- Finding bits: OCR of her burned-in captions over all 22 originals (2 fps, white-text mask, tesseract) searched for trees/sand/cart path/cactus/water/lie lines, then 2 fps contact sheets + 0.1 s / 20 ms loudness maps for cut points, and frame-diff for her own scene cuts (every part starts/ends clear of a scene cut, so no stray frames).
- Every shot kept whole from address through the ball flight / tracer (the cart-path drive, the cactus drive, the tree shot). The only thing cut out of a shot bit is a PRACTICE swing's follow-up chatter in bit 5 ("think that would have done it / especially with the sound effects") and standing/walking dead air. No swearing cut ("god damn it" kept). No shirt wipes (bit 1 starts right after her own cut out of the wipe at 44.43 s). No text added; her captions untouched. No speed changes, no music.
- Punch-ins (1.15): "and yet now I'm in the sand", "zoinks that is a tough lie", the cactus/poked shot.
- Audio: per-bit gain to −18 LUFS (mosquito selfie was very quiet: +15 dB cap +3.5 dB), 20/30 ms fades at jumps, alimiter, loudnorm 2-pass linear → **−16.0 LUFS, peak −1.4 dBFS**; every section within ~1 LU.
- Spacing (Mack's rule): San Angelo green pinstripe → white shirt/camo hat → San Angelo green pinstripe (different hole, cactus) → orange checker (Colorado) → white shirt/camo hat (different hole). No two bits from the same shirt/day back to back.
- Nothing reused from comps 1–4, edging or the wipes comp. (Bit 1's 50–55 s was in comp2 ROUND 1 only — replaced in round 2, never posted.)

## Bits (in order)
| # | out (s) | source (Golf Captions original) | src in–out (s) | what happens |
|---|---|---|---|---|
| 1 | 0.00–8.43 | Video Oct 12 2026, 12 03 20 AM.mov (green pinstripe, San Angelo) | 44.47–47.07 + 48.07–48.97 + 50.17–55.10 (punch-in) | "I actually didn't realize that the Sahara Desert was in Texas / what's up with this" (bunker) → "and of course I'm in there" → "I thought it was like one of the best drives of my life / and yet now I'm in the sand" |
| 2 | 8.43–19.27 | Video Oct 12 2026, 7 16 02 AM.mov (white shirt, camo hat) | 23.86–27.30 + 31.32–32.27 + 35.31–36.95 + 37.61–40.14 + 41.31–43.59 (punch-in) | drive (tracer) → "still rolling" → "technically kind of in the fairway / kind of on the cart path, who really knows what that's called" → "zoinks, that is a tough lie" (trees, cart path) |
| 3 | 19.27–32.30 | Video Oct 12 2026, 7 30 44 AM.mov (green, cactus day) | 12.76–16.64 + 19.53–21.59 + 23.71–29.20 (punch-in) + 29.20–30.80 | full drive → "I think that landed in the edge of the trees" → "seems it actually landed in the cactus" → "oh I'm scared / aw I got poked / aw I got poked again / aw" → "we're back in business, I'm just gonna take a drop out here" |
| 4 | 32.30–35.43 | Video Oct 11 2026, 9 02 57 AM.mp4 (orange checker) | 20.52–23.65 | hand over face → "getting eaten by mosquitoes" → "wow okay" |
| 5 | 35.43–47.00 | Video Oct 12 2026, 7 26 20 AM.mov (white shirt, camo hat) | 37.58–43.95 + 48.44–53.44 | "shot two, I'm a little worried about this tree / so I gotta try to keep it low" (practice swing) → real swing, tracer straight into the tree → "god damn it, well I hit the tree" |

Length note: 47.0 s, a touch over the 45 s aim (5 bits; each keeps its shot whole). To get under 45: drop bit 4 (→ 43.9 s).

## Covers ("the course hates me", white Poppins Bold, one rounded box, mid-frame)
1. `comp6_course-hates-me_cover_opt1.jpg` — comp @ 0.9 s, "Sahara Desert" close-up, red #E8101A
2. `comp6_course-hates-me_cover_opt2.jpg` — comp @ 7.0 s, "and yet now I'm in the sand" side-eye, blue #1E90FF
3. `comp6_course-hates-me_cover_opt3.jpg` — comp @ 26.6 s, bent over in the cactus, orange #F7931E
4. `comp6_course-hates-me_cover_opt4.jpg` — comp @ 34.6 s, hand over face (mosquitoes), purple #A21CAF
5. `comp6_course-hates-me_cover_opt5.jpg` — comp @ 31.3 s, grin after the cactus ("back in business"), yellow #F5C518

## Other course-hates-me moments found (swaps / later)
- Video Oct 12 2026, 12 03 20 AM.mov 84.4–86.2 + 89.4–101.21 "I've got to pop it over this tree" → shot (tracer) → "well it technically did go over the tree / but then it fell down the right side of the green so / hate to see that, at least I'm in the shade now" (13.6 s — great ender, cut for length; same day as bit 1)
- Video Oct 12 2026, 12 22 39 AM.mov 61.55–69.85 "don't hit this tree above you Mac" → chip into the tree → "well I hit the tree / don't tell me I'm in the sand"
- Video Oct 12 2026, 12 11 12 AM.mov ~76–82.5 "oh pulled that and it hit the tree / but that was gonna be a perfect shot"; 7–13 water hazard (used in comp3 r1 only); 125–158 tree + bunker → lucky rake bounce onto the green ("shout out to that rake… I'm so freaking back baby")
- Video Oct 12 2026, 12 17 30 AM.mov ~58–64 "that's in some tall grass, I'm not fetching that / I'm literally not a dog"
- Video Oct 12 2026, 7 16 02 AM.mov 54–56 "a whole forest in my way"; 65–69 "oh this is a really unfortunate… had all that fairway and this is where we…"; 75.5–77.5 "dang I'm actually close to the cart path now, this is worse"; 91.5–94 "another tough lie, another tough lie"
- Video Oct 12 2026, 12 03 20 AM.mov 75.5–77 "well that landed on their tee box / so that sucks"
- Video Oct 12 2026, 12 14 03 AM.mov 57.5–62 "I know it went into like one of these divots / but which one" (right after comp3's neon-ball bit)
