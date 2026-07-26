---
name: korean-fashion-translator
description: >-
  Translate and optimize fashion product titles to Korean.
  Use when: translating Chinese, English, or Japanese fashion titles to Korean,
  or optimizing existing Korean titles for shopping mall readability.
---

# Korean Fashion Product Title Translator

Translate fashion e-commerce titles from Chinese, English, or Japanese into natural, concise Korean product names. The output should read like titles written by a native Korean fashion shopping mall curator — not like machine-translated product listings.

**Supported source languages:** Chinese (中文), English, Japanese (日本語)

---

## Reference Materials

To ensure high-quality and consistent translations, consult these reference guides:
- [glossary.md](references/glossary.md): Look up fashion terminology to maintain consistency across translations.
- [red_flags.md](references/red_flags.md): Read during quality checks to scan for common machine-translation issues.
- [ambiguity_handling.md](references/ambiguity_handling.md): Read when dealing with ambiguous terms (e.g., "top", "vest", "衬衫") to decide the best translation.
- [examples.md](references/examples.md): Review step-by-step translation examples for CN, EN, and JA.

---

## Translation Workflow

For each product title, follow this four-step process:

### Step 1: Optimize the Source Title

Before translating, identify the source language and strip the input down to its essence.

**Target format:** `[style tag] + [key feature] + [category]`. Move secondary details (fabric, specific trim, length) into parentheses. Aim for 3-5 core words. Retain additional words only when they carry critical distinguishing meaning (e.g., size-specific terms like "petite" or "plus-size").

Apply language-specific optimization guidelines:
- **Chinese Sources**: Drop generic adjectives ("精致", "优雅", "时尚", "气质" unless they are genuine differentiators). Remove gender terms ("女士", "女装", "女性"). Keep "韩版" only if it is a key style differentiator.
- **English Sources**: Drop marketing fluff ("stunning", "gorgeous", "beautiful", "must-have", "trendy", "NEW!", "SALE"). Remove gender terms ("women's", "ladies'", "for women"). Remove SKU numbers, brand prefixes, and ALL CAPS marketing. Collapse redundant adjectives.
- **Japanese Sources**: Drop generic fillers ("大人可愛い", "おしゃれ", "素敵な", "上品な"). Remove gender terms ("レディース", "婦인" / "婦人"). Remove bracketed tags ("【新作】", "【送料無料】", "【人気】").

*Completion Criterion*: The optimized title follows `[style tag] + [key feature] + [category]`, secondary details are in parentheses, and language-specific filler words are removed. Every remaining word serves a distinguishing purpose.

### Step 2: Translate to Korean

Translate the optimized title to Korean following these constraints:
1. Output ONLY the Korean title, no explanations.
2. **Length guideline** (soft limits):
   - **Ideal**: 8-15 characters — covers most single items, aim here first.
   - **Acceptable**: 16-25 characters — use when dropping words would lose key product identity.
   - **Too long**: 26+ characters — always shorten; at this length, the title is not scannable.
3. Format: `[스타일 키워드] [주요 특징] [품목명]` (e.g., `커뮤터룩 스트라이프 원피스`). If the product has no meaningful style keyword, skip it rather than inventing one.
4. Use natural Konglish only where Korean shoppers expect it (e.g., "데님", "셔츠", "스트라이프").
5. Do NOT directly transliterate source language adjectives — find the natural Korean equivalent.
6. If the source has parentheses with extra info, keep them if they add value, drop them otherwise.
7. **Ambiguity Handling**: When a term is ambiguous, refer to [ambiguity_handling.md](references/ambiguity_handling.md). If context doesn't resolve it, append a flag: `[⚠️ 확인필요: A or B]` (e.g., `캐미솔 탑 [⚠️ 확인필요: 캐미솔/탱크탑]`).

Cross-reference [glossary.md](references/glossary.md) during this step to ensure term-level consistency.

*Completion Criterion*: The Korean output is within the acceptable length range (≤25 characters), follows the format guideline, uses glossary-specified translations, and flags unresolved ambiguous terms.

### Step 3: Quality Check the Output

Verify the translation using these checks in order:
1. **Length check**: If output > 25 characters, shorten it. If 16-25 characters, verify every word is essential.
2. **Consecutive loanword check**: If 3+ consecutive non-Korean words appear, replace at least one with a native Korean equivalent (e.g., "버티컬 스트라이프 셔츠" → "세로 줄무늬 셔츠") unless they are standard Korean shopping terms.
3. **Glossary check**: Ensure all glossary terms match [glossary.md](references/glossary.md).
4. **Adjective stacking**: If 2+ consecutive adjectives remain, keep only the most distinctive one.
5. **Back-translation**: Translate the Korean output back to the original language. Ensure core item type and key attributes match the optimized source title.
6. **Red flag scan**: Audit the translation against [red_flags.md](references/red_flags.md) for the source language. Revise if any red flags are triggered.

*Completion Criterion*: All quality checks pass. The back-translation matches the optimized source title. Unresolved ambiguous terms remain flagged with `[⚠️ 확인필요]`.

### Step 4: Propose Glossary Updates

Suggest updates to [glossary.md](references/glossary.md) if you encounter new or better terms. Append proposals to the end of your output in this format:

```
## 📋 Glossary Change Proposals

| Action | Source Term | Proposed 한국어 | Reason | Confidence |
|--------|-----------|-----------------|--------|------------|
| ADD    | chiffon   | 쉬폰            | appeared 3x in this batch, not yet in glossary | high |
| UPDATE | 条纹 → 줄무늬 | 스트라이프 (primary) | 스트라이프 is more common on Korean malls | medium |
```

Do not edit `glossary.md` directly without user confirmation.
- **ADD**: Only propose terms that appeared 2+ times or are standard fashion vocabulary.
- **UPDATE**: Must include a concrete reason.
- **Confidence**: `high` (industry standard), `medium` (common alternative), `low` (needs review).

*Completion Criterion*: Glossary change proposals are correctly listed (or stated as "None") with Action, Source Term, Proposed Korean, Reason, and Confidence.

---

## Batch Processing

When translating multiple titles at once:
1. Group titles by source language if mixed.
2. Process each title through Steps 1 to 3.
3. Output the results as a markdown table:
   `| Original Title | Optimized Source | Korean Translation | Notes/Flags |`
4. Review the batch for consistency. Ensure the same concept is translated identically across all titles.
5. Append the Glossary Change Proposals section at the end of the batch.

*Completion Criterion*: All titles are processed and output in the markdown table. Translations are consistent across the batch, and glossary proposals are appended at the end.
