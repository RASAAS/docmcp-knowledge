#!/usr/bin/env python3
"""
Automated Regulatory Update Monitoring Script
Checks official sources for new/updated regulatory content and creates update reports.

Usage:
    python scripts/fetch_updates.py --check-all
    python scripts/fetch_updates.py --check eu_mdr
    python scripts/fetch_updates.py --check nmpa
    python scripts/fetch_updates.py --report  # Output JSON report for GitHub Actions

Designed to run as a GitHub Actions cron job (daily).
Outputs a JSON report that can be used to create draft PRs.
"""

import argparse
import json
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path

try:
    import requests
except ImportError:
    print("ERROR: requests not installed. Run: pip install requests")
    sys.exit(1)

ROOT = Path(__file__).parent.parent

# ---------------------------------------------------------------------------
# Source definitions: official URLs to monitor for updates
# ---------------------------------------------------------------------------
SOURCES = {
    "eu_mdr": {
        "harmonised_standards": {
            "name": "EU MDR Harmonised Standards (OJ)",
            # Canonical EC page listing all harmonised standards implementing decisions
            "url": "https://health.ec.europa.eu/medical-devices-topics-interest/harmonised-standards_en",
            "check_type": "http_head",
            "category": "eu_mdr/standards",
        },
        "harmonised_standards_oj": {
            "name": "EU MDR Harmonised Standards - Latest Implementing Decision (EUR-Lex)",
            # CID (EU) 2021/1182 base + amendments tracked via EUR-Lex
            "url": "https://eur-lex.europa.eu/eli/dec_impl/2021/1182/oj",
            "check_type": "http_head",
            "category": "eu_mdr/standards",
        },
        "mdcg_guidance": {
            "name": "MDCG Guidance Documents",
            "url": "https://health.ec.europa.eu/medical-devices-sector/new-regulations/guidance-mdcg-endorsed-documents-and-other-guidance_en",
            "check_type": "http_head",
            "category": "eu_mdr/mdcg",
        },
        "team_nb": {
            "name": "TEAM-NB Position Papers",
            "url": "https://www.team-nb.org/position-papers/",
            "check_type": "http_head",
            "category": "eu_mdr/team_nb",
        },
    },
    "fda": {
        "guidance_rss": {
            "name": "FDA Medical Device Guidance (RSS)",
            "url": "https://www.fda.gov/about-fda/contact-fda/stay-informed/rss-feeds/medical-devices/rss.xml",
            "check_type": "rss",
            "category": "fda/guidance",
        },
        "consensus_standards": {
            "name": "FDA Recognized Consensus Standards",
            # CDRH standards database search page
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
            # CMDE official guidance principles listing page
            "url": "https://www.cmde.org.cn/flfg/zdyz/",
            "check_type": "http_head",
            "category": "nmpa/guidance",
        },
        "nmpa_announcements": {
            "name": "NMPA Medical Device Announcements",
            "url": "https://www.nmpa.gov.cn/ylqx/ylqxggtg/",
            "check_type": "http_head",
            "category": "nmpa/regulations",
        },
        "nmpa_regulations": {
            "name": "NMPA Medical Device Regulations",
            "url": "https://www.nmpa.gov.cn/ylqx/ylqxfgwj/",
            "check_type": "http_head",
            "category": "nmpa/regulations",
        },
    },
    "shared": {
        "iso_standards": {
            "name": "ISO TC 210 Medical Device Standards",
            # ISO TC 210 is the committee for quality management and general aspects of medical devices
            "url": "https://www.iso.org/committee/54892/x/catalogue/",
            "check_type": "http_head",
            "category": "_shared/standards",
        },
        "iec_standards": {
            "name": "IEC TC 62 Medical Electrical Equipment Standards",
            "url": "https://www.iec.ch/dyn/www/f?p=103:7:::::FSP_ORG_ID:1245",
            "check_type": "http_head",
            "category": "_shared/standards",
        },
    },
}


class UpdateChecker:
    def __init__(self, state_file: Path = None):
        self.state_file = state_file or ROOT / "scripts" / ".update_state.json"
        self.state = self._load_state()
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "docmcp-knowledge-update-checker/1.0"
        })
        self.updates_found = []

    def _load_state(self) -> dict:
        """Load previous check state (last-modified headers, ETags)."""
        if self.state_file.exists():
            try:
                with open(self.state_file, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                pass
        return {}

    def _save_state(self):
        """Save current check state."""
        self.state_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.state_file, "w", encoding="utf-8") as f:
            json.dump(self.state, f, indent=2, ensure_ascii=False)

    def check_http_head(self, source_id: str, source: dict) -> dict | None:
        """Check if a URL has been modified since last check using HEAD request."""
        url = source["url"]
        prev = self.state.get(source_id, {})

        headers = {}
        if prev.get("etag"):
            headers["If-None-Match"] = prev["etag"]
        if prev.get("last_modified"):
            headers["If-Modified-Since"] = prev["last_modified"]

        try:
            resp = self.session.head(url, headers=headers, timeout=15, allow_redirects=True)

            # Update state
            new_state = {
                "url": url,
                "last_checked": datetime.now().isoformat(),
                "status_code": resp.status_code,
            }
            if resp.headers.get("ETag"):
                new_state["etag"] = resp.headers["ETag"]
            if resp.headers.get("Last-Modified"):
                new_state["last_modified"] = resp.headers["Last-Modified"]

            self.state[source_id] = new_state

            if resp.status_code == 304:  # Not Modified
                return None
            elif resp.status_code == 200:
                # Check if content actually changed
                if prev.get("etag") and new_state.get("etag") == prev["etag"]:
                    return None  # Same ETag, no change
                return {
                    "source_id": source_id,
                    "name": source["name"],
                    "url": url,
                    "category": source["category"],
                    "check_type": "http_head",
                    "detected_at": datetime.now().isoformat(),
                    "note": "Page may have been updated - manual review required",
                }
            else:
                print(f"    WARNING: {url} returned {resp.status_code}")
                return None

        except requests.RequestException as e:
            print(f"    ERROR checking {url}: {e}")
            return None

    def check_rss(self, source_id: str, source: dict) -> dict | None:
        """Check RSS feed for new items since last check."""
        url = source["url"]
        prev = self.state.get(source_id, {})
        last_checked = prev.get("last_checked")

        try:
            resp = self.session.get(url, timeout=15)
            resp.raise_for_status()

            # Simple RSS parsing without external library
            import xml.etree.ElementTree as ET
            root = ET.fromstring(resp.content)

            new_items = []
            for item in root.findall(".//item")[:10]:  # Check last 10 items
                pub_date_el = item.find("pubDate")
                title_el = item.find("title")
                link_el = item.find("link")

                if pub_date_el is not None and last_checked:
                    # Simple date comparison
                    try:
                        from email.utils import parsedate_to_datetime
                        pub_dt = parsedate_to_datetime(pub_date_el.text)
                        last_dt = datetime.fromisoformat(last_checked)
                        if pub_dt.timestamp() <= last_dt.timestamp():
                            continue
                    except Exception:
                        pass

                new_items.append({
                    "title": title_el.text if title_el is not None else "Unknown",
                    "link": link_el.text if link_el is not None else "",
                    "pub_date": pub_date_el.text if pub_date_el is not None else "",
                })

            self.state[source_id] = {
                "url": url,
                "last_checked": datetime.now().isoformat(),
            }

            if new_items:
                return {
                    "source_id": source_id,
                    "name": source["name"],
                    "url": url,
                    "category": source["category"],
                    "check_type": "rss",
                    "detected_at": datetime.now().isoformat(),
                    "new_items": new_items,
                    "note": f"{len(new_items)} new item(s) found in RSS feed",
                }
            return None

        except Exception as e:
            print(f"    ERROR checking RSS {url}: {e}")
            return None

    def check_source(self, source_id: str, source: dict) -> dict | None:
        """Dispatch to appropriate check method."""
        check_type = source.get("check_type", "http_head")
        if check_type == "rss":
            return self.check_rss(source_id, source)
        else:
            return self.check_http_head(source_id, source)

    def check_regulation(self, regulation: str) -> list:
        """Check all sources for a regulation."""
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
            time.sleep(0.5)

        return updates

    def check_all(self) -> list:
        """Check all sources."""
        all_updates = []
        for regulation in SOURCES:
            updates = self.check_regulation(regulation)
            all_updates.extend(updates)
        return all_updates

    def generate_report(self, updates: list) -> dict:
        """Generate a structured report for GitHub Actions."""
        return {
            "checked_at": datetime.now().isoformat(),
            "updates_found": len(updates),
            "updates": updates,
            "summary": (
                f"{len(updates)} potential update(s) detected across "
                f"{len(set(u['category'] for u in updates))} categories"
                if updates else "No updates detected"
            ),
        }


def main():
    parser = argparse.ArgumentParser(description="Check for regulatory content updates")
    parser.add_argument("--check-all", action="store_true", help="Check all sources")
    parser.add_argument("--check", help="Check specific regulation (eu_mdr/fda/nmpa/shared)")
    parser.add_argument("--report", action="store_true",
                        help="Output JSON report (for GitHub Actions)")
    parser.add_argument("--output", help="Save report to file")
    args = parser.parse_args()

    if not args.check_all and not args.check:
        parser.print_help()
        sys.exit(0)

    checker = UpdateChecker()

    if args.check_all:
        updates = checker.check_all()
    else:
        updates = checker.check_regulation(args.check)

    checker._save_state()

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

    # Exit with code 1 if updates found (for GitHub Actions to detect)
    if updates and args.report:
        sys.exit(1)


if __name__ == "__main__":
    main()
