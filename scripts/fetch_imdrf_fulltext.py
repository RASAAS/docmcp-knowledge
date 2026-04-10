"""Fetch IMDRF technical document full-text from DOCX downloads.

IMDRF provides both PDF and DOCX for most technical documents.
DOCX -> Markdown (via mammoth) gives much cleaner output than PDF extraction.

Usage:
    python scripts/fetch_imdrf_fulltext.py
"""

import json
import re
import sys
import tempfile
import time
from pathlib import Path

import mammoth
import requests
from html2text import HTML2Text

INDEX_PATH = Path(__file__).resolve().parent.parent / "_shared" / "imdrf" / "_index.json"
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "_shared" / "imdrf" / "fulltext"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
}


def fetch_docx_url(page_url: str) -> tuple[str, str]:
    """Scrape the IMDRF document page to find DOCX and PDF download links."""
    try:
        resp = requests.get(page_url, headers=HEADERS, timeout=30)
        resp.raise_for_status()
        html = resp.text
    except Exception as e:
        print(f"  [WARN] Failed to fetch page {page_url}: {e}")
        return "", ""

    docx_match = re.search(r'href=["\']?([^"\'>\s]+\.docx)["\']?', html)
    pdf_match = re.search(r'href=["\']?([^"\'>\s]+\.pdf)["\']?', html)

    docx_url = docx_match.group(1) if docx_match else ""
    pdf_url = pdf_match.group(1) if pdf_match else ""

    if docx_url and not docx_url.startswith("http"):
        docx_url = "https://www.imdrf.org" + docx_url
    if pdf_url and not pdf_url.startswith("http"):
        pdf_url = "https://www.imdrf.org" + pdf_url

    return docx_url, pdf_url


def docx_to_markdown(docx_path: str) -> str:
    """Convert DOCX to Markdown via mammoth (DOCX -> HTML) + html2text (HTML -> MD)."""
    with open(docx_path, "rb") as f:
        result = mammoth.convert_to_html(f)

    html = result.value

    h2t = HTML2Text()
    h2t.body_width = 0
    h2t.unicode_snob = True
    h2t.protect_links = True
    h2t.wrap_links = False
    h2t.single_line_break = False

    md = h2t.handle(html)
    md = _clean_markdown(md)
    return md


def _clean_markdown(text: str) -> str:
    """Post-process the converted markdown."""
    text = re.sub(r'\n{4,}', '\n\n\n', text)
    text = re.sub(r'^\s*\n', '\n', text, flags=re.MULTILINE)
    text = re.sub(r'!\[.*?\]\(.*?\)', '', text)
    lines = text.split('\n')
    cleaned = []
    for line in lines:
        stripped = line.strip()
        if stripped in ('', '---'):
            cleaned.append(line)
            continue
        if re.match(r'^#+\s', stripped):
            cleaned.append(line)
            continue
        cleaned.append(line)

    text = '\n'.join(cleaned)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip() + '\n'


def process_entry(entry: dict) -> bool:
    """Process a single IMDRF index entry: download DOCX and convert to Markdown."""
    doc_id = entry["id"]
    title = entry["title"]
    title_en = title.get("en", "") if isinstance(title, dict) else str(title)
    source_url = entry.get("source_url", "")
    doc_number = entry.get("document_number", "")

    output_path = OUTPUT_DIR / f"{doc_id}.md"
    if output_path.exists():
        size = output_path.stat().st_size
        if size > 500:
            print(f"  [SKIP] {doc_id} -- already exists ({size} bytes)")
            return False

    print(f"  Processing: {doc_id}")
    print(f"    Title: {title_en}")
    print(f"    URL: {source_url}")

    if not source_url:
        print(f"    [WARN] No source URL")
        return False

    docx_url, pdf_url = fetch_docx_url(source_url)
    print(f"    DOCX: {docx_url or '(none)'}")
    print(f"    PDF:  {pdf_url or '(none)'}")

    if not docx_url:
        print(f"    [WARN] No DOCX link found, skipping")
        return False

    try:
        print(f"    Downloading DOCX...")
        resp = requests.get(docx_url, headers=HEADERS, timeout=60)
        resp.raise_for_status()
    except Exception as e:
        print(f"    [ERROR] Download failed: {e}")
        return False

    with tempfile.NamedTemporaryFile(suffix=".docx", delete=False) as tmp:
        tmp.write(resp.content)
        tmp_path = tmp.name

    try:
        print(f"    Converting to Markdown...")
        md = docx_to_markdown(tmp_path)

        header = f"# {title_en}\n\n"
        if doc_number:
            header += f"**Document Number**: {doc_number}\n\n"
        header += f"**Source**: [{source_url}]({source_url})\n\n---\n\n"

        full_md = header + md
        output_path.write_text(full_md, encoding="utf-8")
        print(f"    [OK] Written {len(full_md)} chars -> {output_path.name}")
        return True
    except Exception as e:
        print(f"    [ERROR] Conversion failed: {e}")
        return False
    finally:
        Path(tmp_path).unlink(missing_ok=True)


def main():
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        index = json.load(f)

    entries = index.get("entries", [])
    print(f"IMDRF Index: {len(entries)} entries")
    print(f"Output dir: {OUTPUT_DIR}")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    success = 0
    skipped = 0
    failed = 0

    for entry in entries:
        result = process_entry(entry)
        if result is True:
            success += 1
            time.sleep(2)
        elif result is False:
            if (OUTPUT_DIR / f"{entry['id']}.md").exists():
                skipped += 1
            else:
                failed += 1

    print(f"\nDone: {success} converted, {skipped} skipped, {failed} failed")


if __name__ == "__main__":
    main()
