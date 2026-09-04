---
name: huxiang-fashion-prompt
description: Build production-ready photorealistic candid fashion image prompts in the user's matrix-driven style. Use when the user asks Codex to write, improve, or systematize image-generation prompts for fashion, AMASS outfits, street style, cafe scenes, iPhone/Fujifilm documentary looks, OUTFIT_REF/FACE_REF identity locks, random prompt matrices, anti-collapse rules, photorealistic lifestyle fashion images, European/Japan/Korea street style scenes, or a first-frame image meant to be animated by an AI video model (subject frame-share, aspect ratio, avoiding too-tight or too-loose framing).
---

# Huxiang Fashion Prompt

## Overview

Use this skill to turn the user's rough fashion-image idea into a complete image prompt that follows their established style: lock the non-negotiable identity/outfit inputs first, matrix the variable scene choices, then add anti-collapse rules and a quality gate so the model cannot drift into generic fashion imagery.

Default to producing one copy-pasteable final prompt. Ask a question only when the missing detail changes the whole prompt direction; otherwise make a conservative choice and include replaceable reference names such as `OUTFIT_REF` and `FACE_REF`.

## Core Workflow

1. Extract the user's intent:
   - Subject, outfit/reference requirements, face/reference requirements.
   - Setting world, mood, season, location, brand context, camera language.
   - Must-have objects, action, light, wind, props, body read, and forbidden outcomes.
2. Establish authority locks before any scene writing:
   - `OUTFIT_REF` is the wardrobe authority when clothing fidelity matters.
   - `FACE_REF` is optional by default, but becomes the identity authority when provided.
   - If no `FACE_REF` is provided, use the verified default identity wording in `references/style-system.md` (Default Identity Pattern) exactly rather than paraphrasing it — do not add facial or beauty descriptors beyond it.
   - For the coffee-run street style domain, apply the verified Mandatory Props Rule (coffee cup, bag, sunglasses or low-pulled cap) from `references/style-system.md` unless the user's request is a different domain.
   - State that reference images override conflicting text.
3. Define the photographic spine:
   - One image only.
   - Photorealistic candid fashion image, not a studio campaign.
   - Use a concrete camera surface such as iPhone native camera, Fujifilm film simulation, 24-28mm main lens, 35mm documentary feel, natural exposure, mild highlight roll-off, realistic white balance, fine grain.
4. Add physical realism:
   - Natural sunlight or a specific light source must be present.
   - Wind and motion should share one believable cause.
   - Hair, garment edges, light props, and body movement should respond consistently.
5. Build randomization matrices only for replaceable variables:
   - Typical matrices: action, scene/world, light, foreground, camera position, prop/accessory, background social layer, material/color atmosphere.
   - For the European-old-town / coffee-run street style domain, reuse the user's verified matrix library in `references/style-system.md` (Scene, Sunlight, Passing Car, Foreground, Action, Accessory) instead of inventing new generic options — it is proven to read well, unlike ad-hoc generic phrases.
   - For Japan or Korea street style requests, use the Extended Matrix Libraries in `references/style-system.md` (Japan Street Style / Korea Street Style) — these follow the same concreteness standard but are not yet confirmed against a user-approved result, so flag results back to the user if something looks off so the library can be calibrated the same way the European one was.
   - For other domains, build fresh matrices following the same concreteness standard: specific and spatial, never a generic one- or two-word label.
   - Each matrix should offer specific, visually different options.
   - Require exactly one option per matrix, internal shuffle, no first-option bias, no exposed labels in the final image.
6. Add anti-collapse rules:
   - Name the default failure mode directly, for example generic cafe window seating, tourist landmark street, beach postcard, beige interior, fake luxury set, overposed fashion campaign.
   - Preserve the chosen action and scene world; do not let the final prompt rewrite an active scene into a seated pose.
7. Add composition rules and a quality gate:
   - Subject remains the hero.
   - Outfit is readable.
   - Foreground adds depth but never covers face or outfit.
   - Space is specific, not generic.
   - Camera and body proportions create elegance without anatomical distortion.
   - A vague instruction like "full-body framing, slightly low angle" is not enough on its own — it produces inconsistent results (verified: the same style of prompt produced a well-proportioned 66% frame-share image once, and an 84% frame-share, feet-touching-the-edge image another time). Always pair the general framing language with an explicit, concrete line pinning down subject share and ground/head buffers, so the model has a hard target instead of an open-ended one.
   - Verified working line (Chinese, insert after the full-body/low-angle framing sentence): `取景为接近全身的中远景，受试者占画面高度约60-70%；头顶留白与脚下地面缓冲区必须清晰可见，脚部不得贴近、接触或超出画面下边缘。`
   - English equivalent when writing the prompt in English: `Frame as a near-full-body medium-long shot; the subject occupies roughly 60-70% of frame height. Headroom above the head and a ground buffer below the feet must both be clearly visible — the feet must never touch, crop at, or extend past the bottom edge of the frame.`
7a. If the image is a first frame for AI video generation, apply video-first-frame framing rules:
   - Ask (once) for target aspect ratio if not stated, since it changes the framing math.
   - Use the same explicit frame-share line from step 7 (roughly 60-70%, calibrated from a confirmed reference) — do not rely on generic "full-body" language alone.
   - Include foreground, midground, and background depth cues so the frame reads as a coherent real place.
   - Do not plan the framing around a specific camera move or direction of travel — video models typically extend or regenerate the background beyond frame one rather than only panning across the provided pixels.
   - See `references/style-system.md` Video First-Frame Framing section for concrete values.
8. Finish with strict negative constraints:
   - Use specific high-risk negatives, not a generic low-quality word dump.
   - Always include no identity drift, no outfit drift, no plastic skin, no unreadable anatomy, no random logos/watermarks, no readable accidental text unless requested.
   - Always include a framing negative: no feet touching, cropped at, or extending past the bottom edge; no head cropped at the top edge (Chinese: `无脚部贴边或被裁切、无头顶被裁切`).

## Output Shape

For most user requests, output:

1. A concise Chinese note explaining the chosen direction if useful.
2. The final prompt, in whichever language the user's own verified template uses — if the user has shared a working production prompt (see Reference below), match its language and section-header style exactly rather than defaulting to English. The user's confirmed-good production template is written entirely in Chinese with bracket-style section headers such as `【核心输入规则｜最高优先级】`, `【服装规则｜绝对锁定】`, `【强制道具与配饰规则】`, `【风与动态｜必须保留】`, `【随机矩阵引擎｜由模型自行随机选择】`, `【画面与摄影要求】`, `【环境真实感要求】`, `【最终生成指令】`, `【负面约束】`. Default to this Chinese template style unless the user asks for English or has no established template.
3. Optional short variants only if the user asks for alternatives.

The final prompt should be a complete prompt, not a plan. It may include matrix section names when writing a prompt in the user's long-form style. The important constraint is that the image model must not render labels, option numbers, placeholders, brackets, variables, or menu text into the image. Do not ask the user to choose from matrices unless the user explicitly asks to co-design the system.

## Prompt Sections

Use this section order for full prompts (English generic names on the left; the user's verified Chinese production headers on the right where they exist):

1. Role or generation target.
2. Required inputs — `【核心输入规则｜最高优先级】`
3. Identity and outfit lock — `【服装规则｜绝对锁定】`
4. Mandatory props/accessories, if the user's style uses them — `【强制道具与配饰规则】`
5. Core mood and photographic look.
6. Light, wind, and motion — `【风与动态｜必须保留】`
7. Environment or world definition — `【环境真实感要求】`
8. Hidden selection protocol + Matrices — `【随机矩阵引擎｜由模型自行随机选择】`
9. Composition rules (including the explicit frame-share line from Core Workflow step 7) — `【画面与摄影要求】`
10. Final render directive — `【最终生成指令】`
11. Negative prompt — `【负面约束】`

For shorter prompts, keep the same priority order even if sections are compressed.

## Reference

Read `references/style-system.md` when constructing a longer prompt, when the user asks to preserve their exact method, or when you need matrix examples, anti-collapse patterns, and quality checks.
