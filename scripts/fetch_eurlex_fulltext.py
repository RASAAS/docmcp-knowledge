#!/usr/bin/env python3
"""Fetch EU regulation full text from EUR-Lex and convert to Markdown.

Parses EUR-Lex HTML pages using BeautifulSoup and extracts structured
regulation text. Saves as markdown files in eu_mdr/regulations/fulltext/.

Usage:
    python scripts/fetch_eurlex_fulltext.py --dry-run
    python scripts/fetch_eurlex_fulltext.py
    python scripts/fetch_eurlex_fulltext.py --id eu-mdr-2017-745
    python scripts/fetch_eurlex_fulltext.py --force
"""

import argparse
import json
import logging
import re
import sys
import time
from pathlib import Path
from typing import Optional

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

try:
    import requests
except ImportError:
    logger.error("requests not installed. pip install requests")
    sys.exit(1)

try:
    from bs4 import BeautifulSoup, NavigableString, Tag
except ImportError:
    logger.error("beautifulsoup4 not installed. pip install beautifulsoup4")
    sys.exit(1)


KNOWLEDGE_ROOT = Path(__file__).parent.parent
REGULATIONS_INDEX = KNOWLEDGE_ROOT / "eu_mdr" / "regulations" / "_index.json"
FULLTEXT_DIR = KNOWLEDGE_ROOT / "eu_mdr" / "regulations" / "fulltext"

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/125.0.0.0 Safari/537.36"
)
HEADERS = {
    "User-Agent": USER_AGENT,
    "Accept": "text/html,application/xhtml+xml,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
}

CELEX_PATTERN = re.compile(r"CELEX[:%](\d+\w+)")
ELI_PATTERN = re.compile(r"/eli/(dir|reg|dec)/(\d{4})/(\d+)(?:/oj)?")

CONSOLIDATED_CELEX_OVERRIDES: dict[str, str] = {
    "32006R1907": "02006R1907-20231201",
    "32001L0083": "02001L0083-20220101",
    "32008R1272": "02008R1272-20200101",
}

MAX_RETRIES = 3
RETRY_DELAY = 15


def celex_to_html_url(celex: str) -> str:
    """Build HTML full text URL from CELEX number."""
    return (
        "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/"
        f"?uri=CELEX:{celex}"
    )


def source_url_to_html_url(source_url: str) -> Optional[str]:
    """Convert a EUR-Lex source URL to the HTML full text URL (fallback)."""
    celex_match = CELEX_PATTERN.search(source_url)
    if celex_match:
        return celex_to_html_url(celex_match.group(1))

    eli_match = ELI_PATTERN.search(source_url)
    if eli_match:
        act_type, year, number = eli_match.groups()
        prefix = "L" if act_type == "dir" else "R"
        celex = f"3{year}{prefix}{number.zfill(4)}"
        return celex_to_html_url(celex)

    return None


# ---------------------------------------------------------------------------
# BeautifulSoup-based EUR-Lex parser
# ---------------------------------------------------------------------------

def _has_class(tag: Tag, cls_fragment: str) -> bool:
    """Check if any of the tag's CSS classes contain cls_fragment."""
    for c in tag.get("class", []):
        if cls_fragment in c:
            return True
    return False


def _is_layout_table(table: Tag) -> bool:
    """Detect EUR-Lex layout tables (<=2 columns, used for numbered lists)."""
    rows = table.find_all("tr")
    if not rows:
        return True
    for row in rows:
        cells = row.find_all(["td", "th"])
        if len(cells) > 2:
            return False
    return True


def _table_has_content(table: Tag) -> bool:
    """Check if table contains any meaningful text."""
    text = table.get_text(strip=True)
    return len(text) > 5


def _layout_table_to_text(table: Tag) -> list[str]:
    """Convert a 2-column layout table to indented text lines."""
    lines: list[str] = []
    for row in table.find_all("tr"):
        cells = row.find_all(["td", "th"])
        if not cells:
            continue
        parts = [c.get_text(strip=True) for c in cells]
        parts = [p for p in parts if p]
        if not parts:
            continue
        if len(parts) == 2:
            label, content = parts
            if re.match(r"^[\(\[]?\d+[\)\]]?\.?$|^[\(\[]?[a-z][\)\]]?\.?$",
                        label):
                lines.append(f"{label} {content}")
            else:
                lines.append(f"{label} {content}")
        else:
            lines.append(" ".join(parts))
    return lines


def _real_table_to_markdown(table: Tag) -> list[str]:
    """Convert a real data table to Markdown table syntax."""
    rows_data: list[list[str]] = []
    for row in table.find_all("tr"):
        cells = row.find_all(["td", "th"])
        row_cells = []
        for c in cells:
            text = c.get_text(" ", strip=True)
            text = re.sub(r"\s+", " ", text)
            text = text.replace("|", "\\|")
            row_cells.append(text)
        if row_cells:
            rows_data.append(row_cells)

    if not rows_data:
        return []

    max_cols = max(len(r) for r in rows_data)
    if max_cols == 0:
        return []

    lines = [""]
    for i, row in enumerate(rows_data):
        while len(row) < max_cols:
            row.append("")
        lines.append("| " + " | ".join(row) + " |")
        if i == 0:
            lines.append("| " + " | ".join(["---"] * max_cols) + " |")
    lines.append("")
    return lines


def _element_to_markdown(el: Tag, depth: int = 0) -> list[str]:
    """Recursively convert a BeautifulSoup element to markdown lines."""
    lines: list[str] = []

    for child in el.children:
        if isinstance(child, NavigableString):
            text = str(child).strip()
            if text:
                text = re.sub(r"\s+", " ", text)
                lines.append(text)
            continue

        if not isinstance(child, Tag):
            continue

        tag_name = child.name
        classes = child.get("class", [])
        cls_str = " ".join(classes)

        if tag_name in ("script", "style", "head", "nav", "footer"):
            continue

        if _has_class(child, "eli-main-title"):
            continue

        if tag_name == "table":
            if not _table_has_content(child):
                continue
            if _is_layout_table(child):
                text_lines = _layout_table_to_text(child)
                if text_lines:
                    lines.append("")
                    lines.extend(text_lines)
                    lines.append("")
            else:
                lines.extend(_real_table_to_markdown(child))
            continue

        if "oj-ti-section-1" in cls_str:
            lines.append("")
            lines.append(f"## {child.get_text(strip=True)}")
            lines.append("")
            continue

        if "oj-ti-section-2" in cls_str:
            lines.append("")
            lines.append(f"### {child.get_text(strip=True)}")
            lines.append("")
            continue

        if "oj-ti-art" in cls_str:
            lines.append("")
            lines.append(f"### {child.get_text(strip=True)}")
            lines.append("")
            continue

        if "oj-doc-ti" in cls_str:
            lines.append("")
            lines.append(f"## {child.get_text(strip=True)}")
            lines.append("")
            continue

        if tag_name in ("h1", "h2", "h3", "h4", "h5", "h6"):
            level = int(tag_name[1])
            prefix = "#" * min(level, 6)
            lines.append("")
            lines.append(f"{prefix} {child.get_text(strip=True)}")
            lines.append("")
            continue

        if tag_name in ("ol", "ul"):
            for li in child.find_all("li", recursive=False):
                li_text = li.get_text(" ", strip=True)
                li_text = re.sub(r"\s+", " ", li_text)
                if li_text:
                    lines.append(f"- {li_text}")
            lines.append("")
            continue

        if tag_name == "p" or _has_class(child, "oj-normal"):
            text = child.get_text(" ", strip=True)
            text = re.sub(r"\s+", " ", text)
            if text:
                lines.append(text)
            continue

        if tag_name == "br":
            continue

        sub = _element_to_markdown(child, depth + 1)
        lines.extend(sub)

    return lines


def _parse_flattened_body(soup: BeautifulSoup) -> tuple[str, str]:
    """Parse EUR-Lex pages with flattened body format (no eli-container).

    Some consolidated regulations (e.g. CLP) serve content directly under
    <body> with <p class="reference">, <hr class="separator">, and plain <p>
    tags instead of the standard eli-container/eli-subdivision wrappers.
    """
    body = soup.find("body")
    if not body:
        return ("", "")

    title = ""
    all_lines: list[str] = []
    past_separator = False

    for child in body.children:
        if isinstance(child, NavigableString):
            t = child.strip()
            if t:
                all_lines.append(t)
            continue

        if not isinstance(child, Tag):
            continue

        tag_name = child.name
        classes = child.get("class", [])

        if "disclaimer" in classes or "reference" in classes:
            continue

        if tag_name == "hr":
            if not past_separator:
                past_separator = True
                all_lines.append("---")
                all_lines.append("")
            continue

        if tag_name == "script" or tag_name == "style":
            continue

        sub_lines = _element_to_markdown(child)
        text = "\n".join(sub_lines).strip()

        if not title and text and len(text) > 20 and not text.startswith("|"):
            title = text.split("\n")[0].strip().lstrip("#").strip()

        all_lines.extend(sub_lines)

    markdown = "\n".join(all_lines)
    markdown = re.sub(r"\n{4,}", "\n\n\n", markdown)
    return (title, markdown.strip())


def parse_eurlex_html(html: str) -> tuple[str, str]:
    """Parse EUR-Lex HTML and return (title, markdown_body).

    Handles two HTML formats:
    1. Standard eli-container / document1 structure (most regulations)
    2. Flattened body format (some consolidated versions like CLP)
    """
    soup = BeautifulSoup(html, "html.parser")

    container = soup.find(class_="eli-container")
    if not container:
        container = soup.find(id="document1")

    if not container:
        body = soup.find("body")
        if body:
            p_count = len(body.find_all("p", recursive=False))
            if p_count > 20:
                logger.info("  Using flattened body parser")
                return _parse_flattened_body(soup)
        return ("", "")

    title = ""
    title_el = container.find(class_="eli-main-title")
    if title_el:
        doc_ti = title_el.find(class_="doc-ti")
        if doc_ti:
            title = doc_ti.get_text(" ", strip=True)
        else:
            title = title_el.get_text(" ", strip=True)
        title = re.sub(r"\s+", " ", title).strip()

    subdivisions = container.find_all(class_="eli-subdivision",
                                      recursive=False)
    if not subdivisions:
        subdivisions = container.find_all(class_="eli-subdivision")

    all_lines: list[str] = []
    for subdiv in subdivisions:
        subdiv_id = subdiv.get("id", "")
        if subdiv_id == "pbl_1":
            all_lines.append("## Preamble")
            all_lines.append("")
        elif subdiv_id == "enc_1":
            all_lines.append("")
        elif subdiv_id == "fnp_1":
            all_lines.append("")
            all_lines.append("---")
            all_lines.append("")

        sub_lines = _element_to_markdown(subdiv)
        all_lines.extend(sub_lines)

    markdown = "\n".join(all_lines)
    markdown = re.sub(r"\n{4,}", "\n\n\n", markdown)
    return (title, markdown.strip())


def fetch_and_parse(html_url: str) -> Optional[tuple[str, str]]:
    """Fetch EUR-Lex HTML and parse to markdown.

    Retries on HTTP 202 (Accepted) which EUR-Lex returns when generating
    large documents asynchronously.
    """
    session = requests.Session()
    session.headers.update(HEADERS)

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp = session.get(html_url, timeout=120, allow_redirects=True)
        except Exception as e:
            logger.error(f"  Failed to fetch {html_url}: {e}")
            return None

        if resp.status_code == 202:
            if attempt < MAX_RETRIES:
                logger.info(
                    f"  HTTP 202 Accepted (attempt {attempt}/{MAX_RETRIES}), "
                    f"retrying in {RETRY_DELAY}s...")
                time.sleep(RETRY_DELAY)
                continue
            else:
                logger.warning(
                    f"  HTTP 202 after {MAX_RETRIES} attempts, giving up")
                return None

        if resp.status_code != 200:
            logger.error(f"  HTTP {resp.status_code} for {html_url}")
            return None

        break

    content_type = resp.headers.get("content-type", "").lower()
    if "html" not in content_type:
        logger.error(f"  Unexpected content type: {content_type}")
        return None

    html = resp.text
    logger.info(f"  Downloaded {len(html):,} bytes")

    title, markdown = parse_eurlex_html(html)

    if not markdown or len(markdown) < 100:
        logger.warning(f"  Extracted text too short ({len(markdown)} chars)")
        return None

    return (title, markdown)


# ---------------------------------------------------------------------------
# Index loading and file I/O
# ---------------------------------------------------------------------------

def load_regulation_entries(doc_id: str = "") -> list[dict]:
    """Load regulation entries from _index.json."""
    if not REGULATIONS_INDEX.exists():
        logger.error(f"Index file not found: {REGULATIONS_INDEX}")
        return []

    with open(REGULATIONS_INDEX, "r", encoding="utf-8") as f:
        data = json.load(f)

    entries = []
    for doc in data.get("documents", []):
        if doc_id and doc.get("id") != doc_id:
            continue
        source_url = doc.get("source_url", "")
        if not source_url:
            continue
        if "eur-lex.europa.eu" not in source_url:
            continue
        entries.append(doc)

    return entries


def get_fulltext_path(entry: dict) -> Path:
    """Get the output path for a regulation fulltext."""
    slug = entry.get("slug", "")
    if not slug:
        slug = entry.get("id", "unknown")
    return FULLTEXT_DIR / f"{slug}.md"


def process_regulation(entry: dict, dry_run: bool = False,
                       force: bool = False) -> bool:
    """Process a single regulation entry."""
    eid = entry.get("id", "")
    title = entry.get("title", {})
    if isinstance(title, dict):
        display = title.get("en", "") or title.get("zh", "") or eid
    else:
        display = str(title)
    number = entry.get("number", "")

    logger.info(f"Processing: {eid}")
    logger.info(f"  Title: {display[:80]}")

    out_path = get_fulltext_path(entry)
    if out_path.exists() and not force:
        logger.info(f"  SKIP: Fulltext already exists at {out_path}")
        return False

    source_url = entry.get("source_url", "")
    celex = entry.get("celex", "")
    if celex:
        consolidated = CONSOLIDATED_CELEX_OVERRIDES.get(celex, "")
        if consolidated:
            html_url = celex_to_html_url(consolidated)
            logger.info(f"  Using consolidated CELEX: {consolidated}")
        else:
            html_url = celex_to_html_url(celex)
    else:
        html_url = source_url_to_html_url(source_url)
    if not html_url:
        logger.warning(f"  SKIP: Cannot derive HTML URL from {source_url}")
        return False

    logger.info(f"  HTML URL: {html_url}")

    if dry_run:
        logger.info("  DRY RUN: Would fetch and extract")
        return True

    result = fetch_and_parse(html_url)

    if not result and celex and celex not in CONSOLIDATED_CELEX_OVERRIDES:
        fallback_url = source_url_to_html_url(source_url)
        if fallback_url and fallback_url != html_url:
            logger.info(f"  Trying fallback URL: {fallback_url}")
            result = fetch_and_parse(fallback_url)

    if not result:
        return False

    parsed_title, body = result
    final_title = parsed_title or display

    header = f"# {final_title}\n\n"
    if number:
        header += f"**Number:** {number}\n\n"
    header += f"**Source:** [{source_url}]({source_url})\n\n"
    header += "---\n\n"

    markdown = header + body + "\n"

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(markdown, encoding="utf-8")
    logger.info(f"  Saved: {out_path.name} ({len(markdown):,} chars)")
    return True


def main():
    parser = argparse.ArgumentParser(
        description="Fetch EU regulation full text from EUR-Lex")
    parser.add_argument("--id", default="",
                        help="Process a specific regulation by ID")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would be done without fetching")
    parser.add_argument("--force", action="store_true",
                        help="Re-fetch even if fulltext exists")
    args = parser.parse_args()

    entries = load_regulation_entries(doc_id=args.id)
    if not entries:
        logger.info("No EUR-Lex regulation entries found.")
        return

    logger.info(f"Found {len(entries)} EUR-Lex regulations to process")

    success = 0
    skipped = 0
    failed = 0

    for entry in entries:
        try:
            ok = process_regulation(entry, dry_run=args.dry_run,
                                    force=args.force)
            if ok:
                success += 1
            else:
                skipped += 1
        except Exception as e:
            logger.error(f"  EXCEPTION: {e}")
            failed += 1

        if not args.dry_run:
            time.sleep(2)

    logger.info(
        f"\nSummary: {success} fetched, {skipped} skipped, "
        f"{failed} failed (total: {len(entries)})"
    )


if __name__ == "__main__":
    main()
