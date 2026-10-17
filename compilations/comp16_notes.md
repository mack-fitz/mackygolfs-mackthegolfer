# Compilation 16 — "Macky vs. my comment section" (new idea, Oct 17; FOR REVIEW, not posted)

- Why this idea: the idea list (1–12 + asmr + golf lingo) is used up, and comp15 already took the first new idea. New pattern in the transcripts: her talking straight to the comments — telling them to shut up about the hat, daring them to guess high, worrying about the "uproar", asking what's up with her swings. Every bit is her addressing viewers, so the theme reads in each one on its own.
- Account: @mackthegolfer trial (default). Caption: **say something about my hat. i dare you** (picks a fight, per the Oct 16 caption rule).
- Video: `compilations/comp16_comment-section.mp4` — 49.6 s, 5 bits, 1080x1920 30 fps, H.264 High crf 17 slow, AAC 192k 48 kHz, +faststart, 14.0 Mbps. ONE encode from the true originals with `tools/render_comp.py` (bits in `comp16_bits.json`). Loudness −16.0 LUFS.
- Sources: Golf Captions originals from `inbox/videos/` (.partNN rejoined straight from git blobs, sha256 verified against the relay .sha256 for all 4 files; 8.1–11.2 Mbps).
- No text added, no shirt wipes, no music, no speed changes. Swearing kept ("didn't say shit to me", "absolute asshole"). The only shot in the comp (bit 5, the bogey putt) runs address → putt → drop → her reaction. Bits 2 and 3 are talk during address/practice swings (frame-checked: the ball stays at her feet inside the kept windows; the real shots come after each bit ends).
- Cuts at measured quiet gaps (20 ms RMS) or her own scene cuts (frame-diff). Bit 2 drops 0.25 s of the pause between her two sentences, with a 1.15 punch-in over the jump. No words cut (word timings from state/transcripts).
- SPACING: green pinstripe polo/black cap (12 11 12) → white shirt/camo (Amarillo, 7 17 58) → dark green polo/"Bad" hat (12 17 30) → green pinstripe (7 30 44) → white/camo (7 17 58, other hole). Never the same shirt back to back.

## Bits (in order)
| # | out (s) | source | src in–out (s) | what |
|---|---|---|---|---|
| 1 | 0.00–9.17 | Video Oct 12 2026, 12 11 12 AM.mov (cart selfie) | 112.08–121.25 (her cuts at 112.067 / 121.267) | "another thing, because everybody always tells me I need to turn my hat around and tuck my shirt in, this golf course does have a strict dress code, and that was a marshal and he didn't say shit to me. so you guys all need to shut up" |
| 2 | 9.17–20.33 | Video Oct 12 2026, 7 17 58 AM.mov | 8.59–13.75, 14.00–20.00 (1.15) | "I'm basically gonna try to just whack it with my eight iron straight into the hole. that way anybody who guesses above one looks like an absolute asshole" |
| 3 | 20.33–28.78 | Video Oct 12 2026, 12 17 30 AM.mov | 43.55–52.00 | "I'd actually love to just putt this, but I can only imagine the uproar in my comment section if I were to do that" (ends before her backswing) |
| 4 | 28.78–38.70 | Video Oct 12 2026, 7 30 44 AM.mov | 155.59–165.51 | "genuinely though please let me know like what's up with all of my swings, because I do want to be better, that's all I live for, is being the best in the world" (ends before the putt) |
| 5 | 38.70–49.53 | Video Oct 12 2026, 7 17 58 AM.mov | 100.95–111.78 (to the end of her file) | bogey putt drops → "bump bump" → "I'll take a bog, I will take a bog. did you guess a four? because if you guessed higher than a four, you're a…" |

## Reuse
- Not in any posted/pending compilation or shorty. Overlaps only with dropped/superseded cuts: comp11 (dropped) 7 17 58 14.16–19.6; comp7 r3/r4 drafts (superseded — posted r5 cut it) 7 17 58 8.75–13.55; dropped shorty not-to-putt-it starts at 12 17 30 52.1 (after bit 3). comp1 (posted Oct 13) uses 12 17 30 154.6–165.1 (different moment). All bits < 15 s, so nothing uses up a never-posted video.
- B's 026 re-edit of 12 17 30 is planned Sun Oct 18 on @mackthegolfer — don't post this the same day.

## Covers ("Macky vs. my comment section")
1. `comp16_comment-section_cover_opt1.jpg` — comp @ 7.4 s, cart selfie on "you guys all need to shut up", red pill
2. `comp16_comment-section_cover_opt2.jpg` — comp @ 48.3 s, leaning into the camera "you're a…", purple pill
3. `comp16_comment-section_cover_opt3.jpg` — comp @ 31.5 s, on the green by the flag "let me know", blue pill
4. `comp16_comment-section_cover_opt4.jpg` — comp @ 6.2 s, cart selfie, typewriter "you guys all need to shut up"

## Spares (not used)
- 7 26 20 27.87–35.9 "most of my drives do not look like that. I think I was really feeling the weight and pressure of you telling me that I was a decent golfer"
- 12 11 12 62.7–75.1 "I do just want to float this in front of my mostly male audience…" (lesson from the old guy)
- 12 05 56 4.9–13.7 "you gotta lock your guess into the comments before I hit my drive, otherwise that's cheating… cheaters never win. I think that's from the Bible"
- 12 22 39 123.6–134.0 "a lot of you tell me to hit behind the ball, but would you look at that… six inches" (needs the bunker shot before it)
