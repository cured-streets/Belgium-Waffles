# Decisions

Record significant creative and technical decisions here.

| Date | Decision | Rationale | Owner |
|---|---|---|---|
| 2026-08-26 | Initial repository scaffold created from README plan. | Establish project structure and source-of-truth documents. | Arena.ai agent |
| 2026-08-26 | Uploaded song and lyrics organized into production folders. | Keep root clean and make audio/lyrics discoverable by the production docs. | Arena.ai agent |
| 2026-08-26 | First-pass lyric timing marked provisional. | Exact sync requires listening pass against the final master. | Arena.ai agent |
| 2026-08-26 | CapCut auto-lyrics JSON accepted as rough timing source. | We only need approximate scene-change timing, not on-screen lyrics. | User / Arena.ai agent |
| 2026-08-26 | Created timed shot plan from CapCut lyric cues. | Converts the 2:12.37 song into practical AI video, still, insert, and graphic production beats. | Arena.ai agent |
| 2026-08-26 | Uploaded cartoon references organized as style/concept references. | Keep inspiration images discoverable while avoiding direct reuse of copyrighted characters or trademarks. | Arena.ai agent |
| 2026-08-26 | Visual direction steered away from kid-coded cartoon style. | Adult innuendo should not be paired with imagery strongly associated with children or family cartoons. | User / Arena.ai agent |
| 2026-08-26 | Adult retro country breakfast commercial parody selected as safer core style. | Keeps the joke campy, wholesome-on-screen, and clearly adult-coded. | User / Arena.ai agent |
| 2026-08-28 | Six remaining hero shots (V001, V006, V007, V008, V009, V010) generated as on-model stills and converted to editorial-motion clips via ffmpeg zoompan (push-ins/pan + film grain). | Hybrid workflow: stills + motion where dedicated i2v generation is unavailable; keeps character/kitchen consistency and covers the timed plan. | Arena.ai agent |
| 2026-08-28 | New clips rendered 1920x1080 @ 24 fps with silent stereo track. | Matches project target format and drops cleanly into the 2:12 timeline. | Arena.ai agent |
| 2026-08-28 | V009 product box kept blank; no readable AI text generated. | Reduces risk of AI pseudo-text; label gets added in post per README guardrails. | Arena.ai agent |
| 2026-08-28 | Removed embedded cover art from the song master for social renders (`belgium-waffles-and-babybatter_clean.mp3`). | The embedded cover-art video stream disrupted input labeling and made single-pass renders unreliable; shorts now use the clean audio-only file. | Arena.ai agent |
| 2026-08-28 | Shorts rendered vertical 1080x1920 with blur-padded 16:9 source and a Pillow-built CTA end card (@plaguedr.online). | FB/IG-friendly format; all lettering drawn in post per no-AI-text guardrails. | Arena.ai agent |
| 2026-08-28 | Social render pipeline split into two ffmpeg passes (encode video+overlay, then copy-mux audio). | One-pass encode+mux with `-ss/-t` audio input produced a corrupt H.264 stream in the bundled build; two-pass files decode cleanly. | Arena.ai agent |
| 2026-08-28 | Full-length rough cut assembled from the complete timed shot plan; all segments rendered to 1920x1080 and muxed with the clean audio master. | Gives a reviewable 2:12 cut; stills get editorial motion, video slots use the clips. | Arena.ai agent |
| 2026-08-28 | Product label composited in post with Pillow (perspective warp onto the blank box panel). | No AI text on the box; label matches README copy BABY'S BRAND WAFFLE BATTER. | Arena.ai agent |
| 2026-08-28 | Remaining dedicated stills (S013-S024) not yet generated; placeholder reuse of approved frames (reuse tags in SHOTS list) until next batch. | Keeps rough cut reviewable; dedicated keyframes land in the next generation pass. | Arena.ai agent |
