#!/usr/bin/env python3
"""Detect insight articles superseded by newer knowledge base pages.

Three detection layers:
  1. Manual registry -- known supersessions (maintained by editors)
  2. Heuristic matching -- version strings, date patterns, title overlap
  3. LLM semantic check -- for ambiguous cases (optional, --use-llm)

Actions on superseded articles:
  - Data layer (.zh.md): add superseded_by / superseded_reason front matter
  - Docs layer (docs/zh/...md): inject VitePress warning callout
  - Index (_index.json): update entry status to "superseded"

Integrated into CI via check-updates.yml or run standalone:
    python scripts/detect_superseded_insights.py               # scan only
    python scripts/detect_superseded_insights.py --fix          # apply changes
    python scripts/detect_superseded_insights.py --fix --use-llm  # with LLM check
"""

import json
import logging
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)

REPO = Path(__file__).resolve().parent.parent
INSIGHTS_DIR = REPO / "insights"
DOCS_ZH = REPO / "docs" / "zh"
DOCS_EN = REPO / "docs" / "en"

# ---- Layer 1: Manual supersession registry ----
# Maintained by editors. Each entry maps an insight slug to its replacement.
# When a KB page is updated and an insight is known to be outdated, add it here.
SUPERSESSION_REGISTRY = {
    "mdr-td-bpg": {
        "subcategory": "eu-mdr-updates",
        "superseded_by": "/zh/eu_mdr/td/",
        "reason": "Content updated to Team-NB BPG Rev.4 (2026-04-21); insight was based on V3 (2025-04-09)",
        "reason_zh": "内容已更新至 Team-NB BPG Rev.4 (2026-04-21)，本文基于旧版 V3 (2025-04-09)",
    },
}

# ---- Layer 2: Heuristic topic-to-page mapping ----
# Maps insight title keywords to KB page paths for overlap detection.
# "keywords" are case-insensitive substrings checked against insight title.
TOPIC_KB_MAP = [
    {
        "keywords": ["技术文档", "technical documentation", "td bpg", "team-nb", "team nb"],
        "kb_pages": ["docs/zh/eu_mdr/td/index.md"],
        "regulation": "eu_mdr",
    },
    {
        "keywords": ["classification", "分类", "分类规则"],
        "kb_pages": ["docs/zh/eu_mdr/mdcg/mdcg-2021-24.md"],
        "regulation": "eu_mdr",
    },
    {
        "keywords": ["pmcf", "上市后临床"],
        "kb_pages": ["docs/zh/eu_mdr/td/pmcf.md"],
        "regulation": "eu_mdr",
    },
    {
        "keywords": ["sscp", "安全性和临床性能"],
        "kb_pages": ["docs/zh/eu_mdr/td/sscp.md"],
        "regulation": "eu_mdr",
    },
    {
        "keywords": ["pms", "上市后监督"],
        "kb_pages": ["docs/zh/eu_mdr/td/pms.md"],
        "regulation": "eu_mdr",
    },
    {
        "keywords": ["psur", "定期安全更新"],
        "kb_pages": ["docs/zh/eu_mdr/td/psur.md"],
        "regulation": "eu_mdr",
    },
    {
        "keywords": ["eudamed", "udi"],
        "kb_pages": ["docs/zh/eu_mdr/mdcg/mdcg-2024-11.md"],
        "regulation": "eu_mdr",
    },
    {
        "keywords": ["网络安全", "cybersecurity"],
        "kb_pages": ["docs/zh/eu_mdr/td/cybersecurity.md", "docs/zh/eu_mdr/mdcg/mdcg-2019-16.md"],
        "regulation": "eu_mdr",
    },
]

# Version patterns to extract from content
VERSION_PATTERNS = [
    re.compile(r"(?:Rev\.?\s*|Version\s*|V)(\d+)", re.IGNORECASE),
    re.compile(r"(\d{4})[.\-](\d{2})[.\-](\d{2})[-—]V(\d+)", re.IGNORECASE),
    re.compile(r"BPG\s+Rev\.?\s*(\d+)", re.IGNORECASE),
]


def load_yaml_front_matter(path: Path) -> dict:
    """Parse YAML front matter from markdown file."""
    content = path.read_text(encoding="utf-8")
    if not content.startswith("---"):
        return {}
    end = content.find("---", 3)
    if end < 0:
        return {}
    try:
        import yaml
        return yaml.safe_load(content[3:end]) or {}
    except Exception:
        return {}


def extract_versions(content: str) -> list[str]:
    """Extract version references from content."""
    versions = []
    for pat in VERSION_PATTERNS:
        for m in pat.finditer(content[:2000]):
            versions.append(m.group(0))
    return versions


def _is_already_superseded(data_path: Path) -> bool:
    """Check if data layer file already has superseded_by."""
    try:
        content = data_path.read_text(encoding="utf-8")
        return "superseded_by:" in content
    except Exception:
        return False


def inject_superseded_callout(md_path: Path, superseded_by: str, reason_zh: str, lang: str = "zh") -> bool:
    """Add a warning callout to the top of a docs page."""
    content = md_path.read_text(encoding="utf-8")

    if "superseded" in content.lower() and ":::warning" in content.lower():
        return False
    if "::: warning" in content:
        return False

    if content.startswith("---"):
        end = content.find("---", 3)
        if end > 0:
            front = content[:end + 3]
            body = content[end + 3:]
        else:
            front, body = "", content
    else:
        front, body = "", content

    if lang == "zh":
        callout = f"""

::: warning 本文内容已更新
{reason_zh}。请参阅最新版本：[点击查看]({superseded_by})
:::
"""
    else:
        en_path = superseded_by.replace("/zh/", "/en/")
        callout = f"""

::: warning This article has been superseded
{reason_zh}. See the updated version: [View here]({en_path})
:::
"""

    md_path.write_text(front + callout + body, encoding="utf-8")
    return True


def update_front_matter_superseded(data_path: Path, superseded_by: str, reason: str) -> bool:
    """Add superseded_by field to the data layer front matter."""
    content = data_path.read_text(encoding="utf-8")
    if "superseded_by:" in content:
        return False

    if content.startswith("---"):
        end = content.find("---", 3)
        if end > 0:
            fm = content[:end]
            rest = content[end:]
            fm += f"superseded_by: '{superseded_by}'\nsuperseded_reason: '{reason}'\n"
            data_path.write_text(fm + rest, encoding="utf-8")
            return True
    return False


def update_index_status(index_path: Path, insight_id: str, superseded_by: str) -> bool:
    """Update _index.json entry to mark as superseded."""
    if not index_path.exists():
        return False
    try:
        data = json.loads(index_path.read_text(encoding="utf-8"))
    except Exception:
        return False

    changed = False
    for entry in data.get("entries", []):
        if entry.get("id") == insight_id or entry.get("id") == f"insights-{insight_id}":
            if entry.get("status") != "superseded":
                entry["status"] = "superseded"
                entry["superseded_by"] = superseded_by
                changed = True
                break

    if changed:
        index_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return changed


def heuristic_check(slug: str, subcat: str) -> Optional[dict]:
    """Layer 2: Check if an insight's topic is covered by a KB page with newer content."""
    data_path = INSIGHTS_DIR / subcat / f"{slug}.zh.md"
    if not data_path.exists():
        return None

    content = data_path.read_text(encoding="utf-8")
    title_line = ""
    for line in content.split("\n"):
        if line.strip().startswith("zh:"):
            title_line = line.strip().replace("zh:", "").strip()
            break

    title_lower = title_line.lower()
    insight_versions = extract_versions(content[:3000])

    for mapping in TOPIC_KB_MAP:
        kw_match = any(kw.lower() in title_lower for kw in mapping["keywords"])
        if not kw_match:
            continue

        for kb_page_rel in mapping["kb_pages"]:
            kb_path = REPO / kb_page_rel
            if not kb_path.exists():
                continue

            kb_content = kb_path.read_text(encoding="utf-8")
            kb_versions = extract_versions(kb_content[:3000])

            # Compare versions: if KB has a higher version number
            insight_nums = [int(re.search(r"\d+", v).group()) for v in insight_versions if re.search(r"\d+", v)]
            kb_nums = [int(re.search(r"\d+", v).group()) for v in kb_versions if re.search(r"\d+", v)]

            if kb_nums and insight_nums and max(kb_nums) > max(insight_nums):
                kb_url = "/" + kb_page_rel.replace("docs/", "").replace("/index.md", "/").replace(".md", ".html")
                return {
                    "superseded_by": kb_url,
                    "reason": f"KB page updated to version {max(kb_nums)}; insight referenced version {max(insight_nums)}",
                    "reason_zh": f"知识库页面已更新至版本 {max(kb_nums)}，本文引用的是旧版本 {max(insight_nums)}",
                    "confidence": "heuristic",
                }

    return None


def llm_check_superseded(insight_content: str, kb_content: str, insight_title: str, kb_title: str) -> Optional[dict]:
    """Layer 3: Use LLM to determine if an insight is superseded by a KB page."""
    api_key = os.environ.get("LLM_API_KEY", "")
    base_url = os.environ.get("LLM_BASE_URL", "https://api.deepseek.com/v1")
    model = os.environ.get("LLM_MODEL", "deepseek-v4-pro")

    if not api_key:
        logger.warning("LLM_API_KEY not set, skipping LLM check")
        return None

    try:
        import requests
    except ImportError:
        return None

    prompt = f"""Compare these two documents and determine if Document A (insight article) has been
superseded by Document B (knowledge base page).

Document A (insight): "{insight_title}"
First 2000 chars:
{insight_content[:2000]}

Document B (KB page): "{kb_title}"
First 2000 chars:
{kb_content[:2000]}

Answer in JSON format:
{{
  "superseded": true/false,
  "confidence": 0.0-1.0,
  "reason": "brief explanation",
  "reason_zh": "brief explanation in Chinese"
}}

Only mark as superseded if Document B clearly contains updated/more comprehensive information
on the same topic as Document A. Minor overlaps or related-but-different topics should NOT
be marked as superseded."""

    try:
        resp = requests.post(
            f"{base_url}/chat/completions",
            headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
            json={
                "model": model,
                "messages": [{"role": "user", "content": prompt}],
                "max_tokens": 500,
                "temperature": 0.1,
            },
            timeout=30,
        )
        resp.raise_for_status()
        text = resp.json()["choices"][0]["message"]["content"].strip()
        # Extract JSON from response
        json_match = re.search(r"\{[^{}]+\}", text, re.DOTALL)
        if json_match:
            result = json.loads(json_match.group())
            if result.get("superseded") and result.get("confidence", 0) >= 0.7:
                return result
    except Exception as e:
        logger.error(f"LLM check failed: {e}")

    return None


def scan_all_insights(fix: bool = False, use_llm: bool = False) -> dict:
    """Main scan function. Returns summary of findings."""
    results = {"superseded": [], "warnings": [], "errors": []}

    # ---- Layer 1: Manual registry ----
    logger.info("Layer 1: Checking manual supersession registry...")
    for slug, info in SUPERSESSION_REGISTRY.items():
        subcat = info["subcategory"]
        data_path = INSIGHTS_DIR / subcat / f"{slug}.zh.md"

        if not data_path.exists():
            results["errors"].append(f"Registry: {slug} data file not found")
            continue

        if _is_already_superseded(data_path):
            logger.info(f"  {slug}: already marked as superseded")
            continue

        superseded_by = info["superseded_by"]
        reason = info["reason"]
        reason_zh = info["reason_zh"]

        logger.info(f"  SUPERSEDED (registry): {slug} -> {superseded_by}")
        results["superseded"].append({
            "slug": slug, "subcategory": subcat,
            "superseded_by": superseded_by, "reason": reason,
            "source": "registry",
        })

        if fix:
            _apply_superseded(slug, subcat, superseded_by, reason, reason_zh)

    # ---- Layer 2: Heuristic matching ----
    logger.info("Layer 2: Running heuristic version/topic matching...")
    for subcat_dir in INSIGHTS_DIR.iterdir():
        if not subcat_dir.is_dir() or subcat_dir.name.startswith("_"):
            continue
        for zh_file in subcat_dir.glob("*.zh.md"):
            slug = zh_file.stem.replace(".zh", "")
            subcat = subcat_dir.name

            if slug in SUPERSESSION_REGISTRY:
                continue
            if _is_already_superseded(zh_file):
                continue

            match = heuristic_check(slug, subcat)
            if match:
                logger.info(f"  SUPERSEDED (heuristic): {slug} -> {match['superseded_by']}")
                results["superseded"].append({
                    "slug": slug, "subcategory": subcat,
                    "superseded_by": match["superseded_by"],
                    "reason": match["reason"],
                    "source": "heuristic",
                })
                if fix:
                    _apply_superseded(
                        slug, subcat,
                        match["superseded_by"],
                        match["reason"],
                        match["reason_zh"],
                    )

    # ---- Layer 3: LLM semantic check (optional) ----
    if use_llm:
        logger.info("Layer 3: Running LLM semantic checks on remaining insights...")
        already_checked = {r["slug"] for r in results["superseded"]}

        for subcat_dir in INSIGHTS_DIR.iterdir():
            if not subcat_dir.is_dir() or subcat_dir.name.startswith("_"):
                continue
            for zh_file in subcat_dir.glob("*.zh.md"):
                slug = zh_file.stem.replace(".zh", "")
                if slug in already_checked or _is_already_superseded(zh_file):
                    continue

                insight_content = zh_file.read_text(encoding="utf-8")
                insight_title = ""
                for line in insight_content.split("\n"):
                    if line.strip().startswith("zh:"):
                        insight_title = line.strip().replace("zh:", "").strip()
                        break

                # Find potentially matching KB pages via topic map
                for mapping in TOPIC_KB_MAP:
                    kw_match = any(kw.lower() in insight_title.lower() for kw in mapping["keywords"])
                    if not kw_match:
                        continue
                    for kb_rel in mapping["kb_pages"]:
                        kb_path = REPO / kb_rel
                        if not kb_path.exists():
                            continue
                        kb_content = kb_path.read_text(encoding="utf-8")
                        kb_title = ""
                        for line in kb_content.split("\n"):
                            if line.startswith("# "):
                                kb_title = line[2:].strip()
                                break

                        result = llm_check_superseded(
                            insight_content, kb_content, insight_title, kb_title
                        )
                        if result:
                            kb_url = "/" + kb_rel.replace("docs/", "").replace("/index.md", "/").replace(".md", ".html")
                            logger.info(f"  SUPERSEDED (LLM, conf={result['confidence']}): {slug} -> {kb_url}")
                            results["superseded"].append({
                                "slug": slug, "subcategory": subcat_dir.name,
                                "superseded_by": kb_url,
                                "reason": result.get("reason", "LLM determined superseded"),
                                "source": f"llm (confidence={result['confidence']})",
                            })
                            if fix:
                                _apply_superseded(
                                    slug, subcat_dir.name, kb_url,
                                    result.get("reason", ""),
                                    result.get("reason_zh", result.get("reason", "")),
                                )
                            break

    # Summary
    logger.info(f"\n{'='*60}")
    logger.info(f"Scan complete: {len(results['superseded'])} superseded, "
                f"{len(results['warnings'])} warnings, {len(results['errors'])} errors")
    for r in results["superseded"]:
        logger.info(f"  [{r['source']}] {r['slug']} -> {r['superseded_by']}")
    return results


def _apply_superseded(slug: str, subcat: str, superseded_by: str, reason: str, reason_zh: str):
    """Apply all supersession markers to an insight article."""
    data_path = INSIGHTS_DIR / subcat / f"{slug}.zh.md"
    docs_zh_path = DOCS_ZH / "insights" / subcat / f"{slug}.md"
    docs_en_path = DOCS_EN / "insights" / subcat / f"{slug}.md"
    index_path = INSIGHTS_DIR / subcat / "_index.json"

    if data_path.exists():
        if update_front_matter_superseded(data_path, superseded_by, reason):
            logger.info(f"    Updated data layer: {data_path.relative_to(REPO)}")

    if docs_zh_path.exists():
        if inject_superseded_callout(docs_zh_path, superseded_by, reason_zh, "zh"):
            logger.info(f"    Injected ZH callout: {docs_zh_path.relative_to(REPO)}")

    if docs_en_path.exists():
        if inject_superseded_callout(docs_en_path, superseded_by, reason, "en"):
            logger.info(f"    Injected EN callout: {docs_en_path.relative_to(REPO)}")

    if index_path.exists():
        insight_id = f"insights-{slug}"
        if update_index_status(index_path, insight_id, superseded_by):
            logger.info(f"    Updated index: {index_path.relative_to(REPO)}")


# ---- Integration point: called by auto_regulatory_pipeline.py ----
def check_new_content_supersedes(new_kb_page: str, new_content: str, new_title: str) -> list[dict]:
    """Check if a newly published/updated KB page supersedes any existing insights.

    Called by the regulatory pipeline after publishing a new KB page.
    Returns list of insights that should be marked as superseded.
    """
    candidates = []

    for subcat_dir in INSIGHTS_DIR.iterdir():
        if not subcat_dir.is_dir() or subcat_dir.name.startswith("_"):
            continue
        for zh_file in subcat_dir.glob("*.zh.md"):
            slug = zh_file.stem.replace(".zh", "")
            if _is_already_superseded(zh_file):
                continue

            insight_content = zh_file.read_text(encoding="utf-8")
            insight_title = ""
            for line in insight_content.split("\n"):
                if line.strip().startswith("zh:"):
                    insight_title = line.strip().replace("zh:", "").strip()
                    break

            # Quick keyword overlap check
            new_words = set(re.findall(r"[\w\u4e00-\u9fff]{2,}", new_title.lower()))
            insight_words = set(re.findall(r"[\w\u4e00-\u9fff]{2,}", insight_title.lower()))
            overlap = len(new_words & insight_words) / max(len(insight_words), 1)

            if overlap > 0.3:
                # Potential overlap; check versions
                new_versions = extract_versions(new_content[:3000])
                insight_versions = extract_versions(insight_content[:3000])

                new_nums = [int(re.search(r"\d+", v).group()) for v in new_versions if re.search(r"\d+", v)]
                ins_nums = [int(re.search(r"\d+", v).group()) for v in insight_versions if re.search(r"\d+", v)]

                if new_nums and ins_nums and max(new_nums) > max(ins_nums):
                    candidates.append({
                        "slug": slug,
                        "subcategory": subcat_dir.name,
                        "insight_title": insight_title,
                        "overlap_score": overlap,
                        "version_new": max(new_nums),
                        "version_old": max(ins_nums),
                    })

    return candidates


if __name__ == "__main__":
    fix = "--fix" in sys.argv
    use_llm = "--use-llm" in sys.argv

    if not fix:
        logger.info("Scan-only mode. Use --fix to apply changes, --use-llm for LLM checks.\n")

    scan_all_insights(fix=fix, use_llm=use_llm)
