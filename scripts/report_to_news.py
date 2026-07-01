#!/usr/bin/env python3
"""Convert fetch_updates.py report into regulatory_news JSON items.

Pipeline:
  1. Read the JSON report from fetch_updates.py
  2. For each detected update, build a RegulatoryNewsItem skeleton
  3. Optionally call LLM (DeepSeek) for bilingual summary generation
  4. Merge new items into existing regulatory_news/{framework}.json
  5. Deduplicate by item ID

Usage:
    python scripts/report_to_news.py --report /tmp/news_report.json [--dry-run]
    python scripts/report_to_news.py --report /tmp/news_report.json --use-llm

Environment:
    LLM_API_KEY   : API key for summary generation (DeepSeek / OpenAI compatible)
    LLM_BASE_URL  : Base URL (default: https://api.deepseek.com/v1)
    LLM_MODEL     : Model name (default: deepseek-chat)
"""

import argparse
import json
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Optional

REPO_ROOT = Path(__file__).resolve().parent.parent
NEWS_DIR = REPO_ROOT / "regulatory_news"

LLM_API_KEY = os.environ.get("LLM_API_KEY", "")
LLM_BASE_URL = os.environ.get("LLM_BASE_URL", "https://api.deepseek.com/v1")
LLM_MODEL = os.environ.get("LLM_MODEL", "deepseek-chat")

CATEGORY_MAP = {
    "eu_mdr/mdcg": ("eu_mdr", "guidance_new"),
    "eu_mdr/standards": ("eu_mdr", "regulation_update"),
    "eu_mdr/regulations": ("eu_mdr", "regulation_update"),
    "eu_mdr/team_nb": ("eu_mdr", "guidance_new"),
    "fda/guidance": ("fda", "guidance_new"),
    "fda/regulations": ("fda", "regulation_update"),
    "fda/standards": ("fda", "standard_revision"),
    "fda/safety": ("fda", "safety_communication"),
    "fda/recall": ("fda", "recall_class1"),
    "fda/cdrh_news": ("fda", "cdrh_news"),
    "nmpa/regulations": ("nmpa", "regulation_update"),
    "nmpa/guidance": ("nmpa", "guidance_new"),
    "nmpa/standards": ("nmpa", "standard_revision"),
    "_shared/standards": ("_shared", "standard_revision"),
    # Tier 1 international markets
    "uk_mhra/safety": ("uk_mhra", "safety_communication"),
    "uk_mhra/regulations": ("uk_mhra", "regulation_update"),
    "canada/safety": ("canada", "safety_communication"),
    "canada/regulations": ("canada", "regulation_update"),
    "australia_tga/safety": ("australia_tga", "safety_communication"),
    "australia_tga/regulations": ("australia_tga", "regulation_update"),
    "japan_pmda/regulations": ("japan_pmda", "regulation_update"),
    "japan_pmda/safety": ("japan_pmda", "safety_communication"),
    "korea_mfds/regulations": ("korea_mfds", "regulation_update"),
    "korea_mfds/safety": ("korea_mfds", "safety_communication"),
}


def generate_item_id(framework: str, title: str, date: str) -> str:
    """Generate a stable item ID from framework + title keywords."""
    slug = re.sub(r"[^a-z0-9]+", "_", title.lower())[:60].strip("_")
    return f"{framework}_{date.replace('-','')[:8]}_{slug}"


_CATEGORY_PROMPTS = {
    "fda/safety": (
        "This is an FDA Safety Communication -- a critical safety alert about medical devices. "
        "The summary MUST cover: (1) what the safety issue is, (2) which devices/manufacturers are affected, "
        "(3) what health risks are involved, (4) what patients/providers should do. "
        "importance should almost always be 'high'."
    ),
    "fda/recall": (
        "This is a Class I medical device recall -- the most serious type. "
        "The summary MUST cover: (1) recalling firm and product, (2) reason for recall (health hazard), "
        "(3) quantity and distribution, (4) recommended actions. "
        "importance should always be 'high'."
    ),
    "fda/cdrh_news": (
        "This is a CDRH (Center for Devices and Radiological Health) news item. "
        "The summary should cover: (1) what was announced, (2) who is affected, "
        "(3) key dates or deadlines, (4) actions needed by manufacturers. "
        "importance: 'high' for new guidance/rules, 'medium' for town halls/updates."
    ),
    "japan_pmda/safety": (
        "This is a Japanese PMDA medical device safety/recall item. "
        "Input may be in Japanese -- translate to English and Chinese. "
        "The summary MUST cover: (1) the device name and manufacturer, (2) recall class (I=most serious, II=moderate, III=minor), "
        "(3) the safety issue or reason for recall, (4) actions needed. "
        "importance: 'high' for Class I recalls, 'medium' for Class II, 'low' for Class III and informational items."
    ),
    "japan_pmda/regulations": (
        "This is a Japanese PMDA regulatory update for medical devices. "
        "Input may be in Japanese -- translate to English and Chinese. "
        "The summary should cover: (1) what changed, (2) which devices are affected, "
        "(3) key dates or deadlines, (4) actions needed by manufacturers. "
        "importance: 'high' for new precaution revisions, 'medium' for guidance updates."
    ),
}


def call_llm_summary_single(item: dict, category: str, context_note: str = "") -> Optional[dict]:
    """Call LLM to generate bilingual summary for a SINGLE news item."""
    if not LLM_API_KEY:
        return None

    try:
        import requests as _requests
    except ImportError:
        return None

    title = item.get("title", "N/A")
    link = item.get("link", "")
    snippet = item.get("snippet", item.get("description", ""))[:400]

    category_hint = _CATEGORY_PROMPTS.get(category, "")
    if category_hint:
        category_hint = f"\nSpecial instructions for this category:\n{category_hint}\n"

    prompt = f"""You are a medical device regulatory affairs expert. Generate a bilingual news summary for this SPECIFIC regulatory item.

Item info:
- Title: {title}
- URL: {link}
- Description: {snippet}
- Category: {category}
- Context: {context_note}
{category_hint}
Generate a JSON object with these exact fields:
{{
  "title_en": "Concise English title (max 120 chars) -- be specific to THIS item",
  "title_zh": "Concise Chinese title (max 80 chars)",
  "summary_en": "2-4 sentence English summary covering: what this specific item is about, who is affected, key actions needed",
  "summary_zh": "2-4 sentence Chinese summary covering the same points",
  "importance": "high|medium|low",
  "tags": ["tag1", "tag2", "tag3"]
}}

Rules:
- Title must be specific to THIS single item, not a summary of multiple items
- If the title mentions a specific product, company, or document, include that
- Summaries should be informative for regulatory affairs professionals
- Tags should be lowercase_underscore format, relevant to medical device compliance
- importance: "high" for new regulations/major guidance/safety alerts/Class I recalls, "medium" for updates/revisions, "low" for minor changes
- Return ONLY the JSON object, no markdown"""

    try:
        resp = _requests.post(
            f"{LLM_BASE_URL.rstrip('/')}/chat/completions",
            headers={
                "Authorization": f"Bearer {LLM_API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": LLM_MODEL,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.2,
            },
            timeout=30,
        )
        resp.raise_for_status()
        content = resp.json()["choices"][0]["message"]["content"]
        content = re.sub(r"```json\s*", "", content)
        content = re.sub(r"```\s*$", "", content)
        return json.loads(content.strip())
    except Exception as e:
        print(f"  LLM error: {e}")
        return None


def _resolve_source_name(url: str) -> str:
    """Resolve human-readable source name from URL domain."""
    url_lower = url.lower()
    for domain, name in [
        ("eur-lex", "EUR-Lex"),
        ("ec.europa.eu", "European Commission"),
        ("accessdata.fda.gov", "FDA CDRH"),
        ("fda.gov", "FDA"),
        ("ecfr.gov", "eCFR"),
        ("govinfo.gov", "Federal Register"),
        ("nmpa.gov.cn", "NMPA"),
        ("iso.org", "ISO"),
        ("iec.ch", "IEC"),
        ("gov.uk", "MHRA (UK)"),
        ("recalls-rappels.canada.ca", "Health Canada"),
        ("canada.ca", "Health Canada"),
        ("tga.gov.au", "TGA (Australia)"),
        ("info.pmda.go.jp", "PMDA (Japan)"),
        ("pmda.go.jp", "PMDA (Japan)"),
        ("mhlw.go.jp", "MHLW (Japan)"),
        ("mfds.go.kr", "MFDS (Korea)"),
    ]:
        if domain in url_lower:
            return name
    return "Official Source"


def build_news_item_from_single(
    item: dict,
    framework: str,
    news_category: str,
    check_type: str,
    source_id: str,
    llm_result: Optional[dict] = None,
    fallback_url: str = "",
) -> dict:
    """Build one RegulatoryNewsItem from a SINGLE detection item."""
    source_url = item.get("link", "") or fallback_url

    if llm_result:
        title_en = llm_result.get("title_en", item.get("title", "")[:120])
        title_zh = llm_result.get("title_zh", title_en)
        summary_en = llm_result.get("summary_en", item.get("description", ""))
        summary_zh = llm_result.get("summary_zh", summary_en)
        importance = llm_result.get("importance", "medium")
        tags = llm_result.get("tags", [])
    else:
        title_en = item.get("title", "Untitled")[:120]
        title_zh = title_en
        desc = item.get("description", "") or item.get("snippet", "")
        summary_en = desc[:500] if desc else title_en
        summary_zh = summary_en
        importance = "medium"
        tags = []

    pub_date = item.get("pub_date", "") or datetime.now().strftime("%Y-%m-%d")
    today = datetime.now().strftime("%Y-%m-%d")
    item_id = generate_item_id(framework, title_en, today)

    return {
        "id": item_id,
        "framework": framework,
        "category": news_category,
        "title": {"en": title_en, "zh": title_zh},
        "summary": {"en": summary_en, "zh": summary_zh},
        "source_url": source_url,
        "source_name": _resolve_source_name(source_url),
        "published_date": pub_date if len(pub_date) == 10 else today,
        "detected_date": datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "importance": importance,
        "tags": tags,
        "related_docs": [],
        "status": "published",
        "_detection": {
            "check_type": check_type,
            "source_id": source_id,
        },
    }


def merge_into_framework(framework: str, new_items: list, dry_run: bool = False) -> int:
    """Merge new items into the framework's news JSON file."""
    fp = NEWS_DIR / f"{framework}.json"
    if fp.exists():
        data = json.loads(fp.read_text(encoding="utf-8"))
    else:
        data = {"framework": framework, "last_updated": "", "items": []}

    existing_ids = {item["id"] for item in data["items"]}
    added = 0
    for item in new_items:
        if item["id"] not in existing_ids:
            det = item.pop("_detection", None)
            data["items"].append(item)
            existing_ids.add(item["id"])
            added += 1
            print(f"  + Added: {item['id']}")
        else:
            print(f"  = Skipped (duplicate): {item['id']}")

    if added > 0 and not dry_run:
        data["last_updated"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
        data["items"].sort(key=lambda x: x.get("published_date", ""), reverse=True)
        fp.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"  Saved {fp} ({len(data['items'])} total items)")

    return added


def main():
    parser = argparse.ArgumentParser(description="Convert update report to news JSON")
    parser.add_argument("--report", required=True, help="Path to news_report.json from fetch_updates.py")
    parser.add_argument("--use-llm", action="store_true", help="Use LLM for bilingual summary generation")
    parser.add_argument("--dry-run", action="store_true", help="Don't write files, just show what would be added")
    args = parser.parse_args()

    report_path = Path(args.report)
    if not report_path.exists():
        print(f"ERROR: Report file not found: {report_path}")
        sys.exit(1)

    report = json.loads(report_path.read_text(encoding="utf-8"))
    updates = report.get("updates", [])
    print(f"Report: {report.get('summary', 'N/A')}")
    print(f"Processing {len(updates)} update(s)...\n")

    if args.use_llm and not LLM_API_KEY:
        print("WARNING: --use-llm specified but LLM_API_KEY not set. Falling back to template-based summaries.\n")

    new_by_framework: dict[str, list] = {}

    for update in updates:
        category_key = update.get("category", "")
        mapping = CATEGORY_MAP.get(category_key)
        if not mapping:
            print(f"SKIP: {category_key} (no mapping)")
            continue

        framework, news_category = mapping
        items = update.get("new_items", update.get("db_confirmed_items", []))
        check_type = update.get("check_type", "")
        source_id = update.get("source_id", "")
        fallback_url = update.get("url", "")
        note = update.get("note", "")

        if not items:
            print(f"SKIP: [{category_key}] no items")
            continue

        print(f"Processing: [{category_key}] {len(items)} item(s) -- {note[:60]}")

        for idx, item in enumerate(items):
            item_title = item.get("title", "")[:60]
            print(f"  Item {idx + 1}/{len(items)}: {item_title}...")

            llm_result = None
            if args.use_llm and LLM_API_KEY:
                llm_result = call_llm_summary_single(
                    item, category_key, context_note=note,
                )
                if llm_result:
                    print(f"    LLM: {llm_result.get('title_en', '')[:60]}")
                time.sleep(1)

            news_item = build_news_item_from_single(
                item, framework, news_category,
                check_type, source_id,
                llm_result=llm_result,
                fallback_url=fallback_url,
            )
            new_by_framework.setdefault(framework, []).append(news_item)

    print(f"\n{'='*50}")
    total_added = 0
    for framework, items in new_by_framework.items():
        print(f"\nFramework: {framework} ({len(items)} new items)")
        added = merge_into_framework(framework, items, dry_run=args.dry_run)
        total_added += added

    mode = "DRY RUN" if args.dry_run else "APPLIED"
    print(f"\n{mode}: {total_added} new item(s) added across {len(new_by_framework)} framework(s)")


if __name__ == "__main__":
    main()
