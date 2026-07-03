"""Tier 2 regulatory source checkers for Phase 3b global expansion.

Covers: Switzerland (Swissmedic), Saudi Arabia (SFDA), Brazil (ANVISA),
        Singapore (HSA), India (CDSCO).

Also includes TGA RSS checker (fix for Phase 3a Australia TGA).
"""

import csv
import io
import re
from datetime import datetime, timedelta
from typing import Optional

try:
    import requests
except ImportError:
    raise SystemExit("ERROR: requests not installed. Run: pip install requests")


def _make_update(source_id: str, source: dict, method: str, note: str) -> dict:
    return {
        "source_id": source_id,
        "name": source.get("name", source_id),
        "url": source.get("url", ""),
        "category": source.get("category", ""),
        "method": method,
        "note": note,
        "timestamp": datetime.now().isoformat(),
    }


# ---------------------------------------------------------------------------
# TGA RSS Checker (Phase 3a fix)
# Uses TGA official RSS feeds: safety-alerts.xml, market-actions.xml
# These feeds may be inaccessible from some networks but work in GitHub Actions.
# ---------------------------------------------------------------------------

class TGARSSChecker:
    """Parses TGA RSS feeds for medical device safety alerts and market actions.

    Falls back gracefully if TGA RSS feeds are unreachable (HTTP/2 errors
    observed from some networks due to WAF/CDN).
    """

    def __init__(self, session: requests.Session, state: dict,
                 seed_mode: bool = False):
        self.session = session
        self.state = state
        self.seed_mode = seed_mode

    def check(self, source_id: str, source: dict) -> Optional[dict]:
        url = source["url"]
        prev = self.state.get(source_id, {})
        prev_ids = set(prev.get("seen_ids", []))

        resp = None
        for attempt in range(3):
            try:
                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                                  "Chrome/130.0.0.0 Safari/537.36",
                    "Accept": "application/rss+xml, application/xml, text/xml, */*",
                }
                timeout = 45 + attempt * 15
                resp = self.session.get(url, timeout=timeout, headers=headers)
                resp.raise_for_status()
                if len(resp.content) < 50:
                    print(f"    WARNING: TGA RSS returned tiny response ({len(resp.content)} bytes), retry {attempt+1}/3")
                    resp = None
                    continue
                break
            except Exception as e:
                print(f"    WARNING: TGA RSS attempt {attempt+1}/3 failed: {e}")
                resp = None
                import time
                time.sleep(2 + attempt * 3)

        if resp is None:
            print("    ERROR: TGA RSS unreachable after 3 attempts")
            return None

        entries = self._parse_rss(resp.content)
        if not entries:
            print("    WARNING: No entries parsed from TGA RSS feed")
            return None

        print(f"    INFO: Parsed {len(entries)} entries from TGA RSS feed")

        title_filter = source.get("title_filter")
        title_exclude = source.get("title_exclude")
        max_age_days = source.get("max_age_days", 0)
        new_items = []
        all_ids = list(prev_ids)

        if max_age_days > 0:
            age_cutoff = (datetime.now() - timedelta(days=max_age_days)).strftime("%Y-%m-%d")
        else:
            age_cutoff = ""

        for entry in entries:
            eid = entry.get("link") or entry.get("title", "")
            title = entry.get("title", "")
            if not eid or eid in prev_ids:
                continue
            if title_filter and not re.search(title_filter, title, re.IGNORECASE):
                continue
            if title_exclude and re.search(title_exclude, title, re.IGNORECASE):
                all_ids.append(eid)
                continue
            if age_cutoff and entry.get("pub_date", "") and entry["pub_date"][:10] < age_cutoff:
                all_ids.append(eid)
                continue
            all_ids.append(eid)
            new_items.append(entry)

        self.state[source_id] = {
            "url": url,
            "last_checked": datetime.now().isoformat(),
            "seen_ids": all_ids[-500:],
        }

        if new_items and (prev_ids or self.seed_mode):
            if self.seed_mode and not prev_ids:
                new_items = new_items[:10]
                print(f"    INFO: Seed mode -- returning top {len(new_items)} TGA entries")
            result = _make_update(
                source_id, source, "tga_rss",
                f"{len(new_items)} new TGA alert(s) detected"
            )
            result["new_items"] = new_items
            return result
        elif not prev_ids:
            print(f"    INFO: Baseline established ({len(entries)} TGA RSS entries)")

        return None

    @staticmethod
    def _parse_rss(content: bytes) -> list[dict]:
        import xml.etree.ElementTree as ET
        from email.utils import parsedate_to_datetime as _rfc2822
        results = []
        try:
            root = ET.fromstring(content)
            for item in root.findall(".//item")[:30]:
                title_el = item.find("title")
                link_el = item.find("link")
                desc_el = item.find("description")
                pub_el = item.find("pubDate")
                pub_date = ""
                if pub_el is not None and pub_el.text:
                    try:
                        pub_date = _rfc2822(pub_el.text.strip()).strftime("%Y-%m-%d")
                    except Exception:
                        pub_date = pub_el.text.strip()[:10]
                results.append({
                    "title": (title_el.text or "").strip() if title_el is not None else "",
                    "link": (link_el.text or "").strip() if link_el is not None else "",
                    "pub_date": pub_date,
                    "description": (desc_el.text or "").strip()[:300] if desc_el is not None else "",
                })
        except ET.ParseError as e:
            print(f"    ERROR parsing TGA RSS XML: {e}")
        return results


# ---------------------------------------------------------------------------
# ANVISA (Brazil) Tecnovigilancia alerts HTML checker
# Parses the ANVISA alerts page filtered by tecnovigilancia tag.
# ---------------------------------------------------------------------------

class ANVISAChecker:
    """Checks ANVISA (Brazil) medical device tecnovigilance alerts.

    Parses antigo.anvisa.gov.br/alertas?tagsName=tecnovigilancia page
    which lists FSCA/recall alerts for medical devices in Brazil (Portuguese).
    """

    ALERTS_URL = "https://antigo.anvisa.gov.br/alertas?tagsName=tecnovigil%C3%A2ncia"

    def __init__(self, session: requests.Session, state: dict,
                 seed_mode: bool = False):
        self.session = session
        self.state = state
        self.seed_mode = seed_mode

    def check(self, source_id: str, source: dict) -> Optional[dict]:
        url = source.get("url") or self.ALERTS_URL
        prev = self.state.get(source_id, {})
        prev_ids = set(prev.get("seen_ids", []))

        try:
            resp = self.session.get(url, timeout=30, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                              "AppleWebKit/537.36 Chrome/130.0 Safari/537.36",
            })
            resp.raise_for_status()
        except Exception as e:
            print(f"    ERROR ANVISA: {e}")
            return None

        entries = self._parse_alerts(resp.text)
        if not entries:
            print("    WARNING: No entries from ANVISA alerts page")
            return None

        print(f"    INFO: Parsed {len(entries)} entries from ANVISA tecnovigilancia")

        new_items = []
        all_ids = list(prev_ids)
        cutoff = (datetime.now() - timedelta(days=90)).strftime("%Y-%m-%d")

        for entry in entries:
            eid = entry.get("id") or entry.get("title", "")
            if not eid or eid in prev_ids:
                continue
            all_ids.append(eid)
            pub = entry.get("pub_date", "")
            if pub and pub < cutoff:
                continue
            new_items.append(entry)

        self.state[source_id] = {
            "url": url,
            "last_checked": datetime.now().isoformat(),
            "seen_ids": all_ids[-500:],
        }

        if new_items and (prev_ids or self.seed_mode):
            if self.seed_mode and not prev_ids:
                new_items = new_items[:10]
                print(f"    INFO: Seed mode -- returning top {len(new_items)} ANVISA entries")
            result = _make_update(
                source_id, source, "anvisa_page",
                f"{len(new_items)} new ANVISA tecnovigilance alert(s) detected"
            )
            result["new_items"] = new_items
            return result
        elif not prev_ids:
            print(f"    INFO: Baseline established ({len(entries)} ANVISA entries)")

        return None

    @staticmethod
    def _parse_alerts(html: str) -> list[dict]:
        import re
        results = []
        try:
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(html, "html.parser")
            for div in soup.find_all("div", class_="lista-noticias"):
                date_div = div.find("div", class_="data-hora")
                title_div = div.find("div", class_="titulo-resumo")
                if not title_div:
                    continue
                a_tag = title_div.find("a")
                if not a_tag:
                    continue

                title = a_tag.get_text(strip=True)
                link = a_tag.get("href", "")
                if link and not link.startswith("http"):
                    link = "https://antigo.anvisa.gov.br" + link

                date_text = date_div.get_text(strip=True) if date_div else ""
                dm = re.search(r"(\d{2})/(\d{2})/(\d{4})", date_text)
                pub_date = f"{dm.group(3)}-{dm.group(2)}-{dm.group(1)}" if dm else ""

                alert_id = ""
                am = re.search(r"Alerta\s+(\d+)", title)
                if am:
                    alert_id = f"ANVISA-{am.group(1)}"

                results.append({
                    "id": alert_id,
                    "title": title,
                    "link": link,
                    "pub_date": pub_date,
                    "description": "",
                })
        except ImportError:
            pass
        return results


# ---------------------------------------------------------------------------
# Swissmedic FSCA CSV Checker
# Uses the public FSCA export API: CSV format, no auth required.
# URL: https://fsca.swissmedic.ch/mep/api/publications/export
# ---------------------------------------------------------------------------

class SwissmedicChecker:
    """Checks Swissmedic FSCA (Field Safety Corrective Actions) via CSV export API.

    The API returns a CSV with columns:
    swissmedicRef, publicationDate, statusDate, reason, manufacturer,
    tradename, description, model, lot, sn, softwareVersion, directLink
    """

    EXPORT_URL = ("https://fsca.swissmedic.ch/mep/api/publications/export"
                  "?direction=DESC&onlyUpdates=false&sortingProperty=PUBLICATION_DATE")

    def __init__(self, session: requests.Session, state: dict,
                 seed_mode: bool = False):
        self.session = session
        self.state = state
        self.seed_mode = seed_mode

    def check(self, source_id: str, source: dict) -> Optional[dict]:
        prev = self.state.get(source_id, {})
        prev_refs = set(prev.get("seen_refs", []))

        try:
            resp = self.session.get(self.EXPORT_URL, timeout=30)
            resp.raise_for_status()
        except Exception as e:
            print(f"    ERROR Swissmedic CSV: {e}")
            return None

        entries = self._parse_csv(resp.text)
        if not entries:
            print("    WARNING: No entries parsed from Swissmedic CSV")
            return None

        print(f"    INFO: Parsed {len(entries)} entries from Swissmedic FSCA CSV")

        md_only = source.get("device_only", True)
        new_items = []
        all_refs = list(prev_refs)

        for entry in entries:
            ref = entry.get("ref", "")
            if not ref or ref in prev_refs:
                continue
            if md_only and not entry.get("description", "").startswith("MD:"):
                continue
            all_refs.append(ref)
            new_items.append({
                "title": f"{entry.get('tradename', 'Unknown')} - {entry.get('manufacturer', '')}".strip(" -"),
                "link": entry.get("link", ""),
                "pub_date": entry.get("pub_date", ""),
                "description": f"FSCA: {entry.get('description', '')}. "
                               f"Reason: {entry.get('reason', 'N/A')}. "
                               f"Model: {entry.get('model', 'N/A')}."[:300],
            })

        self.state[source_id] = {
            "url": self.EXPORT_URL,
            "last_checked": datetime.now().isoformat(),
            "seen_refs": all_refs[-1000:],
        }

        if new_items and (prev_refs or self.seed_mode):
            if self.seed_mode and not prev_refs:
                new_items = new_items[:10]
                print(f"    INFO: Seed mode -- returning top {len(new_items)} Swissmedic FSCA entries")
            result = _make_update(
                source_id, source, "swissmedic_csv",
                f"{len(new_items)} new Swissmedic FSCA(s) detected"
            )
            result["new_items"] = new_items
            return result
        elif not prev_refs:
            print(f"    INFO: Baseline established ({len(entries)} Swissmedic entries)")

        return None

    @staticmethod
    def _parse_csv(text: str) -> list[dict]:
        results = []
        lines = text.strip().split("\n")
        if not lines:
            return results
        start = 0
        for i, line in enumerate(lines):
            if line.startswith("swissmedicRef,"):
                start = i
                break
        try:
            reader = csv.DictReader(lines[start:])
            for row in reader:
                ref = row.get("swissmedicRef", "").strip()
                if not ref:
                    continue
                results.append({
                    "ref": ref,
                    "pub_date": row.get("publicationDate", ""),
                    "manufacturer": row.get("manufacturer", ""),
                    "tradename": row.get("tradename", ""),
                    "description": row.get("description", ""),
                    "reason": row.get("reason", ""),
                    "model": row.get("model", ""),
                    "link": row.get("directLink", ""),
                })
        except Exception as e:
            print(f"    ERROR parsing Swissmedic CSV: {e}")
        return results[:100]


# ---------------------------------------------------------------------------
# SFDA (Saudi Arabia) Weekly Alert Checker
# Parses the NCMDR weekly alert page for new medical device safety reports.
# Also supports SFDA RSS feed for general medical device sector news.
# ---------------------------------------------------------------------------

class SFDAChecker:
    """Checks SFDA (Saudi Arabia) for medical device safety updates.

    Two sources:
    1. NCMDR Weekly Alert page (weekly PDF reports) -- parsed from HTML table
    2. SFDA RSS feed (general medical device news) -- filtered for device content
    """

    def __init__(self, session: requests.Session, state: dict,
                 seed_mode: bool = False):
        self.session = session
        self.state = state
        self.seed_mode = seed_mode

    def check(self, source_id: str, source: dict) -> Optional[dict]:
        check_sub = source.get("check_sub", "weekly_alert")
        if check_sub == "rss":
            return self._check_rss(source_id, source)
        return self._check_weekly_alert(source_id, source)

    def _check_weekly_alert(self, source_id: str, source: dict) -> Optional[dict]:
        url = source["url"]
        prev = self.state.get(source_id, {})
        prev_ids = set(prev.get("seen_ids", []))

        try:
            resp = self.session.get(url, timeout=30)
            resp.raise_for_status()
        except Exception as e:
            print(f"    ERROR SFDA weekly: {e}")
            return None

        entries = self._parse_weekly_page(resp.text)
        if not entries:
            print("    WARNING: No entries from SFDA weekly alert page")
            return None

        print(f"    INFO: Parsed {len(entries)} weekly reports from SFDA")

        new_items = []
        all_ids = list(prev_ids)

        for entry in entries:
            eid = entry.get("id", entry.get("title", ""))
            if not eid or eid in prev_ids:
                continue
            all_ids.append(eid)
            new_items.append(entry)

        self.state[source_id] = {
            "url": url,
            "last_checked": datetime.now().isoformat(),
            "seen_ids": all_ids[-200:],
        }

        if new_items and (prev_ids or self.seed_mode):
            if self.seed_mode and not prev_ids:
                new_items = new_items[:5]
                print(f"    INFO: Seed mode -- returning top {len(new_items)} SFDA weekly reports")
            result = _make_update(
                source_id, source, "sfda_weekly",
                f"{len(new_items)} new SFDA weekly report(s) detected"
            )
            result["new_items"] = new_items
            return result
        elif not prev_ids:
            print(f"    INFO: Baseline established ({len(entries)} SFDA weekly reports)")

        return None

    def _check_rss(self, source_id: str, source: dict) -> Optional[dict]:
        url = source["url"]
        prev = self.state.get(source_id, {})
        prev_ids = set(prev.get("seen_ids", []))
        title_filter = source.get("title_filter")

        try:
            resp = self.session.get(url, timeout=30)
            resp.raise_for_status()
        except Exception as e:
            print(f"    ERROR SFDA RSS: {e}")
            return None

        import xml.etree.ElementTree as ET
        entries = []
        try:
            root = ET.fromstring(resp.content)
            for item in root.findall(".//item")[:30]:
                title_el = item.find("title")
                link_el = item.find("link")
                desc_el = item.find("description")
                title = (title_el.text or "").strip() if title_el is not None else ""
                link = (link_el.text or "").strip() if link_el is not None else ""
                desc = (desc_el.text or "").strip()[:300] if desc_el is not None else ""
                if title_filter and not re.search(title_filter, title + " " + desc, re.IGNORECASE):
                    continue
                entries.append({
                    "title": title,
                    "link": link,
                    "pub_date": "",
                    "description": desc,
                })
        except ET.ParseError as e:
            print(f"    ERROR parsing SFDA RSS: {e}")
            return None

        if not entries:
            print("    WARNING: No device-relevant entries from SFDA RSS")
            return None

        print(f"    INFO: {len(entries)} entries from SFDA RSS (after filter)")

        new_items = []
        all_ids = list(prev_ids)

        for entry in entries:
            eid = entry.get("link") or entry.get("title", "")
            if not eid or eid in prev_ids:
                continue
            all_ids.append(eid)
            new_items.append(entry)

        self.state[source_id] = {
            "url": url,
            "last_checked": datetime.now().isoformat(),
            "seen_ids": all_ids[-300:],
        }

        if new_items and (prev_ids or self.seed_mode):
            if self.seed_mode and not prev_ids:
                new_items = new_items[:10]
            result = _make_update(
                source_id, source, "sfda_rss",
                f"{len(new_items)} new SFDA news item(s) detected"
            )
            result["new_items"] = new_items
            return result
        elif not prev_ids:
            print(f"    INFO: Baseline established ({len(entries)} SFDA RSS entries)")

        return None

    @staticmethod
    def _parse_weekly_page(html: str) -> list[dict]:
        """Parse SFDA weekly alert page.

        PDF links have empty text -- WU number and date are encoded
        in the URL-encoded href path, e.g.:
        /sites/default/files/2026-06/%28WU2627%29%20NCMDR%20Weekly%20Update%2028%20June%202026.pdf
        """
        results = []
        from urllib.parse import unquote

        MONTH_MAP = {
            "january": "01", "february": "02", "march": "03", "april": "04",
            "may": "05", "june": "06", "july": "07", "august": "08",
            "september": "09", "october": "10", "november": "11", "december": "12",
        }

        try:
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(html, "html.parser")
            for a in soup.find_all("a", href=True):
                href = a.get("href", "")
                if ".pdf" not in href.lower():
                    continue
                decoded = unquote(href)
                wu_match = re.search(r"WU(\d{4})", decoded)
                if not wu_match:
                    continue
                wu_num = wu_match.group(1)
                wu_id = f"WU{wu_num}"
                if not href.startswith("http"):
                    href = "https://www.sfda.gov.sa" + href
                date_match = re.search(
                    r"(\d{1,2})\s+(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{4})",
                    decoded, re.IGNORECASE,
                )
                date_str = ""
                if date_match:
                    day = date_match.group(1).zfill(2)
                    month = MONTH_MAP.get(date_match.group(2).lower(), "01")
                    year = date_match.group(3)
                    date_str = f"{year}-{month}-{day}"
                results.append({
                    "id": wu_id,
                    "title": f"SFDA NCMDR Weekly Update ({wu_id})",
                    "link": href,
                    "pub_date": date_str,
                    "description": f"Saudi FDA National Center for Medical Devices Reporting weekly safety update report {wu_id}.",
                })
        except ImportError:
            decoded_html = unquote(html)
            for m in re.finditer(r"WU(\d{4})", decoded_html):
                wu_id = f"WU{m.group(1)}"
                results.append({
                    "id": wu_id,
                    "title": f"SFDA NCMDR Weekly Update ({wu_id})",
                    "link": "https://www.sfda.gov.sa/en/weekly-alert",
                    "pub_date": "",
                    "description": f"Saudi FDA NCMDR weekly safety update report {wu_id}.",
                })
        return results


# ---------------------------------------------------------------------------
# Medsafe (New Zealand) Safety Communications Checker
# Parses the structured table at medsafe.govt.nz/safety/SafetyCommunications.asp
# ---------------------------------------------------------------------------

class MedsafeChecker:
    """Checks Medsafe (NZ) Safety Communications for medical device alerts.

    Parses the HTML table with columns: Date, Communication, Product Type, Topic.
    Filters for Product Type containing 'Device'.
    """

    def __init__(self, session: requests.Session, state: dict,
                 seed_mode: bool = False):
        self.session = session
        self.state = state
        self.seed_mode = seed_mode

    def check(self, source_id: str, source: dict) -> Optional[dict]:
        url = source.get("url", "https://medsafe.govt.nz/safety/SafetyCommunications.asp")
        prev = self.state.get(source_id, {})
        prev_ids = set(prev.get("seen_ids", []))

        try:
            resp = self.session.get(url, timeout=30, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/130.0",
            })
            resp.raise_for_status()
        except Exception as e:
            print(f"    ERROR Medsafe: {e}")
            return None

        entries = self._parse_table(resp.text)
        if not entries:
            print("    WARNING: No entries from Medsafe Safety Communications")
            return None

        print(f"    INFO: Parsed {len(entries)} device entries from Medsafe")

        new_items = []
        all_ids = list(prev_ids)

        for entry in entries:
            eid = entry.get("title", "")
            if not eid or eid in prev_ids:
                continue
            all_ids.append(eid)
            new_items.append(entry)

        self.state[source_id] = {
            "url": url,
            "last_checked": datetime.now().isoformat(),
            "seen_ids": all_ids[-200:],
        }

        if new_items and (prev_ids or self.seed_mode):
            if self.seed_mode and not prev_ids:
                new_items = new_items[:10]
                print(f"    INFO: Seed mode -- returning top {len(new_items)} Medsafe entries")
            result = _make_update(
                source_id, source, "medsafe_page",
                f"{len(new_items)} new Medsafe device safety communication(s)"
            )
            result["new_items"] = new_items
            return result
        elif not prev_ids:
            print(f"    INFO: Baseline established ({len(entries)} Medsafe entries)")

        return None

    @staticmethod
    def _parse_table(html: str) -> list[dict]:
        import re
        results = []
        try:
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(html, "html.parser")
            table = soup.find("table")
            if not table:
                return results
            for tr in table.find_all("tr")[1:]:
                cells = tr.find_all("td")
                if len(cells) < 4:
                    continue
                date_text = cells[0].get_text(strip=True)
                comm_type = cells[1].get_text(strip=True)
                prod_type = cells[2].get_text(strip=True)
                topic = cells[3].get_text(strip=True)
                if "device" not in prod_type.lower():
                    continue
                a_tag = cells[3].find("a")
                link = ""
                if a_tag and a_tag.get("href"):
                    href = a_tag["href"]
                    if not href.startswith("http"):
                        link = "https://medsafe.govt.nz/safety/" + href
                    else:
                        link = href
                dm = re.search(r"(\d{1,2})\s+(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{4})", date_text)
                pub_date = ""
                if dm:
                    month_map = {"January": "01", "February": "02", "March": "03", "April": "04",
                                 "May": "05", "June": "06", "July": "07", "August": "08",
                                 "September": "09", "October": "10", "November": "11", "December": "12"}
                    pub_date = f"{dm.group(3)}-{month_map.get(dm.group(2), '01')}-{dm.group(1).zfill(2)}"
                results.append({
                    "title": f"[{comm_type}] {topic}",
                    "link": link,
                    "pub_date": pub_date,
                    "description": f"Medsafe {comm_type} - Product: {prod_type}",
                })
        except ImportError:
            pass
        return results
