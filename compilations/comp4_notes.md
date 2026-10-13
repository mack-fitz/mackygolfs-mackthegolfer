# Compilation 4 — "me talking to my golf ball" (FOR REVIEW, not posted)

- Account: @mackthegolfer trial (default for compilations)
- Video: `compilations/comp4_golf-ball.mp4` — 43.3 s, 1080x1920, 30 fps, H.264 High crf 17 preset slow (12.4 Mbps), AAC 192k 48 kHz, +faststart. One encode straight from the originals (`tools/render_comp.py`, bits in `comp4_bits.json`).
- SOURCE QUALITY: all true originals — copy_2CC073A6 (beach day, Dropbox /golfclips original via clips relay, HEVC 11.2 Mbps), inbox/videos `Video Oct 11 2026, 9 02 57 AM (3).mp4` (7.7 Mbps, the Dropbox file itself), `Video Oct 12 2026, 7 19 40 AM.mov` (9.5), `7 30 44 AM.mov` (11.2, .partNN rejoined, sha256 OK), `7 17 58 AM.mov` (8.1, rejoined, sha256 OK).
- No text added; her captions untouched. No shirt wipes. Swearing kept ("motherf*cker"). Every shot in a bit kept whole (address → swing/stroke → ball flight/roll → result). Cuts at measured quiet points (20 ms windows) and clear of her own scene cuts (checked for stray frames).
- Audio: per-bit (and per-shot-distance) gain, limiter, loudnorm 2-pass linear → −16.1 LUFS, peak −1.3 dBFS. Far-camera lines ("get in there", "into the hole") lifted so they're as clear as the close-up ones.
- Punch-ins (1.15): "break in break in", "boom boom", "not bad not bad".
- Outfits alternate: green stripe → orange checker → white polo/camo hat → olive → white tee. No two from the same shirt/day back to back.
- No bits from comp 1/2/3 reused (comp1 used the beach-day "stop stop stop" at 46.4 s — not used here; comp3's altitude bit starts at 37.4 s of 7 17 58, this one ends at 37.34 s).
- Moments found by OCR of her burned-in captions (outline-aware mask + tesseract, 3 fps) over all 24 originals.

## Suggested caption
she never listens

## Bits (in order)
| # | out (s) | source | source in–out (s) | what she says to the ball |
|---|---|---|---|---|
| 1 | 0.00–11.19 | copy_2CC073A6-0417-450E-A364-BDCE638A2D66.MOV (beach day, green stripe) | 26.95–38.14 | "hopefully I can get pretty close to the green on this one" → swing (tracer) → "oh don't go in that sand, motherf*cker" → "yeah we're at the beach" |
| 2 | 11.19–17.16 | Video Oct 11 2026, 9 02 57 AM (3).mp4 (orange checker) | 83.00–88.97 | "whatever works dude" → putts with the driver → "get in there, get in there" → ball rolls past the cup |
| 3 | 17.16–23.99 | Video Oct 12 2026, 7 19 40 AM.mov (white polo, camo hat) | 66.15–72.98 (punch-in from 71.30) | "this is for par" → putt → "break in, break in" |
| 4 | 23.99–32.15 | Video Oct 12 2026, 7 30 44 AM.mov (olive) | 119.32–127.48 (punch-in from 126.0) | "anyway let's get on the green" → swing → "get on the green, get on the green… boom boom" |
| 5 | 32.15–43.30 | Video Oct 12 2026, 7 17 58 AM.mov (white tee) | 24.50–33.93 + 35.75–37.34 (punch-in) | "into the hole, into the hole" → swing, full tracer to landing → (1.8 s of standing cut) → "not bad, not bad" |

## Covers (title "me talking to / my golf ball", white Poppins Bold on a rounded box, mid-frame)
1. `comp4_golf-ball_cover.jpg` — comp @ 11.9 s, close-up "whatever works dude", red #E8101A
2. `comp4_golf-ball_cover_alt1.jpg` — comp @ 10.3 s, "yeah we're at the beach", blue #1E90FF
3. `comp4_golf-ball_cover_alt2.jpg` — comp @ 31.5 s, the "boom boom" kick, orange #F7931E
4. `comp4_golf-ball_cover_alt3.jpg` — comp @ 43.15 s, "not bad not bad", purple #A21CAF

## Other ball-talk found (swaps / later comps)
- Oct 11 9 02 57 AM (1).mp4 41.6–45.65 second putt "get in there" (+ 46.5–50.4 "that is a tough bog after two incredibly perfect shots so"); 33.3 "got two shots to sink this baby" → first putt (long roll to 41.5)
- Oct 11 9 02 57 AM (2).mp4 27.0 "so I'm just gonna try to lag her up there and get a nice par tap in" → putt → 32.7 "get up there get up there" (soft voice)
- Oct 11 9 02 57 AM.mp4 23.7 "nice and easy let's get her on the green" → chip → "little hot" → putt → 31.0 "get in there" → 35.0 "get in"
- copy_0B6BFBE5 (guess my score) 36–41 putt → "that's gonna be good x2 / that's gonna be real freaking good"
- Video Oct 12 2026, 12 03 20 AM.mov 155.3 "get a double get a double" → putt → 159.0 "oh it lipped / freaking lipped"
- Video Oct 12 2026, 12 17 30 AM.mov 165.7 "have to get this in or… somebody's in big trouble"
