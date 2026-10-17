# Compilation 15 — "Macky vs. course management" (new idea, Oct 17; FOR REVIEW, not posted)

- Why this idea: the idea list (1–12 + asmr + golf lingo) is used up (#8/#10 skipped per comp9/comp14 notes). New pattern found in the transcripts: her "strategy" talk — guessing yardage by eye, no rangefinder, sea-level/air-pressure club math, "shooting straight is the name of the game", "no choice but to whack it as hard as I can".
- Account: @mackthegolfer trial (default). Caption: **rangefinders are for people who don't have eyes** (picks a fight, per the Oct 16 caption rule).
- Video: `compilations/comp15_course-management.mp4` — 47.7 s, 5 bits, 1080x1920 30 fps, H.264 High crf 17 slow, AAC 192k 48 kHz, +faststart. ONE encode from the true originals with `tools/render_comp.py` (bits in `comp15_bits.json`). Loudness −16.0 LUFS, LRA 4.2.
- Sources: Golf Captions originals from `inbox/videos/` (.partNN rejoined, sha256 verified against the relay .sha256 for all 5 files; 9.7–11.2 Mbps).
- No text added, no shirt wipes, no music, no speed changes. Swearing kept ("holy shit holy shit"). Every shot kept whole: the only shot in the comp (bit 5, sand/tree recovery) runs address → swing → ball off the rake onto the green → her reaction. Bits 1 and 3 are talk-only during address/practice swings (checked frame by frame: the ball never leaves her feet inside the kept windows; the real shots come after the bit ends).
- Cuts only at measured quiet gaps (20 ms RMS) or her own scene cuts (frame-diff). Bit 3 is tightened at the pauses between her sentences ("sea… level water… water? what am I even saying? air pressure") with alternating 1.15 punch-ins over the jumps; no words cut.
- SPACING: green polo (San Angelo) → orange checker (Colorado) → green (San Angelo, other hole) → white/camo (Amarillo) → green (San Angelo). Never the same shirt back to back.

## Bits (in order)
| # | out (s) | source | src in–out (s) | what |
|---|---|---|---|---|
| 1 | 0.00–8.57 | Video Oct 12 2026, 12 05 56 AM.mov (green polo) | 34.533–43.10 (starts on her cut) | "all right, we're some amount of yards out. I don't know how to range find her, but I do have eyes and I would say it's a good distance" |
| 2 | 8.57–15.81 | Video Oct 11 2026, 9 02 57 AM (3).mp4 (orange checker) | 5.48–12.72 | "so I'm gonna tee off with a putter, then pitch a bunch of sevens till I get on the green, and then I'm putting with a driver. I don't really think I have the skill set for this, but let's see how I do" |
| 3 | 15.81–30.96 | Video Oct 12 2026, 12 11 12 AM.mov (green) | 81.567–85.50, 86.25–87.34, 87.90–92.10, 92.85–96.08 (1.15), 96.62–97.40, 98.04–99.96 (1.15) | "I really need to invest in a rangefinder because I feel like I'm right in between eight and nine iron territory. I went eight because I'm in Texas and I'm not used to these sea… level water… water? what am I even saying? air pressure. so I think that makes the ball go less far" |
| 4 | 30.96–36.68 | Video Oct 12 2026, 7 26 20 AM.mov (white/camo) | 67.90–73.62 (her cuts at 67.9 / 71.5) | "I don't see a flag, but I'm assuming the green is like right in front of me. shooting straight is the name of the game" |
| 5 | 36.68–47.53 | Video Oct 12 2026, 12 11 12 AM.mov (green) | 131.25–142.10 | "I think I have no choice but to just whack it as hard as I can" → the whole shot → "shout out to that rake, holy shit, holy shit… that rake just shot it up in the air straight onto the green" |

## Reuse
- No overlap with any posted/pending compilation or shorty window except bit 5's swing contains the 0.4 s contact hit comp13 r2 (asmr) uses (12 11 12 135.3–135.7). Bit 4 (7 26 20 67.9–73.6) and bit 2 sit next to, not inside, earlier windows (comp6 dropped 37.6–53.4; comp7 75.5–81.3 ends before bit 3). All bits < 15 s, so nothing uses up a never-posted video.

## Covers ("Macky vs. course management")
1. `comp15_course-management_cover_opt1.jpg` — comp @ 13.9 s, orange checker close-up, hands up "skill set", red pill
2. `comp15_course-management_cover_opt2.jpg` — comp @ 44.8 s, walking up after the rake shot, purple pill
3. `comp15_course-management_cover_opt3.jpg` — comp @ 33.5 s, white shirt under the clouds "shooting straight", blue pill
4. `comp15_course-management_cover_opt4.jpg` — comp @ 4.0 s, backswing on the fairway, typewriter "i don't have a rangefinder but i do have eyes"

## Spares (not used)
- 7 30 44 99.60–109.86 "I'm ecstatic to announce I'm bringing something other than a seven iron out of the bag, this is a pitching wedge and actually that's not true, it's a 56 degree" (+110.5 "I'm probably like 70 out")
- 7 16 02 44.3–55.6 "isn't there a rule that if you're close to a cart path you can drop the ball one club-length back. I don't want to be accused of cheating but also I've got a whole forest in my way"
- 12 14 03 22.9–30.1 "128 to the center, let's call it 120 into the hole"
- 12 05 56 88.4–97.8 "I really do need to invest in a range finder, I thought I was like 90 out" (after the shot)
