# Compilation 20 — "Macky vs. where did it go" (new idea, Oct 19; FOR REVIEW, not posted)

- Why this idea: the idea list (1–12 + asmr + golf lingo) is used up; comp15–19 were new patterns. New pattern from the transcripts: losing track of the ball — "I don't see the ball", "I'm not fetching that", "right into the water", "left of what I'm assuming is the green", "which divot?". Every bit is her losing (or almost losing) her ball, so the theme reads in each one.
- Account: @mackthegolfer trial (default). Clean. Caption: **if you've never lost a ball in a divot you're lying** (picks a fight, Oct 16 caption rule).
- Video: `compilations/comp20_where-did-it-go.mp4` — 48.5 s, 5 bits, 1080x1920 30 fps, H.264 High crf 17 slow (~14.5 Mbps), AAC 192k 48 kHz, +faststart. ONE encode from the true originals with `tools/render_comp.py` (bits in `comp20_bits.json`; bit 3 adj +2.5 dB, it is mostly swing/silence). Loudness −16.0 LUFS integrated, per-bit −15.6 to −17.7, true peak −2.5 dBFS.
- New in render_comp.py: opt-in `COMP_FINAL_LIMIT=0.71` (true-peak safety limiter after the linear loudnorm). Without it this mix's club impacts went +0.3 dBFS; with it they sit at −2.5. Used for this render only; other comps unchanged.
- Sources: Golf Captions originals in `inbox/videos/` (.partNN rejoined into tools/src/, sha256 verified vs the relay .sha256 for 12 11 12, 12 17 30, 7 26 20, 12 14 03). 9.7–11.1 Mbps.
- No text added, no shirt wipes, no music, no speed changes. Every shot kept whole: bit 2 swing → tracer → "motherfucker" (only the 3 s of silent standing after the tracer ends is cut, 56.4→59.6), bit 3 drive → tracer → "ooh… right into the water", bit 4 approach → full tracer → (2 s silent walk cut, 81.0→82.8) → her verdict. Cuts only in gaps between words (word timestamps, state/transcripts) or on her own scene cuts. Swearing kept ("holy shit" ×2, "motherfucker").
- Punch-in 1.15 on bit 2's second half ("I'm literally not a dog").
- SPACING: green pinstripe (San Angelo) → dark green tee + Bad hat (triple-dipper day) → green pinstripe (water hole) → white shirt + camo hat (Amarillo) → green pinstripe (yellow-ball par 3). No two same-shirt/day bits back to back.

## Bits (in order)
| # | out (s) | source | src in–out (s) | what |
|---|---|---|---|---|
| 1 | 0.00–8.88 | Video Oct 12 2026, 12 11 12 AM.mov (pinstripe) | 148.367–157.25 | "I don't see the ball. Oh, I do. Holy shit, I thought for a second there I raked her into the hole. Holy shit. But I do see it, it's on the other side of the green in the shade, so." |
| 2 | 8.88–22.23 | Video Oct 12 2026, 12 17 30 AM.mov (dark tee) | 52.30–56.40 + 59.60–68.85 (zoom) | swing → tracer → "motherfucker" → "that's in some tall grass, I'm not fetching that. I'm literally not a dog, but I'm just gonna drop another one and try again. Who cares?" |
| 3 | 22.23–28.55 | Video Oct 12 2026, 12 11 12 AM.mov (pinstripe) | 18.10–24.42 | drive → tracer → "ooh… right into the water" |
| 4 | 28.55–42.87 | Video Oct 12 2026, 7 26 20 AM.mov (white, camo hat) | 74.00–81.00 + 82.80–90.12 | approach → tracer → "I think I landed off a little to the left of what I'm assuming is the green. We'll see… found the flag, probably did" |
| 5 | 42.87–48.42 | Video Oct 12 2026, 12 14 03 AM.mov (pinstripe) | 56.40–61.95 | "I know it went into like one of these divots… but which one?" |

## Reuse
- Not in any posted / scheduled / waiting compilation or shorty (checked every compilations/*bits*.json + shorties notes). Avoided on purpose: 12 14 03 50.0–55.1 "neon yellow ball" (comp3, posted), 7 26 20 67.9–73.6 "shooting straight is the name of the game" (comp15, waiting), 12 11 12 131–142 bunker shot (comp15, waiting).
- Only overlap: bit 2's 52.3–63.0 sits inside dropped shorty not-to-putt-it (52.1–63.0, never posted). 12 17 30 43.5–52.0 is in comp16 (dropped).
- All bits < 15 s → no never-posted video used up.

## Covers ("Macky vs. where did it go", COVER_WRAP=15; text kept off her chest, inside the grid crop; checked full size + grid size)
1. `comp20_where-did-it-go_cover_opt1.jpg` — comp @ 2.3 s, grinning close-up "I thought for a second there…", red pill over her cap (0.15–0.26)
2. `comp20_where-did-it-go_cover_opt2.jpg` — comp @ 25.4 s, follow-through with the tracer heading at the water, blue pill over the grass below her (0.73–0.84)
3. `comp20_where-did-it-go_cover_opt3.jpg` — comp @ 39.3 s, white shirt leaning into the camera "left of what I'm assuming is the green", purple pill over the camo hat/clouds (0.15–0.26)
4. `comp20_where-did-it-go_cover_opt4.jpg` — comp @ 47.6 s, "but which one", typewriter "i know it went into one of these divots. but which one" in the sky (0.15–0.29)

## Spares (not used)
- 12 11 12 33.3–34.4 "not in the water!" (her re-tee after bit 3; 24.4–33.3 is re-teeing)
- 12 17 30 70–84.4 re-hit → "at least that one I'm not getting bit by a snake"
- 7 16 02 31.2–45 "still rolling… technically kind of in the fairway, kind of on the cart path, who really knows what that's called. Zoinks" (white/camo, same day as bit 4; comp6 dropped + fairway-to-hit dropped used parts)
- 12 22 39 94.7–100 "also you might have noticed I didn't actually land in the sand, so today's my lucky day" (stop before 109.95 — comp1 posted)
