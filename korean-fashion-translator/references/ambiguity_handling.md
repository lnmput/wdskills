# Ambiguous Term Handling Reference

Some source terms map to multiple Korean terms depending on context. When translating, do not silently guess — follow this guide to resolve or flag the ambiguity.

## Known Ambiguous Terms

| Source Term | Possible Korean Mappings | How to Decide | If Still Unclear |
|------------|------------------------|---------------|------------------|
| EN: "top" | 탑 (sleeveless/cropped), 티셔츠 (t-shirt), 블라우스 (blouse) | Check if source mentions sleeve/fabric/neckline cues | Flag: `[⚠️ 확인필요: 탑/티셔츠/블라우스]` |
| CN: "衬衫" | 셔츠 (casual shirt), 블라우스 (formal/feminine) | 셔츠 for unisex/casual cuts, 블라우스 for feminine/dressy | Flag: `[⚠️ 확인필요: 셔츠/블라우스]` |
| EN: "vest" | 베스트 (layering vest/gilet), 탱크탑 (sleeveless top) | 베스트 if outerwear/layering, 탱크탑 if underwear/casual | Flag: `[⚠️ 확인필요: 베스트/탱크탑]` |
| CN: "背心" | 베스트 (outerwear vest), 탱크탑 (tank top) | Same as above | Flag: `[⚠️ 확인필요: 베스트/탱크탑]` |
| JA: "ワンピース" | 원피스 (dress, default) | Almost always 원피스 in Korean | Rarely ambiguous |
| EN: "pants" / CN: "裤子" | 팬츠 (Konglish), 바지 (native Korean) | 팬츠 for fashion-forward context, 바지 for casual/daily | Default: 팬츠 |
| CN: "外套" | 아우터 (generic outerwear), 자켓 (jacket), 코트 (coat) | 자켓 if short/structured, 코트 if long, 아우터 if ambiguous | Flag if no length/structure cues |

## General Ambiguity Protocol

1. **Contextual Clues**: Search for contextual cues in the source title (fabric, sleeve type, formality, length).
2. **Resolve**: If cues resolve the ambiguity, pick the appropriate term. No flag is needed.
3. **Flag**: If no cues exist or cues are contradictory, output the most likely option followed by a flag: `[⚠️ 확인필요: option A/option B]`.
4. **Batch Review**: In batch mode, highlight these flags in the "Notes/Flags" column of your output table for easy human review.
