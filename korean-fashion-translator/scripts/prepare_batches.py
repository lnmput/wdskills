#!/usr/bin/env python3
"""
prepare_batches.py — Fetch products from API and generate batch files for Antigravity translation.

Usage:
    python prepare_batches.py

Output:
    data/batches/batch_001.md, batch_002.md, ...
    Each file contains a formatted prompt ready to paste into Antigravity.
"""

import json
import math
import os
import sys
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode

from config import API_BASE_URL, API_TOKEN, BATCH_SIZE, BATCHES_DIR


def fetch_products(page: int = 1, page_size: int = 100) -> dict:
    """Fetch a page of untranslated products from the API."""
    params = urlencode({"status": "untranslated", "page": page, "page_size": page_size})
    url = f"{API_BASE_URL}/products?{params}"

    req = Request(url, method="GET")
    req.add_header("Authorization", f"Bearer {API_TOKEN}")
    req.add_header("Accept", "application/json")

    try:
        with urlopen(req) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except HTTPError as e:
        print(f"❌ API error: {e.code} {e.reason}")
        print(f"   URL: {url}")
        if e.code == 401:
            print("   → Check API_TOKEN in config.py")
        sys.exit(1)
    except URLError as e:
        print(f"❌ Connection error: {e.reason}")
        print(f"   → Check API_BASE_URL in config.py: {API_BASE_URL}")
        sys.exit(1)


def fetch_all_products() -> list[dict]:
    """Fetch all untranslated products with pagination."""
    all_products = []
    page = 1

    print(f"📡 Fetching products from {API_BASE_URL}/products ...")

    while True:
        data = fetch_products(page=page, page_size=100)
        products = data.get("products", [])
        total = data.get("total", 0)

        if not products:
            break

        all_products.extend(products)
        print(f"   Page {page}: fetched {len(products)} products (total so far: {len(all_products)}/{total})")

        if len(all_products) >= total:
            break
        page += 1

    print(f"✅ Fetched {len(all_products)} products total\n")
    return all_products


def generate_batch_prompt(batch_number: int, products: list[dict]) -> str:
    """Generate a markdown prompt for a batch of products."""
    lines = [
        f"请按照 korean-fashion-translator skill 翻译以下 {len(products)} 条产品标题。",
        "",
        "输出为 markdown 表格，列为：`| id | source_lang | title_optimized | title_ko | status | review_flag |`",
        "",
        "如有术语表提案，请附在表格后的 `## 📋 Glossary Change Proposals` 区块中。",
        "",
        "---",
        "",
        "| id | title | source_lang |",
        "|----|-------|-------------|",
    ]

    for p in products:
        pid = p["id"]
        title = p["title"].replace("|", "\\|")  # Escape pipes in markdown tables
        lang = p.get("source_lang", "auto")
        lines.append(f"| {pid} | {title} | {lang} |")

    return "\n".join(lines) + "\n"


def main():
    # Fetch all products
    products = fetch_all_products()

    if not products:
        print("ℹ️  No untranslated products found.")
        return

    # Create batches directory
    batches_path = Path(BATCHES_DIR)
    batches_path.mkdir(parents=True, exist_ok=True)

    # Clear existing batch files
    for f in batches_path.glob("batch_*.md"):
        f.unlink()

    # Split into batches and write files
    num_batches = math.ceil(len(products) / BATCH_SIZE)

    for i in range(num_batches):
        start = i * BATCH_SIZE
        end = start + BATCH_SIZE
        batch = products[start:end]
        batch_number = i + 1

        filename = batches_path / f"batch_{batch_number:03d}.md"
        content = generate_batch_prompt(batch_number, batch)

        filename.write_text(content, encoding="utf-8")
        print(f"📄 {filename.name}: {len(batch)} products (id {batch[0]['id']} ~ {batch[-1]['id']})")

    print(f"\n✅ Generated {num_batches} batch files in {BATCHES_DIR}/")
    print(f"   Total: {len(products)} products, {BATCH_SIZE} per batch")
    print(f"\n📋 Next steps:")
    print(f"   1. Open each batch file in {BATCHES_DIR}/")
    print(f"   2. Copy the content and paste into an Antigravity conversation")
    print(f"   3. Copy Antigravity's translation result")
    print(f"   4. Save it to {Path('data/results').as_posix()}/result_001.md (matching batch number)")
    print(f"   5. After all batches are done, run: python write_back.py")


if __name__ == "__main__":
    main()
