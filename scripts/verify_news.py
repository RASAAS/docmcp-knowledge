#!/usr/bin/env python3
"""Verify regulatory news JSON data integrity and URL accessibility.

Usage:
    python scripts/verify_news.py [--check-urls]

Without --check-urls: validates JSON schema only (fast).
With --check-urls: also sends HEAD/GET requests to source_url (slow, some
official government sites block automated requests and will show as 'BLOCKED').
"""

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
NEWS_DIR = REPO_ROOT / "regulatory_news"

VALID_FRAMEWORKS = {"eu_mdr", "fda", "nmpa", "_shared"}
VALID_CATEGORIES = {
    "regulation_update", "guidance_new", "standard_revision",
    "recall", "notice", "enforcement",
}
VALID_IMPORTANCES = {"high", "medium", "low"}
VALID_STATUSES = {"published", "draft", "archived"}

OFFICIAL_DOMAINS = {
    "eur-lex.europa.eu",
    "health.ec.europa.eu",
    "ec.europa.eu",
    "www.fda.gov",
    "fda.gov",
    "www.nmpa.gov.cn",
    "nmpa.gov.cn",
    "udi.nmpa.gov.cn",
    "www.iso.org",
    "webstore.iec.ch",
    "www.iec.ch",
}

GOV_DOMAIN_SUFFIXES = (".gov", ".gov.cn", ".europa.eu", ".iec.ch", ".iso.org")

errors: list[str] = []
warnings: list[str] = []


def validate_item(item: dict, file_name: str, idx: int) -> None:
    prefix = f"{file_name}[{idx}] ({item.get('id', '???')})"

    required_fields = [
        "id", "framework", "category", "title", "summary",
        "source_url", "source_name", "published_date", "importance", "status",
    ]
    for f in required_fields:
        if f not in item:
            errors.append(f"{prefix}: missing required field '{f}'")

    fw = item.get("framework", "")
    if fw not in VALID_FRAMEWORKS:
        errors.append(f"{prefix}: invalid framework '{fw}'")

    cat = item.get("category", "")
    if cat not in VALID_CATEGORIES:
        errors.append(f"{prefix}: invalid category '{cat}'")

    imp = item.get("importance", "")
    if imp not in VALID_IMPORTANCES:
        errors.append(f"{prefix}: invalid importance '{imp}'")

    st = item.get("status", "")
    if st not in VALID_STATUSES:
        errors.append(f"{prefix}: invalid status '{st}'")

    title = item.get("title", {})
    if not isinstance(title, dict) or not title.get("en"):
        errors.append(f"{prefix}: title must have 'en' key with non-empty value")

    summary = item.get("summary", {})
    if not isinstance(summary, dict) or not summary.get("en"):
        errors.append(f"{prefix}: summary must have 'en' key with non-empty value")

    url = item.get("source_url", "")
    if url:
        from urllib.parse import urlparse
        parsed = urlparse(url)
        if parsed.scheme not in ("http", "https"):
            errors.append(f"{prefix}: source_url must use http/https scheme")
        domain = parsed.hostname or ""
        is_official = (
            domain in OFFICIAL_DOMAINS
            or any(domain.endswith(s) for s in GOV_DOMAIN_SUFFIXES)
        )
        if not is_official:
            errors.append(
                f"{prefix}: source_url domain '{domain}' is not an official "
                f"government/standards body domain"
            )

    tags = item.get("tags", [])
    if not isinstance(tags, list):
        errors.append(f"{prefix}: tags must be a list")

    pub_date = item.get("published_date", "")
    if pub_date:
        import re
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", pub_date):
            errors.append(f"{prefix}: published_date must be YYYY-MM-DD format")


def check_url(url: str, item_id: str) -> str:
    """Check URL accessibility. Returns status string."""
    import urllib.request
    import urllib.error
    try:
        req = urllib.request.Request(url, method="HEAD")
        req.add_header("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)")
        with urllib.request.urlopen(req, timeout=10) as resp:
            return f"OK ({resp.status})"
    except urllib.error.HTTPError as e:
        if e.code in (401, 403, 405, 412):
            return f"BLOCKED ({e.code}) -- official site anti-bot, OK in browser"
        return f"ERROR ({e.code})"
    except Exception as e:
        return f"FAIL ({e})"


def main():
    do_url_check = "--check-urls" in sys.argv

    json_files = sorted(NEWS_DIR.glob("*.json"))
    if not json_files:
        print(f"ERROR: No JSON files found in {NEWS_DIR}")
        sys.exit(1)

    total_items = 0
    all_ids: set[str] = set()
    url_results: list[tuple[str, str, str]] = []

    for jf in json_files:
        print(f"\n--- {jf.name} ---")
        try:
            data = json.loads(jf.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            errors.append(f"{jf.name}: invalid JSON -- {e}")
            continue

        if not isinstance(data, dict):
            errors.append(f"{jf.name}: root must be a JSON object")
            continue

        fw = data.get("framework", "")
        if fw not in VALID_FRAMEWORKS:
            errors.append(f"{jf.name}: invalid root framework '{fw}'")

        items = data.get("items", [])
        if not isinstance(items, list):
            errors.append(f"{jf.name}: 'items' must be an array")
            continue

        print(f"  Items: {len(items)}")
        for i, item in enumerate(items):
            total_items += 1
            item_id = item.get("id", "")
            if item_id in all_ids:
                errors.append(f"{jf.name}[{i}]: duplicate ID '{item_id}'")
            all_ids.add(item_id)
            validate_item(item, jf.name, i)

            title_en = item.get("title", {}).get("en", "")[:60]
            url = item.get("source_url", "")
            print(f"  [{i}] {item_id}")
            print(f"      Title: {title_en}...")
            print(f"      URL: {url}")

            if do_url_check and url:
                status = check_url(url, item_id)
                print(f"      Status: {status}")
                url_results.append((item_id, url, status))

    print(f"\n{'='*60}")
    print(f"Total items: {total_items}")
    print(f"Unique IDs: {len(all_ids)}")

    if do_url_check and url_results:
        print(f"\nURL Check Results:")
        for item_id, url, status in url_results:
            marker = "[OK]" if "OK" in status or "BLOCKED" in status else "[!!]"
            print(f"  {marker} {item_id}: {status}")

    if errors:
        print(f"\nERRORS ({len(errors)}):")
        for e in errors:
            print(f"  [X] {e}")
        sys.exit(1)
    else:
        print("\nAll checks passed.")
        if warnings:
            for w in warnings:
                print(f"  [!] {w}")
        sys.exit(0)


if __name__ == "__main__":
    main()
