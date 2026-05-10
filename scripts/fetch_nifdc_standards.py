#!/usr/bin/env python3
"""
Fetch NMPA medical device standard *metadata only* from NIFDC public listing.

Source page (ASP .do query endpoint, paginated server-side):
    https://app.nifdc.org.cn/biaogzx/qxqwk.do

We only collect the metadata visible on the listing table (no full text):
    标准编号 (number), 标准名称 (title_zh), 一级目录, 二级目录,
    批准日期 (approval_date), 实施日期 (effective_date), 实施状态 (status).

Decision (2026-05-10): full-text PDFs are NOT crawled. Standards full text
must be uploaded by users when needed for V&V. We retain only metadata so
the plugin's standards browser can offer up-to-date searchable references
to *active* GB / YY standards, with a click-through link back to the
official NIFDC listing.

Output:
    docmcp-knowledge/nmpa/standards/master/standards.json  (one big array)
    docmcp-knowledge/nmpa/standards/master/meta.json       (run metadata)

Usage:
    python scripts/fetch_nifdc_standards.py --fetch           # full crawl + overwrite
    python scripts/fetch_nifdc_standards.py --incremental     # crawl + diff + merge-write
    python scripts/fetch_nifdc_standards.py --diff-only       # crawl + diff report only (no write)
    python scripts/fetch_nifdc_standards.py --dry-run         # crawl, print summary, no write
    python scripts/fetch_nifdc_standards.py --max-pages 5     # limit pages for testing

This script is **not** wired into CI. Run it locally when refreshing the
standards index. Be respectful: 0.5-1s sleep between requests, retry on
transient errors. The NIFDC site is a public service of the China Institute
for Food and Drug Control; do not hammer it.
"""

import argparse
import json
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Optional

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("ERROR: beautifulsoup4 not installed. Run: pip install beautifulsoup4")
    sys.exit(1)

try:
    import requests
except ImportError:
    print("ERROR: requests not installed. Run: pip install requests")
    sys.exit(1)


ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "nmpa" / "standards" / "master"
OUT_DIR.mkdir(parents=True, exist_ok=True)

LIST_URL = "https://app.nifdc.org.cn/biaogzx/qxqwk.do"
LIST_ACTION_URL = LIST_URL + "?formAction=list"
DEFAULT_TIMEOUT = 20
SLEEP_BETWEEN = 0.6  # seconds
MAX_RETRIES = 3
USER_AGENT = (
    "ReguverseStandardsBot/1.0 (+https://reguverse.com; metadata-only collection)"
)


def _make_session() -> requests.Session:
    s = requests.Session()
    s.headers.update(
        {
            "User-Agent": USER_AGENT,
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        }
    )
    return s


def _request_with_retry(
    session: requests.Session,
    method: str,
    url: str,
    *,
    params=None,
    data=None,
    timeout: int = DEFAULT_TIMEOUT,
) -> Optional[requests.Response]:
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            r = session.request(method, url, params=params, data=data, timeout=timeout)
            if r.status_code >= 500:
                raise requests.HTTPError(f"{r.status_code}")
            return r
        except (requests.RequestException, requests.HTTPError) as exc:
            print(f"[warn] {method} {url} attempt {attempt}/{MAX_RETRIES}: {exc}", flush=True)
            time.sleep(min(2 ** attempt, 10))
    return None


def _parse_listing_page(html: str) -> tuple[list[dict], dict]:
    """Parse one listing page. Returns (rows, page_info).

    The NIFDC page structures data across **multiple** ``<table>`` elements,
    one per classification sub-directory. We iterate all tables and collect
    every data row that matches the expected column layout.
    """
    soup = BeautifulSoup(html, "html.parser")
    rows: list[dict] = []
    for table in soup.find_all("table"):
        for tr in table.find_all("tr"):
            tds = tr.find_all("td")
            if len(tds) < 8:
                continue
            cells = [td.get_text(strip=True) for td in tds]
            if not re.match(r"^\d+$", cells[0]):
                continue
            # Guard: cells[4] must look like a standard number (GB/YY/...)
            if not re.match(r"^[A-Za-z]", cells[4]):
                continue
            try:
                row = {
                    "seq": int(cells[0]),
                    "dir_name": cells[1],
                    "l1": cells[2],
                    "l2": cells[3],
                    "number": cells[4],
                    "title_zh": cells[5],
                    "approval_date": cells[6] if len(cells) > 6 else "",
                    "effective_date": cells[7] if len(cells) > 7 else "",
                    "status_zh": cells[8] if len(cells) > 8 else "",
                }
            except Exception:
                continue
            rows.append(row)
    page_info: dict = {}
    return rows, page_info


def _normalize_status(status_zh: str) -> str:
    """Map Chinese status labels to canonical English flags.

    现行 -> active
    即将实施 -> upcoming (still active)
    其它 -> other
    """
    if not status_zh:
        return "unknown"
    if "现行" in status_zh:
        return "active"
    if "即将" in status_zh or "实施" in status_zh:
        return "upcoming"
    return "other"


def _stable_id(number: str) -> str:
    base = number.lower().strip().replace(" ", "-").replace("/", "-")
    return f"nmpa-{re.sub(r'[^a-z0-9.-]+', '-', base)}"


def fetch_all(max_pages: Optional[int] = None) -> tuple[list[dict], dict]:
    """Paginate the full standards list (general + professional domains).

    NIFDC ``qxqwk.do`` lists only 228 general-domain standards by default. To
    fetch ALL 2100+ standards (including the professional/specialized domain),
    we use the ``istiaojian`` query parameter -- any non-empty value triggers
    the full-catalog pagination. Each page returns up to ~300 rows (from
    multiple ``<table>`` elements). We paginate with ``index=N`` in the URL.

    Stops when two consecutive pages yield zero new (de-duped) rows.
    """
    session = _make_session()
    # Warm up session cookies
    _request_with_retry(session, "GET", LIST_URL)
    all_rows: list[dict] = []
    seen_keys: set[str] = set()
    page = 1
    consecutive_empty = 0
    while True:
        if max_pages and page > max_pages:
            break
        url = f"{LIST_ACTION_URL}&istiaojian=all&index={page}"
        r = _request_with_retry(session, "GET", url)
        if r is None:
            print(f"[error] page {page} failed all retries; stopping.")
            break
        if r.status_code != 200:
            print(f"[error] page {page} HTTP {r.status_code}; stopping.")
            break
        rows, _info = _parse_listing_page(r.text)
        new_count = 0
        for row in rows:
            key = row["number"]
            if key in seen_keys:
                continue
            seen_keys.add(key)
            row["status"] = _normalize_status(row.get("status_zh", ""))
            row["id"] = _stable_id(row["number"])
            row["source_url"] = LIST_URL
            all_rows.append(row)
            new_count += 1
        print(f"[info] page {page}: parsed {len(rows)} (new {new_count}; total {len(all_rows)})", flush=True)
        if new_count == 0:
            consecutive_empty += 1
            if consecutive_empty >= 2:
                break
        else:
            consecutive_empty = 0
        if not rows:
            break
        page += 1
        time.sleep(SLEEP_BETWEEN)
    return all_rows, {
        "fetched_at": datetime.utcnow().isoformat() + "Z",
        "page_count": page,
        "rows_collected": len(all_rows),
        "source": LIST_URL,
        "note": "metadata-only crawl (general + professional domains) per project decision 2026-05-10",
    }


def filter_active_only(rows: list[dict]) -> list[dict]:
    return [r for r in rows if r.get("status") in ("active", "upcoming")]


def _load_existing() -> dict[str, dict]:
    """Load existing standards.json into a dict keyed by standard number."""
    out_path = OUT_DIR / "standards.json"
    if not out_path.exists():
        return {}
    try:
        with open(out_path, "r", encoding="utf-8") as f:
            items = json.load(f)
        return {r["number"]: r for r in items if isinstance(r, dict) and "number" in r}
    except Exception as e:
        print(f"[warn] could not load existing standards.json: {e}")
        return {}


def _compute_diff(existing: dict[str, dict], fetched: list[dict]) -> dict:
    """Compare fetched data with existing and return a diff report."""
    fetched_map = {r["number"]: r for r in fetched}
    existing_nums = set(existing.keys())
    fetched_nums = set(fetched_map.keys())

    added = sorted(fetched_nums - existing_nums)
    removed = sorted(existing_nums - fetched_nums)

    changed: list[dict] = []
    for num in sorted(existing_nums & fetched_nums):
        old, new = existing[num], fetched_map[num]
        diffs = {}
        for field in ("title_zh", "status", "status_zh", "effective_date", "approval_date"):
            ov, nv = old.get(field, ""), new.get(field, "")
            if ov != nv:
                diffs[field] = {"old": ov, "new": nv}
        if diffs:
            changed.append({"number": num, "fields": diffs})

    return {
        "added_count": len(added),
        "removed_count": len(removed),
        "changed_count": len(changed),
        "added": added[:20],
        "removed": removed[:20],
        "changed": changed[:20],
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fetch", action="store_true", help="Crawl and write JSON outputs")
    ap.add_argument("--dry-run", action="store_true", help="Crawl but do not write")
    ap.add_argument("--incremental", action="store_true",
                     help="Crawl, compare with existing, show diff, and merge (new+changed)")
    ap.add_argument("--diff-only", action="store_true",
                     help="Like --incremental but only print diff report, no write")
    ap.add_argument("--max-pages", type=int, default=None, help="Limit pages (for testing)")
    ap.add_argument("--include-other", action="store_true", help="Include non-active standards")
    args = ap.parse_args()

    if not (args.fetch or args.dry_run or args.incremental or args.diff_only):
        ap.print_help()
        return 1

    rows, meta = fetch_all(max_pages=args.max_pages)
    if not args.include_other:
        rows = filter_active_only(rows)
        meta["filter"] = "active+upcoming only"

    print(f"\n[summary] collected {len(rows)} rows; pages={meta.get('page_count')}; total_pages={meta.get('total_pages_hint')}")

    if args.dry_run:
        print(json.dumps(rows[:3], ensure_ascii=False, indent=2))
        return 0

    if args.incremental or args.diff_only:
        existing = _load_existing()
        diff = _compute_diff(existing, rows)
        print(f"\n[diff] added={diff['added_count']}, removed={diff['removed_count']}, changed={diff['changed_count']}")
        if diff["added"]:
            print(f"  added (first 20): {diff['added']}")
        if diff["removed"]:
            print(f"  removed (first 20): {diff['removed']}")
        if diff["changed"]:
            for c in diff["changed"]:
                print(f"  changed: {c['number']} -> {c['fields']}")
        meta["mode"] = "incremental"
        meta["diff_summary"] = {
            "added": diff["added_count"],
            "removed": diff["removed_count"],
            "changed": diff["changed_count"],
        }
        if args.diff_only:
            return 0

    out_path = OUT_DIR / "standards.json"
    meta_path = OUT_DIR / "meta.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)
    print(f"[written] {out_path} ({out_path.stat().st_size} bytes)")
    print(f"[written] {meta_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
