# Machine Translation Red Flags

Check your translation output against these red flags for the relevant source language. If any pattern is detected, revise immediately.

## CN → KR Red Flags

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

## EN → KR Red Flags

| Red Flag | Example (❌ wrong) | Fix (✅ correct) | Why it's wrong |
|----------|-------------------|-----------------|----------------|
| English kept untranslated | "Floral Print Chiffon Dress" | "플로럴 쉬폰 원피스" | Must be Korean, not English |
| English adjective directly transliterated | "스터닝 엘레강트 드레스" | "시크 원피스" | "stunning elegant" are marketing fluff, not Korean fashion vocabulary |
| English word order preserved | "캐주얼 코튼 루즈핏 와이드 팬츠" | "코튼 와이드 팬츠 (루즈핏)" | Too many stacked modifiers; move secondary details to parentheses |
| Marketing term carried over | "머스트해브 뉴 시즌 원피스" | "신상 원피스" | "must-have" has no Korean shopping equivalent; use 신상 |
| English compound kept as-is | "버튼프론트 셔츠자켓" | "버튼 셔츠 자켓" | Break compounds into natural Korean word spacing |
| Over-Konglish | "캐주얼 컴포터블 릴렉스핏" | "캐주얼 루즈핏" | Not every English word has a Konglish equivalent; "comfortable" is not used in KR fashion titles |

## JA → KR Red Flags

| Red Flag | Example (❌ wrong) | Fix (✅ correct) | Why it's wrong |
|----------|-------------------|-----------------|----------------|
| Japanese katakana carried unchanged | "ワンピース" → "완피스" | "원피스" | Must use established Korean spelling, not phonetic transfer from Japanese |
| Japanese-only fashion term | "ゆったり" → "유탓리" | "루즈핏" or "오버핏" | ゆったり has no Korean transliteration; use the Korean fashion equivalent |
| Japanese honorific/polite register | "お上品な 원피스" | "시크 원피스" | Korean shopping titles don't use Japanese politeness markers |
| Japanese bracket marketing | "【新作】신상 원피스" | "신상 원피스" | Remove Japanese brackets and tags entirely |
| Japanese reading of shared kanji | "紺色" → "곤색" (Japanese reading kon) | "네이비" | Use the Korean shopping term, not the Japanese kanji reading |
| Mixing Japanese and Korean particles | "스트라이프の원피스" | "스트라이프 원피스" | No Japanese particles in Korean output |
