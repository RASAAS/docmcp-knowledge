#!/usr/bin/env python3
"""
WordPress to Markdown Migration Script
Migrates content from reguverse.com/documentation (BetterDocs) to docmcp-knowledge repo structure.

BetterDocs uses hierarchical parent-child relationships (not doc_category taxonomy).
Path mapping is derived from the WordPress link URL path segments.

Usage:
    python scripts/migrate_wordpress.py --site https://reguverse.com --output ./
    python scripts/migrate_wordpress.py --site https://reguverse.com --filter nmpa --output ./
    python scripts/migrate_wordpress.py --site https://reguverse.com --list-structure
    python scripts/migrate_wordpress.py --site https://reguverse.com --dry-run
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from urllib.parse import unquote

try:
    import requests
except ImportError:
    print("ERROR: requests not installed. Run: pip install requests")
    sys.exit(1)

try:
    import html2text
except ImportError:
    print("ERROR: html2text not installed. Run: pip install html2text")
    sys.exit(1)

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml not installed. Run: pip install pyyaml")
    sys.exit(1)


# ---------------------------------------------------------------------------
# URL path segment -> repo directory mapping (ordered, most-specific first)
# Based on actual reguverse.com/documentation URL structure
# ---------------------------------------------------------------------------
URL_PATH_MAP = [
    # EU MDR
    ("eu-mdr-indexing/mdcg",                                           "eu_mdr/mdcg",           "eu_mdr"),
    ("eu-mdr-indexing/team-nb",                                        "eu_mdr/team_nb",        "eu_mdr"),
    ("eu-mdr-indexing/eu-ivdr",                                        "eu_mdr/ivdr",           "eu_mdr"),
    ("eu-mdr-indexing/eu-mdr-classification",                          "eu_mdr/classification", "eu_mdr"),
    ("eu-mdr-indexing/harmonised-standards",                           "eu_mdr/standards",      "eu_mdr"),
    ("eu-mdr-indexing/clinical-evaluation",                            "eu_mdr/mdcg",           "eu_mdr"),
    ("eu-mdr-indexing",                                                "eu_mdr",                "eu_mdr"),
    # NMPA
    ("nmpa-regulations-index/pre-market-submission/guidance-document", "nmpa/guidance",         "nmpa"),
    ("nmpa-regulations-index/pre-market-submission/review-points",     "nmpa/guidance",         "nmpa"),
    ("nmpa-regulations-index/pre-market-submission/high-end",          "nmpa/guidance",         "nmpa"),
    ("nmpa-regulations-index/pre-market-submission/notice",            "nmpa/regulations",      "nmpa"),
    ("nmpa-regulations-index/pre-market-submission",                   "nmpa/guidance",         "nmpa"),
    ("nmpa-regulations-index/qms-gmp",                                 "nmpa/regulations",      "nmpa"),
    ("nmpa-regulations-index/regulations",                             "nmpa/regulations",      "nmpa"),
    ("nmpa-regulations-index/classification",                          "nmpa/classification",   "nmpa"),
    ("nmpa-regulations-index",                                         "nmpa/guidance",         "nmpa"),
    # FDA
    ("fda-indexing/guidance",                                          "fda/guidance",          "fda"),
    ("fda-indexing/regulations",                                       "fda/regulations",       "fda"),
    ("fda-indexing/standards",                                         "fda/standards",         "fda"),
    ("fda-indexing",                                                   "fda/guidance",          "fda"),
    # Clinical evaluation / SOTA
    ("clinical-evaluation",                                            "eu_mdr/mdcg",           "eu_mdr"),
    ("open-sota",                                                      "_shared",               "shared"),
    # QMS
    ("qms",                                                            "_shared",               "shared"),
]

# Minimum content length to consider a doc worth migrating (chars)
MIN_CONTENT_LENGTH = 100


class WordPressMigrator:
    def __init__(self, site_url: str, output_dir: str, delay: float = 0.3,
                 dry_run: bool = False, url_filter: Optional[str] = None):
        self.site_url = site_url.rstrip("/")
        self.output_dir = Path(output_dir)
        self.delay = delay
        self.dry_run = dry_run
        self.url_filter = url_filter
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "docmcp-knowledge-migrator/1.0"
        })
        self.h2t = html2text.HTML2Text()
        self.h2t.ignore_links = False
        self.h2t.ignore_images = False
        self.h2t.body_width = 0
        self.h2t.protect_links = True
        self.h2t.unicode_snob = True
        self.stats: Dict[str, int] = {
            "total": 0, "success": 0, "skipped": 0, "error": 0
        }

    def api_get(self, endpoint: str, params: Optional[dict] = None) -> Optional[object]:
        url = f"{self.site_url}/wp-json/wp/v2/{endpoint}"
        try:
            resp = self.session.get(url, params=params, timeout=30)
            if resp.status_code == 400:
                return None
            resp.raise_for_status()
            return resp.json()
        except requests.RequestException as e:
            print(f"  ERROR fetching {url}: {e}")
            return None

    def get_all_docs(self) -> List[dict]:
        """Fetch all published docs with pagination."""
        all_docs = []
        page = 1
        params: dict = {
            "per_page": 100,
            "status": "publish",
            "_fields": "id,title,slug,link,content,parent,modified",
        }
        while True:
            params["page"] = page
            docs = self.api_get("docs", params)
            if not docs or not isinstance(docs, list):
                break
            all_docs.extend(docs)
            print(f"  Fetched page {page}: {len(docs)} docs (total: {len(all_docs)})")
            if len(docs) < 100:
                break
            page += 1
            time.sleep(self.delay)
        return all_docs

    def detect_output_path(self, link: str) -> Tuple[str, str]:
        """
        Derive repo output path and regulation from WordPress link URL.
        Returns (output_path, regulation).
        """
        link_decoded = unquote(link).lower()
        match = re.search(r"/documentation/(.+?)/?$", link_decoded)
        if not match:
            return "_shared", "shared"
        path_part = match.group(1)

        for url_segment, repo_path, regulation in URL_PATH_MAP:
            if path_part.startswith(url_segment):
                return repo_path, regulation

        return "_shared", "shared"

    def html_to_markdown(self, html: str) -> str:
        """Convert HTML content to clean Markdown."""
        if not html:
            return ""
        md = self.h2t.handle(html)
        md = re.sub(r"\n{3,}", "\n\n", md)
        md = re.sub(r"\[/?[a-z_]+[^\]]*\]", "", md)
        md = md.replace("&hellip;", "...").replace("&amp;", "&")
        md = md.replace("&#8211;", "-").replace("&#8212;", "--")
        md = md.replace("&#038;", "&").replace("&nbsp;", " ")
        return md.strip()

    def clean_title(self, title_raw: str) -> str:
        """Clean HTML entities from title."""
        t = re.sub(r"<[^>]+>", "", title_raw)
        t = t.replace("&amp;", "&").replace("&#8211;", "-")
        t = t.replace("&#038;", "&").replace("&hellip;", "...")
        t = t.replace("&#8212;", "--").replace("&nbsp;", " ")
        return t.strip()

    def slugify(self, text: str) -> str:
        """Convert text to URL-safe slug."""
        text = text.lower()
        text = re.sub(r"[^\w\s-]", "", text)
        text = re.sub(r"[\s_]+", "-", text)
        text = re.sub(r"-+", "-", text)
        return text.strip("-")[:80]

    def build_front_matter(self, doc: dict, output_path: str, regulation: str) -> dict:
        """Build YAML front matter metadata from WordPress doc."""
        title_clean = self.clean_title(doc.get("title", {}).get("rendered", ""))

        doc_number = ""
        num_match = re.search(
            r"(CMDE-\d{4}-\d+|\d{4}/\d+/EU|21 CFR \d+|MDCG \d{4}-\d+|YY/T \d+[\.\d]*|GB \d+[\.\d]*)",
            title_clean
        )
        if num_match:
            doc_number = num_match.group(1)

        modified = doc.get("modified", "")[:10] if doc.get("modified") else ""
        doc_id = f"{regulation}-{self.slugify(title_clean)[:60]}"

        fm: dict = {
            "id": doc_id,
            "title": {"zh": title_clean, "en": ""},
            "regulation": regulation,
            "category": output_path,
            "status": "active",
            "source_url": doc.get("link", ""),
            "source_url_verified": datetime.now().strftime("%Y-%m-%d"),
            "source_url_status": "migrated",
            "source_format": "html",
            "translation": "original",
            "last_verified": datetime.now().strftime("%Y-%m-%d"),
            "contributor": "RASAAS",
            "migrated_from": "wordpress",
            "wordpress_id": doc.get("id"),
        }
        if doc_number:
            fm["document_number"] = doc_number
        if modified:
            fm["effective_date"] = modified

        return fm

    def save_document(self, doc: dict) -> Tuple[Optional[Path], Optional[dict]]:
        """Save a single WordPress doc as Markdown files. Returns (zh_file, fm)."""
        link = doc.get("link", "")
        output_path, regulation = self.detect_output_path(link)

        title_clean = self.clean_title(doc.get("title", {}).get("rendered", ""))
        slug = doc.get("slug") or self.slugify(title_clean)

        content_html = doc.get("content", {}).get("rendered", "")
        content_md = self.html_to_markdown(content_html)

        # Skip near-empty docs (likely category index pages)
        if len(content_md) < MIN_CONTENT_LENGTH:
            return None, None

        fm = self.build_front_matter(doc, output_path, regulation)
        fm_str = yaml.dump(fm, allow_unicode=True, default_flow_style=False, sort_keys=False)

        out_dir = self.output_dir / output_path
        zh_file = out_dir / f"{slug}.zh.md"
        en_file = out_dir / f"{slug}.en.md"

        if not self.dry_run:
            out_dir.mkdir(parents=True, exist_ok=True)
            with open(zh_file, "w", encoding="utf-8") as f:
                f.write(f"---\n{fm_str}---\n\n")
                f.write(f"# {title_clean}\n\n")
                f.write(content_md)
                f.write("\n")

            if not en_file.exists():
                fm_en = fm.copy()
                fm_en["translation"] = "ai-assisted"
                fm_en["title"] = {"zh": title_clean, "en": f"[Translation needed] {title_clean}"}
                fm_en_str = yaml.dump(
                    fm_en, allow_unicode=True, default_flow_style=False, sort_keys=False
                )
                with open(en_file, "w", encoding="utf-8") as f:
                    f.write(f"---\n{fm_en_str}---\n\n")
                    f.write(f"# [Translation needed] {title_clean}\n\n")
                    f.write("> This document requires English translation. "
                            "See CONTRIBUTING.md for translation guidelines.\n")

        return zh_file, fm

    def update_index(self, output_path: str, entries: List[dict]) -> None:
        """Update or create _index.json for a directory."""
        index_file = self.output_dir / output_path / "_index.json"
        existing: List[dict] = []
        if index_file.exists():
            with open(index_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                existing = data.get("entries", [])

        existing_ids = {e["id"] for e in existing}
        for entry in entries:
            if entry["id"] not in existing_ids:
                existing.append(entry)

        index_data = {
            "category": output_path,
            "last_updated": datetime.now().strftime("%Y-%m-%d"),
            "count": len(existing),
            "entries": existing,
        }
        with open(index_file, "w", encoding="utf-8") as f:
            json.dump(index_data, f, ensure_ascii=False, indent=2)

    def list_structure(self) -> None:
        """Fetch all docs and show how they would be mapped."""
        print("\nFetching all docs to analyze structure...\n")
        docs = self.get_all_docs()
        print(f"\nTotal docs: {len(docs)}\n")

        path_counts: Dict[str, int] = {}
        for doc in docs:
            link = doc.get("link", "")
            output_path, _ = self.detect_output_path(link)
            path_counts[output_path] = path_counts.get(output_path, 0) + 1

        print("Mapping summary:")
        for path, count in sorted(path_counts.items()):
            print(f"  {path:<50} {count:3d} docs")
        print(f"\n  Total: {len(docs)} docs across {len(path_counts)} directories")

    def migrate(self, url_filter: Optional[str] = None) -> None:
        """Main migration entry point."""
        mode = "[DRY RUN] " if self.dry_run else ""
        print(f"\n{mode}Starting migration from {self.site_url}")
        print(f"Output directory: {self.output_dir}")
        if url_filter:
            print(f"URL filter: {url_filter}")
        print()

        docs = self.get_all_docs()

        if url_filter:
            docs = [d for d in docs if url_filter.lower() in d.get("link", "").lower()]
            print(f"After filter: {len(docs)} docs match '{url_filter}'")

        print(f"\nTotal docs to process: {len(docs)}")

        path_entries: Dict[str, List[dict]] = {}

        for i, doc in enumerate(docs, 1):
            self.stats["total"] += 1
            title = self.clean_title(doc.get("title", {}).get("rendered", ""))
            link = doc.get("link", "")
            output_path, _ = self.detect_output_path(link)
            print(f"[{i:3d}/{len(docs)}] {title[:65]}")

            try:
                zh_file, fm = self.save_document(doc)
                if fm is None:
                    self.stats["skipped"] += 1
                    print(f"        SKIP (empty content)")
                    continue

                if output_path not in path_entries:
                    path_entries[output_path] = []
                path_entries[output_path].append({
                    "id": fm["id"],
                    "title": fm["title"],
                    "status": fm["status"],
                    "source_url": fm["source_url"],
                    "source_url_verified": fm["source_url_verified"],
                    "effective_date": fm.get("effective_date", ""),
                })

                self.stats["success"] += 1
                if self.dry_run:
                    print(f"        -> [DRY] {output_path}/{doc.get('slug', '')}.zh.md")
                else:
                    print(f"        -> {zh_file.relative_to(self.output_dir)}")
            except Exception as e:
                self.stats["error"] += 1
                print(f"        ERROR: {e}")

            time.sleep(self.delay)

        if not self.dry_run:
            print("\nUpdating _index.json files...")
            for path, entries in path_entries.items():
                self.update_index(path, entries)
                print(f"  Updated {path}/_index.json ({len(entries)} entries)")

        print(f"\n{'='*50}")
        print(f"Migration {'(DRY RUN) ' if self.dry_run else ''}complete:")
        print(f"  Total:   {self.stats['total']}")
        print(f"  Success: {self.stats['success']}")
        print(f"  Skipped: {self.stats['skipped']}")
        print(f"  Errors:  {self.stats['error']}")
        print(f"{'='*50}")


def main():
    parser = argparse.ArgumentParser(description="Migrate WordPress docs to Markdown")
    parser.add_argument("--site", default="https://reguverse.com",
                        help="WordPress site URL (default: https://reguverse.com)")
    parser.add_argument("--output", default=".",
                        help="Output directory (default: current directory)")
    parser.add_argument("--filter", default=None,
                        help="Filter docs by URL substring (e.g. 'nmpa', 'eu-mdr')")
    parser.add_argument("--list-structure", action="store_true",
                        help="Show URL->path mapping without migrating")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would be migrated without writing files")
    parser.add_argument("--delay", type=float, default=0.3,
                        help="Delay between API requests in seconds (default: 0.3)")
    args = parser.parse_args()

    migrator = WordPressMigrator(
        args.site, args.output, args.delay,
        dry_run=args.dry_run,
        url_filter=args.filter,
    )

    if args.list_structure:
        migrator.list_structure()
        return

    migrator.migrate(url_filter=args.filter)


if __name__ == "__main__":
    main()
