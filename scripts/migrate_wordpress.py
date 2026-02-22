#!/usr/bin/env python3
"""
WordPress to Markdown Migration Script
Migrates content from reguverse.com/documentation (BetterDocs) to docmcp-knowledge repo structure.

Usage:
    python scripts/migrate_wordpress.py --site https://reguverse.com --output ./
    python scripts/migrate_wordpress.py --site https://reguverse.com --category nmpa --output ./nmpa/guidance/
    python scripts/migrate_wordpress.py --site https://reguverse.com --list-categories
"""

import argparse
import json
import os
import re
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
# Category mapping: WordPress category slug -> repo path
# ---------------------------------------------------------------------------
CATEGORY_MAP = {
    "eu-mdr": "eu_mdr",
    "eu-mdr-compliance": "eu_mdr",
    "mdcg": "eu_mdr/mdcg",
    "team-nb": "eu_mdr/team_nb",
    "nmpa": "nmpa/guidance",
    "nmpa-regulations": "nmpa/regulations",
    "nmpa-guidance": "nmpa/guidance",
    "nmpa-classification": "nmpa/classification",
    "fda": "fda/guidance",
    "fda-regulations": "fda/regulations",
    "clinical-evaluation": "eu_mdr/mdcg",
    "qms": "_shared",
    "standards": "_shared/standards",
    "sota": "_shared",
}

# Regulation detection by category path
REGULATION_MAP = {
    "eu_mdr": "eu_mdr",
    "fda": "fda",
    "nmpa": "nmpa",
    "_shared": "shared",
}


class WordPressMigrator:
    def __init__(self, site_url: str, output_dir: str, delay: float = 0.5):
        self.site_url = site_url.rstrip("/")
        self.output_dir = Path(output_dir)
        self.delay = delay
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "docmcp-knowledge-migrator/1.0"
        })
        self.h2t = html2text.HTML2Text()
        self.h2t.ignore_links = False
        self.h2t.ignore_images = False
        self.h2t.body_width = 0  # No line wrapping
        self.h2t.protect_links = True
        self.stats = {"total": 0, "success": 0, "skipped": 0, "error": 0}

    def api_get(self, endpoint: str, params: dict = None) -> dict | list | None:
        url = f"{self.site_url}/wp-json/wp/v2/{endpoint}"
        try:
            resp = self.session.get(url, params=params, timeout=30)
            resp.raise_for_status()
            return resp.json()
        except requests.RequestException as e:
            print(f"  ERROR fetching {url}: {e}")
            return None

    def get_all_docs(self, category_slug: str = None) -> list:
        """Fetch all docs from WordPress REST API with pagination."""
        all_docs = []
        page = 1
        params = {"per_page": 100, "status": "publish"}
        if category_slug:
            # Get category ID first
            cats = self.api_get("doc_category", {"slug": category_slug})
            if cats and len(cats) > 0:
                params["doc_category"] = cats[0]["id"]

        while True:
            params["page"] = page
            docs = self.api_get("docs", params)
            if not docs:
                break
            all_docs.extend(docs)
            print(f"  Fetched page {page}: {len(docs)} docs (total: {len(all_docs)})")
            if len(docs) < 100:
                break
            page += 1
            time.sleep(self.delay)

        return all_docs

    def get_categories(self) -> list:
        """Fetch all doc categories."""
        return self.api_get("doc_category", {"per_page": 100}) or []

    def list_categories(self):
        """Print all available categories."""
        cats = self.get_categories()
        print(f"\nFound {len(cats)} categories:\n")
        for cat in cats:
            print(f"  [{cat['id']:4d}] {cat['slug']:<40} {cat['name']} ({cat['count']} docs)")

    def html_to_markdown(self, html: str) -> str:
        """Convert HTML content to clean Markdown."""
        md = self.h2t.handle(html)
        # Clean up excessive blank lines
        md = re.sub(r"\n{3,}", "\n\n", md)
        # Fix WordPress shortcodes that leaked through
        md = re.sub(r"\[/?[a-z_]+[^\]]*\]", "", md)
        return md.strip()

    def slugify(self, text: str) -> str:
        """Convert text to URL-safe slug."""
        text = text.lower()
        text = re.sub(r"[^\w\s-]", "", text)
        text = re.sub(r"[\s_]+", "-", text)
        text = re.sub(r"-+", "-", text)
        return text.strip("-")[:80]

    def detect_regulation(self, categories: list, slug: str) -> str:
        """Detect regulation from category slugs."""
        for cat_slug in categories:
            for key, reg in REGULATION_MAP.items():
                if key.replace("_", "-") in cat_slug or key in cat_slug:
                    return reg
        return "shared"

    def detect_output_path(self, categories: list) -> str:
        """Map WordPress categories to repo directory path."""
        for cat_slug in categories:
            if cat_slug in CATEGORY_MAP:
                return CATEGORY_MAP[cat_slug]
        # Fallback: use first category
        if categories:
            return CATEGORY_MAP.get(categories[0], "_shared")
        return "_shared"

    def build_front_matter(self, doc: dict, categories: list, output_path: str) -> dict:
        """Build YAML front matter metadata from WordPress doc."""
        regulation = self.detect_regulation(categories, doc.get("slug", ""))
        title_raw = doc.get("title", {}).get("rendered", "")
        title_clean = re.sub(r"<[^>]+>", "", title_raw)

        # Try to extract document number from title (e.g., CMDE-2022-9)
        doc_number = ""
        num_match = re.search(r"(CMDE-\d{4}-\d+|\d{4}/\d+/EU|21 CFR \d+)", title_clean)
        if num_match:
            doc_number = num_match.group(1)

        # Extract date from WordPress modified date
        modified = doc.get("modified", "")[:10] if doc.get("modified") else ""

        doc_id = f"{regulation}-{self.slugify(title_clean)[:60]}"

        fm = {
            "id": doc_id,
            "title": {"zh": title_clean, "en": ""},
            "regulation": regulation,
            "category": output_path,
            "status": "active",
            "source_url": doc.get("link", ""),
            "source_url_verified": datetime.now().strftime("%Y-%m-%d"),
            "source_url_status": "ok",
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

    def save_document(self, doc: dict, categories: list):
        """Save a single WordPress doc as Markdown files."""
        output_path = self.detect_output_path(categories)
        out_dir = self.output_dir / output_path
        out_dir.mkdir(parents=True, exist_ok=True)

        title_raw = doc.get("title", {}).get("rendered", "")
        title_clean = re.sub(r"<[^>]+>", "", title_raw)
        slug = doc.get("slug") or self.slugify(title_clean)

        content_html = doc.get("content", {}).get("rendered", "")
        content_md = self.html_to_markdown(content_html)

        fm = self.build_front_matter(doc, categories, output_path)
        fm_str = yaml.dump(fm, allow_unicode=True, default_flow_style=False, sort_keys=False)

        # Write Chinese version (original)
        zh_file = out_dir / f"{slug}.zh.md"
        with open(zh_file, "w", encoding="utf-8") as f:
            f.write(f"---\n{fm_str}---\n\n")
            f.write(f"# {title_clean}\n\n")
            f.write(content_md)
            f.write("\n")

        # Write English placeholder
        fm_en = fm.copy()
        fm_en["translation"] = "ai-assisted"
        fm_en["title"] = {"zh": title_clean, "en": f"[Translation needed] {title_clean}"}
        fm_en_str = yaml.dump(fm_en, allow_unicode=True, default_flow_style=False, sort_keys=False)
        en_file = out_dir / f"{slug}.en.md"
        if not en_file.exists():
            with open(en_file, "w", encoding="utf-8") as f:
                f.write(f"---\n{fm_en_str}---\n\n")
                f.write(f"# [Translation needed] {title_clean}\n\n")
                f.write("> This document requires English translation. "
                        "See CONTRIBUTING.md for translation guidelines.\n")

        return zh_file, fm

    def update_index(self, output_path: str, entries: list):
        """Update or create _index.json for a directory."""
        index_file = self.output_dir / output_path / "_index.json"
        existing = []
        if index_file.exists():
            with open(index_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                existing = data.get("entries", [])

        # Merge: update existing entries by id, append new ones
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

    def migrate(self, category_slug: str = None):
        """Main migration entry point."""
        print(f"\nStarting migration from {self.site_url}")
        print(f"Output directory: {self.output_dir}")
        if category_slug:
            print(f"Category filter: {category_slug}")
        print()

        docs = self.get_all_docs(category_slug)
        print(f"\nTotal docs to migrate: {len(docs)}")

        # Group by output path for index building
        path_entries: dict[str, list] = {}

        for i, doc in enumerate(docs, 1):
            self.stats["total"] += 1
            title = re.sub(r"<[^>]+>", "", doc.get("title", {}).get("rendered", ""))
            print(f"[{i:3d}/{len(docs)}] {title[:70]}")

            # Get category slugs for this doc
            cat_ids = doc.get("doc_category", [])
            cat_slugs = []
            if cat_ids:
                for cat_id in cat_ids:
                    cats = self.api_get(f"doc_category/{cat_id}")
                    if cats:
                        cat_slugs.append(cats.get("slug", ""))
                time.sleep(self.delay)

            try:
                zh_file, fm = self.save_document(doc, cat_slugs)
                output_path = fm["category"]

                # Collect for index
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
                print(f"        -> {zh_file.relative_to(self.output_dir)}")
            except Exception as e:
                self.stats["error"] += 1
                print(f"        ERROR: {e}")

            time.sleep(self.delay)

        # Update indexes
        print("\nUpdating _index.json files...")
        for path, entries in path_entries.items():
            self.update_index(path, entries)
            print(f"  Updated {path}/_index.json ({len(entries)} entries)")

        # Print summary
        print(f"\n{'='*50}")
        print(f"Migration complete:")
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
    parser.add_argument("--category", default=None,
                        help="Filter by category slug")
    parser.add_argument("--list-categories", action="store_true",
                        help="List all available categories and exit")
    parser.add_argument("--delay", type=float, default=0.5,
                        help="Delay between API requests in seconds (default: 0.5)")
    args = parser.parse_args()

    migrator = WordPressMigrator(args.site, args.output, args.delay)

    if args.list_categories:
        migrator.list_categories()
        return

    migrator.migrate(args.category)


if __name__ == "__main__":
    main()
