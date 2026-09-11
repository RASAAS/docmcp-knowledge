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
    "FDA ", "Under ", "It ", "We ", "Our ", "Its ", "Such ", "Any ", "All ", "Each ",
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
    r"^(Introduction|Scope|Background|Definitions?|Terminology|Purpose|"
    r"General Principles|Using |Medical |Cybersecurity Transparency|Cyber Devices|"
    r"Remediating|Recommended Content|Criteria for|Appendix|"
    r"Regulatory Requirements|Considerations for Labeling|"
    r"Relevant Considerations|Changes Involving|Guiding Principles|"
    r"Maintaining Safety|510\(k\)|FDA Actions|Submitter Actions|"
    r"Q.?submission|How to Use|Documentation Level|Policy for|"
    r"Description of Modifications|Modification Protocol|Impact Assessment|"
    r"Refuse to Accept|The Checklist|The Checklists|Paperwork Reduction|"
    r"Additional Information)\b",
    re.I,
)

# Named section titles (PDF often omits I./A. markers; bold title alone).
_NAMED_H2 = [
    "Introduction",
    "Scope",
    "Background",
    "Terminology",
    "Definitions",
    "Purpose",
    "Relevant Consensus Standards and Guidance Documents",
    "Addressing Hazards for Medical Devices in the MR Environment",
    "Extent of Image Artifact",
    "Reporting Results",
    "MRI Safety Labeling",
]

_NAMED_H3 = [
    "Consensus Standards",
    "Guidance Documents",
    "Magnetically Induced Displacement Force",
    "Magnetically Induced Torque",
    "Heating",
    "Gradient Induced Vibration",
    "Gradient Induced Extrinsic Electrical Potential (Unintended Stimulation)",
    "Rectification of RF pulses from MR Exams (Unintended Stimulation)",
    "Medical Device Malfunction",
    "MR Safe",
    "MR Unsafe",
    "MR Conditional",
    "Safety in MRI Not Evaluated",
    "What is a significant change to device performance or safety specifications?",
    "Determining whether activities are “remanufacturing”",
    'Determining whether activities are "remanufacturing"',
    "Establishment Registration and Medical Device Listing",
    "Marketing Authorization",
    "Medical Device Reporting and Electronic Product Reports",
    "Reports of Corrections and Removals and Notifications of Defects",
    "Quality System",
    "Labeling",
    "Documentation Level Evaluation",
    "Software Description",
    "Risk Management File",
    "Software Requirements Specification (SRS)",
    "System and Software Architecture Diagram",
    "Software Design Specification (SDS)",
    "Software Development, Configuration Management, and Maintenance Practices",
    "Software Testing as part of Verification and Validation",
    "Software Version History",
    "Unresolved Software Anomalies",
    "Contraindications",
    "Warnings",
    "Precautions",
]

_ROMAN_VAL = {r: i for i, r in enumerate(_TOP_ROMAN, start=1)}


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
    body = _fix_false_atx_headings(body)
    body = _fix_broken_list_items(body)
    body = _normalize_section_headings(body)
    body = _promote_named_and_appendix_headings(body)
    body = _rejoin_truncated_flowchart_headings(body)
    body = _promote_numbered_subheadings(body)
    body = _rejoin_truncated_flowchart_headings(body)
    body = _repair_roman_heading_levels(body)
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
    words = s.split()
    # Title Case / heading-like phrases are not sentences.
    if len(words) >= 2 and not s.endswith((".", "?", "!")):
        cap = sum(1 for w in words if w[:1].isupper() or not w[:1].isalpha())
        if cap / len(words) >= 0.55:
            return False
    if len(s) > 40 and s[0].isupper():
        if s.startswith(_SENTENCE_STARTERS) or re.match(r"^[A-Z][a-z]+ ", s):
            return True
    if s.startswith(_SENTENCE_STARTERS) and len(s) > 30:
        return True
    if re.match(r"^(We|Our|You|Your|Please|Replace|Throughout)\b", s):
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
        # Provisional: multi-char romans are H2; ambiguous I/V/X demoted unless
        # clearly a top-level title. _repair_roman_heading_levels finalizes.
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
        if _sentence_like(title) or len(title) > 120:
            return m.group(0)
        sep = ". " if not title.startswith((":",)) else " "
        if title.startswith(":"):
            title = title.lstrip(": ").strip()
            return f"\n## Appendix {ident}: {title}"
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
    # Only promote numbered headings when the number is alone on its line
    # (PDF wrap). Do NOT promote "1. List item..." prose/checklist lines.
    text = re.sub(
        r"\n(\d+)\.\s*\n\s*([A-Z][^\n]+)",
        lambda m: (
            f"\n#### {m.group(1)}. {re.sub(r'\s+', ' ', m.group(2).strip())}"
            if not _sentence_like(m.group(2)) and len(m.group(2).split()) <= 14
            else m.group(0)
        ),
        text,
    )
    text = re.sub(
        r"\nAppendix\s+([A-Z0-9]+)\.\s*\n\s*([A-Z][^\n]+)",
        appendix_heading,
        text,
        flags=re.I,
    )
    text = re.sub(
        r"\nAppendix\s+([A-Z0-9]+)[.:]\s+([A-Z][^\n]+)",
        appendix_heading,
        text,
        flags=re.I,
    )
    return text


def _fix_false_atx_headings(text: str) -> str:
    """Rejoin PDF wraps that left a literal '#' starting a line (e.g. RFD #)."""
    lines = text.split("\n")
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        # False H1/H2: "# and confirm..." or "# " + lowercase continuation
        if re.match(r"^#+\s+(and|[a-z])", line) and not re.match(r"^#+\s+[A-Z][A-Za-z].{8,}", line):
            if out and out[-1].strip():
                # Preserve a literal '#' (e.g. "RFD # and confirm...").
                out[-1] = out[-1].rstrip() + " " + line.lstrip()
                i += 1
                continue
        # "identify the RFD" then "# and confirm"
        if re.match(r"^#\s+", line) and out and re.search(r"(RFD|No\.|number|ID)\s*$", out[-1], re.I):
            out[-1] = out[-1].rstrip() + " " + line.lstrip()
            i += 1
            continue
        out.append(line)
        i += 1
    return "\n".join(out)


def _rejoin_truncated_flowchart_headings(text: str) -> str:
    """Rejoin flowchart headings split after a trailing slash or mid-word."""
    lines = text.split("\n")
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if (
            re.match(r"^#{0,5}\s*A\d+", line)
            and not line.rstrip().endswith(("?", ".", ":"))
            and i + 1 < len(lines)
        ):
            nxt = lines[i + 1].strip()
            if nxt and not nxt.startswith("#") and (
                nxt[0].islower()
                or nxt.startswith(("material", "ns ", "tions", "specifications", "indirectly"))
            ):
                line = line.rstrip() + " " + nxt
                i += 1
        out.append(line)
        i += 1
    return "\n".join(out)


def _promote_named_and_appendix_headings(text: str) -> str:
    """Promote known bare section titles and Appendix lines to markdown headings."""
    for title in _NAMED_H2 + _NAMED_H3:
        # Split when glued after a closing quote (not after "I." periods).
        text = re.sub(
            rf'([\u201d\u2019"\'])\s+({re.escape(title)})\b',
            r"\1\n\n\2",
            text,
        )

    def promote(level: int, titles: list[str], body: str) -> str:
        hashes = "#" * level
        for title in sorted(titles, key=len, reverse=True):
            pat = re.compile(rf"(?m)^(?!#{{1,6}}\s)({re.escape(title)})\s*$")
            body = pat.sub(lambda m, h=hashes: f"{h} {m.group(1)}", body)
        return body

    text = promote(2, _NAMED_H2, text)
    text = promote(3, _NAMED_H3, text)

    # Bare Appendix lines not already headings (dot or colon form).
    def appendix_line(m: re.Match) -> str:
        ident = m.group(1)
        title = re.sub(r"\s+", " ", m.group(2).strip())
        if len(title) > 120 or _sentence_like(title):
            return m.group(0)
        sep = ":" if m.group(0).find(":") != -1 and f"Appendix {ident}." not in m.group(0) else "."
        # Prefer original separator style from match text
        if re.search(rf"Appendix\s+{re.escape(ident)}\s*:", m.group(0), re.I):
            return f"\n## Appendix {ident}: {title}"
        return f"\n## Appendix {ident}. {title}"

    text = re.sub(
        r"(?m)^(?!#{1,6}\s)Appendix\s+([A-Z0-9]+)[.:]\s+([A-Z][^\n]+)$",
        appendix_line,
        text,
    )
    return text


def _promote_numbered_subheadings(text: str) -> str:
    """Promote flowchart A1/A2 and parenthetical (1)/(2) subheads."""

    def a_step(m: re.Match) -> str:
        code, title = m.group(1), re.sub(r"\s+", " ", m.group(2).strip())
        # Require question / decision-node style; skip narrative mentions.
        if not (
            "?" in title
            or re.match(r"^(Add|Is |Is there|Remove|Change)\b", title)
        ):
            return m.group(0)
        if len(title.split()) > 22:
            return m.group(0)
        level = "#####" if "." in code else "####"
        return f"\n{level} {code}. {title}"

    text = re.sub(
        r"(?m)^(?!#{1,6}\s)(A\d+(?:\.\d+)?)\.?\s+([A-Z?][^\n]{3,160})$",
        a_step,
        text,
    )
    # Parenthetical numbered subheads: (1) Basic Documentation Level
    text = re.sub(
        r"(?m)^(?!#{1,6}\s)\((\d+)\)\s+([A-Z][^\n]{3,80})$",
        lambda m: (
            f"\n#### ({m.group(1)}) {re.sub(r'\s+', ' ', m.group(2).strip())}"
            if (
                not _sentence_like(m.group(2))
                and len(m.group(2).split()) <= 8
                and not re.match(r"^(The |A |An |If |When |For |In |This )", m.group(2))
            )
            else m.group(0)
        ),
        text,
    )
    return text


def _repair_roman_heading_levels(text: str) -> str:
    """Fix ambiguous I/V/X heading depth using neighboring section markers."""
    lines = text.split("\n")
    heads: list[tuple[int, str, str, str]] = []
    for i, line in enumerate(lines):
        m = re.match(r"^(#{2,4})\s+([IVXLCDM]+|[A-Z])\.\s+(.+)$", line)
        if not m:
            continue
        marker = m.group(2)
        # Skip long roman-looking junk
        if marker.isalpha() and marker.upper() == marker and len(marker) <= 6:
            heads.append((i, m.group(1), marker, m.group(3).strip()))

    def nearest_roman(k: int, direction: int):
        j = k + direction
        while 0 <= j < len(heads):
            mk = heads[j][2]
            if mk in _ROMAN_VAL:
                return heads[j]
            j += direction
        return None

    for k, (i, hashes, marker, title) in enumerate(heads):
        # Non-ambiguous multi-character romans stay/force H2
        if marker in _ROMAN_VAL and marker not in ("I", "V", "X"):
            if hashes != "##":
                lines[i] = f"## {marker}. {title}"
            continue
        if marker not in ("I", "V", "X"):
            # Plain letter A-Z (except I/V/X handled above): force H3 unless already H2 title roman-like
            if len(marker) == 1 and marker.isalpha() and hashes == "##" and not _H2_TITLES.match(title):
                # Do not demote true romans already handled; letters as H2 are wrong
                lines[i] = f"### {marker}. {title}"
            continue

        prev = heads[k - 1] if k > 0 else None
        letter_continue = bool(
            prev
            and len(prev[2]) == 1
            and prev[2].isalpha()
            and prev[2] not in _ROMAN_VAL
            and ord(marker) == ord(prev[2]) + 1
        )
        # H -> I is letter continuation even though I is also roman
        if prev and prev[2] == "H" and marker == "I":
            letter_continue = True

        prev_r = nearest_roman(k, -1)
        next_r = nearest_roman(k, 1)
        val = _ROMAN_VAL.get(marker, 0)
        roman_context = False
        if prev_r and prev_r[2] in _ROMAN_VAL and _ROMAN_VAL[prev_r[2]] + 1 == val:
            roman_context = True
        if next_r and next_r[2] in _ROMAN_VAL and _ROMAN_VAL[next_r[2]] - 1 == val:
            roman_context = True
        if prev_r and next_r and prev_r[2] in _ROMAN_VAL and next_r[2] in _ROMAN_VAL:
            if _ROMAN_VAL[prev_r[2]] < val < _ROMAN_VAL[next_r[2]]:
                roman_context = True
        if _H2_TITLES.match(title):
            roman_context = True
            letter_continue = False

        if letter_continue and not roman_context:
            lines[i] = f"### {marker}. {title}"
        elif roman_context:
            lines[i] = f"## {marker}. {title}"
        elif letter_continue:
            lines[i] = f"### {marker}. {title}"
        else:
            # Short definition-like titles after a letter heading stay H3
            words = title.split()
            if prev and len(prev[2]) == 1 and prev[2].isalpha() and len(words) <= 3:
                lines[i] = f"### {marker}. {title}"
            else:
                lines[i] = f"## {marker}. {title}"

    return "\n".join(lines)


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
