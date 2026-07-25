---
name: extract-product-detail-json
description: Extract complete product information from a public e-commerce product detail URL with ego-browser by default and save it as a JSON file with an exact, validated schema. Use when a user provides a product page (including JavaScript-rendered or marketplace pages), asks to scrape or collect product details, or requires output compatible with demo.json fields such as prices, gallery images, detail images, variants, sizes, and shop data.
---

# Extract Product Detail JSON

Extract one product page into a single UTF-8 JSON object and return the saved `.json` file.

## Workflow

1. Read [references/schema.md](references/schema.md) before extracting. Treat it as the output contract.
2. Use the `ego-browser` skill and `ego-browser nodejs` as the default and first extraction route. Do not start with a built-in browser, web fetch, or `curl`.
3. Create or reuse one task space for the extraction, open the supplied URL with `openOrReuseTab`, and wait for the page to render.
4. Inspect `snapshotText()` first, then use one `js()` IIFE when compact DOM, structured-data, page-state, or image extraction is needed. Inspect relevant browser network state only when the rendered page is insufficient.
5. Extract only evidence from the target page. Do not invent missing values or use a different seller's listing.
6. Assemble all 11 required top-level fields. Use the fallback rules in the schema reference for genuinely unavailable values.
7. Save the candidate object to a `.json` file, then run:

   ```bash
   python3 scripts/validate_product_json.py candidate.json --output product.json
   ```

8. If validation fails, correct the extraction and rerun it. Do not deliver an unvalidated file.
9. After a prior browser round confirms extraction is complete, close the task space in a dedicated final `ego-browser` invocation with `completeTaskSpace(taskId, { keep: false })`.
10. Return a link to `product.json` and briefly disclose any fields that used fallback values or any access limitation.

## Ego-browser Default

Use a short goal-specific task-space name and reuse its numeric ID across browser rounds:

```bash
ego-browser nodejs <<'EOF'
const task = await useOrCreateTaskSpace('extract product detail')
await openOrReuseTab(PRODUCT_URL, { wait: true, timeout: 30 })
cliLog(JSON.stringify({
  taskId: task.id,
  page: await pageInfo(),
  snapshot: await snapshotText(),
}))
EOF
```

Replace `PRODUCT_URL` with a valid JavaScript string literal before running the command. Keep browser-side extraction inside one explicit `js(String.raw\`(() => { ... })()\`)` call and print results only through `cliLog`.

Use direct HTTP retrieval only as a fallback after ego-browser fails for a technical reason and only when the HTTP response exposes equivalent product evidence. Do not silently substitute another browser tool.

## Extraction Rules

- Preserve the canonical or final resolved product URL in `url`.
- Prefer the product/listing ID exposed by page data; otherwise derive the stable ID from the URL path or query.
- Record displayed numeric prices without currency symbols. Set `market_price` to the struck/list/original price when shown; otherwise use `price`.
- Deduplicate `images` without changing the order of first occurrence.
- Deduplicate `content` without changing the order of first occurrence. The same URL may remain once in `images` and once in `content`.
- Put long-description/detail images in `content`, not in `images`. Exclude site chrome, payment badges, tracking pixels, and unrelated recommendations.
- Collect every visible color/style variant and its swatch or preview image. Use an empty string for a color image only when none is supplied.
- Keep size labels exactly as displayed, including recommendations.
- Use the seller/store link for `shop.url`; if unavailable, use the product URL.
- Set `from` to exactly the same absolute product URL as `url`.
- Convert protocol-relative URLs beginning with `//` to `https://` before delivery.
- Preserve non-ASCII text and write valid UTF-8 JSON.

## Access Failures

If authentication, CAPTCHA, region restrictions, or anti-bot controls interrupt ego-browser, hand off its task space to the user and state the exact action required. Resume only after the user explicitly confirms. If the data still cannot be accessed, stop and report the blocked URL and reason; do not fabricate a JSON file that appears complete.
