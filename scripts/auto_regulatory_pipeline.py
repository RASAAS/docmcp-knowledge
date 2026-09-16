#!/usr/bin/env python3
"""
Automated Regulatory Pipeline: News -> Full Text -> Deep Insight -> Publish

End-to-end pipeline that:
  1. Reads new items from regulatory_news/*.json (output of fetch_updates + report_to_news)
  2. Fetches full text from source URLs (.doc/.docx/.pdf/HTML)
  3. Generates deep regulatory interpretation via LLM
  4. Creates knowledge base pages (insights + guidance full text)
  5. Updates indexes and prepares for deployment

Excluded: safety_communication, recall_class1 categories (per user requirement)

Usage:
    # Process all new items from a specific framework
    python scripts/auto_regulatory_pipeline.py --framework nmpa --dry-run
    python scripts/auto_regulatory_pipeline.py --framework fda

    # Process a single item by ID
    python scripts/auto_regulatory_pipeline.py --item-id nmpa_2026_46_industry_standards

    # Full pipeline: all frameworks, publish
    python scripts/auto_regulatory_pipeline.py --all --publish

    # Only fetch full text (no insight generation)
    python scripts/auto_regulatory_pipeline.py --framework nmpa --fetch-only

    # Only generate insights for items that already have full text
    python scripts/auto_regulatory_pipeline.py --framework nmpa --insight-only

Environment:
    LLM_API_KEY   : API key for LLM (OpenAI-compatible endpoint)
    LLM_BASE_URL  : Base URL (default: https://api.deepseek.com/v1)
    LLM_MODEL     : Model name (default: deepseek-v4-pro)
"""

import argparse
import hashlib
import json
import logging
import os
import re
import subprocess
import sys
import tempfile
import time
from datetime import datetime
from pathlib import Path
from typing import Optional
from urllib.parse import urlparse

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

try:
    import yaml
except ImportError:
    yaml = None
    logger.warning("pyyaml not installed. pip install pyyaml")

REPO_ROOT = Path(__file__).resolve().parent.parent
NEWS_DIR = REPO_ROOT / "regulatory_news"
INSIGHTS_DIR = REPO_ROOT / "insights"
DOCS_DIR = REPO_ROOT / "docs"
SCRIPTS_DIR = REPO_ROOT / "scripts"

LLM_API_KEY = os.environ.get("LLM_API_KEY", "")
LLM_BASE_URL = os.environ.get("LLM_BASE_URL", "https://api.deepseek.com/v1")
LLM_MODEL = os.environ.get("LLM_MODEL", "deepseek-v4-pro")

# Categories to SKIP (safety announcements, recalls)
SKIP_CATEGORIES = {
    "safety_communication",
    "recall_class1",
    "recall_class2",
    "cdrh_news",
}

# Map news category -> insight subcategory
CATEGORY_TO_INSIGHT = {
    "regulation_update": "analysis",
    "guidance_new": "analysis",
    "standard_revision": "analysis",
}

# Map framework -> insight subcategory for periodic updates
FRAMEWORK_INSIGHT_MAP = {
    "nmpa": "nmpa-updates",
    "fda": "fda-updates",
    "eu_mdr": "eu-mdr-updates",
}

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/125.0.0.0 Safari/537.36"
)

PIPELINE_STATE_FILE = REPO_ROOT / "scripts" / ".pipeline_state.json"

# Alternative news mirror/aggregator sites for NMPA content.
# These sites re-publish NMPA announcements without anti-bot protection.
# Ordered by reliability: try first site, fall back to next on failure.
NMPA_MIRROR_SITES = [
    # Major financial news portals (fast repost, no paywall, no anti-bot)
    "finance.sina.com.cn",
    "finance.eastmoney.com",
    "stock.hexun.com",
    "med.china.com.cn",
    # Government portals (usually accessible)
    "www.gov.cn",
    "www.moj.gov.cn",
    # Medical industry portals
    "www.cn-healthcare.com",
    "www.qgyyzs.net",
]

# Search engines for finding mirror copies of NMPA content
SEARCH_ENGINES = {
    "bing": "https://www.bing.com/search?q={query}&cc=cn",
    "baidu": "https://www.baidu.com/s?wd={query}",
}


# ---------------------------------------------------------------------------
# State management
# ---------------------------------------------------------------------------

def load_pipeline_state() -> dict:
    if PIPELINE_STATE_FILE.exists():
        return json.loads(PIPELINE_STATE_FILE.read_text(encoding="utf-8"))
    return {"processed_items": {}, "last_run": None}


def save_pipeline_state(state: dict):
    state["last_run"] = datetime.now().isoformat()
    PIPELINE_STATE_FILE.write_text(
        json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8"
    )


# ---------------------------------------------------------------------------
# Full text fetching
# ---------------------------------------------------------------------------

class FullTextFetcher:
    """Fetch and extract full text from regulatory document source URLs."""

    # Sites known to have SSL cert issues
    SSL_SKIP_HOSTS = {"www.nifdc.org.cn", "nifdc.org.cn"}
    # Sites with anti-bot protection (need curl_cffi or Playwright)
    ANTIBOT_HOSTS = {"www.nmpa.gov.cn", "nmpa.gov.cn", "www.samr.gov.cn"}
    # JS-rendered sites (need Playwright)
    JS_RENDER_HOSTS = {"udi.nmpa.gov.cn", "www.cmde.org.cn"}

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        })
        # Try to use curl_cffi for anti-bot sites
        self._cffi_session = None
        try:
            from curl_cffi import requests as cffi_requests
            self._cffi_session = cffi_requests.Session(impersonate="chrome")
        except ImportError:
            logger.info("curl_cffi not available; anti-bot sites may fail")

    def fetch(self, source_url: str, title: str = "") -> Optional[str]:
        """Fetch full text from a source URL. Returns markdown text or None."""
        if not source_url:
            return None

        parsed = urlparse(source_url)
        path_lower = parsed.path.lower()
        hostname = parsed.hostname or ""

        try:
            if path_lower.endswith(".doc") or path_lower.endswith(".docx"):
                return self._fetch_doc(source_url)
            elif path_lower.endswith(".pdf"):
                return self._fetch_pdf(source_url)
            elif hostname in self.ANTIBOT_HOSTS:
                return self._fetch_antibot(source_url, title)
            elif hostname in self.JS_RENDER_HOSTS:
                logger.warning(f"  JS-rendered site ({hostname}), skipping HTML extraction")
                return None
            else:
                verify_ssl = hostname not in self.SSL_SKIP_HOSTS
                return self._fetch_html(source_url, title, verify_ssl=verify_ssl)
        except Exception as e:
            logger.error(f"Failed to fetch {source_url}: {e}")
            return None

    def _fetch_antibot(self, url: str, title: str = "") -> Optional[str]:
        """Fetch from anti-bot protected sites using curl_cffi."""
        if self._cffi_session:
            try:
                resp = self._cffi_session.get(url, timeout=30)
                if resp.status_code == 200 and len(resp.text) > 500:
                    return self._extract_html_content(resp.text, url, title)
            except Exception as e:
                logger.warning(f"  curl_cffi failed for {url}: {e}")

        # Fallback: try Playwright if available
        try:
            return self._fetch_playwright(url, title)
        except Exception as e:
            logger.warning(f"  Playwright fallback also failed: {e}")
            return None

    def _fetch_playwright(self, url: str, title: str = "") -> Optional[str]:
        """Fetch page using Playwright headless browser."""
        try:
            from playwright.sync_api import sync_playwright
        except ImportError:
            logger.info("  Playwright not available")
            return None

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(url, wait_until="networkidle", timeout=30000)
            content = page.content()
            browser.close()
            return self._extract_html_content(content, url, title)

    def fetch_with_mirrors(self, source_url: str, title: str, framework: str = "") -> Optional[str]:
        """Fetch full text with mirror site fallback for NMPA content.

        For NMPA items whose official URL is blocked by anti-bot protection,
        search for the same content on mirror/aggregator sites.
        """
        # First try the original URL
        text = self.fetch(source_url, title)
        if text and len(text) > 500:
            return text

        # Only use mirror strategy for NMPA/Chinese regulatory content
        if framework not in ("nmpa", "samr"):
            return text

        logger.info("  Trying mirror sites for NMPA content...")

        # Strategy 1: Search known mirror sites via Bing
        search_query = f'"{title[:40]}" site:({" OR site:".join(NMPA_MIRROR_SITES[:4])})'
        mirror_url = self._search_bing_for_mirror(search_query)
        if mirror_url:
            text = self.fetch(mirror_url, title)
            if text and len(text) > 500:
                logger.info(f"  Found content via mirror: {mirror_url}")
                return text

        # Strategy 2: Direct search on sina.com.cn (most reliable repost site)
        sina_query = f'site:finance.sina.com.cn "{title[:30]}"'
        mirror_url = self._search_bing_for_mirror(sina_query)
        if mirror_url:
            text = self.fetch(mirror_url, title)
            if text and len(text) > 500:
                logger.info(f"  Found content via Sina mirror: {mirror_url}")
                return text

        logger.warning(f"  No mirror found for: {title[:50]}...")
        return None

    def _search_bing_for_mirror(self, query: str) -> Optional[str]:
        """Search Bing for a mirror URL. Returns first result URL or None."""
        try:
            encoded = requests.utils.quote(query)
            url = f"https://www.bing.com/search?q={encoded}&cc=cn"
            resp = self.session.get(url, timeout=15)
            if resp.status_code != 200:
                return None
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(resp.text, "html.parser")
            for result in soup.select("li.b_algo h2 a"):
                href = result.get("href", "")
                if href and any(site in href for site in NMPA_MIRROR_SITES):
                    return href
        except Exception as e:
            logger.debug(f"  Bing search failed: {e}")
        return None

    def _fetch_doc(self, url: str) -> Optional[str]:
        """Download .doc/.docx and extract text."""
        parsed = urlparse(url)
        hostname = parsed.hostname or ""
        verify_ssl = hostname not in self.SSL_SKIP_HOSTS
        resp = self.session.get(url, timeout=60, verify=verify_ssl)
        resp.raise_for_status()

        suffix = ".docx" if url.lower().endswith(".docx") else ".doc"
        with tempfile.NamedTemporaryFile(suffix=suffix, delete=False) as tmp:
            tmp.write(resp.content)
            tmp_path = tmp.name

        try:
            # Try textutil (macOS) first
            txt_path = tmp_path + ".txt"
            result = subprocess.run(
                ["textutil", "-convert", "txt", "-output", txt_path, tmp_path],
                capture_output=True, text=True, timeout=30,
            )
            if result.returncode == 0 and os.path.exists(txt_path):
                text = Path(txt_path).read_text(encoding="utf-8", errors="replace")
                os.unlink(txt_path)
                if len(text.strip()) > 100:
                    return text.strip()

            # Fallback: python-docx for .docx
            if suffix == ".docx":
                try:
                    from docx import Document
                    doc = Document(tmp_path)
                    paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]
                    text = "\n\n".join(paragraphs)
                    if len(text.strip()) > 100:
                        return text.strip()
                except ImportError:
                    pass

            # Fallback: LibreOffice headless
            with tempfile.TemporaryDirectory() as tmpdir:
                result = subprocess.run(
                    ["libreoffice", "--headless", "--convert-to", "txt:Text",
                     "--outdir", tmpdir, tmp_path],
                    capture_output=True, text=True, timeout=120,
                )
                if result.returncode == 0:
                    txt_files = list(Path(tmpdir).glob("*.txt"))
                    if txt_files:
                        text = txt_files[0].read_text(encoding="utf-8", errors="replace")
                        if len(text.strip()) > 100:
                            return text.strip()

            logger.warning(f"Could not extract text from {url}")
            return None
        finally:
            os.unlink(tmp_path)

    def _fetch_pdf(self, url: str) -> Optional[str]:
        """Download PDF and extract text."""
        try:
            import fitz  # PyMuPDF
        except ImportError:
            logger.error("PyMuPDF not installed for PDF extraction. pip install pymupdf")
            return None

        resp = self.session.get(url, timeout=60)
        resp.raise_for_status()

        doc = fitz.open(stream=resp.content, filetype="pdf")
        pages = []
        for page in doc:
            text = page.get_text("text")
            if text.strip():
                pages.append(text.strip())
        doc.close()

        full_text = "\n\n".join(pages)
        if len(full_text.strip()) < 100:
            logger.warning(f"PDF text extraction yielded very little content from {url}")
            return None
        return full_text.strip()

    def _fetch_html(self, url: str, title: str = "", verify_ssl: bool = True) -> Optional[str]:
        """Fetch HTML page and extract main content."""
        try:
            resp = self.session.get(url, timeout=30, verify=verify_ssl)
            resp.raise_for_status()
        except Exception as e:
            logger.error(f"HTTP error for {url}: {e}")
            return None

        return self._extract_html_content(resp.text, url, title)

    def _extract_html_content(self, html: str, url: str, title: str = "") -> Optional[str]:
        """Extract main text content from HTML."""
        if len(html) < 200:
            return None

        try:
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(html, "html.parser")

            # Remove nav, header, footer, script, style
            for tag in soup.find_all(["nav", "header", "footer", "script",
                                       "style", "aside", "iframe"]):
                tag.decompose()

            # Try to find main content area
            main = (
                soup.find("main")
                or soup.find("article")
                or soup.find("div", class_=re.compile(r"content|article|main|body", re.I))
                or soup.find("div", id=re.compile(r"content|article|main|body", re.I))
            )
            if main:
                text = main.get_text(separator="\n", strip=True)
            else:
                text = soup.get_text(separator="\n", strip=True)

            # Clean up
            lines = [line.strip() for line in text.split("\n") if line.strip()]
            text = "\n".join(lines)

            if len(text) < 200:
                logger.warning(f"HTML extraction yielded very little content from {url}")
                return None
            return text

        except ImportError:
            # Fallback: basic regex extraction
            text = re.sub(r"<script[^>]*>.*?</script>", "", html, flags=re.DOTALL | re.I)
            text = re.sub(r"<style[^>]*>.*?</style>", "", text, flags=re.DOTALL | re.I)
            text = re.sub(r"<[^>]+>", "\n", text)
            text = re.sub(r"\n{3,}", "\n\n", text)
            lines = [line.strip() for line in text.split("\n") if line.strip()]
            return "\n".join(lines) if len("\n".join(lines)) > 200 else None


# ---------------------------------------------------------------------------
# LLM Insight Generator
# ---------------------------------------------------------------------------

class InsightGenerator:
    """Generate deep regulatory interpretation using LLM."""

    SYSTEM_PROMPT = """You are a senior regulatory affairs specialist for medical devices.
You write deep regulatory interpretations and compliance analysis articles.

Your articles follow this structure:
1. Policy Background & Significance (why this was issued, regulatory context)
2. Core Changes Analysis (numbered key changes with detailed explanation)
3. Impact Analysis (for manufacturers, for the industry, for patients/users)
4. Compliance Recommendations (practical steps for affected parties)
5. Timeline & Key Dates (if applicable)

Requirements:
- Write in a professional, authoritative tone
- Be specific -- cite article numbers, exact requirements, dates
- Provide actionable compliance advice
- Include both Chinese (primary) and English sections
- The Chinese section comes FIRST, followed by a horizontal rule, then the English translation
- Use markdown formatting with ## headings for major sections, ### for subsections
- Do NOT include a table of contents
- The article title should be a concise, descriptive Chinese title (not just the document name)
"""

    def generate(self, item: dict, full_text: str) -> Optional[dict]:
        """Generate insight article from a regulatory news item and its full text.

        Returns dict with keys: title_zh, title_en, content_zh, content_en, full_content
        """
        if not LLM_API_KEY:
            logger.error("LLM_API_KEY not set. Cannot generate insights.")
            return None

        title_zh = item.get("title", {}).get("zh", "")
        title_en = item.get("title", {}).get("en", "")
        summary_zh = item.get("summary", {}).get("zh", "")
        category = item.get("category", "")
        framework = item.get("framework", "")
        published_date = item.get("published_date", "")

        # Truncate full text if too long (keep first 60K chars for LLM context)
        if len(full_text) > 60000:
            full_text = full_text[:60000] + "\n\n[... full text truncated for analysis ...]"

        user_prompt = f"""Please write a deep regulatory interpretation article for the following regulatory update.

## Document Information
- Title (Chinese): {title_zh}
- Title (English): {title_en}
- Framework: {framework.upper()}
- Category: {category}
- Published Date: {published_date}
- Summary: {summary_zh}

## Full Text of the Document
{full_text}

## Requirements
1. Generate a compelling article title in Chinese (not just the document title -- make it descriptive of the significance)
2. Write the FULL article in Chinese first (2000-4000 words), following the structure in the system prompt
3. Then write "---" separator
4. Write the FULL English translation (matching the Chinese content)
5. The Chinese title should capture the essence and impact of the regulation, not just repeat the document name

Output format:
TITLE_ZH: [Chinese article title]
TITLE_EN: [English article title]
---CONTENT_START---
[Full Chinese article in markdown]

---

[Full English translation in markdown]
---CONTENT_END---
"""

        try:
            headers = {
                "Authorization": f"Bearer {LLM_API_KEY}",
                "Content-Type": "application/json",
            }
            payload = {
                "model": LLM_MODEL,
                "messages": [
                    {"role": "system", "content": self.SYSTEM_PROMPT},
                    {"role": "user", "content": user_prompt},
                ],
                "max_tokens": 16000,
                "temperature": 0.3,
            }

            resp = requests.post(
                f"{LLM_BASE_URL}/chat/completions",
                headers=headers,
                json=payload,
                timeout=300,
            )
            resp.raise_for_status()

            result = resp.json()
            content = result["choices"][0]["message"]["content"]
            return self._parse_llm_output(content)

        except Exception as e:
            logger.error(f"LLM generation failed: {e}")
            return None

    def _parse_llm_output(self, raw: str) -> Optional[dict]:
        """Parse structured output from LLM."""
        # Extract title
        title_zh = ""
        title_en = ""

        title_zh_match = re.search(r"TITLE_ZH:\s*(.+)", raw)
        title_en_match = re.search(r"TITLE_EN:\s*(.+)", raw)
        if title_zh_match:
            title_zh = title_zh_match.group(1).strip()
        if title_en_match:
            title_en = title_en_match.group(1).strip()

        # Extract content
        content_match = re.search(
            r"---CONTENT_START---\s*\n(.*?)\n---CONTENT_END---",
            raw, re.DOTALL,
        )
        if not content_match:
            # Fallback: use everything after the titles
            lines = raw.split("\n")
            content_start = 0
            for i, line in enumerate(lines):
                if line.startswith("TITLE_EN:"):
                    content_start = i + 1
                    break
            content = "\n".join(lines[content_start:]).strip()
            if content.startswith("---CONTENT_START---"):
                content = content[len("---CONTENT_START---"):].strip()
            if content.endswith("---CONTENT_END---"):
                content = content[:-len("---CONTENT_END---")].strip()
        else:
            content = content_match.group(1).strip()

        if not content or len(content) < 500:
            logger.error("LLM output too short or empty")
            return None

        # Split Chinese and English by "---" separator
        parts = re.split(r"\n---\n", content, maxsplit=1)
        content_zh = parts[0].strip()
        content_en = parts[1].strip() if len(parts) > 1 else ""

        # Fallback title extraction from content
        if not title_zh:
            h1_match = re.search(r"^#\s+(.+)", content_zh, re.MULTILINE)
            if h1_match:
                title_zh = h1_match.group(1).strip()

        return {
            "title_zh": title_zh,
            "title_en": title_en,
            "content_zh": content_zh,
            "content_en": content_en,
            "full_content": content,
        }


# ---------------------------------------------------------------------------
# Knowledge Base Publisher
# ---------------------------------------------------------------------------

class KBPublisher:
    """Publish insight articles and full-text documents to the knowledge base."""

    def publish_insight(
        self,
        item: dict,
        insight: dict,
        subcategory: str,
        dry_run: bool = False,
    ) -> Optional[str]:
        """Publish an insight article. Returns the slug or None."""
        title_zh = insight["title_zh"]
        title_en = insight.get("title_en", "")
        item_id = item.get("id", "")
        source_url = item.get("source_url", "")
        published_date = item.get("published_date", datetime.now().strftime("%Y-%m-%d"))

        # Generate slug
        slug = self._generate_slug(item_id, title_zh, title_en)

        # Determine target directories
        data_dir = INSIGHTS_DIR / subcategory
        docs_zh_dir = DOCS_DIR / "zh" / "insights" / subcategory
        docs_en_dir = DOCS_DIR / "en" / "insights" / subcategory

        if dry_run:
            logger.info(f"  [DRY] Would publish insight: {slug} to {subcategory}")
            return slug

        # Create directories
        data_dir.mkdir(parents=True, exist_ok=True)
        docs_zh_dir.mkdir(parents=True, exist_ok=True)
        docs_en_dir.mkdir(parents=True, exist_ok=True)

        # Build front matter
        fm = {
            "id": f"insights-{slug}",
            "title": {"zh": title_zh, "en": title_en},
            "type": "insight",
            "subcategory": subcategory,
            "category": f"insights/{subcategory}",
            "status": "active",
            "published_date": published_date,
            "source_url": source_url,
            "source_format": "auto-generated",
            "translation": "original",
            "contributor": "RASAAS",
            "auto_generated": True,
            "news_item_id": item_id,
            "excerpt": {
                "zh": insight["content_zh"][:200].replace("\n", " "),
                "en": insight.get("content_en", "")[:200].replace("\n", " "),
            },
        }

        # Write data layer file (.zh.md)
        zh_data_path = data_dir / f"{slug}.zh.md"
        zh_content = self._build_markdown(fm, insight["content_zh"])
        zh_data_path.write_text(zh_content, encoding="utf-8")
        logger.info(f"  Written: {zh_data_path.relative_to(REPO_ROOT)}")

        # Write docs/zh page
        docs_zh_path = docs_zh_dir / f"{slug}.md"
        docs_zh_path.write_text(zh_content, encoding="utf-8")
        logger.info(f"  Written: {docs_zh_path.relative_to(REPO_ROOT)}")

        # Write docs/en page (if English content available)
        if insight.get("content_en"):
            en_fm = dict(fm)
            en_fm["translation"] = "machine"
            en_content = self._build_markdown(en_fm, insight["content_en"])
            docs_en_path = docs_en_dir / f"{slug}.md"
            docs_en_path.write_text(en_content, encoding="utf-8")
            logger.info(f"  Written: {docs_en_path.relative_to(REPO_ROOT)}")

        # Update _index.json
        self._update_index(data_dir, fm, slug)

        return slug

    def publish_guidance_fulltext(
        self,
        item: dict,
        full_text: str,
        framework: str,
        dry_run: bool = False,
    ) -> Optional[str]:
        """Publish full text as a guidance document page (e.g., NMPA guidance).
        Returns the slug or None."""
        title_zh = item.get("title", {}).get("zh", "")
        title_en = item.get("title", {}).get("en", "")
        source_url = item.get("source_url", "")
        published_date = item.get("published_date", "")
        item_id = item.get("id", "")

        slug = self._generate_slug(item_id, title_zh, title_en)

        if framework == "nmpa":
            docs_zh_dir = DOCS_DIR / "zh" / "nmpa" / "guidance"
            docs_en_dir = DOCS_DIR / "en" / "nmpa" / "guidance"
        elif framework == "fda":
            docs_zh_dir = DOCS_DIR / "zh" / "fda" / "guidance"
            docs_en_dir = DOCS_DIR / "en" / "fda" / "guidance"
        else:
            docs_zh_dir = DOCS_DIR / "zh" / framework / "guidance"
            docs_en_dir = DOCS_DIR / "en" / framework / "guidance"

        if dry_run:
            logger.info(f"  [DRY] Would publish guidance: {slug} to {framework}/guidance")
            return slug

        docs_zh_dir.mkdir(parents=True, exist_ok=True)
        docs_en_dir.mkdir(parents=True, exist_ok=True)

        # Determine source format from URL
        source_format = "html"
        if source_url:
            if source_url.lower().endswith(".doc") or source_url.lower().endswith(".docx"):
                source_format = "doc"
            elif source_url.lower().endswith(".pdf"):
                source_format = "pdf"

        fm = {
            "id": f"{framework}-{slug}",
            "title": {"zh": title_zh, "en": title_en},
            "regulation": framework,
            "category": f"{framework}/guidance",
            "status": "active",
            "source_url": source_url,
            "source_url_verified": datetime.now().strftime("%Y-%m-%d"),
            "source_url_status": "active",
            "source_format": source_format,
            "translation": "original",
            "last_verified": datetime.now().strftime("%Y-%m-%d"),
            "contributor": "RASAAS",
            "effective_date": published_date or datetime.now().strftime("%Y-%m-%d"),
        }

        # Ensure full text starts with H1 title
        body = full_text
        if not body.startswith("# "):
            body = f"# {title_zh}\n\n{body}"

        zh_content = self._build_markdown(fm, body)
        zh_path = docs_zh_dir / f"{slug}.md"
        zh_path.write_text(zh_content, encoding="utf-8")
        logger.info(f"  Written: {zh_path.relative_to(REPO_ROOT)}")

        return slug

    def _build_markdown(self, fm: dict, body: str) -> str:
        """Build a complete markdown file with YAML front matter."""
        fm_lines = ["---"]
        for key, val in fm.items():
            if isinstance(val, dict):
                fm_lines.append(f"{key}:")
                for k, v in val.items():
                    fm_lines.append(f"  {k}: '{self._yaml_escape(str(v))}'")
            elif isinstance(val, bool):
                fm_lines.append(f"{key}: {'true' if val else 'false'}")
            else:
                fm_lines.append(f"{key}: '{self._yaml_escape(str(val))}'")
        fm_lines.append("---")
        fm_str = "\n".join(fm_lines)
        return f"{fm_str}\n\n{body}\n"

    @staticmethod
    def _yaml_escape(s: str) -> str:
        return s.replace("'", "''")

    def _generate_slug(self, item_id: str, title_zh: str, title_en: str) -> str:
        """Generate a URL-safe slug from item metadata."""
        # Try English title first for cleaner slugs
        if title_en:
            slug = re.sub(r"[^a-z0-9]+", "-", title_en.lower())[:80].strip("-")
            if len(slug) > 10:
                return slug

        # Fallback: use item_id
        if item_id:
            slug = re.sub(r"[^a-z0-9_]+", "-", item_id.lower())[:80].strip("-")
            return slug

        # Last resort: hash
        h = hashlib.md5(title_zh.encode()).hexdigest()[:8]
        return f"doc-{h}"

    def _update_index(self, data_dir: Path, fm: dict, slug: str):
        """Update _index.json in the insight data directory."""
        index_path = data_dir / "_index.json"
        index = {"category": fm.get("category", ""), "last_updated": "", "count": 0, "entries": []}

        if index_path.exists():
            try:
                index = json.loads(index_path.read_text(encoding="utf-8"))
            except Exception:
                pass

        # Check for duplicate
        existing_ids = {e.get("id") for e in index.get("entries", [])}
        if fm["id"] in existing_ids:
            logger.info(f"  Index already contains {fm['id']}, skipping update")
            return

        entry = {
            "id": fm["id"],
            "title": fm.get("title", {}),
            "published_date": fm.get("published_date", ""),
            "subcategory": fm.get("subcategory", ""),
            "source_url": fm.get("source_url", ""),
            "excerpt": fm.get("excerpt", {}),
            "status": "active",
        }

        index["entries"].insert(0, entry)
        index["count"] = len(index["entries"])
        index["last_updated"] = datetime.now().strftime("%Y-%m-%d")

        index_path.write_text(
            json.dumps(index, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        logger.info(f"  Updated index: {index_path.relative_to(REPO_ROOT)}")


# ---------------------------------------------------------------------------
# Pipeline orchestration
# ---------------------------------------------------------------------------

def should_process_item(item: dict) -> bool:
    """Check if an item should be processed by the pipeline."""
    category = item.get("category", "")
    if category in SKIP_CATEGORIES:
        return False
    if item.get("status") not in ("published", "new", None, ""):
        return False
    return True


def determine_insight_subcategory(item: dict) -> str:
    """Determine which insight subcategory an item should go to."""
    framework = item.get("framework", "")
    category = item.get("category", "")

    # Framework-specific update channels
    if framework in FRAMEWORK_INSIGHT_MAP:
        return FRAMEWORK_INSIGHT_MAP[framework]

    # Category-based mapping
    return CATEGORY_TO_INSIGHT.get(category, "analysis")


def process_single_item(
    item: dict,
    fetcher: FullTextFetcher,
    generator: InsightGenerator,
    publisher: KBPublisher,
    state: dict,
    dry_run: bool = False,
    fetch_only: bool = False,
    insight_only: bool = False,
) -> bool:
    """Process a single regulatory news item through the pipeline."""
    item_id = item.get("id", "unknown")
    title_zh = item.get("title", {}).get("zh", item_id)
    source_url = item.get("source_url", "")

    # Check if already processed
    if item_id in state.get("processed_items", {}):
        logger.info(f"  Skipping {item_id} (already processed)")
        return False

    logger.info(f"\n{'='*60}")
    logger.info(f"Processing: {title_zh}")
    logger.info(f"  ID: {item_id}")
    logger.info(f"  URL: {source_url}")

    # Step 1: Fetch full text
    full_text = None
    framework = item.get("framework", "")
    if not insight_only:
        logger.info("  Step 1: Fetching full text...")
        full_text = fetcher.fetch_with_mirrors(source_url, title_zh, framework)
        if full_text:
            logger.info(f"  Fetched {len(full_text)} chars of full text")
        else:
            logger.warning(f"  Could not fetch full text from {source_url}")

    if fetch_only:
        if full_text:
            state.setdefault("processed_items", {})[item_id] = {
                "status": "fulltext_only",
                "chars": len(full_text),
                "timestamp": datetime.now().isoformat(),
            }
        return full_text is not None

    # Step 2: Generate insight (requires full text or at least summary)
    insight = None
    if full_text or item.get("summary", {}).get("zh"):
        text_for_analysis = full_text or item.get("summary", {}).get("zh", "")
        logger.info("  Step 2: Generating deep insight via LLM...")
        insight = generator.generate(item, text_for_analysis)
        if insight:
            logger.info(f"  Generated insight: {insight['title_zh']}")
        else:
            logger.warning("  LLM insight generation failed")

    if not insight:
        logger.warning(f"  Skipping publish for {item_id} (no insight generated)")
        return False

    # Step 3: Publish
    logger.info("  Step 3: Publishing to knowledge base...")
    subcategory = determine_insight_subcategory(item)

    slug = publisher.publish_insight(item, insight, subcategory, dry_run=dry_run)
    if slug:
        logger.info(f"  Published insight as: {slug}")

    # Also publish full text as guidance page if applicable
    framework = item.get("framework", "")
    category = item.get("category", "")
    if full_text and category == "guidance_new" and framework in ("nmpa", "fda"):
        logger.info("  Also publishing guidance full text...")
        publisher.publish_guidance_fulltext(item, full_text, framework, dry_run=dry_run)

    # Update state
    if not dry_run:
        state.setdefault("processed_items", {})[item_id] = {
            "status": "published",
            "slug": slug,
            "subcategory": subcategory,
            "has_fulltext": full_text is not None,
            "timestamp": datetime.now().isoformat(),
        }

    return True


def run_pipeline(
    frameworks: list[str],
    item_id: str = "",
    dry_run: bool = False,
    fetch_only: bool = False,
    insight_only: bool = False,
    publish: bool = False,
) -> dict:
    """Run the full pipeline."""
    state = load_pipeline_state()
    fetcher = FullTextFetcher()
    generator = InsightGenerator()
    publisher = KBPublisher()

    stats = {"processed": 0, "skipped": 0, "failed": 0, "published": 0}

    for fw in frameworks:
        news_file = NEWS_DIR / f"{fw}.json"
        if not news_file.exists():
            logger.warning(f"No news file for {fw}: {news_file}")
            continue

        data = json.loads(news_file.read_text(encoding="utf-8"))
        items = data.get("items", [])
        logger.info(f"\nFramework: {fw} ({len(items)} items)")

        for item in items:
            if item_id and item.get("id") != item_id:
                continue

            if not should_process_item(item):
                stats["skipped"] += 1
                continue

            success = process_single_item(
                item, fetcher, generator, publisher, state,
                dry_run=dry_run,
                fetch_only=fetch_only,
                insight_only=insight_only,
            )

            if success:
                stats["published"] += 1
                # Rate limit between LLM calls
                if not fetch_only and not dry_run:
                    time.sleep(3)
            else:
                stats["failed"] += 1

            stats["processed"] += 1

            if item_id:
                break

    if not dry_run:
        save_pipeline_state(state)

    # Update standards library from insight full text (if applicable)
    if stats["published"] > 0 and not dry_run:
        logger.info("\nChecking for standards to add to standards library...")
        try:
            _update_standards_library()
        except Exception as e:
            logger.error(f"  Standards library update failed: {e}")

    # Run index regeneration if anything was published
    if stats["published"] > 0 and not dry_run:
        logger.info("\nRegenerating knowledge base indexes...")
        try:
            subprocess.run(
                [sys.executable, str(SCRIPTS_DIR / "generate_docs_index.py"),
                 "--output-root", str(REPO_ROOT)],
                check=True, capture_output=True, text=True,
            )
            logger.info("  Index regeneration complete")
        except Exception as e:
            logger.error(f"  Index regeneration failed: {e}")

    # Deploy if requested
    if publish and stats["published"] > 0 and not dry_run:
        logger.info("\nDeploying to Cloudflare Pages...")
        deploy_to_cloudflare()

    return stats


def _update_standards_library():
    """Parse newly generated insight articles for standards lists and update
    the master standards.json if new standards are found."""
    standards_json = REPO_ROOT / "nmpa" / "standards" / "master" / "standards.json"
    if not standards_json.exists():
        return

    standards = json.loads(standards_json.read_text(encoding="utf-8"))
    existing_numbers = {s.get("number", "").strip() for s in standards}

    # Pattern: "YY 1234-2026" or "YY/T 1234.2-2026"
    std_pattern = re.compile(
        r"((?:GB|GB/T|YY|YY/T)\s+\d[\d.]*[\u2014\-]\d{4})"
    )

    state = load_pipeline_state()
    new_count = 0

    for item_id, info in state.get("processed_items", {}).items():
        if info.get("status") != "published":
            continue
        slug = info.get("slug", "")
        if not slug:
            continue

        # Check the insight content for standards references
        for subcat in ("nmpa-updates", "analysis"):
            zh_path = INSIGHTS_DIR / subcat / f"{slug}.zh.md"
            if not zh_path.exists():
                continue
            content = zh_path.read_text(encoding="utf-8")

            # Look for a standards table (markdown table with standard numbers)
            for match in std_pattern.finditer(content):
                number = match.group(1).replace("\u2014", "-").strip()
                # Normalize spacing: "YY 1234-2026" -> "YY 1234-2026"
                number = re.sub(r"\s+", " ", number)
                if number not in existing_numbers:
                    # Try to extract title from the same line
                    line = content[max(0, match.start() - 5):match.end() + 200]
                    # Look for title in table: | number | title | or after number
                    title_match = re.search(
                        r"[|\s]" + re.escape(number) + r"\s*[|\s]+([^|]+)",
                        line,
                    )
                    title = title_match.group(1).strip() if title_match else ""

                    if not title:
                        # Try "number《title》" pattern
                        title_match2 = re.search(
                            re.escape(number) + r"\s*(?:\u300A|)(.+?)(?:\u300B|$)",
                            line,
                        )
                        title = title_match2.group(1).strip() if title_match2 else ""

                    if title and len(title) > 4:
                        # Determine domain and standard type
                        is_mandatory = number.startswith("GB ") or number.startswith("YY ")
                        is_general = False  # Default to professional

                        new_entry = {
                            "seq": len(standards) + new_count + 1,
                            "dir_name": "通用技术领域" if is_general else "专业技术领域",
                            "l1": "",
                            "l2": "",
                            "number": number,
                            "title_zh": title,
                            "approval_date": "",
                            "effective_date": "",
                            "status_zh": "即将实施",
                            "status": "upcoming",
                            "id": f"nmpa-{number.lower().replace('/', '-').replace(' ', '-')}",
                            "source_url": "https://app.nifdc.org.cn/biaogzx/qxqwk.do",
                            "auto_added": True,
                        }
                        standards.append(new_entry)
                        existing_numbers.add(number)
                        new_count += 1
                        logger.info(f"  Added standard: {number} - {title[:40]}...")

    if new_count > 0:
        standards_json.write_text(
            json.dumps(standards, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        logger.info(f"  Updated standards.json: +{new_count} standards (total: {len(standards)})")

        # Regenerate standards pages
        try:
            subprocess.run(
                [sys.executable, str(SCRIPTS_DIR / "generate_standards_pages.py")],
                check=True, capture_output=True, text=True,
            )
            logger.info("  Standards pages regenerated")
        except Exception as e:
            logger.error(f"  Standards page generation failed: {e}")


def deploy_to_cloudflare():
    """Build VitePress and deploy to Cloudflare Pages."""
    try:
        # Build
        logger.info("  Building VitePress site...")
        subprocess.run(
            ["npm", "run", "docs:build"],
            cwd=str(REPO_ROOT),
            check=True, capture_output=True, text=True,
            timeout=300,
        )

        # Deploy
        logger.info("  Deploying via wrangler...")
        result = subprocess.run(
            ["npx", "wrangler", "pages", "deploy", "docs/.vitepress/dist",
             "--project-name", "docmcp-knowledge", "--branch", "main",
             "--commit-dirty=true"],
            cwd=str(REPO_ROOT),
            check=True, capture_output=True, text=True,
            timeout=300,
        )
        logger.info(f"  Deploy complete: {result.stdout[-200:]}")
    except subprocess.CalledProcessError as e:
        logger.error(f"  Deploy failed: {e.stderr[-500:]}")
    except Exception as e:
        logger.error(f"  Deploy error: {e}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Automated Regulatory Pipeline")
    parser.add_argument("--framework", help="Process items from specific framework (nmpa, fda, eu_mdr, ...)")
    parser.add_argument("--all", action="store_true", help="Process all frameworks")
    parser.add_argument("--item-id", help="Process a single item by ID")
    parser.add_argument("--dry-run", action="store_true", help="Simulate without writing files")
    parser.add_argument("--fetch-only", action="store_true", help="Only fetch full text, no insight generation")
    parser.add_argument("--insight-only", action="store_true", help="Only generate insights (skip fetch)")
    parser.add_argument("--publish", action="store_true", help="Build and deploy after processing")
    parser.add_argument("--stats", action="store_true", help="Show pipeline state stats")
    parser.add_argument("--reset", action="store_true", help="Reset pipeline state (re-process all)")
    args = parser.parse_args()

    if args.stats:
        state = load_pipeline_state()
        processed = state.get("processed_items", {})
        print(f"Pipeline State:")
        print(f"  Last run: {state.get('last_run', 'never')}")
        print(f"  Processed items: {len(processed)}")
        for status in set(p.get("status") for p in processed.values()):
            count = sum(1 for p in processed.values() if p.get("status") == status)
            print(f"    {status}: {count}")
        return

    if args.reset:
        PIPELINE_STATE_FILE.unlink(missing_ok=True)
        print("Pipeline state reset.")
        return

    frameworks = []
    if args.all:
        frameworks = [p.stem for p in NEWS_DIR.glob("*.json") if p.stem != "_shared"]
    elif args.framework:
        frameworks = [args.framework]
    elif args.item_id:
        # Find framework from item ID prefix
        for f in NEWS_DIR.glob("*.json"):
            if f.stem == "_shared":
                continue
            data = json.loads(f.read_text(encoding="utf-8"))
            for item in data.get("items", []):
                if item.get("id") == args.item_id:
                    frameworks = [f.stem]
                    break
            if frameworks:
                break
        if not frameworks:
            logger.error(f"Item ID not found: {args.item_id}")
            sys.exit(1)
    else:
        parser.print_help()
        sys.exit(1)

    stats = run_pipeline(
        frameworks,
        item_id=args.item_id or "",
        dry_run=args.dry_run,
        fetch_only=args.fetch_only,
        insight_only=args.insight_only,
        publish=args.publish,
    )

    print(f"\n{'='*60}")
    print(f"Pipeline Results:")
    print(f"  Processed: {stats['processed']}")
    print(f"  Published: {stats['published']}")
    print(f"  Skipped:   {stats['skipped']}")
    print(f"  Failed:    {stats['failed']}")


if __name__ == "__main__":
    main()
