#!/usr/bin/env python3
"""
Automated Regulatory Update Monitoring Script
Checks official sources for new/updated regulatory content and creates update reports.

Strategy (3-layer anti-scraping bypass):
  Layer 1: RSS Feed     - FDA Medical Devices RSS (real-time, no anti-scraping)
  Layer 2: HTTP ETag    - EUR-Lex, eCFR, gov.cn (reliable, no anti-scraping)
  Layer 3: Google CSE   - NMPA, CMDE, ISO, FDA supplement (bypasses anti-scraping)
  Bonus:   OpenFDA API  - FDA guidance search via official API

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
            "name": "EU MDR Harmonised Standards (OJ)",
            "url": "https://health.ec.europa.eu/medical-devices-topics-interest/harmonised-standards_en",
            "check_type": "http_head",
            "category": "eu_mdr/standards",
        },
        "harmonised_standards_oj": {
            "name": "EU MDR Harmonised Standards - Latest Implementing Decision (EUR-Lex)",
            "url": "https://eur-lex.europa.eu/eli/dec_impl/2021/1182/oj",
            "check_type": "http_head",
            "category": "eu_mdr/standards",
        },
        "mdcg_guidance": {
            "name": "MDCG Guidance Documents",
            "url": "https://health.ec.europa.eu/medical-devices-sector/new-regulations/guidance-mdcg-endorsed-documents-and-other-guidance_en",
            "check_type": "http_head",
            "category": "eu_mdr/mdcg",
            "google_query": "site:health.ec.europa.eu MDCG guidance 2025 OR 2026 medical devices",
        },
        "team_nb": {
            "name": "TEAM-NB Position Papers",
            "url": "https://www.team-nb.org/",
            "check_type": "http_head",
            "category": "eu_mdr/team_nb",
            "google_query": "site:team-nb.org position paper 2025 OR 2026",
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
            "google_query": "site:fda.gov medical device guidance final 2025 OR 2026 -draft",
        },
        "consensus_standards": {
            "name": "FDA Recognized Consensus Standards",
            "url": "https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfStandards/search.cfm",
            "check_type": "http_head",
            "category": "fda/standards",
        },
        "regulations_ecfr": {
            "name": "FDA 21 CFR (eCFR)",
            "url": "https://www.ecfr.gov/current/title-21",
            "check_type": "http_head",
            "category": "fda/regulations",
        },
    },
    "nmpa": {
        "cmde_guidance": {
            "name": "CMDE Guidance Principles Index",
            "url": "https://www.cmde.org.cn/flfg/zdyz/",
            "check_type": "google_search",
            "category": "nmpa/guidance",
            "google_query": "site:cmde.org.cn 指导原则 医疗器械 2025 OR 2026",
        },
        "nmpa_regulations": {
            "name": "NMPA Medical Device Regulations (SAMR)",
            "url": "https://www.samr.gov.cn/zw/zfxxgk/fdzdgknr/fgs/",
            "check_type": "google_search",
            "category": "nmpa/regulations",
            "google_query": "site:samr.gov.cn 医疗器械 部门规章 2025 OR 2026",
        },
        "nmpa_announcements": {
            "name": "NMPA Medical Device Announcements",
            "url": "https://www.nmpa.gov.cn/ylqx/ylqxggtg/",
            "check_type": "google_search",
            "category": "nmpa/regulations",
            "google_query": "site:nmpa.gov.cn 医疗器械 公告 通告 2025 OR 2026",
        },
        "nmpa_standards": {
            "name": "NMPA Medical Device Standards (YY/GB)",
            "url": "https://std.samr.gov.cn",
            "check_type": "google_search",
            "category": "nmpa/standards",
            "google_query": "site:std.samr.gov.cn YY 医疗器械 2025 OR 2026",
        },
    },
    "shared": {
        "iso_tc210": {
            "name": "ISO TC 210 Medical Device Standards",
            "url": "https://www.iso.org/committee/54892/x/catalogue/",
            "check_type": "google_search",
            "category": "_shared/standards",
            "google_query": "site:iso.org 13485 OR 14971 OR 62304 OR 10993 medical device 2025 OR 2026",
        },
        "iec_tc62": {
            "name": "IEC TC 62 Medical Electrical Equipment Standards",
            "url": "https://www.iec.ch/dyn/www/f?p=103:7:::::FSP_ORG_ID:1245",
            "check_type": "google_search",
            "category": "_shared/standards",
            "google_query": "site:iec.ch 60601 OR 62133 medical device standard 2025 OR 2026",
        },
    },
}


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
# Layer 2: HTTP ETag/Last-Modified checker
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

    def search(self, query: str, num: int = 10) -> list:
        if not self.available:
            return []
        try:
            resp = requests.get(self.BASE_URL, params={
                "key": self.api_key, "cx": self.engine_id,
                "q": query, "num": min(num, 10), "sort": "date",
            }, timeout=15)
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
        prev = self.state.get(source_id, {})
        prev_titles = set(prev.get("seen_titles", []))
        items = self.search(query)
        new_items = []
        all_titles = list(prev_titles)
        for item in items:
            title = item.get("title", "")
            if title not in prev_titles:
                new_items.append({"title": title, "link": item.get("link", ""),
                                  "snippet": item.get("snippet", "")[:200]})
                all_titles.append(title)
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
        session = requests.Session()
        session.headers.update({"User-Agent": "Mozilla/5.0 (docmcp-knowledge-bot/2.0)"})
        self.http = HTTPChecker(session, self.state)
        self.rss = RSSChecker(session, self.state)
        self.google = GoogleSearchChecker(GOOGLE_SEARCH_API_KEY, GOOGLE_SEARCH_ENGINE_ID,
                                          self.state)
        self.openfda = OpenFDAChecker(FDA_API_KEY, self.state)
        self.llm = LLMVersionAnalyzer(LLM_API_KEY, LLM_BASE_URL, LLM_MODEL)
        if not self.google.available:
            print("INFO: Google CSE not configured - set GOOGLE_SEARCH_API_KEY + "
                  "GOOGLE_SEARCH_ENGINE_ID to enable NMPA/CMDE/ISO checks.")
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

    def check_source(self, source_id: str, source: dict) -> Optional[dict]:
        check_type = source.get("check_type", "http_head")
        if check_type == "rss":
            return self.rss.check(source_id, source)
        elif check_type == "google_search":
            return self.google.check(source_id, source)
        elif check_type == "openfda_guidance":
            return self.openfda.check(source_id, source)
        else:
            result = self.http.check(source_id, source)
            if source.get("google_query") and self.google.available:
                g_result = self.google.check(source_id + "_google", source)
                if g_result:
                    return g_result
            return result

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
            print("INFO: LLM analysis skipped (OPENAI_API_KEY not set)")
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
        return {
            "checked_at": datetime.now().isoformat(),
            "updates_found": len(updates),
            "confirmed_updates": len(confirmed),
            "updates": updates,
            "summary": (
                f"{len(updates)} potential update(s) detected "
                f"({len(confirmed)} LLM-confirmed) across "
                f"{len(set(u['category'] for u in updates))} categories"
                if updates else "No updates detected"
            ),
            "checkers_used": {
                "google_cse": self.google.available,
                "openfda_api": True,
                "llm_analysis": self.llm.available,
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
