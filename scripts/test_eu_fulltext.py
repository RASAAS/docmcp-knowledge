"""EU full-text filing: legal acts in, standard documents out."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import eu_fulltext as eu

ANNEX = """
<div id="anx_1">
<table>
<tr><td>No</td><td>Reference of the standard</td></tr>
<tr><td>1.</td><td>
  <p>EN ISO 10993-1:2018</p>
  <p>Biological evaluation of medical devices - Part 1</p>
</td></tr>
<tr><td colspan="2">replaced</td></tr>
<tr><td>1a.</td><td>
  <p>EN ISO 10993-1:2018</p>
  <p>Biological evaluation of medical devices - Part 1</p>
  <p>EN ISO 10993-1:2018/A1:2025</p>
  <p>Restriction: presumption of conformity is limited to clause 5.</p>
</td></tr>
<tr><td>2.</td><td>
  <p>EN ISO 13485:2016</p>
  <p>Medical devices - Quality management systems</p>
</td></tr>
</table>
</div>
"""

DECISION = """
<p class="title-doc-first">COMMISSION IMPLEMENTING DECISION (EU) 2026/1231</p>
<p class="oj-normal">Whereas:</p>
<p class="oj-normal">(1) The references of harmonised standards need updating.</p>
<p class="title-article-norm">Article 1</p>
<p class="norm">The Annex is amended.</p>
<div id="anx_1"><p class="norm">EN ISO 10993-1:2025 full standard text must not be copied from here.</p></div>
"""


def test_standard_bodies_are_not_downloaded():
    assert eu.is_standard_body_url("https://www.iso.org/standard/123.html")
    assert eu.is_standard_body_url("https://cdn.iec.ch/files/iec-60601.pdf")
    assert not eu.is_standard_body_url(
        "https://health.ec.europa.eu/document/download/abc_en?filename=mdcg_2025-10_en.pdf"
    )
    assert eu.is_harmonised_standards_act("Commission Implementing Decision on harmonised standards", "")
    assert eu.is_harmonised_standards_act("anything", "32021D1182")
    assert not eu.is_harmonised_standards_act("Regulation (EU) 2024/1860 amending the MDR", "32024R1860")


def test_annex_keeps_the_later_row_and_its_note():
    rows = eu.parse_consolidated_annex(ANNEX)
    assert [row["number"] for row in rows] == ["EN ISO 10993-1:2018", "EN ISO 13485:2016"]
    first = rows[0]
    assert first["amendments"] == ["EN ISO 10993-1:2018/A1:2025"]
    assert "clause 5" in first["note"]
    assert "Quality management" in rows[1]["title"]


def test_explanation_stops_before_the_annex():
    text = eu.decision_explanation(DECISION)
    assert "Article 1" in text
    assert "need updating" in text
    assert "must not be copied" not in text
    assert "\n\n" in text


def test_merge_adds_rows_without_erasing_chinese_titles():
    existing = [{
        "number": "EN ISO 13485:2016",
        "title": {"en": "old", "zh": "质量管理体系"},
        "category": "quality_management",
        "standard_type": "harmonised",
        "abstract": "keep me",
    }]
    rows = eu.parse_consolidated_annex(ANNEX)
    # Parser needs 40 rows before withdraw; this fixture only checks add/update.
    result = eu.merge_harmonised_entries(existing, rows, "https://example.test", "2026-10-26")
    assert "EN ISO 10993-1:2018" in result["added"]
    kept = existing[0]
    assert kept["title"]["zh"] == "质量管理体系"
    assert kept["abstract"] == "keep me"
    added = next(item for item in existing if item["number"].startswith("EN ISO 10993-1"))
    assert added["title"]["zh"] == ""
    assert added["oj_note"]
    assert added["category"] == "biocompatibility"


def test_act_heading_ignores_the_filename():
    html = """
    <title>L_202600977EN.000101.fmx.xml</title>
    <p class="oj-doc-ti">COMMISSION IMPLEMENTING REGULATION (EU) 2026/977</p>
    <p class="oj-doc-ti">of 4 May 2026</p>
    <p class="oj-doc-ti">laying down requirements for notified bodies</p>
    <p class="oj-doc-ti">(Text with EEA relevance)</p>
    """
    assert eu.act_heading(html) == (
        "COMMISSION IMPLEMENTING REGULATION (EU) 2026/977 laying down requirements for notified bodies"
    )
    assert ".xml" not in eu.act_heading(html)


def test_celex_and_embed():
    html = '<a href="https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1860">x</a> eli/dec_impl/2026/1231'
    assert eu.celex_numbers_in(html) == ["32024R1860", "32026D1231"]
    page = "# Summary\n\n<!-- fulltext-start -->\n\n参见 [fulltext](./fulltext/x)\n"
    updated = eu.embed_fulltext(page, "Paragraph one.\n\nParagraph two.")
    assert updated.count("<!-- fulltext-start -->") == 1
    assert "Paragraph two." in updated
    assert "参见" not in updated.split("<!-- fulltext-start -->", 1)[1]
    assert not eu.page_already_has_fulltext(page)
