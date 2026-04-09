#!/usr/bin/env python3
"""Automated full-text acquisition for regulatory knowledge base documents.

Level 2 automation: Fetch PDFs from source URLs, extract text using PyMuPDF (fitz),
and save as markdown files in the knowledge base.

Supports:
  - FDA guidance documents (PDF download from fda.gov)
  - MDCG guidance (PDF from health.ec.europa.eu)
  - Any document with a direct PDF source_url

Usage:
    python scripts/fetch_fulltext.py --framework fda --type guidance [--dry-run]
    python scripts/fetch_fulltext.py --id fda-cybersecurity-premarket-2026
    python scripts/fetch_fulltext.py --all --dry-run
"""

import argparse
import json
import logging
import os
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
    import fitz  # PyMuPDF
except ImportError:
    fitz = None
    logger.warning("PyMuPDF (fitz) not installed. PDF extraction will be unavailable.")

try:
    from curl_cffi import requests as cffi_requests
except ImportError:
    cffi_requests = None
    logger.warning("curl-cffi not installed. Akamai-protected sites may fail. pip install curl-cffi")

KNOWLEDGE_ROOT = Path(__file__).parent.parent
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/125.0.0.0 Safari/537.36"
)
REQUEST_HEADERS = {
    "User-Agent": USER_AGENT,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
}
MAX_PDF_SIZE = 50 * 1024 * 1024  # 50 MB limit


class PDFExtractor:
    """Extract text from PDF using PyMuPDF."""

    @staticmethod
    def extract_text(pdf_bytes: bytes) -> str:
        if fitz is None:
            raise RuntimeError("PyMuPDF not installed")
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        pages = []
        for i, page in enumerate(doc):
            text = page.get_text("text")
            if text.strip():
                pages.append(f"<!-- Page {i + 1} -->\n{text.strip()}")
        doc.close()
        return "\n\n---\n\n".join(pages)


KNOWN_PDF_URLS = {
    "fda-cybersecurity-premarket-2026": "https://www.fda.gov/media/119933/download",
    "fda-postmarket-cybersecurity-2016": "https://www.fda.gov/media/95862/download",
    "fda-remanufacturing-2024": "https://www.fda.gov/media/150141/download",
}


class FDAFetcher:
    """Fetch FDA guidance documents using curl-cffi to bypass Akamai bot detection."""

    FDA_GUIDANCE_BASE = "https://www.fda.gov/regulatory-information/search-fda-guidance-documents/"
    FDA_MEDIA_PATTERN = re.compile(r"https://www\.fda\.gov/media/(\d+)/download")
    IMPERSONATE = "chrome124"

    @staticmethod
    def _cffi_get(url: str, timeout: int = 30, **kwargs) -> Optional[object]:
        """Use curl-cffi with Chrome TLS impersonation, bypassing proxy for FDA.
        Akamai bot detection blocks requests from proxy/VPN IPs.
        """
        if cffi_requests is not None:
            saved = {k: os.environ.pop(k, None) for k in ("http_proxy", "https_proxy", "HTTP_PROXY", "HTTPS_PROXY", "all_proxy", "ALL_PROXY")}
            try:
                session = cffi_requests.Session(impersonate=FDAFetcher.IMPERSONATE)
                return session.get(url, timeout=timeout, allow_redirects=True, **kwargs)
            finally:
                for k, v in saved.items():
                    if v is not None:
                        os.environ[k] = v
        return requests.get(url, headers=REQUEST_HEADERS, timeout=timeout, allow_redirects=True, **kwargs)

    @staticmethod
    def discover_pdf_url(source_url: str) -> Optional[str]:
        """Try to discover the PDF download URL from an FDA guidance page."""
        try:
            resp = FDAFetcher._cffi_get(source_url, timeout=30)
            resp.raise_for_status()
            content_type = resp.headers.get("content-type", "")
            if "pdf" in content_type.lower():
                return source_url

            text = resp.text
            pdf_links = re.findall(
                r'href=["\']?(https://www\.fda\.gov/media/\d+/download)["\']?',
                text,
            )
            if pdf_links:
                return pdf_links[0]

            media_links = re.findall(
                r'href=["\']?(/media/\d+/download)["\']?',
                text,
            )
            if media_links:
                return f"https://www.fda.gov{media_links[0]}"

        except Exception as e:
            logger.warning(f"  Failed to discover PDF URL from {source_url}: {e}")
        return None

    @staticmethod
    def fetch_pdf(pdf_url: str, source_url: str = "") -> Optional[bytes]:
        """Fetch PDF using curl-cffi with Chrome TLS impersonation."""
        try:
            resp = FDAFetcher._cffi_get(pdf_url, timeout=120)
            resp.raise_for_status()

            content = resp.content
            if len(content) > MAX_PDF_SIZE:
                logger.warning(f"  PDF too large: {len(content) / 1024 / 1024:.1f} MB")
                return None

            content_type = resp.headers.get("content-type", "").lower()
            if "html" in content_type and len(content) < 20000:
                body = content.decode("utf-8", errors="replace")
                if "Access Denied" in body or "Pardon Our" in body or "apology" in body:
                    logger.warning(f"  Blocked by Akamai (response contains block page)")
                    return None

            return content
        except Exception as e:
            logger.warning(f"  Failed to fetch PDF from {pdf_url}: {e}")
            return None


class GenericFetcher:
    """Generic fetcher that handles direct PDF URLs and HTML pages."""

    @staticmethod
    def fetch(source_url: str) -> Optional[tuple[str, bytes]]:
        """Returns (content_type, data) or None."""
        try:
            resp = requests.get(
                source_url,
                headers=REQUEST_HEADERS,
                timeout=30,
                allow_redirects=True,
            )
            resp.raise_for_status()
            content_type = resp.headers.get("content-type", "").lower()
            if "pdf" in content_type:
                return ("pdf", resp.content)
            if "html" in content_type:
                return ("html", resp.content)
            return (content_type, resp.content)
        except Exception as e:
            logger.warning(f"  Failed to fetch {source_url}: {e}")
            return None


def load_entries(framework: str = "", doc_type: str = "", doc_id: str = "") -> list[dict]:
    """Load document entries from _index.json files."""
    entries = []

    framework_dirs = {}
    for d in KNOWLEDGE_ROOT.iterdir():
        if d.is_dir() and not d.name.startswith(".") and not d.name == "scripts":
            framework_dirs[d.name] = d

    for fw_id, fw_path in framework_dirs.items():
        if framework and fw_id != framework:
            continue

        for type_dir in fw_path.iterdir():
            if not type_dir.is_dir():
                if type_dir.name == "_index.json" and fw_id == "_shared":
                    try:
                        with open(type_dir, "r", encoding="utf-8") as f:
                            data = json.load(f)
                        for entry in data.get("entries", []):
                            entry["_framework"] = fw_id
                            entry["_type"] = "standards"
                            entries.append(entry)
                    except Exception:
                        pass
                continue

            t_id = type_dir.name
            if doc_type and t_id != doc_type:
                continue

            index_file = type_dir / "_index.json"
            if not index_file.exists():
                continue

            try:
                with open(index_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
            except Exception as e:
                logger.warning(f"Failed to load {index_file}: {e}")
                continue

            for entry in data.get("entries", []):
                entry["_framework"] = fw_id
                entry["_type"] = t_id
                if doc_id and entry.get("id") != doc_id:
                    continue
                entries.append(entry)

    return entries


def get_fulltext_path(entry: dict) -> Path:
    """Get the fulltext markdown file path for an entry."""
    fw = entry["_framework"]
    tp = entry["_type"]
    slug = entry.get("slug", "")
    eid = entry.get("id", "")
    filename = slug or re.sub(r'[^\w\-.]', '_', eid)
    return KNOWLEDGE_ROOT / fw / tp / "fulltext" / f"{filename}.md"


def fulltext_exists(entry: dict) -> bool:
    return get_fulltext_path(entry).exists()


def process_entry(entry: dict, dry_run: bool = False) -> bool:
    """Process a single entry: discover PDF, download, extract, save."""
    title = entry.get("title", {})
    if isinstance(title, dict):
        display = title.get("en", "") or title.get("zh", "")
    else:
        display = str(title)
    eid = entry.get("id", "")
    source_url = entry.get("source_url", "")
    fw = entry["_framework"]

    logger.info(f"Processing: {eid} - {display[:60]}")

    if not source_url:
        logger.warning(f"  SKIP: No source_url")
        return False

    if fulltext_exists(entry):
        logger.info(f"  SKIP: Fulltext already exists")
        return False

    pdf_url = KNOWN_PDF_URLS.get(eid)
    if pdf_url:
        logger.info(f"  Using known PDF URL")
    elif fw == "fda" or "fda.gov" in source_url:
        if source_url.endswith("/download"):
            pdf_url = source_url
        else:
            logger.info(f"  Discovering PDF URL from FDA page...")
            pdf_url = FDAFetcher.discover_pdf_url(source_url)
    elif source_url.lower().endswith(".pdf"):
        pdf_url = source_url
    else:
        result = GenericFetcher.fetch(source_url)
        if result and result[0] == "pdf":
            pdf_url = source_url

    if not pdf_url:
        logger.warning(f"  SKIP: Could not find PDF URL")
        return False

    logger.info(f"  PDF URL: {pdf_url}")

    if dry_run:
        logger.info(f"  DRY RUN: Would download and extract")
        return True

    if fitz is None:
        logger.error(f"  ERROR: PyMuPDF not installed, cannot extract text")
        return False

    logger.info(f"  Downloading PDF...")
    pdf_bytes = FDAFetcher.fetch_pdf(pdf_url, source_url=source_url)
    if not pdf_bytes:
        return False

    logger.info(f"  Extracting text ({len(pdf_bytes) / 1024:.1f} KB)...")
    try:
        text = PDFExtractor.extract_text(pdf_bytes)
    except Exception as e:
        logger.error(f"  ERROR extracting text: {e}")
        return False

    if not text.strip():
        logger.warning(f"  SKIP: Extracted text is empty (scanned PDF?)")
        return False

    markdown = f"# {display}\n\n"
    markdown += f"**Source:** [{source_url}]({source_url})\n\n"
    if entry.get("published_date"):
        markdown += f"**Published:** {entry['published_date']}\n\n"
    markdown += f"---\n\n{text}\n"

    out_path = get_fulltext_path(entry)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(markdown, encoding="utf-8")
    logger.info(f"  Saved: {out_path} ({len(markdown)} chars)")
    return True


def main():
    parser = argparse.ArgumentParser(description="Fetch fulltext for knowledge base documents")
    parser.add_argument("--framework", "-f", default="", help="Filter by framework (fda, eu_mdr, nmpa)")
    parser.add_argument("--type", "-t", default="", help="Filter by document type (guidance, regulations)")
    parser.add_argument("--id", default="", help="Process a specific document by ID")
    parser.add_argument("--all", action="store_true", help="Process all documents")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be done without fetching")
    parser.add_argument("--force", action="store_true", help="Re-fetch even if fulltext exists")
    args = parser.parse_args()

    if not args.framework and not args.id and not args.all:
        parser.print_help()
        print("\nExamples:")
        print("  python scripts/fetch_fulltext.py --framework fda --type guidance")
        print("  python scripts/fetch_fulltext.py --id fda-cybersecurity-premarket-2026")
        print("  python scripts/fetch_fulltext.py --all --dry-run")
        return

    entries = load_entries(
        framework=args.framework,
        doc_type=args.type,
        doc_id=args.id,
    )

    if not entries:
        logger.info("No entries found matching criteria.")
        return

    logger.info(f"Found {len(entries)} entries to process")

    success = 0
    skipped = 0
    failed = 0

    for entry in entries:
        if not args.force and fulltext_exists(entry):
            skipped += 1
            continue

        try:
            ok = process_entry(entry, dry_run=args.dry_run)
            if ok:
                success += 1
            else:
                skipped += 1
        except Exception as e:
            logger.error(f"  EXCEPTION: {e}")
            failed += 1

        time.sleep(1)

    logger.info(f"\nSummary: {success} processed, {skipped} skipped, {failed} failed (total: {len(entries)})")


if __name__ == "__main__":
    main()
