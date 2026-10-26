#!/usr/bin/env python3
"""Download gov.cn 通告/法规/指导原则 full text into the public catalog.

Reads the same policy search the news job uses. For each device document
it opens the article, downloads a .doc/.docx/.pdf attachment when the
page has one, and writes or updates nmpa/guidance or nmpa/regulations.
The VitePress catalog is regenerated from those files.

Existing long pages are kept. A short placeholder is replaced when the
official text is longer. A page that already has the full text only
gets its source address pointed at the official page.
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

import generate_docs_index as docs_index
import official_fulltext as fulltext
import official_notices as notices

QUERIES = ("医疗器械", "指导原则")
COUNT_KEY = {
    "create": "created",
    "replace": "replaced",
    "retarget": "retargeted",
    "present": "present",
    "no_fulltext": "no_fulltext",
}


def fetch_policy(session: requests.Session, pages: int) -> list[dict]:
    entries = []
    seen = set()
    for query in QUERIES:
        for page in range(pages):
            resp = session.get(
                notices.GOV_SEARCH_URL,
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
                headers={"User-Agent": "Mozilla/5.0", "Accept": "application/json"},
            )
            resp.raise_for_status()
            for item in notices.parse_gov_policy(resp.json()):
                if item["link"] in seen:
                    continue
                seen.add(item["link"])
                entries.append(item)
    entries.sort(key=lambda item: item.get("pub_date") or "", reverse=True)
    return entries


def load_state(path: Path) -> dict:
    if not path.is_file():
        return {"done": {}}
    data = json.loads(path.read_text(encoding="utf-8"))
    data.setdefault("done", {})
    return data


def save_state(path: Path, state: dict) -> None:
    path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def fetch_article(session: requests.Session, url: str) -> tuple[str, str]:
    resp = session.get(url, timeout=40, headers={"User-Agent": "Mozilla/5.0", "Referer": "https://www.gov.cn/"})
    resp.raise_for_status()
    resp.encoding = resp.apparent_encoding or "utf-8"
    html_body, links = fulltext.parse_article(resp.text, url)
    best = html_body
    attachment = ""
    for link in links:
        try:
            got = session.get(link, timeout=60, headers={"User-Agent": "Mozilla/5.0", "Referer": url})
        except requests.RequestException:
            continue
        if got.status_code != 200 or not fulltext.looks_like_file(got.content):
            continue
        text = fulltext.bytes_to_text(got.content)
        if len(text) > len(best):
            best = text
            attachment = link
    return best, attachment


def publish_new(repo: Path, pages: list[dict], title: str, section: str, body: str,
                source_url: str, attachment: str, published: str, doc_number: str,
                prefix: str = "gov") -> dict:
    slug = fulltext.slug_for(title, published, prefix)
    taken = {page["slug"] for page in pages}
    if slug in taken:
        slug = slug + "-2"
    page = fulltext.render_page(
        doc_id=f"nmpa-{slug}",
        title=title,
        section=section,
        doc_number=doc_number,
        source_url=source_url,
        attachment=attachment,
        published=published or datetime.now().strftime("%Y-%m-%d"),
        body=body,
    )
    path = repo / section / f"{slug}.zh.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(page, encoding="utf-8")
    record = {
        "section": section,
        "path": path,
        "slug": slug,
        "title": title,
        "key": fulltext.normalize_key(title),
        "body_len": len(body),
        "source_url": source_url,
        "doc_id": f"nmpa-{slug}",
    }
    pages.append(record)
    return record


def retarget(page: dict, source_url: str, published: str) -> None:
    text = page["path"].read_text(encoding="utf-8")
    page["path"].write_text(fulltext.set_official_source(text, source_url, published), encoding="utf-8")
    page["source_url"] = source_url


def fetch_cmde_notices(session: requests.Session, pages: int) -> list[dict]:
    """Guidance text library first, then published-notice pages for bundled attachments."""
    notices_found = []
    seen = set()
    for base in (fulltext.CMDE_PRINCIPLE_URL, fulltext.CMDE_RELEASE_URL):
        for index in range(pages):
            url = base if index == 0 else f"{base}-{index + 1}"
            try:
                resp = session.get(url, timeout=30, headers={"User-Agent": "Mozilla/5.0"})
                resp.raise_for_status()
            except Exception as exc:
                print(f"  FAIL cmde list {url} {exc}")
                break
            resp.encoding = resp.apparent_encoding or "utf-8"
            article_links = {
                href for href in re.findall(r'href="(/article/\d+)"', resp.text)
                if href != "/article/805"
            }
            if not article_links:
                break
            for item in fulltext.parse_cmde_release_list(resp.text):
                if item["link"] in seen:
                    continue
                seen.add(item["link"])
                notices_found.append(item)
    return notices_found


def sync_cmde(session, repo, catalog, state, changed, regen, summary, limit, dry_run, today) -> None:
    """Read published CMDE guidance from the Yangtze mirror and download the files."""
    try:
        notices_found = fetch_cmde_notices(session, pages=70)
    except Exception as exc:
        print(f"  FAIL cmde list {exc}")
        summary["failed"] += 1
        return
    checked = 0
    for notice in notices_found:
        if checked >= limit:
            break
        link = notice["link"]
        if link in state["done"] and not dry_run:
            continue
        checked += 1
        summary["checked"] += 1
        listing_title = fulltext.strip_issue_number(re.sub(r"\s+", "", notice["title"]))
        listing_title = listing_title.replace("《", "").replace("》", "")
        if "关于发布" not in listing_title and "关于印发" not in listing_title:
            listed = fulltext.find_page(catalog, listing_title, "", "")
            if listed and listed.get("body_len", 0) >= fulltext.MIN_KEEP:
                print(f"  present: {listing_title[:48]} ({listed['body_len']} chars)")
                summary["present"] += 1
                if not dry_run:
                    state["done"][link] = {"at": today, "outcomes": ["present"]}
                continue
        try:
            resp = session.get(link, timeout=30, headers={"User-Agent": "Mozilla/5.0"})
            resp.raise_for_status()
            resp.encoding = resp.apparent_encoding or "utf-8"
            published, downloads = fulltext.parse_cmde_article(resp.text, link)
        except Exception as exc:
            print(f"  FAIL {link} {exc}")
            summary["failed"] += 1
            continue
        published = published or today
        notice_number = fulltext.issue_number(notice["title"]) or fulltext.document_number(notice["title"])
        outcomes = []
        incomplete = False
        downloaded = 0
        for item in downloads:
            title = fulltext.strip_issue_number(item["title"])
            number = fulltext.issue_number(item["title"]) or notice_number
            existing = fulltext.find_page(catalog, title, "", published)
            needs_file = existing is None or existing.get("body_len", 0) < fulltext.MIN_KEEP
            if needs_file and downloaded >= 80:
                incomplete = True
                continue
            text = ""
            if needs_file:
                try:
                    got = session.get(item["url"], timeout=60, headers={"User-Agent": "Mozilla/5.0", "Referer": link})
                    got.raise_for_status()
                    text = fulltext.bytes_to_text(got.content) if fulltext.looks_like_file(got.content) else ""
                except Exception as exc:
                    print(f"  FAIL {title[:40]} {exc}")
                    summary["failed"] += 1
                    incomplete = True
                    continue
                downloaded += 1
                action = fulltext.plan_document(existing, text)
            else:
                action = "present"
            outcomes.append(action)
            section = existing["section"] if existing else "nmpa/guidance"
            print(f"  {action}: {title[:48]} ({len(text) or existing.get('body_len', 0)} chars)")
            summary[COUNT_KEY[action]] += 1
            if dry_run or action in ("present", "no_fulltext"):
                continue
            if action == "create":
                record = publish_new(
                    repo, catalog, title, section, text, link, item["url"], published, number, prefix="cmde",
                )
                changed[section].add(record["slug"])
                regen.add(section)
            elif action == "replace":
                page = fulltext.render_page(
                    doc_id=existing["doc_id"] or f"nmpa-{existing['slug']}",
                    title=existing["title"],
                    section=existing["section"],
                    doc_number=number or existing.get("doc_number", ""),
                    source_url=link,
                    attachment=item["url"],
                    published=published,
                    body=text,
                )
                existing["path"].write_text(page, encoding="utf-8")
                existing["body_len"] = len(text)
                existing["source_url"] = link
                changed[existing["section"]].add(existing["slug"])
                regen.add(existing["section"])
            elif action == "retarget":
                retarget(existing, link, published)
                changed[existing["section"]].add(existing["slug"])
        if not dry_run and not incomplete and downloads:
            state["done"][link] = {"at": today, "outcomes": outcomes}


def refresh_catalog(repo: Path, changed: dict[str, set[str]], regen: set[str]) -> None:
    for section, slugs in changed.items():
        if not slugs:
            continue
        meta = docs_index.SECTION_MAP[section]
        entries = docs_index.get_doc_entries(repo / section, section)
        picked = [entry for entry in entries if entry["slug"] in slugs]
        docs_index.sync_content_to_docs(section, picked, repo)
        if section in regen:
            docs_index.generate_section_page(section, meta[0], meta[1], entries, repo)


def sync(repo: Path, limit: int, pages: int, dry_run: bool, cmde_limit: int | None = None) -> dict:
    session = requests.Session()
    state_path = repo / "scripts" / ".official_fulltext_state.json"
    state = load_state(state_path)
    catalog = fulltext.load_pages(repo)
    summary = {"checked": 0, "created": 0, "replaced": 0, "retargeted": 0, "present": 0, "no_fulltext": 0, "failed": 0}
    changed: dict[str, set[str]] = {section: set() for section in fulltext.SECTIONS}
    regen: set[str] = set()
    today = datetime.now().strftime("%Y-%m-%d")

    for item in fetch_policy(session, pages):
        if summary["checked"] >= limit:
            break
        link = item["link"]
        if link in state["done"] and not dry_run:
            continue
        summary["checked"] += 1
        try:
            body, attachment = fetch_article(session, link)
        except Exception as exc:
            print(f"  FAIL {link} {exc}")
            summary["failed"] += 1
            continue
        titles = fulltext.document_titles(item["title"])
        chunks = fulltext.split_bodies(body, titles)
        if not chunks:
            label = titles[0] if len(titles) == 1 else item["title"]
            chunks = {label: body}
        if len(chunks) == 1:
            pieces = fulltext.split_attachments(next(iter(chunks.values())))
            if len(pieces) >= 2:
                chunks = {title: text for title, text in pieces}
        number = fulltext.document_number(item["title"])
        published = item.get("pub_date") or today
        outcomes = []
        for title, text in chunks.items():
            existing = fulltext.find_page(catalog, title, text, published)
            action = fulltext.plan_document(existing, text)
            outcomes.append(action)
            section = existing["section"] if existing else fulltext.target_section(title, item.get("category_key", ""))
            print(f"  {action}: {title[:48]} ({len(text)} chars)")
            summary[COUNT_KEY[action]] += 1
            if dry_run or action in ("present", "no_fulltext"):
                continue
            if action == "create":
                record = publish_new(repo, catalog, title, section, text, link, attachment, published, number)
                changed[section].add(record["slug"])
                regen.add(section)
            elif action == "replace":
                page = fulltext.render_page(
                    doc_id=existing["doc_id"] or f"nmpa-{existing['slug']}",
                    title=existing["title"],
                    section=existing["section"],
                    doc_number=number or existing.get("doc_number", ""),
                    source_url=link,
                    attachment=attachment,
                    published=published,
                    body=text,
                )
                existing["path"].write_text(page, encoding="utf-8")
                existing["body_len"] = len(text)
                existing["source_url"] = link
                changed[existing["section"]].add(existing["slug"])
                regen.add(existing["section"])
            elif action == "retarget":
                retarget(existing, link, published)
                changed[existing["section"]].add(existing["slug"])
        if not dry_run:
            state["done"][link] = {"at": today, "outcomes": outcomes}
    sync_cmde(
        session, repo, catalog, state, changed, regen, summary,
        cmde_limit if cmde_limit is not None else limit, dry_run, today,
    )
    if not dry_run:
        refresh_catalog(repo, changed, regen)
        save_state(state_path, state)
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Sync gov.cn full text into the NMPA catalog")
    parser.add_argument("--repo", default=".")
    parser.add_argument("--limit", type=int, default=8)
    parser.add_argument("--cmde-limit", type=int, default=40)
    parser.add_argument("--pages", type=int, default=3)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    repo = Path(args.repo).resolve()
    summary = sync(repo, args.limit, args.pages, args.dry_run, args.cmde_limit)
    print(
        "official full text: checked {checked}, created {created}, replaced {replaced}, "
        "retargeted {retargeted}, already present {present}, no full text {no_fulltext}, failed {failed}".format(**summary)
    )


if __name__ == "__main__":
    main()
