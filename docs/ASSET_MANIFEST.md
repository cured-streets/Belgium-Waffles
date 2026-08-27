# Asset Manifest

Approval states: PLANNED, PROMPT READY, GENERATING, CANDIDATE, REVISION NEEDED, APPROVED, IN EDIT, FINAL, REJECTED.

| Asset ID | File Path | Type | Shot ID | Status | Source / Generator | Rights Notes | Notes |
|---|---|---|---|---|---|---|---|
| AUD001 | `assets/audio/belgium-waffles-and-babybatter.mp3` | Audio master | Project-wide | CANDIDATE | Uploaded to GitHub by user | Rights/ownership TODO | MP3, 48 kHz stereo, parsed duration approx. 2:12.38 |
| DOC001 | `docs/LYRICS.md` | Lyrics | Project-wide | CANDIDATE | Uploaded to GitHub by user | Rights/ownership TODO | Raw lyric sheet moved from repository root |
| DOC002 | `docs/LYRICS_AND_TIMECODES.md` | Timing document | Project-wide | CANDIDATE | Arena.ai agent + CapCut auto-lyrics | N/A | CapCut rough sync; useful for scene changes, not final on-screen captions |
| REF001 | `assets/style-references/prehistory-waffle-eatery-reference.jpg` | Style/concept reference | Project-wide | CANDIDATE | Uploaded to GitHub by user | Copyright/trademark clearance TODO; use only as broad inspiration | Retro prehistoric cartoon waffle/eatery composition reference |
| REF002 | `assets/style-references/prehistory-couple-reference.jpg` | Style/concept reference | Project-wide | CANDIDATE | Uploaded to GitHub by user | Copyright/trademark clearance TODO; use only as broad inspiration | Retro prehistoric couple/family-sitcom reference |
| REF003 | `assets/style-references/retro-future-family-reference.jpg` | Style/concept reference | Project-wide | CANDIDATE | Uploaded to GitHub by user | Copyright/trademark clearance TODO; use only as broad inspiration | Retro-futurist cartoon family/home reference |
| CHAR001 | `generations/stills/candidates/CHAR_singer-reference_v001.png` | Character reference candidate | Singer | REJECTED | Arena.ai image generation | Original generated candidate | Good adult country vibe, but rejected due to unwanted readable sign and severe giant boot/leg artifacts |
| CHAR003 | `generations/stills/candidates/CHAR_singer-reference_v002.png` | Character reference candidate | Singer | CANDIDATE | Arena.ai image generation | Original generated candidate | Cleaner adult singer reference, correct legs/boots, good whisk-as-microphone prop; possible lock candidate |
| CHAR002 | `generations/stills/candidates/CHAR_cowboy-reference_v001.png` | Character reference candidate | Cowboy | CANDIDATE | Arena.ai image generation | Original generated candidate | Strong cowboy cook direction; may need more waffle-specific props and fewer breakfast-skillet elements |
| LOC001 | `generations/stills/candidates/LOC_farmhouse-kitchen-wide_v001.png` | Location reference candidate | Kitchen | CANDIDATE | Arena.ai image generation | Original generated candidate | Strong farmhouse kitchen layout; good waffle iron, prep island, red gingham, warm light |
| S030 | `generations/stills/candidates/S030_good-morning-kiss-shirtless-cook_v001.png` | Story still candidate | Verse 1 / morning kitchen | CANDIDATE | Arena.ai image generation | Original generated candidate | Adult good-morning cheek-kiss while cowboy mixes batter shirtless under apron; tasteful but has tattoos and possible pseudo-text on bags |
| CHAR004 | `generations/stills/candidates/CHAR_cowboy-reference_v002.png` | Character reference candidate | Cowboy | CANDIDATE | Arena.ai image generation | Original generated candidate | Same cowboy as v001, now with waffle batter, mixing bowl, whisk, and waffle iron; strong character lock candidate |
| LOC002 | `generations/stills/candidates/LOC_farmhouse-kitchen-stove_v001.png` | Location reference candidate | Kitchen | CANDIDATE | Arena.ai image generation | Original generated candidate | Stove-facing angle; includes readable pseudo-sign that must be covered/blurred or regenerated if used |
| LOC003 | `generations/stills/candidates/LOC_farmhouse-kitchen-reverse_v001.png` | Location reference candidate | Kitchen | CANDIDATE | Arena.ai image generation | Original generated candidate | Reverse angle across prep island toward sink/window; strong continuity candidate |
| S001 | `generations/stills/candidates/S001_farmhouse-exterior-sunrise_v001.png` | Story still candidate | Intro 00:00.00–00:03.00 | CANDIDATE | Arena.ai image generation | Original generated candidate | Farmhouse exterior establishing shot |
| S002 | `generations/stills/candidates/S002_empty-kitchen-intro_v001.png` | Story still candidate | Intro 00:03.00–00:06.10 | CANDIDATE | Arena.ai image generation | Original generated candidate | Empty kitchen intro, no readable text |
| S006 | `generations/stills/candidates/S006_belgian-waffle-hero_v001.png` | Story still candidate | Chorus 1 00:23.13–00:26.26 | CANDIDATE | Arena.ai image generation | Original generated candidate | Belgian waffle hero shot with butter and syrup |

## Uploaded Raw Filename Mapping

Files were uploaded at the repository root under temporary names and then organized into the production structure. The canonical paths above are the source of truth.

| Raw Uploaded Filename | Canonical Path |
|---|---|
| `Belgium Waffles and BabyBatter.mp3` | `assets/audio/belgium-waffles-and-babybatter.mp3` |
| `lyrics` | `docs/LYRICS.md` |
| `fred and betty.jpg` | `assets/style-references/prehistory-waffle-eatery-reference.jpg` |
| `fred and wilma.jfif` | `assets/style-references/prehistory-couple-reference.jpg` |
| `jetsons.jpg` | `assets/style-references/retro-future-family-reference.jpg` |
| `CHAR_singer-reference_v002.png` | `generations/stills/candidates/CHAR_singer-reference_v002.png` |
| `S9j1eL8o1qyVIaontugLTpJ7ZsSQQlxQVxXc7XRolX8.png` | `generations/stills/candidates/S030_good-morning-kiss-shirtless-cook_v001.png` |

## Prompt Records

Individual prompt records live under `prompts/`. Batch 002 files include:

- `prompts/characters/CHAR_cowboy-reference_v002.md`
- `prompts/locations/LOC_farmhouse-kitchen-stove_v001.md`
- `prompts/locations/LOC_farmhouse-kitchen-reverse_v001.md`
- `prompts/stills/S001_farmhouse-exterior-sunrise_v001.md`
- `prompts/stills/S002_empty-kitchen-intro_v001.md`
- `prompts/stills/S006_belgian-waffle-hero_v001.md`
