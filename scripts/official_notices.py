#!/usr/bin/env python3
"""Official notices, announcements, regulations, and guidance.

Two collectors feed the compliance news files:

- gov.cn policy search. It is a JSON API and does not sit behind the NMPA
  Ruishu challenge, so the weekly job can read mirrored 公告/通知/指导原则.
- A desktop browser inbox. Reguverse Desktop opens the real NMPA and CMDE
  pages and can drop scripts/.browser_inbox/notices.json for the same job.

Vigilance feeds (FSCA, recalls) stay available but are capped here so a
successful safety API cannot crowd out a thin regulatory page.
"""

from __future__ import annotations

import html
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Optional
from urllib.parse import urlparse

GOV_SEARCH_URL = "https://sousuo.www.gov.cn/search-gov/data"
INBOX_PATH = Path(__file__).resolve().parent / ".browser_inbox" / "notices.json"

VIGILANCE_CATEGORIES = {
    "safety_communication",
    "recall_class1",
    "recall",
    "enforcement",
}

CATEGORY_KEY = {
    "guidance_new": "nmpa/guidance",
    "standard_revision": "nmpa/standards",
    "regulation_update": "nmpa/regulations",
    "notice": "nmpa/notice",
}

_VIGILANCE_ONLY = re.compile(r"召回|警戒|不良事件|FSCA|field safety|recall", re.I)
_KEEP_WITH_VIGILANCE = re.compile(r"公告|通告|通知|指导原则|办法|规定")
_GUIDANCE = re.compile(r"指导原则|指南|guidance", re.I)
_STANDARD = re.compile(r"行业标准|国家标准|YY/T|YY／T|GB/T|GB／T")
_REGULATION = re.compile(r"公告|通告|通知|决定|办法|规定|条例|规章")
_DEVICE = re.compile(r"器械|体外诊断|诊断试剂|注册审查")
_NOT_DEVICE = re.compile(r"药品|化妆品|中药|疫苗")
_OFFICIAL_HOSTS = (
    "nmpa.gov.cn",
    "cmde.org.cn",
    "samr.gov.cn",
    "nifdc.org.cn",
    "gov.cn",
)


def strip_markup(value: str) -> str:
    text = html.unescape(value or "")
    text = re.sub(r"<[^>]+>", "", text)
    return re.sub(r"\s+", " ", text).strip()


def classify_title(title: str, strict: bool = False) -> Optional[str]:
    """Map an official title onto a news category.

    Company-level recall lines are dropped. A regulation that happens to
    mention 召回 (召回管理办法, 召回通告) stays.
    strict=True requires 公告/通知/指导原则/标准. The gov.cn search uses
    that. A scoped NMPA or CMDE list may also keep a plain notice.
    """
    text = re.sub(r"\s+", "", strip_markup(title))
    if len(text) < 8:
        return None
    if _VIGILANCE_ONLY.search(text) and not _KEEP_WITH_VIGILANCE.search(text):
        return None
    if _GUIDANCE.search(text):
        return "guidance_new"
    if _STANDARD.search(text):
        return "standard_revision"
    if _REGULATION.search(text):
        return "regulation_update"
    if strict:
        return None
    return "notice"


def is_device_policy(title: str) -> bool:
    text = strip_markup(title)
    if _NOT_DEVICE.search(text) and not re.search(r"器械|体外诊断", text):
        return False
    return _DEVICE.search(text) is not None


def normalize_date(value: str) -> str:
    text = (value or "").strip().replace(".", "-").replace("/", "-")
    match = re.match(r"(20\d{2})-(\d{1,2})-(\d{1,2})", text)
    if not match:
        return ""
    month = int(match.group(2))
    day = int(match.group(3))
    if not (1 <= month <= 12 and 1 <= day <= 31):
        return ""
    return f"{match.group(1)}-{month:02d}-{day:02d}"


def importance_for(category: str) -> str:
    if category in ("guidance_new", "regulation_update"):
        return "high"
    return "medium"


def allowed_official_url(url: str) -> bool:
    if not url or not url.startswith("https://") or len(url) > 500:
        return False
    host = (urlparse(url).hostname or "").lower()
    return any(host == suffix or host.endswith("." + suffix) for suffix in _OFFICIAL_HOSTS)


def parse_gov_policy(payload: dict) -> list[dict]:
    rows = ((payload or {}).get("searchVO") or {}).get("listVO") or []
    items = []
    seen = set()
    for row in rows:
        title = strip_markup(str(row.get("title") or ""))
        link = str(row.get("url") or "").strip()
        if link and not link.startswith("http"):
            link = "https://" + link
        if not title or not allowed_official_url(link) or link in seen:
            continue
        if not is_device_policy(title):
            continue
        category = classify_title(title, strict=True)
        if not category:
            continue
        seen.add(link)
        org = strip_markup(str(row.get("puborg") or "")) or "中国政府网"
        items.append({
            "title": title,
            "link": link,
            "pub_date": normalize_date(str(row.get("pubtimeStr") or "")),
            "description": strip_markup(str(row.get("summary") or ""))[:500],
            "category_key": CATEGORY_KEY[category],
            "importance": importance_for(category),
            "source_name": org,
        })
    items.sort(key=lambda item: item.get("pub_date") or "", reverse=True)
    return items


def choose_unseen(entries: list[dict], seen_titles: set, baseline_limit: int = 25) -> list[dict]:
    """First sight of a historical page publishes the filtered page, capped.

    Later runs publish whatever is actually new, up to 20.
    """
    unseen = [entry for entry in entries if entry.get("title") not in seen_titles]
    unseen.sort(key=lambda entry: entry.get("pub_date") or "", reverse=True)
    if not seen_titles:
        return unseen[:baseline_limit]
    return unseen[:20]


def cap_batch(items: list, news_category: str, vigilance_cap: int = 4, other_cap: int = 30) -> list:
    cap = vigilance_cap if news_category in VIGILANCE_CATEGORIES else other_cap
    dated = [item for item in items if len(str(item.get("pub_date") or "")) >= 10]
    undated = [item for item in items if item not in dated]
    dated.sort(key=lambda item: item.get("pub_date") or "", reverse=True)
    return (dated + undated)[:cap]


def _update_shell(source_id: str, source: dict, check_type: str, note: str, items: list) -> dict:
    return {
        "source_id": source_id,
        "name": source.get("name", source_id),
        "url": source.get("url", ""),
        "category": source.get("category", ""),
        "check_type": check_type,
        "detected_at": datetime.now().isoformat(),
        "note": note,
        "new_items": items,
    }


class GovPolicyChecker:
    """Read NMPA documents mirrored in the gov.cn policy library."""

    def __init__(self, session, state: dict):
        self.session = session
        self.state = state

    def check(self, source_id: str, source: dict) -> Optional[dict]:
        prev = self.state.get(source_id, {})
        seen = set(prev.get("seen_titles", []))
        queries = source.get("queries") or ["医疗器械", "指导原则"]
        entries = []
        seen_links = set()
        try:
            for query in queries:
                for page in range(int(source.get("pages") or 2)):
                    resp = self.session.get(
                        source.get("url") or GOV_SEARCH_URL,
                        params={
                            "t": "zhengcelibrary_bm",
                            "q": query,
                            "sort": "pubtime",
                            "sortType": 1,
                            "searchfield": "title",
                            "p": page,
                            "n": 20,
                        },
                        timeout=30,
                        headers={
                            "User-Agent": "Mozilla/5.0",
                            "Accept": "application/json",
                        },
                    )
                    resp.raise_for_status()
                    for item in parse_gov_policy(resp.json()):
                        if item["link"] in seen_links:
                            continue
                        seen_links.add(item["link"])
                        entries.append(item)
        except Exception as exc:
            print(f"    ERROR gov policy: {exc}")
            return None

        entries.sort(key=lambda item: item.get("pub_date") or "", reverse=True)
        if not entries:
            print("    WARNING: gov.cn returned no device policy items")
            return None

        chosen = choose_unseen(entries, seen)
        titles = list(seen)
        for entry in entries:
            if entry["title"] not in titles:
                titles.append(entry["title"])
        self.state[source_id] = {
            "url": source.get("url") or GOV_SEARCH_URL,
            "last_checked": datetime.now().isoformat(),
            "seen_titles": titles[-500:],
        }
        print(f"    INFO: gov.cn device policy {len(entries)}, new {len(chosen)}")
        if not chosen:
            return None
        return _update_shell(
            source_id, source, "gov_policy",
            f"{len(chosen)} official notice(s) from gov.cn policy library",
            chosen,
        )


def load_browser_inbox(path: Path) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    items = []
    seen = set()
    for raw in data.get("items") or []:
        title = strip_markup(str(raw.get("title") or ""))
        link = str(raw.get("link") or raw.get("source_url") or "").strip()
        if not title or not allowed_official_url(link) or link in seen:
            continue
        category = classify_title(title, strict=False)
        if not category or category not in CATEGORY_KEY:
            continue
        seen.add(link)
        body = strip_markup(str(raw.get("description") or raw.get("body") or ""))
        items.append({
            "title": title,
            "link": link,
            "pub_date": normalize_date(str(raw.get("pub_date") or raw.get("published_date") or "")),
            "description": body[:500],
            "category_key": CATEGORY_KEY[category],
            "importance": importance_for(category),
            "source_name": str(raw.get("source_name") or "")[:40],
        })
    return items


class BrowserInboxChecker:
    """Read notices the desktop browser already collected."""

    def __init__(self, state: dict):
        self.state = state

    def check(self, source_id: str, source: dict) -> Optional[dict]:
        path = Path(source.get("inbox_path") or INBOX_PATH)
        if not path.is_file():
            return None
        prev = self.state.get(source_id, {})
        seen = set(prev.get("seen_titles", []))
        try:
            entries = load_browser_inbox(path)
        except Exception as exc:
            print(f"    ERROR browser inbox: {exc}")
            return None
        chosen = [entry for entry in entries if entry["title"] not in seen]
        titles = list(seen)
        for entry in entries:
            if entry["title"] not in titles:
                titles.append(entry["title"])
        self.state[source_id] = {
            "url": source.get("url", ""),
            "last_checked": datetime.now().isoformat(),
            "seen_titles": titles[-500:],
        }
        if not chosen:
            print(f"    INFO: browser inbox has no new notices ({len(entries)} seen)")
            return None
        return _update_shell(
            source_id, source, "browser_inbox",
            f"{len(chosen)} official notice(s) from the desktop browser",
            chosen,
        )
