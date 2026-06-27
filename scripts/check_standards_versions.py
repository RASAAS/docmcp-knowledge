#!/usr/bin/env python3
"""
Precise Standards Version Monitor (Issue #52)

Directly fetches official standard body pages and checks for newer versions.
No search engine dependency -- reads page content for authoritative signals.

Detection signals:
  - ISO: "This standard has been revised by" or "Revised by" link
  - IEC: "A more recent version of this publication exists"
  - ASTM: "Withdrawn" status or "Historical" label
  - iTeh (EN): Status shows "Withdrawn" or has successor

Usage:
    python scripts/check_standards_versions.py                    # Full scan
    python scripts/check_standards_versions.py --source iso       # ISO only
    python scripts/check_standards_versions.py --source iec       # IEC only
    python scripts/check_standards_versions.py --source other     # ASTM/EN/etc
    python scripts/check_standards_versions.py --category sterilization  # One category
    python scripts/check_standards_versions.py --report /tmp/report.json
"""

import argparse
import json
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).parent.parent
STANDARDS_DIR = ROOT / "eu_mdr" / "other_standards"
REPORT_PATH = ROOT / "scripts" / "standards_update_report.json"

HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; DocMCP-Monitor/1.0)"}
FETCH_DELAY = 0.5  # seconds between requests


def load_all_standards() -> list[dict]:
    """Load all standards from JSON files with their category."""
    items = []
    for jf in sorted(STANDARDS_DIR.glob("standards-*.json")):
        cat = jf.stem.replace("standards-", "")
        data = json.loads(jf.read_text(encoding="utf-8"))
        for s in data["standards"]:
            url = s.get("source_url", "")
            if not url:
                continue
            source_type = classify_source(url)
            items.append({
                "category": cat,
                "number": s["number"],
                "id": s.get("id", ""),
                "name": s.get("name", ""),
                "url": url,
                "source_type": source_type,
            })
    return items


def classify_source(url: str) -> str:
    if "iso.org" in url:
        return "iso"
    elif "webstore.iec.ch" in url:
        return "iec"
    elif "astm.org" in url or "store.astm.org" in url:
        return "astm"
    elif "standards.iteh.ai" in url:
        return "iteh"
    elif "eur-lex.europa.eu" in url:
        return "eurlex"
    elif "aami.org" in url:
        return "aami"
    elif "bsigroup.com" in url:
        return "bsi"
    else:
        return "other"


def fetch_page(url: str, max_bytes: int = 8000) -> tuple[int, str]:
    """Fetch page content. Returns (status_code, html_text)."""
    try:
        req = Request(url, headers=HEADERS)
        resp = urlopen(req, timeout=15)
        content = resp.read(max_bytes).decode("utf-8", errors="ignore")
        return resp.status, content
    except HTTPError as e:
        return e.code, ""
    except (URLError, OSError) as e:
        return 0, str(e)


def check_iso(standard: dict) -> dict | None:
    """Check ISO page for revision signals.
    
    ISO marks old standard pages with 'Withdrawn' status and 'Revised by' links.
    The lifecycle section is deep (50-80KB). Key insight for distinguishing current vs
    withdrawn: on a withdrawn standard's page, "Withdrawn" appears BEFORE "Published"
    in the HTML. On current standards, "Published" appears first (and "Withdrawn" may
    appear later in the lifecycle history section referring to the OLD version).
    """
    status, html = fetch_page(standard["url"], max_bytes=80000)
    if status != 200:
        return {"type": "error", "detail": f"HTTP {status}"}

    # Find positions of first "Published" and first "Withdrawn"
    pub_idx = html.find("Published")
    withdrawn_idx = html.find("Withdrawn")

    # If "Withdrawn" not found at all, standard is current
    if withdrawn_idx < 0:
        return None

    # If "Published" not found but "Withdrawn" is found, it's withdrawn
    # If "Withdrawn" appears BEFORE "Published", the standard itself is withdrawn
    is_withdrawn = (pub_idx < 0) or (withdrawn_idx < pub_idx)

    if not is_withdrawn:
        # "Published" comes first -> standard is current, "Withdrawn" is about old versions
        return None

    # Standard is genuinely withdrawn. Try to find what replaced it.
    revised_match = re.search(
        r"Revised by.*?(?:href=\"([^\"]+)\").*?(ISO[/ ][\w\-]+:\d{4})",
        html, re.IGNORECASE | re.DOTALL
    )
    if revised_match:
        new_std = revised_match.group(2)
        href = revised_match.group(1)
        new_url = f"https://www.iso.org{href}" if href.startswith("/") else href
        return {
            "type": "revised",
            "signal": f"Revised by {new_std}",
            "new_version": new_std,
            "new_url": new_url,
        }

    return {"type": "withdrawn", "signal": "Status: Withdrawn (no replacement found in page)"}


def check_iec(standard: dict) -> dict | None:
    """Check IEC webstore page for newer version signal.
    
    IEC webstore does NOT mark old publication pages as superseded.
    Detection strategy:
    1. Check for explicit "more recent version" text (rare but possible)
    2. Compare page title year against our stored version year
    3. Check for "Withdrawn" status
    """
    status, html = fetch_page(standard["url"], max_bytes=15000)
    if status != 200:
        return {"type": "error", "detail": f"HTTP {status}"}

    # Signal 1: "A more recent version of this publication exists"
    if "more recent version" in html.lower():
        newer_match = re.search(
            r"more recent version.*?:\s*(IEC[^<\"]+)",
            html, re.IGNORECASE | re.DOTALL
        )
        new_ver = newer_match.group(1).strip() if newer_match else "unknown"
        link_match = re.search(
            r'more recent version.*?href="(/en/publication/\d+)"',
            html, re.IGNORECASE | re.DOTALL
        )
        new_url = f"https://webstore.iec.ch{link_match.group(1)}" if link_match else ""
        return {
            "type": "newer_version",
            "signal": f"A more recent version exists: {new_ver}",
            "new_version": new_ver,
            "new_url": new_url,
        }

    # Signal 2: Page title contains a DIFFERENT year than our stored version
    # e.g. our data says "IEC 60068-2-78:2012" but page title says "IEC 60068-2-78:2025"
    title_match = re.search(r'<title>([^<]+)</title>', html)
    if title_match:
        page_title = title_match.group(1)
        # Extract year from page title
        page_year_match = re.search(r':(\d{4})', page_title)
        our_year_match = re.search(r':(\d{4})', standard["number"])
        if page_year_match and our_year_match:
            page_year = int(page_year_match.group(1))
            our_year = int(our_year_match.group(1))
            if page_year > our_year:
                return {
                    "type": "newer_version",
                    "signal": f"Page shows {page_title.strip()} but we have {standard['number']}",
                    "new_version": page_title.strip().replace(" | IEC", ""),
                }

    # Signal 3: "Withdrawn" status
    if re.search(r"status.*?withdrawn", html, re.IGNORECASE):
        return {"type": "withdrawn", "signal": "Status: Withdrawn"}

    return None


def check_astm(standard: dict) -> dict | None:
    """Check ASTM page for withdrawal/historical status."""
    status, html = fetch_page(standard["url"])
    if status == 404:
        return {"type": "error", "detail": "HTTP 404 - page not found"}
    if status != 200:
        return {"type": "error", "detail": f"HTTP {status}"}

    # Signal: "Historical" or "Withdrawn" in status
    if re.search(r"\bHistorical\b", html):
        superseded = re.search(r"Superseded\s*(?:by)?\s*([A-Z]\d[\w\-]+)", html)
        return {
            "type": "withdrawn",
            "signal": f"Historical/Withdrawn. {superseded.group(0) if superseded else ''}".strip(),
            "new_version": superseded.group(1) if superseded else "",
        }

    if re.search(r"\bWithdrawn\b", html, re.IGNORECASE):
        return {"type": "withdrawn", "signal": "Withdrawn"}

    return None


def check_iteh(standard: dict) -> dict | None:
    """Check iTeh/CEN page for withdrawn status."""
    status, html = fetch_page(standard["url"])
    if status == 404:
        return {"type": "error", "detail": "HTTP 404 - page removed or URL changed"}
    if status != 200:
        return {"type": "error", "detail": f"HTTP {status}"}

    # Signal: Status "Withdrawn"
    if re.search(r"Status\s*Withdrawn", html, re.IGNORECASE):
        replaced = re.search(r"Replaced by\s*([^<\n]+)", html)
        return {
            "type": "withdrawn",
            "signal": f"Withdrawn. {replaced.group(0) if replaced else ''}".strip(),
            "new_version": replaced.group(1).strip() if replaced else "",
        }

    return None


CHECKERS = {
    "iso": check_iso,
    "iec": check_iec,
    "astm": check_astm,
    "iteh": check_iteh,
}


def run_check(
    source_filter: str | None = None,
    category_filter: str | None = None,
    report_path: str | None = None,
) -> dict:
    """Run version checks and return report."""
    standards = load_all_standards()

    if source_filter:
        standards = [s for s in standards if s["source_type"] == source_filter]
    if category_filter:
        standards = [s for s in standards if s["category"] == category_filter]

    # Skip sources without checkers (eurlex, aami, bsi, other)
    checkable = [s for s in standards if s["source_type"] in CHECKERS]
    skipped = [s for s in standards if s["source_type"] not in CHECKERS]

    print(f"Standards to check: {len(checkable)} (skipping {len(skipped)} without checker)")
    print(f"  ISO: {sum(1 for s in checkable if s['source_type'] == 'iso')}")
    print(f"  IEC: {sum(1 for s in checkable if s['source_type'] == 'iec')}")
    print(f"  ASTM: {sum(1 for s in checkable if s['source_type'] == 'astm')}")
    print(f"  iTeh: {sum(1 for s in checkable if s['source_type'] == 'iteh')}")
    print()

    updates = []
    errors = []
    checked = 0

    for i, std in enumerate(checkable):
        checker = CHECKERS[std["source_type"]]
        result = checker(std)
        checked += 1

        if result:
            if result["type"] == "error":
                errors.append({**std, "error": result["detail"]})
                print(f"  [{i+1}/{len(checkable)}] ERROR {std['number']}: {result['detail']}")
            else:
                updates.append({
                    "category": std["category"],
                    "number": std["number"],
                    "current_url": std["url"],
                    "signal": result.get("signal", ""),
                    "new_version": result.get("new_version", ""),
                    "new_url": result.get("new_url", ""),
                    "action_required": result["type"],
                })
                print(f"  [{i+1}/{len(checkable)}] UPDATE {std['number']}: {result['signal']}")
        else:
            if (i + 1) % 20 == 0:
                print(f"  [{i+1}/{len(checkable)}] ... {std['number']} OK")

        time.sleep(FETCH_DELAY)

    report = {
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "total_standards": len(standards),
        "total_checked": checked,
        "total_skipped": len(skipped),
        "updates_detected": len(updates),
        "errors_count": len(errors),
        "updates": updates,
        "errors": errors,
        "summary": (
            f"{len(updates)} updates detected, "
            f"{checked - len(updates) - len(errors)} standards current, "
            f"{len(errors)} fetch errors"
        ),
    }

    out_path = Path(report_path) if report_path else REPORT_PATH
    out_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    print(f"\nReport saved to: {out_path}")
    print(f"Summary: {report['summary']}")

    return report


def main():
    parser = argparse.ArgumentParser(description="Check standards for version updates")
    parser.add_argument("--source", choices=["iso", "iec", "astm", "iteh", "all"],
                        default="all", help="Filter by source type")
    parser.add_argument("--category", type=str, help="Filter by category name")
    parser.add_argument("--report", type=str, help="Output report JSON path")
    args = parser.parse_args()

    source = None if args.source == "all" else args.source
    run_check(source_filter=source, category_filter=args.category, report_path=args.report)


if __name__ == "__main__":
    main()
