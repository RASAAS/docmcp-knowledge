#!/usr/bin/env python3
"""Clean FDA guidance fulltext extracted from PDF.

Fixes:
- Remove page markers (<!-- Page N -->) and repeated headers
- Remove Table of Contents and cover/preface without dropping body sections
- Remove page numbers embedded in text
- Rejoin paragraphs broken by PDF line wraps / hyphenation
- Collect footnotes and move to end of document
- Normalize roman / letter section headings
- Escape PDF placeholder angle-brackets for VitePress/Vue

Usage:
    python scripts/clean_fda_fulltext.py
    python scripts/clean_fda_fulltext.py --slugs remanufacturing cybersecurity-premarket
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from json_to_markdown import _escape_vue_tags  # noqa: E402

FULLTEXT_DIR = Path(__file__).resolve().parent.parent / "fda" / "guidance" / "fulltext"

REPEATED_HEADERS = [
    "Contains Nonbinding Recommendations",
    "Contains Nonbinding Recommendation",
]

BOILERPLATE_MARKERS = [
    r"This guidance represents the current thinking",
    r"This guidance document was issued prior",
    r"FDA's guidance documents, including this (?:final )?guidance, do not establish",
    r"FDA’s guidance documents, including this (?:final )?guidance, do not establish",
]

_COMPOUND_RIGHT = {
    "related", "connected", "based", "shelf", "market", "approval", "use",
    "label", "cycle", "source", "party", "house", "time", "level", "risk",
    "benefit", "cost", "effective", "making", "only", "free", "specific",
    "looking", "term", "clinical", "device", "software", "hardware",
    "security", "production", "processing", "defined", "oriented",
    "compatible", "sensitive", "resistant", "proof", "safe", "critical",
    "up", "down", "out", "in", "of", "the", "to", "and", "or",
}

_SENTENCE_STARTERS = (
    "The ", "This ", "These ", "Those ", "That ", "A ", "An ", "As ", "For ",
    "In ", "On ", "At ", "To ", "Of ", "If ", "When ", "While ", "Although ",
    "However ", "Therefore ", "Additionally ", "Furthermore ", "Moreover ",
    "FDA ", "Under ", "It ", "Its ", "Such ", "Any ", "All ", "Each ",
    "Manufacturers ", "Sponsors ", "Entities ", "Device ", "Medical ",
    "Section ", "Appendix ", "Figure ", "Table ", "See ", "Note ",
)

_FOOTNOTE_STARTERS = (
    "See ", "See also", "Available at", "For the purposes", "For more information",
    "For additional", "For example,", "For a full", "https://", "http://",
    "21 CFR", "42 U.S.C", "21 U.S.C", "ANSI/", "ISO ", "NIST ", "AAMI ",
    "IEC ", "Id.", "Ibid", "As defined", "As described", "As stated",
    "As noted", "As IDE", "Under section", "Under 21", "Per ",
    "FDA's ", "FDA’s ", "FDA guidance", "FDA has recognized",
    "The HHS", "The term ", "Refers to", "Defined in", "Indicators ",
    "E.g.,", "e.g.,", "i.e.,", "Ransomware.",
)

_TOP_ROMAN = (
    "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X",
    "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX",
)

_H2_TITLES = re.compile(
    r"^(Introduction|Scope|Background|Definitions?|General Principles|"
    r"Using |Medical |Cybersecurity Transparency|Cyber Devices|"
    r"Remediating|Recommended Content|Criteria for|Appendix|"
    r"Regulatory Requirements|Considerations for Labeling|"
    r"Relevant Considerations|Changes Involving|Guiding Principles|"
    r"Maintaining Safety|510\(k\)|FDA Actions|Submitter Actions|"
    r"Q.?submission)\b",
    re.I,
)


def clean_fulltext(text: str) -> str:
    header, body = _split_header_body(text)

    body = _remove_page_markers(body)
    body = _remove_repeated_headers(body)
    notices = _extract_front_notices(body)
    body = _remove_toc(body)
    body = _remove_preface_and_cover(body, notices=notices)
    body = _remove_stray_page_numbers(body)
    body, footnotes = _extract_footnotes(body)
    body = _rejoin_broken_paragraphs(body)
    body = _fix_broken_list_items(body)
    body = _normalize_section_headings(body)
    body = _collapse_blank_lines(body)

    result = header + "\n" + body.strip()
    if footnotes:
        if not re.search(r"^## Footnotes\s*$", result, re.M):
            result += "\n\n---\n\n## Footnotes\n\n" + "\n\n".join(footnotes)
    result += "\n"
    # Escape PDF placeholder angle-brackets so VitePress/Vue does not
    # treat them as HTML tags (e.g. <Insert Month and\nYear>).
    result = _escape_vue_tags(result)
    return result


def _split_header_body(text: str) -> tuple[str, str]:
    lines = text.split("\n")
    header_lines = []
    body_start = 0
    for i, line in enumerate(lines):
        if line.startswith("---") and i > 0:
            body_start = i + 1
            break
        header_lines.append(line)
    header = "\n".join(header_lines) + "\n\n---\n"
    body = "\n".join(lines[body_start:])
    return header, body


def _remove_page_markers(text: str) -> str:
    text = re.sub(r"<!--\s*Page\s+\d+\s*-->", "", text)
    text = re.sub(r"\n---\n\s*\n+", "\n\n", text)
    return text


def _remove_repeated_headers(text: str) -> str:
    for header in REPEATED_HEADERS:
        text = re.sub(re.escape(header) + r"[ \t]*\n?", "\n", text)
        text = text.replace(header, "")
    return text


def _looks_like_toc_line(stripped: str) -> bool:
    if re.search(r"\.{3,}\s*\d+\s*$", stripped):
        return True
    if re.search(r"[.…·]{3,}", stripped):
        return True
    if re.match(r"^[IVXLCDM]+\.\s*$", stripped):
        return True
    if re.match(r"^[A-Z]\.\s*$", stripped):
        return True
    if re.match(r"^\d+(\.\d+)*\.?\s*$", stripped):
        return True
    if re.match(r"^(Appendix|ANNEX)\s+[A-Z0-9]", stripped, re.I) and len(stripped) < 80:
        return True
    if re.search(r"\s+\d{1,3}\s*$", stripped) and len(stripped) < 90:
        return True
    if len(stripped) < 80 and stripped.isupper() and not stripped.startswith("FDA"):
        return True
    return False


def _remove_toc(text: str) -> str:
    lines = text.split("\n")
    cleaned: list[str] = []
    skip = False
    for line in lines:
        stripped = line.strip()
        if re.match(r"^Table of Contents\s*$", stripped, re.I):
            skip = True
            continue
        if skip:
            if re.search(
                r"This guidance represents the current thinking|"
                r"FDA'?s guidance documents, including this",
                stripped,
            ):
                skip = False
                cleaned.append(line)
                continue
            if stripped == "":
                continue
            if _looks_like_toc_line(stripped):
                continue
            skip = False
            cleaned.append(line)
            continue
        cleaned.append(line)
    return "\n".join(cleaned)


def _extract_front_notices(text: str) -> str:
    cover_re = re.compile(
        r"Guidance for Industry|"
        r"Document issued on|"
        r"U\.S\. Department of Health and Human Services|"
        r"^Preface\s*$|"
        r"^Public Comment\s*$|"
        r"^Table of Contents",
        re.M,
    )
    m = cover_re.search(text)
    if not m:
        return ""
    prefix = text[: m.start()]
    keep_lines = []
    for line in prefix.split("\n"):
        s = line.strip()
        if not s:
            keep_lines.append("")
            continue
        if s in REPEATED_HEADERS:
            continue
        if re.fullmatch(r"\d{1,3}", s):
            continue
        keep_lines.append(line)
    notice = _collapse_blank_lines("\n".join(keep_lines)).strip()
    if len(notice) < 80:
        return ""
    return notice


def _remove_preface_and_cover(text: str, notices: str = "") -> str:
    """Drop cover/preface/TOC; keep banner notices + body from FDA boilerplate onward.

    Do not slice to a later standalone roman numeral — that dropped whole
    middle sections (e.g. remanufacturing II–VII) when headings were split
    across lines as ``VIII.\\nTitle``.
    """
    best_start = None
    for marker in BOILERPLATE_MARKERS:
        m = re.search(marker, text)
        if m:
            best_start = m.start()
            break

    if best_start is not None:
        body = text[best_start:]
    else:
        heading = re.search(
            r"(?:^|\n)((?:I\.|1\.)\s*\n?\s*Introduction\b)",
            text,
            re.I,
        )
        body = text[heading.start():] if heading else text

    body = body.strip()
    if notices:
        probe = notices.split("\n", 1)[0][:80].strip()
        if probe and probe not in body:
            return notices.rstrip() + "\n\n" + body
    return body


def _remove_stray_page_numbers(text: str) -> str:
    def _drop(m: re.Match) -> str:
        n = int(m.group(1))
        return "\n" if 1 <= n <= 400 else m.group(0)

    return re.sub(r"\n\s*(\d{1,3})\s*\n", _drop, text)


def _is_structural(line: str) -> bool:
    s = line.strip()
    if not s:
        return False
    if s.startswith("#") or s.startswith("|") or s.startswith("```"):
        return True
    if s.startswith("- ") or s.startswith("* ") or s.startswith("> "):
        return True
    if re.match(r"^\d+\.\s+\S", s):
        return True
    return False


def _is_heading_number(s: str) -> bool:
    s = s.strip()
    return bool(
        re.match(r"^[IVXLCDM]+\.\s*$", s)
        or re.match(r"^[A-Z]\.\s*$", s)
        or re.match(r"^\d+\.\s*$", s)
        or re.match(r"^[A-Z]\d+\.?\s*$", s)
    )


def _looks_like_heading(s: str) -> bool:
    s = s.strip()
    if not s:
        return False
    if s.startswith("#"):
        return True
    if _is_heading_number(s):
        return True
    if re.match(r"^[IVXLCDM]+\.\s+[A-Z0-9(\[]", s):
        return True
    if re.match(r"^[A-Z]\.\s+[A-Z]", s) and len(s) < 220:
        return True
    if re.match(r"^Appendix\s+[A-Z0-9]", s, re.I):
        return True
    return False


def _title_like(s: str) -> bool:
    if not s or s.endswith((".", "?", "!")):
        return False
    if len(s) > 100:
        return False
    s2 = re.sub(r"^[IVXLCDM]+\.\s+", "", s)
    s2 = re.sub(r"^[A-Z]\.\s+", "", s2)
    if ". " in s2:
        return False
    return s[0].isupper() or _is_heading_number(s)


def _sentence_like(s: str) -> bool:
    if not s:
        return False
    if len(s) > 50 and s[0].isupper():
        if s.startswith(_SENTENCE_STARTERS) or re.match(r"^[A-Z][a-z]+ ", s):
            return True
    if s.startswith(_SENTENCE_STARTERS) and len(s) > 35:
        return True
    return False


def _join_hyphen(left: str, right: str) -> str:
    right_first = re.split(r"\s", right, maxsplit=1)[0]
    rest = right[len(right_first):]
    token = re.sub(r"[^A-Za-z].*$", "", right_first)
    left_word = re.sub(r"^.*?([A-Za-z]+)$", r"\1", left)
    if token.lower() in _COMPOUND_RIGHT or len(left_word) <= 3:
        return left + right_first + rest
    return left[:-1] + right_first + rest


def _rejoin_broken_paragraphs(text: str) -> str:
    lines = text.split("\n")
    result: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.rstrip()

        if not stripped:
            result.append(line)
            i += 1
            continue

        if _is_structural(stripped) and not _is_heading_number(stripped.strip()):
            result.append(line)
            i += 1
            continue

        while i + 1 < len(lines):
            next_line = lines[i + 1].strip()
            if not next_line:
                break
            if _is_structural(next_line) and not _is_heading_number(next_line):
                break
            if next_line.startswith("#") or next_line.startswith("|") or next_line.startswith("```"):
                break
            if _looks_like_heading(next_line):
                break

            cur = stripped.strip()

            if _is_heading_number(cur):
                stripped = cur.rstrip() + " " + next_line
                i += 1
                continue

            if _title_like(cur) and _sentence_like(next_line):
                break
            if _looks_like_heading(cur):
                if _sentence_like(next_line) or len(next_line) > 70:
                    break
                if re.search(r"\b(is|are|was|were|must|should|may|can|this|these)\b", next_line, re.I) and len(next_line) > 30:
                    break

            ends_hyphen = cur.endswith("-") or cur.endswith("\u00ad")
            ends_mid = bool(re.search(
                r"[a-z,;:\u00ad]$|"
                r"\b(the|a|an|and|or|of|to|in|on|for|with|by|as|at|from|"
                r"that|which|this|these|those|than|into|onto|upon|over|"
                r"under|its|their|his|her|not|be|been|is|are|was|were|"
                r"may|can|must|should|including|such)\s*$",
                cur,
                re.I,
            ))
            ends_wrap = (
                len(cur) >= 60
                and not re.search(r'[.!?]"?\s*$', cur)
                and not re.search(r"[.!?]\d+\s*$", cur)
            )
            starts_lower = bool(re.match(r"^[a-z]", next_line))
            starts_cont = bool(re.match(
                r"^(and|or|the|that|which|with|for|to|in|of|on|at|by|as|"
                r"is|are|was|were|be|been|not|from|their|its|this|these|"
                r"those|than|including|such|when|where|while|however|"
                r"therefore|additionally|furthermore|also|but|nor|yet|so)\b",
                next_line,
            ))

            if ends_hyphen and (starts_lower or starts_cont or next_line[:1].islower()):
                stripped = _join_hyphen(cur, next_line)
                i += 1
                continue

            if ends_mid and not _sentence_like(next_line) and not _is_heading_number(next_line):
                stripped = cur + " " + next_line
                i += 1
                continue

            if ends_wrap and (
                starts_lower or starts_cont or next_line[:1].islower()
                or (next_line[0].isupper() and not _sentence_like(next_line) and len(next_line) < 80)
            ):
                stripped = cur + " " + next_line
                i += 1
                continue

            if (
                ends_wrap
                and next_line[0].isupper()
                and not _sentence_like(next_line)
                and not _is_heading_number(next_line)
            ):
                stripped = cur + " " + next_line
                i += 1
                continue

            break

        result.append(stripped)
        i += 1

    return "\n".join(result)


def _extract_footnotes(text: str) -> tuple[str, list[str]]:
    footnotes: dict[int, str] = {}
    lines = text.split("\n")
    cleaned: list[str] = []
    i = 0

    while i < len(lines):
        stripped = lines[i].strip()
        m = re.match(r"^(\d{1,3})\s+(.+)$", stripped)
        if m:
            fn_num = int(m.group(1))
            fn_text = m.group(2)
            if fn_num < 200 and any(fn_text.startswith(s) for s in _FOOTNOTE_STARTERS):
                while i + 1 < len(lines):
                    next_s = lines[i + 1].strip()
                    if not next_s:
                        break
                    if re.match(r"^\d{1,3}\s+", next_s):
                        break
                    if next_s.startswith("#") or next_s.startswith("---"):
                        break
                    if _looks_like_heading(next_s):
                        break
                    if re.match(r"^[A-Z][a-z]", next_s) and not re.match(r"^[a-z]", next_s):
                        if not fn_text.rstrip().endswith((",", "-", "/")):
                            if not fn_text.rstrip().endswith(("http://", "https://", ".gov/", ".pdf")):
                                break
                    fn_text += " " + next_s
                    i += 1
                footnotes[fn_num] = fn_text.strip()
                i += 1
                continue
        cleaned.append(lines[i])
        i += 1

    fn_list = [f"[^{n}]: {t}" for n, t in sorted(footnotes.items())]
    return "\n".join(cleaned), fn_list


def _fix_broken_list_items(text: str) -> str:
    text = re.sub(r"(\xb7|\u00b7)\s*\n\s*([A-Z])", r"- \2", text)
    text = re.sub(r"^(\xb7|\u00b7)\s+", "- ", text, flags=re.MULTILINE)
    return text


def _normalize_section_headings(text: str) -> str:
    def roman_heading(m: re.Match) -> str:
        num, title = m.group(1), m.group(2).strip()
        title = re.sub(r"\s+", " ", title)
        if num in ("I", "V", "X") and not _H2_TITLES.match(title):
            return f"\n### {num}. {title}"
        return f"\n## {num}. {title}"

    def letter_heading(m: re.Match) -> str:
        let, title = m.group(1), m.group(2).strip()
        title = re.sub(r"\s+", " ", title)
        if let in ("I", "V", "X") and _H2_TITLES.match(title):
            return f"\n## {let}. {title}"
        return f"\n### {let}. {title}"

    def appendix_heading(m: re.Match) -> str:
        ident, title = m.group(1), re.sub(r"\s+", " ", m.group(2).strip())
        if _sentence_like(title) or len(title) > 90:
            return m.group(0)
        return f"\n## Appendix {ident}. {title}"

    roman_alt = "|".join(sorted(_TOP_ROMAN, key=len, reverse=True))
    text = re.sub(
        rf"\n({roman_alt})\.\s*\n\s*([A-Z0-9(\[][^\n]+)",
        roman_heading,
        text,
    )
    text = re.sub(
        rf"\n({roman_alt})\.\s+([A-Z0-9(\[][^\n]+)",
        roman_heading,
        text,
    )
    text = re.sub(
        r"\n([A-Z])\.\s*\n\s*([A-Z][^\n]+)",
        letter_heading,
        text,
    )
    text = re.sub(
        r"\n([A-Z])\.\s+([A-Z][^\n]{3,220})$",
        letter_heading,
        text,
        flags=re.M,
    )
    text = re.sub(
        r"\n(\d+)\.\s*\n\s*([A-Z][^\n]+)",
        lambda m: f"\n#### {m.group(1)}. {re.sub(r'\s+', ' ', m.group(2).strip())}",
        text,
    )
    text = re.sub(
        r"\nAppendix\s+([A-Z0-9])\.\s*\n\s*([A-Z][^\n]+)",
        appendix_heading,
        text,
        flags=re.I,
    )
    text = re.sub(
        r"\nAppendix\s+([A-Z0-9])\.\s+([A-Z][^\n]+)",
        appendix_heading,
        text,
        flags=re.I,
    )
    return text


def _collapse_blank_lines(text: str) -> str:
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    text = re.sub(r" +\n", "\n", text)
    return text


def iter_fulltext_files(slugs: list[str] | None = None) -> list[Path]:
    files = sorted(
        p for p in FULLTEXT_DIR.glob("*.md")
        if not p.name.endswith(".zh.md")
    )
    if slugs:
        wanted = set(slugs)
        files = [p for p in files if p.stem in wanted]
    return files


def main() -> None:
    parser = argparse.ArgumentParser(description="Clean FDA guidance PDF fulltext")
    parser.add_argument("--slugs", nargs="*", help="Limit to these slugs")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    files = iter_fulltext_files(args.slugs)
    if not files:
        print("No fulltext files found")
        return

    for fpath in files:
        original = fpath.read_text(encoding="utf-8")
        cleaned = clean_fulltext(original)
        orig_lines = len(original.split("\n"))
        clean_lines = len(cleaned.split("\n"))
        delta = orig_lines - clean_lines
        action = "DRY" if args.dry_run else "Cleaning"
        print(f"{action}: {fpath.name}  {orig_lines} -> {clean_lines} lines ({delta:+d})")
        if not args.dry_run:
            fpath.write_text(cleaned, encoding="utf-8")

    print("\nDone!")


if __name__ == "__main__":
    main()
