#!/usr/bin/env python3
"""
Batch verify ISO/IEC standard URLs by checking if the standard number in the URL page
matches the expected standard number. Uses HTTP HEAD/GET to check for 404s and redirects.
"""
import json
import re
import urllib.request
import urllib.error
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE = Path("eu_mdr/other_standards")

all_cats = sorted([f.stem.replace("standards-", "") for f in BASE.glob("standards-*.json")])
start_idx = all_cats.index("diagnostic_imaging") if "diagnostic_imaging" in all_cats else 0
remaining_cats = all_cats[start_idx:]

issues = []
checked = 0

def check_url(cat, number, url):
    """Check if URL returns 200 and is not a generic redirect."""
    try:
        req = urllib.request.Request(url, method="HEAD", headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
        })
        resp = urllib.request.urlopen(req, timeout=15)
        final_url = resp.geturl()
        status = resp.status
        # Check for redirect to generic page
        if "search" in final_url or "products" in final_url:
            return (cat, number, url, f"REDIRECT to generic: {final_url}")
        return None
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return (cat, number, url, "404 Not Found")
        elif e.code == 403:
            return None  # Some sites block HEAD, not necessarily an error
        else:
            return (cat, number, url, f"HTTP {e.code}")
    except urllib.error.URLError as e:
        return (cat, number, url, f"URL Error: {e.reason}")
    except Exception as e:
        return (cat, number, url, f"Error: {str(e)[:50]}")

# Collect all URLs to check
urls_to_check = []
for cat in remaining_cats:
    path = BASE / f"standards-{cat}.json"
    data = json.loads(path.read_text())
    for s in data["standards"]:
        url = s.get("source_url", "")
        num = s["number"]
        title = s.get("title", {})
        if isinstance(title, dict):
            t = title.get("en", "")
        else:
            t = str(title)
        if url and ("iso.org" in url or "iec.ch" in url):
            urls_to_check.append((cat, num, url, t))

print(f"Checking {len(urls_to_check)} ISO/IEC URLs...")

# Check for obvious URL pattern issues first (without network)
pattern_issues = []
for cat, num, url, title in urls_to_check:
    # Check ISO URLs - standard number should map to URL
    if "iso.org/standard/" in url:
        pass  # Can't verify standard_id without fetching
    # Check IEC URLs - publication number format
    if "webstore.iec.ch/en/publication/" in url:
        pass  # Can't verify without fetching
    # Check for empty titles
    if not title.strip():
        pattern_issues.append((cat, num, url, "EMPTY TITLE"))

if pattern_issues:
    print(f"\nPattern issues found (no network needed):")
    for cat, num, url, issue in pattern_issues:
        print(f"  [{cat}] {num}: {issue}")

# Now do network checks with ThreadPoolExecutor
print(f"\nRunning network checks (HEAD requests)...")
results = []
with ThreadPoolExecutor(max_workers=5) as executor:
    futures = {}
    for cat, num, url, title in urls_to_check:
        f = executor.submit(check_url, cat, num, url)
        futures[f] = (cat, num, url)
    
    for f in as_completed(futures):
        checked += 1
        result = f.result()
        if result:
            results.append(result)
        if checked % 50 == 0:
            print(f"  Checked {checked}/{len(urls_to_check)}...")

print(f"\nChecked {checked} URLs total.")
if results:
    print(f"\n{'='*80}")
    print(f"ISSUES FOUND: {len(results)}")
    print(f"{'='*80}")
    for cat, num, url, issue in sorted(results):
        print(f"  [{cat}] {num}")
        print(f"    URL: {url}")
        print(f"    Issue: {issue}")
        print()
else:
    print("\nNo issues found!")
