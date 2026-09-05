# Huxiang Fashion Prompt Style System

## Method In One Sentence

First lock the non-negotiable subject inputs, then randomize only the replaceable scene variables through controlled matrices, then block common model failure modes with anti-collapse rules and a final quality gate.

## What Makes This Style Work

- It treats references as authorities, not inspiration.
- It gives the model specific photographic physics: lens, light, wind, exposure, depth, and motion.
- It creates variation with matrices instead of vague requests for creativity.
- It prevents lazy defaults by naming the most likely bad result.
- It checks coherence before final output: action, space, light, props, outfit readability, body proportion, and mood must agree.

## Authority Locks

Use direct priority language:

```text
OUTFIT_REF is REQUIRED and is the absolute wardrobe authority.
Reproduce garment type, silhouette, color, fabric, texture, pattern, layering, structure, fit, proportions, footwear, and styling elements with 100% fidelity.
No substitutions, no simplification, no redesign, no invented styling.

FACE_REF is OPTIONAL.
If FACE_REF is provided, it becomes the absolute identity authority: match facial structure, proportions, skin texture, hairstyle, and overall identity exactly with zero drift.
If FACE_REF is not provided, use the default identity specified below.

If any written clothing or identity description conflicts with the uploaded reference, the uploaded reference always wins.
```

When the user's request is not clothing-reference based, replace `OUTFIT_REF` with the real authority, such as `PRODUCT_REF`, `LOCATION_REF`, or `MOODBOARD_REF`.

## Default Identity Pattern

Use a default only when the user has not supplied a face reference and still needs a fashion subject. This is the user's verified production wording — use it exactly rather than a paraphrase, since paraphrasing has dropped details (e.g. leg length) that were in the working version:

```text
If FACE_REF is NOT provided, use a beautiful young Korean woman with a tall, slender fashion-model body frame, very long legs, and naturally textured short hair.
Beyond this default identity logic, do not add any additional facial description or beauty styling.
```

Chinese original: `如果未提供 FACE_REF，默认使用一位美丽的年轻韩国女性，具有高挑的时尚模特身材框架、非常长的腿，以及自然纹理的短发。除此默认身份逻辑外，不要添加任何面部描述风格。`

The "do not add anything beyond this" instruction is deliberate, not an omission — over-specifying beauty/facial traits tends to push the model toward generic AI-beautified faces rather than a natural-looking one. Adjust identity respectfully when the user specifies age, gender, ethnicity, body type, or brand model direction. Never over-describe ethnicity or beauty traits when they are not needed.

## Photographic Spine

Choose one concrete camera language:

- `Authentic iPhone native-camera feeling, main wide lens around 24-28mm equivalent, natural exposure, realistic white balance, no Portrait mode blur.`
- `Humanistic 35mm documentary street perspective with Fujifilm film simulation, soft highlight roll-off, gentle contrast, slightly warm tones, fine natural grain.`
- `Premium real-life frame captured in passing by a stylish friend, slight handheld imperfection, candid timing, not a staged campaign.`

Avoid mixing incompatible camera claims. Do not request iPhone native and DSLR compression in the same prompt.

## Context-Dependent Prop Rule

Prop choice should follow the outfit and implied life context, not be a fixed requirement. The original working template's coffee-cup-and-bag combination was verified for one specific context — a tailored, office/commute-style outfit (sweater vest, collared shirt, structured trousers) — and reads as natural there. Applying the same coffee-cup default to every outfit is a mistake: on a homemaker or casual-daily look it reads as staged/campaign-like rather than candid.

Decide props from the outfit's implied context:

```text
Read the outfit's implied context before choosing props: tailored/office-adjacent pieces (blazers, collared shirts, structured trousers, polished sneakers or loafers) suggest a commute or work-break moment; soft/loose loungewear, simple daily basics, or an at-home-adjacent look suggest a domestic errand or casual outing instead. Match the prop choice to that context rather than defaulting to the same prop every time.
```

**PROP MATRIX** (pick one option matching the outfit's context, or none — empty hands are also valid and often more natural):

- Office/commute-coded outfit: paper coffee cup + structured bag; sunglasses optional.
- Casual daily / homemaker-coded outfit: phone in hand, a tote or crossbody bag, an umbrella (if the scene calls for overcast or light rain), a book or magazine, light everyday shopping in a cloth bag, or nothing held at all.
- Errand-coded outfit (simple top, jeans, sneakers): phone + small bag is usually enough; avoid coffee cup and sunglasses unless the outfit itself reads as polished.
- When uncertain, empty hands (just a bag on the shoulder) is a safe, natural default — not every candid photo needs a hand-held prop.

```text
Regardless of which prop is chosen, bag/phone/umbrella/book colors should coordinate naturally with the outfit — prefer restrained neutral tones (black, brown, beige, cream, grey, muted olive).
Do not introduce loud logos, bright colors, or attention-stealing accessories.
```

Sunglasses or a low-pulled cap remain a reasonable default across most contexts as a face-styling choice (not a hand-held prop), but skip them too if the outfit or mood calls for a bare, unguarded look.

Chinese original of the verified office-context version (use only when the outfit reads as office/commute): `无论上传的服装如何，受试者必须始终携带一个纸质咖啡杯。受试者必须始终携带一个包。受试者还必须佩戴太阳镜 或 一顶拉得很低的棒球帽...`

## Verified Matrix Library (User's Production Template)

These are the user's own tested matrix options for the European-old-town coffee-run street style domain. When a request fits this domain, reuse these options directly (still selecting exactly one per matrix, still hidden from the rendered image) instead of inventing new generic options — they are proven to read well, unlike ad-hoc generic phrases like "beautiful cafe" or "nice light."

**SCENE MATRIX** (pick one):
1. Dark grey old-town cobblestone street, continuous dark facades, doorways, black iron railings.
2. Cream stone-pillared entrance, large windows, a parked dark SUV, clean sidewalk.
3. Black cast-iron facade street, long narrow perspective, cobblestone paving.
4. Quiet residential fashion side street, dark walls, white trim, steps, metal railings.
5. Old-town sidewalk with neatly parked cars and repeating townhouse entrances.
6. Tall white stone facade, black doorway, columned entrance.
7. Dark facade mixed with a light stone base, a black luxury car parked nearby.
8. Elegant doorway-front street with steps, wrought-iron railings, tall windows.
9. Cobblestone driveway meeting a light grey sidewalk under a row of dark historic buildings.
10. Boutique-like street front, neutral architecture, glass windows.
11. Clean urban block, black/grey facades, parked vehicles, almost no signage.
12. Old-town corner street, a slightly open driveway and tall buildings creating a light gap.

**SUNLIGHT MATRIX** (pick one):
1. Morning low-angle sunlight cutting across the street.
2. Soft afternoon sunlight lighting only the subject and one stretch of pavement.
3. Warm evening back-side sunlight outlining hair and garment edges.
4. Fragmented sunlight falling between tall buildings, breaking into patches on the road.
5. Cool clear-day sunlight, crisp architectural shadows, clean skin tones.
6. Reflected sunlight bouncing softly onto the subject from a parked car's window or hood.

**PASSING CAR MATRIX** (pick one):
1. A dark sedan passing slowly in the background, slight motion blur.
2. A parked SUV nearby plus a moving car further down the street.
3. The edge of a parked car in the foreground, another car passing in the distance.
4. A city car gliding through the background without becoming the subject.
5. A black or grey premium car parked beside the scene to anchor urban realism.
6. A moving vehicle leaving slight blur at the frame edge.

**FOREGROUND MATRIX** (pick one):
1. A car hood or corner entering the lower frame.
2. A slightly blurred railing or stair edge creating depth.
3. A doorway edge or building column framing one side of the image.
4. A soft, blurred stone base or step edge in the foreground.
5. A passerby partially entering the frame edge without blocking the subject.
6. A side mirror, car window edge, or vehicle reflection adding layered depth.

**ACTION MATRIX** (pick one):
1. Walking naturally left to right, holding coffee cup and bag.
2. Walking while looking down at a phone, coffee and bag integrated naturally.
3. Stepping from a doorway or stair edge into the street's rhythm.
4. Touching sunglasses while walking, coffee in the other hand.
5. Adjusting a low-pulled baseball cap while walking, bag carried naturally.
6. Pausing mid-step and turning slightly, still holding coffee and bag.
7. Passing a parked car, wind moving garment edges.
8. Carrying coffee plus an English newspaper, bag still in frame.

**ACCESSORY MATRIX** (pick one — this list assumes an office/commute-coded outfit; for a casual or homemaker-coded outfit, use the Context-Dependent Prop Rule above instead):
1. Sunglasses + structured leather bag + paper coffee cup.
2. Large dark sunglasses + compact bag + paper coffee cup.
3. Low-pulled baseball cap + leather shoulder bag + paper coffee cup.
4. Neutral-toned low-pulled cap + minimalist bag + paper coffee cup.
5. Sunglasses + bag + English newspaper + paper coffee cup.
6. Low-pulled cap + bag + English newspaper + paper coffee cup.

For other scene domains (a different city, indoor setting, seasonal theme, etc.), build fresh matrices following the same concreteness standard shown here — specific and spatial, never a generic one- or two-word label.

## Extended Matrix Libraries: Japan And Korea Street Style

These follow the same design standard as the Verified Matrix Library above (concrete, spatial, never a generic one-word label), but unlike the European set, they have not yet been confirmed against a user-approved generated result. Treat them as a strong starting library, not yet calibration-verified — update this note once a specific option set is confirmed good or bad, the same way the European library and the frame-share numbers were calibrated.

### Japan Street Style

**SCENE MATRIX** (pick one):
1. Narrow Tokyo backstreet with tangled overhead power lines and a softly glowing vending machine against a shuttered shopfront.
2. Kyoto old-town lane with wooden lattice (machiya) facades, stone paving, paper lanterns.
3. Quiet residential Tokyo street, low concrete walls, potted plants by doorways, a bicycle leaned against a wall.
4. Retro covered shopping arcade (shotengai), hanging shop signs, tiled walkway.
5. Narrow alley beside a train line, a level-crossing barrier visible, a train passing in the distance.
6. Convenience-store (konbini) storefront corner, bright interior glow through glass doors, small curb parking area.
7. Canal-side old-town street, a low stone bridge, willow branches overhanging the water.
8. Modern Tokyo side street with a row of vending machines, narrow sidewalk, low-rise apartment block.
9. Shrine approach street (sando), stone lanterns lining the path, a torii gate glimpsed in the distance.
10. Quiet Kyoto backstreet with bamboo fencing, a moss-lined stone wall, a wooden gate.
11. Izakaya alley at dusk, red paper lanterns, a narrow passage, hanging fabric noren curtains.
12. Suburban train-station-front street, rows of parked bicycles, small shops with fabric awnings.

**SUNLIGHT MATRIX**: reuse the Verified Matrix Library sunlight options above; they are not location-specific.

**PASSING TRAFFIC MATRIX** (pick one) — bicycles and small vehicles read more naturally here than cars:
1. A bicycle passing slowly in the background, slight motion blur.
2. A small kei car parked unobtrusively at the curb.
3. A train glimpsed crossing in the distance through a gap between buildings.
4. A delivery scooter passing at the edge of frame.
5. A row of parked bicycles anchoring the residential feel.
6. A local bus passing in the far background, not the subject.

**FOREGROUND MATRIX** (pick one):
1. The edge of a vending machine entering the lower frame.
2. A utility pole or cluster of overhead power lines framing one side.
3. A hanging shop curtain (noren) edge, softly blurred.
4. A bicycle handlebar or basket edge entering the frame.
5. A stone lantern or low wall edge creating depth.
6. A string of paper lanterns softly blurred in the upper foreground.

**ACTION MATRIX** (pick one):
1. Walking naturally along the alley, holding a canned or bottled drink and a bag.
2. Pausing at a train-crossing barrier as it lifts.
3. Stepping out of a konbini entrance, bag in hand.
4. Walking past a vending machine, glancing at it briefly.
5. Adjusting a scarf or collar while walking through a narrow alley.
6. Crossing a small stone bridge over a canal.

**ACCESSORY MATRIX** (pick one, matched to outfit context) — apply the Context-Dependent Prop Rule above, adapted to local props:
1. Sunglasses + canvas tote bag + paper coffee cup.
2. Low-pulled cap + crossbody bag + a canned or bottled drink in hand.
3. Sunglasses + structured leather bag + a convenience-store coffee cup.

### Korea Street Style

**SCENE MATRIX** (pick one):
1. Seongsu-style brick alley, exposed pipework, cafe signage, industrial-chic facades.
2. Hongdae side street, a colorful mural wall, narrow sidewalk, cafe awnings.
3. Traditional hanok village lane, grey tiled roofs, stone walls, a wooden gate.
4. Modern Seoul cafe street, glass storefronts, minimalist signage, clean pavement.
5. Quiet residential alley of low brick villas, parked scooters along the wall.
6. Convenience-store corner (CU/GS25-style signage), bright storefront, a small outdoor table.
7. Subway station entrance staircase, tiled steps, a railing, a glimpse of the street above.
8. Han River-adjacent promenade street, a low railing, a bridge silhouette in the distance.
9. Insadong-style traditional shopping lane, hanji paper shopfronts, narrow stone paving.
10. Hillside alley with hanging laundry, low walls, a staircase leading further up.
11. Seongsu warehouse-conversion street, exposed brick, large factory windows.
12. Narrow Seoul back alley, a couple of parked delivery scooters, minimal signage clutter.

**SUNLIGHT MATRIX**: reuse the Verified Matrix Library sunlight options above; they are not location-specific.

**PASSING TRAFFIC MATRIX** (pick one):
1. A scooter passing in the background, slight motion blur.
2. A small sedan parked at the curb near a cafe.
3. A city bus passing in the distance, not the subject.
4. A delivery motorcycle parked against a wall.
5. A cyclist passing along the sidewalk edge.
6. A taxi passing slowly in the background.

**FOREGROUND MATRIX** (pick one):
1. The edge of a cafe's outdoor signage board entering the lower frame.
2. A brick wall corner or exposed pipe framing one side of the image.
3. A parked scooter's mirror or handlebar edge in the foreground.
4. A hanging cafe menu board, softly blurred.
5. A stair railing edge creating depth near a subway entrance.
6. A potted plant or small storefront display, softly blurred in the foreground.

**ACTION MATRIX** (pick one):
1. Walking naturally down the alley, holding a takeaway coffee and a bag.
2. Stepping out of a cafe doorway, cup in hand.
3. Pausing to glance at a mural wall while walking.
4. Walking up subway station steps, bag on shoulder.
5. Adjusting sunglasses while walking past a brick facade.
6. Crossing a quiet residential alley past parked scooters.

**ACCESSORY MATRIX** (pick one, matched to outfit context) — apply the Context-Dependent Prop Rule above:
1. Sunglasses + crossbody bag + takeaway coffee cup.
2. Low-pulled cap + canvas tote + takeaway coffee cup.
3. Sunglasses + structured mini bag + takeaway coffee cup.



Build matrices from variables that can change without breaking the user's core idea.

Useful matrix categories:

- Action or pose.
- Scene/world family.
- Scene detail zone.
- Light behavior.
- Wind or motion behavior.
- Foreground or occlusion layer.
- Camera position.
- Prop/accessory interaction.
- Background social layer.
- Material and color atmosphere.

Matrix rules:

```text
The model must internally shuffle and select EXACTLY ONE option from each matrix.
Do not ask the user to choose.
Do not render matrix labels, option numbers, placeholders, brackets, variables, or alternative choices into the final image.
Do not default to the first-listed option, the safest option, or the most generic option by habit.
If two selected items feel repetitive, weak, incompatible, or too generic together, replace only that one item once, then lock the full set again.
```

Long-form prompts may include visible matrix headings such as `ACTION MATRIX` or `SUNLIGHT MATRIX`; this is part of the user's established style. The prohibition is against the generated image containing prompt text, labels, option numbers, or menu artifacts.

For complex systems, use staged selection:

```text
Stage 1: Privately select EXACTLY ONE action family first and lock it.
Stage 2: Privately select EXACTLY ONE scene/world family compatible with the action and lock it.
Stage 3: Privately select EXACTLY ONE option from each remaining matrix.
Run a coherence check before writing the final prompt.
```

## Matrix Option Quality

Good options are concrete and spatial:

- `walking out of the cafe holding takeaway coffee, just past the threshold`
- `fragmented sunlight falling between tall buildings, creating broken patches on the road`
- `glass reflection layer partially crossing the subject`
- `cave-mouth daylight fading from bright exterior to cool interior stone shadow`

Weak options are generic:

- `beautiful cafe`
- `nice light`
- `stylish pose`
- `cinematic background`

When possible, include spatial relationships: through a gap, beyond a railing, at a threshold, reflected in glass, behind a facade, between parked cars, under a colonnade.

## Anti-Collapse Rules

Write anti-collapse rules for the specific prompt domain. Examples:

```text
Do not collapse into the default safe answer of "woman sitting quietly by a wooden cafe window."
If the selected action is standing, ordering, walking, waiting, chatting, or picking up coffee, the image must remain standing, transitional, or active.
Do not turn the partial sea glimpse into a full beach scene or resort postcard.
Do not reduce the cave, waterfall, greenhouse, courtyard, roastery, gallery, terrace, or heritage setting to a generic beige cafe background.
No tourist-landmark framing; the street must feel real, clean, and lived-in.
```

Name the failure directly. The point is to stop the image model from using its most common template.

## Light, Wind, And Motion

Light must be directional and consistent:

- Morning low-angle sunlight.
- Warm late-afternoon back-side sunlight.
- Fragmented light between tall buildings.
- Reflected light from pavement, water, stone, or car windows.
- Cave-mouth or threshold daylight.
- Real lens flare only when requested.

Wind must have one believable source:

```text
Wind dynamics are mandatory.
Short hair must show visible natural movement.
Several strands of hair should drift naturally across the face without hiding identity.
Outfit edges, hems, collars, sleeves, or loose structural areas should respond subtly to the same breeze.
If indoors, airflow should feel believable from an open door, window gap, corridor draft, courtyard opening, cave mouth, skylight shaft, terrace edge, or semi-outdoor threshold.
Motion must feel real, gentle, and unforced.
```

## Composition And Body Read

Use camera and posture to create elegance, not anatomy distortion:

```text
The subject is always the hero.
Outfit readability must remain clear.
Foreground adds depth but must not block the face.
Use a slightly low-angle full-body frame only when it helps create a tall, long-leg impression naturally.
The body should feel elongated because of posture, lens position, silhouette clarity, and line of movement, never because of anatomical stretching.
```

## Video First-Frame Framing

Use this section whenever the image is explicitly a first frame for an AI video model, not a standalone still. A still photo optimizes for a single balanced composition; a first frame optimizes for giving the video model a strong, well-placed subject to animate. Get the target aspect ratio if it is not already stated, since that changes the framing math.

### Why standalone composition rules fail here

A frame that looks perfectly balanced as a still can still fail as a first frame if the subject is framed too tight or too loose. The symptom is usually one of two failure modes:

- Subject fills too much of the frame: any subsequent motion crops into the body or face.
- Subject is too small / environment dominates: the subject becomes a minor background element with no presence.

Note that video models typically extend or regenerate the background beyond frame one rather than only panning across the exact pixels provided, so framing does not need to reserve space for a specific camera move or a specific direction of travel. The goal is simply a well-proportioned, non-cropped subject placement — not pre-planning where the camera will go.

### Frame-share targets

```text
Subject occupies roughly 60-70% of frame height. Never edge-to-edge, never a tight crop at the ankles, wrists, or top of the head.
Leave headroom and a ground buffer below the feet of roughly 15-20% each, kept close to symmetric, so the subject clearly does not touch the frame edges.
```

Calibrated reference point: a confirmed-good 9:16 (0.5625 ratio) full-body street-style frame measured at roughly 66% subject frame-share, ~16% headroom, ~16% footroom, with a soft foreground element in one corner, a midground street/railing layer, and a receding background facade. Treat this as the working target across video first frames rather than a lower, untested guess.

**Do not rely on generic framing language alone.** A prompt that only says something like "slightly low-angle full-body framing" (no explicit share or margin numbers) was tested twice with the same underlying template: once it produced the calibrated-good result above (66% share, ~16%/16% margins), and once it produced a bad result — roughly 84% frame-share with only ~4-5% footroom, feet effectively touching the bottom edge, ~12% headroom. Same style of instruction, meaningfully different outcome. The fix is to always pair the general framing language with an explicit, concrete constraint line rather than trusting the model to infer consistent margins on its own.

Verified working insertion line (drop this directly into the composition/photography section of the prompt, right after any "full-body, slightly low angle" sentence):

- Chinese: `取景为接近全身的中远景，受试者占画面高度约60-70%；头顶留白与脚下地面缓冲区必须清晰可见，脚部不得贴近、接触或超出画面下边缘。`
- English: `Frame as a near-full-body medium-long shot; the subject occupies roughly 60-70% of frame height. Headroom above the head and a ground buffer below the feet must both be clearly visible — the feet must never touch, crop at, or extend past the bottom edge of the frame.`

Pair this with a matching negative-prompt line (see Negative Prompt Pattern below) so the constraint is reinforced from both directions.

### Aspect-ratio notes

- 9:16 (vertical, social feed): the narrow horizontal width means side-to-side environment padding is limited. Build some visual depth (foreground/midground/background) so the frame reads as a real place, not a flat cutout. This is the calibrated reference case above.
- 16:9 (horizontal): more lateral room is available. Not yet calibrated against a confirmed reference — start from the same 60-70% share and adjust based on results.
- 1:1 (square): treat as the tightest case for both dimensions; keep subject share toward the lower end of the 60-70% range.

### Depth cues

```text
Include a foreground element (soft, non-blocking), the subject as midground, and a background with some spatial recession (receding street, layered buildings, depth-of-field falloff).
This makes the still read as a coherent real place, which gives the video model a stronger starting point even though it may extend or regenerate what lies beyond the frame.
```

### Additional negatives for video first frames

```text
No frame-filling close-up that leaves no visible margin around the subject.
No subject cropped at ankles, wrists, or top of head.
No feet touching, cropped at, or extending past the bottom edge of the frame — verified recurring failure mode, not a hypothetical.
No flat, single-layer background with no sense of depth.
No environment so dominant that the subject reads as a minor background element.
```

## Negative Prompt Pattern

Use strict, domain-relevant negatives:

```text
No deviation from OUTFIT_REF.
No face drift if FACE_REF is provided.
No age change, ethnicity change, beautification drift, or identity reinterpretation.
No feet touching, cropped at, or extending past the bottom edge of the frame; no head cropped at the top edge (Chinese: 无脚部贴边或被裁切、无头顶被裁切). Include this in every full-body or near-full-body prompt, not only video-first-frame prompts — it was observed failing in a standalone still as well.
No studio lighting rigs.
No fake cinematic LUT.
No Portrait mode blur unless requested.
No DSLR compression when iPhone native camera is requested.
No heavy beauty filters, plastic skin, or AI-smoothed texture.
No distorted hands, face, limbs, or body proportions.
No cluttered tourist background or cheap visual noise.
No loud logos, brand marks, watermarks, or readable random text.
No foreground, crowd, prop, or reflection blocking the face or outfit.
```

## Final Quality Gate

Before returning the prompt, verify:

- The output asks for one image only.
- Input locks are written before creative scene description.
- References override conflicting text.
- Every matrix has an exact-one selection rule.
- Any matrix labels and option numbers are prompt instructions only and must not appear as image text.
- The scene world has specific spatial identity.
- Light direction, wind, action, props, and environment are physically compatible.
- Outfit and face remain readable.
- The anti-collapse rule names the likely failure mode.
- Negative constraints are specific and not a generic word dump.
- If this is a video first frame: subject frame-share is 60-70% (not edge-to-edge, not a tiny background element), and headroom/footroom of roughly 15-20% each are present.
- Every full-body or near-full-body prompt includes the explicit frame-share/margin line (not just generic "full-body, low angle" language) and the matching feet/head-crop negative — vague framing language alone has produced inconsistent results (verified).
- For the coffee-run / Japan / Korea street style domains: matrices are drawn from the verified or extended library (not ad-hoc invented options), the default identity wording matches the verified text exactly when no FACE_REF is given, and prop choice matches the outfit's implied context (office/commute vs. casual/homemaker/errand) rather than defaulting to the same coffee-cup combo regardless of outfit.
