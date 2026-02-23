#!/usr/bin/env python3
"""
Embed docling full-text into .zh.md data layer files and generate .en.md counterparts.

For each MDCG document that has a fulltext/*.md file:
1. Append full-text section to the .zh.md file (if not already present)
2. Create a .en.md file with English summary + full text

Run from repo root:
    python3 scripts/embed_fulltext_and_gen_en.py [--ids mdcg-2020-5 mdcg-2020-6] [--dry-run]
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
MDCG_DATA_DIR = REPO_ROOT / "eu_mdr" / "mdcg"
FULLTEXT_DIR = MDCG_DATA_DIR / "fulltext"
FULLTEXT_MARKER = "<!-- fulltext-start -->"
FULLTEXT_END_MARKER = "<!-- fulltext-end -->"

# English summaries for each document (key facts extracted from full text)
# These are concise English-language overviews for the .en.md files
EN_SUMMARIES = {
    "mdcg-2020-5": {
        "title": "MDCG 2020-5: Clinical Evaluation – Equivalence",
        "purpose": "Clarifies the concept of 'equivalence' under MDR Article 61(1) and Annex XIV Part A Section 3, providing practical guidance for manufacturers and notified bodies on demonstrating equivalence to an existing device.",
        "key_points": [
            "Equivalence must be demonstrated across **three dimensions simultaneously**: technical, biological, and clinical characteristics.",
            "**Technical**: Similar design, conditions of use, specifications, deployment methods, and principles of operation.",
            "**Biological**: Same materials or substances in contact with body tissues/cells/fluids.",
            "**Clinical**: Same intended purpose, body site, patient population, and conditions of use.",
            "For **Class III and implantable devices**: manufacturer must have a contract with the equivalent device's manufacturer granting access to technical documentation (Article 61(5)).",
            "**Single device rule**: Equivalence must be established to a single device — combining characteristics from multiple devices to create a 'virtual' equivalent is not permitted.",
            "All differences must be identified, documented, and justified as not affecting safety or clinical performance.",
        ],
        "related": [
            ("MDCG 2020-6", "./mdcg-2020-6", "Sufficient clinical evidence for legacy devices"),
            ("MDCG 2023-7", "./mdcg-2023-7", "Exemptions from clinical investigations"),
            ("Annex XIV", "/en/eu_mdr/regulations/annex-xiv-clinical-evaluation", "Clinical Evaluation"),
        ],
    },
    "mdcg-2020-6": {
        "title": "MDCG 2020-6: Sufficient Clinical Evidence for Legacy Devices",
        "purpose": "Defines what constitutes 'sufficient clinical evidence' for legacy devices (devices CE-marked under MDD/AIMDD before MDR application date of 26 May 2021) to meet MDR Article 61 requirements.",
        "key_points": [
            "**Legacy device**: A device CE-marked under MDD (93/42/EEC) or AIMDD (90/385/EEC) before 26 May 2021.",
            "Manufacturers must demonstrate an acceptable benefit/risk ratio based on existing clinical data.",
            "**Existing clinical data sources**: post-market data (complaints, vigilance, PMCF), published literature, clinical investigation data.",
            "Clinical evidence sufficiency is assessed on **quantity, quality, relevance, and currency** of data.",
            "**PMCF is mandatory**: manufacturers must have a PMCF plan to address data gaps.",
            "The background note clarifies the relationship between this guidance and MEDDEV 2.7/1 rev.4.",
        ],
        "related": [
            ("MDCG 2020-5", "./mdcg-2020-5", "Equivalence guidance"),
            ("MDCG 2020-7", "./mdcg-2020-7", "PMCF Plan template"),
            ("MDCG 2020-8", "./mdcg-2020-8", "PMCF Evaluation Report template"),
        ],
    },
    "mdcg-2020-7": {
        "title": "MDCG 2020-7: PMCF Plan Template",
        "purpose": "Provides a template for the Post-Market Clinical Follow-up (PMCF) Plan required under MDR Annex XIV Part B.",
        "key_points": [
            "**PMCF Plan** is a mandatory component of the clinical evaluation documentation under MDR Annex XIV Part B.",
            "The template covers: general device information, PMCF objectives, methods (PMCF studies, registries, surveys, literature), timelines, and responsible persons.",
            "PMCF activities must be proactive and systematic — not just reactive vigilance reporting.",
            "The plan must be updated periodically based on PMCF evaluation report findings.",
            "Manufacturers may use alternative formats provided all required elements are addressed.",
        ],
        "related": [
            ("MDCG 2020-8", "./mdcg-2020-8", "PMCF Evaluation Report template"),
            ("MDCG 2020-6", "./mdcg-2020-6", "Sufficient clinical evidence for legacy devices"),
        ],
    },
    "mdcg-2020-8": {
        "title": "MDCG 2020-8: PMCF Evaluation Report Template",
        "purpose": "Provides a template for the Post-Market Clinical Follow-up (PMCF) Evaluation Report required under MDR Annex XIV Part B.",
        "key_points": [
            "**PMCF Evaluation Report** documents the results of PMCF activities and feeds back into the Clinical Evaluation Report (CER).",
            "Must be updated at least annually for high-risk devices (Class III, implantable) or when significant new information is available.",
            "The report must assess whether PMCF objectives were met and identify any new risks or performance issues.",
            "Conclusions must be reflected in the CER, risk management file, and instructions for use.",
            "The template includes sections for: executive summary, PMCF activities performed, data analysis, conclusions, and next steps.",
        ],
        "related": [
            ("MDCG 2020-7", "./mdcg-2020-7", "PMCF Plan template"),
            ("MDCG 2022-21", "./mdcg-2022-21", "PSUR guidance"),
        ],
    },
    "mdcg-2019-9": {
        "title": "MDCG 2019-9 rev.1: Summary of Safety and Clinical Performance (SSCP)",
        "purpose": "Provides guidance on the content and format of the Summary of Safety and Clinical Performance (SSCP) required under MDR Article 32 for implantable devices and Class III devices.",
        "key_points": [
            "**SSCP is mandatory** for implantable devices and Class III devices under MDR Article 32.",
            "Must be written in a way that is clear to the intended user (lay person and healthcare professional).",
            "Must be validated by the notified body as part of the conformity assessment.",
            "Must be uploaded to EUDAMED and made publicly available.",
            "Key sections: device description, intended purpose, clinical evidence summary, residual risks, profile of intended users, revision history.",
            "Must be updated whenever the CER is updated or when significant new information becomes available.",
            "Rev.1 (2022) updated to align with EUDAMED requirements and clarify content expectations.",
        ],
        "related": [
            ("MDCG 2020-5", "./mdcg-2020-5", "Equivalence guidance"),
            ("MDCG 2022-21", "./mdcg-2022-21", "PSUR guidance"),
        ],
    },
    "mdcg-2019-7": {
        "title": "MDCG 2019-7 rev.1: Person Responsible for Regulatory Compliance (PRRC)",
        "purpose": "Guidance on Article 15 MDR/IVDR regarding the Person Responsible for Regulatory Compliance (PRRC) — qualifications, responsibilities, and manufacturer obligations.",
        "key_points": [
            "**PRRC is mandatory** for all manufacturers and authorised representatives placing devices on the EU market.",
            "Minimum qualifications: relevant degree PLUS at least one year of professional experience in regulatory affairs or QMS.",
            "Micro and small enterprises may designate a person who does not permanently work for the organisation.",
            "PRRC responsibilities: ensuring conformity assessments, technical documentation, post-market obligations, and reporting are fulfilled.",
            "Rev.1 (2023) updated to clarify qualification requirements and responsibilities.",
        ],
        "related": [("MDCG 2021-27", "./mdcg-2021-27", "Q&A on Articles 13 & 14")],
    },
    "mdcg-2019-15": {
        "title": "MDCG 2019-15 rev.1: Guidance for Manufacturers of Class I Medical Devices",
        "purpose": "Guidance notes for manufacturers of Class I medical devices on self-declaration of conformity under MDR, including sterile, measuring, and reusable surgical instrument sub-classes.",
        "key_points": [
            "Class I devices are self-declared by the manufacturer (no notified body required for standard Class I).",
            "**Exceptions**: Class Is (sterile), Class Im (measuring), Class Ir (reusable surgical) require notified body involvement for specific aspects.",
            "Manufacturers must establish a QMS and maintain technical documentation.",
        ],
        "related": [("MDCG 2021-24", "./mdcg-2021-24", "Classification of medical devices")],
    },
    "mdcg-2019-16": {
        "title": "MDCG 2019-16 rev.1: Guidance on Cybersecurity for Medical Devices",
        "purpose": "Guidance on cybersecurity requirements for medical devices under MDR/IVDR, covering the full device lifecycle from design through post-market surveillance.",
        "key_points": [
            "Cybersecurity is a **safety and performance** requirement under MDR Annex I (GSPR).",
            "Manufacturers must implement a **Secure Development Lifecycle (SDLC)**.",
            "Minimum security requirements: authentication, authorisation, encryption, audit logging, software update mechanisms.",
            "Post-market: manufacturers must monitor for vulnerabilities and provide security patches.",
        ],
        "related": [("MDCG 2020-1", "./mdcg-2020-1", "Clinical evaluation of MDSW")],
    },
    "mdcg-2020-1": {
        "title": "MDCG 2020-1: Clinical Evaluation of Medical Device Software (MDSW)",
        "purpose": "Guidance on clinical evaluation of Medical Device Software (MDSW) under MDR/IVDR, addressing software-specific challenges.",
        "key_points": [
            "Clinical evaluation of MDSW follows the same framework as hardware devices (MDR Article 61, Annex XIV).",
            "**Intended purpose** must be precisely defined including clinical condition, patient population, and context.",
            "**Equivalence** for software is particularly challenging — algorithm, data inputs, and clinical context must all be equivalent.",
            "**Real-world performance data** is especially important for AI/ML-based MDSW.",
        ],
        "related": [("MDCG 2019-16", "./mdcg-2019-16", "Cybersecurity guidance"), ("MDCG 2025-6", "./mdcg-2025-6", "MDR/IVDR and AI Act")],
    },
    "mdcg-2020-3": {
        "title": "MDCG 2020-3 rev.1: Significant Changes under Article 120 MDR Transitional Provisions",
        "purpose": "Guidance on what constitutes a 'significant change' triggering MDR re-certification under Article 120 transitional provisions.",
        "key_points": [
            "A **significant change** to design or intended purpose triggers MDR certification requirement.",
            "Significant changes include: new intended purpose, new patient population, new clinical claims, major design changes.",
            "Non-significant changes (minor labelling updates, supplier changes not affecting performance) do not trigger re-certification.",
            "Rev.1 (2023) updated to reflect extended timelines under Regulation 2023/607.",
        ],
        "related": [("MDCG 2021-25", "./mdcg-2021-25", "MDR requirements for legacy devices")],
    },
    "mdcg-2020-13": {
        "title": "MDCG 2020-13: Clinical Evaluation Assessment Report (CEAR) Template",
        "purpose": "Template for the Clinical Evaluation Assessment Report (CEAR) used by notified bodies when reviewing the manufacturer's Clinical Evaluation Report.",
        "key_points": [
            "The CEAR is the notified body's documented assessment of the manufacturer's CER.",
            "Required for Class IIb, Class III, and implantable devices.",
            "Covers: device identification, clinical evaluation methodology, clinical data adequacy, equivalence assessment, PMCF plan review.",
        ],
        "related": [("MDCG 2020-5", "./mdcg-2020-5", "Equivalence guidance")],
    },
    "mdcg-2021-5": {
        "title": "MDCG 2021-5 rev.1: Guidance on Standardisation for Medical Devices",
        "purpose": "Guidance on the role of harmonised standards in demonstrating conformity with MDR/IVDR requirements.",
        "key_points": [
            "Harmonised standards provide a **presumption of conformity** with MDR/IVDR requirements they cover.",
            "Use of harmonised standards is voluntary — manufacturers may use other means.",
            "**Common Specifications (CS)** are mandatory where specified by the Commission.",
            "Manufacturers must monitor for standard updates and assess impact on technical documentation.",
        ],
        "related": [],
    },
    "mdcg-2021-6": {
        "title": "MDCG 2021-6 rev.1: Q&A on Clinical Investigations under MDR",
        "purpose": "Q&A on clinical investigations under MDR, covering application procedures, substantial modifications, and safety reporting.",
        "key_points": [
            "Clinical investigations require prior authorisation from the Member State(s) where conducted.",
            "**Substantial modifications** require notification and may require re-authorisation.",
            "Safety reporting: SAEs and device deficiencies must be reported within defined timelines.",
        ],
        "related": [("MDCG 2021-8", "./mdcg-2021-8", "Clinical investigation application documents")],
    },
    "mdcg-2021-8": {
        "title": "MDCG 2021-8: Clinical Investigation Application/Notification Documents",
        "purpose": "Document checklist for clinical investigation applications (Article 70) and notifications (Article 74) under MDR.",
        "key_points": [
            "Article 70 applications: full package including CIP, IB, risk assessment, and device documentation.",
            "Article 74 notifications (CE-marked devices, within intended purpose): simplified procedure.",
            "Documents must be in the official language(s) of the Member State(s) or accepted language.",
        ],
        "related": [("MDCG 2024-3", "./mdcg-2024-3", "CIP content guidance")],
    },
    "mdcg-2021-24": {
        "title": "MDCG 2021-24: Guidance on Classification of Medical Devices",
        "purpose": "Comprehensive guidance on the classification of medical devices under MDR Annex VIII, covering all 22 classification rules with examples.",
        "key_points": [
            "MDR Annex VIII contains **22 classification rules** based on intended purpose, duration, invasiveness, and active device status.",
            "Classification is the manufacturer's responsibility, subject to challenge by competent authorities.",
            "Software classification: Rule 11 applies — most diagnostic software is Class IIa or higher.",
            "When multiple rules apply, the **highest classification** takes precedence.",
        ],
        "related": [("MDCG 2022-5", "./mdcg-2022-5", "Borderline devices/medicinal products")],
    },
    "mdcg-2021-25": {
        "title": "MDCG 2021-25 rev.1: MDR Requirements for Legacy Devices",
        "purpose": "Clarifies MDR requirements for legacy devices and their continued availability under transitional provisions (as amended by Regulation 2023/607).",
        "key_points": [
            "Extended deadlines: Class III/IIb implantables until 31 Dec 2027; Class IIb non-implantables/IIa until 31 Dec 2028.",
            "Conditions: valid MDD/AIMDD certificate, no significant changes, active MDR certification process.",
            "Manufacturers must register in EUDAMED and have a QMS in place.",
        ],
        "related": [("MDCG 2020-3", "./mdcg-2020-3", "Significant changes under transitional provisions")],
    },
    "mdcg-2021-27": {
        "title": "MDCG 2021-27 rev.1: Q&A on Articles 13 & 14 MDR/IVDR (Distributors & Importers)",
        "purpose": "Q&A on obligations of distributors and importers under Articles 13 and 14 of MDR/IVDR.",
        "key_points": [
            "**Importers** must verify CE marking, EU DoC, labelling, and PRRC before placing devices on the market.",
            "**Distributors** must verify CE marking and labelling before making devices available.",
            "Both must maintain traceability records and register in EUDAMED.",
        ],
        "related": [("MDCG 2019-7", "./mdcg-2019-7", "PRRC guidance")],
    },
    "mdcg-2022-5": {
        "title": "MDCG 2022-5 rev.1: Borderline Between Medical Devices and Medicinal Products",
        "purpose": "Guidance on determining whether a product is a medical device or a medicinal product, addressing borderline and combination products.",
        "key_points": [
            "**Principal mode of action** determines classification: pharmacological/immunological/metabolic → medicinal product; physical/mechanical → medical device.",
            "**Drug-device combinations**: ancillary drug → medical device; ancillary device → medicinal product.",
            "Manufacturers must document their regulatory status determination with scientific justification.",
        ],
        "related": [("MDCG 2021-24", "./mdcg-2021-24", "Classification of medical devices")],
    },
    "mdcg-2022-21": {
        "title": "MDCG 2022-21: Guidance on Periodic Safety Update Report (PSUR)",
        "purpose": "Guidance on content, format, and submission of the PSUR required under MDR Article 86 for Class IIa, IIb, and III devices.",
        "key_points": [
            "**PSUR is mandatory** for Class IIa, IIb, and III devices.",
            "Frequency: Class III/implantable IIb — annually; other IIb — every 2 years; IIa — every 2 years.",
            "Must summarise: PMS data, benefit/risk conclusions, PMCF conclusions, sales volumes, corrective actions.",
            "Conclusions must be reflected in the CER update.",
        ],
        "related": [("MDCG 2020-7", "./mdcg-2020-7", "PMCF Plan template")],
    },
    "mdcg-2023-1": {
        "title": "MDCG 2023-1: Health Institution Exemption under Article 5(5) MDR/IVDR",
        "purpose": "Guidance on the health institution exemption allowing in-house manufacture and use of devices without full MDR/IVDR conformity assessment.",
        "key_points": [
            "Conditions: no equivalent CE-marked device available, used within the institution, patients/users informed.",
            "Institution must have a QMS, document justification, and notify the competent authority.",
            "Does **not** apply to devices manufactured at industrial scale.",
        ],
        "related": [],
    },
    "mdcg-2023-4": {
        "title": "MDCG 2023-4: Medical Device Software (MDSW) – Hardware Combinations",
        "purpose": "Guidance on MDSW intended to work in combination with hardware, clarifying regulation and documentation requirements.",
        "key_points": [
            "The combination may be regulated as a **system** or as separate devices depending on intended purpose.",
            "Classification determined by the highest-risk component.",
            "If software and hardware are placed on the market separately, each needs its own conformity assessment.",
        ],
        "related": [("MDCG 2020-1", "./mdcg-2020-1", "Clinical evaluation of MDSW")],
    },
    "mdcg-2023-5": {
        "title": "MDCG 2023-5: Qualification and Classification of Annex XVI Products",
        "purpose": "Guidance on qualification and classification of products without intended medical purpose listed in MDR Annex XVI.",
        "key_points": [
            "MDR Annex XVI lists **6 categories** of non-medical products regulated as medical devices.",
            "Common Specifications (CS) for Annex XVI products are mandatory.",
            "Clinical evaluation requirements apply, including demonstration of safety and performance.",
        ],
        "related": [("MDCG 2023-6", "./mdcg-2023-6", "Equivalence for Annex XVI products")],
    },
    "mdcg-2023-6": {
        "title": "MDCG 2023-6: Equivalence for Annex XVI Products",
        "purpose": "Guidance on demonstrating equivalence for Annex XVI products (products without intended medical purpose regulated under MDR).",
        "key_points": [
            "Equivalence follows the same three-dimensional framework (technical, biological, clinical) as for medical devices.",
            "The **intended purpose** for Annex XVI products is defined by the Common Specifications.",
            "Access to technical documentation requirements (Article 61(5)) apply equally.",
        ],
        "related": [("MDCG 2023-5", "./mdcg-2023-5", "Qualification and classification of Annex XVI products")],
    },
    "mdcg-2023-7": {
        "title": "MDCG 2023-7: Exemptions from Clinical Investigations (Article 61(4)-(6) MDR)",
        "purpose": "Guidance on conditions for exemption from clinical investigations under Article 61(4)-(6) MDR and on sufficient data access for equivalence claims.",
        "key_points": [
            "Article 61(4): exemption where clinical data from equivalent device is sufficient.",
            "Article 61(5): Class III/implantable devices require contract for access to equivalent device's technical documentation.",
            "**'Sufficient access'** means verifying completeness and accuracy of clinical data, not just published literature.",
            "Generic literature reviews are generally insufficient for Class III/implantable devices.",
        ],
        "related": [("MDCG 2020-5", "./mdcg-2020-5", "Equivalence guidance")],
    },
    "mdcg-2024-3": {
        "title": "MDCG 2024-3: Clinical Investigation Plan (CIP) Content Guidance",
        "purpose": "Guidance on CIP content requirements under MDR Annex XV Chapter II, including a CIP Synopsis Template.",
        "key_points": [
            "Key CIP sections: rationale, design, endpoints, statistics, risk management, monitoring, data management, ethics.",
            "**Primary endpoint** must be clinically meaningful and directly reflect the device's intended purpose.",
            "The CIP Synopsis Template provides a standardised format for EUDAMED submission.",
        ],
        "related": [("MDCG 2024-5", "./mdcg-2024-5", "Investigator's Brochure content")],
    },
    "mdcg-2024-5": {
        "title": "MDCG 2024-5: Investigator's Brochure (IB) Content Guidance",
        "purpose": "Guidance on the content of the Investigator's Brochure required for clinical investigations under MDR.",
        "key_points": [
            "Required content: device description, preclinical data, clinical data summary, risk/benefit assessment, IFU.",
            "Must be updated throughout the investigation as new information becomes available.",
            "For first-in-human studies, must include comprehensive preclinical safety data.",
        ],
        "related": [("MDCG 2024-3", "./mdcg-2024-3", "CIP content guidance")],
    },
    "mdcg-2024-10": {
        "title": "MDCG 2024-10: Clinical Evaluation of Orphan Medical Devices",
        "purpose": "Guidance on clinical evaluation of orphan medical devices intended for rare conditions (≤5 in 10,000 persons in the EU).",
        "key_points": [
            "Small patient population makes adequately powered clinical investigations challenging.",
            "Alternative evidence strategies: registries, case series, real-world data, pathophysiology literature.",
            "Notified bodies must apply proportionate scrutiny recognising inherent evidence limitations.",
            "PMCF is particularly important to collect post-market real-world data.",
        ],
        "related": [("MDCG 2023-7", "./mdcg-2023-7", "Exemptions from clinical investigations")],
    },
    "mdcg-2025-4": {
        "title": "MDCG 2025-4: Safe Making Available of MDSW Apps on Online Platforms",
        "purpose": "Guidance on obligations of online platforms and manufacturers when making MDSW apps available online, addressing the intersection of MDR and the Digital Services Act (DSA).",
        "key_points": [
            "Online platforms hosting MDSW apps must implement measures to prevent non-compliant apps.",
            "Manufacturers remain responsible for MDR compliance regardless of distribution channel.",
            "Platforms should implement **Know Your Business Customer (KYBC)** checks for MDSW developers.",
        ],
        "related": [("MDCG 2020-1", "./mdcg-2020-1", "Clinical evaluation of MDSW")],
    },
    "mdcg-2025-6": {
        "title": "MDCG 2025-6: FAQ on MDR/IVDR and Artificial Intelligence Act (AIA) Interplay",
        "purpose": "FAQ on the interplay between MDR/IVDR and the EU Artificial Intelligence Act for AI-based medical devices.",
        "key_points": [
            "AI-based medical devices may be subject to **both MDR/IVDR and the AI Act** simultaneously.",
            "**High-risk AI systems** under the AI Act include AI used in medical devices.",
            "Where requirements overlap, the **more specific regulation takes precedence**.",
            "Conformity assessment under both frameworks may be conducted jointly by the same notified body.",
        ],
        "related": [("MDCG 2020-1", "./mdcg-2020-1", "Clinical evaluation of MDSW")],
    },
    "mdcg-2025-9": {
        "title": "MDCG 2025-9: Guidance on Breakthrough Devices (BtX)",
        "purpose": "Guidance on the Breakthrough Devices (BtX) pathway under MDR/IVDR, which provides accelerated access for innovative devices addressing unmet medical needs.",
        "key_points": [
            "BtX designation is available for devices that provide more effective diagnosis or treatment of life-threatening or seriously debilitating conditions.",
            "Benefits: early and enhanced interaction with notified bodies, prioritised conformity assessment.",
            "Manufacturers must apply for BtX designation and meet specific eligibility criteria.",
            "A pilot programme is expected to be launched in Q2 2026.",
            "BtX does **not** lower the safety and performance requirements — full MDR/IVDR compliance is still required.",
        ],
        "related": [("MDCG 2024-10", "./mdcg-2024-10", "Clinical evaluation of orphan devices")],
    },
}


def read_front_matter_raw(file_path: Path) -> tuple[str, str]:
    """Return (front_matter_block, body) where front_matter_block includes --- delimiters."""
    content = file_path.read_text(encoding="utf-8")
    if not content.startswith("---"):
        return "", content
    end = content.find("---", 3)
    if end < 0:
        return "", content
    fm = content[:end + 3]
    body = content[end + 3:].lstrip("\n")
    return fm, body


def get_en_title(zh_file: Path) -> str:
    """Extract English title from YAML front matter."""
    content = zh_file.read_text(encoding="utf-8")
    m = re.search(r'en:\s*"([^"]+)"', content)
    if m:
        return m.group(1)
    m = re.search(r"en:\s*(.+)", content)
    if m:
        return m.group(1).strip()
    return zh_file.stem.replace(".zh", "").upper()


def get_source_url(zh_file: Path) -> str:
    content = zh_file.read_text(encoding="utf-8")
    m = re.search(r"source_url:\s*(https?://\S+)", content)
    return m.group(1) if m else ""


def get_published_date(zh_file: Path) -> str:
    content = zh_file.read_text(encoding="utf-8")
    m = re.search(r'published_date:\s*"?(\d{4})', content)
    return m.group(1) if m else ""


def embed_fulltext_in_zh(doc_id: str, zh_file: Path, fulltext: str, dry_run: bool) -> bool:
    """Append full-text section to .zh.md if not already present. Returns True if modified."""
    content = zh_file.read_text(encoding="utf-8")
    if FULLTEXT_MARKER in content:
        print(f"  [SKIP] {doc_id}.zh.md already has full text")
        return False

    fulltext_section = f"""
{FULLTEXT_MARKER}

---

## 官方文件全文

{fulltext}

{FULLTEXT_END_MARKER}
"""
    new_content = content.rstrip() + "\n" + fulltext_section
    if dry_run:
        print(f"  [DRY] Would embed full text into {zh_file.name} (+{len(fulltext)} chars)")
        return True
    zh_file.write_text(new_content, encoding="utf-8")
    print(f"  [OK] Embedded full text into {zh_file.name}")
    return True


def generate_en_file(doc_id: str, zh_file: Path, fulltext: str, dry_run: bool) -> bool:
    """Generate .en.md file alongside .zh.md. Returns True if created."""
    en_file = zh_file.parent / zh_file.name.replace(".zh.md", ".en.md")
    if en_file.exists():
        print(f"  [SKIP] {en_file.name} already exists")
        return False

    en_title = get_en_title(zh_file)
    source_url = get_source_url(zh_file)
    year = get_published_date(zh_file)
    doc_num = doc_id.replace("mdcg-", "MDCG ").replace("-", "-", 1)
    # e.g. mdcg-2020-5 -> MDCG 2020-5
    parts = doc_id.replace("mdcg-", "").split("-")
    if len(parts) == 2:
        doc_num = f"MDCG {parts[0]}-{parts[1]}"
    else:
        doc_num = doc_id.upper()

    summary_data = EN_SUMMARIES.get(doc_id)

    # Build front matter
    fm_lines = [
        "---",
        f"title:",
        f"  en: \"{en_title}\"",
        f"document_number: {doc_num}",
        f"regulation: eu_mdr",
        f"category: eu_mdr/mdcg",
        f"source_url: {source_url}",
        f'published_date: "{year}-01-01"' if year else "",
        f"status: active",
        f"lang: en",
        "---",
        "",
    ]
    fm = "\n".join(l for l in fm_lines if l != "") + "\n"

    # Build body
    body_lines = [
        f"# {en_title}",
        "",
        f"**Document**: {doc_num}  ",
        f"**Year**: {year}  " if year else "",
        f"**Regulation**: EU MDR 2017/745  ",
        f"**Official PDF**: [Download]({source_url})" if source_url else "",
        "",
    ]

    if summary_data:
        body_lines += [
            "## Purpose",
            "",
            summary_data["purpose"],
            "",
            "## Key Points",
            "",
        ]
        for point in summary_data["key_points"]:
            body_lines.append(f"- {point}")
        body_lines.append("")

        if summary_data.get("related"):
            body_lines += ["## Related Documents", ""]
            for ref_num, ref_link, ref_desc in summary_data["related"]:
                body_lines.append(f"- [{ref_num}]({ref_link}): {ref_desc}")
            body_lines.append("")
    else:
        body_lines += [
            "## Overview",
            "",
            f"> This page provides the full text of {doc_num}.",
            "",
        ]

    body_lines += [
        FULLTEXT_MARKER,
        "",
        "---",
        "",
        "## Full Text",
        "",
        fulltext,
        "",
        FULLTEXT_END_MARKER,
    ]

    final_content = fm + "\n".join(b for b in body_lines if b is not None)

    if dry_run:
        print(f"  [DRY] Would create {en_file.name} ({len(final_content)} chars)")
        return True
    en_file.write_text(final_content, encoding="utf-8")
    print(f"  [OK] Created {en_file.name}")
    return True


def process_doc(doc_id: str, dry_run: bool) -> dict:
    zh_file = MDCG_DATA_DIR / f"{doc_id}.zh.md"
    fulltext_file = FULLTEXT_DIR / f"{doc_id}.md"

    result = {"zh_updated": False, "en_created": False, "error": None}

    if not zh_file.exists():
        result["error"] = f"zh file not found: {zh_file}"
        return result
    if not fulltext_file.exists():
        result["error"] = f"fulltext not found: {fulltext_file} (not yet converted?)"
        return result

    fulltext = fulltext_file.read_text(encoding="utf-8")

    result["zh_updated"] = embed_fulltext_in_zh(doc_id, zh_file, fulltext, dry_run)
    result["en_created"] = generate_en_file(doc_id, zh_file, fulltext, dry_run)
    return result


def main():
    parser = argparse.ArgumentParser(description="Embed full text and generate English versions")
    parser.add_argument("--ids", nargs="+", help="Specific doc IDs to process")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if args.ids:
        target_ids = args.ids
    else:
        # Process all that have fulltext available
        target_ids = sorted(
            f.stem for f in FULLTEXT_DIR.glob("*.md")
        )

    print(f"Processing {len(target_ids)} documents...")
    zh_updated = en_created = errors = 0

    for doc_id in target_ids:
        print(f"\n[{doc_id}]")
        result = process_doc(doc_id, args.dry_run)
        if result["error"]:
            print(f"  [ERROR] {result['error']}")
            errors += 1
        else:
            if result["zh_updated"]:
                zh_updated += 1
            if result["en_created"]:
                en_created += 1

    print(f"\n=== Summary ===")
    print(f"zh updated: {zh_updated}, en created: {en_created}, errors: {errors}")


if __name__ == "__main__":
    main()
