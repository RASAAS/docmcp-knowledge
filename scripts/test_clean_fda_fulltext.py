#!/usr/bin/env python3
"""Unit tests for scripts/clean_fda_fulltext.py layout cleanup."""

from __future__ import annotations

import re
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from clean_fda_fulltext import (  # noqa: E402
    clean_fulltext,
    _extract_footnotes,
    _join_hyphen,
    _normalize_section_headings,
    _remove_preface_and_cover,
    _rejoin_broken_paragraphs,
)


def _wrap(body: str) -> str:
    return (
        "# Title\n\n"
        "**Source:** https://example.com\n\n"
        "**Published:** 2024-01-01\n\n"
        "---\n\n"
        + body
    )


class PrefaceTests(unittest.TestCase):
    def test_does_not_drop_middle_sections(self):
        body = (
            "Cover page junk\nGuidance for Industry\n\n"
            "Table of Contents\nI. Introduction .... 1\nII. Background .... 2\n"
            "VIII. Regulatory .... 17\n\n"
            "This guidance represents the current thinking of the Food and Drug "
            "Administration (FDA or Agency) on this topic.\n\n"
            "I.\nIntroduction\n"
            "Medical devices encompass a vast array of products.\n\n"
            "II. Background\n"
            "FDA has been working to gain additional perspectives.\n\n"
            "III. Scope\n"
            "This guidance applies to devices.\n\n"
            "VIII.\nRegulatory Requirements and Considerations for\n"
            "Remanufacturers\n"
            "As stated above, remanufacturers are considered manufacturers.\n"
        )
        kept = _remove_preface_and_cover(body)
        self.assertIn("This guidance represents", kept)
        self.assertIn("I.", kept)
        self.assertIn("Introduction", kept)
        self.assertIn("II. Background", kept)
        self.assertIn("III. Scope", kept)
        self.assertIn("VIII.", kept)
        self.assertNotIn("Cover page junk", kept)

    def test_clean_keeps_roman_sequence(self):
        raw = _wrap(
            "Contains Nonbinding Recommendations\n"
            "Guidance for Industry\n"
            "Table of Contents\n"
            "I. Introduction .................. 1\n"
            "II. Background ................... 2\n"
            "This guidance represents the current thinking of the Food and Drug "
            "Administration (FDA or Agency) on this topic. It does not establish "
            "any rights.\n\n"
            "I.\nIntroduction\n"
            "Medical devices encompass a vast array of products with different "
            "technologies.\n\n"
            "II. Background\n"
            "FDA has been working to gain additional perspectives on servicing.\n\n"
            "III. Scope\n"
            "This guidance is intended to help clarify activities.\n\n"
            "VIII.\nRegulatory Requirements and Considerations for\n"
            "Remanufacturers\n"
            "As stated above, remanufacturers are considered manufacturers.\n"
        )
        out = clean_fulltext(raw)
        for needle in ("## I. Introduction", "## II. Background", "## III. Scope"):
            self.assertIn(needle, out)
        self.assertIn("## VIII. Regulatory Requirements", out)
        self.assertNotIn("Table of Contents", out)
        self.assertNotIn("Contains Nonbinding", out)


class HeadingTests(unittest.TestCase):
    def test_letter_subsections_are_h3_not_h2(self):
        text = (
            "\nIV. General Principles\n"
            "Intro paragraph.\n"
            "\nC.\nCybersecurity Testing\n"
            "Testing is used to demonstrate effectiveness.\n"
            "\nD. Submission Documentation\n"
            "Device cybersecurity design should scale.\n"
        )
        out = _normalize_section_headings(text)
        self.assertIn("## IV. General Principles", out)
        self.assertIn("### C. Cybersecurity Testing", out)
        self.assertIn("### D. Submission Documentation", out)

    def test_ambiguous_I_threat_modeling_is_h3(self):
        text = "\nI.\nThreat Modeling\nThreat modeling is a methodology.\n"
        out = _normalize_section_headings(text)
        self.assertRegex(out, r"(?m)^### I\. Threat Modeling$")
        self.assertFalse(re.search(r"(?m)^## I\. Threat Modeling$", out))


class RejoinTests(unittest.TestCase):
    def test_wrap_capitalized_continuation(self):
        text = (
            "This guidance represents the current thinking of the Food and Drug "
            "Administration (FDA or\n"
            "Agency) on this topic.\n"
        )
        out = _rejoin_broken_paragraphs(text)
        self.assertIn("FDA or Agency", out)
        self.assertNotIn("or\nAgency", out)

    def test_does_not_glue_heading_to_paragraph(self):
        text = (
            "VIII. Regulatory Requirements and Considerations for\n"
            "Remanufacturers\n"
            "As stated above, remanufacturers are considered manufacturers under the Act.\n"
        )
        out = _rejoin_broken_paragraphs(text)
        self.assertIn("for Remanufacturers", out)
        self.assertIn("As stated above", out)
        self.assertNotRegex(out, r"Remanufacturers As stated")

    def test_device_related_keeps_hyphen(self):
        self.assertEqual(_join_hyphen("device-", "related health"), "device-related health")

    def test_syllable_hyphen_dropped(self):
        self.assertEqual(_join_hyphen("informa-", "tion about"), "information about")


class FootnoteTests(unittest.TestCase):
    def test_extracts_real_footnote_not_body(self):
        text = (
            "A cybersecurity signal is any information which indicates a vulnerability.\n"
            "1 See FDA guidance titled “Content of Premarket Submissions”.\n"
            "Manufacturers should monitor sources.\n"
        )
        body, fns = _extract_footnotes(text)
        self.assertTrue(any(f.startswith("[^1]:") for f in fns))
        self.assertIn("A cybersecurity signal", body)
        self.assertNotIn("See FDA guidance titled", body)

    def test_does_not_swallow_roman_heading(self):
        text = (
            "46 See 21 CFR 820.3(w).\n"
            "VIII.\n"
            "Regulatory Requirements and Considerations for\n"
            "Remanufacturers\n"
            "As stated above, remanufacturers are considered manufacturers.\n"
        )
        body, fns = _extract_footnotes(text)
        self.assertTrue(any("[^46]:" in f for f in fns))
        self.assertIn("VIII.", body)
        self.assertIn("Regulatory Requirements", body)
        self.assertNotIn("VIII.", "".join(fns))

    def test_does_not_eat_body_starting_with_A(self):
        text = "A cybersecurity signal is any information which indicates a vulnerability.\n"
        body, fns = _extract_footnotes(text)
        self.assertEqual(fns, [])
        self.assertIn("A cybersecurity signal", body)


class EscapeTests(unittest.TestCase):
    def test_insert_tags_escaped(self):
        raw = _wrap(
            "This guidance represents the current thinking of the Food and Drug "
            "Administration (FDA or Agency) on this topic.\n\n"
            "I. Introduction\n"
            "Replace <Insert Month and Year> with the date.\n"
        )
        out = clean_fulltext(raw)
        self.assertIn("&lt;Insert", out)
        self.assertNotIn("<Insert Month", out)


if __name__ == "__main__":
    unittest.main()
