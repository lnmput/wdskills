---
name: korean-fashion-translator
description: >-
  Translate fashion product titles to Korean for e-commerce.
  Use when: translating Chinese, English, or Japanese fashion titles to Korean,
  batch-localizing multilingual product titles to Korean,
  or optimizing existing Korean product titles for shopping mall readability.
---

# Korean Fashion Product Title Translator

Translate fashion e-commerce titles from Chinese, English, or Japanese into natural, concise Korean product names. The output should read like titles written by a native Korean fashion shopping mall curator — not like machine-translated product listings.

**Supported source languages:** Chinese (中文), English, Japanese (日本語)

## Translation Workflow

For each product title, follow this four-step process:

### Step 1: Optimize the Source Title

Before translating, identify the source language and strip the input down to its essence. The target structure is always the same regardless of source language:

**Target format:** `[style tag] + [key feature] + [category]`. Move secondary details (fabric, specific trim, length) into parentheses. Aim for 3-5 core words, but retain additional words when they carry real distinguishing meaning (e.g., a size-specific category term like "petite" or "plus-size" should survive optimization).

Apply the language-specific optimization rules below:

#### Chinese Sources

| Original (verbose) | Optimized (trimmed) |
|---|---|
| 精致通勤垂直条纹衬衫撞色荷叶边饰自系腰带连衣裙 | 通勤风条纹连衣裙（撞色荷叶边） |
| 优雅通勤翻领 A 字短袖连衣裙 | 通勤风 A 字连衣裙 |
| 复古水洗薄款短袖牛仔连衣裙 | 水洗牛仔连衣裙（短袖） |

- Drop generic adjectives: "精致", "优雅", "时尚", "气质" unless they carry real distinguishing meaning
- Remove "女士", "女装", "女性" — implied by store context
- "韩版" → only keep when it's a genuine style differentiator

#### English Sources

| Original (verbose) | Optimized (trimmed) |
|---|---|
| Women's Stunning Elegant Floral Print Chiffon Midi Wrap Dress | Floral chiffon wrap dress (midi) |
| NEW! Must-Have Vintage Washed Denim Button-Front Shirt Jacket | Vintage washed denim shacket |
| Ladies Casual Summer Loose Fit Linen Blend Wide Leg Pants | Casual linen wide-leg pants |

- Drop marketing fluff: "stunning", "gorgeous", "beautiful", "must-have", "trendy", "NEW!", "SALE"
- Remove "women's", "ladies'", "for women" — implied by store context
- Remove SKU numbers, brand prefixes, ALL CAPS marketing words
- Collapse redundant descriptors: "elegant stylish sophisticated" → keep the most specific one

#### Japanese Sources

| Original (verbose) | Optimized (trimmed) |
|---|---|
| 大人可愛い通勤オフィスカジュアルAラインフレアスカート | 通勤風Aラインスカート |
| 【新作】おしゃれで上品な花柄シフォンロングワンピース | 花柄シフォンワンピース（ロング） |
| レディース韓国ファッション ゆったりオーバーサイズデニムジャケット | オーバーサイズデニムジャケット |

- Drop generic fillers: "大人可愛い", "おしゃれ", "素敵な", "上品な" unless they are real differentiators
- Remove "レディース", "婦人" — implied by store context
- Remove brackets with marketing tags: "【新作】", "【送料無料】", "【人気】"
- "韓国ファッション" → only keep when it's a genuine style differentiator

*Completion Criterion*: The optimized title follows `[style tag] + [key feature] + [category]`, secondary details are in parentheses, and all language-specific filler words are removed. Every remaining word serves a distinguishing purpose — if removing it would make the product confusable with a different product, keep it.

### Step 2: Translate to Korean

Translate the optimized title to Korean following these constraints:

1. Output ONLY the Korean title, no explanation
2. **Length guideline** (soft, not hard limit):
   - **Ideal**: 8-15 characters — covers most single items, aim here first
   - **Acceptable**: 16-25 characters — use when dropping words would lose key product identity (e.g., compound items like "셔츠 자켓", size-specific terms like "빅사이즈")
   - **Too long**: 26+ characters — always shorten; at this length the title is not scannable
3. Format: `[스타일 키워드] [주요 특징] [품목명]` — this is a guideline, not a rigid template. If the product has no meaningful style keyword, skip it rather than inventing one.
4. Use natural Konglish only where Korean shoppers expect it (e.g., "데님", "셔츠", "스트라이프")
5. Do NOT directly transliterate source language adjectives — find the natural Korean equivalent
6. If the source has parentheses with extra info, keep them if they add value, drop them otherwise
7. **Ambiguity rule**: When a source term maps to multiple possible Korean terms and the correct one cannot be determined from context alone (see Ambiguous Term Handling in Reference section), output the most likely translation followed by `[⚠️ 확인필요: A or B]`. Example: `캐미솔 탑 [⚠️ 확인필요: 캐미솔/탱크탑]`

Cross-reference [glossary.md](references/glossary.md) during this step to ensure term-level consistency across products. The glossary has columns for all three source languages — look up using the source language column, output using the 한국어 column.

*Completion Criterion*: The Korean output is within the acceptable length range (≤25 chars, ideally ≤15), follows the format guideline, all terms with glossary entries use the glossary-specified translation, and any ambiguous terms are flagged with `[⚠️ 확인필요]`.

### Step 3: Quality Check the Output

After translation, run these checks **in order** and fix any issues:

1. **Length check**: If output > 25 characters → shorten by dropping the least important modifier. If 16-25 characters, verify every word is essential for product identity.
2. **Consecutive loanword check**: If 3+ *consecutive* non-Korean words appear → replace at least one with native Korean equivalent (e.g., "버티컬 스트라이프 셔츠" → "세로 줄무늬 셔츠"). Exception: consecutive loanwords are acceptable if each is the standard Korean shopping term with no better native equivalent.
3. **Glossary consistency**: Cross-reference against [glossary.md](references/glossary.md) — if a term exists, use the glossary version
4. **Adjective stacking**: If the title still has 2+ consecutive adjectives → keep only the most distinctive one
5. **Back-translation verification**: Translate the Korean output back to the **original source language**. Compare it with the Step 1 optimized title:
   - If the core item type changed (e.g., 원피스 back-translates to "shirt" instead of "dress") → fix the item type
   - If a key attribute was lost (e.g., "striped" was in the source but doesn't appear in the back-translation) → add it back
   - If the back-translation contains meaning that wasn't in the source → the Korean likely has unintended connotations, revise
   - Minor stylistic differences are acceptable — focus on factual accuracy of item type + key features
6. **Machine translation red flag scan**: Check the output against the red flag list for the source language in the Reference section below. If any red flag is detected → revise the title.

*Completion Criterion*: All six checks pass or have been fixed. The back-translation preserves the same item type and key features as the optimized source title. Any ambiguous terms remain flagged with `[⚠️ 확인필요]` for human review.

### Step 4: Propose Glossary Updates

After translation, **propose** changes to [glossary.md](references/glossary.md) — do NOT edit the glossary directly. Instead, append proposed changes to the end of your output in a clearly marked section:

```
## 📋 Glossary Change Proposals

| Action | Source Term | Proposed 한국어 | Reason | Confidence |
|--------|-----------|-----------------|--------|------------|
| ADD    | chiffon   | 쉬폰            | appeared 3x in this batch, not yet in glossary | high |
| UPDATE | 条纹 → 줄무늬 | 스트라이프 (primary) | 스트라이프 is more common on Korean malls | medium |
```

**Proposal rules:**
- **ADD**: Only propose terms that appeared 2+ times in the current session or are clearly standard fashion vocabulary
- **UPDATE**: Must include a concrete reason (not just "I think this is better")
- **Confidence**: `high` = standard industry term, `medium` = common but alternatives exist, `low` = uncertain, needs native speaker input
- After the user approves (or modifies) the proposals, then apply them to the glossary file

*Completion Criterion*: All glossary change proposals are listed with Action, Source Term, Proposed Korean, Reason, and Confidence. No direct edits have been made to the glossary without user approval.

---

## Batch Processing

When translating multiple titles at once:
1. Group by source language if mixed, then process each title through all four steps
2. Output as a table: `| Source Language | Original | Optimized | Korean | Flags |`
   - The **Flags** column captures any `[⚠️ 확인필요]` markers from ambiguous terms
3. After the batch, review for consistency — if the same concept was translated differently across titles, standardize it and re-run affected titles
4. Append the Glossary Change Proposals section at the end (see Step 4)

*Completion Criterion*: All titles in the batch are processed through all 4 steps, output as a table with a Flags column for ambiguous items. Glossary change proposals are listed (not directly applied). No concept is translated inconsistently across the batch.

---

## Reference

### Machine Translation Red Flags

Check the output against the red flags for the relevant source language. If any pattern is detected, revise immediately.

#### CN → KR Red Flags

| Red Flag | Example (❌ wrong) | Fix (✅ correct) | Why it's wrong |
|----------|-------------------|-----------------|----------------|
| Chinese idiom transliterated | "정치통근" (from 精致通勤) | "커뮤터룩" or omit | Korean fashion never transliterates 四字成语 |
| Sino-Korean where Konglish is norm | "연의상" (连衣裙 → 连衣裳) | "원피스" | Real shoppers say 원피스, never 연의상 |
| Chinese modifier order preserved | "우아한 통근 A라인 원피스" | "A라인 오피스룩 원피스" | Korean puts the most specific modifier closest to the noun |
| Overly literary register | "정교한 자수 장식" | "자수 디테일" | Shopping titles use casual, magazine-style register |
| "의" particle chains | "봄의 새로운 스타일의 원피스" | "봄 신상 원피스" | Real titles drop particles; "의" chains = translation smell |
| Non-existent Konglish | "커뮤팅 스타일" | "커뮤터룩" or "오피스룩" | Inventing Konglish that Korean speakers don't use |
| Redundant category word | "여성 원피스 드레스" | "원피스" | 원피스 already means dress; 여성 is implied |
| Meaning-empty adjective survived | "세련된 고급스러운 시크한 원피스" | "시크 원피스" | Stacked vague adjectives = classic MT artifact |

#### EN → KR Red Flags

| Red Flag | Example (❌ wrong) | Fix (✅ correct) | Why it's wrong |
|----------|-------------------|-----------------|----------------|
| English kept untranslated | "Floral Print Chiffon Dress" | "플로럴 쉬폰 원피스" | Must be Korean, not English |
| English adjective directly transliterated | "스터닝 엘레강트 드레스" | "시크 원피스" | "stunning elegant" are marketing fluff, not Korean fashion vocabulary |
| English word order preserved | "캐주얼 코튼 루즈핏 와이드 팬츠" | "코튼 와이드 팬츠 (루즈핏)" | Too many stacked modifiers; move secondary details to parentheses |
| Marketing term carried over | "머스트해브 뉴 시즌 원피스" | "신상 원피스" | "must-have" has no Korean shopping equivalent; use 신상 |
| English compound kept as-is | "버튼프론트 셔츠자켓" | "버튼 셔츠 자켓" | Break compounds into natural Korean word spacing |
| Over-Konglish | "캐주얼 컴포터블 릴렉스핏" | "캐주얼 루즈핏" | Not every English word has a Konglish equivalent; "comfortable" is not used in KR fashion titles |

#### JA → KR Red Flags

| Red Flag | Example (❌ wrong) | Fix (✅ correct) | Why it's wrong |
|----------|-------------------|-----------------|----------------|
| Japanese katakana carried unchanged | "ワンピース" → "완피스" | "원피스" | Must use established Korean spelling, not phonetic transfer from Japanese |
| Japanese-only fashion term | "ゆったり" → "유탓리" | "루즈핏" or "오버핏" | ゆったり has no Korean transliteration; use the Korean fashion equivalent |
| Japanese honorific/polite register | "お上品な 원피스" | "시크 원피스" | Korean shopping titles don't use Japanese politeness markers |
| Japanese bracket marketing | "【新作】신상 원피스" | "신상 원피스" | Remove Japanese brackets and tags entirely |
| Japanese reading of shared kanji | "紺色" → "곤색" (Japanese reading kon) | "네이비" | Use the Korean shopping term, not the Japanese kanji reading |
| Mixing Japanese and Korean particles | "스트라이프の원피스" | "스트라이프 원피스" | No Japanese particles in Korean output |

### Ambiguous Term Handling

Some source terms map to multiple Korean terms depending on context. When you encounter these, do NOT silently pick one — flag the ambiguity.

**Known ambiguous terms:**

| Source Term | Possible Korean Mappings | How to Decide | If Still Unclear |
|------------|------------------------|---------------|------------------|
| EN: "top" | 탑 (sleeveless/cropped), 티셔츠 (t-shirt), 블라우스 (blouse) | Check if source mentions sleeve/fabric/neckline cues | Flag: `[⚠️ 확인필요: 탑/티셔츠/블라우스]` |
| CN: "衬衫" | 셔츠 (casual shirt), 블라우스 (formal/feminine) | 셔츠 for unisex/casual cuts, 블라우스 for feminine/dressy | Flag: `[⚠️ 확인필요: 셔츠/블라우스]` |
| EN: "vest" | 베스트 (layering vest/gilet), 탱크탑 (sleeveless top) | 베스트 if outerwear/layering, 탱크탑 if underwear/casual | Flag: `[⚠️ 확인필요: 베스트/탱크탑]` |
| CN: "背心" | 베스트 (outerwear vest), 탱크탑 (tank top) | Same as above | Flag: `[⚠️ 확인필요: 베스트/탱크탑]` |
| JA: "ワンピース" | 원피스 (dress, default) | Almost always 원피스 in Korean | Rarely ambiguous |
| EN: "pants" / CN: "裤子" | 팬츠 (Konglish), 바지 (native Korean) | 팬츠 for fashion-forward context, 바지 for casual/daily | Default: 팬츠 |
| CN: "外套" | 아우터 (generic outerwear), 자켓 (jacket), 코트 (coat) | 자켓 if short/structured, 코트 if long, 아우터 if ambiguous | Flag if no length/structure cues |

**General ambiguity protocol:**
1. Look for contextual cues in the source title (fabric, sleeve type, formality, length)
2. If cues resolve the ambiguity → pick the appropriate term, no flag needed
3. If no cues or cues are contradictory → output the most likely option + `[⚠️ 확인필요: option A/option B]`
4. In batch mode, group all flagged items at the end for efficient human review

### Translation Principles

**What makes a good Korean fashion title:**
- Concise: shoppers scan, they don't read
- Descriptive over decorative: "세로 줄무늬" > "버티컬 스트라이프" when possible
- Action-oriented: it should help the shopper imagine wearing it
- Consistent: same concept should use the same Korean term across all products

**What to avoid:**
- Direct transliteration of source language adjectives
- Stacking multiple adjectives before the item type
- Including size/fit details in the title (those belong in the description)
- Using brand-style names that don't mean anything in Korean

### Examples

#### Chinese → Korean

**CN Example 1 — Over-decorated source:**

Input: "精致通勤垂直条纹衬衫撞色荷叶边饰自系腰带连衣裙"

Step 1 (optimize): "通勤风条纹连衣裙（撞色荷叶边）"

Step 2 (translate): `커뮤터룩 스트라이프 원피스 (컬러블록 러플)`

Step 3 (check):
- Length: 18 chars → ideal range would be ≤15, but all words carry product identity → acceptable at 16-25 tier
- Consecutive loanwords: "커뮤터룩 스트라이프 원피스" = 3 consecutive, but all standard Korean shopping terms → acceptable exception
- Glossary: consistent → OK
- Adjective stacking: none → OK
- Back-translation: "커뮤터룩 스트라이프 원피스 (컬러블록 러플)" → "通勤风条纹连衣裙（撞色荷叶边）" — matches optimized source → OK
- Red flag scan: no transliterated idioms, no particle chains, casual register → OK
- **PASS**

**CN Example 2 — Simple item:**

Input: "100% 纯棉 T 恤"

Step 1 (optimize): "纯棉 T 恤"

Step 2 (translate): `순면 티셔츠`

Step 3 (check):
- Length: 6 chars → OK. Loanwords: 0 consecutive → OK. Back-translation: "순면 티셔츠" → "纯棉T恤" — matches → OK. Red flags: none → **PASS**

#### English → Korean

**EN Example 1 — Marketing-heavy source:**

Input: "Women's Stunning Elegant Floral Print Chiffon Midi Wrap Dress"

Step 1 (optimize): "Floral chiffon wrap dress (midi)"

Step 2 (translate): `플로럴 쉬폰 랩 원피스 (미디)`

Step 3 (check):
- Length: 15 chars → ideal range ≤15 → OK
- Consecutive loanwords: "플로럴 쉬폰 랩 원피스" = 4 consecutive, but 쉬폰/원피스 are standard and "랩" is established Konglish for wrap style → acceptable exception
- Back-translation: "플로럴 쉬폰 랩 원피스 (미디)" → "Floral chiffon wrap dress (midi)" — matches → OK
- Red flag scan: no untranslated English, no marketing terms carried over → OK
- **PASS**

**EN Example 2 — Over-described casual item:**

Input: "NEW! Must-Have Trendy Vintage Washed Relaxed Fit Oversized Denim Jacket for Women"

Step 1 (optimize): "Vintage washed denim jacket (oversized)"

Step 2 (translate): `빈티지 워싱 데님 자켓 (오버핏)`

Step 3 (check):
- Length: 15 chars → ideal range ≤15 → OK
- Back-translation: "빈티지 워싱 데님 자켓 (오버핏)" → "Vintage washed denim jacket (oversized)" — matches → OK
- Red flag scan: "must-have" and "trendy" correctly removed, no transliterated English marketing → OK
- **PASS**

**EN Example 3 — Ambiguous "top" (demonstrating ambiguity flagging):**

Input: "Women's Casual Chic Satin Top"

Step 1 (optimize): "Satin top"

Step 2 (translate): "top" maps to 탑/티셔츠/블라우스 — source says "satin" (dressy fabric) but "casual" (informal context). Cues are contradictory → flag.

Output: `새틴 블라우스 [⚠️ 확인필요: 블라우스/캐미솔]`

Step 3 (check):
- Length: 10 chars (excluding flag) → ideal range → OK
- Back-translation: "새틴 블라우스" → "Satin blouse" — close to "Satin top" but not identical, ambiguity flag is warranted → OK
- **PASS (with flag for human review)**

#### Japanese → Korean

**JA Example 1 — Filler-heavy source:**

Input: "大人可愛い通勤オフィスカジュアルAラインフレアスカート"

Step 1 (optimize): "通勤風Aラインスカート"

Step 2 (translate): `오피스룩 A라인 스커트`

Step 3 (check):
- Length: 12 chars → ideal range ≤15 → OK
- Back-translation: "오피스룩 A라인 스커트" → "通勤風Aラインスカート" — matches → OK
- Red flag scan: no Japanese katakana carried unchanged, no Japanese particles → OK
- **PASS**

**JA Example 2 — Bracket marketing with detail:**

Input: "【新作】おしゃれで上品な花柄シフォンロングワンピース"

Step 1 (optimize): "花柄シフォンワンピース（ロング）"

Step 2 (translate): `플로럴 쉬폰 원피스 (롱)`

Step 3 (check):
- Length: 13 chars → ideal range ≤15 → OK
- Back-translation: "플로럴 쉬폰 원피스 (롱)" → "花柄シフォンワンピース（ロング）" — matches → OK
- Red flag scan: brackets removed, "おしゃれ/上品" correctly dropped, no Japanese readings used → OK
- **PASS**
