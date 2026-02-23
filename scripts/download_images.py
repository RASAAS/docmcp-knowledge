#!/usr/bin/env python3
"""
Image downloader for docmcp-knowledge migration.

Downloads images referenced in migrated Markdown files from WordPress
(or any external URL) into the local assets/images/ directory, then
updates the Markdown files to use relative paths.

Usage:
    # Download all images in migrated docs
    python scripts/download_images.py --scan .

    # Download images in a specific directory only
    python scripts/download_images.py --scan nmpa/guidance

    # Dry run (show what would be downloaded)
    python scripts/download_images.py --scan . --dry-run

    # Download images for a single file
    python scripts/download_images.py --file nmpa/guidance/some-doc.zh.md
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
import time
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from urllib.parse import unquote, urlparse

try:
    import requests
except ImportError:
    print("ERROR: requests not installed. Run: pip install requests")
    sys.exit(1)

# Image domains to download (external images that should be localized)
DOWNLOAD_DOMAINS = {
    "reguverse.com",
    "www.reguverse.com",
}

# Image domains to keep as external links (official sources, CDNs)
KEEP_EXTERNAL_DOMAINS = {
    "www.cmde.org.cn",
    "www.nmpa.gov.cn",
    "www.fda.gov",
    "eur-lex.europa.eu",
}

# Supported image extensions
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"}

# Assets directory relative to repo root
ASSETS_DIR = "assets/images"


class ImageDownloader:
    def __init__(self, repo_root: str, dry_run: bool = False, delay: float = 0.3):
        self.repo_root = Path(repo_root)
        self.dry_run = dry_run
        self.delay = delay
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (compatible; docmcp-knowledge-migrator/1.0)",
            "Referer": "https://reguverse.com/",
        })
        self.stats: Dict[str, int] = {
            "files_scanned": 0,
            "images_found": 0,
            "images_downloaded": 0,
            "images_skipped": 0,
            "images_failed": 0,
        }
        # Cache: url -> local relative path (to avoid re-downloading same image)
        self.url_cache: Dict[str, str] = {}

    def should_download(self, url: str) -> bool:
        """Determine if an image URL should be downloaded locally."""
        parsed = urlparse(url)
        domain = parsed.netloc.lower().lstrip("www.")
        full_domain = parsed.netloc.lower()

        if full_domain in KEEP_EXTERNAL_DOMAINS:
            return False
        if full_domain in DOWNLOAD_DOMAINS or domain in DOWNLOAD_DOMAINS:
            return True
        # Download any non-official external image
        if parsed.scheme in ("http", "https") and full_domain not in KEEP_EXTERNAL_DOMAINS:
            return True
        return False

    def derive_local_path(self, url: str, category_hint: str = "") -> Path:
        """
        Derive a local file path for an image URL.
        Uses the URL path structure to organize images by category.
        """
        parsed = urlparse(url)
        url_path = unquote(parsed.path)

        # Extract filename from URL
        filename = Path(url_path).name
        if not filename:
            # Generate a hash-based name
            filename = hashlib.md5(url.encode()).hexdigest()[:12] + ".png"

        # Clean filename: remove special chars, keep extension
        stem = Path(filename).stem
        suffix = Path(filename).suffix.lower()
        if suffix not in IMAGE_EXTENSIONS:
            suffix = ".png"

        # Sanitize stem
        stem = re.sub(r"[^\w\-.]", "-", stem)
        stem = re.sub(r"-+", "-", stem).strip("-")[:60]
        clean_filename = stem + suffix

        # Organize by category hint (e.g., "nmpa/guidance")
        if category_hint:
            subdir = category_hint.replace("/", "-")
        else:
            # Try to derive from URL path
            parts = [p for p in url_path.split("/") if p and p not in ("wp-content", "uploads")]
            subdir = parts[0] if parts else "misc"

        return Path(ASSETS_DIR) / subdir / clean_filename

    def download_image(self, url: str, local_path: Path) -> bool:
        """Download a single image. Returns True on success."""
        if url in self.url_cache:
            return True

        abs_path = self.repo_root / local_path

        if abs_path.exists():
            self.url_cache[url] = str(local_path)
            return True

        if self.dry_run:
            print(f"    [DRY] Would download: {url}")
            print(f"          -> {local_path}")
            self.url_cache[url] = str(local_path)
            return True

        try:
            abs_path.parent.mkdir(parents=True, exist_ok=True)
            resp = self.session.get(url, timeout=30, stream=True)
            resp.raise_for_status()

            # Check content type
            content_type = resp.headers.get("content-type", "")
            if "image" not in content_type and "octet-stream" not in content_type:
                print(f"    WARN: Unexpected content-type '{content_type}' for {url}")

            with open(abs_path, "wb") as f:
                for chunk in resp.iter_content(chunk_size=8192):
                    f.write(chunk)

            size_kb = abs_path.stat().st_size // 1024
            print(f"    Downloaded ({size_kb}KB): {local_path}")
            self.url_cache[url] = str(local_path)
            time.sleep(self.delay)
            return True

        except requests.RequestException as e:
            print(f"    FAILED: {url} -> {e}")
            return False

    def process_file(self, md_file: Path) -> int:
        """
        Process a single Markdown file: find external images, download them,
        update references. Returns number of images processed.
        """
        content = md_file.read_text(encoding="utf-8")

        # Find all image references: ![alt](url) and <img src="url">
        md_images = re.findall(r"!\[([^\]]*)\]\((https?://[^)]+)\)", content)
        html_images = re.findall(r'<img[^>]+src=["\']?(https?://[^\s"\']+)["\']?', content)

        all_images: List[Tuple[str, str]] = [(alt, url) for alt, url in md_images]
        all_images += [("", url) for url in html_images]

        if not all_images:
            return 0

        # Derive category from file path relative to repo root
        rel_path = md_file.relative_to(self.repo_root)
        parts = rel_path.parts
        category_hint = "/".join(parts[:2]) if len(parts) >= 2 else parts[0]

        modified = content
        downloaded = 0

        for alt, url in all_images:
            if not self.should_download(url):
                continue

            self.stats["images_found"] += 1

            # Check cache first
            if url in self.url_cache:
                local_rel = self.url_cache[url]
            else:
                local_path = self.derive_local_path(url, category_hint)
                # Handle filename collision
                abs_path = self.repo_root / local_path
                counter = 1
                while abs_path.exists() and not self._same_url(url, local_path):
                    stem = local_path.stem.rstrip(f"-{counter-1}") if counter > 1 else local_path.stem
                    local_path = local_path.parent / f"{stem}-{counter}{local_path.suffix}"
                    abs_path = self.repo_root / local_path
                    counter += 1

                success = self.download_image(url, local_path)
                if not success:
                    self.stats["images_failed"] += 1
                    continue
                local_rel = str(local_path)

            # Calculate relative path from the markdown file to the asset
            md_dir = md_file.parent
            asset_abs = self.repo_root / local_rel
            try:
                rel_to_md = Path(asset_abs).relative_to(md_dir)
                rel_str = str(rel_to_md).replace("\\", "/")
            except ValueError:
                # Use repo-root-relative path with leading /
                rel_str = "/" + local_rel.replace("\\", "/")

            # Replace in content
            if f"]({url})" in modified:
                modified = modified.replace(f"]({url})", f"]({rel_str})")
            if f'src="{url}"' in modified:
                modified = modified.replace(f'src="{url}"', f'src="{rel_str}"')
            if f"src='{url}'" in modified:
                modified = modified.replace(f"src='{url}'", f"src='{rel_str}'")

            self.stats["images_downloaded"] += 1
            downloaded += 1

        if modified != content and not self.dry_run:
            md_file.write_text(modified, encoding="utf-8")

        return downloaded

    def _same_url(self, url: str, local_path: Path) -> bool:
        """Check if a local path was created for this URL (via cache)."""
        return self.url_cache.get(url) == str(local_path)

    def scan_directory(self, scan_dir: str) -> None:
        """Scan a directory for Markdown files and process images."""
        target = self.repo_root / scan_dir if scan_dir != "." else self.repo_root
        md_files = list(target.rglob("*.md"))
        # Exclude docs/ VitePress source (those reference data layer files)
        md_files = [f for f in md_files if "node_modules" not in str(f)]

        print(f"\nScanning {len(md_files)} Markdown files in {target}")
        if self.dry_run:
            print("[DRY RUN MODE]\n")

        for md_file in md_files:
            self.stats["files_scanned"] += 1
            rel = md_file.relative_to(self.repo_root)
            count = self.process_file(md_file)
            if count > 0:
                print(f"  {rel}: {count} image(s) processed")

        self._print_summary()

    def process_single_file(self, file_path: str) -> None:
        """Process a single Markdown file."""
        md_file = self.repo_root / file_path
        if not md_file.exists():
            print(f"ERROR: File not found: {md_file}")
            sys.exit(1)

        print(f"\nProcessing: {file_path}")
        if self.dry_run:
            print("[DRY RUN MODE]\n")

        count = self.process_file(md_file)
        print(f"Processed {count} image(s)")
        self._print_summary()

    def _print_summary(self) -> None:
        print(f"\n{'='*50}")
        print(f"Summary:")
        print(f"  Files scanned:      {self.stats['files_scanned']}")
        print(f"  Images found:       {self.stats['images_found']}")
        print(f"  Images downloaded:  {self.stats['images_downloaded']}")
        print(f"  Images failed:      {self.stats['images_failed']}")
        print(f"{'='*50}")


def main():
    parser = argparse.ArgumentParser(description="Download images from Markdown files")
    parser.add_argument("--scan", default=None,
                        help="Directory to scan (relative to repo root, use '.' for all)")
    parser.add_argument("--file", default=None,
                        help="Process a single Markdown file")
    parser.add_argument("--repo-root", default=".",
                        help="Repo root directory (default: current directory)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would be downloaded without writing files")
    parser.add_argument("--delay", type=float, default=0.3,
                        help="Delay between downloads in seconds (default: 0.3)")
    args = parser.parse_args()

    if not args.scan and not args.file:
        parser.error("Specify either --scan <dir> or --file <path>")

    downloader = ImageDownloader(args.repo_root, dry_run=args.dry_run, delay=args.delay)

    if args.file:
        downloader.process_single_file(args.file)
    else:
        downloader.scan_directory(args.scan)


if __name__ == "__main__":
    main()
