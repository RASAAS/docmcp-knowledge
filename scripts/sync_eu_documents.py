#!/usr/bin/env python3
"""Write new EU legal acts and MDCG guidance into the catalog.

The harmonised-standards job updates the Official Journal list and the
amendment explanation. It does not download ISO, IEC, or EN standard texts.

    python scripts/sync_eu_documents.py
    python scripts/sync_eu_documents.py --mdcg-limit 8 --reg-limit 4
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))

import eu_fulltext as eu

ROOT = Path(__file__).resolve().parent.parent
STATE_PATH = ROOT / "scripts" / ".eu_fulltext_state.json"
SPARQL_URL = "https://publications.europa.eu/webapi/rdf/sparql"
SPARQL_QUERY = """
PREFIX cdm: <http://publications.europa.eu/ontology/cdm#>
SELECT DISTINCT ?celex WHERE {
  ?work cdm:resource_legal_id_celex ?celex .
  FILTER(STRSTARTS(?celex, "02021D1182"))
} ORDER BY DESC(?celex) LIMIT 1
"""
MDCG_PAGE = (
    "https://health.ec.europa.eu/medical-devices-sector/"
    "new-regulations/guidance-mdcg-endorsed-documents-and-other-guidance_en"
)
EC_UPDATES = "https://health.ec.europa.eu/medical-devices-sector/latest-updates_en"
MIN_BODY = 500


def session() -> requests.Session:
    client = requests.Session()
    client.headers.update({
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
        ),
        "Accept": "application/xhtml+xml,text/html;q=0.9,*/*;q=0.8",
        "Accept-Language": "en",
    })
    return client


def load_state() -> dict:
    if not STATE_PATH.exists():
        return {}
    return json.loads(STATE_PATH.read_text(encoding="utf-8"))


def save_state(state: dict) -> None:
    STATE_PATH.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def fetch_celex_html(client: requests.Session, celex: str) -> str:
    response = client.get(
        f"https://publications.europa.eu/resource/celex/{celex}",
        timeout=60,
        allow_redirects=True,
    )
    response.raise_for_status()
    if len(response.content) < 1000:
        raise RuntimeError(f"CELEX {celex} returned {len(response.content)} bytes")
    return response.text


def _load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _write_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _entries(data: dict) -> list:
    if isinstance(data.get("standards"), list):
        return data["standards"]
    if isinstance(data.get("entries"), list):
        return data["entries"]
    return []


def sync_standards(client: requests.Session) -> dict:
    print("== Harmonised standards list ==")
    response = client.get(SPARQL_URL, params={"query": SPARQL_QUERY, "format": "application/json"}, timeout=40)
    response.raise_for_status()
    bindings = response.json().get("results", {}).get("bindings", [])
    if not bindings:
        print("  No consolidated CELEX")
        return {}
    celex = bindings[0].get("celex", {}).get("value", "")
    print(f"  Consolidated {celex}")
    html = fetch_celex_html(client, celex)
    rows = eu.parse_consolidated_annex(html)
    print(f"  Annex rows {len(rows)}")
    if len(rows) < 40:
        print("  Annex parse too short; list left unchanged")
        return {"rows": len(rows)}

    standards_dir = ROOT / "eu_mdr" / "standards"
    index = _load_json(standards_dir / "_index.json")
    files = {}
    pooled = []
    for cat, info in index.get("categories", {}).items():
        path = standards_dir / info["file"]
        data = _load_json(path)
        files[cat] = (path, data)
        for entry in _entries(data):
            entry.setdefault("category", cat)
            pooled.append(entry)

    source_url = f"https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:{celex}"
    today = datetime.now().strftime("%Y-%m-%d")
    result = eu.merge_harmonised_entries(pooled, rows, source_url, today)
    print(
        f"  Added {len(result['added'])}, updated {len(result['updated'])}, "
        f"withdrawn {len(result['withdrawn'])}"
    )

    by_cat: dict[str, list] = {}
    for entry in pooled:
        by_cat.setdefault(entry.get("category") or "general", []).append(entry)
    touched = set(result["added"] + result["updated"] + result["withdrawn"])
    for cat, entries in by_cat.items():
        if not any(entry.get("number") in touched for entry in entries):
            continue
        if cat not in files:
            filename = f"standards-{cat}.json"
            files[cat] = (standards_dir / filename, {"standards": []})
            index.setdefault("categories", {})[cat] = {
                "name": {"zh": cat, "en": cat},
                "count": 0,
                "file": filename,
            }
        path, data = files[cat]
        if "standards" in data:
            data["standards"] = entries
        elif "entries" in data:
            data["entries"] = entries
        else:
            data["standards"] = entries
        data["count"] = len(entries)
        _write_json(path, data)
        index["categories"][cat]["count"] = len(entries)

    amendment = eu.latest_amendment_celex(html)
    decision = eu.celex_to_decision_number(amendment)
    if decision:
        index["latest_amendment"] = decision
        index["latest_amendment_url"] = f"https://eur-lex.europa.eu/eli/dec_impl/{decision}/oj"
    index["last_updated"] = today
    active = [entry for entry in pooled if entry.get("status") != "withdrawn" and entry.get("category") != "software"]
    index["total_standards"] = len(active)
    index["harmonised_count"] = len(active)
    _write_json(standards_dir / "_index.json", index)

    if amendment:
        try:
            notes = eu.decision_explanation(fetch_celex_html(client, amendment))
        except Exception as exc:
            print(f"  Amendment text skipped: {exc}")
            notes = ""
        if len(notes) >= MIN_BODY:
            _write_notes(decision, amendment, notes)
            print(f"  Wrote amendment explanation {decision} ({len(notes)} chars)")

    _refresh_overview(index, result["added"])
    if result["added"] or result["updated"] or result["withdrawn"]:
        from json_to_markdown import generate_standards
        generate_standards()
    return result


def _write_notes(decision: str, celex: str, body: str) -> None:
    source = f"https://eur-lex.europa.eu/eli/dec_impl/{decision}/oj"
    zh = (
        "---\n"
        f"title: 协调标准清单说明（CID (EU) {decision}）\n"
        "---\n\n"
        f"# 协调标准清单说明（CID (EU) {decision}）\n\n"
        "本页是欧盟官方公报修正决定的说明，用来交代清单为何变化。"
        "协调标准正文不收录。\n\n"
        f"**官方来源**：[{source}]({source})\n\n"
        f"{body.strip()}\n"
    )
    en = (
        "---\n"
        f"title: Harmonised standards list note (CID (EU) {decision})\n"
        "---\n\n"
        f"# Harmonised standards list note (CID (EU) {decision})\n\n"
        "This page is the Official Journal explanation of the latest list change. "
        "The text of the harmonised standards themselves is not stored.\n\n"
        f"**Source**: [{source}]({source})\n\n"
        f"{body.strip()}\n"
    )
    for path, text in (
        (ROOT / "eu_mdr" / "standards" / "oj-notes.md", zh),
        (ROOT / "docs" / "zh" / "eu_mdr" / "standards" / "oj-notes.md", zh),
        (ROOT / "docs" / "en" / "eu_mdr" / "standards" / "oj-notes.md", en),
    ):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")


def _refresh_overview(index: dict, added: list[str]) -> None:
    total = index.get("total_standards", 0)
    amendment = index.get("latest_amendment", "")
    amendment_url = index.get("latest_amendment_url", "")
    replacements = {
        ROOT / "docs" / "zh" / "eu_mdr" / "standards.md": (
            rf"共计: \*\*\d+\*\*",
            f"共计: **{total}**",
            f"- **公报说明**：[CID (EU) {amendment} 说明](./standards/oj-notes)",
        ),
        ROOT / "docs" / "en" / "eu_mdr" / "standards.md": (
            r"Total: \*\*\d+\*\*",
            f"Total: **{total}**",
            f"- **List note**: [CID (EU) {amendment} explanation](./standards/oj-notes)",
        ),
    }
    zh_extra = _added_block("公报新增", added)
    en_extra = _added_block("Added in the latest Official Journal list", added)
    extras = {
        ROOT / "docs" / "zh" / "eu_mdr" / "standards.md": zh_extra,
        ROOT / "docs" / "en" / "eu_mdr" / "standards.md": en_extra,
    }
    for path, (pattern, repl, note_line) in replacements.items():
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        text = re.sub(pattern, repl, text, count=1)
        if "oj-notes" not in text and amendment:
            text = text.replace(
                f"[CID (EU) {amendment}]({amendment_url})",
                f"[CID (EU) {amendment}]({amendment_url})\n{note_line}",
                1,
            )
        extra = extras[path]
        if extra and "oj-added-list" not in text:
            warning = "::: warning"
            if warning in text:
                text = text.replace(warning, extra + "\n" + warning, 1)
            else:
                text = text.rstrip() + "\n" + extra
        path.write_text(text, encoding="utf-8")


def _added_block(heading: str, added: list[str]) -> str:
    if not added:
        return ""
    lines = ["", f"<!-- oj-added-list -->", f"## {heading}", ""]
    lines.extend(f"- {number}" for number in added)
    return "\n".join(lines) + "\n"


def _append_mdcg_row(slug: str, title: str, year: str) -> None:
    """List a filed guide that the hand-maintained catalog does not already link."""
    site_path = f"./mdcg/{slug}"
    label = slug.removeprefix("mdcg-")
    sections = {
        "zh": ("## 新收录全文", "| 文件 | 标题 | 年份 |\n|------|------|------|"),
        "en": ("## Newly filed full text", "| Document | Title | Year |\n|----------|-------|------|"),
    }
    for lang, docs in (("zh", ROOT / "docs" / "zh" / "eu_mdr" / "mdcg.md"), ("en", ROOT / "docs" / "en" / "eu_mdr" / "mdcg.md")):
        if not docs.exists():
            continue
        text = docs.read_text(encoding="utf-8")
        if site_path in text:
            continue
        heading, header = sections[lang]
        row = f"| [MDCG {label}]({site_path}) | {title} | {year} |"
        if heading not in text:
            text = text.rstrip() + f"\n\n{heading}\n\n{header}\n{row}\n"
        else:
            text = text.rstrip() + f"\n{row}\n"
        docs.write_text(text, encoding="utf-8")


def sync_mdcg(client: requests.Session, limit: int) -> int:
    print("== MDCG full text ==")
    index = _load_json(ROOT / "eu_mdr" / "mdcg" / "_index.json")
    full_dir = ROOT / "eu_mdr" / "mdcg" / "fulltext"
    full_dir.mkdir(parents=True, exist_ok=True)
    written = 0
    embedded = 0
    entries = sorted(
        index.get("entries", []),
        key=lambda item: item.get("published_date") or item.get("id") or "",
        reverse=True,
    )
    downloads = 0
    for entry in entries:
        slug = entry.get("slug") or entry.get("id") or ""
        url = entry.get("source_url") or ""
        if not slug or eu.is_standard_body_url(url):
            continue
        if ".pdf" not in url.lower():
            continue
        full_path = full_dir / f"{slug}.md"
        body = ""
        if full_path.exists() and full_path.stat().st_size > MIN_BODY:
            body = full_path.read_text(encoding="utf-8")
        elif downloads < limit:
            try:
                response = client.get(url, timeout=60, headers={"Referer": MDCG_PAGE})
                response.raise_for_status()
            except Exception as exc:
                print(f"  Skip {slug}: {exc}")
                continue
            if not response.content.startswith(b"%PDF"):
                print(f"  Skip {slug}: not a PDF")
                continue
            body = _pdf_text(response.content)
            downloads += 1
            if len(body) < MIN_BODY:
                print(f"  Skip {slug}: extract too short")
                continue
            full_path.write_text(body, encoding="utf-8")
            written += 1
            print(f"  Full text {slug} ({len(body)} chars)")
        if not body:
            continue
        title = ""
        raw_title = entry.get("title")
        if isinstance(raw_title, dict):
            title = raw_title.get("en") or raw_title.get("zh") or slug
        else:
            title = str(raw_title or slug)
        for lang, docs in (("zh", ROOT / "docs" / "zh" / "eu_mdr" / "mdcg"), ("en", ROOT / "docs" / "en" / "eu_mdr" / "mdcg")):
            page = docs / f"{slug}.md"
            heading = "官方全文" if lang == "zh" else "Official text"
            if page.exists():
                current = page.read_text(encoding="utf-8")
                if eu.page_already_has_fulltext(current):
                    continue
                page.write_text(eu.embed_fulltext(current, body, heading), encoding="utf-8")
            else:
                intro = f"# {title}\n\n**Source**: [{url}]({url})\n"
                page.parent.mkdir(parents=True, exist_ok=True)
                page.write_text("---\ntitle: " + title.replace(":", " -") + "\n---\n\n" + eu.embed_fulltext(intro, body, heading), encoding="utf-8")
            embedded += 1
        for catalog in (ROOT / "docs" / "zh" / "eu_mdr" / "mdcg.md", ROOT / "docs" / "en" / "eu_mdr" / "mdcg.md"):
            if not catalog.exists():
                continue
            text = catalog.read_text(encoding="utf-8")
            updated = eu.retarget_link(text, url, f"./mdcg/{slug}")
            if updated != text:
                catalog.write_text(updated, encoding="utf-8")
        year = str(entry.get("published_date") or "")[:4]
        _append_mdcg_row(slug, title.replace("|", "/").replace("\n", " "), year)
    print(f"  New extracts {written}, pages updated {embedded}")
    return written


def _pdf_text(data: bytes) -> str:
    import fitz
    document = fitz.open(stream=data, filetype="pdf")
    pages = []
    for page in document:
        text = page.get_text("text").strip()
        if text:
            pages.append(text)
    document.close()
    return eu.reflow_pdf_text("\n\n".join(pages))


def _known_celex() -> set[str]:
    known = set()
    index_path = ROOT / "eu_mdr" / "regulations" / "_index.json"
    if index_path.exists():
        for item in _load_json(index_path).get("documents", []):
            if item.get("celex"):
                known.add(str(item["celex"]).upper())
    for path in (ROOT / "eu_mdr" / "regulations" / "fulltext").glob("*.md"):
        match = re.search(r"(3\d{4}[A-Z]\d{3,5})", path.stem.upper())
        if match:
            known.add(match.group(1))
    return known


def sync_regulations(client: requests.Session, limit: int) -> int:
    print("== EU legal acts ==")
    try:
        page = client.get(EC_UPDATES, timeout=40)
        page.raise_for_status()
    except Exception as exc:
        print(f"  Latest updates unavailable: {exc}")
        return 0
    articles = re.findall(r'<article[\s\S]*?</article>', page.text)
    print(f"  Latest-update cards {len(articles)}")
    known = _known_celex()
    written = 0
    for article in articles:
        if written >= limit:
            break
        link_match = re.search(r'href="([^"]+)"', article)
        if not link_match:
            continue
        link = link_match.group(1)
        if link.startswith("/"):
            link = "https://health.ec.europa.eu" + link
        if eu.is_standard_body_url(link):
            continue
        try:
            detail = client.get(link, timeout=40)
            detail.raise_for_status()
        except Exception as exc:
            print(f"  Skip article: {exc}")
            continue
        title_match = re.search(r"<title>([^<]+)</title>", detail.text)
        page_title = re.sub(r"\s+", " ", title_match.group(1)).strip() if title_match else ""
        for celex in eu.celex_numbers_in(detail.text):
            if written >= limit or celex in known:
                continue
            if celex.startswith("0"):
                continue
            if eu.is_harmonised_standards_act(page_title, celex):
                continue
            try:
                html = fetch_celex_html(client, celex)
            except Exception as exc:
                print(f"  Skip {celex}: {exc}")
                continue
            act_title = eu.act_heading(html)
            if eu.is_harmonised_standards_act(act_title, celex):
                continue
            body = eu.legal_act_markdown(html)
            if len(body) < MIN_BODY:
                print(f"  Skip {celex}: text too short")
                continue
            slug = f"eu-act-{celex.lower()}"
            source = f"https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:{celex}"
            text = (
                "---\n"
                f"title: {act_title or celex}\n"
                "---\n\n"
                f"# {act_title or celex}\n\n"
                f"**Source**: [{source}]({source})\n\n"
                f"{body}\n"
            )
            full = ROOT / "eu_mdr" / "regulations" / "fulltext" / f"{slug}.md"
            full.parent.mkdir(parents=True, exist_ok=True)
            full.write_text(text, encoding="utf-8")
            for docs in (ROOT / "docs" / "zh" / "eu_mdr" / "regulations", ROOT / "docs" / "en" / "eu_mdr" / "regulations"):
                docs.mkdir(parents=True, exist_ok=True)
                (docs / f"{slug}.md").write_text(text, encoding="utf-8")
            _append_regulation_index(celex, slug, act_title or celex, source)
            known.add(celex)
            written += 1
            print(f"  Legal act {celex} ({len(body)} chars)")
            break
    print(f"  New legal acts {written}")
    return written


def _append_regulation_index(celex: str, slug: str, title: str, source: str) -> None:
    index_path = ROOT / "eu_mdr" / "regulations" / "_index.json"
    data = _load_json(index_path)
    documents = data.setdefault("documents", [])
    if any(item.get("celex") == celex for item in documents):
        return
    documents.append({
        "id": slug,
        "slug": slug,
        "celex": celex,
        "title": {"zh": title, "en": title},
        "status": "active",
        "source_url": source,
    })
    data["last_updated"] = datetime.now().strftime("%Y-%m-%d")
    _write_json(index_path, data)
    row = f"| {celex} | {title} | [全文](./regulations/{slug}) |\n"
    for path in (ROOT / "docs" / "zh" / "eu_mdr" / "regulations.md", ROOT / "docs" / "en" / "eu_mdr" / "regulations.md"):
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        if slug in text:
            continue
        heading = "\n## 新发布法规\n\n| CELEX | 标题 | 全文 |\n|------|------|------|\n"
        if path.as_posix().endswith("/en/eu_mdr/regulations.md"):
            heading = "\n## Newly published acts\n\n| CELEX | Title | Text |\n|------|------|------|\n"
        if "新发布法规" in text or "Newly published acts" in text:
            text = text.rstrip() + "\n" + row
        else:
            text = text.rstrip() + "\n" + heading + row
        path.write_text(text, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mdcg-limit", type=int, default=8)
    parser.add_argument("--reg-limit", type=int, default=4)
    parser.add_argument("--skip-standards", action="store_true")
    parser.add_argument("--skip-mdcg", action="store_true")
    parser.add_argument("--skip-regulations", action="store_true")
    args = parser.parse_args()
    client = session()
    if not args.skip_standards:
        sync_standards(client)
    if not args.skip_mdcg:
        sync_mdcg(client, args.mdcg_limit)
    if not args.skip_regulations:
        sync_regulations(client, args.reg_limit)


if __name__ == "__main__":
    main()
