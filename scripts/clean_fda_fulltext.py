#!/usr/bin/env python3
"""Clean FDA guidance fulltext extracted from PDF.

Fixes:
- Remove page markers (<!-- Page N -->) and repeated headers
- Remove Table of Contents
- Remove page numbers embedded in text
- Rejoin paragraphs broken by page boundaries
- Collect footnotes and move to end of document
- Clean up formatting artifacts
"""

import re
import sys
from pathlib import Path

FULLTEXT_DIR = Path(__file__).resolve().parent.parent / "fda" / "guidance" / "fulltext"

REPEATED_HEADERS = [
    "Contains Nonbinding Recommendations",
    "Contains Nonbinding Recommendation",
]


def clean_fulltext(text: str) -> str:
    lines = text.split("\n")

    header_lines = []
    body_start = 0
    for i, line in enumerate(lines):
        if line.startswith("---") and i > 0:
            body_start = i
            break
        header_lines.append(line)

    header = "\n".join(header_lines) + "\n\n---\n"

    body_lines = lines[body_start:]
    body = "\n".join(body_lines)

    body = _remove_page_markers(body)
    body = _remove_repeated_headers(body)
    body = _remove_toc(body)
    body = _remove_preface_and_cover(body)
    body = _remove_stray_page_numbers(body)
    body, footnotes = _extract_footnotes(body)
    body = _rejoin_broken_paragraphs(body)
    body = _fix_broken_list_items(body)
    body = _normalize_section_headings(body)
    body = _collapse_blank_lines(body)

    result = header + "\n" + body.strip()
    if footnotes:
        result += "\n\n---\n\n## Footnotes\n\n" + "\n\n".join(footnotes)
    result += "\n"
    return result


def _remove_toc(text: str) -> str:
    """Remove Table of Contents block."""
    toc_patterns = [
        r"Table of Contents\n(?:.*?\.{4,}.*?\n)+",
        r"Table of Contents\s*\n(?:(?:[IVXLCDM]+\.\s|[A-Z]\.\s|\d+\.\s|Appendix).*?\n)+",
    ]
    for pat in toc_patterns:
        text = re.sub(pat, "", text, flags=re.DOTALL)

    lines = text.split("\n")
    cleaned = []
    skip = False
    for line in lines:
        stripped = line.strip()
        if stripped == "Table of Contents":
            skip = True
            continue
        if skip:
            if re.search(r"\.{3,}\s*\d+\s*$", stripped):
                continue
            if re.match(r"^[IVXLCDM]+\.\s*$", stripped):
                continue
            if re.match(r"^[A-Z]\.\s*$", stripped):
                continue
            if re.match(r"^\d+\.\s*$", stripped):
                continue
            if stripped == "":
                continue
            if re.search(r"\.{3,}", stripped):
                continue
            skip = False
        cleaned.append(line)
    return "\n".join(cleaned)


def _remove_preface_and_cover(text: str) -> str:
    """Remove cover page, preface, and preamble -- everything before the first real section.

    Strategy: find the FDA boilerplate 'This guidance represents...' paragraph,
    then find the first roman numeral section heading after it.
    If boilerplate not found, just look for the first heading.
    """
    boilerplate_markers = [
        r"This guidance represents the current thinking",
        r"This guidance document was issued prior",
    ]

    best_start = None
    for marker in boilerplate_markers:
        m = re.search(marker, text)
        if m:
            best_start = m.start()
            break

    if best_start is not None:
        after_boilerplate = text[best_start:]
        heading_m = re.search(r"\n[IVXLCDM]+\.\s*\n", after_boilerplate)
        if heading_m:
            boilerplate_para_end = after_boilerplate.find("\n\n")
            if boilerplate_para_end > 0:
                boilerplate_text = after_boilerplate[:boilerplate_para_end].strip()
                remaining = after_boilerplate[boilerplate_para_end:]
                heading_in_remaining = re.search(r"\n[IVXLCDM]+\.\s*\n", remaining)
                if heading_in_remaining:
                    section_text = remaining[heading_in_remaining.start():]
                    return "\n" + boilerplate_text + "\n" + section_text
            return "\n" + after_boilerplate

    first_heading = re.search(r"\n[IVXLCDM]+\.\s*\n", text)
    if first_heading:
        return text[first_heading.start():]

    return text


def _remove_page_markers(text: str) -> str:
    text = re.sub(r"<!--\s*Page\s+\d+\s*-->", "", text)
    text = re.sub(r"\n---\n\s*\n+", "\n\n", text)
    return text


def _remove_repeated_headers(text: str) -> str:
    for header in REPEATED_HEADERS:
        text = text.replace(header + "\n", "")
        text = text.replace(header, "")
    return text


def _remove_stray_page_numbers(text: str) -> str:
    """Remove standalone page numbers (single number on its own line)."""
    text = re.sub(r"\n\s*(\d{1,3})\s*\n", lambda m: "\n" if 1 <= int(m.group(1)) <= 200 else m.group(0), text)
    return text


def _rejoin_broken_paragraphs(text: str) -> str:
    """Rejoin lines that were broken by PDF extraction.

    If a line ends with a lowercase letter, comma, or similar continuation
    character and the next non-empty line starts with a lowercase letter,
    they should be joined.
    """
    lines = text.split("\n")
    result = []
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.rstrip()

        if not stripped:
            result.append(line)
            i += 1
            continue

        if stripped.startswith("#") or stripped.startswith("|") or stripped.startswith("- ") or stripped.startswith("* "):
            result.append(line)
            i += 1
            continue

        while i + 1 < len(lines):
            next_line = lines[i + 1].strip()
            if not next_line:
                break
            if next_line.startswith("#") or next_line.startswith("|") or next_line.startswith("- ") or next_line.startswith("* ") or next_line.startswith("```"):
                break

            ends_mid = bool(re.search(r"[a-z,;:\-]$", stripped)) or stripped.endswith("the") or stripped.endswith("a") or stripped.endswith("an")
            starts_lower = bool(re.match(r"^[a-z]", next_line))
            starts_continuation = bool(re.match(r"^(and|or|the|that|which|with|for|to|in|of|on|at|by|as|is|are|was|were|be|been|not|from|their|its|this|these|those|than|including|such|when|where|while|however|therefore|additionally|furthermore|also|but|nor|yet|so)\b", next_line, re.IGNORECASE)) and not next_line[0].isupper()

            if (ends_mid and starts_lower) or (ends_mid and starts_continuation):
                if stripped.endswith("-"):
                    stripped = stripped[:-1] + next_line
                else:
                    stripped = stripped + " " + next_line
                i += 1
            else:
                break

        result.append(stripped)
        i += 1

    return "\n".join(result)


def _extract_footnotes(text: str) -> tuple[str, list[str]]:
    """Extract inline footnotes and collect them at end of document.

    Footnotes in FDA PDFs appear as lines starting with a number followed by
    text like 'See ...', 'For the purposes ...', etc.
    Also catches short inline footnotes like '2 21 CFR 3.2(e).'
    """
    FOOTNOTE_STARTERS = (
        "For the purposes", "For more information", "For example",
        "See ", "See also", "As defined", "Refers to",
        "The term", "Under ", "Per ", "In accordance", "As described",
        "A ", "An ", "This ", "Note", "Id.", "Ibid", "21 CFR", "42 U.S.C",
        "Section ", "Defined ", "NIST ", "FDA ", "Pursuant", "Indicators ",
    )

    footnotes = {}
    lines = text.split("\n")
    cleaned_lines = []
    i = 0

    while i < len(lines):
        stripped = lines[i].strip()
        m = re.match(r"^(\d{1,3})\s+(.+)$", stripped)
        if m:
            fn_num = int(m.group(1))
            fn_text = m.group(2)
            if fn_num < 200 and any(fn_text.startswith(s) for s in FOOTNOTE_STARTERS):
                while i + 1 < len(lines):
                    next_s = lines[i + 1].strip()
                    if not next_s:
                        break
                    if re.match(r"^\d{1,3}\s+", next_s):
                        break
                    if next_s.startswith("#") or next_s.startswith("---"):
                        break
                    if re.match(r"^[IVXLCDM]+\.\s", next_s):
                        break
                    if re.match(r"^[A-Z][a-z]", next_s) and not re.match(r"^[a-z]", next_s):
                        if not fn_text.rstrip().endswith(",") and not fn_text.rstrip().endswith("-"):
                            break
                    fn_text += " " + next_s
                    i += 1
                footnotes[fn_num] = fn_text.strip()
                i += 1
                continue
        cleaned_lines.append(lines[i])
        i += 1

    fn_list = [f"[^{n}]: {t}" for n, t in sorted(footnotes.items())]
    return "\n".join(cleaned_lines), fn_list


def _fix_broken_list_items(text: str) -> str:
    """Fix list items where the bullet is on one line and content on the next."""
    text = re.sub(r"(\xb7|\u00b7)\s*\n\s*([A-Z])", r"- \2", text)
    text = re.sub(r"^(\xb7|\u00b7)\s+", "- ", text, flags=re.MULTILINE)
    return text


def _normalize_section_headings(text: str) -> str:
    """Convert roman numeral section headers to proper markdown headings."""
    text = re.sub(r"\n([IVXLCDM]+)\.\s*\n\s*([A-Z][^\n]+)", r"\n## \1. \2", text)
    text = re.sub(r"\n([A-Z])\.\s*\n\s*([A-Z][^\n]+)", r"\n### \1. \2", text)
    text = re.sub(r"\n(\d+)\.\s*\n\s*([A-Z][^\n]+)", r"\n#### \1. \2", text)
    text = re.sub(r"\n([IVXLCDM]+)\.\s+([A-Z][^\n]+)", r"\n## \1. \2", text)
    return text


def _collapse_blank_lines(text: str) -> str:
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    text = re.sub(r" +\n", "\n", text)
    return text


def main():
    files = sorted(FULLTEXT_DIR.glob("*.md"))
    if not files:
        print("No fulltext files found")
        return

    for fpath in files:
        print(f"Cleaning: {fpath.name}")
        original = fpath.read_text(encoding="utf-8")
        cleaned = clean_fulltext(original)

        orig_lines = len(original.split("\n"))
        clean_lines = len(cleaned.split("\n"))
        print(f"  {orig_lines} -> {clean_lines} lines ({orig_lines - clean_lines} removed)")

        fpath.write_text(cleaned, encoding="utf-8")
        print(f"  Written: {fpath}")

    print("\nDone!")


if __name__ == "__main__":
    main()
