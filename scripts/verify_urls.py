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
    "eur-lex.europa.eu", "ec.europa.eu", "cen.eu", "team-nb.org",
    # FDA
    "fda.gov", "www.fda.gov", "accessdata.fda.gov", "ecfr.gov",
    # NMPA
    "nmpa.gov.cn", "www.nmpa.gov.cn", "cmde.org.cn", "www.cmde.org.cn",
    # Standards
    "iso.org", "www.iso.org", "iec.ch", "www.iec.ch",
    "sac.gov.cn", "www.sac.gov.cn",
    # WordPress source (reguverse.com - for migrated content)
    "reguverse.com", "www.reguverse.com",
}


def extract_front_matter(md_content: str) -> dict | None:
    match = re.match(r"^---\n(.+?)\n---", md_content, re.DOTALL)
    if not match:
        return None
    try:
        return yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        return None


def get_changed_files() -> list[Path]:
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


def check_url(url: str, session: requests.Session, timeout: int = 15) -> tuple[bool, str]:
    """Check if a URL is accessible. Returns (ok, status_message)."""
    if not url or url.startswith("#"):
        return False, "empty or anchor URL"

    parsed = urlparse(url)
    if not parsed.scheme in ("http", "https"):
        return False, f"invalid scheme: {parsed.scheme}"

    # Check domain is official
    domain = parsed.netloc.lower()
    if domain not in OFFICIAL_DOMAINS:
        return None, f"non-official domain: {domain} (manual review needed)"

    try:
        # Try HEAD first (faster)
        resp = session.head(url, timeout=timeout, allow_redirects=True)
        if resp.status_code == 405:  # HEAD not allowed
            resp = session.get(url, timeout=timeout, allow_redirects=True, stream=True)
            resp.close()

        if resp.status_code == 200:
            return True, f"OK ({resp.status_code})"
        elif resp.status_code in (301, 302, 303, 307, 308):
            return True, f"Redirect ({resp.status_code}) -> {resp.headers.get('Location', '?')}"
        elif resp.status_code == 404:
            return False, f"Not Found (404)"
        elif resp.status_code == 403:
            return None, f"Forbidden (403) - may require auth"
        else:
            return None, f"HTTP {resp.status_code}"
    except requests.Timeout:
        return None, "Timeout"
    except requests.ConnectionError as e:
        return False, f"Connection error: {str(e)[:60]}"
    except Exception as e:
        return None, f"Error: {str(e)[:60]}"


def collect_urls_from_file(md_file: Path) -> tuple[str, str] | None:
    """Extract source_url from a Markdown file's front matter."""
    content = md_file.read_text(encoding="utf-8")
    fm = extract_front_matter(content)
    if not fm:
        return None
    url = fm.get("source_url", "")
    if not url:
        return None
    return url, fm.get("source_url_status", "ok")


def collect_urls_from_index(index_file: Path) -> list[tuple[str, str]]:
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


def verify_files(files: list[Path], delay: float = 0.3) -> tuple[int, int, int]:
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
    parser.add_argument("--all", action="store_true", help="Check all files")
    parser.add_argument("--file", help="Check a specific file")
    parser.add_argument("--path", help="Check all files under a path")
    parser.add_argument("--changed-only", action="store_true",
                        help="Only check files changed in current PR (for CI)")
    parser.add_argument("--delay", type=float, default=0.3,
                        help="Delay between requests in seconds (default: 0.3)")
    args = parser.parse_args()

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
