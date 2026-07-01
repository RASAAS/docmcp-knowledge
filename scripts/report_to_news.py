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
}


def call_llm_summary(title: str, note: str, items: list, category: str) -> Optional[dict]:
    """Call LLM to generate bilingual summary for a detected update."""
    if not LLM_API_KEY:
        return None

    try:
        import requests
    except ImportError:
        return None

    context_items = "\n".join(
        f"- {it.get('title', 'N/A')} | {it.get('link', '')} | {it.get('snippet', it.get('description', ''))[:200]}"
        for it in items[:5]
    )

    category_hint = _CATEGORY_PROMPTS.get(category, "")
    if category_hint:
        category_hint = f"\nSpecial instructions for this category:\n{category_hint}\n"

    prompt = f"""You are a medical device regulatory affairs expert. Based on the following detected regulatory update, generate a bilingual news summary.

Detection info:
- Category: {category}
- Detection note: {note}
- Related items:
{context_items}
{category_hint}
Generate a JSON object with these exact fields:
{{
  "title_en": "Concise English title (max 120 chars)",
  "title_zh": "Concise Chinese title (max 80 chars)",
  "summary_en": "2-4 sentence English summary covering: what changed, effective date, who is affected, key actions needed",
  "summary_zh": "2-4 sentence Chinese summary covering the same points",
  "importance": "high|medium|low",
  "tags": ["tag1", "tag2", "tag3"],
  "source_url": "the most relevant official source URL from the items above"
}}

Rules:
- Titles should be factual and specific (include document numbers, dates)
- Summaries should be informative for regulatory affairs professionals
- Tags should be lowercase_underscore format, relevant to medical device compliance
- importance: "high" for new regulations/major guidance/safety alerts/Class I recalls, "medium" for updates/revisions, "low" for minor changes
- source_url must be from an official government or standards body domain
- Return ONLY the JSON object, no markdown"""

    try:
        resp = requests.post(
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


def build_news_item(update: dict, llm_result: Optional[dict]) -> Optional[dict]:
    """Convert a fetch_updates detection into a RegulatoryNewsItem."""
    category_key = update.get("category", "")
    mapping = CATEGORY_MAP.get(category_key)
    if not mapping:
        print(f"  SKIP: unknown category {category_key}")
        return None

    framework, news_category = mapping
    note = update.get("note", "")
    items = update.get("new_items", update.get("db_confirmed_items", []))
    check_type = update.get("check_type", "")
    source_url = update.get("url", "")

    if llm_result:
        title_en = llm_result.get("title_en", note[:120])
        title_zh = llm_result.get("title_zh", note[:80])
        summary_en = llm_result.get("summary_en", note)
        summary_zh = llm_result.get("summary_zh", note)
        importance = llm_result.get("importance", "medium")
        tags = llm_result.get("tags", [])
        if llm_result.get("source_url"):
            source_url = llm_result["source_url"]
    else:
        first_item = items[0] if items else {}
        title_en = first_item.get("title", note[:120])
        title_zh = title_en
        summary_en = note
        summary_zh = note
        importance = "medium"
        tags = []
        if first_item.get("link"):
            source_url = first_item["link"]

    today = datetime.now().strftime("%Y-%m-%d")
    item_id = generate_item_id(framework, title_en, today)

    source_name = "Official Source"
    if "eur-lex" in source_url.lower():
        source_name = "EUR-Lex"
    elif "ec.europa.eu" in source_url.lower():
        source_name = "European Commission"
    elif "accessdata.fda.gov" in source_url.lower():
        source_name = "FDA CDRH"
    elif "fda.gov" in source_url.lower():
        source_name = "FDA"
    elif "ecfr.gov" in source_url.lower():
        source_name = "eCFR"
    elif "govinfo.gov" in source_url.lower():
        source_name = "Federal Register"
    elif "nmpa.gov.cn" in source_url.lower():
        source_name = "NMPA"
    elif "iso.org" in source_url.lower():
        source_name = "ISO"
    elif "iec.ch" in source_url.lower():
        source_name = "IEC"
    elif "gov.uk" in source_url.lower():
        source_name = "MHRA (UK)"
    elif "canada.ca" in source_url.lower() or "recalls-rappels.canada.ca" in source_url.lower():
        source_name = "Health Canada"
    elif "tga.gov.au" in source_url.lower():
        source_name = "TGA (Australia)"
    elif "pmda.go.jp" in source_url.lower():
        source_name = "PMDA (Japan)"
    elif "mhlw.go.jp" in source_url.lower():
        source_name = "MHLW (Japan)"
    elif "mfds.go.kr" in source_url.lower():
        source_name = "MFDS (Korea)"

    return {
        "id": item_id,
        "framework": framework,
        "category": news_category,
        "title": {"en": title_en, "zh": title_zh},
        "summary": {"en": summary_en, "zh": summary_zh},
        "source_url": source_url,
        "source_name": source_name,
        "published_date": today,
        "detected_date": datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "importance": importance,
        "tags": tags,
        "related_docs": [],
        "status": "published",
        "_detection": {
            "check_type": check_type,
            "source_id": update.get("source_id", ""),
            "original_note": note,
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

        framework = mapping[0]
        print(f"Processing: [{category_key}] {update.get('note', '')[:80]}")

        llm_result = None
        if args.use_llm and LLM_API_KEY:
            items = update.get("new_items", update.get("db_confirmed_items", []))
            llm_result = call_llm_summary(
                update.get("name", ""),
                update.get("note", ""),
                items,
                category_key,
            )
            if llm_result:
                print(f"  LLM summary generated: {llm_result.get('title_en', '')[:60]}...")
            time.sleep(1)

        news_item = build_news_item(update, llm_result)
        if news_item:
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
