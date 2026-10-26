"""EU catalog updates: legal-act full text, MDCG guidance, harmonised-standards list.

Harmonised standard documents (ISO, IEC, EN bodies) are never downloaded.
The Official Journal list and the amendment explanation are updated instead.
"""

from __future__ import annotations

import re
from urllib.parse import urlparse

FULLTEXT_MARKER = "<!-- fulltext-start -->"

_STANDARD_HOSTS = (
    "iso.org",
    "iec.ch",
    "bsigroup.",
    "cen.eu",
    "cenelec.",
    "beuth.de",
    "evs.ee",
    "standards.iteh.ai",
    "ihs.com",
)

_CELEX_RE = re.compile(
    r"(?:CELEX:|celex/)([0-3]\d{4}[A-Z]\d{3,5})",
    re.IGNORECASE,
)
_ELI_RE = re.compile(
    r"eli/(reg_del|reg_impl|dec_impl|dec_del|dir_impl|dir_del|reg|dec|dir)/(\d{4})/(\d+)",
    re.IGNORECASE,
)
_STD_RE = re.compile(r"^EN\s+(?:ISO|IEC|\d)", re.IGNORECASE)
_NOTE_RE = re.compile(
    r"restriction|does not|presumption|only the|except |not cover",
    re.IGNORECASE,
)

CATEGORY_RULES = [
    (r"13485", "quality_management"),
    (r"14971|24971", "risk_management"),
    (r"10993|Biological evaluation", "biocompatibility"),
    (r"60601|62353", "electrical_safety"),
    (r"11135|11137|11607|11737|13408|14160|17665|25424|556-|285:|18562|Steriliz|steriliz", "sterilization"),
    (r"62304|62366|82304", "software"),
    (r"15223|20417", "labelling"),
    (r"14155", "clinical_investigation"),
    (r"455-", "medical_gloves"),
    (r"13795|14683", "surgical_textiles"),
    (r"14630|21535|21536", "surgical_implants"),
    (r"1865-", "patient_handling"),
    (r"80369", "connectors"),
    (r"17664", "processing"),
]


def is_standard_body_url(url: str) -> bool:
    """True when the URL points at a copyrighted standard, not an official legal text."""
    if not url:
        return False
    host = urlparse(url).netloc.lower()
    if any(piece in host for piece in _STANDARD_HOSTS):
        return True
    path = urlparse(url).path.lower()
    return bool(re.search(r"(?:iso|iec)[-_]?\d{3,}", path) and host not in (
        "health.ec.europa.eu",
        "ec.europa.eu",
        "eur-lex.europa.eu",
        "publications.europa.eu",
    ))


def is_harmonised_standards_act(title: str, celex: str = "") -> bool:
    """Implementing decisions that only publish the standards list."""
    token = (celex or "").upper()
    if token in {"32021D1182", "32021D1195"} or token.startswith("02021D1182") or token.startswith("02021D1195"):
        return True
    return bool(re.search(r"harmonised standards", title or "", re.IGNORECASE))


def normalize_standard_number(value: str) -> str:
    text = (value or "").replace("\xa0", " ").replace("\u2011", "-")
    text = re.sub(r"\s+", " ", text).strip()
    text = text.split(" + ")[0].strip()
    return text.upper()


def classify_standard(number: str, title: str) -> str:
    haystack = f"{number} {title}"
    for pattern, category in CATEGORY_RULES:
        if re.search(pattern, haystack, re.IGNORECASE):
            return category
    return "general"


def parse_consolidated_annex(html: str) -> list[dict]:
    """Read the current OJ annex. A later row for the same standard replaces the earlier one."""
    try:
        from bs4 import BeautifulSoup
    except ImportError as exc:
        raise RuntimeError("beautifulsoup4 is required") from exc

    soup = BeautifulSoup(html, "html.parser")
    annex = soup.find(id="anx_1")
    table = annex.find("table") if annex else None
    if table is None:
        return []

    order: list[str] = []
    by_key: dict[str, dict] = {}
    for row in table.find_all("tr"):
        cells = row.find_all("td")
        if len(cells) < 2:
            continue
        lines = []
        for para in cells[-1].find_all("p"):
            text = re.sub(r"\s+", " ", para.get_text(" ", strip=True).replace("\xa0", " ")).strip()
            if text:
                lines.append(text)
        if not lines or not _STD_RE.match(lines[0]):
            continue
        number = lines[0]
        amendments = []
        title_parts = []
        notes = []
        for line in lines[1:]:
            if _STD_RE.match(line):
                amendments.append(line)
            elif _NOTE_RE.search(line):
                notes.append(line)
            else:
                title_parts.append(line)
        key = normalize_standard_number(number)
        if key not in by_key:
            order.append(key)
        by_key[key] = {
            "number": number,
            "title": " ".join(title_parts),
            "amendments": amendments,
            "note": " ".join(notes),
        }
    return [by_key[key] for key in order]


def latest_amendment_celex(html: str) -> str:
    """Last amending act linked from the consolidated text, ignoring the base decision."""
    found = re.findall(r"celex/(3\d{4}D\d+)", html, re.IGNORECASE)
    amending = [item.upper() for item in found if item.upper() not in {"32021D1182", "32021D1195"}]
    return amending[-1] if amending else ""


def celex_to_decision_number(celex: str) -> str:
    match = re.match(r"3(\d{4})D0*(\d+)$", (celex or "").upper())
    if not match:
        return ""
    return f"{match.group(1)}/{int(match.group(2))}"


def decision_explanation(html: str) -> str:
    """Recitals and articles of an OJ decision. The annex list is not repeated here."""
    try:
        from bs4 import BeautifulSoup
    except ImportError as exc:
        raise RuntimeError("beautifulsoup4 is required") from exc

    soup = BeautifulSoup(html, "html.parser")
    chunks = []
    for para in soup.find_all("p"):
        if para.find_parent(id="anx_1"):
            break
        classes = " ".join(para.get("class") or [])
        if "title-annex" in classes:
            break
        if not any(token in classes for token in ("title-doc", "oj-normal", "norm", "title-article")):
            continue
        text = re.sub(r"\s+", " ", para.get_text(" ", strip=True)).strip()
        if not text or text in {"Whereas:", "HAS ADOPTED THIS DECISION:"}:
            if text == "Whereas:":
                chunks.append("## Whereas")
            continue
        if "title-article" in classes or "title-doc-first" in classes:
            chunks.append(f"## {text}")
        else:
            chunks.append(text)
    return "\n\n".join(chunks).strip()


def act_heading(html: str) -> str:
    """Official act title. The HTML <title> is often only the OJ filename."""
    try:
        from bs4 import BeautifulSoup
    except ImportError as exc:
        raise RuntimeError("beautifulsoup4 is required") from exc

    soup = BeautifulSoup(html, "html.parser")
    parts = []
    for class_name in ("title-doc-first", "title-doc-last", "oj-doc-ti"):
        for node in soup.find_all("p", class_=class_name):
            text = re.sub(r"\s+", " ", node.get_text(" ", strip=True)).strip()
            if not text or ".xml" in text or ".fmx" in text or text in parts:
                continue
            if re.match(r"^of \d", text, re.I) or text.startswith("(Text with EEA"):
                continue
            parts.append(text)
    return " ".join(parts)


def legal_act_markdown(html: str) -> str:
    """Paragraphs of a regulation or directive, including its annexes."""
    try:
        from bs4 import BeautifulSoup
    except ImportError as exc:
        raise RuntimeError("beautifulsoup4 is required") from exc

    soup = BeautifulSoup(html, "html.parser")
    chunks = []
    for para in soup.find_all("p"):
        classes = " ".join(para.get("class") or [])
        if not any(token in classes for token in (
            "title-doc", "oj-normal", "norm", "title-article", "title-annex", "oj-ti",
        )):
            continue
        text = re.sub(r"\s+", " ", para.get_text(" ", strip=True)).strip()
        if not text:
            continue
        if "title-article" in classes or "title-annex" in classes or "title-doc-first" in classes:
            chunks.append(f"## {text}")
        else:
            chunks.append(text)
    return "\n\n".join(chunks).strip()


def celex_numbers_in(html: str) -> list[str]:
    found = []
    seen = set()
    for match in _CELEX_RE.finditer(html or ""):
        token = match.group(1).upper()
        if token not in seen:
            seen.add(token)
            found.append(token)
    for match in _ELI_RE.finditer(html or ""):
        token = eli_to_celex(match.group(1), match.group(2), match.group(3))
        if token and token not in seen:
            seen.add(token)
            found.append(token)
    return found


def eli_to_celex(kind: str, year: str, number: str) -> str:
    kind = kind.lower()
    sector = "R" if kind.startswith("reg") else "D" if kind.startswith("dec") else "L" if kind.startswith("dir") else ""
    if not sector:
        return ""
    return f"3{year}{sector}{int(number):04d}"


def reflow_pdf_text(text: str) -> str:
    """Turn PDF line wraps into paragraphs separated by a blank line."""
    blocks = []
    paragraph = []
    for raw in (text or "").replace("\f", "\n").splitlines():
        line = raw.strip()
        if not line:
            if paragraph:
                blocks.append(" ".join(paragraph))
                paragraph = []
            continue
        if re.match(r"^\d+(?:\.\d+)*\s+\S", line) or (line.isupper() and 8 < len(line) < 90):
            if paragraph:
                blocks.append(" ".join(paragraph))
                paragraph = []
            blocks.append(line)
            continue
        paragraph.append(line)
    if paragraph:
        blocks.append(" ".join(paragraph))
    return "\n\n".join(blocks).strip()


def embed_fulltext(page: str, body: str, heading: str = "官方全文") -> str:
    block = f"{FULLTEXT_MARKER}\n\n## {heading}\n\n{body.strip()}\n"
    if FULLTEXT_MARKER in page:
        return page[:page.find(FULLTEXT_MARKER)] + block
    return page.rstrip() + "\n\n" + block


def page_already_has_fulltext(page: str) -> bool:
    if FULLTEXT_MARKER not in page:
        return False
    tail = page.split(FULLTEXT_MARKER, 1)[1]
    plain = re.sub(r"\[[^\]]*\]\([^)]+\)", "", tail)
    return len(plain.strip()) > 800


def retarget_link(markdown: str, source_url: str, site_path: str) -> str:
    if not source_url or source_url not in markdown:
        return markdown
    return markdown.replace(f"]({source_url})", f"]({site_path})")


def merge_harmonised_entries(existing: list[dict], oj_rows: list[dict], source_url: str, verified: str) -> dict:
    """Update list fields. Keep Chinese titles, GSPR notes, and abstracts already in the catalog."""
    index = {}
    for entry in existing:
        key = normalize_standard_number(str(entry.get("number") or ""))
        if key:
            index[key] = entry

    added = []
    updated = []
    for row in oj_rows:
        key = normalize_standard_number(row["number"])
        current = index.get(key)
        if current is None:
            title = row.get("title") or ""
            category = classify_standard(row["number"], title)
            slug = re.sub(r"[^a-z0-9]+", "-", key.lower()).strip("-")
            current = {
                "id": f"eu_mdr-hs-{slug}",
                "number": row["number"],
                "title": {"en": title, "zh": ""},
                "status": "active",
                "source_url": source_url,
                "source_verified": verified,
                "category": category,
                "standard_type": "harmonised",
                "harmonized": True,
            }
            if row.get("amendments"):
                current["amendments"] = list(row["amendments"])
            if row.get("note"):
                current["oj_note"] = row["note"]
            existing.append(current)
            index[key] = current
            added.append(row["number"])
            continue
        changed = False
        amendments = list(row.get("amendments") or [])
        if amendments and list(current.get("amendments") or []) != amendments:
            current["amendments"] = amendments
            changed = True
        if row.get("note") and current.get("oj_note") != row["note"]:
            current["oj_note"] = row["note"]
            changed = True
        title = current.get("title")
        if isinstance(title, dict) and not (title.get("en") or "").strip() and row.get("title"):
            title["en"] = row["title"]
            changed = True
        elif not title and row.get("title"):
            current["title"] = {"en": row["title"], "zh": ""}
            changed = True
        if changed:
            current["source_verified"] = verified
            updated.append(row["number"])

    oj_keys = {normalize_standard_number(row["number"]) for row in oj_rows}
    withdrawn = []
    if len(oj_rows) >= 40:
        for entry in existing:
            if entry.get("category") == "software":
                continue
            if entry.get("standard_type") != "harmonised" and not entry.get("harmonized"):
                continue
            key = normalize_standard_number(str(entry.get("number") or ""))
            if key and key not in oj_keys and entry.get("status") != "withdrawn":
                entry["status"] = "withdrawn"
                withdrawn.append(entry.get("number"))
    return {"added": added, "updated": updated, "withdrawn": withdrawn}
