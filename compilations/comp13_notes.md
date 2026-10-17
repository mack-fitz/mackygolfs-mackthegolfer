# Compilation 13 — "asmr but it's golf" (Mack's idea, Oct 15; FOR REVIEW, not posted)

- Account: @mackthegolfer trial (default). Clean cover/caption.
- Video: `compilations/comp13_asmr-golf.mp4` — 21.5 s, 18 bits (≈1.1–1.4 s each), 1080x1920 30 fps, H.264 High crf 17 slow, AAC 192k 48 kHz, +faststart. ONE encode from the true originals (`tools/asmr/render.py`, bits in `comp13_bits.json` / `tools/asmr/bits.py`).
- On-screen text: ONLY "asmr but it's golf" for the first 2.0 s (Inter SemiBold 72, white, soft shadow, y≈330 — sky, clear of her head; fades out 1.8–2.0 s). Per Mack's brief for this one. Nothing else drawn.
- Sound: only the natural contact / cup sounds. Every window was picked with NO words in it (checked against the word-timestamped transcripts, ≥0.1 s clear on both sides, plus a 500 Hz voice-band check: 0 voice frames). No music. Each bit gained so its loudest 10 ms sits at −5 dBFS (cap +24 dB) so every hit is about equally loud, 80 Hz highpass (wind rumble), 15/25 ms fades, limiter. Output −23.4 LUFS integrated, peak −0.6 dBFS (short transients with silence between read quiet on LUFS; the hits themselves are full level).
- Cuts tight around contact: ~0.35–0.55 s before (downswing / putter stroke) and ~0.6–0.8 s after (tracer leaving / ball rolling). Every contact kept whole; no shot's contact is cut. Video and audio trimmed frame-exact together (sync checked at 4 bits: contact frame lands on the transient).
- Mix: 6 drives, 4 irons, 2 bunker shots (one big sand splash), 4 putts, 1 chip, ending on the ball dropping in the cup (low camera).
- SPACING: white/camo → orange checker → green (San Angelo) → blue rain polo → olive (cactus day) → orange → green polo → white/camo → black shirt (Colorado) → green → orange → green polo → white/camo → blue rain → olive → orange → green → light blue (cup). No same shirt/day back to back; green days are never adjacent to each other.
- Footage: Golf Captions originals only, all already-posted videos except bits from never-posted-at-index-time 7 30 44 (full posted on @mackygolfs Oct 15). All bits are ≈1 s (< 15 s), so they use up nothing.
- Reuse: no overlap with any live compilation's bits (comp1, comp2 r6, comp3 r5, comp7, comp9, comp11, comp12, edging, wipes) or with shorties, EXCEPT the closing cup drop (7 33 50 25.72–27.15), which sits inside the read-the-putt shorty's window (17.3–29.1, approved/scheduled). It's the only clean ball-in-the-cup sound in the footage (the other drops have her talking over them: "boom", "get in", "finally got it in"), so I kept it — 1.4 s. Swap if she wants: end on the 7 16 02 lag putt instead.

## Caption
**very peaceful sport**  — alt: "turn your sound on"

## Bits (in order; src in–out s, contact s)
| # | source | shirt/day | in–out | contact | what |
|---|---|---|---|---|---|
| 1 | 7 16 02 | white/camo | 25.27–26.42 | 25.77 | driver |
| 2 | 9 02 57 (3) | orange checker | 28.665–29.815 | 29.165 | driver |
| 3 | 12 11 12 | green (San Angelo) | 19.73–20.88 | 20.23 | driver over the water |
| 4 | 12 00 30 | blue rain polo | 7.96–9.11 | 8.46 | driver |
| 5 | 7 30 44 | olive, cactus day | 146.595–147.895 | 147.145 | putt |
| 6 | 9 02 57 (2) | orange checker | 30.665–31.965 | 31.215 | lag putt |
| 7 | 12 22 39 | green polo | 121.875–123.125 | 122.375 | bunker, sand splash |
| 8 | 7 13 58 | white/camo | 43.895–45.045 | 44.395 | iron off thin grass |
| 9 | 7 35 57 | black shirt | 12.43–13.58 | 12.78 | putt (starts on her own scene cut 12.41) |
| 10 | 12 05 56 | green | 78.9–80.05 | 79.4 | iron |
| 11 | 9 02 57 AM | orange checker | 17.2–18.35 | 17.7 | iron off the dirt |
| 12 | 12 17 30 | green polo | 103.31–104.51 | 103.81 | bunker |
| 13 | 7 16 02 | white/camo | 130.775–132.075 | 131.325 | the lag putt |
| 14 | 12 00 30 | blue rain polo | 21.285–22.435 | 21.785 | iron |
| 15 | 7 30 44 | olive, cactus day | 92.9–94.05 | 93.4 | iron |
| 16 | 9 02 57 (1) | orange checker | 9.08–10.18 | 9.53 | driver |
| 17 | 12 14 03 | green | 75.335–76.435 | 75.835 | chip |
| 18 | 7 33 50 | light blue print | 25.72–27.15 | 26.76 (drop) | tap-in rolls in, ball drops in the cup (low camera) |

## Covers ("asmr but it's golf")
1. `comp13_asmr-golf_cover_opt1.jpg` — comp @ 7.95 s, bunker sand splash, red pill
2. `comp13_asmr-golf_cover_opt2.jpg` — comp @ 20.7 s, low camera at the cup, ball by the putter, purple pill
3. `comp13_asmr-golf_cover_opt3.jpg` — comp @ 18.65 s, orange-checker driver follow-through, typewriter note
4. `comp13_asmr-golf_cover_opt4.jpg` — comp @ 11.55 s, iron with tracer, blue pill

## How bits were found
Onset detector over every Golf Captions original (5 ms windows, >1.5 kHz, ≥18 dB jump) → 140 transients → 4-frame contact sheets around each → kept real contacts with no words within ~0.5 s (`tools/asmr/onsets.py`). Cup drops searched via transcripts ("get in", "tap", "boom", "finally got it in") + 10 fps strips at the cup.

## Round 2 — Mack's note (Oct 16, 11:12am MT): "The sounds need to be way closer together. Like multiple sounds per second"
- File: `compilations/comp13_asmr-golf_r2.mp4` — 22.1 s, **53 hits + the cup drop** (≈2.5 sounds per second, was 18 bits ≈0.8/s). Every hit is 0.40 s (12 frames): 0.13 s before contact, 0.27 s after, so contact sits at the same spot in every bit and the rhythm is steady. Cup drop at the end trimmed to 0.95 s (26.20–27.15). Single crf-17 export (`tools/asmr/render_r2.py`, order `tools/asmr/order_r2.py`, bits `compilations/comp13_r2_bits.json`).
- Hits found by the onset detector over every Oct 11/12 Golf Captions original, each checked on a 3-frame contact sheet (real contact only), no transcript word within 0.08 s of the window, no scene cut inside (frame-diff), and no overlap with any other compilation/shorty window (all *_bits.json + shorty windows; read-the-putt overlap only on the cup drop, as in r1).
- Same rules as r1: no talking, no music, per-hit gain so every hit is about equally loud, 80 Hz highpass, 6/20 ms fades; limiter lowered to 0.7 so the AAC export peaks at −0.8 dBFS (no clipping). "asmr but it's golf" for the first 2 s only. No same shirt/day back to back.
- Covers unchanged (all four cover frames are still in the edit). Caption unchanged: "very peaceful sport".

## Round 3 (Oct 17) — Mack: "The text is too big" / "also should be more legible" (+ Oct 16: text can't sit that high)
- File: `compilations/comp13_asmr-golf_r3.mp4` — same 54 hits + cup drop as r2 (bits from `comp13_r2_bits.json`, same per-hit gains/fades/limiter; identical frames to r2 outside the text), ONE crf-17 encode from the true originals (`tools/asmr/render_r3.py`).
- "asmr but it's golf": Inter Bold 46 px, white, 3 px black stroke (~85%) + soft drop shadow (`tools/ontext.py`), lower band (compilation default), ink y 1180–1231, x 347–732; first 2.0 s, fades out 1.8–2.0 s. Checked every frame 0–2.1 s: over legs/grass, never her face; legible at full res and phone size.
- Covers unchanged (cover pills at 7.95 / 20.7 / 18.65 / 11.55 s, after the line is gone; no on-reel line on them).
