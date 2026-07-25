# Product JSON contract

Output exactly one JSON object with these keys in this order. Additional keys are not allowed.

```json
{
  "id": "string",
  "url": "https://example.com/product/123",
  "title": "string",
  "market_price": 0.0,
  "price": 0.0,
  "images": ["https://example.com/gallery-1.jpg"],
  "content": ["https://example.com/detail-1.jpg"],
  "colors": [{"name": "string", "img": "https://example.com/swatch.jpg"}],
  "sizes": ["string"],
  "shop": {"id": "string", "name": "string", "url": "https://example.com/shop", "price": 0.0},
  "from": "https://example.com/product/123"
}
```

## Field rules

| Field | Type | Rule |
|---|---|---|
| `id` | string | Stable listing/product identifier; must not be empty. |
| `url` | string | Absolute `http` or `https` product URL. |
| `title` | string | Product title as displayed; must not be empty. |
| `market_price` | number | Original/list price when shown; otherwise equal to `price`. |
| `price` | number | Current displayed base price; use the minimum current variant price for a range. |
| `images` | string array | Ordered gallery image URLs; deduplicate without reordering; absolute URLs only. |
| `content` | string array | Ordered detail-image URLs; deduplicate without reordering. A URL may also appear in `images`. |
| `colors` | object array | Each object contains exactly `name` and `img`; `img` may be empty when unavailable. |
| `sizes` | string array | Visible size/option labels in display order. |
| `shop` | object | Contains exactly `id`, `name`, `url`, and `price`; `price` normally equals top-level `price`. |
| `from` | string | Must equal the absolute product URL in `url`. |

## Missing-value policy

- Never omit a field and never use `null`.
- Use `[]` when `images`, `content`, `colors`, or `sizes` are genuinely absent.
- Use `""` for unavailable `shop.id`, `shop.name`, or `colors[].img`.
- Use the product URL for `shop.url` when no separate shop URL exists.
- Use `price` for unavailable `market_price` and `shop.price`.
- Do not use empty strings for `id`, `url`, `title`, or `from`.
- Deduplicate `images` and `content` independently; do not remove a URL merely because it occurs in both arrays.
