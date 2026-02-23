#!/usr/bin/env python3
"""
Migrate WordPress Posts (blog articles) to insights/ directory.

Fetches published posts from WordPress REST API and converts them to
structured Markdown files in insights/{year}/ subdirectories.

Usage:
    python scripts/migrate_posts.py --site https://reguverse.com --output .
    python scripts/migrate_posts.py --site https://reguverse.com --output . --dry-run
    python scripts/migrate_posts.py --site https://reguverse.com --list
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

# WordPress category slug -> insights subcategory
CATEGORY_MAP = {
    "nmpa-update": "nmpa-updates",
    "eu-mdr-update": "eu-mdr-updates",
    "fda-update": "fda-updates",
    "blog": "analysis",
    "regulatory-update": "regulatory-updates",
    "clinical-evaluation": "clinical-evaluation",
}

DEFAULT_SUBCATEGORY = "analysis"
MIN_CONTENT_LENGTH = 200


class PostsMigrator:
    def __init__(self, site_url: str, output_dir: str, delay: float = 0.3,
                 dry_run: bool = False):
        self.site_url = site_url.rstrip("/")
        self.output_dir = Path(output_dir)
        self.delay = delay
        self.dry_run = dry_run
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
        self._category_cache: Dict[int, str] = {}

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

    def get_all_posts(self) -> List[dict]:
        """Fetch all published posts with pagination."""
        all_posts = []
        page = 1
        params: dict = {
            "per_page": 100,
            "status": "publish",
            "_fields": "id,title,slug,link,content,excerpt,date,modified,categories,tags",
        }
        while True:
            params["page"] = page
            posts = self.api_get("posts", params)
            if not posts or not isinstance(posts, list):
                break
            all_posts.extend(posts)
            print(f"  Fetched page {page}: {len(posts)} posts (total: {len(all_posts)})")
            if len(posts) < 100:
                break
            page += 1
            time.sleep(self.delay)
        return all_posts

    def get_category_slug(self, cat_id: int) -> str:
        """Get category slug by ID (cached)."""
        if cat_id in self._category_cache:
            return self._category_cache[cat_id]
        cat = self.api_get(f"categories/{cat_id}")
        if cat and isinstance(cat, dict):
            slug = cat.get("slug", "")
            self._category_cache[cat_id] = slug
            return slug
        return ""

    def detect_subcategory(self, post: dict) -> str:
        """Detect insights subcategory from post categories."""
        cat_ids = post.get("categories", [])
        for cat_id in cat_ids:
            slug = self.get_category_slug(cat_id)
            if slug in CATEGORY_MAP:
                return CATEGORY_MAP[slug]
        return DEFAULT_SUBCATEGORY

    def html_to_markdown(self, html: str) -> str:
        if not html:
            return ""
        md = self.h2t.handle(html)
        md = re.sub(r"\n{3,}", "\n\n", md)
        md = md.replace("&hellip;", "...").replace("&amp;", "&")
        md = md.replace("&#8211;", "-").replace("&#8212;", "--")
        md = md.replace("&#038;", "&").replace("&nbsp;", " ")
        return md.strip()

    def clean_title(self, title_raw: str) -> str:
        t = re.sub(r"<[^>]+>", "", title_raw)
        t = t.replace("&amp;", "&").replace("&#8211;", "-")
        t = t.replace("&#038;", "&").replace("&hellip;", "...")
        t = t.replace("&#8212;", "--").replace("&nbsp;", " ")
        return t.strip()

    def slugify(self, text: str) -> str:
        text = text.lower()
        text = re.sub(r"[^\w\s-]", "", text)
        text = re.sub(r"[\s_]+", "-", text)
        text = re.sub(r"-+", "-", text)
        return text.strip("-")[:80]

    def save_post(self, post: dict) -> Tuple[Optional[Path], Optional[dict]]:
        """Save a single post as a Markdown file."""
        title_clean = self.clean_title(post.get("title", {}).get("rendered", ""))
        slug = post.get("slug") or self.slugify(title_clean)

        content_html = post.get("content", {}).get("rendered", "")
        content_md = self.html_to_markdown(content_html)

        if len(content_md) < MIN_CONTENT_LENGTH:
            return None, None

        excerpt_html = post.get("excerpt", {}).get("rendered", "")
        excerpt_md = self.html_to_markdown(excerpt_html)
        excerpt_clean = re.sub(r"\n+", " ", excerpt_md).strip()[:200]

        date_raw = post.get("date", "")[:10]
        year = date_raw[:4] if date_raw else "unknown"

        subcategory = self.detect_subcategory(post)
        output_path = f"insights/{subcategory}"

        fm: dict = {
            "id": f"insights-{slug}",
            "title": {"zh": title_clean, "en": ""},
            "type": "insight",
            "subcategory": subcategory,
            "category": output_path,
            "status": "active",
            "published_date": date_raw,
            "source_url": post.get("link", ""),
            "source_format": "html",
            "translation": "original",
            "contributor": "RASAAS",
            "migrated_from": "wordpress",
            "wordpress_id": post.get("id"),
        }
        if excerpt_clean:
            fm["excerpt"] = {"zh": excerpt_clean, "en": ""}

        fm_str = yaml.dump(fm, allow_unicode=True, default_flow_style=False, sort_keys=False)

        out_dir = self.output_dir / output_path
        zh_file = out_dir / f"{slug}.zh.md"

        if not self.dry_run:
            out_dir.mkdir(parents=True, exist_ok=True)
            with open(zh_file, "w", encoding="utf-8") as f:
                f.write(f"---\n{fm_str}---\n\n")
                f.write(f"# {title_clean}\n\n")
                if excerpt_clean:
                    f.write(f"> {excerpt_clean}\n\n")
                f.write(content_md)
                f.write("\n")

        return zh_file, fm

    def update_index(self, output_path: str, entries: List[dict]) -> None:
        """Update or create _index.json for insights directory."""
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

        # Sort by published_date descending
        existing.sort(key=lambda e: e.get("published_date", ""), reverse=True)

        index_data = {
            "category": output_path,
            "last_updated": datetime.now().strftime("%Y-%m-%d"),
            "count": len(existing),
            "entries": existing,
        }
        with open(index_file, "w", encoding="utf-8") as f:
            json.dump(index_data, f, ensure_ascii=False, indent=2)

    def list_posts(self) -> None:
        """List all posts and their detected subcategories."""
        posts = self.get_all_posts()
        print(f"\nTotal posts: {len(posts)}\n")
        subcategory_counts: Dict[str, int] = {}
        for post in posts:
            title = self.clean_title(post.get("title", {}).get("rendered", ""))
            date = post.get("date", "")[:10]
            subcat = self.detect_subcategory(post)
            subcategory_counts[subcat] = subcategory_counts.get(subcat, 0) + 1
            print(f"  [{date}] [{subcat}] {title[:60]}")
        print(f"\nSubcategory distribution:")
        for subcat, count in sorted(subcategory_counts.items()):
            print(f"  {subcat:<30} {count:3d} posts")

    def migrate(self) -> None:
        """Main migration entry point."""
        mode = "[DRY RUN] " if self.dry_run else ""
        print(f"\n{mode}Migrating WordPress posts to insights/")
        print(f"Output directory: {self.output_dir}\n")

        posts = self.get_all_posts()
        print(f"\nTotal posts to process: {len(posts)}")

        path_entries: Dict[str, List[dict]] = {}

        for i, post in enumerate(posts, 1):
            self.stats["total"] += 1
            title = self.clean_title(post.get("title", {}).get("rendered", ""))
            date = post.get("date", "")[:10]
            print(f"[{i:3d}/{len(posts)}] [{date}] {title[:60]}")

            # Resolve category slugs (with delay to avoid rate limiting)
            cat_ids = post.get("categories", [])
            for cat_id in cat_ids:
                self.get_category_slug(cat_id)
            if cat_ids:
                time.sleep(self.delay)

            try:
                zh_file, fm = self.save_post(post)
                if fm is None:
                    self.stats["skipped"] += 1
                    print(f"        SKIP (empty content)")
                    continue

                output_path = fm["category"]
                if output_path not in path_entries:
                    path_entries[output_path] = []
                path_entries[output_path].append({
                    "id": fm["id"],
                    "title": fm["title"],
                    "published_date": fm["published_date"],
                    "subcategory": fm["subcategory"],
                    "source_url": fm["source_url"],
                    "excerpt": fm.get("excerpt", {}),
                })

                self.stats["success"] += 1
                if self.dry_run:
                    print(f"        -> [DRY] {output_path}/{post.get('slug', '')}.zh.md")
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
        print(f"Posts migration {'(DRY RUN) ' if self.dry_run else ''}complete:")
        print(f"  Total:   {self.stats['total']}")
        print(f"  Success: {self.stats['success']}")
        print(f"  Skipped: {self.stats['skipped']}")
        print(f"  Errors:  {self.stats['error']}")
        print(f"{'='*50}")


def main():
    parser = argparse.ArgumentParser(description="Migrate WordPress posts to insights/")
    parser.add_argument("--site", default="https://reguverse.com",
                        help="WordPress site URL")
    parser.add_argument("--output", default=".",
                        help="Output directory (repo root)")
    parser.add_argument("--list", action="store_true",
                        help="List posts and their subcategories without migrating")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would be migrated without writing files")
    parser.add_argument("--delay", type=float, default=0.3,
                        help="Delay between API requests in seconds")
    args = parser.parse_args()

    migrator = PostsMigrator(args.site, args.output, args.delay, dry_run=args.dry_run)

    if args.list:
        migrator.list_posts()
        return

    migrator.migrate()


if __name__ == "__main__":
    main()
