#!/usr/bin/env python3
"""Fetch overview/description content from ISO and IEC standard pages.

Uses html2text to convert HTML to markdown, then extracts relevant sections.
"""

import json
import re
import time
from pathlib import Path

import requests
import html2text

ROOT = Path(__file__).resolve().parent.parent
INDEX_PATH = ROOT / "_shared" / "iso_iec" / "_index.json"
FULLTEXT_DIR = ROOT / "_shared" / "iso_iec" / "fulltext"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}


def fetch_and_convert(url: str) -> str:
    resp = requests.get(url, headers=HEADERS, timeout=30)
    resp.raise_for_status()
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.body_width = 0
    return h.handle(resp.text)


def extract_iso_content(md: str, title: str, url: str) -> str:
    sections = []

    for pat in [r'#+\s*What is [^\n]+\n(.*?)(?=\n#+\s)', r'### What is [^\n]+\n(.*?)(?=\n##)']:
        m = re.search(pat, md, re.DOTALL)
        if m:
            text = _clean(m.group(1))
            if text:
                sections.append(f"## Overview\n\n{text}")
            break

    for pat in [r'#+\s*Why is [^\n]+\n(.*?)(?=\n#+\s)', r'### Why is [^\n]+\n(.*?)(?=\n##)']:
        m = re.search(pat, md, re.DOTALL)
        if m:
            text = _clean(m.group(1))
            if text:
                sections.append(f"## Importance\n\n{text}")
            break

    m = re.search(r'#+\s*Benefits[^\n]*\n(.*?)(?=\n#+\s*(?:FAQ|Buy|General))', md, re.DOTALL)
    if m:
        text = _clean(m.group(1))
        if text:
            sections.append(f"## Benefits\n\n{text}")

    m = re.search(r'#+\s*FAQ\s*\n(.*?)(?=\n#+\s*(?:Buy|General))', md, re.DOTALL)
    if m:
        text = _clean(m.group(1))
        if text:
            sections.append(f"## FAQ\n\n{text}")

    m = re.search(r'#+\s*General information\s*\n(.*?)(?=\n#+\s*Life cycle)', md, re.DOTALL)
    if m:
        text = _extract_general_info(m.group(1))
        if text:
            sections.append(f"## General Information\n\n{text}")

    return "\n\n".join(sections)


def extract_iec_content(md: str, title: str, url: str) -> str:
    sections = []

    desc_match = re.search(
        r'(?:IEC \d[^\n]*?(?:Defines|Applies|Specifies|This)[^\n]+(?:\n[^\n#]+)*)',
        md, re.DOTALL,
    )
    if desc_match:
        text = desc_match.group(0).strip()
        first_sentence_end = re.search(r'\. (?=[A-Z])', text)
        if first_sentence_end and len(text[:first_sentence_end.end()]) < 50:
            pass
        text = _clean(text)
        if text and len(text) > 100:
            sections.append(f"## Description\n\n{text}")

    m = re.search(r'Technical committee\s*\n\s*(.*?)(?=\n#+|\nKeywords)', md, re.DOTALL)
    if m:
        tc = m.group(1).strip()
        if tc:
            sections.append(f"**Technical Committee:** {tc}")

    m = re.search(r'Keywords\s*\n\s*(.*?)(?=\n#+|\n\|)', md, re.DOTALL)
    if m:
        kw = m.group(1).strip()
        if kw:
            sections.append(f"**Keywords:** {kw}")

    m = re.search(r'\| Publication type \| ([^\|]+) \|', md)
    if m:
        pub_type = m.group(1).strip()
        pub_info = [f"- **Publication type:** {pub_type}"]

        for field, label in [("Publication date", "Publication date"),
                             ("Edition", "Edition"), ("Pages", "Pages")]:
            fm = re.search(rf'\| {field} \| ([^\|]+) \|', md)
            if fm:
                pub_info.append(f"- **{label}:** {fm.group(1).strip()}")
        sections.append("## General Information\n\n" + "\n".join(pub_info))

    return "\n\n".join(sections)


def _clean(text: str) -> str:
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r'(?i)buy together.*', '', text, flags=re.DOTALL)
    text = re.sub(r'CHF \d+.*', '', text)
    text = re.sub(r'English \| PDF.*', '', text)
    text = re.sub(r'\*\*Read sample\*\*.*', '', text, flags=re.DOTALL)
    text = text.strip()
    return text


def _extract_general_info(text: str) -> str:
    info = {}
    for field in ['Status', 'Publication date', 'Edition', 'Number of pages']:
        m = re.search(rf'{field}\s*\n\s*:\s*(.*?)(?=\n[A-Z]|\Z)', text, re.DOTALL)
        if m:
            val = m.group(1).strip()
            if val:
                info[field] = val
    if not info:
        return ""
    return "\n".join(f"- **{k}:** {v}" for k, v in info.items())


def process_standard(entry: dict) -> bool:
    entry_id = entry["id"]
    title = entry["title"]["en"]
    source_url = entry["source_url"]
    safe_id = re.sub(r'[^\w\-.]', '_', entry_id)
    output_path = FULLTEXT_DIR / f"{safe_id}.md"

    print(f"  Fetching: {title}")

    try:
        md = fetch_and_convert(source_url)
    except Exception as e:
        print(f"    ERROR: {e}")
        return False

    if "iso.org" in source_url:
        content = extract_iso_content(md, title, source_url)
    elif "iec.ch" in source_url:
        content = extract_iec_content(md, title, source_url)
    else:
        print(f"    SKIP: unknown domain")
        return False

    if not content or len(content) < 100:
        print(f"    WARNING: insufficient content ({len(content)} chars)")
        return False

    result = f"# {title}\n\n"
    result += f"**Source:** [{source_url}]({source_url})\n\n---\n\n"
    result += content + "\n"

    output_path.write_text(result, encoding="utf-8")
    print(f"    OK: {output_path.name} ({len(content)} chars)")
    return True


def main():
    FULLTEXT_DIR.mkdir(parents=True, exist_ok=True)
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        index = json.load(f)

    entries = index.get("entries", [])
    print(f"Processing {len(entries)} standards...\n")

    success = 0
    for entry in entries:
        if process_standard(entry):
            success += 1
        time.sleep(2)

    print(f"\nDone: {success}/{len(entries)} standards")


if __name__ == "__main__":
    main()
