# Image-to-Video Prompt Pack — Belgium Waffles & Baby Batter

**Vendor:** Seedance (image-to-video), matching the "Take the Streets Back" workflow.
**Method:** feed the listed reference still, paste the prompt + negative, run 3 variants, pick the strongest, then cut into the edit.

## Seedance settings (use for every clip)

- Duration: listed per clip (4–8s each; keep clips short)
- FPS: 16
- Aspect Ratio: 16:9
- Guidance / CFG: 6.5–8.0
- Steps: 30–40
- Image-reference weight: 0.6–0.8
- Motion strength: 0.18–0.30
- Variants: 3

## Global style block (append to every prompt)

> 1970s adult country-variety-show breakfast-commercial parody, warm Kodachrome film grain, soft-focus golden farmhouse light, wholesome on-screen tone, practical food-commercial energy, no readable text, no logos, no watermark, no childlike/cartoon rendering, no celebrity likeness, no explicit imagery, adult cast only, 16:9, photorealistic, cinematic film stock look, tactile surface detail, natural facial detail, natural hands, stable subject, 24fps feel.

## Global negative prompt (use if the tool supports it)

> readable text, misspelled labels, logos, watermark, title cards, childlike/cartoon style, anime, painterly, degraded quality, warped faces, extra limbs, extra fingers, morphing, flicker, changing wardrobe, ceiling lights, explicit imagery, modern LED glow, green screen seams, celebrity likeness, obvious CGI artifacts, warped geometry, glitchy motion, oversaturated modern commercial lighting.

## Global notes

- **Aspect ratio:** 16:9 (1920×1080 or higher).
- **Frame rate:** request 16 fps (Seedance setting); the edit runs at 24 fps but Seedance outputs are fine to conform.
- **Reference strengths:** use the listed still as the image-reference / first frame; keep likeness and room continuity similar.
- **Do not generate on-screen text.** The product label ("BABY'S BRAND WAFFLE BATTER") is added in post.
- **One primary action per clip.** Avoid complex hand choreography; keep motion physically plausible and subtle for food inserts.
- **Motion should be subtle** for food inserts, larger only for the finale. The song is a parody, not an action scene.
- Run **3 variants** per clip and keep only the strongest; cut around any unstable frames in the edit.

---

## V001 — Singer Wakes and Smells Breakfast

- Reference frame: `generations/stills/candidates/S002_empty-kitchen-intro_v001.png`
- Duration: ~3.7 s
- Timecode: 00:06.10–00:09.80
- Pupper: "Well I wake up…"

Prompt:
> Slow camera push from a warm farmhouse kitchen window toward scented steam, morning light pours over the prep island and waffle iron, flour dust and steam drift in the sunbeam, cozy breakfast-commercial mood, 1970s country warmth, no people, no faces, no readable text, 16:9.

---

## V002 — Cowboy Turns From Stove

- Reference frame: `generations/stills/candidates/CHAR_cowboy-reference_v002.png`
- Duration: ~2.1 s
- Timecode: 00:12.50–00:14.60
- Pupper: "boots I love the most"

Prompt:
> Medium shot of an adult cowboy cook in a weathered hat, denim and apron, turning from a golden stream of steam at a cast-iron stove, warm backlight, smiling toward camera as he lifts a cream ceramic mixing bowl and starts mixing, 1970s country breakfast-commercial confidence, adult cast, no readable text, no logos, 16:9.

---

## V003 — Batter Pour / First Chorus

- Reference frame: `generations/stills/candidates/T003_waffle-stack-focus_v001.png`
- Duration: ~3.6 s
- Timecode: 00:19.54–00:23.13
- Pupper: "Baby batter... pour it on my plate"

Prompt:
> Extreme close-up of thick golden waffle batter pouring from a cream ceramic bowl onto a cast-iron waffle iron, creamy ribbon texture, steam and warm backlight, slow-motion pour, no people, no faces, no readable text, food-commercial parody, 16:9.

---

## V003B — Batter Pour Reprise / Second Chorus

- Reference frame: `generations/stills/candidates/T003_waffle-stack-focus_v001.png`
- Duration: ~3.6 s
- Timecode: 00:52.80–00:56.42
- Pupper: "Baby batter... pour it on my plate"

Prompt:
> Slightly faster and more exaggerated repeated pour: thick waffle batter pours from a cream ceramic bowl onto a sizzling waffle iron, syrup and butter are already on the finished stack behind, warm steam billows, playful over-the-top food-commercial timing, no people, no faces, no readable text, 16:9.

---

## V004 — Singer Performs Into Whisk (Whisk-as-Mic)

- Reference frame: `generations/stills/candidates/S012_flour-on-nose-wink_v001.png`
- Duration: ~3.5 s
- Timecode: 00:26.26–00:29.74
- Pupper: "For lunch and supper..."

Prompt:
> Close-up of an adult country singer with voluminous blonde curls, red gingham blouse and denim, performing a whimsical "whisk-as-microphone" pose, flour on her nose, she winks and leans slightly toward the whisk as if singing a commercial jingle, warm farmhouse kitchen, playful campy energy, adult cast, no readable text, no logos, 16:9.

---

## V005 — Syrup and Jam Pushed Aside

- Reference frame: `generations/stills/candidates/T002_syrup-and-jam-pushed-aside_v001.png`
- Duration: ~3.5 s
- Timecode: 00:39.33–00:42.86
- Pupper: "Forget maple syrup, don't need no jam"

Prompt:
> Warm farmhouse counter, adult hands in denim push a maple syrup bottle and jam jar aside with a clear decisive motion, the waffle stack stays in warm focus behind, breakfast-commercial "reject the extras" moment, no faces, no readable text, no readable labels, practical prop motion, 16:9.

---

## V005B — Faster Reprise / Syrup and Jam Rejected Again

- Reference frame: `generations/stills/candidates/T002_syrup-and-jam-pushed-aside_v001.png`
- Duration: ~6.2 s
- Timecode: 01:06.80–01:13.03
- Pupper: Verse 2 reprise

Prompt:
> Faster, more exaggerated repeat: adult hands in denim shove the syrup bottle and jam jar further across the counter with a comedic swish, a tiny wobble on the jar, waffle stack remains the hero, playful over-the-top breakfast-commercial timing, no faces, no readable text, no readable labels, 16:9.

---

## V006 — Couple Stirrs Batter Together

- Reference frame: `generations/stills/candidates/S020_slow-whisk-close_v001.png`
- Duration: ~6.6 s
- Timecode: 01:32.97–01:39.53
- Pupper: "Every day's a feast..."

Prompt:
> Soft-focus romantic close-up of two adult hands stirring thick waffle batter together with a wire whisk in a cream ceramic bowl, warm golden dusk light, lens flare and flour dust, slow gentle stirring rhythm, intimate but wholesome, no faces, no readable text, 16:9.

---

## V007 — Waffle Flip Through Air

- Reference frame: `generations/stills/candidates/S006_belgian-waffle-hero_v001.png`
- Duration: ~3.5 s
- Timecode: 01:47.04–01:50.50
- Pupper: "Every day's a feast..."

Prompt:
> Slow-motion golden Belgian waffle flipping through warm steam-filled air, caught on a cream ceramic plate, butter and syrup gleam, warm farmhouse backlight, satisfying product-shot flip, no people, no faces, no readable text, 16:9.

---

## V008 — Flour-Cloud Dance Finale

- Reference frame: `generations/stills/candidates/S008_sunbeam-flour-transition_v001.png`
- Duration: ~5.7 s
- Timecode: 01:41.37–01:47.04
- Pupper: Final chorus

Prompt:
> Warm farmhouse kitchen with a slow swirl of flour dust and steam in a golden sunbeam, a gentle dance begins around the prep island, soft 1970s commercial charm, dreamy light flares, no readable text, no people or faces, or a dressed adult retro couple cued by your tool's preference, wholesome comedy, 16:9.

---

## V009 — Product Box Placement

- Reference frame: `generations/stills/candidates/S024_final-product-beauty-hold_v001.png`
- Duration: ~5.1 s
- Timecode: 01:53.77–01:58.90
- Pupper: "waffles, biscuits or pie"

Prompt:
> Adult cowboy hands in denim place a blank retro product box onto a warm wooden farmhouse counter beside a waffle stack, soft golden light, the box face stays blank (label is added in post), proud but deadpan, no readable text, no logos, 16:9.

---

## V010 — Final Thumbs-Up

- Reference frame: `generations/stills/candidates/CHAR_cowboy-reference_v002.png`
- Duration: ~3.1 s
- Timecode: 02:03.43–02:06.50
- Pupper: Final hold begins

Prompt:
> Adult cowboy cook gives camera a warm final thumbs-up, singer beams beside a waffle stack, 1970s country-variety-show energy, holding the pose with a tiny slow push, adult cast, no readable text, no logos, 16:9.

---

## SH004 — Transition Wink Into Dream (cold-open optional clip)

- Reference frame: `generations/stills/candidates/SH004_wink-into-dream_v001.png`
- Duration: ~2.0 s
- Timecode: cold open 00:10.00–00:12.00

Prompt:
> Visibly pregnant adult country singer in a red gingham wrap dress seated in a 1970s baby shower, warm golden dream light dissolves around her, she laughs/winks into camera as the balloons and bunting soften, wholesome and storybook, no readable text, no logos, 16:9.

---

## DOG004 — Setter Nuzzles Bassinette (warmth beat)

- Reference frame: `generations/stills/candidates/DOG004_setter-nuzzles-bassinette_v001.png`
- Duration: ~2.5 s
- Timecode: outro, near end

Prompt:
> Adult Irish Setter with glossy red-gold coat and long ears gently rests its chin near a wicker baby bassinette with red gingham blanket, soft golden kitchen light, warm soulful gaze upward, tender and wholesome, no people, no faces, no readable text, no cartoon puppy style, 16:9.

---
