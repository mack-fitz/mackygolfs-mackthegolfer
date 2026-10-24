# Trial reels playbook — @mackygolfs (A) + @mackthegolfer (B), Instagram only

Operating rules for the trial-reel accounts. The daily task reads this file first.

## REPEAT RULE (Mack, Oct 20: 30 DAYS) — HARD RULE. Full text: HARD RULES at the BOTTOM of this file (they win).
- Pool = Instagram @mackygolfs + @mackthegolfer ONLY. A reel (any version: original, re-edit, Mack's own post) may not post
  on either account within 30 days, before or after, of any version of it on either account, AND it is not eligible at all
  (review page or schedule) if any version posted on those two accounts in the 30 calendar days before TODAY.
  Least-recently-used first. Shorties and comps are exempt. Main accounts use ONLY /Golf Captions (HARD RULE 12). TikTok, @moremackygolfs, X and FB don't count and aren't restricted by it.
- Exact-duplicate guard per account: the same file never posts twice on the same account.
- Run `tools/check_repeats.py` before scheduling, moving, or putting anything on the review page.

Source videos: Dropbox `/Golf Captions` (captioned by Mack). Media is served to Zernio from
https://raw.githubusercontent.com/mack-fitz/mackygolfs-mackthegolfer/main/... (URL-encode spaces).
Tools: `tools/render.sh src segs.json "" "" out.mp4` (segments `[start,end,zoom]`, empty hooks =
no text) and `tools/snap.py` (snap cuts to the quietest point). Never mid-word cuts.
Cross-check: also clone mack-fitz/clips (read only) to see what @moremackygolfs has posted
(state/schedule.json, queue/) so this account's versions differ from those cuts and covers.

## Trial reels: @mackygolfs (A) and @mackthegolfer (B) on Instagram
Two Zernio profiles, one per account: "mackygolfs" (6acce3f0662265cf261fca4a) holds A (account 6acce837f3bd55021dad245f),
"mackthegolfer trials" (6acce6402daf1733722343d0) holds B (account 6accea22c485191e985aa1cb). Get account IDs with accounts_list
filtered by profile, and always post by exact account ID: a B edit must never land on A. Trial reels ONLY on these two accounts; @moremackygolfs keeps posting
regular reels from the mack-fitz/clips repo. X and TikTok setups are not touched by any of this.

- **Source:** Dropbox `/Golf Captions`, captioned reels
  only. Pull in random order. Relay via `inbox/want.txt` (names only), files land in
  `inbox/videos/`. Track in `state/trials.json` (secret DROPBOX_FOLDER_URL holds the folder link; per reel: Dropbox ID, A version + date + post ID,
  B version + date + post ID, opening style, A `cover_words` (the words on the cover, "" for none),
  views/shares/saves/watch time when available).
- **NO burned-in text on any A or B video.** Render with `tools/render.sh src segs.json "" "" out.mp4`
  (empty hooks = nothing drawn). Don't add hook text, subtitles, captions or labels to
  the picture. Mack's own captions already in the video stay as they are. (Cover words on A's
  cover image are allowed for the cover test; that's the cover, not the video.)
- **A (@mackygolfs):** post the original, unedited, opening on the shirt wipe ALWAYS.
  **A's cover is ALWAYS a shirt-wipe frame.** Test cover words: alternate covers with 1-3 blunt
  words (big, inside the center square) and covers with no words; record `cover_words` per reel
  in state/trials.json and compare views weekly, then lean toward the winner (keep testing ~1 in 4). If the reel
  looks like it was already posted on A (compare against A's existing reels), make a different edit
  for A instead: new cut points and punch-ins, still opening on the shirt wipe.
- **B (@mackthegolfer):** its own clean edit. NEVER the shirt wipe. ALWAYS open on Mack talking:
  the first spoken line right after the wipe (no teasers, no cold opens; Mack, Oct 13). Fully clean: no innuendo in captions,
  nothing suggestive in covers, no OF tie-in, no story shares or links to A or the other accounts.
- **Every IG account gets its own version.** If a reel has also gone out on @moremackygolfs (or
  the other trial account), make sure cuts and cover differ from those versions. Never skip a reel
  for being a duplicate: re-edit it.
- **Assignment is random, never by length or anything else.** When picking today's reels, shuffle
  and assign by coin flip.
- **Order: each account pulls randomly on its own.** B is NOT staggered behind A. Each day pick
  B's reels at random from everything in /Golf Captions not yet used on B (same for A). The only
  rule: never post the same reel on both accounts on the same day.
- **Pace:** **[SUPERSEDED Oct 23 by POSTING RULES v2 at the bottom: weekly folders, 1 morning 7:00-8:30 + afternoons 2:00-3:30 MT]** start at 3 trial reels a day per account (A ~7:30-8:00am, 1-2pm, 6:30-7:30pm MT; mornings early to catch the East Coast;
  B offset by ~45 min). Raise to 4-5 a day only if reach holds and no Account Status warnings.
  Stay under 10 a day.
- **Posting:** Zernio posts_create_post, instagram, platformSpecificData
  `{"trialParams": {"graduationStrategy": "MANUAL"}}` (NEVER auto-share: Mack shares
  trials to followers himself. Never use SS_PERFORMANCE.), `instagramThumbnail` for the cover. Captions: same dumb lowercase voice,
  no hashtags or links.
- **Weekly review:** compare A vs B and the two B openings; say which trials graduated.

### Dashboards
- A (@mackygolfs): "Mackygolfs Trials" https://claude.ai/artifact/UjxPU7xShmePKLoJhjQFwc
- B (@mackthegolfer): "Mackthegolfer Trials" https://claude.ai/artifact/UsvudPUSVtCX3yPFqj4Knc
Stats and followers are live Zernio queries scoped to each profile_id (nothing to refresh). Two file
datasets per dashboard need refreshing by the daily run: `trials` (trial log: cover test for A,
opening test for B, built from state/trials.json) and `upnext` (scheduled trial reels, time in MT).
Build them with `tools/dash_trials.py` (see its header).

### Trial pipeline (daily task "Golf trial reels daily run")
1. List `/Golf Captions`; new = file IDs not in state/trials.json. Relay a few at a time (only what
   the next 3 days need, plus 2 spare) via `inbox/want.txt`; wait for "Fetch inbox videos";
   copy files out of inbox/videos, `git rm -r inbox/videos`, commit, push.
2. Check against A's existing reels: try pulling A's Instagram media (analytics_get_analytics for
   A's account, source "all", or posts_list for that profile) and compare thumbnails/captions/
   length. If it can't be checked, treat the reel as new for A.
3. Make the versions: A = original (untouched file whenever possible, shirt wipe first) or, if already
   on A, a different edit that still opens on the wipe. B = clean edit, no wipe (opening per rules).
   Covers: A = shirt-wipe frame (words on/off per the test); B = plain strongest frame, no text, never the wipe. Save to trials/NNN_slug_{a,b}.mp4 + _{a,b}_cover.jpg.
4. Schedule (run tools/check_repeats.py --candidates FIRST — HARD RULE 5 at the bottom; nothing that fails goes on the review page or into Zernio): keep 3 days of slots filled on each account, each picking its own random reels
   (never the same reel on both accounts the same day). posts_create_post with the account's exact ID and trialParams. Record in
   state/trials.json.
5. Refresh both dashboards' trial file datasets (after scheduling and recording in state/trials.json):
   for each account (A → UjxPU7xShmePKLoJhjQFwc, B → UsvudPUSVtCX3yPFqj4Knc):
   - `python3 tools/dash_trials.py trials A /tmp/dash/a/trials.json` (B likewise).
   - Zernio posts_list_posts with that account's profile_id (limit 50, sort_by "scheduled-asc"),
     save the raw answer to a file, then `python3 tools/dash_trials.py upnext A <answer file> /tmp/dash/a/upnext.json`.
   - Upload each JSON as an asset to that dashboard (Artifact publish, `url` = the dashboard, `asset: true`).
   - ArtifactData: `get` datasets/trials and datasets/upnext, then `update` each (pinned with
     if_version) with `source.url` = the new `/_blob/<id>` url, `source.name`, and
     `updated: {at: <ISO now>, by: "Claude"}`. Don't touch the posts/followers queries or the page.
6. Fix it yourself rules apply. Then message Mack in the same short format as the main run.

## Editing rules (B edits, and A re-edits)
- A re-edits: open on the shirt wipe, then the first full sentence (no wipe in the source: strongest action).
  B (@mackthegolfer): never the wipe — open on her first spoken line (rules below).
- Never start or end a cut mid-word or mid-sentence. Cut only on measured audio
  pauses (no transcription available — snap cuts to the quietest point nearby).
- Tighten: remove filler talk, dead air, waiting between shots. Keep every shot
  with its tracer fully visible (strike to landing), and every payoff line.
- Punch in ~15% on reaction moments.
- NO hook text, NO subtitles, nothing burned in (Mack's rule for these accounts).
- Keep Mack's captions untouched (they sit mid-frame).
- Target length: tight, usually 30–70s depending on the story.
- Cover: strongest frame (action or reaction, never suggestive out of context), no text.
- Export once, high quality: `tools/render.sh` (libx264 -crf 17 -preset slow, source resolution/fps, AAC 192k 48 kHz). No bitrate caps, no double encodes. (Oct 23: see Quality in POSTING RULES v2 — level 4.2, AAC 256k, originals untouched.)

## Captions (all platforms)
- Dumb, short, lowercase, Mack's voice. Reference style: "golf is so easy guys",
  "6 is basically par".
- NO hashtags. No links. No OnlyFans mentions or innuendo.

## Account safety
- No bio link (Mack's choice). No fake engagement, no automated scrolling.
- Watch for: failed posts, account health issues, sudden non-follower reach drops.
- Remind Mack to check Instagram Account Status weekly.

## Fix it yourself (Mack's standing rule)
Mack should never have to tell you to circle back. Every run, before messaging him:
- **Failed posts:** find them (posts_list_failed, and any post in this account's schedule whose
  status is failed/error). Fix the cause (re-encode or shrink media, swap a broken media URL for a
  pinned-commit raw URL, re-crop, shorten a caption) and reschedule into the next open slot, or the
  same slot if it hasn't passed. Retry transient errors once; if it fails again, change approach.
- **Empty slots:** every slot for the next 3 days must have a post. Fill any gap.
- **Bad content:** anything that breaks the rules here (AI tells, wrong crop, cut mid-word, hook
  under the audio bar) gets replaced or re-edited before it goes out.
- **Disconnected account / expired token:** this is the one thing you can't fix — tell Mack
  exactly what to reconnect.
- In the message, report fixes as done ("Thursday 8pm was empty — filled it with X"), not as
  questions. Only ask Mack for things you truly can't do.


## Macky To Do page
**Macky To Do** (https://claude.ai/artifact/NkJnRhgLLfSWz1XXfHbQ79): every run, ArtifactData `update` this account's doc in collection `queues` with `days_left` (number), `detail` (one plain line: what is left and the pace) and `updated` ("Mon D"). Sundays: add 2-3 new docs to `ideas` (fields order, title, where, effort, what, why) that fit Mack's masc/dry/silly vibe. Doc id(s) for this repo: trials-mackygolfs and trials-mackthegolfer.

Base Camp schedule (same page): every run, ArtifactData `set` collection `schedule`, doc id(s) mackygolfs and mackthegolfer, to `{items: [{date: "YYYY-MM-DD" (Mountain), time: "HH:MM" 24h Mountain, caption, where?}]}` covering today and tomorrow for that account. The page is now named "Base Camp".

## Duplicate check (MANDATORY before scheduling any trial)
Instagram buries reposts. Golf Captions overlaps heavily with what Mack has ALREADY posted himself
(Oct 12: the "lag masta", "Bomb City", "blue ball", "mama didn't raise" and "wet or dry" reels were all
already on @mackthegolfer; "new shirt" and "absolutely brutal" were already on @mackygolfs).
1. Pull the target account's full post history: analytics_get_analytics(profile_id, source "all",
   limit 100, paginate) -> each post's caption + videoDurationSeconds. Also pull the other
   golf accounts (@moremackygolfs, the other trial account) for the last 30 days.
2. A reel is a LIKELY DUPLICATE if its length is within 3 s of a post on that account AND the
   content matches (same course/outfit/story/line: read your contact sheet and Mack's caption
   on that post), or the caption plainly describes the same moment.
3. Likely duplicate on the SAME account: never post it as-is, and don't post a light re-edit
   either. Use it only inside a genuinely new edit (see compilations below), or skip it.
4. Same footage on any other account in the last 7 days: skip it for now. (For @mackygolfs/@mackthegolfer the
   30-day pool rule in HARD RULES 1-2 applies and wins.)
5. Log every check in state/trials.json (`dup_check`: matched post date + caption, or "clear").

## What to post (Mack's rules, Oct 12) **[SUPERSEDED Oct 23 by POSTING RULES v2 at the bottom: weekly folders, 1 morning 7:00-8:30 + afternoons 2:00-3:30 MT]**
- NO compilations for now.
- PRIORITY 1: UNUSED reels (never posted on any of Mack's accounts: check @mackygolfs and
  @mackthegolfer full history per the duplicate check). Most unused reels go to @mackygolfs
  (as originals, shirt wipe first), but give @mackthegolfer some too (about 1 in 3 unused reels).
  An unused reel can go to both accounts on different days.
- Unused footage NEVER goes to @moremackygolfs.
- Only once unused reels run out: already-posted reels, following the duplicate rules above
  (never on the account that already posted it).
- @mackthegolfer edits must be CLEARLY DIFFERENT from the original, not just the wipe trimmed:
  opening on Mack's first spoken line after the wipe (never a cold open), restructured middle where the story
  allows, 25-40% of the runtime cut (dead time, walking, setup, repeats), punch-ins on 3+
  moments, a different end beat, a different cover. Before posting, compare your edit to the
  original side by side (contact sheets): if a viewer would recognize it as the same video in
  the first 3 seconds, re-edit.
- The unused "putting with a driver" video (golfclips 010_wrong-clubs, find it in Golf Captions
  by content/length ~99.5 s) was pulled from @moremackygolfs: use it on the trials.

## Length test (Mack, Oct 13) **[SUPERSEDED Oct 23 by POSTING RULES v2 at the bottom: weekly folders, 1 morning 7:00-8:30 + afternoons 2:00-3:30 MT]**
Each day, of each account's 2 trial reels, one must be SHORTER and one LONGER, so Mack can compare.
- Shorter = under ~35 s; longer = over ~60 s (A: pick never-posted originals that naturally fall in each range; B: pick source videos and edits that land in each range — still 25–40% cut from the original).
- Alternate which slot (morning/evening) gets the short one day to day. Log `length_test: "short"|"long"` and the final duration on each entry in state/trials.json, and report short-vs-long views/skip rate in the daily message.
- This is a deliberate test; it does not change the rule that videos are otherwise picked at random within each length range.

## COVER TEXT NEVER OVER HER CHEST (Mack, Oct 17) — overrides every placement note below
Mack, Oct 17: "You've been putting the text over my cleavage a lot." Her chest / cleavage / bra must stay visible on EVERY cover (A, B, compilations, shorties, and @moremackygolfs).
- Put the words over the shirt-over-face / head area ABOVE the chest, or BELOW the chest (stomach/waist/lower frame), whichever is clear. Never across the chest.
- The whole text block stays inside the centered 3:4 grid crop (the profile grid shows the middle 1080x1440 of a 1080x1920 cover = 12.5%–87.5% of the height) and below Instagram's top bar (block no higher than ~15%).
- Find the chest per image by LOOKING at the frame: `tools/cover_a.py --guide video t guide.jpg` draws %-of-height lines and the grid crop. The chest moves from video to video; never reuse a y from another cover. cover_a.py has no default position: `COVER_Y` is required and checked (0.15–0.85, block inside the crop). If no clear spot exists on that frame, use a nearby frame.
- Verify every new cover before it goes anywhere: view it at grid-thumbnail size (center 1080x1440 crop at ~240–360 px wide) AND full size, and confirm the chest is clear in both.
- "Mid-frame (45–70% down)" in older notes below is replaced by this rule.

## Cover text style (Mack, Oct 13)
Cover words copy Mack's own @mackygolfs grid (screenshot: covers/grid-reference.png — Read it before making covers). Three styles she uses, placed inside the center 3:4 grid crop and NEVER over her chest (see the Oct 17 rule above: over the shirt-over-face/head area or below the chest):
1. **"Macky vs. ___" pill** (her main series): "Macky vs. a Par 4", "Macky vs. a 7 iron", "Macky vs. the LPGA", "macky vs. a chili cheese dawg", "Macky vs. Something that Should Have Stayed a Draft". Bold rounded sans (Poppins Bold/SemiBold is close), white text on a solid rounded-corner color box (orange #F7931E, red #E8101A, yellow #F5C518 with white text, purple #A21CAF, blue #1E90FF). Rotate colors; 1–2 lines.
2. **Typewriter note**: lowercase monospace black text on a plain white rectangle, deadpan quote/thought, e.g. "i'm so wet :/", "does anyone on instagram know what lag means", "i was served dry burger". Use a monospace font (DejaVu Sans Mono or similar).
3. **Big question**: heavy italic red text with white outline, right-aligned, stacked one word or two per line, e.g. "Is Macky about to be soaking wet?" Use sparingly.
Mostly use style 1, some style 2, rarely 3. Words fit the specific video (the hole, club, food or situation). @mackthegolfer covers: same styles but brand-safe (no "wet"/innuendo; never a shirt-wipe frame). "No words" covers stay as the on/off test for A.

## CURRENT RULES (Mack, Oct 13, 12am) — override anything above that conflicts
**[SUPERSEDED Oct 23 by POSTING RULES v2 at the bottom: the 2/day morning+evening slots, short/long test, A = 1 new + 1 re-edit, B = re-edits-only rotation and the 3-day spacing are replaced. Approval flow, never cut shots/swearing, and B opening rules still apply.]**
- Exactly 2 trial reels per day per account (morning + evening). Never 3. No midday.
- Every day, on EACH account: one SHORT (under ~35 s) and one LONG (over ~60 s). Alternate which slot gets the short one.
- @mackygolfs (A): never-posted footage only, Mack's original untouched.
- @mackthegolfer (B), for now (until Mack says otherwise): ONLY re-edits of footage Mack has ALREADY POSTED herself (on @mackygolfs/@mackthegolfer, or via @moremackygolfs/X/TikTok). Never never-posted footage on B. Each re-edit must be clearly different from every existing version (restructure, 25–40% cut, 3+ alternating punch-ins, different open/end/cover; side-by-side check). Don't reuse B's own earlier trials.
- Never the same footage on both accounts within 3 days.
- Schedule only today and tomorrow.
- NEVER cut swearing or profanity out of any edit (Mack, Oct 13). Keep her words as she said them; cuts are only for pacing/structure, at quiet gaps.
- @mackthegolfer (B) OPENING (Mack, Oct 13 10:18am): ALWAYS open on Mack talking at the beginning (the first spoken line right after where the shirt wipe would be). NO cold opens, NO teasers of later moments, NO "cut to the end" openings. Restructure only after the opening (trim, tighten, reorder the middle, change the ending, punch-ins).
- TWO-INTRO VIDEOS (Mack, Oct 13): some new uploads will have two intros back to back at the start (often "2 intros" in the file name; a pause or clap separates them): first = shirt-wipe while talking, second = just talking (no wipe). Split them: @mackygolfs (A) = intro 1 + the rest (remove intro 2 only; otherwise unedited, Mack's quality untouched where possible); @mackthegolfer (B) = intro 2 + the rest, edited per B rules. These count as NEW footage for both accounts; post the two versions at least 3 days apart. Check every new upload for a second intro even without the file-name tag.
- BASE CAMP QUEUE COUNTS (Mack, Oct 13): trials-mackygolfs days_left = never-posted videos left (A uses 1 new per day), warn_under_days 3; detail says how many new videos are left and that the other daily slot is a re-edit. trials-mackthegolfer = already-posted source videos not yet re-edited on B ÷ 2 per day, capped at 30; it is NOT low just because Golf Captions is used up (B can re-edit Mack's whole @mackygolfs/@mackthegolfer history).
- [SUPERSEDED Oct 23 by POSTING RULES v2] ONE NEW VIDEO A DAY ON A (Mack, Oct 13 11am, "just do one new video a day on mackygolfs for now"): @mackygolfs (A) gets exactly ONE never-posted video per day. A's other daily slot is a RE-EDIT of already-posted footage (Mack's own posts on any account, or @moremackygolfs/X/TikTok; never footage A itself already posted; never the same footage as B within 3 days), still opening on the shirt wipe, A cover style, clearly different cut. Short/long rule still applies across the two. B = re-edits of already-posted footage only (the two-intro B version above is the one exception).
- APPROVAL (Mack, Oct 13 11am, "I want to see and approve everything you are posting on mackygolfs/mackthegolfer"): NOTHING posts on A or B unless Mack approved that exact reel (video, cover, caption) on the **Trial Reels Review** page (https://claude.ai/artifact/Ez1N5G9ywcawNCaEjT15qg).
  - Every evening the prep run ("Trial reels nightly prep for review", 6:47pm MT) makes the NEXT day's 4 reels (2 A + 2 B: per account one short + one long, morning + evening) and has them on the review page by **9:00pm Mountain (10pm Central)**, then messages Mack the link.
  - [SUPERSEDED Oct 23 — see clips RULES.md §8] NO Zernio drafts: Never create a Zernio post (draft or scheduled) for anything Mack hasn't approved. On approval, create and schedule it in one step. Until then keep file + planned time on the review doc / state/trials.json.
  - Review page data: ArtifactData on the review page, collection `reels`, one doc per reel, id `YYYY-MM-DD_{A|B}_{am|pm}`. Claude writes: date, account, handle, slot, time_mt, time_ct (MT+1h), length (short/long), duration, kind (new/re-edit), reuses (one plain line: what footage, where/when it was posted, what's different), caption, cover_note, video_url/cover_url (`/_blob/<id>` from an Artifact asset upload; videos as 540-wide preview copies under ~14 MB, covers 720 wide), video_asset, cover_asset, file, cover_file, media_url (pinned raw URL), zernio, status (ready|scheduled|posted|dropped), round (1, +1 each fix), history []. Mack writes: decision (approved|changes|null), notes, decided_at, decided_round.
  - Approved (decision "approved" AND decided_round == round): create and schedule it in Zernio in one step at its planned time (posts_create_post with `scheduled_for` + `timezone: "America/Denver"` + trialParams MANUAL + pinned media/cover URLs), set the doc's status "scheduled", record in state/trials.json.
  - Needs changes: apply the notes (re-edit / new cover / new caption, re-upload preview assets; no Zernio post yet), push `history` {round, decision, notes, fix}, round+1, decision null, status "ready" — it shows again on the page. Message Mack that it's fixed and ready for another look. Never schedule a fixed version she hasn't approved.
  - No decision: no Zernio post exists, so it never posts. If the slot passes, drop it (status "dropped"; footage goes back to the pool).
  - The 5:38am daily run ONLY schedules approved reels (and applies notes); it never creates scheduled posts on its own. Approvals that came in late still get scheduled that morning; if the planned morning time is under ~10 minutes away, shift it up to 30 min later. Tonight's evening posts already scheduled before Oct 13 11am are grandfathered.

- NEVER CUT OUT SHOTS (Mack, Oct 13): every golf shot/stroke in the source must stay in the edit (tee shots, approaches, chips, every putt, penalty drops). Her comments refer to them, so cutting a shot makes the talking make no sense. Only cut dead air, walking, waiting, ball-searching and pauses between sentences. This applies to every account and every edit, including re-edits and compilations.
- REVIEW FLOW (Mack, Oct 13 noon — standing rule):
  * Every trial reel (A and B) goes on the Trial Reels Review page (https://claude.ai/artifact/Ez1N5G9ywcawNCaEjT15qg, hole 6 in Macky HQ) for Mack to Approve or leave notes. Nothing posts on A or B without her approval.
  * Stay AHEAD: the next day must ALWAYS be fully prepared and on the review page (at minimum by 9pm Mountain the night before). Work ahead as far as possible — up to 7 days out — whenever footage allows. The day before posting is for working through her notes.
  * When Mack leaves notes: apply them, put the new version back on the review page (round +1, decision reset), and then SendUserMessage her: "Your notes are done — [which reels] are ready to re-review" so she knows to look again. Always notify after notes are applied.
  * Approved reels get scheduled in Zernio at their planned time (trialParams MANUAL). Unapproved reels never post; if a reel isn't approved by its slot, skip that slot and tell her.

## COMPILATIONS (Mack, Oct 13) — make a bunch over the next week
Why: compilations avoid the duplicate flag that single re-posts get. Mack wants many.
- Format (proven by comp #1 "what it's like playing with me", which she loved): HER TALKING while playing; 2–7 s bits back to back; 30–45 s; open on the strongest bit; never cut a shot out of a setup→shot→result bit; never cut swearing; no wipe needs to be added (Mack, Oct 21: comps are exempt from the wipe rule; one already in the source is fine, the shirt-wipe montage comp is its own thing), NEVER a wipe in @mackthegolfer versions; no text burned in; even loudness; 1080x1920 30 fps crf 17. Method + sources: compilations/comp1_notes.md.
- Cover: strong face/reaction frame + the title in her grid style (white bold Poppins on a rounded colored box, inside the grid crop and never over her chest — Oct 17 rule; rotate colors). Always give 3+ cover options. Caption: short, lowercase, dry (her edit of comp1: "why do I like this sport").
- Every compilation goes on the review page (https://claude.ai/artifact/Ez1N5G9ywcawNCaEjT15qg, collection "compilations") for her notes/approval; notify her when one is up or when notes are applied. Nothing posts without approval. Default account: @mackthegolfer trial unless she says otherwise (the shirt-wipe one is for @mackygolfs).
- Don't reuse the same bit in two compilations that would post within 2 weeks of each other.
- Idea list (work down it; skip any already made; add new ones as you find patterns in the footage):
  1. what it's like playing with me (done — comp1)
  2. what it's like being delusional — confident line → shot → disaster (comp2)
  3. every excuse I've ever made — blaming wind, ball, bounce, marshall, course
  4. me talking to my golf ball — "stop stop stop", "get in", "sit", "go"
  5. what it's like golfing with me in the summer — shirt-wipe montage (@mackygolfs; caption "sorry I'm so wet")
  6. worst bounces / the course hates me
  7. "that's not bad" — her rating her own bad shots generously
  8. almost moments — lip-outs, almost eagle, almost hole-in-one
  9. me vs. putting — every putt drama, the "lag master"
  10. me hyping myself up before a shot (then the result)
  11. guess my score — her asking viewers to guess, with the reveals
  12. golf math — "6 is basically par", "a double is par in texas", scores talk
- SOURCE QUALITY (Oct 13): every edit (A, B, compilations) must be cut from Mack's TRUE original file (Dropbox original fetched byte-for-byte via the fixed relay, or rejoined .partNN pieces). NEVER edit from clips repo queue/*_full.mp4 or any file the old relay re-encoded (~4 Mbps). Before rendering, ffprobe the source: if video bitrate < 8 Mbps for 1080x1920 it is a shrunk copy — re-fetch the original first. Log source bitrate in state/trials.json.
- COMPILATIONS FILL TRIAL SLOTS (Mack, Oct 13): approved compilations count as fresh content and can fill trial slots on @mackygolfs or @mackthegolfer (per the compilation's account). When planning days ahead, mix them in, especially once A runs out of never-posted videos (A then = re-edits + compilations). Re-edits are fine with Mack.
- BASE CAMP SYNC (Mack, Oct 13): whenever a reel or compilation is approved/scheduled/posted, immediately update Base Camp's schedule (ArtifactData https://claude.ai/artifact/NkJnRhgLLfSWz1XXfHbQ79, collection "schedule", docs "mackygolfs"/"mackthegolfer"/"golf" — read for if_version, keep existing items, add {date, time HH:MM Mountain, caption, where}). The review page only shows items waiting on Mack; approved items live in Base Camp's schedule.

## MACK'S COMPILATION IDEA — "golf lingo" (Mack, Oct 13) — add to the END of the compilation idea list (does NOT jump the line)
- Bits where Mack uses her hands/body to act out what the shot needs to do: sticking her butt out, "bump and roll", "just up and over", etc. Lots of these are in the ORANGE CHECKERED SHIRT videos — use them, plus bits from other outfits/days.
- SPACING (Mack): do NOT put the orange-checkered-shirt bits back to back. Alternate outfits/days so it's clear this is over many rounds — no two consecutive bits from the same shirt/day where avoidable. (Applies to all compilations.)
- Cover text: something about golf lingo to use on your next round (e.g. "golf lingo to use next round"); 3+ cover options in her grid styles.
- Caption: "make sure to really get your hips involved"
- Usual compilation rules: her talking, never cut a shot or swearing, no wipe added (comps exempt; never a wipe on @mackthegolfer; Oct 21 rule at the bottom), no added text, true originals, single high-quality export.
- BASE CAMP — COMPILATIONS (Mack, Oct 13): every compilation that posts or gets scheduled must appear in Base Camp's schedule on its account's doc, with where = 'trial reel (compilation "<title>", posted)' (or 'scheduled'), time in Mountain, and its caption. Do this in the same run that posts it.
- NEW-VIDEO FOLDER (Mack, Oct 14): as Mack gets new videos back from the tracer, she'll put them in a NEW SUBFOLDER inside the trial reels Dropbox folder (/Golf Captions). Anything in a subfolder she adds = guaranteed never posted — use those first for "new" slots, no guessing needed (still log them in state/never_posted.json; once used, mark used). Check for new subfolders every run. Until then, never-posted status comes from the fingerprint check (DUPLICATE CHECK V2). Goal she's working toward: ~28 brand-new videos a week so BOTH @mackygolfs and @mackthegolfer get only brand-new videos (2/day each, never the same video on both) — but B stays re-edits-only until she says to switch.

## DUPLICATE CHECK V2 (Oct 14) — overrides "Duplicate check" above and any length/caption-based check
Why: the Oct 14 @mackygolfs reel "please send broomstick putter recs" (010) was called "never posted" because the
old check matched mostly on video length. It was the same footage @mackthegolfer posted Oct 13 (3-day rule broken).
- **Never-posted status comes ONLY from `state/never_posted.json`.** That file is built by fingerprint-matching every
  Golf Captions source against EVERY post on all three IG accounts (@mackygolfs 6acce837f3bd55021dad245f,
  @mackthegolfer 6accea22c485191e985aa1cb, @moremackygolfs 6acc2885bac230e9d1133105). A source not in that file is
  already posted, full stop. (Mack's new-video subfolders in /Golf Captions are guaranteed never posted: add their
  files to `state/fp/sources_meta.json` so they get fingerprinted and land in never_posted.json; once one posts, the
  next refresh drops it because it matches its own post.)
- **Never judge by length or caption.** Not for "never posted", not for "already on this account", not for the 3-day rule.
- **Fingerprint** = chromaprint audio (fpcalc -raw) + perceptual hash of a frame every 2 s (`tools/fingerprint.py`).
  Match rule (`tools/match_fp.py`): ALREADY POSTED if one aligned audio stretch is > 5 s, or aligned >= 3 s stretches add
  up to >= 12 s (re-edits), or >= 8 s of changing frames line up. Calibrated Oct 14: unrelated videos never pass.
- **How the index is built** (`tools/posted_index.py`, header has the exact steps): Zernio analytics_get_analytics per
  account, source "all", limit 100, every page, 366-day windows back to the first post -> `posted_index.py want` writes
  `fp/want_posts.tsv` (fresh mediaItems video URL, else yt-dlp on the permalink, else the thumbnail; IG CDN URLs expire,
  so fetch them from Zernio right before pushing) and `fp/want_sources.txt` -> push -> the **fingerprint** workflow
  (`.github/workflows/fingerprint.yml`) downloads, fingerprints and commits ONLY the small JSON under `state/fp/`
  ("Fingerprints [skip ci]"; never commit IG videos) -> pull -> `posted_index.py build` -> `state/posted_index.json` +
  `state/never_posted.json`. Posts that went out but are gone from IG go in `state/fp/manual_posts.json`.
- **The morning trial run refreshes the index if `state/posted_index.json` "updated" is over 24 h old, BEFORE picking any
  video** (only new posts and new sources get fingerprinted, so it's quick). If the refresh fails, don't label anything
  new that day: use re-edits/approved compilations and tell Mack why.
- **The A/B 3-day same-footage rule is checked against fingerprints too.** Before a reel goes on the review page,
  fingerprint the rendered file (`fp/want_repo.txt` -> `state/fp/repo/`) and check it against (a) `posted_index.json`
  posts on the other account in the last 3 days and (b) everything scheduled or waiting on the review page for the
  other account within 3 days of its slot (`python3 tools/match_fp.py pair a.json b.json`). Any match = pick other footage.
- **Review page card for A's new video** starts its `reuses` line with: "NEW — never posted (fingerprint checked)".
  Anything not in never_posted.json is described as a re-edit with where/when it was posted (from posted_index.json).
- DUP CHECK FIX (Oct 14): a source only counts as ALREADY POSTED if a post contains >= 15 s of it (audio or frames). Short bits (< 15 s) that appear inside compilations or other montages do NOT make the whole video "posted" — the triple-dipper par 4 (Video Oct 12 2026, 12 17 30 AM.mov) was wrongly called posted because of 5 s bits in comp1, then wrongly used as a B "re-edit". Log the short overlaps but keep the source never-posted. Re-run the never_posted.json match with this rule.
- Oct 14: Mack posted the full triple-dipper original on @mackygolfs herself. B's 026 re-edit moved to Sun Oct 18 08:23 MT (review doc 2026-10-18_B_am). Fri Oct 16 B morning slot is open — fill it with a REAL re-edit (long, >60 s, talk-first) for her approval.
- HARD RULE — NEVER MISLABEL "ALREADY POSTED" (Mack, Oct 14: "don't ever make that mistake again"): before ANY video is used as a re-edit (B, A's re-edit slot, @moremackygolfs) you must name the exact post it re-edits — account, date, caption, platformPostUrl — from state/posted_index.json with >= 15 s of that source in ONE post. Our own trial posts don't count as "Mack already posted it" (only her own posts, or a post she approved as the full video). Compilation bits never count. If you can't name that post, the video is NEW: it is not allowed on B, and it is protected for A's new slot. Put the matched post link in the review card's "reuses" line so Mack can check it. No guesses from length, outfit, caption or memory.

## SHORTIES (Mack, Oct 14) — 2 per day, in addition to compilations
Format (her reference: a guy lining up an iron, on-screen text "Me after deciding between 7 or 8 iron", then he shanks it):
- 10–15 s single moment: the setup/address, then the bad (or absurd) result. The joke is the contrast between a confident on-screen line and what happens.
- ON-SCREEN TEXT: one short dumb/funny meme line (style, size and position: see ON-REEL TEXT (Mack, Oct 17) at the end of this file — Inter Bold 46 px, never above y 400). This is the ONLY format where on-screen text is allowed — every other rule against burned-in text still stands.
- Usually no talking — keep her original sound but trim talk unless the talk IS the punchline. Never cut the shot itself or its result; never cut swearing that's in the kept moment.
- Caption (post text): short, dry, lowercase, no hashtags.
- Footage: ONLY footage Mack has already posted (HARD RULE: name the exact >= 15 s post). Never burn never-posted videos on shorties. Don't reuse a moment used in another shorty or compilation within 2 weeks.
- 3+ cover options (the address frame with the on-screen text works well) .
- Review: put each shorty in the review page db collection "compilations" (same doc shape: title starts "Shorty: ", caption, duration, about, video_url, cover_url, cover_options, file, account default "@mackthegolfer", round 1, decision null, notes "", status "ready", posted false, order next, plus "type": "shorty"). Same approve / notes / account toggle / post now-or-next flow as compilations; approved shorties can fill trial slots like compilations.
- Files: shorties/<slug>.mp4 (+ covers, notes) in this repo; single crf-17 export from the TRUE original.
- Ideas for lines (her voice, dry): "me after a 10 minute practice swing routine", "me when the group behind is watching", "me after telling everyone I've been hitting it pure", "me after saying 'easy par from here'", "me after 3 youtube lessons", "me picking the 'safe' line".
- FULL BEFORE CUT (Mack, Oct 14): a cut/re-edit of a NEVER-POSTED video may never post before the full original. If she wants both, the full original goes first, and the cut follows the RE-EDIT SPACING rule. (Lock-it-in par 3: full moved to Thu Oct 15 6:52pm MT, review doc 2026-10-15_A_pm. The A copy of the 31s cut was deleted. The full's Zernio draft 6acfe80cb278a89ea3578c8e is set to Thu 00:52Z — schedule it once she re-approves after her cover note.)
- RE-EDIT SPACING (Mack, Oct 14 — replaces "never the same video twice on one account"): after footage first posts (full or any cut) on an account, a re-edit of it may go on the SAME account only 5+ days later, or on @mackthegolfer 3+ days later (and the other way round: A 3+ days after B). The full original always goes before any cut of a never-posted video. Count days from the first post of that footage, using posted_index.json + scheduled posts. Short bits < 15 s inside compilations/shorties don't count.
- SHORTIES = ONE CLIP, ONE SHOT (Mack, Oct 14 notes: "supposed to be one clip", "I want these to be like one single shot"): one continuous clip of hers (no cuts inside) built around ONE golf shot — setup → that shot → its result. Find a single clip >= 10 s (frame-diff for cuts; the scene detector misses some) and trim at quiet gaps. The meme line must make sense with the clip on its own (she rejected "me picking the safe line"); keep it clear of her head/face (position per ON-REEL TEXT, Oct 17, below).

## SOURCE FOLDERS (Mack, Oct 14 — overrides anything above)
- Source folders for videos = ONLY Dropbox /Golf Captions (incl. any new subfolders Mack adds) and /golfclips. Do NOT use /Golf tracer, /Golf, /batch *, /1st batch of 5, /Final Batch Sept 25th or any other folder, for counting or for picking footage.
- Copies of the same clip in both folders count once (fingerprint). Oct 14 count: 32 unique videos, 29 already posted, 3 never posted (cactus, lock-it-in, six months), all 3 lined up. Totals: `state/video_inventory.md`.
- "SEND ME TO DOWNLOAD" NOTES (Mack, Oct 14): if her note on any reel/compilation/shorty asks to download it (e.g. to add music and post herself), send her the full-quality file (SendUserFile; if over 30 MB, make a high-quality copy under 30 MB), set decision "self_post", status "sent_to_mack", and never schedule or re-edit it. Log it in manual_posts once she posts it.
- TOOLING (Oct 14): Dropbox is blocked from Claude's sandbox; relay any Dropbox file with a temporary `download_link` in `inbox/links.txt` (`name|url`; fetch-inbox now downloads BEFORE a sparse checkout, so 15-min links survive). Fingerprint Dropbox files outside the Golf Captions folder link with `fp/want_links.tsv` (name<TAB>url). Word-timestamped transcripts: push `fp/want_transcribe.txt` (repo paths, .partNN ok) -> `state/transcripts/<name>.json` (faster-whisper on the runner) — use them to cut only in real gaps between words and to keep every line you mean to keep.

## RED HAWAIIAN SHIRT BATCH (Mack, Oct 14)
6 never-posted Sep 21/23 holes. 4 → @mackygolfs as new originals (Sat Oct 17, Mon Oct 19, Wed Oct 21, Fri Oct 23), 2 → @mackthegolfer (Sun Oct 18, Tue Oct 20) as an exception to B's re-edits-only rule (Mack's call). One per account per day max, never on consecutive days on the same account. These are short, so they take that day's SHORT slot. B versions start on her intro line right after the wipe (wipe removed, nothing else cut). Once a video posts on IG it may go to TikTok/Facebook later; never-posted videos stay off Facebook until their IG post.
- COVER PICKER (Oct 15): reel cards on The Reviewer now show `cover_options` (id, label, file, url) and Mack can tap one; it saves `chosen_cover` (opt1/opt2/...) on the reels doc. When scheduling an approved reel, use the chosen option's file as `instagramThumbnail` (pinned raw URL) in the posts_create_post call. No pick = opt1.

## MACK'S COMPILATION IDEA — "asmr but it's golf" (Mack, Oct 15) — add to the compilation idea list (next in line after whatever is being made now)
- Text: "asmr but it's golf" — use as the cover text (3+ cover options) AND as one short on-screen line for the first ~2 s (shorty style). No other text.
- Content: lots of very short clips (≈0.5–1.5 s each) of just the SOUND moments: club hitting ball (drives, irons, chips, putts) and ball dropping in the cup. Cut tight around the contact/drop so the sound is crisp. No talking, no music; keep only the natural impact/cup sound (duck or cut any voices). Mix shots and putts so the rhythm varies; no two bits from the same shirt/day back to back (SPACING rule). Aim ~15–25 s.
- Footage: only /Golf Captions + /golfclips, already-posted footage preferred; bits are < 15 s each so they don't use up never-posted videos. Never cut a shot's contact; don't use anything from other folders.
- Normalize loudness so every hit is about equally loud. Caption: short, dry, lowercase.
- CAPTIONS + FRAMING (Mack, Oct 16) — from her own top golf reels (kids 719K, "please help me out" 272K, "dead to me" par 248K, "tired of triples" 191K, road to breaking 100 170K): every caption either ASKS FOR HELP ("please help, this is getting embarrassing"), PICKS A FIGHT about the score ("if you say this is a bogey we cant be friends"), or names the STAKES (kids, water, marshal, bet, lost ball) — in her dry voice, lowercase. Avoid neutral captions like "par 3 at sunset. rate it". Long videos are fine (kids one was 106 s); lead with the stakes, not the hole. Bring back the running series "road to breaking 100: day N" on suitable rounds. Do NOT shorten videos to get under a minute — TikTok originals over 60 s are wanted (Creator Rewards).

- ON-REEL TEXT (Mack, Oct 17 — replaces the Oct 16 position rule and every earlier size/position spec for shorties, comp13's "asmr" line and any other on-reel meme text). Her notes: "The text is too big" (read-the-putt at 66 px sat up in Instagram's top bar / "Trial reels" label), "text can't sit that high" (Oct 16), and "also should be more legible".
  * Style: Inter **Bold** 46 px (`/usr/share/fonts/opentype/inter/Inter-Bold.otf`; never 66–72 px again, never SemiBold), white, thin dark outline (3 px stroke, black at ~85% opacity) PLUS the soft drop shadow (black ~80%, offset 3/4 px, 6 px blur). Max ~2 lines, horizontally centered, ≥ 90 px side margins. Build it with `tools/ontext.py '["line 1"]' <ink top y> out.png` (1080x1920 RGBA overlay; prints the ink box).
  * Position: the text's top edge (ink incl. stroke) at **y ≥ 400 of 1920** (clear of Instagram's top bar and the trial-reels label). Shorties: upper part (y 400–700) only when it is clear of her head/face for the WHOLE time the text is on screen; if her head is in that band at any point, drop it to the lower band 1150–1300 (above her own captions). Compilations: default lower band 1150–1300. Never over her face.
  * Check every one: contact sheet across the whole time the text is visible (guide line at y 400), full-res crop of the line over the brightest background (sky/clouds, sand, bright grass), and the frame downscaled to phone size (~390 px wide) — it must read easily at that size.
  * Oct 17 re-renders with this spec (all lower band, ink 1180–1231; her head sits in 400–700 at some point in every one): shorties/hero-shot_r2, improve-my-lie_r2, youtube-lessons_r2, group-watching_r2, listening-to-the-comments_r2, compilations/comp13_asmr-golf_r3 (tools/asmr/render_r3.py). Already-posted read-the-putt, comp7 and safe-line were left as they are.

## HARD RULES (Mack, Oct 19 — FINAL version; window changed to 30 DAYS Oct 20) — these WIN over anything above
1. MAIN-ACCOUNT POOL. The pool is Instagram @mackygolfs + @mackthegolfer ONLY. A reel — ANY version of it (Mack's original,
   any re-edit, Mack's own posts, fingerprint-matched) — must not post on either account within 30 DAYS (before or after) of any
   version of it posting on either of them. Same reel = same source video in Dropbox /Golf Captions or /golfclips
   (byte-identical twins and alt takes of a hole count as one; mack-fitz/clips state/sources.json).
2. NOT IN THE PAST 30 DAYS (Mack, Oct 20; was 7). A reel is only eligible for the review page OR the schedule if NO version
   of it posted on @mackygolfs or @mackthegolfer in the 30 calendar days before TODAY (from 00:00 MT 30 days ago) — even
   if its slot would land later. Least-recently-used first, spread across trips/courses (no Texas-heavy rotation).
   check_repeats.py window = 30 days by default (--window-days / REPEAT_WINDOW_DAYS); its look-back is 2x the window and
   includes Mack's own older posts from posted_index.json, so keep that index current.
   CAPACITY: /Golf Captions has 27 unique videos, so at 30 days the two accounts together can sustain about 27 posts per
   30 days = under 1 original/re-edit per day COMBINED (~6 a week). Fill the remaining slots with comps and shorties
   (exempt) or leave them empty; never break the rule to fill a slot.
3. EXEMPT: shorties and compilations (all of their bits). TikTok, @moremackygolfs, X and Facebook do NOT count toward the
   pool and are not restricted by it; they keep their own existing rules (FB 30-day no-repeat on FB, @moremackygolfs
   already-posted proof, TikTok gets every original) plus rule 4.
4. EXACT DUPLICATE, PER ACCOUNT. The same media file (same bytes, any caption/commit) never posts twice on the same account.
5. RUN THE GUARD before scheduling, moving, promoting a draft, or putting ANYTHING on the Trial Reels Review page:
     # both repos side by side: /home/claude/clips and /home/claude/mackygolfs-mackthegolfer
     # Zernio call_tool posts_list_posts {from_date: today-14d, to_date: today+21d, limit 100, sort_by scheduled-asc},
     #   every page -> save each raw answer (p1.txt, p2.txt ...)
     # analytics_get_analytics for @mackygolfs and @mackthegolfer (source all, from_date today-14d) -> an_*.txt
     python3 /home/claude/clips/tools/build_media_map.py           # after adding any new edit/comp/shorty
     python3 tools/check_repeats.py --zernio p1.txt p2.txt --analytics an_*.txt                       # whole schedule
     python3 tools/check_repeats.py --zernio p1.txt p2.txt --analytics an_*.txt --candidates cands.json  # review gate
   cands.json = [{"label", "account": "ig:mackygolfs|ig:mackthegolfer|...", "media": "repo:path", "time": "<ISO>"}].
   Exit 0 = OK; 1 = violation (do NOT schedule or add the card; leave the slot EMPTY rather than repeat); 2 = unknown media
   or Mack's new post not fingerprinted yet (fix first: fp/want_posts.tsv -> fingerprint workflow). Mack's approval does
   not override it. A card that fails later (e.g. after Mack posts something herself) comes off the review page.
6. REVIEW PAGE HYGIENE. Only future-dated cards that pass rule 5. Cards whose slot passed are removed (archived in
   mackygolfs-mackthegolfer state/review_archive_*.json). Pick footage with
   `python3 /home/claude/clips/tools/inventory.py --zernio ... --analytics ... --free <slot times>` (oldest first).
7. DEBUT RULE. A clip never posted anywhere debuts on @mackygolfs or @mackthegolfer, never on @moremackygolfs.
8. COVERS. TikTok: ALWAYS the video's first frame (tiktokSettings.videoCoverTimestampMs = 0, no videoCoverImageUrl;
   already-published TikToks can't be changed). @moremackygolfs: ALWAYS frame one (ffmpeg -ss 0 -frames:v 1 -> instagramThumbnail;
   no custom shirt-wipe/text covers). @mackygolfs / @mackthegolfer covers unchanged (options on the review page, never
   text over her chest).
9. ZERNIO GOTCHA: when moving a post, set BOTH the top-level scheduled_for AND each platform entry's scheduledFor
   (posts_update_post with platforms[]); the top level alone leaves the platform at the old time.
10. FILE SIZE: renders served from raw.githubusercontent must stay < 100 MiB: render with /home/claude/clips/tools/render.sh
   and VMAXRATE=10M VBUFSIZE=20M for long edits. Never `git stash -u` while a render is writing into the repo.
11. DASHBOARDS MATCH ZERNIO (Mack, Oct 20): before ANY dashboard rebuild (clip dashboard Up next, Base Camp schedule,
   trial dashboards), pull the live schedule from Zernio and update state/schedule.json first:
     call posts_list_posts (from_date 2026-10-05, to_date 2026-12-31, limit 100, sort_by scheduled-asc, EVERY page) ->
     cd /home/claude/clips && python3 tools/sync_schedule.py --zernio p1.txt p2.txt
   then rebuild (python3 tools/upnext.py upnext.json refuses to run if the sync is older than 2 h). Base Camp rows come
   from the same Zernio pull: drafts are shown as "DRAFT: awaiting Mack approval", never as scheduled. Never publish
   dashboard rows from memory, from an old schedule.json, or from what you meant to schedule.
   (mackygolfs-mackthegolfer tools/dash_trials.py upnext already reads Zernio directly; give it the same fresh pull.)
12. @mackygolfs/@mackthegolfer use ONLY /Golf Captions. Never /golfclips. (Mack, Oct 20 - exact wording.)
   /GOLFCLIPS = CLIP PAGES ONLY (Mack, Oct 20). Files added to /golfclips on Oct 20 (the 68-reel batch) are clip-pages only,
   never @mackygolfs/@mackthegolfer. Broader rule: NOTHING from Dropbox /golfclips, old or new, is ever used for @mackygolfs or
   @mackthegolfer (no rotation/inventory pool, no debut edits, no re-edits, no compilation/shorty bits, no Trial Reels Review
   cards). /golfclips feeds only @moremackygolfs, @mackygolfs X + TikTok and the macky.golfs Facebook Page. State:
   mack-fitz/clips state/processed.json "clip_pages_only" (every /golfclips file id) and state/sources.json
   "clip_pages_only": true on every source whose only copies are in /golfclips (tools/build_media_map.py sets it).
   tools/inventory.py --free never offers those sources and tools/check_repeats.py --candidates FAILS any @mackygolfs/
   @mackthegolfer candidate that contains one. A reel that also exists as its own file in /Golf Captions may still reach the
   main accounts only from the /Golf Captions file. @moremackygolfs still needs a named proof post (no proof = skip it).

## CLONING (Oct 21)
- The repos hold ~7-9 GB of video at HEAD. A plain or `--depth 1` clone runs a fresh container out of disk/time (every
  scheduled task errored out after ~20 min on Oct 21). ALWAYS clone blobless + sparse:
  `git clone --filter=blob:none --no-checkout https://github.com/mack-fitz/<repo>; cd <repo>; git sparse-checkout init --no-cone;`
  write `.git/info/sparse-checkout` = `/*` `!*.mp4` `!*.mov` `!*.MOV` `!*.MP4` `!*.m4v` `!*.part[0-9][0-9]` (one per line); `git checkout main`.
  (clips: ~70 MB, ~5 s.)
- Fetch an individual video only when you actually need it (`git show HEAD:path > file`, or the Dropbox relay). Never
  check out all videos. Committing a new video still works: `git add --sparse path/to/file.mp4` (plain `git add` refuses
  paths outside the sparse cone); push as usual.
- The tools (check_repeats.py, sync_schedule.py, inventory.py, build_media_map.py, upnext.py) work without video files
  present: they read state/*.json and list dirs via `git ls-files`.

## SHIRT WIPE OPENS EVERYTHING EXCEPT @mackthegolfer (Mack, Oct 21) — newest rule, wins over anything above
Mack, Oct 21 10:01am: "everything on moremackygolfs ig should be starting with the shirt wipe" and "basically everything
always starts with the shirt wipe except for mackthegolfer".
Mack, Oct 21 11:20am: "If it's a shorty or a comp that doesn't have a wipe then yeah you don't need to add one in."
- EVERY regular reel/edit opens on Mack's shirt wipe: @mackygolfs IG (originals, re-edits), @moremackygolfs IG reels +
  stories, macky.golfs Facebook edits, X/TikTok/FB originals.
- @mackthegolfer: NEVER the wipe (reels, compilations, shorties, covers) — unchanged.
- Compilations and shorties are EXEMPT on every account: don't add a wipe. If a comp/shorty already contains a wipe, that's
  fine; leave it as it is. (The shirt-wipe montage comp is its own thing.)
- Edits still follow every other rule (restructure after the wipe, 25-40 % cut on @moremackygolfs, punch-ins, never cut
  shots or swearing, no captions during the wipe). X/TikTok/FB originals stay untouched: just confirm they open on the wipe.
- Source with no wipe: open on the strongest action and list the clip in the run report.

## SCHEDULED TASK ROLES (Oct 21) **[SUPERSEDED Oct 23 — see SCHEDULED TASK ROLES (Mack, Oct 23) at the bottom]**
Several runs errored (RUN_ERRORED) because the review checks, the makers and the morning run all re-edited the same items
at once. Mack agreed this split on Oct 21:
- Review page checks (:17 and :47, 6am-10pm MT): ONLY schedule/post what Mack approved. They never edit or render video.
  They use the repo only for check_repeats.py and pinned media URLs.
- "Reviewer notes (one per run)" (:32, 6am-10pm MT): the ONLY job that applies Mack's notes (decision "changes") on
  reels, compilations and shorties. One item per run, oldest first, under a claim.
- Compilation maker / Shorties maker: make ONE new piece per run under a claim; never apply notes. 6+ waiting with no
  decision = don't make a new one. Shorties split ~60% @mackygolfs / 40% @mackthegolfer (never a wipe on @mackthegolfer).
- Golf trials morning run (4:38am MT): schedules approved reels and stays ahead on new reels; never applies notes.

Claim files: before working on an item, commit + push state/claims/<doc or slug>.md (job name + UTC time). Any job skips
an item whose claim was committed less than 60 minutes ago by another job. Delete the claim in your final commit (or, if
you give up, in a commit of its own so the next run can retry). A claim older than 60 minutes is stale: take it over.

## POSTING RULES v2 (Mack, Oct 23, 4:11pm MT) — NEWEST, WINS OVER EVERYTHING ABOVE
Replaces for @mackygolfs (A) / @mackthegolfer (B): the A = 1 new + 1 re-edit / B = re-edits-only rotation, the old
morning/evening trial times (A ~7:30-8:00 / 6:30-7:30pm, B +45 min; "2 per day morning + evening", short/long test
slots), and the 2.5/day cadence for TikTok + Facebook (they now follow the weekly folders). @moremackygolfs keeps 2.5/day.
Sources for A/B are now the weekly folders below (+ old /Golf Captions reels for afternoon bounces); /golfclips stays
clip-pages only.

**Weekly folders.** Mack makes a new "week N" folder each week in each account's folder, with at least 7 new reels each:
  Dropbox /Golf/for claude/mackygolfs/week N   (ns:3302941984//Golf/for claude/mackygolfs/week N)
  Dropbox /Golf/for claude/mackthegolfer/week N (ns:3302941984//Golf/for claude/mackthegolfer/week N)
  File order/names are just her counting: post in any order. Loose files directly in /Golf/for claude/<account>/
  (outside a week folder, e.g. the 4 copy_….MOV in mackygolfs/) are NOT used — list them for Mack.
  RE-LIST EVERY WEEK FOLDER ON EVERY RUN (Oct 24): Mack adds files AFTER a folder first appears (Oct 23 ~4-5pm MT she
  added 4 PM files to week 1 after the week 1 job had listed it; they were missed until Oct 24 -> 076-079). Every run
  lists every week N folder again and compares Dropbox file ids with the registry; anything new gets registered,
  fingerprinted and put on The Reviewer. Words in a filename ("never post as a bounce", "never post on mackthegolfer")
  are Mack's instructions; any name starting with PM/pm is a PM file.
  Registry: mack-fitz/clips state/weekly_sources.json (source id "<account>/week N/<file>": home account, pm flag,
  dropbox id, duration, wipe end); tools/build_media_map.py + check_repeats.py read it.
  Relay: clips inbox/relay_links.tsv (links mode, scratch/<branch>), never main. Fingerprint: fp/want_links.tsv here.

**Mornings: ONE trial reel per account every morning.** @mackygolfs posts from its own weekly folder, @mackthegolfer
  from its own. Window 7:00-8:30am MT; vary the minute day to day (never the same time every day; A and B at different
  times). Morning = new footage only, own account only.

**Afternoons: window 2:00-3:30pm MT, also varied.** Afternoon slots take: extras beyond 7 in a weekly folder; PM files;
  comps and shorties (she still wants these); back-and-forth reposts (old /Golf Captions reels too).
  AFTERNOON PRIORITY (Mack, Oct 23): PM files > turn dog reels > YouTube promos > bounces > comps/shorties.
  Comps/shorties only fill empty afternoons (turn dog reels and YouTube promos will take these slots soon).

**PM files.** Files named PM ("pm.MOV", "PM.MOV", any case) are ALWAYS afternoon and NEVER bounce to the other account.

**Shirt wipe.** Every upload in the weekly folders includes her shirt wipe.
  - @mackygolfs ALWAYS opens on the wipe: use the upload as-is.
  - @mackthegolfer NEVER has a wipe: cut out ONLY the wipe, change nothing else (cut right after the shirt is down,
    before her first word; check frame by frame at the start, 10 fps).
  - An upload with no wipe: just proceed as is (list it in the report).

**Back and forth (bounces).**
  - A reel posted in an account's morning slot can go to the OTHER account in an afternoon slot 30 days later: WITH the
    wipe if going to @mackygolfs (use the original upload, which has it), WITHOUT it if going to @mackthegolfer.
  - 60 days after its first post it can go back to the original account, again in an afternoon slot.
  - The 30 days always count from the MOST RECENT time it was posted. PM files never bounce.
  - After the first month, afternoons may pull from the other account's folder under this rule.
  - Old /Golf Captions reels continue under the same back-and-forth rule.
  - BOUNCES (Mack, Oct 23): every back-and-forth repost gets a NEW caption and a NEW cover, plus light edits to lower the
    duplicate-flag risk (a different trim/end point, a different opening beat after the wipe, punch-ins). Never cut
    shots or swearing. (@mackygolfs bounces still open on the wipe; @mackthegolfer bounces never show it.)
  - tools/check_repeats.py enforces it (R5/R6: morning = debut from own folder; repost only 2:00-3:30pm; 30 days from the
    most recent pool post; back on an account only 60 days after its first post there; PM never on the other account).

**Review.** EVERYTHING for these two accounts goes through The Reviewer first (caption + cover approval).
  ADVANCE REVIEW (Mack, Oct 23): when a new "week N" folder appears, the morning run puts the WHOLE week on The Reviewer
  that day; it always keeps at least the next 5-7 days of morning slots on The Reviewer.
  NO ZERNIO DRAFTS FOR ITEMS WAITING ON REVIEW (Mack, Oct 23 late — drafts show in her scheduler and confused her): create
  the Zernio post ONLY when the item is approved (posts_create_post, scheduled, trialParams {graduationStrategy:"MANUAL"}).
  Keep the full-quality file ready instead: upload it to Zernio temp storage (presigned + zupload) and store media_url,
  media_expires (7 days) and media_reupload (scratch branch:file) on the review doc; if the temp upload expired by approval
  time, re-upload from the scratch branch first. (Deleting a Zernio post also deletes its /media/ copy.)

**Quality (Mack, Oct 23: "I want everything uploaded at the highest quality") — replaces the <=5 Mbps IG spec.**
  - @mackygolfs and TikTok/Facebook originals: her original file UNTOUCHED whenever the platform accepts it, no re-encode.
  - Only if a file is unsupported (HEVC, wrong container, over a size limit) do ONE high-quality conversion:
    H.264 High, level 4.2, 1080x1920, CRF 17, maxrate ~25 Mbps (bufsize 50M), AAC 256k 48 kHz, +faststart, original
    frame rate. Never downscale, never double-encode.
  - @mackthegolfer wipe cuts: ONE CRF-17 encode from her original with the same settings (lossless stream copy if the
    wipe ends on a keyframe).
  - Covers: full-resolution JPEG, quality 95. Reviewer previews may stay 720 px (only for her to look at).
  - Files over 100 MB never go through raw.githubusercontent: upload to Zernio storage (media_get_media_presigned_url ->
    clips zupload workflow PUTs it from the scratch branch, since the workspace can't reach R2; Zernio keeps temp uploads
    7 days, creating/scheduling a post copies them to permanent storage).
  - If IG rejects a file (the old level-5.0 "XPV publish blocking encoding" error), re-encode once at level 4.2, ~20 Mbps,
    not 5 Mbps. Record source vs export bitrate in each notes file.

**TikTok (@mackygolfs) and the macky.golfs Facebook Page.** Anything in the weekly folders, PM files included, can post
  as-is: wipe kept, cover = first frame. Facebook is on the same schedule as TikTok. At first they may go up the same day
  as the IG post; as the library grows, Mack prefers TikTok/FB AFTER IG, not the same day. Schedule them only after the
  IG version is approved (plan in mack-fitz/clips state/schedule.json "weekly_plan").

**@moremackygolfs.** Subject to the 30-day rule counted from the most recent time that footage posted ANYWHERE on IG
  (@mackygolfs, @mackthegolfer or @moremackygolfs). Every video there is edited (clearly different) and opens on the wipe.
  Cadence stays 2.5/day.

**Sunday note (Mack, Oct 23).** Every Sunday the morning run sends Mack a short note: which trials beat her normal
  numbers and are worth sharing to followers; and morning trials vs afternoon trials vs bounced reposts.

**COVER WORDS vs. HER BURNED-IN CAPTIONS (Mack, Oct 24 9:35am MT) — standing rule.** "If you put cover words don't
  choose a frame that has captions OR cover the captions with the text box." When a cover has words: pick a frame with NONE
  of her burned-in captions (wipe frames on @mackygolfs usually have none; on @mackthegolfer check the exact frame), OR place
  the text box so it fully hides the caption (measure the caption's pixel bounds and size the pill/box past them; check the
  crop at full size). Never let a caption peek out above/below/beside the box. All the other cover rules still apply (never
  over her chest or face, never at the very top, inside the grid crop; @mackygolfs wipe frame, @mackthegolfer never the wipe).

**Unchanged:** never cut shots or swearing; no added text on trial reels; cover text never over her chest or face and
  never high in the frame (mid-frame between face and chest, or below the chest, always inside the grid crop); captions
  short, dry, lowercase; the same file never twice on the same account.

## SCHEDULED TASK ROLES (Mack, Oct 23 — replaces the Oct 21 version above)
Tasks created Oct 13 or later fail to start (platform issue), so ALL work runs in the 4 tasks created Oct 12:
- Golf trials morning run (trig_01P9WD8sS4Du6GLG8xj8z3BM, 4:38am MT): APPROVALS (schedule every approved reel/comp/
  shorty from The Reviewer — the full approval-scheduling step), weekly folders (new week folder -> whole week on The
  Reviewer that day; always 5-7 days of morning slots on it; afternoon fill), applies Reviewer notes only if any are
  older than 12 h, Sunday note.
- Clip page daily run (trig_01LF9nY2ySafUThxsSh2UvQg, 12:24pm MT): APPROVALS (same step), applies ALL pending Reviewer
  notes every day, makes 1 compilation + 1 shorty per run for afternoon slots (6+ waiting with no decision = don't make
  one; claim files; Mack picks the account for shorties AND comps; never add a wipe), TikTok/FB from the weekly folders,
  @moremackygolfs (30 days from the most recent IG post, edited, wipe first, 2.5/day).
- Nightly post check (trig_01WnerdLHmdyaKw1s5FJDLzB, 10:07pm MT): APPROVALS (same step) + checks.
- heyymackyy (trig_0119mkSwEHeV2n5yGaNJgeDt): not part of golf; never touched.
- DISABLED (fail to start): Review check :17 (trig_012oyY6XmBNE1jTZ28haCufw), Reviewer notes (trig_01AWcyfNhcWgnYheJ8fvEr4c),
  Compilation maker (trig_01CXKLDqcJuWgi338oKsYTsr), Shorties maker (trig_015yiarZSeTSG3oQKtPdn1Ek), :47 check
  (trig_012AZU8wjhSmNqzs9LsR3opk).
- Claim files still apply between the 3 runs: commit + push state/claims/<doc or slug>.md before working on an item;
  skip an item claimed < 60 min ago by another job; delete the claim in your final commit.
