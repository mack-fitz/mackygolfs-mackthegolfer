# Compilation 21 — "Macky vs. the beach" (new idea, Oct 19; FOR REVIEW, not posted)

- Why this idea: the idea list (1–12 + asmr + golf lingo) is used up; comp15–20 were new patterns. New pattern from the transcripts: bunkers. Every bit is her going into, getting out of, or talking about the sand — "oh don't go in that sand motherfucker… yeah we're at the beach", "anytime I'm in a bunker I feel I need to bounce… six inches", "don't be in our bunker", "everything is bigger in Texas in regards to the bunker, but I forgot to make that joke".
- Account: @mackthegolfer trial (default). Caption: **if you say bunker shots are easy we can't be friends** (picks a fight, Oct 16 caption rule). Alt: "please help, i live at the beach now".
- Video: `compilations/comp21_the-beach.mp4` — 52.6 s, 4 bits, 1080x1920 30 fps, H.264 High crf 17 slow (~13.6 Mbps), AAC 192k 48 kHz, +faststart. ONE encode from the true originals with `tools/render_comp.py` + `COMP_FINAL_LIMIT=0.71` (bits in `comp21_bits.json`). Loudness −16.2 LUFS integrated, TP −2.7 dBFS; bits −16.1 / −15.3 / −21.0 / −15.6. Bit 3 (red shirt) is a quiet source (−35.6 LUFS, mostly ambience + one quiet line), so it got +8 dB on top of the capped +15 (`pg`); its line "don't be in our bunker" sits ~−20 LUFS — any more and the two club impacts get crushed by the limiter.
- Sources (true originals, sha256 verified vs the relay .sha256 after rejoining .partNN into tools/src/): golfclips copy_2CC073A6 (beach day, HEVC 11.2 Mbps), Video Oct 12 2026, 12 22 39 AM.mov (H.264 9.9 Mbps), Video Sep 21 2026, 7 28 37 PM.mov (HEVC 11.2 Mbps, single file), Video Oct 12 2026, 12 03 20 AM.mov (H.264 10.8 Mbps).
- No text added, no shirt wipes, no music, no speed changes. Every shot kept whole (bit 1 approach → full tracer into the bunker; bit 2 bunker shot → sand splash → "six inches"; bit 3 bunker shot → tracer, then the next shot → tracer). Cuts only in gaps between words (word timestamps in state/transcripts; beach day by 50 ms RMS gaps + her own scene cuts at 38.167 / 41.6). Swearing kept ("motherfucker", "putting this bitch").
- Punch-in 1.15 on bit 1 ("oh don't go in that sand motherfucker", src 33.6–38.167) and bit 2's ending ("I don't know, six inches… that's how terrible of a shot that was", src 128.0–134.4).
- SPACING: green striped polo (Colorado beach day) → dark green pinstripe (San Angelo par 5) → red Hawaiian (Colorado Sep 21) → dark green pinstripe (San Angelo par 4, other hole). No two same-shirt/day bits back to back.

## Bits (in order)
| # | out (s) | source | src in–out (s) | what |
|---|---|---|---|---|
| 1 | 0.00–14.70 | copy_2CC073A6 (beach day, green striped polo) | 26.60–33.60 + 33.60–38.167 (zoom) + 38.167–41.30 | "hopefully I can get pretty close to the green on this one" → approach → tracer → "oh don't go in that sand motherfucker… yeah we're at the beach" → (her cut) close-up "the lip's pretty small so I'm putting this bitch" |
| 2 | 14.70–32.60 | Video Oct 12 2026, 12 22 39 AM.mov (pinstripe) | 116.50–128.00 + 128.00–134.40 (zoom) | "I don't know how to do these, but for some reason anytime I'm in a bunker I feel I need to bounce, so whatever that means" → bunker shot → "a lot of you tell me to hit behind the ball, but would you look at that, I just did that, and it went… I don't know, six inches. You can still see it, I don't even need to move the camera, that's how terrible of a shot that was." |
| 3 | 32.60–41.63 | Video Sep 21 2026, 7 28 37 PM.mov (red Hawaiian) | 10.033–19.067 (her own cuts) | bunker shot out of the sand → next shot → "don't be in our bunker" |
| 4 | 41.63–52.50 | Video Oct 12 2026, 12 03 20 AM.mov (pinstripe) | 142.033–152.90 | "Dang, I actually just remembered it would have been funny if I said something about everything is bigger in Texas in regards to the bunker, but I forgot to make that joke. If you wouldn't mind going back in time and having a laugh, because that was pretty creative." |

## Reuse
- Not in any posted / scheduled / waiting compilation or shorty (checked every compilations/*bits*.json, comp13 r2 bits, shorties notes). Avoided on purpose: beach day 46.4–51.09 + 62.1–64.25 (comp1, posted Oct 13) — so the putt out of that bunker is NOT used; 12 22 39 109.95–111.80 "fuck that marshal" (comp1); 12 03 20 64.55–77.03 young-boys bunker shot (shorty group-watching, on hold); 12 03 20 108.2–123.75 (shorty chipping-tip, waiting).
- Only overlap: comp13 "asmr" (scheduled) uses the 0.4 s bunker-contact sound at 12 22 39 122.245–122.645, which sits inside bit 2's shot (can't cut a shot). Beach day 26.95+ was in comp4 (dropped, never posted).
- 7 28 37 is a never-posted red-shirt video; bit 3 is 9 s (< 15 s) so it doesn't use it up. All bits < 15 s except bit 2 (17.9 s of 12 22 39, an already-posted source: @mackthegolfer 2026-10-10 "LGB LOOSEY GOOSEY BABY #neverforget" https://www.instagram.com/reel/DeUZyg5xywP/, per state/posted_index.json).

## Covers ("Macky vs. the beach"; text kept off her chest, inside the grid crop; checked full size + grid size)
1. `comp21_the-beach_cover_opt1.jpg` — comp @ 13.2 s, close-up grin "the lip's pretty small…", bunker behind her, orange pill over her cap (0.14–0.20)
2. `comp21_the-beach_cover_opt2.jpg` — comp @ 20.7 s, sand exploding off her bunker shot, blue pill in the sky (0.18–0.23)
3. `comp21_the-beach_cover_opt3.jpg` — comp @ 34.5 s, red shirt in a huge bunker with the tracer, red pill in the clouds (0.19–0.24)
4. `comp21_the-beach_cover_opt4.jpg` — comp @ 9.7 s, typewriter "oh don't go in that sand" in the sky (0.17–0.27)

## Spares (not used)
- 12 22 39 94.70–99.76 "also you might have noticed I didn't actually land in the sand, so today's my lucky day" (pinstripe; left out to keep the length down)
- 12 11 12 102.06–111.72 "we'll see if it makes every single difference in the world" → approach → "I do think either club would have landed in the sand, so" (pinstripe)
- Sep 21 7 24 34 "oh nice, now we're at the beach" (voice-over runs across her cuts — no clean in-point without cutting the shot)
