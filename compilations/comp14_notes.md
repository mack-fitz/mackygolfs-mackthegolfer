# Compilation 14 — "golf lingo to use next round" (Mack's idea, Oct 13; FOR REVIEW, not posted)

- Account: @mackthegolfer trial (default). Caption (Mack's): **make sure to really get your hips involved**
- Video: `compilations/comp14_golf-lingo.mp4` — 43.7 s, 6 bits, 1080x1920 30 fps, H.264 High crf 17 slow, AAC 192k 48 kHz, +faststart. ONE encode from the true originals with `tools/render_comp.py` (bits in `comp14_bits.json`).
- Sources: Golf Captions originals from `inbox/videos/` (.partNN rejoined, sha256 verified vs the relay .sha256; the Oct 11 .mp4s are the Dropbox files themselves, 7.6 Mbps as in comp_edging).
- Audio: per-bit gain to −18 LUFS, 20/30 ms fades at jumps, alimiter, 2-pass linear loudnorm → −16.0 LUFS. Per-bit check: −16.6 … −15.5 LUFS.
- No text added, no shirt wipes, no music, no speed changes. Every shot kept whole (elephant drive: address → swing → full tracer; tweener putt: whole stroke until her own scene cut). No swearing cut ("be a p*ssy" kept). Cuts in measured quiet gaps (20 ms RMS) or on her own scene cuts (frame-diff).
- Theme: her acting the shot out with hands/body while using golf lingo.
- SPACING: orange checker (Oct 11 Colorado) → green polo (Texas) → orange checker → green pinstripe (Texas) → orange checker → white shirt/camo hat (Amarillo). No two bits from the same shirt back to back; the 3 orange bits are from 3 different holes.
- Not chosen by idea-list order alone: #8 "almost moments" = the on-hold "is this edging?" (not enough near-misses yet) and #10 "hype myself up then the result" was absorbed by comp2/comp7 (Mack: no good shots after hype → just the lines) — so this run made the last idea, golf lingo.

## Bits (in order)
| # | out (s) | source | src in–out (s) | what |
|---|---|---|---|---|
| 1 | 0.00–8.12 | Video Oct 11 2026, 9 02 57 AM (1).mp4 (orange) | 18.28–26.40 | "so you got two options on this hill" (peace sign) → "you can either send it or you can be a p*ssy and go that way" (arm sweep) → "and then kick left afterwards" (hip/arm kick) |
| 2 | 8.12–19.76 | Video Oct 12 2026, 12 22 39 AM.mov (green polo) | 8.86–14.45 + 15.55–21.60 (punch-in 1.15 on part 2) | drive straight up, full tracer → "and they call that an elephant's ass" (trunk arm) → "that's supposed to be an elephant noise but my lips are so dry". 1.1 s of silent standing removed after the tracer lands. |
| 3 | 19.76–25.95 | Video Oct 11 2026, 9 02 57 AM (2).mp4 (orange) | 24.20–30.39 | "like I said, we're pretty DC of the G" (points) → "so I'm just gonna try to lag her up there and get a nice par tap in" (putting mime). Her own cuts at 26.63; ends before her cut to the putt (30.40). |
| 4 | 25.95–30.97 | Video Oct 12 2026, 12 03 20 AM.mov (green pinstripe) | 32.60–37.62 (punch-in from 35.16) | "I don't know what I did, I did kind of like a little pause at the top" (acts out the backswing) → "a little pump pump, kind of worked for me". Ends before her cut to the cart (37.80). |
| 5 | 30.97–36.04 | Video Oct 11 2026, 9 02 57 AM (3).mp4 (orange) | 34.90–39.97 | "should be able to get us pretty close, and then hopefully just a little bump and roll" (acts it out with the club) |
| 6 | 36.04–43.58 | Video Oct 12 2026, 7 13 58 AM.mov (white shirt, camo hat) | 89.42–96.96 (her cut to selfie at 92.97) | "tweener, between the legs, blue ball" → the between-the-legs putt → selfie "definitely not my best hole but you know that" |

## Reuse
- No overlap with any live compilation or shorty window, except bit 2's drive contains the 0.4 s drive-contact hit used in comp13 r2 asmr (12 22 39 10.075–10.475). Every bit is < 15 s, so nothing uses up a never-posted video.

## Covers ("golf lingo to use next round", text kept off her face and clear of her own captions)
1. `comp14_golf-lingo_cover_opt1.jpg` — comp @ 1.0 s, peace-sign "two options", red pill
2. `comp14_golf-lingo_cover_opt2.jpg` — comp @ 16.0 s, elephant-trunk arm, purple pill in the sky
3. `comp14_golf-lingo_cover_opt3.jpg` — comp @ 22.8 s, crouched "lag her up there", blue pill
4. `comp14_golf-lingo_cover_opt4.jpg` — comp @ 34.0 s, "bump and roll" with the club, typewriter note

## Spares (not used)
- 12 22 39 54.1–58.7 "I believe you boys call this a gallery drop, and if you don't, I don't care" (shot follows right away)
- 12 14 03 68.5–81.4 "just gotta pop this up there, just an easy pop lock and drop" → chip → "the grass kind of pulled the brake on it" (13 s)
- 7 26 20 41.0–53.4 practice swing "especially with the sound effects" → hits the tree
- 9 02 57 AM (3) 45.2–48.9 "if I stop being an idiot I should be able to hit the G-spot here" (left out: innuendo on the clean account)

## Round 3 (Oct 18, Mack's notes: "D c of the G should not be the first. The lag her up there and tap it in should be." + "Put bubble around the letters so it doesn't look like the captions")
- Old bit 1 split at her own scene cut (src 26.63, silent): now opens on "so I'm just gonna try to lag her up there and get a nice par tap in" (9 02 57 AM (2) 26.63–30.39); "like I said, we're pretty DC of the G" (24.20–26.63) moved to 3rd, after the elephant drive.
- Order: lag/par tap in (orange) → elephant drive (green polo) → DC of the G (orange) → pause at the top (green pinstripe) → bump and roll (orange). No two same-shirt bits back to back. 28.0 s. Bits: comp14_r3_bits.json.
- On-screen line now sits in white rounded bubbles (one per line) with black Inter Bold 46 text + soft shadow (`tools/ontext_bubble.py`, bubble y 1160–1322), so it can't be mistaken for her own white-outlined captions. One encode: `render_comp.py comp14_r3_bits.json comp14_golf-lingo_r3.mp4 comp14_r3_overlay.png`.
- Covers unchanged (opt2–4).
