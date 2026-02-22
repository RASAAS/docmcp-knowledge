#!/usr/bin/env python3
"""
URL Verification Script
Verifies that all source_url fields in content files are accessible.

Usage:
    python scripts/verify_urls.py --all
    python scripts/verify_urls.py --file nmpa/guidance/cmde-2022-9.zh.md
    python scripts/verify_urls.py --changed-only  # For CI: only check changed files
    python scripts/verify_urls.py --path nmpa/guidance
"""

import argparse
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Optional, Tuple, List
from urllib.parse import urlparse

try:
    import requests
except ImportError:
    print("ERROR: requests not installed. Run: pip install requests")
    sys.exit(1)

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml not installed. Run: pip install pyyaml")
    sys.exit(1)

ROOT = Path(__file__).parent.parent

# Official domains that are acceptable sources
OFFICIAL_DOMAINS = {
    # EU
    "eur-lex.europa.eu", "ec.europa.eu", "health.ec.europa.eu", "cen.eu", "team-nb.org",
    "www.team-nb.org",
    # FDA
    "fda.gov", "www.fda.gov", "accessdata.fda.gov", "www.accessdata.fda.gov",
    "ecfr.gov", "www.ecfr.gov", "federalregister.gov", "www.federalregister.gov",
    # NMPA
    "nmpa.gov.cn", "www.nmpa.gov.cn", "cmde.org.cn", "www.cmde.org.cn",
    "samr.gov.cn", "std.samr.gov.cn", "openstd.samr.gov.cn",
    # China government
    "gov.cn", "www.gov.cn",
    # Standards
    "iso.org", "www.iso.org", "iec.ch", "www.iec.ch",
    "sac.gov.cn", "www.sac.gov.cn",
    # GitHub (for repo links)
    "github.com",
    # WordPress source (reguverse.com - for migrated content)
    "reguverse.com", "www.reguverse.com",
}


def extract_front_matter(md_content: str) -> Optional[dict]:
    match = re.match(r"^---\n(.+?)\n---", md_content, re.DOTALL)
    if not match:
        return None
    try:
        return yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        return None


def get_changed_files() -> List[Path]:
    """Get list of changed .md files from git diff."""
    base_ref = os.environ.get("GITHUB_BASE_REF", "main")
    try:
        result = subprocess.run(
            ["git", "diff", "--name-only", f"origin/{base_ref}..."],
            capture_output=True, text=True, cwd=ROOT
        )
        files = []
        for line in result.stdout.strip().split("\n"):
            if line.endswith(".md") and line:
                f = ROOT / line
                if f.exists():
                    files.append(f)
        return files
    except Exception:
        return []


def _is_pdf_url(url: str) -> bool:
    """Heuristic: does this URL point to a PDF document?"""
    lower = url.lower()
    return (
        lower.endswith(".pdf")
        or "filename=" in lower and ".pdf" in lower
        or "/document/download/" in lower
        or "/system/files/" in lower and (".pdf" in lower or "filename" not in lower)
    )


def _validate_content(resp: "requests.Response", url: str) -> Tuple[Optional[bool], str]:
    """
    Validate that the response body looks like the expected content type.
    Returns (ok, message). ok=True means content looks correct.
    ok=None means uncertain (warn). ok=False means content is wrong (fail).
    """
    content_type = resp.headers.get("Content-Type", "").lower()
    content_length = resp.headers.get("Content-Length", "")

    if _is_pdf_url(url):
        # Expect PDF content
        if "application/pdf" in content_type:
            size_str = f" ({content_length} bytes)" if content_length else ""
            # Sanity check: a real PDF should be at least a few KB
            if content_length and int(content_length) < 1024:
                return False, f"PDF too small ({content_length} bytes) - likely an error page"
            return True, f"OK (PDF{size_str})"
        elif "text/html" in content_type:
            # Server returned HTML instead of PDF - likely an error or redirect to login
            return False, f"Expected PDF but got HTML - link may be broken or require auth"
        elif content_type == "" or "application/octet-stream" in content_type:
            # Unknown type - warn but don't fail
            return None, f"Content-Type unclear ({content_type or 'none'}), manual check recommended"
        elif any(x in content_type for x in [
            "officedocument", "ms-excel", "msword", "opendocument"
        ]):
            # Office documents (.docx, .xlsx, etc.) are valid downloadable files
            return None, f"Unexpected Content-Type: {content_type}"
        else:
            return None, f"Unexpected Content-Type: {content_type}"
    else:
        # For HTML pages, just check it's not an error page
        if "text/html" in content_type or content_type == "":
            return True, f"OK (HTML)"
        return True, f"OK ({content_type})"


def check_url(url: str, session: requests.Session, timeout: int = 15) -> Tuple[Optional[bool], str]:
    """
    Check if a URL is accessible and its content is valid.
    Returns (ok, status_message).
    ok=True: accessible and content looks correct
    ok=None: accessible but uncertain (warn)
    ok=False: broken
    """
    if not url or url.startswith("#"):
        return False, "empty or anchor URL"

    parsed = urlparse(url)
    if not parsed.scheme in ("http", "https"):
        return False, f"invalid scheme: {parsed.scheme}"

    # Check domain is official
    domain = parsed.netloc.lower()
    if domain not in OFFICIAL_DOMAINS:
        return None, f"non-official domain: {domain} (manual review needed)"

    # Determine if we need a full GET for content validation
    needs_content_check = _is_pdf_url(url)
    force_get_domains = {"www.fda.gov", "fda.gov"}

    try:
        if needs_content_check or domain in force_get_domains:
            # Use GET with streaming to read headers without downloading full body
            resp = session.get(url, timeout=timeout, allow_redirects=True, stream=True)
            # Read a small chunk to trigger Content-Type resolution
            try:
                next(resp.iter_content(chunk_size=512), None)
            except Exception:
                pass
            resp.close()
        else:
            # Try HEAD first (faster)
            resp = session.head(url, timeout=timeout, allow_redirects=True)
            if resp.status_code == 405:  # HEAD not allowed
                resp = session.get(url, timeout=timeout, allow_redirects=True, stream=True)
                resp.close()

        if resp.status_code == 200:
            if needs_content_check:
                return _validate_content(resp, url)
            return True, f"OK ({resp.status_code})"
        elif resp.status_code in (301, 302, 303, 307, 308):
            return True, f"Redirect ({resp.status_code}) -> {resp.headers.get('Location', '?')}"
        elif resp.status_code == 404:
            return False, f"Not Found (404)"
        elif resp.status_code == 403:
            return None, f"Forbidden (403) - may require auth (ISO/IEC anti-scraping)"
        elif resp.status_code == 412:
            return None, f"HTTP 412 - Precondition Failed (server rejects HEAD, page likely accessible)"
        elif resp.status_code == 202:
            return None, f"HTTP 202 - Accepted (CMDE async response, page likely accessible)"
        elif resp.status_code == 429:
            return None, f"HTTP 429 - Rate Limited (page accessible but too many requests)"
        else:
            return None, f"HTTP {resp.status_code}"
    except requests.Timeout:
        return None, "Timeout"
    except requests.ConnectionError as e:
        return False, f"Connection error: {str(e)[:60]}"
    except Exception as e:
        return None, f"Error: {str(e)[:60]}"


def collect_urls_from_file(md_file: Path) -> Optional[Tuple[str, str]]:
    """Extract source_url from a Markdown file's front matter."""
    content = md_file.read_text(encoding="utf-8")
    fm = extract_front_matter(content)
    if not fm:
        return None
    url = fm.get("source_url", "")
    if not url:
        return None
    return url, fm.get("source_url_status", "ok")


def collect_inline_urls_from_docs(md_file: Path) -> List[str]:
    """Extract all inline markdown links [text](url) from a docs page."""
    content = md_file.read_text(encoding="utf-8")
    # Match [text](url) patterns, skip anchors and relative links
    pattern = re.compile(r'\[([^\]]+)\]\((https?://[^)\s]+)\)')
    urls = []
    for match in pattern.finditer(content):
        url = match.group(2)
        # Strip trailing punctuation that may have been captured
        url = url.rstrip('.,;)')
        if url not in urls:
            urls.append(url)
    return urls


def verify_docs_files(files: List[Path], delay: float = 0.3) -> Tuple[int, int, int]:
    """Verify inline links in docs/ pages. Returns (ok, warn, fail) counts."""
    session = requests.Session()
    session.headers.update({"User-Agent": "docmcp-knowledge-url-verifier/1.0"})

    ok_count = warn_count = fail_count = 0
    checked_urls: set = set()

    for md_file in files:
        if ".vitepress" in str(md_file):
            continue

        urls = collect_inline_urls_from_docs(md_file)
        if not urls:
            continue

        rel_path = md_file.relative_to(ROOT)
        print(f"\n  [{rel_path}] ({len(urls)} links)")

        for url in urls:
            if url in checked_urls:
                continue
            checked_urls.add(url)

            ok, msg = check_url(url, session)

            if ok is True:
                ok_count += 1
                print(f"    OK   {url}")
            elif ok is None:
                warn_count += 1
                print(f"    WARN {url}")
                print(f"         {msg}")
            else:
                fail_count += 1
                print(f"    FAIL {url}")
                print(f"         {msg}")

            time.sleep(delay)

    return ok_count, warn_count, fail_count


def collect_urls_from_index(index_file: Path) -> List[Tuple[str, str]]:
    """Extract source_urls from _index.json."""
    try:
        with open(index_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        results = []
        for entry in data.get("entries", []):
            url = entry.get("source_url", "")
            if url:
                results.append((url, entry.get("source_url_status", "ok")))
        return results
    except Exception:
        return []


def verify_files(files: List[Path], delay: float = 0.3) -> Tuple[int, int, int]:
    """Verify URLs in a list of files. Returns (ok, warn, fail) counts."""
    session = requests.Session()
    session.headers.update({"User-Agent": "docmcp-knowledge-url-verifier/1.0"})

    ok_count = warn_count = fail_count = 0
    checked_urls = set()  # Avoid duplicate checks

    for md_file in files:
        if md_file.name == "README.md" or ".vitepress" in str(md_file):
            continue

        result = collect_urls_from_file(md_file)
        if not result:
            continue

        url, current_status = result
        if url in checked_urls:
            continue
        checked_urls.add(url)

        # Skip already-known broken/archived
        if current_status in ("archived", "broken"):
            warn_count += 1
            print(f"  SKIP [{current_status}] {url}")
            continue

        ok, msg = check_url(url, session)
        rel_path = md_file.relative_to(ROOT)

        if ok is True:
            ok_count += 1
            print(f"  OK   {url}")
        elif ok is None:
            warn_count += 1
            print(f"  WARN {url} -- {msg}")
            print(f"       File: {rel_path}")
        else:
            fail_count += 1
            print(f"  FAIL {url} -- {msg}")
            print(f"       File: {rel_path}")

        time.sleep(delay)

    return ok_count, warn_count, fail_count


def main():
    parser = argparse.ArgumentParser(description="Verify source URLs in content files")
    parser.add_argument("--all", action="store_true", help="Check all content files (front matter source_url)")
    parser.add_argument("--docs", action="store_true", help="Check inline links in docs/ pages")
    parser.add_argument("--file", help="Check a specific file")
    parser.add_argument("--path", help="Check all files under a path")
    parser.add_argument("--changed-only", action="store_true",
                        help="Only check files changed in current PR (for CI)")
    parser.add_argument("--delay", type=float, default=0.3,
                        help="Delay between requests in seconds (default: 0.3)")
    args = parser.parse_args()

    # --docs mode: verify inline links in docs/ pages
    if args.docs:
        docs_dir = ROOT / "docs"
        docs_files = [
            f for f in sorted(docs_dir.rglob("*.md"))
            if ".vitepress" not in str(f)
        ]
        print(f"Verifying inline links in {len(docs_files)} docs pages...")
        ok, warn, fail = verify_docs_files(docs_files, args.delay)
        print(f"\nResults: {ok} OK, {warn} warnings, {fail} failed")
        if fail > 0:
            print(f"\nFAILED: {fail} links are broken. Please fix before merging.")
            sys.exit(1)
        else:
            print("\nAll docs links verified successfully.")
        return

    files = []

    if args.file:
        f = ROOT / args.file if not Path(args.file).is_absolute() else Path(args.file)
        if not f.exists():
            print(f"ERROR: File not found: {f}")
            sys.exit(1)
        files = [f]
    elif args.path:
        search_path = ROOT / args.path
        files = sorted(search_path.rglob("*.md"))
    elif args.changed_only:
        files = get_changed_files()
        if not files:
            print("No changed .md files found. Skipping URL verification.")
            sys.exit(0)
        print(f"Checking {len(files)} changed files...")
    elif args.all:
        # All .md files except docs/ and README.md
        files = [
            f for f in sorted(ROOT.rglob("*.md"))
            if "docs" not in f.parts and ".vitepress" not in str(f)
            and f.name != "README.md"
        ]
    else:
        parser.print_help()
        sys.exit(0)

    print(f"Verifying URLs in {len(files)} files...\n")
    ok, warn, fail = verify_files(files, args.delay)

    print(f"\nResults: {ok} OK, {warn} warnings, {fail} failed")

    if fail > 0:
        print(f"\nFAILED: {fail} URLs are broken. Please fix before merging.")
        sys.exit(1)
    else:
        print("\nAll URLs verified successfully.")


if __name__ == "__main__":
    main()
