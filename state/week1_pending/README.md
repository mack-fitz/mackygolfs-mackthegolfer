# Week 1 Reviewer writes NOT yet applied (Oct 24 00:45Z)
ArtifactData / asset-upload calls needed approval and nobody answered, so these are queued here.
1. Upload cover_previews/*.jpg (9 files, 294 KB) to The Reviewer in ONE Artifact publish (asset:true) — the asset store is FULL
   (1 GB; ~350 KB free). These are 360-px review previews; the posted cover stays the full q95 file in trials/.
   Freeing space: 18 unreferenced Oct 13 preview videos (~155 MB, e.g. 0ba9bfab…, 0f627a47…, 1e7bd739…) — delete only with Mack's OK.
2. Put each returned id into docs/2026-10-2{8,9}_B_am.json / 2026-10-30_B_am.json cover_options[].asset/url (replace PENDING1-3), cover_asset/cover_url.
3. ArtifactData batch on https://claude.ai/artifact/KFJoqNkDr6kpxYDkpniAZ7 collection "reels":
   - update (if_version 1) the 8 live docs 2026-10-25..27 A/B, 10-28_A, 10-29_A with docs/*.upd.json (drops the deleted "zernio" draft id,
     sets media_url = Zernio temp upload, media_expires, media_reupload);
   - set docs 2026-10-30_A_am, 2026-11-01_A_pm, 2026-10-28_B_am, 2026-10-29_B_am, 2026-10-30_B_am.
4. No Zernio drafts: the post is created only on approval (PLAYBOOK v2).
