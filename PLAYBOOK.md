# Trial reels playbook — @mackygolfs (A) + @mackthegolfer (B), Instagram only

Operating rules for the trial-reel accounts. The daily task reads this file first.
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
- **Pace:** start at 3 trial reels a day per account (A ~7:30-8:00am, 1-2pm, 6:30-7:30pm MT; mornings early to catch the East Coast;
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
4. Schedule: keep 3 days of slots filled on each account, each picking its own random reels
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
- Open on the attention moment if there is one (e.g. the shirt wipe) and keep it,
  then the first full sentence. Otherwise open on the strongest action.
- Never start or end a cut mid-word or mid-sentence. Cut only on measured audio
  pauses (no transcription available — snap cuts to the quietest point nearby).
- Tighten: remove filler talk, dead air, waiting between shots. Keep every shot
  with its tracer fully visible (strike to landing), and every payoff line.
- Punch in ~15% on reaction moments.
- NO hook text, NO subtitles, nothing burned in (Mack's rule for these accounts).
- Keep Mack's captions untouched (they sit mid-frame).
- Target length: tight, usually 30–70s depending on the story.
- Cover: strongest frame (action or reaction, never suggestive out of context), no text.
- Export once, high quality: `tools/render.sh` (libx264 -crf 17 -preset slow, source resolution/fps, AAC 192k 48 kHz). No bitrate caps, no double encodes.

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
   golf accounts (@moremackygolfs, the other trial account) for the last 7 days.
2. A reel is a LIKELY DUPLICATE if its length is within 3 s of a post on that account AND the
   content matches (same course/outfit/story/line: read your contact sheet and Mack's caption
   on that post), or the caption plainly describes the same moment.
3. Likely duplicate on the SAME account: never post it as-is, and don't post a light re-edit
   either. Use it only inside a genuinely new edit (see compilations below), or skip it.
4. Same footage on any other account in the last 7 days: skip it for now.
5. Log every check in state/trials.json (`dup_check`: matched post date + caption, or "clear").

## What to post (Mack's rules, Oct 12)
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

## Length test (Mack, Oct 13)
Each day, of each account's 2 trial reels, one must be SHORTER and one LONGER, so Mack can compare.
- Shorter = under ~35 s; longer = over ~60 s (A: pick never-posted originals that naturally fall in each range; B: pick source videos and edits that land in each range — still 25–40% cut from the original).
- Alternate which slot (morning/evening) gets the short one day to day. Log `length_test: "short"|"long"` and the final duration on each entry in state/trials.json, and report short-vs-long views/skip rate in the daily message.
- This is a deliberate test; it does not change the rule that videos are otherwise picked at random within each length range.

## Cover text style (Mack, Oct 13)
Cover words copy Mack's own @mackygolfs grid (screenshot: covers/grid-reference.png — Read it before making covers). Three styles she uses, all placed mid-frame (roughly 45–70% down, over the middle of the shirt-wipe frame, inside the center square so the grid crop keeps it):
1. **"Macky vs. ___" pill** (her main series): "Macky vs. a Par 4", "Macky vs. a 7 iron", "Macky vs. the LPGA", "macky vs. a chili cheese dawg", "Macky vs. Something that Should Have Stayed a Draft". Bold rounded sans (Poppins Bold/SemiBold is close), white text on a solid rounded-corner color box (orange #F7931E, red #E8101A, yellow #F5C518 with white text, purple #A21CAF, blue #1E90FF). Rotate colors; 1–2 lines.
2. **Typewriter note**: lowercase monospace black text on a plain white rectangle, deadpan quote/thought, e.g. "i'm so wet :/", "does anyone on instagram know what lag means", "i was served dry burger". Use a monospace font (DejaVu Sans Mono or similar).
3. **Big question**: heavy italic red text with white outline, right-aligned, stacked one word or two per line, e.g. "Is Macky about to be soaking wet?" Use sparingly.
Mostly use style 1, some style 2, rarely 3. Words fit the specific video (the hole, club, food or situation). @mackthegolfer covers: same styles but brand-safe (no "wet"/innuendo; never a shirt-wipe frame). "No words" covers stay as the on/off test for A.

## CURRENT RULES (Mack, Oct 13, 12am) — override anything above that conflicts
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
- ONE NEW VIDEO A DAY ON A (Mack, Oct 13 11am, "just do one new video a day on mackygolfs for now"): @mackygolfs (A) gets exactly ONE never-posted video per day. A's other daily slot is a RE-EDIT of already-posted footage (Mack's own posts on any account, or @moremackygolfs/X/TikTok; never footage A itself already posted; never the same footage as B within 3 days), still opening on the shirt wipe, A cover style, clearly different cut. Short/long rule still applies across the two. B = re-edits of already-posted footage only (the two-intro B version above is the one exception).
- APPROVAL (Mack, Oct 13 11am, "I want to see and approve everything you are posting on mackygolfs/mackthegolfer"): NOTHING posts on A or B unless Mack approved that exact reel (video, cover, caption) on the **Trial Reels Review** page (https://claude.ai/artifact/KFJoqNkDr6kpxYDkpniAZ7).
  - Every evening the prep run ("Trial reels nightly prep for review", 6:47pm MT) makes the NEXT day's 4 reels (2 A + 2 B: per account one short + one long, morning + evening) and has them on the review page by **9:00pm Mountain (10pm Central)**, then messages Mack the link.
  - Unapproved reels are Zernio DRAFTS (posts_update_post `is_draft: true`, or posts_create_post `is_draft: true` with `scheduled_for` + `timezone: "America/Denver"` + trialParams MANUAL + pinned media/cover URLs). Never `scheduled` until approved. If drafts ever stop working, delete the Zernio post and keep file + planned time in state/trials.json.
  - Review page data: ArtifactData on the review page, collection `reels`, one doc per reel, id `YYYY-MM-DD_{A|B}_{am|pm}`. Claude writes: date, account, handle, slot, time_mt, time_ct (MT+1h), length (short/long), duration, kind (new/re-edit), reuses (one plain line: what footage, where/when it was posted, what's different), caption, cover_note, video_url/cover_url (`/_blob/<id>` from an Artifact asset upload; videos as 540-wide preview copies under ~14 MB, covers 720 wide), video_asset, cover_asset, file, cover_file, media_url (pinned raw URL), zernio, status (ready|scheduled|posted|dropped), round (1, +1 each fix), history []. Mack writes: decision (approved|changes|null), notes, decided_at, decided_round.
  - Approved (decision "approved" AND decided_round == round): schedule it in Zernio at its planned time (posts_update_post `is_draft: false` + `scheduled_for`), set the doc's status "scheduled", record in state/trials.json.
  - Needs changes: apply the notes (re-edit / new cover / new caption, re-upload preview assets, update the Zernio draft), push `history` {round, decision, notes, fix}, round+1, decision null, status "ready" — it shows again on the page. Message Mack that it's fixed and ready for another look. Never schedule a fixed version she hasn't approved.
  - No decision: stays a draft and never posts. If the slot passes, drop it (status "dropped"; footage goes back to the pool).
  - The 5:38am daily run ONLY schedules approved reels (and applies notes); it never creates scheduled posts on its own. Approvals that came in late still get scheduled that morning; if the planned morning time is under ~10 minutes away, shift it up to 30 min later. Tonight's evening posts already scheduled before Oct 13 11am are grandfathered.

- NEVER CUT OUT SHOTS (Mack, Oct 13): every golf shot/stroke in the source must stay in the edit (tee shots, approaches, chips, every putt, penalty drops). Her comments refer to them, so cutting a shot makes the talking make no sense. Only cut dead air, walking, waiting, ball-searching and pauses between sentences. This applies to every account and every edit, including re-edits and compilations.
- REVIEW FLOW (Mack, Oct 13 noon — standing rule):
  * Every trial reel (A and B) goes on the Trial Reels Review page (https://claude.ai/artifact/KFJoqNkDr6kpxYDkpniAZ7, hole 6 in Macky HQ) for Mack to Approve or leave notes. Nothing posts on A or B without her approval.
  * Stay AHEAD: the next day must ALWAYS be fully prepared and on the review page (at minimum by 9pm Mountain the night before). Work ahead as far as possible — up to 7 days out — whenever footage allows. The day before posting is for working through her notes.
  * When Mack leaves notes: apply them, put the new version back on the review page (round +1, decision reset), and then SendUserMessage her: "Your notes are done — [which reels] are ready to re-review" so she knows to look again. Always notify after notes are applied.
  * Approved reels get scheduled in Zernio at their planned time (trialParams MANUAL). Unapproved reels never post; if a reel isn't approved by its slot, skip that slot and tell her.
