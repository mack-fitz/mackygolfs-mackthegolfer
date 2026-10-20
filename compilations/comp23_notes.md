# Compilation 23 — "Macky vs. proper technique" (new idea, Oct 20; FOR REVIEW, not posted)

- Why this idea: the idea list (1–12 + asmr + golf lingo) is used up; comp15–22 were new patterns. New pattern from the transcripts: her explaining her own "technique" and then owning it — finger wiggles before every drive, "I normally do not swing like that… maybe I gotta start working on that being my thing", "I don't know why I'm squatting right now". Every bit is her commenting on her own form, with the shot that goes with it.
- Account: @mackthegolfer trial (default). Caption: **the finger wiggles are non negotiable**. Alt: "please don't steal my swing".
- Video: `compilations/comp23_proper-technique.mp4` — 42.1 s, 3 bits, 1080x1920 30 fps, H.264 High crf 17 slow (~12.2 Mbps), AAC 192k 48 kHz, +faststart. ONE encode from the true originals with `tools/render_comp.py` + `COMP_FINAL_LIMIT=0.71` (bits in `comp23_bits.json`). Loudness −15.9 LUFS integrated, peak −2.8 dBFS.
- Sources: /Golf Captions originals only (HARD RULE 12, no /golfclips). 7 26 20 / 12 17 30 rejoined from .partNN (sha256 verified vs .sha256); Oct 11 9 02 57 (2).mp4 single untouched file (7.8 Mbps, natural for the Oct 11 .mp4s, as comp22 noted). All three are already posted (posted_index.json): 7 26 20 = @mackygolfs 2026-10-16 "six months of golf. rate me" https://www.instagram.com/reel/Dek2epXEhPv/ ; 9 02 57 (2) = @mackygolfs 2026-09-04 "do you think my shirt is cute yes or no" https://www.instagram.com/reel/Dc1Mym2tnuh/ ; 12 17 30 = @mackygolfs 2026-10-14 "You me par four?" https://www.instagram.com/reel/DefODPLhS7S/. No never-posted video used.
- No shirt wipes, no text added, no music, no speed changes, nothing to swear in these lines. Every shot whole: bit 1 waggles → drive → full tracer → reaction; bit 2 tee shot → tracer → reaction; bit 3 address (the squat) → whole lag putt → result → reaction. Cuts only in gaps between words (word timestamps, 20 ms RMS) or at her own scene cuts (7 26 20 at 27.867, 9 02 57 (2) at 6.133, 12 17 30 at 143.967). One cut inside a bit: 12 17 30 132.50→133.45 (the pause between "…squatting right now." and "That's so unladylike of me", before the stroke).
- Punch-in 1.15 on the last line ("I'm also sorry you had to see that").
- SPACING: white shirt / camo hat (TX) → orange checker (Colorado) → green pinstripe polo (San Angelo). Three different shirts/days.
- Length: a 4th bit (12 22 39 bunker "anytime I'm in a bunker I feel I need to bounce… six inches", 116.55–129.40) fit the theme but took it to 55 s and was in comp21; left out to stay in the 30–45 s format.

## Bits (in order)
| # | out (s) | source | src in–out (s) | what |
|---|---|---|---|---|
| 1 | 0.00–15.60 | Video Oct 12 2026, 7 26 20 AM.mov (white shirt, camo hat) | 12.20–27.80 | "I like to start every drive with as many finger wiggles as possible" → wiggles → drive → tracer → "Not too bad for someone like me, I'll take that." |
| 2 | 15.60–29.60 | Video Oct 11 2026, 9 02 57 AM (2).mp4 (orange checker) | 6.15–20.15 | tee shot → tracer → "I don't know what just happened. I normally do not swing like that. That did land dead center of the green though. So maybe I gotta start working on that being my thing." |
| 3 | 29.60–42.05 | Video Oct 12 2026, 12 17 30 AM.mov (green pinstripe) | 130.40–132.50 + 133.45–141.90 + 141.90–143.80 (zoom) | over the putt: "I don't know why I'm squatting right now." … "That's so unladylike of me. I'm so sorry you had to see that." → lag putt → "oh" → "I'm also sorry you had to see that." |

## Reuse
- None of these seconds are in any compilation or shorty (checked every compilations/*bits*.json and notes, shorties notes). Nearby but not overlapping: 7 26 20 36.0+ tree shot (comp6 dropped, comp18 waiting), 9 02 57 (2) 1.60–6.10 intro (comp22, waiting) and 24.20–30.39 (comp14, scheduled), 12 17 30 154.62+ triple dipper (comp1, posted).
- All bits < 15 s except bit 1 (15.6 s of an already-posted source).

## Covers ("Macky vs. proper technique"; text off her chest, inside the grid crop; checked full size + grid size)
1. `comp23_proper-technique_cover_opt1.jpg` — comp @ 21.8 s, orange checker big grin "I don't know what just happened", orange pill at her waist below the chest (0.60–0.71)
2. `comp23_proper-technique_cover_opt2.jpg` — comp @ 2.0 s, white shirt over the ball mid finger-wiggle, blue pill in the sky (0.15–0.26)
3. `comp23_proper-technique_cover_opt3.jpg` — comp @ 4.0 s, same address, typewriter "i like to start every drive with as many finger wiggles as possible" in the sky (0.15–0.33)
4. `comp23_proper-technique_cover_opt4.jpg` — comp @ 31.0 s, pinstripe squat over the putt looking at camera, purple pill over her legs (0.56–0.67)

## Spares (not used)
- 12 22 39 116.55–129.40 bunker bounce (see Length above)
- 12 14 03 68.5–81.4 "just got to pop this up there, just an easy pop lock and drop" → chip → "I was actually pretty lucky that the grass kind of pulled the brake on it" (pinstripe)
- 7 26 20 42.6–48.3 practice swing "I think that would have done it, especially with the sound effects. I can't forget to make the sound effects" (the real shot right after is in comp18)
