#!/usr/bin/env python3
"""Automated full-text acquisition for NMPA guidance documents.

CMDE/NMPA websites use Ruishu bot detection, so direct page scraping
is not feasible. This script uses Vertex AI Search (or Google CSE fallback)
to discover docx download URLs, then downloads and extracts text.

Phase 1 (--discover): Search for docx URLs via Vertex AI Search / Google CSE
Phase 2 (--download): Download docx, extract text, generate markdown, update index

Environment variables (same as fetch_updates.py / check-updates.yml):
    VERTEX_AI_PROJECT_ID, VERTEX_AI_SEARCH_APP_ID, VERTEX_AI_SEARCH_API_KEY
    GOOGLE_SEARCH_API_KEY, GOOGLE_SEARCH_ENGINE_ID  (legacy fallback)

Usage:
    python scripts/fetch_nmpa_fulltext.py --discover --limit 20
    python scripts/fetch_nmpa_fulltext.py --download --limit 50
    python scripts/fetch_nmpa_fulltext.py --stats
    python scripts/fetch_nmpa_fulltext.py --discover --download  # both phases
"""

import argparse
import hashlib
import json
import logging
import os
import re
import sys
import time
from io import BytesIO
from pathlib import Path
from typing import Optional

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)

try:
    import requests
except ImportError:
    logger.error("requests not installed. pip install requests")
    sys.exit(1)

KNOWLEDGE_ROOT = Path(__file__).parent.parent
INDEX_PATH = KNOWLEDGE_ROOT / "nmpa" / "guidance" / "_index.json"
FULLTEXT_DIR = KNOWLEDGE_ROOT / "nmpa" / "guidance" / "fulltext"
DISCOVERED_URLS_PATH = KNOWLEDGE_ROOT / "nmpa" / "guidance" / "_discovered_urls.json"

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/125.0.0.0 Safari/537.36"
)

CMDE_DOCX_PATTERN = re.compile(
    r'https?://(?:www\.)?cmde\.org\.cn/[^\s"\'<>]+\.docx?',
    re.IGNORECASE,
)
NMPA_DOCX_PATTERN = re.compile(
    r'https?://(?:www\.)?nmpa\.gov\.cn/[^\s"\'<>]+\.docx?',
    re.IGNORECASE,
)

# Vertex AI Search config (reuses same env vars as fetch_updates.py)
VERTEX_AI_PROJECT_ID = os.environ.get("VERTEX_AI_PROJECT_ID", "")
VERTEX_AI_SEARCH_APP_ID = os.environ.get("VERTEX_AI_SEARCH_APP_ID", "")
VERTEX_AI_SEARCH_API_KEY = os.environ.get("VERTEX_AI_SEARCH_API_KEY", "")

# Legacy Google CSE fallback
GOOGLE_SEARCH_API_KEY = os.environ.get("GOOGLE_SEARCH_API_KEY", "")
GOOGLE_SEARCH_ENGINE_ID = os.environ.get("GOOGLE_SEARCH_ENGINE_ID", "")

CN_SECTION_PATTERNS = [
    re.compile(r'^[一二三四五六七八九十]+[、.．]'),
    re.compile(r'^（[一二三四五六七八九十]+）'),
    re.compile(r'^第[一二三四五六七八九十百]+[章节条]'),
    re.compile(r'^\d+[、.．]\s'),
    re.compile(r'^（\d+）'),
    re.compile(r'^附[录件]\s*[一二三四五六七八九十A-Z\d]'),
]


# ---------------------------------------------------------------------------
# Web Search (Vertex AI Search / Google CSE)
# ---------------------------------------------------------------------------

class WebSearcher:
    """Unified search via Vertex AI Search (preferred) or Google CSE."""

    VERTEX_URL = (
        "https://discoveryengine.googleapis.com/v1/projects/{project_id}"
        "/locations/global/collections/default_collection"
        "/engines/{app_id}/servingConfigs/default_search:searchLite"
    )
    GOOGLE_CSE_URL = "https://www.googleapis.com/customsearch/v1"

    def __init__(self):
        self.use_vertex = bool(
            VERTEX_AI_PROJECT_ID and VERTEX_AI_SEARCH_APP_ID
            and VERTEX_AI_SEARCH_API_KEY
        )
        self.use_google = bool(GOOGLE_SEARCH_API_KEY and GOOGLE_SEARCH_ENGINE_ID)
        if self.use_vertex:
            logger.info("Using Vertex AI Search (searchLite)")
        elif self.use_google:
            logger.info("Using Google CSE (legacy)")
        else:
            logger.warning(
                "No search API configured. Set VERTEX_AI_* or GOOGLE_SEARCH_* env vars."
            )

    @property
    def available(self) -> bool:
        return self.use_vertex or self.use_google

    def search(self, query: str, num: int = 10) -> list[dict]:
        if self.use_vertex:
            return self._vertex_search(query, num)
        if self.use_google:
            return self._google_search(query, num)
        return []

    def _vertex_search(self, query: str, num: int) -> list[dict]:
        query = re.sub(r"site:\S+\s*", "", query).strip()
        url = self.VERTEX_URL.format(
            project_id=VERTEX_AI_PROJECT_ID,
            app_id=VERTEX_AI_SEARCH_APP_ID,
        )
        try:
            resp = requests.post(
                url,
                params={"key": VERTEX_AI_SEARCH_API_KEY},
                json={"query": query, "pageSize": min(num, 25)},
                headers={"Content-Type": "application/json"},
                timeout=20,
            )
            if resp.status_code != 200:
                logger.warning(f"Vertex AI Search HTTP {resp.status_code}")
                return []
            results = []
            for r in resp.json().get("results", []):
                doc = r.get("document", {})
                derived = doc.get("derivedStructData", {})
                link = derived.get("link", "")
                title = derived.get("title", "")
                snippet = ""
                for s in derived.get("snippets", []):
                    if s.get("snippet"):
                        snippet = re.sub(r"<[^>]+>", "", s["snippet"])
                        break
                if title or link:
                    results.append({"title": title, "link": link,
                                    "snippet": snippet[:300]})
            return results
        except Exception as e:
            logger.warning(f"Vertex AI Search error: {e}")
            return []

    def _google_search(self, query: str, num: int) -> list[dict]:
        try:
            params = {
                "key": GOOGLE_SEARCH_API_KEY,
                "cx": GOOGLE_SEARCH_ENGINE_ID,
                "q": query,
                "num": min(num, 10),
            }
            resp = requests.get(self.GOOGLE_CSE_URL, params=params, timeout=15)
            resp.raise_for_status()
            results = []
            for item in resp.json().get("items", []):
                results.append({
                    "title": item.get("title", ""),
                    "link": item.get("link", ""),
                    "snippet": item.get("snippet", "")[:300],
                })
            return results
        except Exception as e:
            logger.warning(f"Google CSE error: {e}")
            return []


# ---------------------------------------------------------------------------
# Index & URL management
# ---------------------------------------------------------------------------

def load_index() -> dict:
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_index(data: dict):
    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    logger.info(f"Saved index: {INDEX_PATH}")


def load_discovered_urls() -> dict:
    if DISCOVERED_URLS_PATH.exists():
        with open(DISCOVERED_URLS_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_discovered_urls(data: dict):
    with open(DISCOVERED_URLS_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def generate_slug(title_zh: str, doc_number: str) -> str:
    dn_match = re.search(r'(\d{4})\D*?(\d+)', doc_number)
    if dn_match:
        return f"cmde-{dn_match.group(1)}-{dn_match.group(2)}"
    short_hash = hashlib.md5(title_zh.encode()).hexdigest()[:6]
    cleaned = re.sub(r'[（()）\[\]【】]', '', title_zh)
    cleaned = re.sub(r'[^\w]', '-', cleaned)
    cleaned = re.sub(r'-+', '-', cleaned).strip('-')
    return f"{cleaned[:50]}-{short_hash}".lower()


def fulltext_exists(entry: dict) -> bool:
    slug = entry.get("slug", "")
    eid = entry.get("id", "")
    for name in [slug, re.sub(r'[^\w\-.]', '_', eid)]:
        if not name:
            continue
        if (FULLTEXT_DIR / f"{name}.md").exists():
            return True
    return False


# ---------------------------------------------------------------------------
# Phase 1: Discover docx URLs via web search
# ---------------------------------------------------------------------------

def extract_docx_url_from_results(results: list[dict]) -> Optional[str]:
    """Extract a docx download URL from search results."""
    for result in results:
        link = result.get("link", "")
        snippet = result.get("snippet", "")
        # Direct docx link in result URL
        if re.search(r'\.docx?$', link, re.IGNORECASE):
            return link
        # Check link for CMDE docx pattern
        m = CMDE_DOCX_PATTERN.search(link)
        if m:
            return m.group(0)
        m = NMPA_DOCX_PATTERN.search(link)
        if m:
            return m.group(0)
        # Check snippet for docx URLs
        for pattern in [CMDE_DOCX_PATTERN, NMPA_DOCX_PATTERN]:
            m = pattern.search(snippet)
            if m:
                return m.group(0)
    return None


def try_fetch_docx_from_page(page_url: str) -> Optional[str]:
    """Try to fetch a page and find docx download links in it.
    Note: CMDE has bot detection, so this may not work for cmde.org.cn pages.
    """
    if "cmde.org.cn" in page_url:
        return None
    try:
        resp = requests.get(
            page_url,
            headers={"User-Agent": USER_AGENT},
            timeout=10,
            allow_redirects=True,
        )
        if resp.status_code != 200:
            return None
        for pattern in [CMDE_DOCX_PATTERN, NMPA_DOCX_PATTERN]:
            m = pattern.search(resp.text)
            if m:
                return m.group(0)
    except Exception:
        pass
    return None


def discover_urls(searcher: WebSearcher, limit: int = 0, dry_run: bool = False):
    """Phase 1: Search for docx URLs for entries without fulltext."""
    if not searcher.available:
        logger.error("No search API available. Cannot discover URLs.")
        return

    index_data = load_index()
    entries = index_data.get("entries", [])
    discovered = load_discovered_urls()

    candidates = [
        e for e in entries
        if not fulltext_exists(e) and e["id"] not in discovered
    ]
    if limit > 0:
        candidates = candidates[:limit]

    logger.info(
        f"Discovering URLs for {len(candidates)} entries "
        f"({len(entries)} total, {len(discovered)} already searched)"
    )

    found = 0
    for i, entry in enumerate(candidates):
        title_zh = entry.get("title", {}).get("zh", "")
        doc_number = entry.get("doc_number", "")
        eid = entry["id"]

        logger.info(f"[{i+1}/{len(candidates)}] {title_zh[:50]}...")

        if dry_run:
            continue

        queries = [
            f'site:cmde.org.cn "{title_zh}" filetype:docx',
            f'site:cmde.org.cn "{title_zh}"',
            f'site:nmpa.gov.cn "{title_zh}" 指导原则',
        ]

        docx_url = None
        for query in queries:
            results = searcher.search(query, num=5)
            docx_url = extract_docx_url_from_results(results)
            if docx_url:
                break

            for result in results:
                link = result.get("link", "")
                if link and "cmde.org.cn" not in link:
                    docx_url = try_fetch_docx_from_page(link)
                    if docx_url:
                        break
            if docx_url:
                break
            time.sleep(0.5)

        if docx_url:
            discovered[eid] = {"url": docx_url, "format": "docx"}
            logger.info(f"  FOUND: {docx_url}")
            found += 1
        else:
            page_url = ""
            if results:
                page_url = results[0].get("link", "")
            discovered[eid] = {"url": "", "page_url": page_url, "format": ""}
            logger.info(f"  NOT FOUND (page: {page_url[:80]})")

        if (i + 1) % 10 == 0:
            save_discovered_urls(discovered)

        time.sleep(1)

    if not dry_run:
        save_discovered_urls(discovered)
    logger.info(f"\nDiscovery: {found} URLs found out of {len(candidates)}")


# ---------------------------------------------------------------------------
# Phase 2: Download & Extract
# ---------------------------------------------------------------------------

def download_docx(url: str) -> Optional[bytes]:
    try:
        resp = requests.get(
            url,
            headers={"User-Agent": USER_AGENT},
            timeout=60,
            allow_redirects=True,
        )
        resp.raise_for_status()
        ct = resp.headers.get("content-type", "").lower()
        if len(resp.content) < 500 and "html" in ct:
            logger.warning(f"  Got HTML instead of docx (blocked?)")
            return None
        return resp.content
    except Exception as e:
        logger.warning(f"  Download failed: {e}")
        return None


def extract_docx_to_markdown(docx_bytes: bytes) -> str:
    try:
        from docx import Document
    except ImportError:
        logger.error("python-docx not installed. pip install python-docx")
        return ""

    try:
        doc = Document(BytesIO(docx_bytes))
    except Exception as e:
        logger.error(f"  Failed to open docx: {e}")
        return ""

    lines = []
    for para in doc.paragraphs:
        text = para.text.strip()
        if not text:
            lines.append("")
            continue
        style_name = para.style.name if para.style else ""
        lines.append(_para_to_markdown(text, style_name, para))

    for table in doc.tables:
        lines.append("")
        lines.extend(_table_to_markdown(table))
        lines.append("")

    content = "\n".join(lines)
    content = re.sub(r'\n{3,}', '\n\n', content)
    return content.strip()


def _para_to_markdown(text: str, style_name: str, para) -> str:
    heading_styles = {
        "Heading 1", "Heading 2", "Heading 3", "Heading 4",
        "heading 1", "heading 2", "heading 3", "heading 4",
    }
    if style_name in heading_styles:
        level_match = re.search(r'(\d)', style_name)
        level = int(level_match.group(1)) if level_match else 2
        return f"{'#' * level} {text}"

    for pattern in CN_SECTION_PATTERNS:
        if pattern.match(text):
            if re.match(r'^[一二三四五六七八九十]+[、.．]', text):
                return f"## {text}"
            elif re.match(r'^（[一二三四五六七八九十]+）', text):
                return f"### {text}"
            elif re.match(r'^第[一二三四五六七八九十百]+[章节]', text):
                return f"## {text}"
            elif re.match(r'^第[一二三四五六七八九十百]+条', text):
                return f"### {text}"
            elif re.match(r'^\d+[、.．]\s', text):
                return f"### {text}"
            elif re.match(r'^（\d+）', text):
                return f"#### {text}"
            elif re.match(r'^附[录件]', text):
                return f"## {text}"

    is_bold = (all(run.bold for run in para.runs if run.text.strip())
               if para.runs else False)
    if is_bold and len(text) < 80:
        return f"**{text}**"

    return text


def _table_to_markdown(table) -> list[str]:
    if not table.rows:
        return []

    rows_data = []
    for row in table.rows:
        cells = [cell.text.strip().replace('\n', ' ').replace('|', '/')
                 for cell in row.cells]
        rows_data.append(cells)

    if not rows_data:
        return []

    max_cols = max(len(r) for r in rows_data)
    for row in rows_data:
        while len(row) < max_cols:
            row.append("")

    lines = []
    header = rows_data[0]
    lines.append("| " + " | ".join(header) + " |")
    lines.append("| " + " | ".join(["---"] * max_cols) + " |")
    for row in rows_data[1:]:
        lines.append("| " + " | ".join(row) + " |")
    return lines


def download_and_extract(limit: int = 0, dry_run: bool = False,
                         force: bool = False):
    """Phase 2: Download docx files and extract fulltext."""
    index_data = load_index()
    entries = index_data.get("entries", [])
    discovered = load_discovered_urls()

    candidates = []
    for entry in entries:
        eid = entry["id"]
        if not force and fulltext_exists(entry):
            continue
        disc = discovered.get(eid, {})
        url = disc.get("url", "")
        if not url:
            continue
        candidates.append((entry, url))

    if limit > 0:
        candidates = candidates[:limit]

    logger.info(f"Downloading {len(candidates)} documents")

    success = 0
    failed = 0
    index_modified = False

    FULLTEXT_DIR.mkdir(parents=True, exist_ok=True)

    for i, (entry, url) in enumerate(candidates):
        title_zh = entry.get("title", {}).get("zh", "")
        doc_number = entry.get("doc_number", "")
        eid = entry["id"]

        logger.info(f"[{i+1}/{len(candidates)}] {title_zh[:50]}")
        logger.info(f"  URL: {url}")

        if dry_run:
            continue

        docx_bytes = download_docx(url)
        if not docx_bytes:
            failed += 1
            continue

        logger.info(f"  Downloaded {len(docx_bytes) / 1024:.1f} KB")

        markdown = extract_docx_to_markdown(docx_bytes)
        if not markdown or len(markdown) < 100:
            logger.warning(
                f"  SKIP: Extracted text too short ({len(markdown)} chars)"
            )
            failed += 1
            continue

        slug = entry.get("slug", "")
        if not slug:
            slug = generate_slug(title_zh, doc_number)
            existing_slugs = {e.get("slug", "") for e in entries}
            if slug in existing_slugs:
                slug = f"{slug}-{hashlib.md5(eid.encode()).hexdigest()[:4]}"
            entry["slug"] = slug
            entry["source_url"] = url
            index_modified = True
            logger.info(f"  Generated slug: {slug}")

        fulltext_md = f"# {title_zh}\n\n"
        if doc_number:
            fulltext_md += f"**{doc_number}**\n\n"
        fulltext_md += f"**Source:** [{url}]({url})\n\n"
        fulltext_md += f"---\n\n{markdown}\n"

        out_path = FULLTEXT_DIR / f"{slug}.md"
        out_path.write_text(fulltext_md, encoding="utf-8")
        logger.info(f"  Saved: {out_path.name} ({len(fulltext_md)} chars)")
        success += 1

        time.sleep(0.5)

    if index_modified and not dry_run:
        save_index(index_data)

    logger.info(f"\nDownload complete: {success} succeeded, {failed} failed")


# ---------------------------------------------------------------------------
# Stats
# ---------------------------------------------------------------------------

def show_stats():
    index_data = load_index()
    entries = index_data.get("entries", [])
    discovered = load_discovered_urls()

    with_slug = [e for e in entries if e.get("slug")]
    with_fulltext = [e for e in entries if fulltext_exists(e)]
    without_fulltext = [e for e in entries if not fulltext_exists(e)]
    discovered_with_url = {k: v for k, v in discovered.items() if v.get("url")}
    discovered_no_url = {k: v for k, v in discovered.items()
                         if k in discovered and not v.get("url")}

    ft_files = list(FULLTEXT_DIR.glob("*.md")) if FULLTEXT_DIR.exists() else []
    en_files = [f for f in ft_files if f.stem.endswith('.en')]
    zh_only = [f for f in ft_files if not f.stem.endswith('.en')]

    print(f"\n=== NMPA Guidance Fulltext Statistics ===")
    print(f"Total index entries:       {len(entries)}")
    print(f"Entries with slug:         {len(with_slug)}")
    print(f"Entries with fulltext:     {len(with_fulltext)}")
    print(f"Entries without fulltext:  {len(without_fulltext)}")
    print(f"")
    print(f"Fulltext files (ZH *.md):  {len(zh_only)}")
    print(f"English translations:      {len(en_files)}")
    print(f"")
    print(f"URL discovery status:")
    print(f"  Searched:                {len(discovered)}")
    print(f"  Found docx URL:          {len(discovered_with_url)}")
    print(f"  No URL found:            {len(discovered_no_url)}")
    not_searched = len(without_fulltext) - len(
        [e for e in without_fulltext if e["id"] in discovered]
    )
    print(f"  Not yet searched:        {not_searched}")
    print()

    by_cat = {}
    for e in entries:
        cat = e.get("category", "unknown")
        ft = fulltext_exists(e)
        by_cat.setdefault(cat, {"total": 0, "has_ft": 0})
        by_cat[cat]["total"] += 1
        if ft:
            by_cat[cat]["has_ft"] += 1

    print("Coverage by category:")
    for cat, s in sorted(by_cat.items(), key=lambda x: -x[1]["total"]):
        pct = s["has_ft"] / s["total"] * 100 if s["total"] else 0
        print(f"  {cat:25s} {s['has_ft']:3d}/{s['total']:3d} ({pct:.0f}%)")


def main():
    parser = argparse.ArgumentParser(
        description="Fetch NMPA guidance fulltext documents",
    )
    parser.add_argument("--discover", action="store_true",
                        help="Phase 1: Search for docx download URLs")
    parser.add_argument("--download", action="store_true",
                        help="Phase 2: Download and extract fulltext")
    parser.add_argument("--stats", action="store_true",
                        help="Show fulltext coverage statistics")
    parser.add_argument("--limit", type=int, default=0,
                        help="Max entries to process (0 = all)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview without downloading/writing")
    parser.add_argument("--force", action="store_true",
                        help="Re-process even if fulltext exists")
    args = parser.parse_args()

    if not (args.discover or args.download or args.stats):
        parser.print_help()
        print("\nExamples:")
        print("  python scripts/fetch_nmpa_fulltext.py --stats")
        print("  python scripts/fetch_nmpa_fulltext.py --discover --limit 20")
        print("  python scripts/fetch_nmpa_fulltext.py --download --limit 50")
        print("  python scripts/fetch_nmpa_fulltext.py --discover --download")
        return

    if args.stats:
        show_stats()
        return

    searcher = WebSearcher()

    if args.discover:
        discover_urls(searcher, limit=args.limit, dry_run=args.dry_run)

    if args.download:
        download_and_extract(limit=args.limit, dry_run=args.dry_run,
                             force=args.force)


if __name__ == "__main__":
    main()
