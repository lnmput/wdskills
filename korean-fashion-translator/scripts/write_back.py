#!/usr/bin/env python3
"""
write_back.py — Parse Antigravity translation results and write them back via API.

Usage:
    python write_back.py              # Write back all results
    python write_back.py --dry-run    # Preview without writing

Input:
    data/results/result_001.md, result_002.md, ...
    Each file should contain Antigravity's markdown table output.

Output:
    PUT /api/products/:id for each translated product.
"""

import json
import re
import sys
import os
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

from config import API_BASE_URL, API_TOKEN, RESULTS_DIR


def parse_result_file(filepath: Path) -> list[dict]:
    """
    Parse a markdown result file and extract translation rows.

    Expected table format:
    | id | source_lang | title_optimized | title_ko | status | review_flag |
    """
    content = filepath.read_text(encoding="utf-8")
    rows = []

    # Find all table rows (lines starting with |, excluding header and separator)
    table_lines = []
    in_table = False

    for line in content.split("\n"):
        stripped = line.strip()
        if not stripped.startswith("|"):
            if in_table:
                in_table = False  # End of table
            continue

        # Skip separator lines like |----|----|
        if re.match(r"^\|[\s\-:|]+\|$", stripped):
            in_table = True
            continue

        # Skip header line (contains "id" and "title_ko")
        if "title_ko" in stripped and "id" in stripped:
            in_table = True
            continue

        if in_table or "title_ko" not in stripped:
            # Only process if we've seen a header
            cells = [c.strip() for c in stripped.split("|")]
            # Remove empty first/last elements from split
            cells = [c for c in cells if c != "" or cells.index(c) not in (0, len(cells) - 1)]
            # Filter out truly empty boundary cells
            while cells and cells[0] == "":
                cells.pop(0)
            while cells and cells[-1] == "":
                cells.pop()

            if len(cells) >= 4:
                table_lines.append(cells)

    # Parse collected table lines
    for cells in table_lines:
        try:
            product_id = cells[0].strip()
            # Try to parse as integer
            try:
                product_id = int(product_id)
            except ValueError:
                continue  # Skip non-numeric IDs (likely header)

            row = {
                "id": product_id,
                "source_lang": cells[1].strip() if len(cells) > 1 else "",
                "title_optimized": cells[2].strip() if len(cells) > 2 else "",
                "title_ko": cells[3].strip() if len(cells) > 3 else "",
                "status": cells[4].strip() if len(cells) > 4 else "done",
                "review_flag": cells[5].strip() if len(cells) > 5 else "",
            }

            # Clean up review_flag
            if not row["review_flag"] or row["review_flag"] in ("-", "—", "null", "None"):
                row["review_flag"] = None

            # Clean up status
            if not row["status"] or row["status"] in ("-", "—"):
                row["status"] = "done"

            # Clean up title_ko: remove backticks if present
            row["title_ko"] = row["title_ko"].strip("`")

            # Detect needs_review from flag or title
            if row["review_flag"] or "확인필요" in row.get("title_ko", ""):
                row["status"] = "needs_review"
                # Extract flag from title_ko if embedded
                flag_match = re.search(r"\[⚠️\s*확인필요[^\]]*\]", row["title_ko"])
                if flag_match and not row["review_flag"]:
                    row["review_flag"] = flag_match.group(0)
                    # Remove flag from title_ko
                    row["title_ko"] = row["title_ko"].replace(flag_match.group(0), "").strip()

            if row["title_ko"]:  # Only include rows with actual translations
                rows.append(row)

        except (IndexError, ValueError) as e:
            print(f"   ⚠️  Skipping malformed row in {filepath.name}: {cells} ({e})")
            continue

    return rows


def write_product(product: dict) -> bool:
    """Write a single product translation back via API."""
    url = f"{API_BASE_URL}/products/{product['id']}"
    body = {
        "title_ko": product["title_ko"],
        "title_optimized": product["title_optimized"],
        "translation_status": product["status"],
        "review_flag": product["review_flag"],
    }

    data = json.dumps(body).encode("utf-8")
    req = Request(url, data=data, method="PUT")
    req.add_header("Authorization", f"Bearer {API_TOKEN}")
    req.add_header("Content-Type", "application/json")

    try:
        with urlopen(req) as resp:
            return resp.status in (200, 201, 204)
    except HTTPError as e:
        print(f"   ❌ API error for product {product['id']}: {e.code} {e.reason}")
        return False
    except URLError as e:
        print(f"   ❌ Connection error for product {product['id']}: {e.reason}")
        return False


def main():
    dry_run = "--dry-run" in sys.argv

    results_path = Path(RESULTS_DIR)
    if not results_path.exists():
        print(f"❌ Results directory not found: {RESULTS_DIR}")
        print(f"   Create it and add result files: result_001.md, result_002.md, ...")
        sys.exit(1)

    result_files = sorted(results_path.glob("result_*.md"))
    if not result_files:
        print(f"❌ No result files found in {RESULTS_DIR}/")
        print(f"   Expected files like: result_001.md, result_002.md, ...")
        sys.exit(1)

    # Parse all result files
    all_rows = []
    for f in result_files:
        rows = parse_result_file(f)
        print(f"📄 {f.name}: parsed {len(rows)} translations")
        all_rows.extend(rows)

    if not all_rows:
        print("\n❌ No valid translation rows found in result files.")
        print("   Make sure the files contain markdown tables with the expected columns.")
        sys.exit(1)

    # Summary before writing
    done_count = sum(1 for r in all_rows if r["status"] == "done")
    review_count = sum(1 for r in all_rows if r["status"] == "needs_review")

    print(f"\n📊 Parsed {len(all_rows)} translations:")
    print(f"   ✅ done: {done_count}")
    print(f"   ⚠️  needs_review: {review_count}")

    if dry_run:
        print(f"\n🔍 Dry run mode — showing first 5 rows:\n")
        for row in all_rows[:5]:
            flag = f" {row['review_flag']}" if row["review_flag"] else ""
            print(f"   [{row['status']}] id={row['id']}: {row['title_ko']}{flag}")
        print(f"\n   ... and {len(all_rows) - min(5, len(all_rows))} more")
        print(f"\n   To write back, run: python write_back.py")
        return

    # Write back via API
    print(f"\n🚀 Writing back {len(all_rows)} translations via API...")

    success = 0
    failed = 0
    for i, row in enumerate(all_rows, 1):
        ok = write_product(row)
        if ok:
            success += 1
        else:
            failed += 1

        # Progress every 50 items
        if i % 50 == 0 or i == len(all_rows):
            print(f"   Progress: {i}/{len(all_rows)} ({success} ✅, {failed} ❌)")

    # Final summary
    print(f"\n{'=' * 50}")
    print(f"✅ Successfully written: {success}")
    print(f"⚠️  Needs review: {review_count}")
    print(f"❌ Failed: {failed}")
    if failed > 0:
        print(f"\n   Failed products need manual handling.")
    if review_count > 0:
        print(f"\n   ⚠️  {review_count} products have ambiguity flags.")
        print(f"   Review them in your database where translation_status = 'needs_review'.")


if __name__ == "__main__":
    main()
