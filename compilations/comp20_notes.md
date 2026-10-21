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

## Round 2 (Oct 20) — Mack: "do a bunch of clips back to back of me saying i have no idea where my ball is / can't find my ball etc"
- Rebuilt as ONLY her lines about not knowing where the ball is / not finding it / not looking for it, back to back. Dropped the water drive ("right into the water") and the white-shirt "left of what I'm assuming is the green" bit (not about finding the ball), and the 12 17 30 swing (bit now starts on "that's in some tall grass").
- Searched every /Golf Captions transcript (see / find / lost / where / searching / fetching / which one) — these 5 are her lines on it. /golfclips not used (HARD RULE 12).
- Video: `compilations/comp20_where-did-it-go_r2.mp4` — 32.9 s, 5 bits, ONE crf-17 encode, `COMP_FINAL_LIMIT=0.71` (bits in `comp20_r2_bits.json`). Cuts in word gaps only. No text, no wipes, swearing kept ("holy shit" x2).
- SPACING: pinstripe (12 11 12) → green polo (12 22 39, par 5 tee) → pinstripe (12 14 03, other hole) → dark tee (12 17 30) → green polo (12 22 39, cactus, later on the hole).

| # | out (s) | source | src in–out (s) | what |
|---|---|---|---|---|
| 1 | 0.00–8.88 | Video Oct 12 2026, 12 11 12 AM.mov | 148.367–157.25 | "I don't see the ball. Oh, I do. Holy shit, I thought for a second there I raked her into the hole. Holy shit. But I do see it, it's on the other side of the green in the shade, so." |
| 2 | 8.88–11.88 | Video Oct 12 2026, 12 22 39 AM.mov | 4.55–7.55 | "I already know I'm going to be pissed with this yellow ball, I'm not going to be able to find it." |
| 3 | 11.88–17.43 | Video Oct 12 2026, 12 14 03 AM.mov | 56.40–61.95 | "I know it went into like one of these divots, but which one?" |
| 4 | 17.43–26.68 | Video Oct 12 2026, 12 17 30 AM.mov | 59.60–68.85 | "That's in some tall grass. I'm not fetching that. I'm literally not a dog, but I'm just going to drop another one and try again. Who cares?" |
| 5 | 26.68–32.78 | Video Oct 12 2026, 12 22 39 AM.mov | 47.50–53.60 | "You might be wondering why my ball turned pink, and that is because I'm surrounded by cactus and I don't feel like searching for the ball." |

- Reuse: bit 2 + bit 5 were never in a comp (comp1 posted uses 12 22 39 33.10–39.30 + 109.95–111.80 only). Bits 1, 3, 4 = r1's.
- Covers r2: opt1 + opt4 = r1's opt1/opt4 (same frames still in the cut); opt2 @19.5 "that's in some tall grass" blue pill in the sky (0.13–0.24); opt3 @30.0 "surrounded by cactus" purple pill at her waist (0.58–0.69, above her captions).

## Round 3 (Oct 21) — Mack: "You did not do what I said. Should be a quick video with clips of me just saying where is my ball I can't find my ball"
- Rebuilt from scratch: ONLY the moments where she literally says she can't see / can't find her ball, nothing before or after. Searched every /Golf Captions transcript (see / find / where / lost / search / fetch / which one / went / no idea / track) — these are the only literal ones.
- Left out on purpose (not literally "can't find my ball"): 12 17 30 "that's in some tall grass, I'm not fetching that" (won't look), 12 22 39 "…and I don't feel like searching for the ball" (mid-sentence, would need the cactus/pink-ball setup), 12 14 03 "neon yellow ball when the grass is so bright green" (in posted comp3), 12 14 03 18.2 "you can't even see it" (the tee), 7 26 20 "I don't see a flag".
- Video: `compilations/comp20_where-did-it-go_r3.mp4` — 8.9 s (was 32.9), 3 bits, ONE crf-17 encode, `COMP_FINAL_LIMIT=0.71` (bits in `comp20_r3_bits.json`). −15.9 LUFS, peak −3.0 dBFS. Sources sha256 re-verified Oct 21.
- Cuts only in measured gaps between words; whole sentences only. No text, no wipes. Export checked frame by frame at every cut + audio at every join.
- Bit 1's own caption reads "I don't see the ball oh I do" (one caption line); the audio stops after "ball" (100 ms gap before "Oh"), so the caption shows "oh I do" for the last ~0.6 s.
- SPACING: pinstripe → green polo → pinstripe (other hole).

| # | out (s) | source | src in–out (s) | what |
|---|---|---|---|---|
| 1 | 0.00–1.00 | Video Oct 12 2026, 12 11 12 AM.mov | 148.60–149.60 | "I don't see the ball." |
| 2 | 1.00–3.85 | Video Oct 12 2026, 12 22 39 AM.mov | 4.70–7.55 | "I already know I'm going to be pissed with this yellow ball, I'm not going to be able to find it." |
| 3 | 3.85–8.83 | Video Oct 12 2026, 12 14 03 AM.mov | 56.97–61.95 | "I know it went into like one of these divots… but which one?" |

- Covers r3: opt1 @0.6 close-up looking for it, red pill over her cap (0.15–0.26); opt2 @2.5 on the tee, blue pill in the sky (0.16–0.27); opt3 @7.8 "but which one", purple pill in the sky (0.15–0.26); opt4 @0.3 typewriter "i don't see the ball" (0.16–0.22). Chest clear on all, checked full size + grid size.
