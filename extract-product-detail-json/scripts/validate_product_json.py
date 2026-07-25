#!/usr/bin/env python3
"""Normalize and validate the fixed product-detail JSON contract."""

import argparse
import json
import math
import sys
from pathlib import Path
from urllib.parse import urlparse

TOP_KEYS = [
    "id", "url", "title", "market_price", "price", "images", "content",
    "colors", "sizes", "shop", "from",
]
SHOP_KEYS = ["id", "name", "url", "price"]
COLOR_KEYS = ["name", "img"]


def fail(message):
    raise ValueError(message)


def text(value, field, allow_empty=False):
    if not isinstance(value, str):
        fail(f"{field} must be a string")
    value = value.strip()
    if not allow_empty and not value:
        fail(f"{field} must not be empty")
    return value


def number(value, field):
    if isinstance(value, bool):
        fail(f"{field} must be a number")
    try:
        value = float(value)
    except (TypeError, ValueError):
        fail(f"{field} must be a number")
    if not math.isfinite(value) or value < 0:
        fail(f"{field} must be a finite non-negative number")
    return int(value) if value.is_integer() else value


def absolute_url(value, field, allow_empty=False):
    value = text(value, field, allow_empty=allow_empty)
    if not value and allow_empty:
        return value
    if value.startswith("//"):
        value = "https:" + value
    parsed = urlparse(value)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        fail(f"{field} must be an absolute HTTP(S) URL")
    return value


def string_list(value, field, urls=False):
    if not isinstance(value, list):
        fail(f"{field} must be an array")
    result = []
    seen = set()
    for index, item in enumerate(value):
        item = absolute_url(item, f"{field}[{index}]") if urls else text(item, f"{field}[{index}]")
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result


def normalize(data):
    if not isinstance(data, dict):
        fail("top-level JSON value must be an object")
    missing = [key for key in TOP_KEYS if key not in data]
    extra = [key for key in data if key not in TOP_KEYS]
    if missing or extra:
        fail(f"top-level keys mismatch; missing={missing}, extra={extra}")

    shop = data["shop"]
    if not isinstance(shop, dict) or set(shop) != set(SHOP_KEYS):
        fail(f"shop must contain exactly {SHOP_KEYS}")

    colors = data["colors"]
    if not isinstance(colors, list):
        fail("colors must be an array")
    normalized_colors = []
    for index, color in enumerate(colors):
        if not isinstance(color, dict) or set(color) != set(COLOR_KEYS):
            fail(f"colors[{index}] must contain exactly {COLOR_KEYS}")
        normalized_colors.append({
            "name": text(color["name"], f"colors[{index}].name"),
            "img": absolute_url(color["img"], f"colors[{index}].img", allow_empty=True),
        })

    product_url = absolute_url(data["url"], "url")
    images = string_list(data["images"], "images", urls=True)
    content = string_list(data["content"], "content", urls=True)

    return {
        "id": text(data["id"], "id"),
        "url": product_url,
        "title": text(data["title"], "title"),
        "market_price": number(data["market_price"], "market_price"),
        "price": number(data["price"], "price"),
        "images": images,
        "content": content,
        "colors": normalized_colors,
        "sizes": string_list(data["sizes"], "sizes"),
        "shop": {
            "id": text(shop["id"], "shop.id", allow_empty=True),
            "name": text(shop["name"], "shop.name", allow_empty=True),
            "url": absolute_url(shop["url"], "shop.url"),
            "price": number(shop["price"], "shop.price"),
        },
        "from": product_url,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        with args.input.open("r", encoding="utf-8") as handle:
            normalized = normalize(json.load(handle))
        rendered = json.dumps(normalized, ensure_ascii=False, indent=2) + "\n"
        if args.output:
            args.output.write_text(rendered, encoding="utf-8")
        else:
            sys.stdout.write(rendered)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
