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
- **B (@mackthegolfer):** its own clean edit. NEVER the shirt wipe. Open either on the first spoken
  line right after the wipe, or on a 1-2 s teaser of a later payoff moment then cut back to Mack
  talking. Alternate the two and track which holds better. Fully clean: no innuendo in captions,
  nothing suggestive in covers, no OF tie-in, no story shares or links to A or the other accounts.
- **Every IG account gets its own version.** If a reel has also gone out on @moremackygolfs (or
  the other trial account), make sure cuts and cover differ from those versions. Never skip a reel
  for being a duplicate: re-edit it.
- **Assignment is random, never by length or anything else.** When picking today's reels, shuffle
  and assign by coin flip.
- **Order: each account pulls randomly on its own.** B is NOT staggered behind A. Each day pick
  B's reels at random from everything in /Golf Captions not yet used on B (same for A). The only
  rule: never post the same reel on both accounts on the same day.
- **Pace:** start at 3 trial reels a day per account (A ~9:30-10:30am, 1-2pm, 6:30-7:30pm MT;
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
3. Make the versions: A = original (scale 1080x1920, ~4.5 Mbps, shirt wipe first) or, if already
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
- Export H.264 1080x1920, keep files small (~4–5 Mbps) so publishing is fast.

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

