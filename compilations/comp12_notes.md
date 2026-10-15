# Compilation 12 — "golf math" (idea #12, FOR REVIEW, not posted)

- Account: @mackthegolfer trial (default). Clean cover/caption.
- Video: `compilations/comp12_golf-math.mp4` — 44.9 s, 5 bits, 1080x1920 30 fps, H.264 High crf 17 slow, AAC 192k 48 kHz, +faststart, 12.8 Mbps. ONE encode from the true originals with `tools/render_comp.py` (bits in `comp12_bits.json`). −16.1 LUFS.
- Theme: Mack doing her own score math — "on in four", "gotta break 100", "fifth or sixth stroke", "a four putt is pretty standard", "lost track of the score, doesn't even matter".
- Cover text: **golf math** (pill red/purple) + typewriter "a four putt is pretty standard" / "gotta break 100". 4 options.
- Caption: **the math checks out**
- Review page doc: `comp12` (round 1, order 19).

## Method
- Sources: Golf Captions originals in inbox/videos (.partNN rejoined into tools/src, sha256 verified). Bitrates: 7 16 02 11.1, 12 00 30 7.2 (untouched phone file, native), 7 30 44 11.2, 9 02 57 (3) 7.7 (the Dropbox file itself), 12 22 39 9.9 Mbps.
- Cuts from word-timestamped transcripts (state/transcripts) + 0.05–0.1 s loudness maps + frame-diff scene cuts. Every in/out sits in a real gap between words / on her own scene cut (vlead used where her audio starts just before the cut / caption swap).
- No shots cut: bit 1 keeps the whole approach (address → swing → tracer → picking up) between "pissed if we're not on in 4" and "as it turns out I'm pissed"; bit 4 keeps the short putts before "a four putt is pretty standard"; bit 5 keeps the whole bunker shot (swing → tracer) before "perfect perfect". Bits 2/3 are talking only (bit 3 ends before her chip, which isn't in the comp). No swearing cut ("pissed", "pissing" kept). No shirt wipes (12 00 30 starts at 1.2 s, after its wipe). No text added. Punch-ins (1.15) on "as it turns out I'm pissed", "so no days off", the orange-checker verdict, the putting-green "lost track of the score".
- Spacing: white/camo (Amarillo) → blue striped (rainy day) → green/olive (San Angelo cactus day) → orange checker (Colorado) → green polo (different video). No same-shirt bits back to back.
- Reuse check: no overlap with comp1, comp2 r6 (7 16 02 122.07–124.25 untouched; this ends 121.7), comp3 r5 (7 30 44 135.16+ untouched; this ends 134.45), comp4, comp6, comp7 r4, comp9, comp11, edging, wipes, shorties.
- Footage status: all already posted on Mack's accounts except 7 30 44 (cactus par 5), whose full original posted on @mackygolfs Oct 15 7:42 MT, so FULL BEFORE CUT is satisfied.

## Bits (in order)
| # | out (s) | source | src in–out (s) | what she says |
|---|---|---|---|---|
| 1 | 0.0–13.7 | 7 16 02 (white/camo) | 108.0–120.033 + 120.033–121.7 (punch-in) | "and you know what? maybe we'll be on in four. I'm actually gonna be pissed if we're not on in four to be honest" → approach shot → "so as it turns out, I'm pissed" |
| 2 | 13.7–19.8 | 12 00 30 (blue striped, rain) | 1.2–4.35 + 4.35–7.28 (punch-in) | "absolutely pissing rain today, but I've got to break 100, so no days off. here's a par four" |
| 3 | 19.8–24.9 | 7 30 44 (green, cactus day) | 129.3–134.45 (vlead 0.067) | "I think this is only my fifth or sixth stroke, but it feels like I've been playing this hole for an hour" |
| 4 | 24.9–33.9 | 9 02 57 (3) (orange checker) | 90.84–94.333 + 94.333–99.8 (punch-in) | short putts → "honestly, a four putt is pretty standard, but that long putt, incredible" |
| 5 | 33.9–44.9 | 12 22 39 (green polo) | 138.56–144.333 (vlead 0.35) + 144.333–149.42 (punch-in) | "here we go, loosey goosey in a bounce, no thoughts" → bunker shot → "perfect, perfect. I've lost track of the score, it doesn't even matter, all that matters is being loosey goosey" |

## Covers
1. `comp12_golf-math_cover_opt1.jpg` — comp @ 17.5 s, wide-eyed in the rain cart (blue polo), red pill
2. `comp12_golf-math_cover_opt2.jpg` — comp @ 31.0 s, orange-checker grin, purple pill
3. `comp12_golf-math_cover_opt3.jpg` — comp @ 29.4 s, orange checker, typewriter "a four putt is pretty standard"
4. `comp12_golf-math_cover_opt4.jpg` — comp @ 16.3 s, rain cart, typewriter "gotta break 100"

## Swaps (not used)
- 7 26 20 111.35–117.95 "I do believe we're putting for bogey now, which is actually pretty good, considering I had that one shot with four yards forward progression because of the tree" (talk over address; never-posted six-months par 5 — its full original posts on @mackygolfs Oct 16 18:44 MT, so only use after that).
- 7 13 58 39.44–51.6 "literally no excuse not to be on the green in three" → shot → "and yet, on the green in four" (same joke as bit 1).
- Sep 21 7 24 34 13.0–15.46 "I think I've taken five shots already. Still can't see the hole." (spoken over two shots, a fairway shank and a bunker shot — would need ~12–19 s to keep both whole).
- golfclips IMG_6391 60.0–64.7 "about time I bring my putter out. I've lost count. I'm just trying to get this in the hole." (original not in this checkout; clips@654e995).
