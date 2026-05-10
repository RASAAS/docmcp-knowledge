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
    python scripts/fetch_nifdc_standards.py --fetch        # crawl + write
    python scripts/fetch_nifdc_standards.py --dry-run      # crawl, print summary, no write
    python scripts/fetch_nifdc_standards.py --max-pages 5  # limit pages for testing

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
DEFAULT_TIMEOUT = 20
DEFAULT_PAGE_SIZE = 100  # NIFDC default
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
    """
    Parse one listing page. Returns (rows, page_info).
    page_info contains best-effort total/page hints when available.
    """
    soup = BeautifulSoup(html, "html.parser")
    rows: list[dict] = []
    # The data table is a <table> immediately containing rows starting at index >= 1.
    for table in soup.find_all("table"):
        head_cells = [c.get_text(strip=True) for c in table.find_all("th")]
        if not head_cells:
            # Fallback: detect by first row containing 标准编号
            first_tr = table.find("tr")
            if not first_tr:
                continue
            head_cells = [c.get_text(strip=True) for c in first_tr.find_all(["td", "th"])]
        if not any("标准编号" in h for h in head_cells):
            continue

        for tr in table.find_all("tr"):
            tds = tr.find_all("td")
            if len(tds) < 8:
                continue
            cells = [td.get_text(strip=True) for td in tds]
            # Layout (verified 2026-05-10):
            #   [seq, dir_name, l1, l2, std_number, std_title, approval, effective, status, action]
            # Some rows have 9 columns when "操作" is omitted.
            if not re.match(r"^\d+$", cells[0]):
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
        break

    # Pagination text -- best-effort; NIFDC shows e.g. "共 1234 条/12 页".
    page_info: dict = {}
    text_blob = soup.get_text(" ")
    m = re.search(r"\u5171\s*(\d+)\s*\u6761", text_blob)
    if m:
        page_info["total_records"] = int(m.group(1))
    m2 = re.search(r"\u5171\s*\d+\s*\u6761\s*/\s*(\d+)\s*\u9875", text_blob)
    if m2:
        page_info["total_pages"] = int(m2.group(1))
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
    session = _make_session()
    all_rows: list[dict] = []
    seen_keys: set[str] = set()
    page = 1
    total_pages: Optional[int] = None
    total_records: Optional[int] = None
    while True:
        if max_pages and page > max_pages:
            break
        params = {"pageNum": page, "pageSize": DEFAULT_PAGE_SIZE, "status": ""}
        r = _request_with_retry(session, "GET", LIST_URL, params=params)
        if r is None:
            print(f"[error] page {page} failed all retries; stopping.")
            break
        if r.status_code != 200:
            print(f"[error] page {page} HTTP {r.status_code}; stopping.")
            break
        rows, info = _parse_listing_page(r.text)
        if total_pages is None and info.get("total_pages"):
            total_pages = info["total_pages"]
        if total_records is None and info.get("total_records"):
            total_records = info["total_records"]
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
        if not rows:
            break
        if total_pages and page >= total_pages:
            break
        page += 1
        time.sleep(SLEEP_BETWEEN)
    return all_rows, {
        "fetched_at": datetime.utcnow().isoformat() + "Z",
        "page_count": page,
        "total_records_hint": total_records,
        "total_pages_hint": total_pages,
        "rows_collected": len(all_rows),
        "source": LIST_URL,
        "note": "metadata-only crawl per project decision 2026-05-10",
    }


def filter_active_only(rows: list[dict]) -> list[dict]:
    return [r for r in rows if r.get("status") in ("active", "upcoming")]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fetch", action="store_true", help="Crawl and write JSON outputs")
    ap.add_argument("--dry-run", action="store_true", help="Crawl but do not write")
    ap.add_argument("--max-pages", type=int, default=None, help="Limit pages (for testing)")
    ap.add_argument("--include-other", action="store_true", help="Include non-active standards")
    args = ap.parse_args()

    if not (args.fetch or args.dry_run):
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
