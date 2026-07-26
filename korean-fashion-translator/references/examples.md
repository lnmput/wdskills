# Step-by-Step Translation Examples

These examples demonstrate the correct application of the translation workflow on various source titles.

## Chinese → Korean Examples

### Example 1 — Over-decorated source
- **Input**: "精致通勤垂直条纹衬衫撞色荷叶边饰自系腰带连衣裙"
- **Step 1 (Optimize)**: "通勤风条纹连衣裙（撞色荷叶边）" *(Dropped "精致", "垂直", "自系腰带" as secondary details or redundant, moved "撞色荷叶边" to parentheses)*
- **Step 2 (Translate)**: `커뮤터룩 스트라이프 원피스 (컬러블록 러플)`
- **Step 3 (Quality Check)**:
  - **Length**: 18 characters (within acceptable range ≤25).
  - **Consecutive loanwords**: "커뮤터룩 스트라이프 원피스" contains 3 consecutive loanwords, but each is a standard Korean shopping term. Acceptable.
  - **Back-translation**: "커뮤터룩 스트라이프 원피스 (컬러블록 러플)" → "通勤风条纹连衣裙（撞色荷叶边）" — matches optimized source exactly.
  - **MT Red Flags**: No transliterated idioms, casual register. Pass.
- **Output**: `커뮤터룩 스트라이프 원피스 (컬러블록 러플)`

### Example 2 — Simple item
- **Input**: "100% 纯棉 T 恤"
- **Step 1 (Optimize)**: "纯棉 T 恤"
- **Step 2 (Translate)**: `순면 티셔츠`
- **Step 3 (Quality Check)**:
  - **Length**: 6 characters (ideal range).
  - **Back-translation**: "순면 티셔츠" → "纯棉T恤". Pass.
- **Output**: `순면 티셔츠`

---

## English → Korean Examples

### Example 1 — Marketing-heavy source
- **Input**: "Women's Stunning Elegant Floral Print Chiffon Midi Wrap Dress"
- **Step 1 (Optimize)**: "Floral chiffon wrap dress (midi)" *(Dropped "Women's", "Stunning", "Elegant" as marketing fluff/implied)*
- **Step 2 (Translate)**: `플로럴 쉬폰 랩 원피스 (미디)`
- **Step 3 (Quality Check)**:
  - **Length**: 15 characters (ideal range).
  - **Consecutive loanwords**: "플로럴 쉬폰 랩 원피스" = 4 consecutive, but all are standard and established Konglish. Acceptable.
  - **Back-translation**: "플로럴 쉬폰 랩 원피스 (미디)" → "Floral chiffon wrap dress (midi)". Pass.
- **Output**: `플로럴 쉬폰 랩 원피스 (미디)`

### Example 2 — Over-described casual item
- **Input**: "NEW! Must-Have Trendy Vintage Washed Relaxed Fit Oversized Denim Jacket for Women"
- **Step 1 (Optimize)**: "Vintage washed denim jacket (oversized)"
- **Step 2 (Translate)**: `빈티지 워싱 데님 자켓 (오버핏)`
- **Step 3 (Quality Check)**:
  - **Length**: 15 characters (ideal range).
  - **Back-translation**: "빈티지 워싱 데님 자켓 (오버핏)" → "Vintage washed denim jacket (oversized)". Pass.
- **Output**: `빈티지 워싱 데님 자켓 (오버핏)`

### Example 3 — Ambiguous "top" (Demonstrating ambiguity flagging)
- **Input**: "Women's Casual Chic Satin Top"
- **Step 1 (Optimize)**: "Satin top"
- **Step 2 (Translate)**: "top" maps to 탑/티셔츠/블라우스. Cues are contradictory ("satin" is formal, "casual" is informal). Flag ambiguity.
- **Output**: `새틴 블라우스 [⚠️ 확인필요: 블라우스/캐미솔]`

---

## Japanese → Korean Examples

### Example 1 — Filler-heavy source
- **Input**: "大人可愛い通勤オフィスカジュアルAラインフレアスカート"
- **Step 1 (Optimize)**: "通勤風Aラインスカート" *(Dropped filler "大人可愛い" and collapsed "通勤オフィスカジュアル")*
- **Step 2 (Translate)**: `오피스룩 A라인 스커트`
- **Step 3 (Quality Check)**:
  - **Length**: 12 characters (ideal range).
  - **Back-translation**: "오피스룩 A라인 스커트" → "通勤風Aラインスカート". Pass.
- **Output**: `오피스룩 A라인 스커트`

### Example 2 — Bracket marketing with detail
- **Input**: "【新作】おしゃれで上品な花柄シフォンロングワンピース"
- **Step 1 (Optimize)**: "花柄シフォンワンピース（ロング）" *(Dropped "【新作】" and fillers "おしゃれで上品な")*
- **Step 2 (Translate)**: `플로럴 쉬폰 원피스 (롱)`
- **Step 3 (Quality Check)**:
  - **Length**: 13 characters.
  - **Back-translation**: "플로럴 쉬폰 원피스 (롱)" → "花柄シフォンワンピース（ロング）". Pass.
- **Output**: `플로럴 쉬폰 원피스 (롱)`
