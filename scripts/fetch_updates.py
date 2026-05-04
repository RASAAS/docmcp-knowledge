#!/usr/bin/env python3
"""
Automated Regulatory Update Monitoring Script
Checks official sources for new/updated regulatory content and creates update reports.

Strategy (4-layer detection with DB comparison):
  Layer 1: RSS Feed          - FDA Medical Devices RSS (real-time, no anti-scraping)
  Layer 2: Structured API    - eCFR Versioner API, EUR-Lex (replaces unreliable http_head)
  Layer 3: Vertex AI Search  - Preferred: searchLite API (free 10K/month, site-restricted)
           (Google CSE)      - Legacy fallback (sunsets 2027-01-01)
  Layer 4: OpenFDA API       - FDA guidance search via official API
  Filter:  DatabaseComparator - Compare detections against existing _index.json data

Usage:
    python scripts/fetch_updates.py --check-all
    python scripts/fetch_updates.py --check eu_mdr
    python scripts/fetch_updates.py --check nmpa
    python scripts/fetch_updates.py --check fda
    python scripts/fetch_updates.py --report  # JSON report for GitHub Actions
    python scripts/fetch_updates.py --analyze-versions  # LLM version analysis

Batched cron schedule (weekly, by regulation group):
  Mon: eu_mdr   Wed: fda   Fri: nmpa   1st of month: shared
"""

import argparse
import json
import os
import re
import sys
import time
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Optional
from urllib.parse import urlparse

try:
    import requests
except ImportError:
    print("ERROR: requests not installed. Run: pip install requests")
    sys.exit(1)

ROOT = Path(__file__).parent.parent
VERSION_REGISTRY_PATH = ROOT / "scripts" / "version_registry.json"

# ---------------------------------------------------------------------------
# Environment variables (set as GitHub Secrets / local .env)
# ---------------------------------------------------------------------------
# Vertex AI Search (preferred -- replaces CSE from 2027-01-01)
VERTEX_AI_PROJECT_ID = os.environ.get("VERTEX_AI_PROJECT_ID", "")
VERTEX_AI_SEARCH_APP_ID = os.environ.get("VERTEX_AI_SEARCH_APP_ID", "")
VERTEX_AI_SEARCH_API_KEY = os.environ.get("VERTEX_AI_SEARCH_API_KEY", "")

# Legacy Google CSE (fallback if Vertex AI not configured; sunsets 2027-01-01)
GOOGLE_SEARCH_API_KEY = os.environ.get("GOOGLE_SEARCH_API_KEY", "")
GOOGLE_SEARCH_ENGINE_ID = os.environ.get("GOOGLE_SEARCH_ENGINE_ID", "")
FDA_API_KEY = os.environ.get("FDA_API_KEY", "")

# LLM (OneAPI-compatible, e.g. https://api.reguverse.com/v1)
# LLM_API_KEY   : API key for the LLM provider
# LLM_BASE_URL  : Base URL of the OpenAI-compatible endpoint (no trailing slash)
# LLM_MODEL     : Model name, e.g. deepseek-chat, gpt-4o-mini
LLM_API_KEY = os.environ.get("LLM_API_KEY", "")
LLM_BASE_URL = os.environ.get("LLM_BASE_URL", "https://api.openai.com/v1")
LLM_MODEL = os.environ.get("LLM_MODEL", "deepseek-chat")

# ---------------------------------------------------------------------------
# Source definitions
# ---------------------------------------------------------------------------
SOURCES = {
    "eu_mdr": {
        "harmonised_standards": {
            "name": "EU MDR Harmonised Standards (EUR-Lex Amendment Check)",
            "url": "https://eur-lex.europa.eu/eli/dec_impl/2021/1182/oj",
            "check_type": "eurlex_amendment",
            "category": "eu_mdr/standards",
            "note": "Checks EUR-Lex for new CID amendments to base decision 2021/1182.",
        },
        "mdcg_guidance": {
            "name": "MDCG Guidance Documents",
            "url": "https://health.ec.europa.eu/medical-devices-sector/new-regulations/guidance-mdcg-endorsed-documents-and-other-guidance_en",
            "check_type": "google_search",
            "category": "eu_mdr/mdcg",
            "google_query": "site:health.ec.europa.eu MDCG guidance medical devices",
            "date_restrict": "y2",
            "title_filter": r"MDCG\s+20\d{2}[-/]\d+",
        },
        "mdcg_guidance_google": {
            "name": "MDCG Guidance (Google CSE)",
            "url": "https://health.ec.europa.eu/medical-devices-sector/new-regulations/guidance-mdcg-endorsed-documents-and-other-guidance_en",
            "check_type": "google_search",
            "category": "eu_mdr/mdcg",
            "google_query": "MDCG guidance medical device",
            "date_restrict": "y2",
            "title_filter": r"MDCG\s+20\d{2}[-/]\d+",
        },
        "team_nb": {
            "name": "TEAM-NB Position Papers",
            "url": "https://www.team-nb.org/",
            "check_type": "google_search",
            "category": "eu_mdr/team_nb",
            "google_query": "site:team-nb.org position paper",
            "date_restrict": "y2",
            "title_filter": r"(?i)position\s+paper|guidance\s+note|team[- ]?nb",
        },
    },
    "fda": {
        "guidance_openfda": {
            "name": "FDA Guidance Documents (OpenFDA API)",
            "url": "https://api.fda.gov/other/guidance.json",
            "check_type": "openfda_guidance",
            "category": "fda/guidance",
        },
        "guidance_google": {
            "name": "FDA Medical Device Guidance (Google Search)",
            "url": "https://www.fda.gov/regulatory-information/search-fda-guidance-documents",
            "check_type": "google_search",
            "category": "fda/guidance",
            "google_query": "site:fda.gov/regulatory-information/search-fda-guidance-documents medical device guidance final",
            "date_restrict": "y2",
            "title_filter": r"(?i)guidance|premarket|510\(k\)|PMA|De\s*Novo|cybersecurity|biocompatibility|software|clinical|labeling|UDI",
        },
        "consensus_standards": {
            "name": "FDA Recognized Consensus Standards (Google CSE)",
            "url": "https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfStandards/search.cfm",
            "check_type": "google_search",
            "category": "fda/standards",
            "google_query": "site:accessdata.fda.gov consensus standards recognized medical device",
            "date_restrict": "y2",
            "title_filter": r"(?i)standard|consensus|ISO|IEC|ASTM|AAMI",
        },
        "regulations_ecfr": {
            "name": "FDA 21 CFR Medical Device Parts (eCFR API)",
            "url": "https://www.ecfr.gov/api/versioner/v1/titles.json",
            "check_type": "ecfr_api",
            "category": "fda/regulations",
            "note": "Checks eCFR Versioner API for Title 21 amendment dates, scoped to Parts 800-898.",
        },
    },
    "nmpa": {
        "cmde_guidance": {
            "name": "CMDE Guidance Principles Index",
            "url": "https://www.cmde.org.cn/flfg/zdyz/",
            "check_type": "google_search",
            "category": "nmpa/guidance",
            "google_query": "site:cmde.org.cn 指导原则 医疗器械",
            "date_restrict": "y1",
            "title_filter": r"(指导原则|技术审查|审查要点|技术指导)",
        },
        "nmpa_regulations": {
            "name": "NMPA Medical Device Regulations (SAMR)",
            "url": "https://www.samr.gov.cn/zw/zfxxgk/fdzdgknr/fgs/",
            "check_type": "google_search",
            "category": "nmpa/regulations",
            "google_query": "site:samr.gov.cn 医疗器械 部门规章",
            "date_restrict": "y1",
            "title_filter": r"(规定|办法|条例|通告|公告|令).{0,30}(医疗器械|体外诊断|器械)",
        },
        "nmpa_announcements": {
            "name": "NMPA Medical Device Announcements",
            "url": "https://www.nmpa.gov.cn/ylqx/ylqxggtg/",
            "check_type": "google_search",
            "category": "nmpa/regulations",
            "google_query": "site:nmpa.gov.cn 医疗器械 公告 通告",
            "date_restrict": "y1",
            "title_filter": r"(医疗器械|体外诊断).{0,20}(公告|通告|通知|决定)",
        },
        "nmpa_standards": {
            "name": "NMPA Medical Device Standards (YY/GB)",
            "url": "https://std.samr.gov.cn",
            "check_type": "google_search",
            "category": "nmpa/standards",
            "google_query": "site:std.samr.gov.cn YY 医疗器械",
            "date_restrict": "y2",
            "title_filter": r"YY[/T\s]*\d{4,5}|GB[/T\s]*\d{4,5}",
        },
    },
    "shared": {
        "iso_tc210": {
            "name": "ISO TC 210 Medical Device Standards",
            "url": "https://www.iso.org/committee/54892/x/catalogue/",
            "check_type": "google_search",
            "category": "_shared/standards",
            "google_query": "site:iso.org 13485 OR 14971 OR 62304 OR 10993 medical device",
            "date_restrict": "y2",
            "title_filter": r"ISO\s+\d{4,5}|IEC\s+\d{4,5}",
        },
        "iec_tc62": {
            "name": "IEC TC 62 Medical Electrical Equipment Standards",
            "url": "https://www.iec.ch/dyn/www/f?p=103:7:::::FSP_ORG_ID:1245",
            "check_type": "google_search",
            "category": "_shared/standards",
            "google_query": "site:iec.ch 60601 OR 62133 medical device standard",
            "date_restrict": "y2",
            "title_filter": r"IEC\s+\d{4,5}|ISO\s+\d{4,5}",
        },
    },
}

# Medical device eCFR parts (800-898)
ECFR_MD_PARTS = set(range(800, 899))


# ---------------------------------------------------------------------------
# Version Registry
# ---------------------------------------------------------------------------

class VersionRegistry:
    """Tracks version history for all regulatory documents."""

    def __init__(self, path: Path = VERSION_REGISTRY_PATH):
        self.path = path
        self.data = self._load()

    def _load(self) -> dict:
        if self.path.exists():
            try:
                with open(self.path, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                pass
        return {"documents": {}, "last_updated": None}

    def save(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.data["last_updated"] = datetime.now().isoformat()
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)

    def get(self, doc_id: str) -> Optional[dict]:
        return self.data["documents"].get(doc_id)

    def upsert(self, doc_id: str, current: dict):
        existing = self.data["documents"].get(doc_id, {})
        history = existing.get("history", [])
        if existing.get("current"):
            history.append(existing["current"])
        self.data["documents"][doc_id] = {"current": current, "history": history}

    def find_outdated(self, days: int = 180) -> list:
        cutoff = datetime.now() - timedelta(days=days)
        result = []
        for doc_id, doc in self.data["documents"].items():
            lv = doc.get("current", {}).get("last_verified")
            if lv:
                try:
                    if datetime.fromisoformat(lv) < cutoff:
                        result.append(doc_id)
                except Exception:
                    pass
        return result


# ---------------------------------------------------------------------------
# Database Comparator -- compares detections against existing _index.json
# ---------------------------------------------------------------------------

class DatabaseComparator:
    """Loads all _index.json files and version_registry.json to classify detections."""

    def __init__(self, root: Path = ROOT):
        self.root = root
        self.mdcg_ids: set[str] = set()
        self.mdcg_titles: set[str] = set()
        self.standards_latest_amendment: str = ""
        self.eu_reg_ids: set[str] = set()
        self.nmpa_reg_titles: set[str] = set()
        self.nmpa_guidance_titles: set[str] = set()
        self.fda_guidance_titles: set[str] = set()
        self.fda_guidance_ids: set[str] = set()
        self.db_stats: dict[str, dict] = {}
        self._load_all()

    def _load_json(self, path: Path) -> dict:
        if not path.exists():
            return {}
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}

    def _load_all(self):
        mdcg = self._load_json(self.root / "eu_mdr" / "mdcg" / "_index.json")
        for entry in mdcg.get("entries", []):
            eid = entry.get("id", "")
            self.mdcg_ids.add(eid)
            for lang in ("zh", "en"):
                t = (entry.get("title") or {}).get(lang, "")
                if t:
                    self.mdcg_titles.add(t.strip().lower())
        self._mdcg_entries = mdcg.get("entries", [])
        self.db_stats["eu_mdr/mdcg"] = {"count": len(self.mdcg_ids)}

        stds = self._load_json(self.root / "eu_mdr" / "standards" / "_index.json")
        self.standards_latest_amendment = stds.get("latest_amendment", "")
        self.db_stats["eu_mdr/standards"] = {
            "count": stds.get("total_standards", 0),
            "latest_amendment": self.standards_latest_amendment,
        }

        regs = self._load_json(self.root / "eu_mdr" / "regulations" / "_index.json")
        for doc in regs.get("documents", []):
            self.eu_reg_ids.add(doc.get("id", ""))
        self.db_stats["eu_mdr/regulations"] = {"count": len(self.eu_reg_ids)}

        nmpa_reg = self._load_json(self.root / "nmpa" / "regulations" / "_index.json")
        for entry in nmpa_reg.get("entries", []):
            t = (entry.get("title") or {}).get("zh", "")
            if t:
                self.nmpa_reg_titles.add(t.strip())
        self.db_stats["nmpa/regulations"] = {"count": len(self.nmpa_reg_titles)}

        nmpa_guide = self._load_json(self.root / "nmpa" / "guidance" / "_index.json")
        for entry in nmpa_guide.get("entries", []):
            t = (entry.get("title") or {}).get("zh", "")
            if t:
                self.nmpa_guidance_titles.add(t.strip())
        self.db_stats["nmpa/guidance"] = {"count": len(self.nmpa_guidance_titles)}

        vreg = self._load_json(self.root / "scripts" / "version_registry.json")
        for doc_id, doc in vreg.get("documents", {}).items():
            cur = doc.get("current", {})
            title = cur.get("title", "")
            if title and "fda" in doc_id.lower():
                self.fda_guidance_titles.add(title.strip().lower())
                self.fda_guidance_ids.add(doc_id)
        self.db_stats["fda/guidance"] = {"count": len(self.fda_guidance_titles)}

    def classify(self, category: str, title: str, link: str = "", date: str = "") -> tuple[str, str]:
        """Classify a detection against the database.

        Returns: ('new', description) | ('update', diff) | ('known', '') | ('irrelevant', reason)
        """
        title_lower = title.strip().lower()

        if category == "eu_mdr/mdcg":
            mdcg_match = re.search(r"MDCG\s+(20\d{2}[-/]\d+)", title, re.IGNORECASE)
            if not mdcg_match:
                return ("irrelevant", "No MDCG ID pattern in title")
            mdcg_id = mdcg_match.group(1).replace("/", "-")
            normalized = f"mdcg-{mdcg_id}"

            # Check for revision indicator in the search result title
            rev_match = re.search(r"[Rr]ev[\.\s]*(\d+)", title)
            new_rev = rev_match.group(0).strip() if rev_match else ""

            if normalized in self.mdcg_ids or f"MDCG {mdcg_id}" in self.mdcg_ids:
                if new_rev:
                    # Search result mentions a revision -- check if our DB already has it
                    db_entry = next(
                        (e for e in self._mdcg_entries if e.get("id") == normalized), None
                    )
                    db_rev = ""
                    if db_entry:
                        db_rev = db_entry.get("revision", "")
                        for lang in ("zh", "en"):
                            t = (db_entry.get("title") or {}).get(lang, "")
                            if t and not db_rev:
                                rm = re.search(r"[Rr]ev[\.\s]*(\d+)", t)
                                if rm:
                                    db_rev = rm.group(0).strip()
                    if db_rev and db_rev.lower().replace(" ", "") == new_rev.lower().replace(" ", ""):
                        return ("known", "")
                    return ("update", f"Revision update: {normalized} has {new_rev} (DB: {db_rev or 'original'})")
                return ("known", "")
            return ("new", f"New MDCG document: {mdcg_match.group(0)}")

        elif category == "eu_mdr/standards":
            cid_match = re.search(r"20\d{2}/\d+", title)
            if cid_match:
                cid = cid_match.group(0)
                if self.standards_latest_amendment and cid > self.standards_latest_amendment:
                    return ("update", f"New amendment {cid} (DB latest: {self.standards_latest_amendment})")
                return ("known", "")
            return ("irrelevant", "No CID amendment number found")

        elif category == "nmpa/regulations":
            for known in self.nmpa_reg_titles:
                if known in title or title in known:
                    return ("known", "")
            return ("new", f"Potentially new NMPA regulation")

        elif category == "nmpa/guidance":
            for known in self.nmpa_guidance_titles:
                if known in title or title in known:
                    return ("known", "")
            return ("new", f"Potentially new NMPA guidance")

        elif category == "fda/guidance":
            for known in self.fda_guidance_titles:
                if known in title_lower or title_lower in known:
                    return ("known", "")
            return ("new", f"Potentially new FDA guidance")

        elif category in ("_shared/standards", "fda/standards", "nmpa/standards"):
            std_match = re.search(r"(ISO|IEC|ASTM|AAMI|YY|GB)\s*[/T]*\s*(\d{4,5})", title, re.IGNORECASE)
            if not std_match:
                return ("irrelevant", "No standard number pattern found")
            return ("new", f"Standard reference: {std_match.group(0)}")

        return ("new", "Unclassified category")

    def get_stats(self) -> dict:
        return dict(self.db_stats)


# ---------------------------------------------------------------------------
# Layer 2: HTTP ETag/Last-Modified checker (kept for backward compat)
# ---------------------------------------------------------------------------

class HTTPChecker:
    def __init__(self, session: requests.Session, state: dict):
        self.session = session
        self.state = state

    def check(self, source_id: str, source: dict) -> Optional[dict]:
        url = source["url"]
        prev = self.state.get(source_id, {})
        headers = {}
        if prev.get("etag"):
            headers["If-None-Match"] = prev["etag"]
        if prev.get("last_modified"):
            headers["If-Modified-Since"] = prev["last_modified"]
        try:
            resp = self.session.head(url, headers=headers, timeout=15, allow_redirects=True)
            new_state = {"url": url, "last_checked": datetime.now().isoformat(),
                         "status_code": resp.status_code}
            if resp.headers.get("ETag"):
                new_state["etag"] = resp.headers["ETag"]
            if resp.headers.get("Last-Modified"):
                new_state["last_modified"] = resp.headers["Last-Modified"]
            self.state[source_id] = new_state
            if resp.status_code == 304:
                return None
            elif resp.status_code == 200:
                if prev.get("etag") and new_state.get("etag") == prev["etag"]:
                    return None
                return _make_update(source_id, source, "http_head",
                                    "Page may have been updated - manual review required")
            else:
                print(f"    WARNING: HTTP {resp.status_code}")
                return None
        except requests.RequestException as e:
            print(f"    ERROR: {e}")
            return None


# ---------------------------------------------------------------------------
# Layer 1: RSS Feed checker
# ---------------------------------------------------------------------------

class RSSChecker:
    def __init__(self, session: requests.Session, state: dict):
        self.session = session
        self.state = state

    def check(self, source_id: str, source: dict) -> Optional[dict]:
        url = source["url"]
        prev = self.state.get(source_id, {})
        last_checked = prev.get("last_checked")
        try:
            resp = self.session.get(url, timeout=15)
            resp.raise_for_status()
            root = ET.fromstring(resp.content)
            new_items = []
            for item in root.findall(".//item")[:20]:
                pub_date_el = item.find("pubDate")
                title_el = item.find("title")
                link_el = item.find("link")
                desc_el = item.find("description")
                if pub_date_el is not None and last_checked:
                    try:
                        pub_dt = parsedate_to_datetime(pub_date_el.text)
                        last_dt = datetime.fromisoformat(last_checked)
                        if pub_dt.timestamp() <= last_dt.timestamp():
                            continue
                    except Exception:
                        pass
                title = title_el.text if title_el is not None else "Unknown"
                link = link_el.text if link_el is not None else ""
                desc = (desc_el.text or "") if desc_el is not None else ""
                if last_checked is None or "final" in title.lower() or "final" in desc.lower():
                    new_items.append({"title": title, "link": link,
                                      "pub_date": pub_date_el.text if pub_date_el is not None else "",
                                      "description": desc[:300]})
            self.state[source_id] = {"url": url, "last_checked": datetime.now().isoformat()}
            if new_items:
                result = _make_update(source_id, source, "rss",
                                      f"{len(new_items)} new Final guidance item(s) in RSS")
                result["new_items"] = new_items
                return result
            return None
        except Exception as e:
            print(f"    ERROR RSS: {e}")
            return None


# ---------------------------------------------------------------------------
# Layer 3: Google Custom Search API (bypasses anti-scraping)
# Mirrors Clin_Eva_Agent/tools/google_search_tool.py pattern
# Free quota: 100 queries/day - sufficient for weekly batched checks
# ---------------------------------------------------------------------------

class GoogleSearchChecker:
    BASE_URL = "https://www.googleapis.com/customsearch/v1"

    def __init__(self, api_key: str, engine_id: str, state: dict):
        self.api_key = api_key
        self.engine_id = engine_id
        self.state = state
        self.available = bool(api_key and engine_id)

    def search(self, query: str, num: int = 10,
               date_restrict: str = "") -> list:
        """Search via Google CSE API.

        Args:
            date_restrict: Google CSE dateRestrict value, e.g. "y2" (past 2 years),
                "m6" (past 6 months), "w4" (past 4 weeks), "d30" (past 30 days).
                When set, filters results by page indexing date -- no hardcoded
                year strings needed in the query.
        """
        if not self.available:
            return []
        try:
            params = {
                "key": self.api_key, "cx": self.engine_id,
                "q": query, "num": min(num, 10), "sort": "date",
            }
            if date_restrict:
                params["dateRestrict"] = date_restrict
            resp = requests.get(self.BASE_URL, params=params, timeout=15)
            resp.raise_for_status()
            return resp.json().get("items", [])
        except Exception as e:
            print(f"    ERROR Google Search: {e}")
            return []

    def check(self, source_id: str, source: dict) -> Optional[dict]:
        query = source.get("google_query")
        if not query or not self.available:
            if not self.available:
                print(f"    SKIP (Google CSE not configured)")
            return None
        title_filter = source.get("title_filter")
        prev = self.state.get(source_id, {})
        prev_titles = set(prev.get("seen_titles", []))
        date_restrict = source.get("date_restrict", "")
        items = self.search(query, date_restrict=date_restrict)
        new_items = []
        filtered_count = 0
        all_titles = list(prev_titles)
        for item in items:
            title = item.get("title", "")
            if title_filter and not re.search(title_filter, title, re.IGNORECASE):
                filtered_count += 1
                continue
            if title not in prev_titles:
                new_items.append({"title": title, "link": item.get("link", ""),
                                  "snippet": item.get("snippet", "")[:200]})
                all_titles.append(title)
        if filtered_count:
            print(f"    INFO: {filtered_count} results filtered by title_filter")
        self.state[source_id] = {"url": source["url"],
                                  "last_checked": datetime.now().isoformat(),
                                  "seen_titles": all_titles[-100:]}
        if new_items and prev_titles:
            result = _make_update(source_id, source, "google_search",
                                  f"{len(new_items)} new result(s) via Google Search")
            result["new_items"] = new_items
            result["query"] = query
            return result
        elif not prev_titles:
            print(f"    INFO: Baseline established ({len(items)} results indexed)")
        return None


# ---------------------------------------------------------------------------
# Layer 3b: Vertex AI Search (searchLite API) -- replaces Google CSE
# Uses API Key auth via searchLite endpoint; domains restricted by data store.
# Free tier: 10,000 queries/month (our weekly cron uses ~44/month).
# Docs: https://docs.cloud.google.com/generative-ai-app-builder/docs/migrate-from-cse
# ---------------------------------------------------------------------------

class VertexAISearchChecker:
    SEARCHLITE_URL = (
        "https://discoveryengine.googleapis.com/v1/projects/{project_id}"
        "/locations/global/collections/default_collection"
        "/engines/{app_id}/servingConfigs/default_search:searchLite"
    )

    def __init__(self, project_id: str, app_id: str, api_key: str, state: dict):
        self.project_id = project_id
        self.app_id = app_id
        self.api_key = api_key
        self.state = state
        self.available = bool(project_id and app_id and api_key)

    def search(self, query: str, num: int = 10) -> list:
        if not self.available:
            return []
        url = self.SEARCHLITE_URL.format(
            project_id=self.project_id, app_id=self.app_id,
        )
        try:
            resp = requests.post(
                url,
                params={"key": self.api_key},
                json={
                    "query": query,
                    "pageSize": min(num, 25),
                },
                headers={"Content-Type": "application/json"},
                timeout=20,
            )
            if resp.status_code != 200:
                body = resp.text[:300] if resp.text else "(empty)"
                print(f"    ERROR Vertex AI Search HTTP {resp.status_code}: {body}")
                return []
            data = resp.json()
            results = []
            for r in data.get("results", []):
                doc = r.get("document", {})
                derived = doc.get("derivedStructData", {})
                link = derived.get("link", "")
                title = derived.get("title", "")
                snippet = ""
                for s in derived.get("snippets", []):
                    if s.get("snippet"):
                        snippet = re.sub(r"<[^>]+>", "", s["snippet"])
                        break
                if title or link:
                    results.append({
                        "title": title,
                        "link": link,
                        "snippet": snippet[:200],
                    })
            return results
        except Exception as e:
            print(f"    ERROR Vertex AI Search: {e}")
            return []

    @staticmethod
    def _strip_site_prefix(query: str) -> str:
        """Remove 'site:domain.com' prefixes -- Vertex AI data store handles domain restriction."""
        return re.sub(r"site:\S+\s*", "", query).strip()

    def check(self, source_id: str, source: dict) -> Optional[dict]:
        query = source.get("google_query")
        if not query or not self.available:
            if not self.available:
                print(f"    SKIP (Vertex AI Search not configured)")
            return None
        query = self._strip_site_prefix(query)
        title_filter = source.get("title_filter")
        prev = self.state.get(source_id, {})
        prev_titles = set(prev.get("seen_titles", []))
        items = self.search(query)
        new_items = []
        filtered_count = 0
        all_titles = list(prev_titles)
        for item in items:
            title = item.get("title", "")
            if title_filter and not re.search(title_filter, title, re.IGNORECASE):
                filtered_count += 1
                continue
            if title not in prev_titles:
                new_items.append({"title": title, "link": item.get("link", ""),
                                  "snippet": item.get("snippet", "")[:200]})
                all_titles.append(title)
        if filtered_count:
            print(f"    INFO: {filtered_count} results filtered by title_filter")
        self.state[source_id] = {"url": source["url"],
                                  "last_checked": datetime.now().isoformat(),
                                  "seen_titles": all_titles[-100:]}
        if new_items and prev_titles:
            result = _make_update(source_id, source, "vertex_ai_search",
                                  f"{len(new_items)} new result(s) via Vertex AI Search")
            result["new_items"] = new_items
            result["query"] = query
            return result
        elif not prev_titles:
            print(f"    INFO: Baseline established ({len(items)} results indexed)")
        return None


# ---------------------------------------------------------------------------
# Bonus: OpenFDA API checker
# Based on Clin_Eva_Agent/tools/fda_510k_tool.py pattern
# FDA_API_KEY raises rate limit; works without key too (lower quota)
# ---------------------------------------------------------------------------

class OpenFDAChecker:
    GUIDANCE_URL = "https://api.fda.gov/other/guidance.json"

    def __init__(self, api_key: str, state: dict):
        self.api_key = api_key
        self.state = state

    def check(self, source_id: str, source: dict) -> Optional[dict]:
        prev = self.state.get(source_id, {})
        last_checked = prev.get("last_checked")
        date_filter = ""
        if last_checked:
            try:
                dt = datetime.fromisoformat(last_checked)
                date_filter = f"+AND+effective_date:[{dt.strftime('%Y%m%d')}+TO+*]"
            except Exception:
                pass
        params = {
            "search": f'product_type:"DEVICE"+AND+status:"Final"{date_filter}',
            "limit": 20, "sort": "effective_date:desc",
        }
        if self.api_key:
            params["api_key"] = self.api_key
        try:
            resp = requests.get(self.GUIDANCE_URL, params=params, timeout=20)
            if resp.status_code == 404:
                self.state[source_id] = {"last_checked": datetime.now().isoformat()}
                return None
            resp.raise_for_status()
            results = resp.json().get("results", [])
            self.state[source_id] = {"last_checked": datetime.now().isoformat()}
            if not results:
                return None
            new_items = []
            for r in results:
                doc_id = r.get("id", "")
                url = r.get("url", "") or (
                    f"https://www.fda.gov/regulatory-information/"
                    f"search-fda-guidance-documents/{doc_id}" if doc_id else "")
                new_items.append({"title": r.get("title", ""), "link": url,
                                  "pub_date": r.get("effective_date", ""), "doc_id": doc_id})
            result = _make_update(source_id, source, "openfda_guidance",
                                  f"{len(new_items)} new/updated FDA Final guidance via OpenFDA API")
            result["new_items"] = new_items
            return result
        except Exception as e:
            print(f"    ERROR OpenFDA: {e}")
            return None


# ---------------------------------------------------------------------------
# eCFR Versioner API checker (replaces http_head for Title 21)
# Public API, no key needed: https://www.ecfr.gov/api/versioner/v1/titles.json
# ---------------------------------------------------------------------------

class ECFRChecker:
    TITLES_URL = "https://www.ecfr.gov/api/versioner/v1/titles.json"

    def __init__(self, session: requests.Session, state: dict):
        self.session = session
        self.state = state

    def check(self, source_id: str, source: dict) -> Optional[dict]:
        prev = self.state.get(source_id, {})
        last_amendment_date = prev.get("last_amendment_date", "")
        try:
            resp = self.session.get(self.TITLES_URL, timeout=15)
            resp.raise_for_status()
            titles = resp.json().get("titles", [])
            title21 = None
            for t in titles:
                if t.get("number") == 21:
                    title21 = t
                    break
            if not title21:
                return None
            new_date = title21.get("latest_amended_on", "") or title21.get("up_to_date_as_of", "")
            self.state[source_id] = {
                "url": source["url"],
                "last_checked": datetime.now().isoformat(),
                "last_amendment_date": new_date,
            }
            if not last_amendment_date:
                print(f"    INFO: eCFR baseline established (Title 21 last amended: {new_date})")
                return None
            if new_date and new_date > last_amendment_date:
                return _make_update(
                    source_id, source, "ecfr_api",
                    f"Title 21 CFR updated: {last_amendment_date} -> {new_date} (medical device Parts 800-898 may be affected)"
                )
            return None
        except Exception as e:
            print(f"    ERROR eCFR API: {e}")
            return None


# ---------------------------------------------------------------------------
# EUR-Lex Amendment checker (replaces http_head for harmonised standards)
# Checks consolidated decision URL date suffix for new amendments
# ---------------------------------------------------------------------------

class EURLexChecker:
    """
    Checks EUR-Lex for harmonised standards amendments via CELLAR SPARQL API.

    Three-layer detection:
    1. SPARQL query: Get all consolidated versions of CID 2021/1182 from CELLAR,
       compare latest consolidated date against last known.
    2. Standards count comparison: Compare current harmonised standards count against
       local _index.json to detect additions/removals between amendment cycles.
    3. Fallback HEAD redirect (unreliable, kept as belt-and-suspenders).

    Note: The old HEAD-redirect approach to eur-lex.europa.eu returns HTTP 202 with
    empty body (anti-bot), so Layer 1 SPARQL is the primary detection mechanism.
    """
    SPARQL_URL = "https://publications.europa.eu/webapi/rdf/sparql"
    SPARQL_QUERY = """
PREFIX cdm: <http://publications.europa.eu/ontology/cdm#>
SELECT DISTINCT ?celex ?date ?consoDate WHERE {
  ?work cdm:resource_legal_id_celex ?celex .
  FILTER(STRSTARTS(?celex, "02021D1182"))
  OPTIONAL { ?work cdm:work_date_document ?date . }
  OPTIONAL { ?work cdm:work_date_creation ?consoDate . }
} ORDER BY DESC(?celex) LIMIT 5
"""

    def __init__(self, session: requests.Session, state: dict):
        self.session = session
        self.state = state

    def check(self, source_id: str, source: dict) -> Optional[dict]:
        prev = self.state.get(source_id, {})
        last_known_amendment = prev.get("last_known_amendment", "")
        last_known_count = prev.get("standards_count", 0)

        # Ignore legacy placeholder "99990101" from old HEAD-redirect approach
        if last_known_amendment == "99990101":
            last_known_amendment = ""

        new_consol_date = ""
        sparql_ok = False

        try:
            # Layer 1: CELLAR SPARQL API -- authoritative consolidated version dates
            new_consol_date = self._sparql_latest_consolidated()
            if new_consol_date:
                sparql_ok = True
                print(f"    INFO: SPARQL latest consolidated: {new_consol_date}")
        except Exception as e:
            print(f"    WARNING: SPARQL failed ({e}), falling back to HEAD redirect")

        if not sparql_ok:
            # Layer 3 fallback: HEAD redirect (unreliable but harmless)
            try:
                consol_url = "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02021D1182-99990101"
                resp = self.session.head(consol_url, timeout=15, allow_redirects=True)
                final_url = str(resp.url) if resp.url else ""
                date_match = re.search(r"02021D1182-(\d{8})", final_url)
                fallback_date = date_match.group(1) if date_match else ""
                if fallback_date and fallback_date != "99990101":
                    new_consol_date = fallback_date
            except Exception:
                pass

        # Layer 2: Local standards count check
        current_count = self._get_local_standards_count()

        self.state[source_id] = {
            "url": source["url"],
            "last_checked": datetime.now().isoformat(),
            "last_known_amendment": new_consol_date or last_known_amendment,
            "standards_count": current_count,
            "detection_method": "sparql" if sparql_ok else "head_fallback",
        }

        if not last_known_amendment:
            print(f"    INFO: EUR-Lex baseline established (consolidated date: {new_consol_date}, count: {current_count})")
            return None

        changes = []
        if new_consol_date and new_consol_date > last_known_amendment:
            changes.append(f"consolidated date: {last_known_amendment} -> {new_consol_date}")

        if last_known_count and current_count != last_known_count:
            changes.append(f"standards count: {last_known_count} -> {current_count}")

        if changes:
            return _make_update(
                source_id, source, "eurlex_amendment",
                f"Harmonised standards change detected ({'; '.join(changes)})"
            )
        return None

    def _sparql_latest_consolidated(self) -> str:
        """Query CELLAR SPARQL for the latest consolidated version date of CID 2021/1182.

        Returns date string like '20260407' or empty string on failure.
        """
        resp = self.session.get(
            self.SPARQL_URL,
            params={"query": self.SPARQL_QUERY, "format": "application/json"},
            timeout=30,
        )
        resp.raise_for_status()
        data = resp.json()
        bindings = data.get("results", {}).get("bindings", [])
        if not bindings:
            return ""
        # CELEX format: 02021D1182-YYYYMMDD -- extract the date part from first (latest) result
        celex = bindings[0].get("celex", {}).get("value", "")
        match = re.search(r"02021D1182-(\d{8})", celex)
        return match.group(1) if match else ""

    def _get_local_standards_count(self) -> int:
        """Get current harmonised standards count from local _index.json."""
        index_path = ROOT / "eu_mdr" / "standards" / "_index.json"
        if not index_path.exists():
            return 0
        try:
            with open(index_path) as f:
                data = json.load(f)
            return data.get("total_standards", 0)
        except Exception:
            return 0


# ---------------------------------------------------------------------------
# LLM Version Analyzer (optional - requires LLM_API_KEY)
# Uses OneAPI-compatible endpoint (deepseek-chat, gpt-4o-mini, etc.)
# ---------------------------------------------------------------------------

class LLMVersionAnalyzer:
    def __init__(self, api_key: str, base_url: str, model: str):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.model = model
        self.available = bool(api_key)

    def analyze(self, doc_id: str, registry_entry: Optional[dict], new_items: list) -> dict:
        if not self.available or not new_items:
            return {"is_update": False, "confidence": 0.0, "reasoning": "LLM not configured"}
        current = (registry_entry or {}).get("current", {})
        prompt = (
            f'You are a regulatory document version analyst.\n\n'
            f'Current entry for "{doc_id}": title={current.get("title","N/A")}, '
            f'version={current.get("version","N/A")}, status={current.get("status","N/A")}, '
            f'published={current.get("published_date","N/A")}\n\n'
            f'New search results:\n{json.dumps(new_items[:5], ensure_ascii=False)}\n\n'
            f'Is this a genuine NEW VERSION or UPDATE? Consider: newer date, same document '
            f'type, Draft->Final transition, revision.\n'
            f'JSON only: {{"is_update":bool,"confidence":0.0-1.0,'
            f'"new_version":"YYYY-MM or null","new_url":"url or null","reasoning":"brief"}}'
        )
        try:
            resp = requests.post(
                f"{self.base_url}/chat/completions",
                headers={"Authorization": f"Bearer {self.api_key}",
                         "Content-Type": "application/json"},
                json={"model": self.model,
                      "messages": [{"role": "user", "content": prompt}],
                      "temperature": 0.1,
                      "response_format": {"type": "json_object"}},
                timeout=30,
            )
            resp.raise_for_status()
            return json.loads(resp.json()["choices"][0]["message"]["content"])
        except Exception as e:
            return {"is_update": False, "confidence": 0.0, "reasoning": f"LLM error: {e}"}


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------

def _make_update(source_id: str, source: dict, check_type: str, note: str) -> dict:
    return {
        "source_id": source_id, "name": source["name"], "url": source["url"],
        "category": source["category"], "check_type": check_type,
        "detected_at": datetime.now().isoformat(), "note": note,
    }


# ---------------------------------------------------------------------------
# Orchestrator
# ---------------------------------------------------------------------------

class UpdateChecker:
    def __init__(self, state_file: Path = None):
        self.state_file = state_file or ROOT / "scripts" / ".update_state.json"
        self.state = self._load_state()
        self.registry = VersionRegistry()
        self.db_comparator = DatabaseComparator(ROOT)
        session = requests.Session()
        session.headers.update({"User-Agent": "Mozilla/5.0 (docmcp-knowledge-bot/2.0)"})
        self.http = HTTPChecker(session, self.state)
        self.rss = RSSChecker(session, self.state)
        self.vertex = VertexAISearchChecker(
            VERTEX_AI_PROJECT_ID, VERTEX_AI_SEARCH_APP_ID,
            VERTEX_AI_SEARCH_API_KEY, self.state,
        )
        self.google = GoogleSearchChecker(GOOGLE_SEARCH_API_KEY, GOOGLE_SEARCH_ENGINE_ID,
                                          self.state)
        self.web_search_available = self.vertex.available or self.google.available
        self.openfda = OpenFDAChecker(FDA_API_KEY, self.state)
        self.ecfr = ECFRChecker(session, self.state)
        self.eurlex = EURLexChecker(session, self.state)
        self.llm = LLMVersionAnalyzer(LLM_API_KEY, LLM_BASE_URL, LLM_MODEL)
        if self.vertex.available:
            print("INFO: Using Vertex AI Search (searchLite) for web queries.")
        elif self.google.available:
            print("INFO: Using legacy Google CSE (sunsets 2027-01-01). "
                  "Set VERTEX_AI_* vars to upgrade.")
        else:
            print("INFO: No web search configured - set VERTEX_AI_PROJECT_ID + "
                  "VERTEX_AI_SEARCH_APP_ID + VERTEX_AI_SEARCH_API_KEY.")
        if not self.llm.available:
            print(f"INFO: LLM analysis not configured - set LLM_API_KEY "
                  f"(LLM_BASE_URL={LLM_BASE_URL}, LLM_MODEL={LLM_MODEL}).")

    def _load_state(self) -> dict:
        if self.state_file.exists():
            try:
                with open(self.state_file, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                pass
        return {}

    def _save_state(self):
        self.state_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.state_file, "w", encoding="utf-8") as f:
            json.dump(self.state, f, indent=2, ensure_ascii=False)

    def _web_search_check(self, source_id: str, source: dict) -> Optional[dict]:
        """Dispatch web search to Vertex AI (preferred) or legacy CSE."""
        if self.vertex.available:
            return self.vertex.check(source_id, source)
        if self.google.available:
            return self.google.check(source_id, source)
        return None

    def check_source(self, source_id: str, source: dict) -> Optional[dict]:
        check_type = source.get("check_type", "http_head")
        if check_type == "rss":
            return self.rss.check(source_id, source)
        elif check_type == "google_search":
            result = self._web_search_check(source_id, source)
            if result:
                result = self._apply_db_comparison(result)
            return result
        elif check_type == "openfda_guidance":
            result = self.openfda.check(source_id, source)
            if result:
                result = self._apply_db_comparison(result)
            return result
        elif check_type == "ecfr_api":
            return self.ecfr.check(source_id, source)
        elif check_type == "eurlex_amendment":
            return self.eurlex.check(source_id, source)
        else:
            result = self.http.check(source_id, source)
            if source.get("google_query") and self.web_search_available:
                g_result = self._web_search_check(source_id + "_google", source)
                if g_result:
                    g_result = self._apply_db_comparison(g_result)
                    return g_result
            return result

    def _apply_db_comparison(self, update: dict) -> Optional[dict]:
        """Run DatabaseComparator on each new_item; keep only new/update items."""
        new_items = update.get("new_items", [])
        if not new_items:
            return update
        category = update.get("category", "")
        confirmed_items = []
        noise_filtered = 0
        for item in new_items:
            title = item.get("title", "")
            link = item.get("link", "")
            date = item.get("pub_date", "")
            classification, desc = self.db_comparator.classify(category, title, link, date)
            item["db_classification"] = classification
            item["db_description"] = desc
            if classification in ("new", "update"):
                confirmed_items.append(item)
            else:
                noise_filtered += 1
        update["noise_filtered"] = noise_filtered
        update["db_confirmed_items"] = confirmed_items
        if not confirmed_items:
            print(f"    INFO: All {len(new_items)} items filtered by DB comparison (noise)")
            return None
        update["new_items"] = confirmed_items
        update["note"] = (
            f"{len(confirmed_items)} DB-confirmed new item(s) "
            f"({noise_filtered} noise filtered from {len(new_items)} total)"
        )
        update["db_confirmed"] = True
        return update

    def check_regulation(self, regulation: str) -> list:
        if regulation not in SOURCES:
            print(f"Unknown regulation: {regulation}")
            return []
        updates = []
        sources = SOURCES[regulation]
        print(f"\nChecking {regulation} ({len(sources)} sources)...")
        for source_id, source in sources.items():
            full_id = f"{regulation}/{source_id}"
            print(f"  [{full_id}] {source['name']}")
            result = self.check_source(full_id, source)
            if result:
                updates.append(result)
                print(f"    -> UPDATE DETECTED: {result.get('note', '')}")
            else:
                print(f"    -> No changes")
            time.sleep(1.0)
        return updates

    def check_all(self) -> list:
        all_updates = []
        for regulation in SOURCES:
            updates = self.check_regulation(regulation)
            all_updates.extend(updates)
        return all_updates

    def analyze_versions(self, updates: list) -> list:
        if not self.llm.available:
            print("INFO: LLM analysis skipped (LLM_API_KEY not set)")
            return updates
        print("\nRunning LLM version analysis...")
        for update in updates:
            new_items = update.get("new_items", [])
            if not new_items:
                continue
            doc_id = update["source_id"]
            analysis = self.llm.analyze(doc_id, self.registry.get(doc_id), new_items)
            update["llm_analysis"] = analysis
            if analysis.get("is_update") and analysis.get("confidence", 0) > 0.7:
                update["confirmed_update"] = True
                update["new_version"] = analysis.get("new_version")
                update["new_url"] = analysis.get("new_url")
                print(f"  CONFIRMED: {doc_id} -> v{analysis.get('new_version')} "
                      f"({analysis.get('confidence', 0):.0%})")
            else:
                print(f"  UNCONFIRMED: {doc_id} - {analysis.get('reasoning','')[:80]}")
            time.sleep(0.5)
        return updates

    def generate_report(self, updates: list) -> dict:
        confirmed = [u for u in updates if u.get("confirmed_update")]
        db_confirmed = [u for u in updates if u.get("db_confirmed")]
        db_confirmed_new = len(db_confirmed)
        total_noise = sum(u.get("noise_filtered", 0) for u in updates)
        return {
            "checked_at": datetime.now().isoformat(),
            "updates_found": len(updates),
            "confirmed_updates": len(confirmed),
            "db_confirmed_new": db_confirmed_new,
            "noise_filtered_total": total_noise,
            "updates": updates,
            "db_stats": self.db_comparator.get_stats(),
            "summary": (
                f"{len(updates)} update(s) detected "
                f"({db_confirmed_new} DB-confirmed, {len(confirmed)} LLM-confirmed, "
                f"{total_noise} noise filtered) across "
                f"{len(set(u['category'] for u in updates))} categories"
                if updates else "No updates detected"
            ),
            "checkers_used": {
                "vertex_ai_search": self.vertex.available,
                "google_cse_legacy": self.google.available and not self.vertex.available,
                "openfda_api": True,
                "llm_analysis": self.llm.available,
                "db_comparator": True,
                "ecfr_api": True,
                "eurlex_checker": True,
            },
        }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Regulatory update checker (3-layer anti-scraping bypass)"
    )
    parser.add_argument("--check-all", action="store_true", help="Check all regulation groups")
    parser.add_argument("--check", metavar="GROUP",
                        help="Check specific group: eu_mdr / fda / nmpa / shared")
    parser.add_argument("--analyze-versions", action="store_true",
                        help="Run LLM version analysis on detected updates")
    parser.add_argument("--report", action="store_true",
                        help="Output JSON report (for GitHub Actions)")
    parser.add_argument("--output", metavar="FILE", help="Save report to file")
    args = parser.parse_args()

    if not args.check_all and not args.check:
        parser.print_help()
        sys.exit(0)

    checker = UpdateChecker()

    if args.check_all:
        updates = checker.check_all()
    else:
        updates = checker.check_regulation(args.check)

    if args.analyze_versions:
        updates = checker.analyze_versions(updates)

    checker._save_state()
    checker.registry.save()

    report = checker.generate_report(updates)

    if args.report or args.output:
        report_json = json.dumps(report, indent=2, ensure_ascii=False)
        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(report_json)
            print(f"\nReport saved to: {args.output}")
        else:
            print("\n" + report_json)
    else:
        print(f"\n{'='*50}")
        print(f"Check complete: {report['summary']}")
        if updates:
            print("\nUpdates found:")
            for u in updates:
                print(f"  - [{u['category']}] {u['name']}")
                print(f"    {u['url']}")
                print(f"    {u.get('note', '')}")
        print(f"{'='*50}")

    if updates and args.report:
        sys.exit(1)


if __name__ == "__main__":
    main()
