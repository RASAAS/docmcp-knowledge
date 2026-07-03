#!/usr/bin/env python3
"""
Automated Regulatory Update Monitoring Script
Checks official sources for new/updated regulatory content and creates update reports.

Strategy (5-layer detection with DB comparison):
  Layer 1: RSS Feed          - FDA Medical Devices RSS (real-time, no anti-scraping)
  Layer 2: Structured API    - eCFR Versioner API, EUR-Lex (replaces unreliable http_head)
  Layer 3: Vertex AI Search  - Preferred: searchLite API (free 10K/month, site-restricted)
           (Google CSE)      - Legacy fallback (sunsets 2027-01-01)
  Layer 4: OpenFDA API       - FDA guidance search via official API
  Layer 5: EC Page Scraper   - Direct HTML parsing of EC MDCG guidance page (full coverage)
  Filter:  DatabaseComparator - Compare detections against existing _index.json data

Usage:
    python scripts/fetch_updates.py --check-all
    python scripts/fetch_updates.py --check eu_mdr
    python scripts/fetch_updates.py --check nmpa
    python scripts/fetch_updates.py --check fda
    python scripts/fetch_updates.py --report  # JSON report for GitHub Actions
    python scripts/fetch_updates.py --analyze-versions  # LLM version analysis

Batched cron schedule (weekly, by regulation group):
  Mon: eu_mdr   Wed: fda   Fri: nmpa   1st of month: shared
"""

import argparse
import json
import os
import re
import sys
import time
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Optional
from urllib.parse import urlparse

try:
    import requests
except ImportError:
    print("ERROR: requests not installed. Run: pip install requests")
    sys.exit(1)

ROOT = Path(__file__).parent.parent
VERSION_REGISTRY_PATH = ROOT / "scripts" / "version_registry.json"

# ---------------------------------------------------------------------------
# Environment variables (set as GitHub Secrets / local .env)
# ---------------------------------------------------------------------------
# Vertex AI Search (preferred -- replaces CSE from 2027-01-01)
VERTEX_AI_PROJECT_ID = os.environ.get("VERTEX_AI_PROJECT_ID", "")
VERTEX_AI_SEARCH_APP_ID = os.environ.get("VERTEX_AI_SEARCH_APP_ID", "")
VERTEX_AI_SEARCH_API_KEY = os.environ.get("VERTEX_AI_SEARCH_API_KEY", "")

# Legacy Google CSE (fallback if Vertex AI not configured; sunsets 2027-01-01)
GOOGLE_SEARCH_API_KEY = ""  # DEPRECATED: Google CSE no longer used, Vertex AI Search only
GOOGLE_SEARCH_ENGINE_ID = ""
FDA_API_KEY = os.environ.get("FDA_API_KEY", "")

# LLM (OneAPI-compatible, e.g. https://api.reguverse.com/v1)
# LLM_API_KEY   : API key for the LLM provider
# LLM_BASE_URL  : Base URL of the OpenAI-compatible endpoint (no trailing slash)
# LLM_MODEL     : Model name, e.g. deepseek-chat, gpt-4o-mini
LLM_API_KEY = os.environ.get("LLM_API_KEY", "")
LLM_BASE_URL = os.environ.get("LLM_BASE_URL", "https://api.openai.com/v1")
LLM_MODEL = os.environ.get("LLM_MODEL", "deepseek-v4-pro")

# ---------------------------------------------------------------------------
# Source definitions
# ---------------------------------------------------------------------------
SOURCES = {
    "eu_mdr": {
        "harmonised_standards": {
            "name": "EU MDR Harmonised Standards (EUR-Lex Amendment Check)",
            "url": "https://eur-lex.europa.eu/eli/dec_impl/2021/1182/oj",
            "check_type": "eurlex_amendment",
            "category": "eu_mdr/standards",
            "note": "Checks EUR-Lex for new CID amendments to base decision 2021/1182.",
        },
        "mdcg_guidance": {
            "name": "MDCG Guidance Documents (EC Page Scrape)",
            "url": "https://health.ec.europa.eu/medical-devices-sector/new-regulations/guidance-mdcg-endorsed-documents-and-other-guidance_en",
            "check_type": "ec_page_scrape",
            "category": "eu_mdr/mdcg",
        },
        "ec_latest_updates": {
            "name": "EC Medical Devices Latest Updates",
            "url": "https://ec.europa.eu/health/medical-devices-sector/latest-updates_en",
            "check_type": "ec_latest_updates",
            "category": "eu_mdr/regulations",
            "note": "Scrapes EC Medical Devices Latest Updates page for Delegated/Implementing Regulations, policy news.",
        },
        "team_nb": {
            "name": "TEAM-NB Position Papers",
            "url": "https://www.team-nb.org/",
            "check_type": "google_search",
            "category": "eu_mdr/team_nb",
            "google_query": "site:team-nb.org position paper",
            "date_restrict": "y2",
            "title_filter": r"(?i)position\s+paper|guidance\s+note|team[- ]?nb",
        },
    },
    "fda": {
        "guidance_openfda": {
            "name": "FDA Guidance Documents (OpenFDA API)",
            "url": "https://api.fda.gov/other/guidance.json",
            "check_type": "openfda_guidance",
            "category": "fda/guidance",
        },
        "guidance_google": {
            "name": "FDA Medical Device Guidance (Google Search)",
            "url": "https://www.fda.gov/regulatory-information/search-fda-guidance-documents",
            "check_type": "google_search",
            "category": "fda/guidance",
            "google_query": "site:fda.gov/regulatory-information/search-fda-guidance-documents medical device guidance final",
            "date_restrict": "y2",
            "title_filter": r"(?i)guidance|premarket|510\(k\)|PMA|De\s*Novo|cybersecurity|biocompatibility|software|clinical|labeling|UDI",
        },
        "consensus_standards": {
            "name": "FDA Recognized Consensus Standards (Google CSE)",
            "url": "https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfStandards/search.cfm",
            "check_type": "google_search",
            "category": "fda/standards",
            "google_query": "site:accessdata.fda.gov consensus standards recognized medical device",
            "date_restrict": "y2",
            "title_filter": r"(?i)standard|consensus|ISO|IEC|ASTM|AAMI",
        },
        "regulations_ecfr": {
            "name": "FDA 21 CFR Medical Device Parts (eCFR API)",
            "url": "https://www.ecfr.gov/api/versioner/v1/titles.json",
            "check_type": "ecfr_api",
            "category": "fda/regulations",
            "note": "Checks eCFR Versioner API for Title 21 amendment dates, scoped to Parts 800-898.",
        },
        "safety_communications": {
            "name": "FDA Medical Device Safety Communications",
            "url": "https://www.fda.gov/medical-devices/medical-device-safety",
            "check_type": "fda_safety_page",
            "category": "fda/safety",
            "note": "Scrapes FDA Medical Device Safety page for new safety communications.",
        },
        "enforcement_class1": {
            "name": "FDA Class I Device Recalls (OpenFDA Enforcement)",
            "url": "https://api.fda.gov/device/enforcement.json",
            "check_type": "openfda_enforcement",
            "category": "fda/recall",
            "note": "OpenFDA enforcement API, filtered to Class I device recalls only.",
        },
        "cdrh_news": {
            "name": "CDRH News and Updates",
            "url": "https://www.fda.gov/medical-devices/medical-devices-news-and-events/cdrh-new-news-and-updates",
            "check_type": "fda_cdrh_news",
            "category": "fda/cdrh_news",
            "note": "CDRH news page for regulatory announcements, town halls, and policy updates.",
        },
    },
    "nmpa": {
        "cmde_guidance": {
            "name": "CMDE Guidance Principles Index",
            "url": "https://www.cmde.org.cn/flfg/zdyz/",
            "check_type": "google_search",
            "category": "nmpa/guidance",
            "google_query": "site:cmde.org.cn 指导原则 医疗器械",
            "date_restrict": "y1",
            "title_filter": r"(指导原则|技术审查|审查要点|技术指导)",
        },
        "nmpa_regulations": {
            "name": "NMPA Medical Device Regulations (SAMR)",
            "url": "https://www.samr.gov.cn/zw/zfxxgk/fdzdgknr/fgs/",
            "check_type": "google_search",
            "category": "nmpa/regulations",
            "google_query": "site:samr.gov.cn 医疗器械 部门规章",
            "date_restrict": "y1",
            "title_filter": r"(规定|办法|条例|通告|公告|令).{0,30}(医疗器械|体外诊断|器械)",
        },
        "nmpa_announcements": {
            "name": "NMPA Medical Device Announcements",
            "url": "https://www.nmpa.gov.cn/ylqx/ylqxggtg/",
            "check_type": "google_search",
            "category": "nmpa/regulations",
            "google_query": "site:nmpa.gov.cn 医疗器械 公告 通告",
            "date_restrict": "y1",
            "title_filter": r"(医疗器械|体外诊断).{0,20}(公告|通告|通知|决定)",
        },
        "nmpa_standards": {
            "name": "NMPA Medical Device Standards (YY/GB)",
            "url": "https://std.samr.gov.cn",
            "check_type": "google_search",
            "category": "nmpa/standards",
            "google_query": "site:std.samr.gov.cn YY 医疗器械",
            "date_restrict": "y2",
            "title_filter": r"YY[/T\s]*\d{4,5}|GB[/T\s]*\d{4,5}",
        },
    },
    # ----- Tier 1: Core international markets -----
    "uk_mhra": {
        "drug_device_alerts": {
            "name": "MHRA Medical Device Alerts (GOV.UK Atom Feed)",
            "url": "https://www.gov.uk/drug-device-alerts.atom",
            "check_type": "atom_feed",
            "category": "uk_mhra/safety",
            "note": "FSN, safety info, recalls for medical devices in the UK.",
            "title_exclude": r"(?i)(class\s+[1234]\s+(medicines?\s+)?recall|class\s+[1234]\s+(medicines?\s+)?defect|medicines?\s+recall|drug\s+(alert|recall)|tablet[s]?\s+(recall|defect)|capsule[s]?\s+(recall|defect)|injection[s]?\s+(recall|defect|solution|suspension)|oral\s+(solution|suspension)\s+(recall|defect)|vaccine\s+(batch|recall)|pill[s]?\s+recall|pharmaceutical\s+recall|defective\s+medicines?|EL\s*\(\d+\)\s*A/\d+|patient\s+information\s+leaflet|PIL\s+error|barcode\s+error|incorrect\s+PIL|GMP\s+deficien|batch\s+recall.{0,20}(medicine|drug|tablet|capsule|oral)|paracetamol|amoxicillin|ibuprofen|flucloxacillin|gabapentin|mirtazapine|cyclizine|benzylpenicillin|methotrexate|omeprazole|levothyroxine|prednisolone|codeine\s+phosphate|tramadol|diazepam|lorazepam)",
        },
        "mhra_news": {
            "name": "MHRA Regulatory News (GOV.UK)",
            "url": "https://www.gov.uk/government/organisations/medicines-and-healthcare-products-regulatory-agency.atom",
            "check_type": "atom_feed",
            "category": "uk_mhra/regulations",
            "note": "MHRA press releases, guidance updates, consultations.",
            "title_filter": r"(?i)(medical\s+device|device\s+safety|UKCA|conformity|clinical\s+investigation|IVD|SaMD|software|vigilance|field\s+safety|recall|adverse\s+incident|borderline\s+product|exceptional\s+use|registration)",
            "title_exclude": r"(?i)(class\s+[1234]\s+(medicines?\s+)?recall|medicines?\s+recall|drug\s+(alert|recall)|tablet[s]?\s+recall|capsule[s]?\s+recall|pharmaceutical\s+recall|vaccine\s+batch|oral\s+(solution|suspension)\s+recall|EL\s*\(\d+\)\s*A/\d+)",
        },
    },
    "canada": {
        "recalls_safety": {
            "name": "Health Canada Medical Device Recalls & Safety Alerts",
            "url": "https://recalls-rappels.canada.ca/en/search/site?f%5B0%5D=category%3A509",
            "check_type": "canada_recalls",
            "category": "canada/safety",
            "note": "Health Canada medical device recalls and safety alerts.",
        },
        "announcements": {
            "name": "Health Canada Medical Device Announcements",
            "url": "https://www.canada.ca/en/health-canada/services/drugs-health-products/medical-devices/activities/announcements.html",
            "check_type": "generic_page",
            "category": "canada/regulations",
            "title_filter": r"(?i)(medical\s+device|device\s+regulation|device\s+licence|MDEL|guidance|class\s+[IViv]+|recall|safety\s+alert|market\s+authorization)",
            "note": "Health Canada announcements on medical device regulations.",
        },
    },
    "australia_tga": {
        "market_actions_rss": {
            "name": "TGA Market Actions / Recalls (RSS)",
            "url": "https://www.tga.gov.au/feeds/alert/market-actions.xml",
            "check_type": "tga_rss",
            "category": "australia_tga/safety",
            "title_filter": r"(?i)(medical\s+device|device|monitor|pump|catheter|implant|stent|pacemaker|defibrillator|ventilator|glucose|insulin|infusion|surgical|diagnostic|endoscope|prosth|ortho|dental|imaging|MRI|CT\s+scan|ultrasound|IV\s+set|blood|steril|recall|product\s+correction|product\s+alert)",
            "title_exclude": r"(?i)(FDA\s+safety|FDA\s+alert|U\.?S\.?\s+FDA|FDA\s+recall)",
            "max_age_days": 90,
            "note": "Official TGA RSS feed for market actions including medical device recalls.",
        },
        "safety_alerts_rss": {
            "name": "TGA Safety Alerts (RSS)",
            "url": "https://www.tga.gov.au/feeds/alert/safety-alerts.xml",
            "check_type": "tga_rss",
            "category": "australia_tga/safety",
            "title_filter": r"(?i)(medical\s+device|device|implant|surgical|monitor|pump|prosth|ventilator|glucose|blood|recall|product\s+correction|product\s+alert|safety\s+alert|market\s+action)",
            "title_exclude": r"(?i)(FDA\s+safety|FDA\s+alert|U\.?S\.?\s+FDA|FDA\s+recall)",
            "max_age_days": 90,
            "note": "Official TGA RSS feed for safety alerts.",
        },
        "news_rss": {
            "name": "TGA News (RSS)",
            "url": "https://www.tga.gov.au/feeds/article/news.xml",
            "check_type": "tga_rss",
            "category": "australia_tga/regulations",
            "title_filter": r"(?i)(medical\s+device|device|UDI|SaMD|software\s+as|IVD|in\s+vitro|essential\s+principles|classification|implant|clinical\s+evidence|regulation|conformity\s+assessment|artg|post-?market|sponsor|TGA\s+guidance|therapeutic\s+goods)",
            "title_exclude": r"(?i)(FDA\s+safety|FDA\s+alert|U\.?S\.?\s+FDA|FDA\s+recall)",
            "max_age_days": 90,
            "note": "Official TGA RSS feed for news articles, filtered for device-related regulatory news.",
        },
        "regulations_search": {
            "name": "TGA Medical Device Regulatory Updates (Search)",
            "url": "https://www.tga.gov.au/products/medical-devices",
            "check_type": "google_search",
            "google_query": "TGA Australia medical device regulation guidance UDI essential principles classification 2026",
            "category": "australia_tga/regulations",
            "date_restrict": "m6",
            "skip_domain_filter": True,
            "exclude_domains": ["fda.gov", "accessdata.fda.gov", "federalregister.gov"],
            "note": "TGA regulatory updates via search (fallback for RSS).",
        },
    },
    "japan_pmda": {
        "whats_new_en": {
            "name": "PMDA What's New (English) -- Medical Devices & Regulatory",
            "url": "https://www.pmda.go.jp/english/0006.html",
            "check_type": "pmda_whatsnew",
            "category": "japan_pmda/regulations",
            "title_filter": r"(?i)(medical\s+device|device\s+review|device\s+standard|device\s+approval|approved\s+medical\s+device|SaMD|software\s+as\s+a\s+medical|IVD|in\s+vitro|QMS|GCTP|IMDRF|cybersecurity|recall\s+class|UDI|CDx|companion\s+diagnostic|MHLW.*device|medical\s+safety\s+information|safety\s+information\s+no|AI\s+utiliz|program.*medical|classification|clinical\s+trial.*device|post-?market|pre-?market|essential\s+principles|approved\s+.*device|device.*approved|implant|prosth|surgical\s+instrument|therapeutic\s+device|diagnostic\s+device|endoscope|pacemaker|defibrillator)",
            "title_exclude": r"(?i)(approved\s+drugs?$|list\s+of\s+approved\s+drugs|revisions?\s+of\s+precaution|proper\s+use\s+of\s+drugs?|pharmacopoeia|vaccine|drug\s+substance|drug\s+product|prescription\s+drug|adverse\s+drug|anti-?cancer\s+drug|pediatric\s+drug|orphan\s+drug|drug\s+development|drug\s+designation|generic\s+drugs?|review\s+report:\s+(?!.*(?:device|SaMD|IVD|implant|monitor|pump|stent|prosth|ventilator))|urgent\s+safety\s+information.*(?:capsule|tablet|injection|oral|ophthalmic|cream|ointment)|risk\s+commun.*(?:omeprazole|aspirin|warfarin|heparin|insulin$)|orange\s+letter|pharmacovigilance\s+seminar|PDG\s+.*news\s+posted|JP\d+|japanese\s+pharmacopoeia|GCP\s+workshop|GMP\s+(?:inspection|workshop)(?!.*device)|副作用|使用上の注意)",
            "note": "Primary: PMDA English What's New page. title_filter includes device keywords; title_exclude rejects drug-only content.",
        },
        "recalls_class1": {
            "name": "PMDA Medical Device Recalls Class I (Japanese)",
            "url": "https://www.info.pmda.go.jp/kaisyuu/rcidx{yy}-1k.html",
            "check_type": "pmda_recalls",
            "category": "japan_pmda/safety",
            "recall_class": "I",
            "dynamic_year": True,
            "note": "PMDA Class I medical device recalls (serious health risk).",
        },
        "recalls_class2": {
            "name": "PMDA Medical Device Recalls Class II (Japanese)",
            "url": "https://www.info.pmda.go.jp/kaisyuu/rcidx{yy}-2k.html",
            "check_type": "pmda_recalls",
            "category": "japan_pmda/safety",
            "recall_class": "II",
            "dynamic_year": True,
            "note": "PMDA Class II medical device recalls.",
        },
        "device_regulatory_search": {
            "name": "PMDA Medical Device Regulatory Updates (Search)",
            "url": "https://www.pmda.go.jp/english/review-services/reviews/0002.html",
            "check_type": "google_search",
            "google_query": "PMDA Japan medical device regulation guidance QMS SaMD software IVD IMDRF device classification approval review 2026",
            "category": "japan_pmda/regulations",
            "date_restrict": "m3",
            "skip_domain_filter": True,
            "exclude_domains": ["fda.gov", "accessdata.fda.gov"],
            "note": "PMDA medical device regulatory updates via search (supplements What's New).",
        },
    },
    "korea_mfds": {
        "news_en": {
            "name": "MFDS General News (English, filtered for medical devices)",
            "url": "https://www.mfds.go.kr/eng/brd/m_61/list.do",
            "check_type": "mfds_page",
            "category": "korea_mfds/regulations",
            "title_filter": r"(?i)(medical\s+device|device\s+approval|medical\s+product|GMP|KGMP|DMPA|digital\s+medical|IVD|in\s+vitro|SaMD|software\s+as|UDI|clinical\s+trial|pre-?market|post-?market|approval\s+(report|review)|240.?day)",
            "note": "MFDS English general news filtered for medical devices only.",
        },
        "md_regulations": {
            "name": "MFDS Medical Device Regulations (English)",
            "url": "https://www.mfds.go.kr/eng/brd/m_40/list.do",
            "check_type": "mfds_page",
            "category": "korea_mfds/regulations",
            "note": "MFDS medical device regulations, guidance, GMP standards.",
        },
        "md_products": {
            "name": "MFDS Medical Device Products & Approvals (English)",
            "url": "https://www.mfds.go.kr/eng/brd/m_41/list.do",
            "check_type": "mfds_page",
            "category": "korea_mfds/regulations",
            "title_filter": r"(?i)(medical\s+device|device\s+approval|approval\s+report|innovative|SaMD|AI|machine\s+learning|digital\s+health)",
            "note": "MFDS medical device product approvals and reports.",
        },
        "md_innovative": {
            "name": "MFDS Innovative Medical Devices Designation (English)",
            "url": "https://www.mfds.go.kr/eng/brd/m_1135/list.do",
            "check_type": "mfds_page",
            "category": "korea_mfds/regulations",
            "note": "MFDS innovative medical device designations.",
        },
        "md_search": {
            "name": "Korea Medical Device Regulatory News (via Search)",
            "url": "https://www.mfds.go.kr/eng/index.do",
            "check_type": "google_search",
            "google_query": "Korea MFDS medical device regulation approval KGMP guidance update 2026",
            "category": "korea_mfds/regulations",
            "date_restrict": "m6",
            "skip_domain_filter": True,
            "title_filter": r"(?i)(Korea|MFDS|KFDA|KGMP|Korean|KR).*(medical\s+device|device|GMP|regulation|approval|guidance)",
            "note": "Korean medical device regulation news via web search.",
        },
    },
    # --- Tier 2 countries (Phase 3b) ---
    "switzerland": {
        "fsca": {
            "name": "Swissmedic FSCA (Medical Device Field Safety Corrective Actions)",
            "url": "https://fsca.swissmedic.ch/mep/api/publications/export",
            "check_type": "swissmedic_csv",
            "category": "switzerland/safety",
            "device_only": True,
            "note": "Swissmedic FSCA export CSV API - structured medical device recalls/corrections.",
        },
    },
    "brazil_anvisa": {
        "tecnovigilance": {
            "name": "ANVISA Medical Device Tecnovigilance Alerts (Direct)",
            "url": "https://antigo.anvisa.gov.br/alertas?tagsName=tecnovigil%C3%A2ncia",
            "check_type": "anvisa_page",
            "category": "brazil_anvisa/safety",
            "note": "Direct HTML parsing of ANVISA tecnovigilancia alerts page (Portuguese).",
        },
        "regulations": {
            "name": "ANVISA Medical Device Regulations (via Search)",
            "url": "https://www.gov.br/anvisa/pt-br/assuntos/produtos-para-a-saude",
            "check_type": "google_search",
            "google_query": "ANVISA Brazil medical device regulation RDC guidance GMP certification 2026",
            "category": "brazil_anvisa/regulations",
            "date_restrict": "m6",
            "skip_domain_filter": True,
            "note": "ANVISA medical device regulations via search.",
        },
    },
    "saudi_sfda": {
        "weekly_alerts": {
            "name": "SFDA NCMDR Weekly Medical Device Safety Reports",
            "url": "https://www.sfda.gov.sa/en/weekly-alert",
            "check_type": "sfda_weekly",
            "category": "saudi_sfda/safety",
            "note": "Saudi FDA weekly medical device safety reports (PDF reports listed on page).",
        },
        "device_news_rss": {
            "name": "SFDA Medical Devices Sector News (RSS)",
            "url": "https://www.sfda.gov.sa/en/news.xml?tags=3",
            "check_type": "sfda_rss",
            "check_sub": "rss",
            "category": "saudi_sfda/regulations",
            "title_filter": r"(?i)(medical\s+device|device|مستلزمات|equipment|MDMA|MDS|regulation|recall|safety)",
            "note": "SFDA RSS for medical device sector news (filtered from general RSS).",
        },
    },
    "singapore_hsa": {
        "device_safety": {
            "name": "HSA Medical Device Safety (via Search)",
            "url": "https://www.hsa.gov.sg/medical-devices",
            "check_type": "google_search",
            "google_query": "Singapore HSA medical device recall FSCA safety alert corrective action 2026",
            "category": "singapore_hsa/safety",
            "date_restrict": "m6",
            "skip_domain_filter": True,
            "note": "HSA medical device safety via search (direct 403).",
        },
        "regulations": {
            "name": "HSA Medical Device Regulatory Updates (via Search)",
            "url": "https://www.hsa.gov.sg/medical-devices/guidance-documents/",
            "check_type": "google_search",
            "google_query": "Singapore HSA medical device guidance regulation registration GN class 2026",
            "category": "singapore_hsa/regulations",
            "date_restrict": "m6",
            "skip_domain_filter": True,
            "note": "HSA medical device regulatory guidance via search.",
        },
    },
    "india_cdsco": {
        "device_alerts": {
            "name": "CDSCO Medical Device Alerts (via Search)",
            "url": "https://cdsco.gov.in/opencms/opencms/en/Medical-Device-Diagnostics/",
            "check_type": "google_search",
            "google_query": "site:cdsco.gov.in medical device alert recall safety",
            "category": "india_cdsco/safety",
            "date_restrict": "m6",
            "skip_domain_filter": True,
            "note": "CDSCO medical device alerts via search (direct 403).",
        },
        "regulations": {
            "name": "CDSCO Medical Device Regulations (via Search)",
            "url": "https://cdsco.gov.in/opencms/opencms/en/Medical-Device-Diagnostics/",
            "check_type": "google_search",
            "google_query": "CDSCO India medical device regulation notification MDR 2017 amendment 2026",
            "category": "india_cdsco/regulations",
            "date_restrict": "m6",
            "skip_domain_filter": True,
            "note": "CDSCO medical device regulations via search.",
        },
    },
    # -----------------------------------------------------------------------
    # Tier 3: Supplementary markets (monthly updates)
    # -----------------------------------------------------------------------
    "mexico_cofepris": {
        "safety_alerts": {
            "name": "COFEPRIS Medical Device Safety Alerts (Mexico)",
            "url": "https://www.gob.mx/cofepris/acciones-y-programas/alertas-sanitarias",
            "check_type": "google_search",
            "google_query": "COFEPRIS Mexico dispositivo medico alerta sanitaria retiro recall medical device 2026",
            "category": "mexico_cofepris/safety",
            "date_restrict": "m6",
            "skip_domain_filter": True,
            "note": "COFEPRIS medical device safety alerts via search (Spanish content + LLM).",
        },
    },
    "argentina_anmat": {
        "safety_alerts": {
            "name": "ANMAT Medical Device Safety Alerts (Argentina)",
            "url": "https://www.argentina.gob.ar/anmat/alertas",
            "check_type": "google_search",
            "google_query": "ANMAT Argentina dispositivo medico alerta retiro producto medico recall 2026",
            "category": "argentina_anmat/safety",
            "date_restrict": "m6",
            "skip_domain_filter": True,
            "note": "ANMAT medical device safety alerts via search (Spanish content + LLM).",
        },
    },
    "taiwan_tfda": {
        "safety_alerts": {
            "name": "TFDA Medical Device Safety Alerts (Taiwan)",
            "url": "https://www.fda.gov.tw/TC/site.aspx?sid=7383",
            "check_type": "google_search",
            "google_query": "site:fda.gov.tw OR site:tdrf.org.tw medical device recall safety alert warning 2026",
            "category": "taiwan_tfda/safety",
            "date_restrict": "m6",
            "skip_domain_filter": True,
            "note": "TFDA medical device safety alerts via search (Chinese + English content).",
        },
    },
    "newzealand_medsafe": {
        "safety_comms": {
            "name": "Medsafe Safety Communications (New Zealand)",
            "url": "https://medsafe.govt.nz/safety/SafetyCommunications.asp",
            "check_type": "medsafe_page",
            "category": "newzealand_medsafe/safety",
            "note": "Direct HTML parsing of Medsafe Safety Communications table (device-filtered).",
        },
    },
    "indonesia_bpom": {
        "device_safety": {
            "name": "BPOM/Kemenkes Medical Device Alerts (Indonesia)",
            "url": "https://www.pom.go.id/",
            "check_type": "google_search",
            "google_query": "Indonesia BPOM Kemenkes medical device alat kesehatan recall safety alert 2026",
            "category": "indonesia_bpom/safety",
            "date_restrict": "m6",
            "skip_domain_filter": True,
            "note": "Indonesian medical device alerts via search (Bahasa + English).",
        },
    },
    "malaysia_mda": {
        "device_safety": {
            "name": "MDA Medical Device Safety (Malaysia)",
            "url": "https://www.mda.gov.my/",
            "check_type": "google_search",
            "google_query": "site:mda.gov.my medical device recall FSCA safety alert guidance 2026",
            "category": "malaysia_mda/safety",
            "date_restrict": "m6",
            "skip_domain_filter": True,
            "note": "MDA Malaysia medical device safety via search (English).",
        },
    },
    "thailand_fda": {
        "device_safety": {
            "name": "Thai FDA Medical Device Alerts (Thailand)",
            "url": "https://www.fda.moph.go.th/",
            "check_type": "google_search",
            "google_query": "Thailand FDA medical device recall safety alert FSCA regulation 2026",
            "category": "thailand_fda/safety",
            "date_restrict": "m6",
            "skip_domain_filter": True,
            "note": "Thai FDA medical device alerts via search (Thai + English).",
        },
    },
    "israel_moh": {
        "device_safety": {
            "name": "Israel MOH Medical Device Alerts",
            "url": "https://www.health.gov.il/English/",
            "check_type": "google_search",
            "google_query": "Israel Ministry Health medical device recall FSCA safety alert regulation 2026",
            "category": "israel_moh/safety",
            "date_restrict": "m6",
            "skip_domain_filter": True,
            "note": "Israel MOH medical device alerts via search (English).",
        },
    },
    "hongkong_mdco": {
        "device_safety": {
            "name": "Hong Kong MDCO Medical Device Safety",
            "url": "https://www.mdco.gov.hk/",
            "check_type": "google_search",
            "google_query": "Hong Kong MDCO medical device recall safety alert regulation 2026",
            "category": "hongkong_mdco/safety",
            "date_restrict": "m6",
            "skip_domain_filter": True,
            "note": "HK MDCO medical device safety via search (English/Chinese).",
        },
    },
    "shared": {
        "iso_tc210": {
            "name": "ISO TC 210 Medical Device Standards",
            "url": "https://www.iso.org/committee/54892/x/catalogue/",
            "check_type": "google_search",
            "category": "_shared/standards",
            "google_query": "site:iso.org 13485 OR 14971 OR 62304 OR 10993 medical device",
            "date_restrict": "y2",
            "title_filter": r"ISO\s+\d{4,5}|IEC\s+\d{4,5}",
        },
        "iec_tc62": {
            "name": "IEC TC 62 Medical Electrical Equipment Standards",
            "url": "https://www.iec.ch/dyn/www/f?p=103:7:::::FSP_ORG_ID:1245",
            "check_type": "google_search",
            "category": "_shared/standards",
            "google_query": "site:iec.ch 60601 OR 62133 medical device standard",
            "date_restrict": "y2",
            "title_filter": r"IEC\s+\d{4,5}|ISO\s+\d{4,5}",
        },
    },
}

# Medical device eCFR parts (800-898)
ECFR_MD_PARTS = set(range(800, 899))


# ---------------------------------------------------------------------------
# Version Registry
# ---------------------------------------------------------------------------

class VersionRegistry:
    """Tracks version history for all regulatory documents."""

    def __init__(self, path: Path = VERSION_REGISTRY_PATH):
        self.path = path
        self.data = self._load()

    def _load(self) -> dict:
        if self.path.exists():
            try:
                with open(self.path, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                pass
        return {"documents": {}, "last_updated": None}

    def save(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.data["last_updated"] = datetime.now().isoformat()
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)

    def get(self, doc_id: str) -> Optional[dict]:
        return self.data["documents"].get(doc_id)

    def upsert(self, doc_id: str, current: dict):
        existing = self.data["documents"].get(doc_id, {})
        history = existing.get("history", [])
        if existing.get("current"):
            history.append(existing["current"])
        self.data["documents"][doc_id] = {"current": current, "history": history}

    def find_outdated(self, days: int = 180) -> list:
        cutoff = datetime.now() - timedelta(days=days)
        result = []
        for doc_id, doc in self.data["documents"].items():
            lv = doc.get("current", {}).get("last_verified")
            if lv:
                try:
                    if datetime.fromisoformat(lv) < cutoff:
                        result.append(doc_id)
                except Exception:
                    pass
        return result


# ---------------------------------------------------------------------------
# Database Comparator -- compares detections against existing _index.json
# ---------------------------------------------------------------------------

class DatabaseComparator:
    """Loads all _index.json files and version_registry.json to classify detections."""

    def __init__(self, root: Path = ROOT):
        self.root = root
        self.mdcg_ids: set[str] = set()
        self.mdcg_titles: set[str] = set()
        self.standards_latest_amendment: str = ""
        self.eu_reg_ids: set[str] = set()
        self.nmpa_reg_titles: set[str] = set()
        self.nmpa_guidance_titles: set[str] = set()
        self.fda_guidance_titles: set[str] = set()
        self.fda_guidance_ids: set[str] = set()
        self.db_stats: dict[str, dict] = {}
        self._load_all()

    def _load_json(self, path: Path) -> dict:
        if not path.exists():
            return {}
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}

    def _load_all(self):
        mdcg = self._load_json(self.root / "eu_mdr" / "mdcg" / "_index.json")
        for entry in mdcg.get("entries", []):
            eid = entry.get("id", "")
            self.mdcg_ids.add(eid)
            for lang in ("zh", "en"):
                t = (entry.get("title") or {}).get(lang, "")
                if t:
                    self.mdcg_titles.add(t.strip().lower())
        self._mdcg_entries = mdcg.get("entries", [])
        self.db_stats["eu_mdr/mdcg"] = {"count": len(self.mdcg_ids)}

        stds = self._load_json(self.root / "eu_mdr" / "standards" / "_index.json")
        self.standards_latest_amendment = stds.get("latest_amendment", "")
        self.db_stats["eu_mdr/standards"] = {
            "count": stds.get("total_standards", 0),
            "latest_amendment": self.standards_latest_amendment,
        }

        regs = self._load_json(self.root / "eu_mdr" / "regulations" / "_index.json")
        for doc in regs.get("documents", []):
            self.eu_reg_ids.add(doc.get("id", ""))
        self.db_stats["eu_mdr/regulations"] = {"count": len(self.eu_reg_ids)}

        nmpa_reg = self._load_json(self.root / "nmpa" / "regulations" / "_index.json")
        for entry in nmpa_reg.get("entries", []):
            t = (entry.get("title") or {}).get("zh", "")
            if t:
                self.nmpa_reg_titles.add(t.strip())
        self.db_stats["nmpa/regulations"] = {"count": len(self.nmpa_reg_titles)}

        nmpa_guide = self._load_json(self.root / "nmpa" / "guidance" / "_index.json")
        for entry in nmpa_guide.get("entries", []):
            t = (entry.get("title") or {}).get("zh", "")
            if t:
                self.nmpa_guidance_titles.add(t.strip())
        self.db_stats["nmpa/guidance"] = {"count": len(self.nmpa_guidance_titles)}

        vreg = self._load_json(self.root / "scripts" / "version_registry.json")
        for doc_id, doc in vreg.get("documents", {}).items():
            cur = doc.get("current", {})
            title = cur.get("title", "")
            if title and "fda" in doc_id.lower():
                self.fda_guidance_titles.add(title.strip().lower())
                self.fda_guidance_ids.add(doc_id)
        self.db_stats["fda/guidance"] = {"count": len(self.fda_guidance_titles)}

    def classify(self, category: str, title: str, link: str = "", date: str = "") -> tuple[str, str]:
        """Classify a detection against the database.

        Returns: ('new', description) | ('update', diff) | ('known', '') | ('irrelevant', reason)
        """
        title_lower = title.strip().lower()

        if category == "eu_mdr/mdcg":
            mdcg_match = re.search(r"MDCG\s+(20\d{2}[-/]\d+)", title, re.IGNORECASE)
            if not mdcg_match:
                return ("irrelevant", "No MDCG ID pattern in title")
            mdcg_id = mdcg_match.group(1).replace("/", "-")
            normalized = f"mdcg-{mdcg_id}"

            # Check for revision indicator attached to THIS MDCG document
            # Only match rev.X that appears near the MDCG ID (within ~30 chars),
            # NOT revision markers belonging to other referenced documents
            # e.g. "MDCG 2021-24 Rev.1" -> rev.1 (correct)
            # e.g. "...MDCG 2020-6 and MEDDEV 2.7/1 rev.4..." -> ignore rev.4
            mdcg_end = mdcg_match.end()
            nearby_text = title[mdcg_end:mdcg_end + 30]
            rev_match = re.search(r"^\s*[-–/]?\s*[Rr]ev[\.\s]*(\d+)", nearby_text)
            new_rev = rev_match.group(0).strip() if rev_match else ""

            if normalized in self.mdcg_ids or f"MDCG {mdcg_id}" in self.mdcg_ids:
                if new_rev:
                    # Search result mentions a revision -- check if our DB already has it
                    db_entry = next(
                        (e for e in self._mdcg_entries if e.get("id") == normalized), None
                    )
                    db_rev = ""
                    if db_entry:
                        db_rev = db_entry.get("revision", "")
                        for lang in ("zh", "en"):
                            t = (db_entry.get("title") or {}).get(lang, "")
                            if t and not db_rev:
                                rm = re.search(r"[Rr]ev[\.\s]*(\d+)", t)
                                if rm:
                                    db_rev = rm.group(0).strip()
                    if db_rev and db_rev.lower().replace(" ", "") == new_rev.lower().replace(" ", ""):
                        return ("known", "")
                    return ("update", f"Revision update: {normalized} has {new_rev} (DB: {db_rev or 'original'})")
                return ("known", "")
            return ("new", f"New MDCG document: {mdcg_match.group(0)}")

        elif category == "eu_mdr/standards":
            cid_match = re.search(r"20\d{2}/\d+", title)
            if cid_match:
                cid = cid_match.group(0)
                if self.standards_latest_amendment and cid > self.standards_latest_amendment:
                    return ("update", f"New amendment {cid} (DB latest: {self.standards_latest_amendment})")
                return ("known", "")
            return ("irrelevant", "No CID amendment number found")

        elif category == "nmpa/regulations":
            for known in self.nmpa_reg_titles:
                if known in title or title in known:
                    return ("known", "")
            return ("new", f"Potentially new NMPA regulation")

        elif category == "nmpa/guidance":
            for known in self.nmpa_guidance_titles:
                if known in title or title in known:
                    return ("known", "")
            return ("new", f"Potentially new NMPA guidance")

        elif category == "fda/guidance":
            for known in self.fda_guidance_titles:
                if known in title_lower or title_lower in known:
                    return ("known", "")
            return ("new", f"Potentially new FDA guidance")

        elif category in ("_shared/standards", "fda/standards", "nmpa/standards"):
            std_match = re.search(r"(ISO|IEC|ASTM|AAMI|YY|GB)\s*[/T]*\s*(\d{4,5})", title, re.IGNORECASE)
            if not std_match:
                return ("irrelevant", "No standard number pattern found")
            return ("new", f"Standard reference: {std_match.group(0)}")

        return ("new", "Unclassified category")

    def get_stats(self) -> dict:
        return dict(self.db_stats)


# ---------------------------------------------------------------------------
# Layer 2: HTTP ETag/Last-Modified checker (kept for backward compat)
# ---------------------------------------------------------------------------

class HTTPChecker:
    def __init__(self, session: requests.Session, state: dict):
        self.session = session
        self.state = state

    def check(self, source_id: str, source: dict) -> Optional[dict]:
        url = source["url"]
        prev = self.state.get(source_id, {})
        headers = {}
        if prev.get("etag"):
            headers["If-None-Match"] = prev["etag"]
        if prev.get("last_modified"):
            headers["If-Modified-Since"] = prev["last_modified"]
        try:
            resp = self.session.head(url, headers=headers, timeout=15, allow_redirects=True)
            new_state = {"url": url, "last_checked": datetime.now().isoformat(),
                         "status_code": resp.status_code}
            if resp.headers.get("ETag"):
                new_state["etag"] = resp.headers["ETag"]
            if resp.headers.get("Last-Modified"):
                new_state["last_modified"] = resp.headers["Last-Modified"]
            self.state[source_id] = new_state
            if resp.status_code == 304:
                return None
            elif resp.status_code == 200:
                if prev.get("etag") and new_state.get("etag") == prev["etag"]:
                    return None
                return _make_update(source_id, source, "http_head",
                                    "Page may have been updated - manual review required")
            else:
                print(f"    WARNING: HTTP {resp.status_code}")
                return None
        except requests.RequestException as e:
            print(f"    ERROR: {e}")
            return None


# ---------------------------------------------------------------------------
# Layer 1: RSS Feed checker
# ---------------------------------------------------------------------------

class RSSChecker:
    def __init__(self, session: requests.Session, state: dict,
                 seed_mode: bool = False):
        self.session = session
        self.state = state
        self.seed_mode = seed_mode

    def check(self, source_id: str, source: dict) -> Optional[dict]:
        url = source["url"]
        prev = self.state.get(source_id, {})
        last_checked = prev.get("last_checked")
        try:
            resp = self.session.get(url, timeout=30)
            resp.raise_for_status()
            root = ET.fromstring(resp.content)
            new_items = []
            for item in root.findall(".//item")[:20]:
                pub_date_el = item.find("pubDate")
                title_el = item.find("title")
                link_el = item.find("link")
                desc_el = item.find("description")
                if pub_date_el is not None and last_checked:
                    try:
                        pub_dt = parsedate_to_datetime(pub_date_el.text)
                        last_dt = datetime.fromisoformat(last_checked)
                        if pub_dt.timestamp() <= last_dt.timestamp():
                            continue
                    except Exception:
                        pass
                title = title_el.text if title_el is not None else "Unknown"
                link = link_el.text if link_el is not None else ""
                desc = (desc_el.text or "") if desc_el is not None else ""
                if last_checked is None or "final" in title.lower() or "final" in desc.lower():
                    new_items.append({"title": title, "link": link,
                                      "pub_date": pub_date_el.text if pub_date_el is not None else "",
                                      "description": desc[:300]})
            self.state[source_id] = {"url": url, "last_checked": datetime.now().isoformat()}
            if new_items:
                result = _make_update(source_id, source, "rss",
                                      f"{len(new_items)} new Final guidance item(s) in RSS")
                result["new_items"] = new_items
                return result
            return None
        except Exception as e:
            print(f"    ERROR RSS: {e}")
            return None


# ---------------------------------------------------------------------------
# Layer 3: Google Custom Search API (bypasses anti-scraping)
# Mirrors Clin_Eva_Agent/tools/google_search_tool.py pattern
# Free quota: 100 queries/day - sufficient for weekly batched checks
# ---------------------------------------------------------------------------

class GoogleSearchChecker:
    BASE_URL = "https://www.googleapis.com/customsearch/v1"

    def __init__(self, api_key: str, engine_id: str, state: dict,
                 seed_mode: bool = False):
        self.api_key = api_key
        self.engine_id = engine_id
        self.state = state
        self.seed_mode = seed_mode
        self.available = bool(api_key and engine_id)

    def search(self, query: str, num: int = 10,
               date_restrict: str = "") -> list:
        """Search via Google CSE API.

        Args:
            date_restrict: Google CSE dateRestrict value, e.g. "y2" (past 2 years),
                "m6" (past 6 months), "w4" (past 4 weeks), "d30" (past 30 days).
                When set, filters results by page indexing date -- no hardcoded
                year strings needed in the query.
        """
        if not self.available:
            return []
        try:
            params = {
                "key": self.api_key, "cx": self.engine_id,
                "q": query, "num": min(num, 10), "sort": "date",
            }
            if date_restrict:
                params["dateRestrict"] = date_restrict
            resp = requests.get(self.BASE_URL, params=params, timeout=15)
            resp.raise_for_status()
            return resp.json().get("items", [])
        except Exception as e:
            print(f"    ERROR Google Search: {e}")
            return []

    def check(self, source_id: str, source: dict) -> Optional[dict]:
        query = source.get("google_query")
        if not query or not self.available:
            if not self.available:
                print(f"    SKIP (Google CSE not configured)")
            return None
        title_filter = source.get("title_filter")
        prev = self.state.get(source_id, {})
        prev_titles = set(prev.get("seen_titles", []))
        date_restrict = source.get("date_restrict", "")
        items = self.search(query, date_restrict=date_restrict)
        new_items = []
        filtered_count = 0
        all_titles = list(prev_titles)
        for item in items:
            title = item.get("title", "")
            if title_filter and not re.search(title_filter, title, re.IGNORECASE):
                filtered_count += 1
                continue
            if title not in prev_titles:
                new_items.append({"title": title, "link": item.get("link", ""),
                                  "snippet": item.get("snippet", "")[:200]})
                all_titles.append(title)
        if filtered_count:
            print(f"    INFO: {filtered_count} results filtered by title_filter")
        self.state[source_id] = {"url": source["url"],
                                  "last_checked": datetime.now().isoformat(),
                                  "seen_titles": all_titles[-100:]}
        if new_items and (prev_titles or self.seed_mode):
            if self.seed_mode and not prev_titles:
                new_items = new_items[:10]
                print(f"    INFO: Seed mode -- returning top {len(new_items)} results as initial news")
            result = _make_update(source_id, source, "google_search",
                                  f"{len(new_items)} new result(s) via Google Search")
            result["new_items"] = new_items
            result["query"] = query
            return result
        elif not prev_titles:
            print(f"    INFO: Baseline established ({len(items)} results indexed)")
        return None


# ---------------------------------------------------------------------------
# Layer 3b: Vertex AI Search (searchLite API) -- replaces Google CSE
# Uses API Key auth via searchLite endpoint; domains restricted by data store.
# Free tier: 10,000 queries/month (our weekly cron uses ~44/month).
# Docs: https://docs.cloud.google.com/generative-ai-app-builder/docs/migrate-from-cse
# ---------------------------------------------------------------------------

class VertexAISearchChecker:
    SEARCHLITE_URL = (
        "https://discoveryengine.googleapis.com/v1/projects/{project_id}"
        "/locations/global/collections/default_collection"
        "/engines/{app_id}/servingConfigs/default_search:searchLite"
    )

    def __init__(self, project_id: str, app_id: str, api_key: str, state: dict,
                 seed_mode: bool = False):
        self.project_id = project_id
        self.app_id = app_id
        self.api_key = api_key
        self.state = state
        self.seed_mode = seed_mode
        self.available = bool(project_id and app_id and api_key)

    def search(self, query: str, num: int = 10) -> list:
        if not self.available:
            return []
        url = self.SEARCHLITE_URL.format(
            project_id=self.project_id, app_id=self.app_id,
        )
        try:
            resp = requests.post(
                url,
                params={"key": self.api_key},
                json={
                    "query": query,
                    "pageSize": min(num, 25),
                },
                headers={"Content-Type": "application/json"},
                timeout=20,
            )
            if resp.status_code != 200:
                body = resp.text[:300] if resp.text else "(empty)"
                print(f"    ERROR Vertex AI Search HTTP {resp.status_code}: {body}")
                return []
            data = resp.json()
            results = []
            for r in data.get("results", []):
                doc = r.get("document", {})
                derived = doc.get("derivedStructData", {})
                link = derived.get("link", "")
                title = derived.get("title", "")
                snippet = ""
                for s in derived.get("snippets", []):
                    if s.get("snippet"):
                        snippet = re.sub(r"<[^>]+>", "", s["snippet"])
                        break
                if title or link:
                    results.append({
                        "title": title,
                        "link": link,
                        "snippet": snippet[:200],
                    })
            return results
        except Exception as e:
            print(f"    ERROR Vertex AI Search: {e}")
            return []

    @staticmethod
    def _extract_site_domain(query: str) -> Optional[str]:
        """Extract domain from 'site:domain.com' in query, if present."""
        m = re.search(r"site:(\S+)", query)
        return m.group(1) if m else None

    def _filter_items(self, items: list, prev_titles: set,
                       site_domain: Optional[str], title_filter: Optional[str],
                       exclude_domains: Optional[list] = None,
                       ) -> tuple:
        """Filter search results, return (new_items, domain_filtered, title_filtered)."""
        new_items = []
        domain_filtered = 0
        title_filtered = 0
        excluded_count = 0
        for item in items:
            title = item.get("title", "")
            link = item.get("link", "")
            if site_domain and link and site_domain not in link:
                domain_filtered += 1
                continue
            if exclude_domains and link:
                link_lower = link.lower()
                if any(d in link_lower for d in exclude_domains):
                    excluded_count += 1
                    print(f"      EXCLUDED (blocked domain): {link[:80]}")
                    continue
            if title_filter and not re.search(title_filter, title, re.IGNORECASE):
                title_filtered += 1
                continue
            if title not in prev_titles:
                new_items.append({"title": title, "link": link,
                                  "snippet": item.get("snippet", "")[:200]})
        if excluded_count:
            print(f"    INFO: {excluded_count} results excluded by domain blocklist")
        return new_items, domain_filtered, title_filtered

    def check(self, source_id: str, source: dict) -> Optional[dict]:
        query = source.get("google_query")
        if not query or not self.available:
            if not self.available:
                print(f"    SKIP (Vertex AI Search not configured)")
            return None
        skip_domain = source.get("skip_domain_filter", False)
        site_domain = None if skip_domain else self._extract_site_domain(query)
        title_filter = source.get("title_filter")
        exclude_domains = source.get("exclude_domains")
        prev = self.state.get(source_id, {})
        prev_titles = set(prev.get("seen_titles", []))

        items = self.search(query)
        new_items, domain_filtered, tf_count = self._filter_items(
            items, prev_titles, site_domain, title_filter, exclude_domains)

        if not new_items and domain_filtered > 0 and site_domain:
            fallback_query = re.sub(r"site:\S+\s*", "", query).strip()
            print(f"    INFO: {domain_filtered} results from wrong domain; "
                  f"retrying without site: prefix")
            items = self.search(fallback_query)
            new_items, domain_filtered, tf_count = self._filter_items(
                items, prev_titles, site_domain, title_filter, exclude_domains)

        if domain_filtered:
            print(f"    INFO: {domain_filtered} results filtered by domain ({site_domain})")
        if tf_count:
            print(f"    INFO: {tf_count} results filtered by title_filter")

        all_titles = list(prev_titles) + [i["title"] for i in new_items]
        self.state[source_id] = {"url": source["url"],
                                  "last_checked": datetime.now().isoformat(),
                                  "seen_titles": all_titles[-100:]}
        if new_items and (prev_titles or self.seed_mode):
            if self.seed_mode and not prev_titles:
                new_items = new_items[:10]
                print(f"    INFO: Seed mode -- returning top {len(new_items)} results as initial news")
            result = _make_update(source_id, source, "vertex_ai_search",
                                  f"{len(new_items)} new result(s) via Vertex AI Search")
            result["new_items"] = new_items
            result["query"] = query
            return result
        elif not prev_titles:
            if not new_items and items:
                print(f"    INFO: All {len(items)} results filtered out (domain/title mismatch)")
            else:
                print(f"    INFO: Baseline established ({len(items)} results indexed)")
        return None


# ---------------------------------------------------------------------------
# Bonus: OpenFDA API checker
# Based on Clin_Eva_Agent/tools/fda_510k_tool.py pattern
# FDA_API_KEY raises rate limit; works without key too (lower quota)
# ---------------------------------------------------------------------------

class OpenFDAChecker:
    GUIDANCE_URL = "https://api.fda.gov/other/guidance.json"

    def __init__(self, api_key: str, state: dict):
        self.api_key = api_key
        self.state = state

    def check(self, source_id: str, source: dict) -> Optional[dict]:
        prev = self.state.get(source_id, {})
        last_checked = prev.get("last_checked")
        date_filter = ""
        if last_checked:
            try:
                dt = datetime.fromisoformat(last_checked)
                date_filter = f"+AND+effective_date:[{dt.strftime('%Y%m%d')}+TO+*]"
            except Exception:
                pass
        params = {
            "search": f'product_type:"DEVICE"+AND+status:"Final"{date_filter}',
            "limit": 20, "sort": "effective_date:desc",
        }
        if self.api_key:
            params["api_key"] = self.api_key
        try:
            resp = requests.get(self.GUIDANCE_URL, params=params, timeout=20)
            if resp.status_code == 404:
                self.state[source_id] = {"last_checked": datetime.now().isoformat()}
                return None
            resp.raise_for_status()
            results = resp.json().get("results", [])
            self.state[source_id] = {"last_checked": datetime.now().isoformat()}
            if not results:
                return None
            new_items = []
            for r in results:
                doc_id = r.get("id", "")
                url = r.get("url", "") or (
                    f"https://www.fda.gov/regulatory-information/"
                    f"search-fda-guidance-documents/{doc_id}" if doc_id else "")
                new_items.append({"title": r.get("title", ""), "link": url,
                                  "pub_date": r.get("effective_date", ""), "doc_id": doc_id})
            result = _make_update(source_id, source, "openfda_guidance",
                                  f"{len(new_items)} new/updated FDA Final guidance via OpenFDA API")
            result["new_items"] = new_items
            return result
        except Exception as e:
            print(f"    ERROR OpenFDA: {e}")
            return None


# ---------------------------------------------------------------------------
# eCFR Versioner API checker (replaces http_head for Title 21)
# Public API, no key needed: https://www.ecfr.gov/api/versioner/v1/titles.json
# ---------------------------------------------------------------------------

class ECFRChecker:
    TITLES_URL = "https://www.ecfr.gov/api/versioner/v1/titles.json"

    def __init__(self, session: requests.Session, state: dict):
        self.session = session
        self.state = state

    def check(self, source_id: str, source: dict) -> Optional[dict]:
        prev = self.state.get(source_id, {})
        last_amendment_date = prev.get("last_amendment_date", "")
        try:
            resp = self.session.get(self.TITLES_URL, timeout=15)
            resp.raise_for_status()
            titles = resp.json().get("titles", [])
            title21 = None
            for t in titles:
                if t.get("number") == 21:
                    title21 = t
                    break
            if not title21:
                return None
            new_date = title21.get("latest_amended_on", "") or title21.get("up_to_date_as_of", "")
            self.state[source_id] = {
                "url": source["url"],
                "last_checked": datetime.now().isoformat(),
                "last_amendment_date": new_date,
            }
            if not last_amendment_date:
                print(f"    INFO: eCFR baseline established (Title 21 last amended: {new_date})")
                return None
            if new_date and new_date > last_amendment_date:
                return _make_update(
                    source_id, source, "ecfr_api",
                    f"Title 21 CFR updated: {last_amendment_date} -> {new_date} (medical device Parts 800-898 may be affected)"
                )
            return None
        except Exception as e:
            print(f"    ERROR eCFR API: {e}")
            return None


# ---------------------------------------------------------------------------
# Layer 5: EC MDCG Page Scraper -- direct HTML parsing for full MDCG coverage
# Fetches the official EC guidance page, extracts all MDCG document references,
# then compares against local _index.json to find new/updated documents.
# ---------------------------------------------------------------------------

class MDCGPageChecker:
    """Scrapes EC MDCG guidance page to detect new/updated MDCG documents."""

    MDCG_URL = (
        "https://health.ec.europa.eu/medical-devices-sector/"
        "new-regulations/guidance-mdcg-endorsed-documents-and-other-guidance_en"
    )

    # Matches patterns like: MDCG 2021-24, MDCG 2024-13, MDCG 2022-5 rev.1
    _REF_RE = re.compile(
        r"MDCG\s+(\d{4})[-–](\d+)(?:[-/](\d+))?"
        r"(?:\s*(?:rev\.?\s*(\d+)|v(\d+)|ADD\.?\s*(\d+)))?",
        re.IGNORECASE,
    )
    _DATE_RE = re.compile(
        r"(January|February|March|April|May|June|July|August|September|"
        r"October|November|December)\s+(\d{4})"
    )
    _MONTHS = {
        "january": "01", "february": "02", "march": "03", "april": "04",
        "may": "05", "june": "06", "july": "07", "august": "08",
        "september": "09", "october": "10", "november": "11", "december": "12",
    }

    def __init__(self, session: requests.Session, state: dict, db_comparator):
        self.session = session
        self.state = state
        self.db_comparator = db_comparator

    def check(self, source_id: str, source: dict) -> Optional[dict]:
        """Fetch EC page, parse all MDCG refs, compare with DB."""
        try:
            resp = self.session.get(self.MDCG_URL, timeout=30)
            resp.raise_for_status()
        except Exception as e:
            print(f"    ERROR fetching EC MDCG page: {e}")
            return None

        page_text = resp.text
        official_docs = self._parse_mdcg_refs(page_text)
        if not official_docs:
            print(f"    WARNING: No MDCG refs parsed from EC page")
            return None

        print(f"    INFO: Parsed {len(official_docs)} unique MDCG documents from EC page")

        new_items = []
        update_items = []

        for doc_id, info in official_docs.items():
            classification, desc = self.db_comparator.classify(
                "eu_mdr/mdcg", info["title"], info.get("url", ""), info.get("date", "")
            )
            if classification == "new":
                new_items.append({
                    "title": info["title"],
                    "link": info.get("url", ""),
                    "pub_date": info.get("date", ""),
                    "doc_id": doc_id,
                    "revision": info.get("revision", ""),
                    "db_classification": "new",
                    "db_description": desc,
                })
            elif classification == "update":
                update_items.append({
                    "title": info["title"],
                    "link": info.get("url", ""),
                    "pub_date": info.get("date", ""),
                    "doc_id": doc_id,
                    "revision": info.get("revision", ""),
                    "db_classification": "update",
                    "db_description": desc,
                })

        self.state[source_id] = {
            "url": source["url"],
            "last_checked": datetime.now().isoformat(),
            "official_count": len(official_docs),
        }

        all_detected = new_items + update_items
        if not all_detected:
            return None

        result = _make_update(
            source_id, source, "ec_page_scrape",
            f"{len(new_items)} new + {len(update_items)} updated MDCG document(s) "
            f"detected via EC page scrape (official total: {len(official_docs)})"
        )
        result["new_items"] = all_detected
        result["db_confirmed_items"] = all_detected
        result["db_confirmed"] = True
        result["noise_filtered"] = len(official_docs) - len(all_detected)
        result["official_total"] = len(official_docs)
        return result

    def _parse_mdcg_refs(self, html: str) -> dict:
        """Extract all MDCG document references from EC page HTML.

        The EC page uses <tr class="ecl-table__row"> with cells:
          - data-ecl-table-header="Reference" : contains MDCG ref + download link
          - data-ecl-table-header="Title" : document title
          - data-ecl-table-header="Publication" : publication date
        """
        docs: dict[str, dict] = {}

        # Strategy: find each table row, extract Reference/Title/Publication cells
        row_re = re.compile(r"<tr[^>]*class=\"ecl-table__row\"[^>]*>(.*?)</tr>", re.DOTALL)
        cell_re = re.compile(
            r'<td[^>]*data-ecl-table-header="(\w+)"[^>]*>(.*?)</td>', re.DOTALL
        )

        for row_match in row_re.finditer(html):
            row_html = row_match.group(1)
            cells = {}
            for cell_match in cell_re.finditer(row_html):
                header = cell_match.group(1)
                content = cell_match.group(2)
                cells[header] = content

            ref_html = cells.get("Reference", "")
            title_html = cells.get("Title", "")
            pub_html = cells.get("Publication", "")

            # Extract MDCG ID from Reference cell
            mdcg_match = self._REF_RE.search(ref_html)
            if not mdcg_match:
                continue

            year, num = mdcg_match.group(1), mdcg_match.group(2)
            sub_num = mdcg_match.group(3)
            rev = mdcg_match.group(4) or mdcg_match.group(5) or ""
            addendum = mdcg_match.group(6) or ""

            base_id = f"mdcg-{year}-{num}"
            if sub_num:
                base_id += f"-{sub_num}"

            revision_str = ""
            if rev:
                revision_str = f"rev.{rev}"
            elif addendum:
                revision_str = f"ADD.{addendum}"

            # Extract title (strip HTML tags)
            title = re.sub(r"<[^>]+>", "", title_html).strip()

            # Extract publication date
            date_str = ""
            pub_text = re.sub(r"<[^>]+>", "", pub_html).strip()
            date_match = self._DATE_RE.search(pub_text)
            if date_match:
                month_num = self._MONTHS.get(date_match.group(1).lower(), "01")
                date_str = f"{date_match.group(2)}-{month_num}"

            # Extract download URL from Reference cell
            url = ""
            url_match = re.search(r'href="([^"]+)"', ref_html)
            if url_match:
                url = url_match.group(1)
                if url.startswith("/"):
                    url = f"https://health.ec.europa.eu{url}"

            full_ref = mdcg_match.group(0).strip()

            if base_id not in docs or revision_str:
                docs[base_id] = {
                    "title": title or full_ref,
                    "revision": revision_str,
                    "date": date_str,
                    "url": url,
                    "ref": full_ref,
                }
            elif not docs[base_id].get("revision") and revision_str:
                docs[base_id]["revision"] = revision_str

        return docs


# ---------------------------------------------------------------------------
# EC Medical Devices Latest Updates page checker
# Scrapes https://ec.europa.eu/health/medical-devices-sector/latest-updates_en
# Covers: Delegated Regulations, Implementing Regulations, MDCG updates, policy
# ---------------------------------------------------------------------------

class ECLatestUpdatesChecker:
    """Scrapes EC Medical Devices Latest Updates page for regulatory news.

    This page covers a much wider scope than the MDCG guidance list:
    - Delegated Regulations (e.g. WET expansions under Art. 52(4), 61(6)(b))
    - Implementing Regulations (e.g. conformity assessment, notified bodies)
    - MDCG position papers and new guidance
    - EUDAMED updates, MIR form updates
    - Policy announcements (breakthrough device programmes, etc.)
    """

    URL = "https://ec.europa.eu/health/medical-devices-sector/latest-updates_en"

    _PRIORITY_KEYWORDS = re.compile(
        r"(?i)(delegated\s+(?:act|regulation)|implementing\s+regulation|"
        r"well.established|harmonised\s+standard|common\s+specification|"
        r"clinical\s+investigation|classification|notified\s+bod|"
        r"unique\s+device\s+identif|UDI|EUDAMED|conformity\s+assessment|"
        r"borderline|breakthrough|Article\s+\d+)",
    )

    def __init__(self, session: requests.Session, state: dict):
        self.session = session
        self.state = state

    def check(self, source_id: str, source: dict) -> Optional[dict]:
        prev = self.state.get(source_id, {})
        prev_titles = set(prev.get("seen_titles", []))

        try:
            resp = self.session.get(self.URL, timeout=30)
            resp.raise_for_status()
        except Exception as e:
            print(f"    ERROR fetching EC Latest Updates: {e}")
            return None

        entries = self._parse_entries(resp.text)
        if not entries:
            print(f"    WARNING: No entries parsed from EC Latest Updates page")
            return None

        print(f"    INFO: Parsed {len(entries)} entries from EC Latest Updates page")

        new_items = []
        all_titles = list(prev_titles)

        for entry in entries:
            title = entry.get("title", "")
            if not title or title in prev_titles:
                continue
            all_titles.append(title)
            new_items.append({
                "title": title,
                "link": entry.get("link", ""),
                "pub_date": entry.get("date", ""),
                "description": entry.get("type", ""),
            })

        self.state[source_id] = {
            "url": source["url"],
            "last_checked": datetime.now().isoformat(),
            "seen_titles": all_titles[-200:],
            "total_entries": len(entries),
        }

        if new_items and prev_titles:
            result = _make_update(
                source_id, source, "ec_latest_updates",
                f"{len(new_items)} new EC Medical Devices update(s) detected"
            )
            result["new_items"] = new_items
            return result
        elif not prev_titles:
            print(f"    INFO: Baseline established ({len(entries)} entries indexed)")

        return None

    def _parse_entries(self, html: str) -> list[dict]:
        """Parse article blocks from EC Latest Updates page."""
        results = []
        article_re = re.compile(r"<article[^>]*>(.*?)</article>", re.DOTALL)

        for art_match in article_re.finditer(html):
            art = art_match.group(1)

            date_m = re.search(r'<time[^>]*datetime="([^"]+)"', art)
            date_str = date_m.group(1)[:10] if date_m else ""

            title = ""
            link = ""
            title_block = re.search(
                r'class="ecl-content-block__title"[^>]*>(.*?)</(?:h\d|div|span)',
                art, re.DOTALL,
            )
            if title_block:
                link_m = re.search(r'<a[^>]*href="([^"]+)"[^>]*>([^<]+)</a>',
                                   title_block.group(1))
                if link_m:
                    link = link_m.group(1)
                    title = link_m.group(2).strip()
                else:
                    title = re.sub(r"<[^>]+>", "", title_block.group(1)).strip()

            if link and link.startswith("/"):
                link = "https://health.ec.europa.eu" + link

            if not title:
                continue

            results.append({
                "title": title,
                "date": date_str,
                "link": link,
                "type": "EC News",
            })

        return results


# ---------------------------------------------------------------------------
# FDA Safety Communications page scraper
# Scrapes the FDA Medical Device Safety page for new safety communications.
# ---------------------------------------------------------------------------

class FDASafetyRecallChecker:
    """Checks OpenFDA device/recall.json for recently initiated recalls (all classes).

    This replaces the web-scraping FDASafetyPageChecker because FDA pages are
    protected by WAF (401). The OpenFDA recall API provides structured data
    about all device recalls initiated in the past 14 days.

    Complements FDARecallChecker (enforcement API, Class I only) by covering
    Class II/III recalls and newly initiated events before enforcement action.
    """

    RECALL_URL = "https://api.fda.gov/device/recall.json"

    def __init__(self, api_key: str, state: dict):
        self.api_key = api_key
        self.state = state

    def check(self, source_id: str, source: dict) -> Optional[dict]:
        prev = self.state.get(source_id, {})
        seen_ids = set(prev.get("seen_res_numbers", []))

        lookback = (datetime.now() - timedelta(days=30)).strftime("%Y%m%d")
        today = datetime.now().strftime("%Y%m%d")

        search_q = f'event_date_initiated:[{lookback} TO {today}]'
        url = (
            f"{self.RECALL_URL}"
            f"?search={requests.utils.quote(search_q)}"
            f"&sort=event_date_initiated:desc&limit=30"
        )
        if self.api_key:
            url += f"&api_key={self.api_key}"

        try:
            resp = requests.get(url, timeout=20)
            if resp.status_code == 404:
                self.state[source_id] = {
                    "url": source["url"],
                    "last_checked": datetime.now().isoformat(),
                    "seen_res_numbers": list(seen_ids),
                }
                return None
            resp.raise_for_status()
            results = resp.json().get("results", [])
        except Exception as e:
            print(f"    ERROR OpenFDA Recall: {e}")
            return None

        new_items = []
        all_ids = list(seen_ids)

        for r in results:
            res_num = r.get("product_res_number") or r.get("res_event_number", "")
            if not res_num or res_num in seen_ids:
                continue
            all_ids.append(res_num)

            firm = r.get("recalling_firm", "Unknown")
            product = (r.get("product_description") or "")[:120]
            reason = r.get("reason_for_recall", "")
            cfres_id = r.get("cfres_id", "")
            init_date = r.get("event_date_initiated", "")

            title = f"Device Recall: {firm} - {product}"
            description = f"Recall {res_num}: {reason[:250]}"
            link = (
                f"https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfRes/res.cfm"
                f"?id={cfres_id}"
            ) if cfres_id else source["url"]

            new_items.append({
                "title": title,
                "link": link,
                "pub_date": self._format_date(init_date),
                "description": description,
                "res_number": res_num,
                "recalling_firm": firm,
            })

        self.state[source_id] = {
            "url": source["url"],
            "last_checked": datetime.now().isoformat(),
            "seen_res_numbers": all_ids[-500:],
        }

        if new_items and seen_ids:
            result = _make_update(
                source_id, source, "fda_safety_page",
                f"{len(new_items)} new device recall(s) detected"
            )
            result["new_items"] = new_items
            return result
        elif not seen_ids:
            print(f"    INFO: Baseline established ({len(results)} recent recalls indexed)")

        return None

    @staticmethod
    def _format_date(date_str: str) -> str:
        if len(date_str) == 8 and date_str.isdigit():
            return f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:8]}"
        return date_str


# ---------------------------------------------------------------------------
# FDA Class I Recall checker via OpenFDA Enforcement API
# Only retrieves Class I (most serious) device recalls.
# ---------------------------------------------------------------------------

class FDARecallChecker:
    """Checks OpenFDA Enforcement API for new Class I medical device recalls.

    Class I recalls are the most serious: reasonable probability that use of or
    exposure to a product will cause serious adverse health consequences or death.
    """

    ENFORCEMENT_URL = "https://api.fda.gov/device/enforcement.json"

    def __init__(self, api_key: str, state: dict):
        self.api_key = api_key
        self.state = state

    def check(self, source_id: str, source: dict) -> Optional[dict]:
        prev = self.state.get(source_id, {})
        last_recall_nums = set(prev.get("seen_recall_numbers", []))

        two_weeks_ago = (datetime.now() - timedelta(days=14)).strftime("%Y%m%d")
        today = datetime.now().strftime("%Y%m%d")

        search_q = (
            f'classification:"Class I"'
            f' AND report_date:[{two_weeks_ago} TO {today}]'
        )
        url = f"{self.ENFORCEMENT_URL}?search={requests.utils.quote(search_q)}&limit=20"
        if self.api_key:
            url += f"&api_key={self.api_key}"

        try:
            resp = requests.get(url, timeout=20)
            if resp.status_code == 404:
                self.state[source_id] = {
                    "url": source["url"],
                    "last_checked": datetime.now().isoformat(),
                    "seen_recall_numbers": list(last_recall_nums),
                }
                return None
            resp.raise_for_status()
            results = resp.json().get("results", [])
        except Exception as e:
            print(f"    ERROR OpenFDA Enforcement: {e}")
            return None

        new_items = []
        all_recall_nums = list(last_recall_nums)

        for r in results:
            recall_num = r.get("recall_number", "")
            if not recall_num or recall_num in last_recall_nums:
                continue
            all_recall_nums.append(recall_num)

            product_desc = r.get("product_description", "")[:200]
            reason = r.get("reason_for_recall", "")
            firm = r.get("recalling_firm", "")
            report_date = r.get("report_date", "")
            quantity = r.get("product_quantity", "")

            title = f"Class I Recall: {firm} - {product_desc[:80]}"
            description = (
                f"Recall #{recall_num} by {firm}. "
                f"Reason: {reason[:200]}. "
                f"Quantity: {quantity}."
            )

            new_items.append({
                "title": title,
                "link": f"https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfres/res.cfm?id={recall_num}",
                "pub_date": self._format_date(report_date),
                "description": description,
                "recall_number": recall_num,
                "recalling_firm": firm,
                "classification": "Class I",
                "reason": reason,
                "product_quantity": quantity,
            })

        self.state[source_id] = {
            "url": source["url"],
            "last_checked": datetime.now().isoformat(),
            "seen_recall_numbers": all_recall_nums[-500:],
        }

        if new_items and last_recall_nums:
            result = _make_update(
                source_id, source, "openfda_enforcement",
                f"{len(new_items)} new Class I device recall(s) detected"
            )
            result["new_items"] = new_items
            return result
        elif not last_recall_nums:
            print(f"    INFO: Baseline established ({len(results)} Class I recalls indexed)")

        return None

    @staticmethod
    def _format_date(date_str: str) -> str:
        """Convert YYYYMMDD to YYYY-MM-DD."""
        if len(date_str) == 8 and date_str.isdigit():
            return f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:8]}"
        return date_str


# ---------------------------------------------------------------------------
# CDRH News and Updates page checker
# Scrapes the CDRH main news page for regulatory announcements.
# ---------------------------------------------------------------------------

class CDRHNewsChecker:
    """Scrapes CDRH News and Updates page for regulatory announcements.

    Captures: town halls, guidance announcements, policy updates, and other
    CDRH communications relevant to medical device manufacturers.
    """

    CDRH_URL = "https://www.fda.gov/medical-devices/medical-devices-news-and-events/cdrh-new-news-and-updates"

    _PRIORITY_KEYWORDS = re.compile(
        r"(?i)(guidance|final\s+rule|proposed\s+rule|safety\s+communication|"
        r"recall|cybersecurity|software|QMSR|510\(k\)|PMA|De\s*Novo|"
        r"UDI|labeling|AI|machine\s+learning|real.world|SaMD|"
        r"postmarket|premarket|clinical\s+investigation|town\s+hall)",
    )

    def __init__(self, session: requests.Session, state: dict):
        self.session = session
        self.state = state

    def check(self, source_id: str, source: dict) -> Optional[dict]:
        prev = self.state.get(source_id, {})
        prev_titles = set(prev.get("seen_titles", []))

        try:
            resp = self.session.get(self.CDRH_URL, timeout=30)
            if resp.status_code == 401:
                print(f"    INFO: CDRH news page returned 401 (WAF block). "
                      f"Falling back to OpenFDA guidance API coverage.")
                self.state[source_id] = {
                    "url": source["url"],
                    "last_checked": datetime.now().isoformat(),
                    "seen_titles": list(prev_titles),
                    "status": "waf_blocked",
                }
                return None
            resp.raise_for_status()
        except Exception as e:
            print(f"    ERROR fetching CDRH news: {e}")
            return None

        entries = self._parse_entries(resp.text)
        if not entries:
            print(f"    WARNING: No entries parsed from CDRH news page")
            return None

        print(f"    INFO: Parsed {len(entries)} entries from CDRH news page")

        new_items = []
        all_titles = list(prev_titles)

        for entry in entries:
            title = entry.get("title", "")
            if not title or title in prev_titles:
                continue
            all_titles.append(title)
            new_items.append({
                "title": title,
                "link": entry.get("link", ""),
                "pub_date": entry.get("date", ""),
                "description": entry.get("type", "CDRH News"),
            })

        self.state[source_id] = {
            "url": source["url"],
            "last_checked": datetime.now().isoformat(),
            "seen_titles": all_titles[-200:],
        }

        if new_items and prev_titles:
            result = _make_update(
                source_id, source, "fda_cdrh_news",
                f"{len(new_items)} new CDRH news/update(s) detected"
            )
            result["new_items"] = new_items
            return result
        elif not prev_titles:
            print(f"    INFO: Baseline established ({len(entries)} CDRH news entries)")

        return None

    def _parse_entries(self, html: str) -> list[dict]:
        """Parse news entries from CDRH News page."""
        results = []
        try:
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(html, "html.parser")
            for link in soup.find_all("a"):
                href = link.get("href", "")
                text = link.get_text(strip=True)
                if not text or len(text) < 10:
                    continue
                if "/medical-devices/" in href and self._PRIORITY_KEYWORDS.search(text):
                    if href.startswith("/"):
                        href = "https://www.fda.gov" + href
                    date_m = re.search(r"(\d{2}/\d{2}/\d{4})", text)
                    date_str = date_m.group(1) if date_m else ""
                    results.append({
                        "title": text,
                        "date": date_str,
                        "link": href,
                        "type": "CDRH News",
                    })
        except ImportError:
            results = self._parse_entries_regex(html)
        return results

    def _parse_entries_regex(self, html: str) -> list[dict]:
        """Fallback regex parser."""
        results = []
        link_re = re.compile(
            r'<a[^>]*href="(/medical-devices/[^"]+)"[^>]*>(.*?)</a>',
            re.DOTALL,
        )
        for m in link_re.finditer(html):
            href = "https://www.fda.gov" + m.group(1)
            title = re.sub(r"<[^>]+>", "", m.group(2)).strip()
            if title and len(title) > 10 and self._PRIORITY_KEYWORDS.search(title):
                results.append({
                    "title": title,
                    "date": "",
                    "link": href,
                    "type": "CDRH News",
                })
        return results


# ---------------------------------------------------------------------------
# Generic Atom Feed checker (GOV.UK, MHRA, etc.)
# Parses Atom XML feeds and detects new entries since last check.
# ---------------------------------------------------------------------------

class AtomFeedChecker:
    """Parses Atom feeds (RFC 4287) for new entries since last check.

    Covers: GOV.UK Atom feeds (MHRA, HSE), EU Atom feeds, etc.
    """

    def __init__(self, session: requests.Session, state: dict,
                 seed_mode: bool = False):
        self.session = session
        self.state = state
        self.seed_mode = seed_mode

    def check(self, source_id: str, source: dict) -> Optional[dict]:
        url = source["url"]
        prev = self.state.get(source_id, {})
        prev_ids = set(prev.get("seen_ids", []))
        title_filter = source.get("title_filter")

        try:
            resp = self.session.get(url, timeout=30)
            resp.raise_for_status()
        except Exception as e:
            print(f"    ERROR Atom feed: {e}")
            return None

        entries = self._parse_atom(resp.content)
        if not entries:
            print(f"    WARNING: No entries parsed from Atom feed")
            return None

        print(f"    INFO: Parsed {len(entries)} entries from Atom feed")

        new_items = []
        all_ids = list(prev_ids)
        title_exclude = source.get("title_exclude")

        for entry in entries:
            eid = entry.get("id", entry.get("link", ""))
            title = entry.get("title", "")
            if not eid or eid in prev_ids:
                continue
            if title_filter and not re.search(title_filter, title, re.IGNORECASE):
                continue
            if title_exclude and re.search(title_exclude, title, re.IGNORECASE):
                print(f"      EXCLUDED (medicine/drug): {title[:80]}")
                all_ids.append(eid)
                continue
            all_ids.append(eid)
            new_items.append({
                "title": title,
                "link": entry.get("link", ""),
                "pub_date": entry.get("updated", "")[:10],
                "description": entry.get("summary", "")[:300],
            })

        self.state[source_id] = {
            "url": url,
            "last_checked": datetime.now().isoformat(),
            "seen_ids": all_ids[-500:],
        }

        if new_items and (prev_ids or self.seed_mode):
            if self.seed_mode and not prev_ids:
                new_items = new_items[:10]
                print(f"    INFO: Seed mode -- returning top {len(new_items)} entries as initial news")
            result = _make_update(
                source_id, source, "atom_feed",
                f"{len(new_items)} new Atom feed entry(ies) detected"
            )
            result["new_items"] = new_items
            return result
        elif not prev_ids:
            print(f"    INFO: Baseline established ({len(entries)} Atom entries indexed)")

        return None

    def _parse_atom(self, content: bytes) -> list[dict]:
        """Parse Atom XML feed into list of entry dicts."""
        results = []
        try:
            root = ET.fromstring(content)
            ns = {"atom": "http://www.w3.org/2005/Atom"}
            for entry in root.findall("atom:entry", ns):
                eid_el = entry.find("atom:id", ns)
                title_el = entry.find("atom:title", ns)
                updated_el = entry.find("atom:updated", ns)
                summary_el = entry.find("atom:summary", ns)
                link_el = entry.find("atom:link[@rel='alternate']", ns)
                if link_el is None:
                    link_el = entry.find("atom:link", ns)

                results.append({
                    "id": eid_el.text.strip() if eid_el is not None and eid_el.text else "",
                    "title": title_el.text.strip() if title_el is not None and title_el.text else "",
                    "updated": updated_el.text.strip() if updated_el is not None and updated_el.text else "",
                    "summary": (summary_el.text or "").strip() if summary_el is not None else "",
                    "link": link_el.get("href", "") if link_el is not None else "",
                })
        except ET.ParseError as e:
            print(f"    ERROR parsing Atom XML: {e}")
        return results


# ---------------------------------------------------------------------------
# Canada Health Canada Recalls checker
# Uses recalls-rappels.canada.ca search page for device recalls/safety alerts.
# ---------------------------------------------------------------------------

class CanadaRecallsChecker:
    """Checks Health Canada recalls and safety alerts for medical devices.

    Uses the official Open Data JSON dataset from recalls-rappels.canada.ca.
    Medical device records are identified by 'Recall class' using 'Type I/II/III'
    (food/consumer products use 'Class 1/2/3' instead).
    """

    DATA_URL = "https://recalls-rappels.canada.ca/sites/default/files/opendata-donneesouvertes/HCRSAMOpenData.json"

    _MEDICAL_DEVICE_CATEGORIES = {
        "Anaesthesiology", "Cardiovascular", "Chemistry", "Dental",
        "Ear, nose and throat", "Gastroenterology and urology",
        "General and plastic surgery", "General hospital and personal use",
        "In vitro diagnostics", "Microbiology", "Neurology",
        "Obstetrics and gynaecology", "Ophthalmology", "Orthopaedics",
        "Radiology", "Physical medicine",
    }

    def __init__(self, session: requests.Session, state: dict,
                 seed_mode: bool = False):
        self.session = session
        self.state = state
        self.seed_mode = seed_mode

    _EXCLUDE_CATEGORIES = {"Drugs", "Alcoholic", "Dairy", "Herbs and spices",
                            "Other", "Candy, confectionary, snacks and sweeten"}

    def _is_medical_device(self, record: dict) -> bool:
        category = record.get("Category", "") or ""
        if any(ec in category for ec in self._EXCLUDE_CATEGORIES):
            return False
        recall_class = record.get("Recall class", "") or ""
        if "Type " in recall_class:
            return True
        return any(mc in category for mc in self._MEDICAL_DEVICE_CATEGORIES)

    def check(self, source_id: str, source: dict) -> Optional[dict]:
        prev = self.state.get(source_id, {})
        prev_nids = set(str(n) for n in prev.get("seen_nids", []))

        try:
            resp = self.session.get(self.DATA_URL, timeout=60)
            resp.raise_for_status()
            all_records = resp.json()
        except Exception as e:
            print(f"    ERROR Canada Open Data: {e}")
            return None

        cutoff = (datetime.now() - timedelta(days=90)).strftime("%Y-%m-%d")
        md_records = []
        for r in all_records:
            if not self._is_medical_device(r):
                continue
            updated = r.get("Last updated", "") or ""
            if updated >= cutoff:
                md_records.append(r)

        print(f"    INFO: {len(md_records)} medical device records in last 90 days (from {len(all_records)} total)")

        new_items = []
        all_nids = list(prev_nids)

        for r in md_records:
            nid = str(r.get("NID", ""))
            if not nid or nid in prev_nids:
                continue
            all_nids.append(nid)
            title = r.get("Title", "Untitled")
            url = r.get("URL", "")
            if url and not url.startswith("http"):
                url = "https://recalls-rappels.canada.ca" + url
            new_items.append({
                "title": title,
                "link": url,
                "pub_date": (r.get("Last updated", "") or "")[:10],
                "description": (r.get("Issue", "") or "")[:400],
                "recall_class": r.get("Recall class", ""),
                "category": r.get("Category", ""),
            })

        self.state[source_id] = {
            "url": self.DATA_URL,
            "last_checked": datetime.now().isoformat(),
            "seen_nids": all_nids[-1000:],
        }

        if new_items and (prev_nids or self.seed_mode):
            if self.seed_mode and not prev_nids:
                new_items = new_items[:10]
                print(f"    INFO: Seed mode -- returning top {len(new_items)} medical device entries")
            result = _make_update(
                source_id, source, "canada_recalls",
                f"{len(new_items)} new Canada medical device recall(s)/alert(s)"
            )
            result["new_items"] = new_items
            return result
        elif not prev_nids:
            print(f"    INFO: Baseline established ({len(md_records)} medical device records)")

        return None


# ---------------------------------------------------------------------------
# PMDA (Japan) page checkers
# Parses PMDA English safety/regulatory pages and Japanese recall lists.
# ---------------------------------------------------------------------------

class PMDAWhatsNewChecker:
    """Checks PMDA English 'What's New' page for device-related updates.

    This page (https://www.pmda.go.jp/english/0006.html) lists all recent
    PMDA updates with category tags (Review, Safety, Other, Events, Int, JP).
    Content is filtered by title_filter regex to extract device-related items only.
    """

    def __init__(self, session: requests.Session, state: dict,
                 seed_mode: bool = False):
        self.session = session
        self.state = state
        self.seed_mode = seed_mode

    def check(self, source_id: str, source: dict) -> Optional[dict]:
        url = source["url"]
        prev = self.state.get(source_id, {})
        prev_ids = set(prev.get("seen_ids", []))
        title_filter = source.get("title_filter")
        title_exclude = source.get("title_exclude")

        try:
            resp = self.session.get(url, timeout=30)
            resp.raise_for_status()
        except Exception as e:
            print(f"    ERROR PMDA What's New: {e}")
            return None

        entries = self._parse_whatsnew(resp.text)
        if not entries:
            print("    WARNING: No entries from PMDA What's New page")
            return None

        print(f"    INFO: Parsed {len(entries)} entries from PMDA What's New")

        new_items = []
        all_ids = list(prev_ids)

        for entry in entries:
            eid = entry.get("link") or entry.get("title", "")
            if not eid or eid in prev_ids:
                continue
            title = entry.get("title", "")
            if title_filter and not re.search(title_filter, title, re.IGNORECASE):
                all_ids.append(eid)
                continue
            if title_exclude and re.search(title_exclude, title, re.IGNORECASE):
                all_ids.append(eid)
                continue
            all_ids.append(eid)
            new_items.append(entry)

        self.state[source_id] = {
            "url": url,
            "last_checked": datetime.now().isoformat(),
            "seen_ids": all_ids[-500:],
        }

        if new_items and (prev_ids or self.seed_mode):
            if self.seed_mode and not prev_ids:
                new_items = new_items[:10]
                print(f"    INFO: Seed mode -- returning top {len(new_items)} PMDA What's New entries")
            result = _make_update(
                source_id, source, "pmda_whatsnew",
                f"{len(new_items)} new PMDA device update(s) detected"
            )
            result["new_items"] = new_items
            return result
        elif not prev_ids:
            print(f"    INFO: Baseline established ({len(entries)} PMDA What's New entries)")

        return None

    @staticmethod
    def _parse_whatsnew(html: str) -> list[dict]:
        """Parse PMDA What's New page -- list items with date, category, and title."""
        _TAG_RE = re.compile(
            r"^(?:(?:January|February|March|April|May|June|July|August|"
            r"September|October|November|December)\s+\d{1,2},?\s*\d{4})"
            r"\s*"
            r"(?:Review|Safety|Other|Events|Int|JP|Devices?|Drug|Regen\.?|IVD|CDx)*"
            r"\s*(?:New)?\s*",
            re.IGNORECASE,
        )
        results = []
        try:
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(html, "html.parser")
            for li in soup.find_all("li"):
                text = li.get_text(" ", strip=True)
                dm = re.search(
                    r"((?:January|February|March|April|May|June|July|August|"
                    r"September|October|November|December)\s+\d{1,2},?\s*\d{4})",
                    text,
                )
                if not dm:
                    continue
                date_str = dm.group(1)
                a_tag = li.find("a")
                if a_tag and a_tag.get("href"):
                    title = a_tag.get_text(strip=True)
                    href = a_tag["href"]
                    if not href.startswith("http"):
                        href = "https://www.pmda.go.jp" + href
                else:
                    remainder = text[dm.end():].strip()
                    remainder = re.sub(
                        r"^(?:Review|Safety|Other|Events|Int|JP|Devices?|Drug|Regen\.?|IVD|CDx)\s*",
                        "", remainder,
                    ).strip()
                    remainder = re.sub(r"^New\s*", "", remainder).strip()
                    title = remainder
                    href = ""
                if not title or len(title) < 10:
                    continue
                title = re.sub(r"\s*\[\d+\s*KB\]", "", title).strip()
                title = _TAG_RE.sub("", title).strip()
                results.append({
                    "title": title,
                    "link": href,
                    "pub_date": date_str,
                    "description": "",
                })
        except ImportError:
            pass
        return results[:50]


class PMDAChecker:
    """Checks PMDA (Japan) English pages for medical device safety & regulatory updates.

    Parses tabular pages: Medical Safety Information, Revisions of PRECAUTIONS,
    Alert for Proper Use of Medical Devices, etc.
    """

    def __init__(self, session: requests.Session, state: dict,
                 seed_mode: bool = False):
        self.session = session
        self.state = state
        self.seed_mode = seed_mode

    def check(self, source_id: str, source: dict) -> Optional[dict]:
        url = source["url"]
        prev = self.state.get(source_id, {})
        prev_titles = set(prev.get("seen_titles", []))

        try:
            resp = self.session.get(url, timeout=30)
            resp.raise_for_status()
        except Exception as e:
            print(f"    ERROR PMDA: {e}")
            return None

        entries = self._parse_table_page(resp.text, url)
        if not entries:
            print(f"    WARNING: No entries from PMDA page ({url})")
            return None

        print(f"    INFO: Parsed {len(entries)} entries from PMDA page")

        new_items = []
        all_titles = list(prev_titles)

        for entry in entries:
            title = entry.get("title", "")
            if not title or title in prev_titles:
                continue
            all_titles.append(title)
            new_items.append(entry)

        self.state[source_id] = {
            "url": url,
            "last_checked": datetime.now().isoformat(),
            "seen_titles": all_titles[-300:],
        }

        if new_items and (prev_titles or self.seed_mode):
            if self.seed_mode and not prev_titles:
                new_items = new_items[:10]
                print(f"    INFO: Seed mode -- returning top {len(new_items)} entries as initial news")
            result = _make_update(
                source_id, source, "pmda_page",
                f"{len(new_items)} new PMDA update(s) detected"
            )
            result["new_items"] = new_items
            return result
        elif not prev_titles:
            print(f"    INFO: Baseline established ({len(entries)} PMDA entries)")

        return None

    def _parse_table_page(self, html: str, base_url: str) -> list[dict]:
        """Parse PMDA table-based pages (safety info, precautions, alerts)."""
        results = []
        try:
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(html, "html.parser")
            for tr in soup.find_all("tr"):
                cells = tr.find_all("td")
                if len(cells) < 2:
                    continue
                date_text = ""
                content_title = ""
                link_title = ""
                link_href = ""
                for cell in cells:
                    cell_text = cell.get_text(strip=True)
                    dm = re.search(r"((?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},?\s*\d{4})", cell_text)
                    if not dm:
                        dm = re.search(r"((?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4})", cell_text)
                    if not dm:
                        dm = re.search(r"(\d{4})[./\-](\d{1,2})[./\-](\d{1,2})", cell_text)
                    if dm and not date_text:
                        if dm.lastindex and dm.lastindex >= 2:
                            date_text = f"{dm.group(1)}-{dm.group(2).zfill(2)}-{dm.group(3).zfill(2)}"
                        else:
                            date_text = dm.group(1)
                    a = cell.find("a")
                    if a and a.get_text(strip=True) and len(a.get_text(strip=True)) > 5:
                        link_title = a.get_text(strip=True)
                        link_href = a.get("href", "")
                    elif len(cell_text) > 5 and not re.match(r"^[\d\s,./]+$", cell_text) and not content_title:
                        if cell_text != date_text and not re.search(r"^\d+$", cell_text):
                            content_title = cell_text
                title_text = content_title or link_title
                if not title_text or len(title_text) < 5:
                    continue
                title_text = re.sub(r"\s*\[\d+\s*KB\]", "", title_text).strip()
                if re.match(r"^(?:January|February|March|April|May|June|July|August|September|October|November|December)\s*\d{4}$", title_text):
                    continue
                if link_href and not link_href.startswith("http"):
                    link_href = "https://www.pmda.go.jp" + link_href
                results.append({
                    "title": title_text,
                    "link": link_href,
                    "pub_date": date_text,
                    "description": "",
                })
            if not results:
                for li in soup.select("ul li, .whatsnew li, dl dt, dl dd"):
                    links = li.find_all("a")
                    for a in links:
                        title = a.get_text(strip=True)
                        href = a.get("href", "")
                        if not title or len(title) < 10:
                            continue
                        if href and not href.startswith("http"):
                            href = "https://www.pmda.go.jp" + href
                        dm = re.search(r"(\d{4})[./\-](\d{1,2})[./\-](\d{1,2})", li.get_text())
                        ds = f"{dm.group(1)}-{dm.group(2).zfill(2)}-{dm.group(3).zfill(2)}" if dm else ""
                        results.append({"title": title, "link": href, "pub_date": ds, "description": ""})
        except ImportError:
            link_re = re.compile(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', re.DOTALL)
            for m in link_re.finditer(html):
                title = re.sub(r"<[^>]+>", "", m.group(2)).strip()
                href = m.group(1)
                if title and len(title) > 10:
                    if not href.startswith("http"):
                        href = "https://www.pmda.go.jp" + href
                    results.append({"title": title, "link": href, "pub_date": "", "description": ""})
        return results[:30]


class PMDARecallsChecker:
    """Checks PMDA Japanese recall list pages for medical device recalls.

    Parses the structured HTML tables at info.pmda.go.jp with device name,
    manufacturer, recall class and publication date.
    """

    def __init__(self, session: requests.Session, state: dict,
                 seed_mode: bool = False):
        self.session = session
        self.state = state
        self.seed_mode = seed_mode

    def check(self, source_id: str, source: dict) -> Optional[dict]:
        url = source["url"]
        if source.get("dynamic_year"):
            yy = str(datetime.now().year % 100).zfill(2)
            url = url.replace("{yy}", yy)
        recall_class = source.get("recall_class", "")
        prev = self.state.get(source_id, {})
        prev_ids = set(prev.get("seen_ids", []))

        try:
            resp = self.session.get(url, timeout=30)
            resp.raise_for_status()
        except Exception as e:
            print(f"    ERROR PMDA Recalls: {e}")
            return None

        entries = self._parse_recall_table(resp.text, recall_class)
        if not entries:
            print(f"    WARNING: No entries from PMDA recall page")
            return None

        print(f"    INFO: Parsed {len(entries)} Class {recall_class} recall entries from PMDA")

        new_items = []
        all_ids = list(prev_ids)
        cutoff = (datetime.now() - timedelta(days=60)).strftime("%Y-%m-%d")

        for entry in entries:
            eid = entry.get("id", "")
            if not eid or eid in prev_ids:
                continue
            all_ids.append(eid)
            pub = entry.get("pub_date", "")
            if pub and pub < cutoff:
                continue
            new_items.append(entry)

        self.state[source_id] = {
            "url": url,
            "last_checked": datetime.now().isoformat(),
            "seen_ids": all_ids[-500:],
        }

        if new_items and (prev_ids or self.seed_mode):
            if self.seed_mode and not prev_ids:
                new_items = new_items[:10]
                print(f"    INFO: Seed mode -- returning top {len(new_items)} recall entries")
            result = _make_update(
                source_id, source, "pmda_recalls",
                f"{len(new_items)} new PMDA Class {recall_class} recall(s) detected"
            )
            result["new_items"] = new_items
            return result
        elif not prev_ids:
            print(f"    INFO: Baseline established ({len(entries)} PMDA recall entries)")

        return None

    def _parse_recall_table(self, html: str, recall_class: str) -> list[dict]:
        """Parse PMDA Japanese recall table page.

        Table columns: [0] recall_num, [1] pub_date, [2] device_type,
        [3] generic_name, [4] product_name (has <a> detail link), [5] manufacturer.
        Detail links use /rgo/MainServlet?recallno=xxx format.
        """
        results = []
        try:
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(html, "html.parser")
            for tr in soup.find_all("tr"):
                cells = tr.find_all("td")
                if len(cells) < 5:
                    continue
                recall_num = cells[0].get_text(strip=True)
                pub_date_raw = cells[1].get_text(strip=True)
                device_type = cells[2].get_text(strip=True)
                generic_name = cells[3].get_text(strip=True)
                product_name = cells[4].get_text(strip=True)
                manufacturer = cells[5].get_text(strip=True) if len(cells) > 5 else ""
                detail_link = ""
                for cell in cells:
                    a_tag = cell.find("a")
                    if a_tag and a_tag.get("href"):
                        href = a_tag["href"]
                        if not href.startswith("http"):
                            href = "https://www.info.pmda.go.jp" + href
                        if "MainServlet" in href or "kaisyuu" in href:
                            detail_link = href
                            break
                if not detail_link:
                    yy = str(datetime.now().year % 100).zfill(2)
                    cls_suffix = "1k" if recall_class == "I" else "2k"
                    detail_link = f"https://www.info.pmda.go.jp/kaisyuu/rcidx{yy}-{cls_suffix}.html"
                dm = re.search(r"(\d{4})/(\d{1,2})/(\d{1,2})", pub_date_raw)
                pub_date = f"{dm.group(1)}-{dm.group(2).zfill(2)}-{dm.group(3).zfill(2)}" if dm else ""
                title = f"[Class {recall_class}] {product_name} ({generic_name})"
                if manufacturer:
                    title += f" - {manufacturer}"
                results.append({
                    "id": recall_num,
                    "title": title,
                    "link": detail_link,
                    "pub_date": pub_date,
                    "description": f"Recall #{recall_num}: {generic_name} / {product_name} by {manufacturer}. Type: {device_type}.",
                })
        except ImportError:
            pass
        return results


# ---------------------------------------------------------------------------
# MFDS (Korea) English news page checker
# Parses the MFDS English news board for device regulatory updates.
# ---------------------------------------------------------------------------

class MFDSChecker:
    """Checks MFDS (Korea) English news page for medical device regulatory updates.

    Korea is transitioning from MFDS to DMPA (2026 reform).
    Captures: KGMP updates, device classification changes, regulatory reforms.
    """

    def __init__(self, session: requests.Session, state: dict,
                 seed_mode: bool = False):
        self.session = session
        self.state = state
        self.seed_mode = seed_mode

    def check(self, source_id: str, source: dict) -> Optional[dict]:
        url = source["url"]
        prev = self.state.get(source_id, {})
        prev_titles = set(prev.get("seen_titles", []))
        title_filter = source.get("title_filter")

        try:
            resp = self.session.get(url, timeout=30)
            resp.raise_for_status()
        except Exception as e:
            print(f"    ERROR MFDS: {e}")
            return None

        base_url = self._detect_base_url(url)
        entries = self._parse_news(resp.text, base_url)
        if not entries:
            print(f"    WARNING: No entries from MFDS page ({url})")
            return None

        print(f"    INFO: Parsed {len(entries)} entries from MFDS page")

        if title_filter:
            before = len(entries)
            entries = [e for e in entries
                       if re.search(title_filter, e.get("title", ""), re.IGNORECASE)]
            print(f"    INFO: {len(entries)} entries after title filter (from {before})")

        new_items = []
        all_titles = list(prev_titles)

        for entry in entries:
            title = entry.get("title", "")
            if not title or title in prev_titles:
                continue
            all_titles.append(title)
            new_items.append(entry)

        self.state[source_id] = {
            "url": url,
            "last_checked": datetime.now().isoformat(),
            "seen_titles": all_titles[-300:],
        }

        if new_items and (prev_titles or self.seed_mode):
            if self.seed_mode and not prev_titles:
                new_items = new_items[:10]
                print(f"    INFO: Seed mode -- returning top {len(new_items)} entries as initial news")
            result = _make_update(
                source_id, source, "mfds_page",
                f"{len(new_items)} new MFDS update(s) detected"
            )
            result["new_items"] = new_items
            return result
        elif not prev_titles:
            print(f"    INFO: Baseline established ({len(entries)} MFDS entries)")

        return None

    @staticmethod
    def _detect_base_url(url: str) -> str:
        """Extract base URL from the board list page URL."""
        m = re.match(r"(https://www\.mfds\.go\.kr/eng/brd/m_\d+/)", url)
        return m.group(1) if m else "https://www.mfds.go.kr/eng/brd/m_61/"

    @staticmethod
    def _parse_news(html: str, base_url: str) -> list[dict]:
        """Parse MFDS English board page (supports m_40, m_41, m_61)."""
        results = []
        try:
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(html, "html.parser")
            for a in soup.find_all("a", href=re.compile(r"view\.do")):
                title = a.get_text(strip=True)
                href = a.get("href", "")
                if not title or len(title) < 10:
                    continue
                href = href.replace("&amp;", "&")
                if href.startswith("./"):
                    href = base_url + href[2:]
                elif href and not href.startswith("http"):
                    href = base_url + href
                date_str = ""
                date_in_title = re.search(
                    r"(\d{4})[.\s]+(?:January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+(\d{1,2})",
                    title,
                )
                if date_in_title:
                    pass
                row = a.find_parent("tr") or a.find_parent("li")
                if row:
                    for el in row.find_all(["td", "span", "p"]):
                        dm = re.search(r"(\d{4})[.\-/](\d{2})[.\-/](\d{2})", el.get_text())
                        if dm:
                            date_str = f"{dm.group(1)}-{dm.group(2)}-{dm.group(3)}"
                            break
                if not date_str:
                    dm_raw = re.search(r"(\d{4})-(\d{2})-(\d{2})", html[html.find(title[:20]):html.find(title[:20])+500] if title[:20] in html else "")
                    if dm_raw:
                        date_str = f"{dm_raw.group(1)}-{dm_raw.group(2)}-{dm_raw.group(3)}"
                if href.endswith("down.do") or "/down.do?" in href:
                    continue
                results.append({
                    "title": title, "link": href,
                    "pub_date": date_str, "description": "",
                })
        except ImportError:
            link_re = re.compile(r'<a[^>]*href="(\./view\.do[^"]*)"[^>]*>(.*?)</a>', re.DOTALL)
            for m in link_re.finditer(html):
                title = re.sub(r"<[^>]+>", "", m.group(2)).strip()
                href = m.group(1).replace("&amp;", "&")
                if title and len(title) > 10:
                    href = base_url + href[2:]
                    results.append({
                        "title": title, "link": href,
                        "pub_date": "", "description": "",
                    })
        seen = set()
        deduped = []
        for r in results:
            key = r["title"][:50]
            if key not in seen:
                seen.add(key)
                deduped.append(r)
        return deduped[:30]


# ---------------------------------------------------------------------------
# Generic page checker (for simple announcement pages with links)
# Used as fallback for pages without RSS/Atom/API support.
# ---------------------------------------------------------------------------

class GenericPageChecker:
    """Scrapes a generic announcement/news page for new links.

    Simple approach: extract all <a> tags with href, filter by title_filter,
    detect new titles since last check. Works for most government news pages.
    """

    def __init__(self, session: requests.Session, state: dict):
        self.session = session
        self.state = state

    def check(self, source_id: str, source: dict) -> Optional[dict]:
        url = source["url"]
        prev = self.state.get(source_id, {})
        prev_titles = set(prev.get("seen_titles", []))
        title_filter = source.get("title_filter")

        try:
            resp = self.session.get(url, timeout=30)
            resp.raise_for_status()
        except Exception as e:
            print(f"    ERROR generic page: {e}")
            return None

        entries = self._parse_links(resp.text, url)
        if not entries:
            print(f"    WARNING: No entries from page {url}")
            return None

        print(f"    INFO: Parsed {len(entries)} entries from page")

        new_items = []
        all_titles = list(prev_titles)

        for entry in entries:
            title = entry.get("title", "")
            if not title or title in prev_titles:
                continue
            if title_filter and not re.search(title_filter, title, re.IGNORECASE):
                continue
            all_titles.append(title)
            new_items.append(entry)

        self.state[source_id] = {
            "url": url,
            "last_checked": datetime.now().isoformat(),
            "seen_titles": all_titles[-300:],
        }

        if new_items and prev_titles:
            result = _make_update(
                source_id, source, "generic_page",
                f"{len(new_items)} new page item(s) detected"
            )
            result["new_items"] = new_items
            return result
        elif not prev_titles:
            print(f"    INFO: Baseline established ({len(entries)} page entries)")

        return None

    def _parse_links(self, html: str, base_url: str) -> list[dict]:
        """Extract meaningful links from an HTML page."""
        results = []
        parsed = urlparse(base_url)
        base_domain = f"{parsed.scheme}://{parsed.netloc}"

        try:
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(html, "html.parser")
            for a in soup.find_all("a"):
                title = a.get_text(strip=True)
                href = a.get("href", "")
                if not title or len(title) < 10:
                    continue
                if href and not href.startswith("http"):
                    href = base_domain + href
                date_el = a.find_parent().find("time") if a.find_parent() else None
                date_str = date_el.get("datetime", "")[:10] if date_el else ""
                results.append({
                    "title": title, "link": href,
                    "pub_date": date_str, "description": "",
                })
        except ImportError:
            link_re = re.compile(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', re.DOTALL)
            for m in link_re.finditer(html):
                title = re.sub(r"<[^>]+>", "", m.group(2)).strip()
                href = m.group(1)
                if title and len(title) > 10:
                    if not href.startswith("http"):
                        href = base_domain + href
                    results.append({
                        "title": title, "link": href,
                        "pub_date": "", "description": "",
                    })
        return results[:30]


# ---------------------------------------------------------------------------
# EUR-Lex Amendment checker (replaces http_head for harmonised standards)
# Checks consolidated decision URL date suffix for new amendments
# ---------------------------------------------------------------------------

class EURLexChecker:
    """
    Checks EUR-Lex for harmonised standards amendments via CELLAR SPARQL API.

    Three-layer detection:
    1. SPARQL query: Get all consolidated versions of CID 2021/1182 from CELLAR,
       compare latest consolidated date against last known.
    2. Standards count comparison: Compare current harmonised standards count against
       local _index.json to detect additions/removals between amendment cycles.
    3. Fallback HEAD redirect (unreliable, kept as belt-and-suspenders).

    Note: The old HEAD-redirect approach to eur-lex.europa.eu returns HTTP 202 with
    empty body (anti-bot), so Layer 1 SPARQL is the primary detection mechanism.
    """
    SPARQL_URL = "https://publications.europa.eu/webapi/rdf/sparql"
    SPARQL_QUERY = """
PREFIX cdm: <http://publications.europa.eu/ontology/cdm#>
SELECT DISTINCT ?celex ?date ?consoDate WHERE {
  ?work cdm:resource_legal_id_celex ?celex .
  FILTER(STRSTARTS(?celex, "02021D1182"))
  OPTIONAL { ?work cdm:work_date_document ?date . }
  OPTIONAL { ?work cdm:work_date_creation ?consoDate . }
} ORDER BY DESC(?celex) LIMIT 5
"""

    def __init__(self, session: requests.Session, state: dict):
        self.session = session
        self.state = state

    def check(self, source_id: str, source: dict) -> Optional[dict]:
        prev = self.state.get(source_id, {})
        last_known_amendment = prev.get("last_known_amendment", "")
        last_known_count = prev.get("standards_count", 0)

        # Ignore legacy placeholder "99990101" from old HEAD-redirect approach
        if last_known_amendment == "99990101":
            last_known_amendment = ""

        new_consol_date = ""
        sparql_ok = False

        try:
            # Layer 1: CELLAR SPARQL API -- authoritative consolidated version dates
            new_consol_date = self._sparql_latest_consolidated()
            if new_consol_date:
                sparql_ok = True
                print(f"    INFO: SPARQL latest consolidated: {new_consol_date}")
        except Exception as e:
            print(f"    WARNING: SPARQL failed ({e}), falling back to HEAD redirect")

        if not sparql_ok:
            # Layer 3 fallback: HEAD redirect (unreliable but harmless)
            try:
                consol_url = "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02021D1182-99990101"
                resp = self.session.head(consol_url, timeout=15, allow_redirects=True)
                final_url = str(resp.url) if resp.url else ""
                date_match = re.search(r"02021D1182-(\d{8})", final_url)
                fallback_date = date_match.group(1) if date_match else ""
                if fallback_date and fallback_date != "99990101":
                    new_consol_date = fallback_date
            except Exception:
                pass

        # Layer 2: Local standards count check
        current_count = self._get_local_standards_count()

        self.state[source_id] = {
            "url": source["url"],
            "last_checked": datetime.now().isoformat(),
            "last_known_amendment": new_consol_date or last_known_amendment,
            "standards_count": current_count,
            "detection_method": "sparql" if sparql_ok else "head_fallback",
        }

        if not last_known_amendment:
            print(f"    INFO: EUR-Lex baseline established (consolidated date: {new_consol_date}, count: {current_count})")
            return None

        changes = []
        if new_consol_date and new_consol_date > last_known_amendment:
            changes.append(f"consolidated date: {last_known_amendment} -> {new_consol_date}")

        if last_known_count and current_count != last_known_count:
            changes.append(f"standards count: {last_known_count} -> {current_count}")

        if changes:
            return _make_update(
                source_id, source, "eurlex_amendment",
                f"Harmonised standards change detected ({'; '.join(changes)})"
            )
        return None

    def _sparql_latest_consolidated(self) -> str:
        """Query CELLAR SPARQL for the latest consolidated version date of CID 2021/1182.

        Returns date string like '20260407' or empty string on failure.
        """
        resp = self.session.get(
            self.SPARQL_URL,
            params={"query": self.SPARQL_QUERY, "format": "application/json"},
            timeout=30,
        )
        resp.raise_for_status()
        data = resp.json()
        bindings = data.get("results", {}).get("bindings", [])
        if not bindings:
            return ""
        # CELEX format: 02021D1182-YYYYMMDD -- extract the date part from first (latest) result
        celex = bindings[0].get("celex", {}).get("value", "")
        match = re.search(r"02021D1182-(\d{8})", celex)
        return match.group(1) if match else ""

    def _get_local_standards_count(self) -> int:
        """Get current harmonised standards count from local _index.json."""
        index_path = ROOT / "eu_mdr" / "standards" / "_index.json"
        if not index_path.exists():
            return 0
        try:
            with open(index_path) as f:
                data = json.load(f)
            return data.get("total_standards", 0)
        except Exception:
            return 0


# ---------------------------------------------------------------------------
# LLM Version Analyzer (optional - requires LLM_API_KEY)
# Uses OneAPI-compatible endpoint (deepseek-chat, gpt-4o-mini, etc.)
# ---------------------------------------------------------------------------

class LLMVersionAnalyzer:
    def __init__(self, api_key: str, base_url: str, model: str):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.model = model
        self.available = bool(api_key)

    def analyze(self, doc_id: str, registry_entry: Optional[dict], new_items: list) -> dict:
        if not self.available or not new_items:
            return {"is_update": False, "confidence": 0.0, "reasoning": "LLM not configured"}
        current = (registry_entry or {}).get("current", {})
        prompt = (
            f'You are a regulatory document version analyst.\n\n'
            f'Current entry for "{doc_id}": title={current.get("title","N/A")}, '
            f'version={current.get("version","N/A")}, status={current.get("status","N/A")}, '
            f'published={current.get("published_date","N/A")}\n\n'
            f'New search results:\n{json.dumps(new_items[:5], ensure_ascii=False)}\n\n'
            f'Is this a genuine NEW VERSION or UPDATE? Consider: newer date, same document '
            f'type, Draft->Final transition, revision.\n'
            f'JSON only: {{"is_update":bool,"confidence":0.0-1.0,'
            f'"new_version":"YYYY-MM or null","new_url":"url or null","reasoning":"brief"}}'
        )
        try:
            resp = requests.post(
                f"{self.base_url}/chat/completions",
                headers={"Authorization": f"Bearer {self.api_key}",
                         "Content-Type": "application/json"},
                json={"model": self.model,
                      "messages": [{"role": "user", "content": prompt}],
                      "temperature": 0.1,
                      "response_format": {"type": "json_object"}},
                timeout=30,
            )
            resp.raise_for_status()
            return json.loads(resp.json()["choices"][0]["message"]["content"])
        except Exception as e:
            return {"is_update": False, "confidence": 0.0, "reasoning": f"LLM error: {e}"}


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------

def _make_update(source_id: str, source: dict, check_type: str, note: str) -> dict:
    return {
        "source_id": source_id, "name": source["name"], "url": source["url"],
        "category": source["category"], "check_type": check_type,
        "detected_at": datetime.now().isoformat(), "note": note,
    }


# ---------------------------------------------------------------------------
# Orchestrator
# ---------------------------------------------------------------------------

class UpdateChecker:
    def __init__(self, state_file: Path = None, seed_mode: bool = False):
        self.state_file = state_file or ROOT / "scripts" / ".update_state.json"
        self.state = self._load_state()
        self.seed_mode = seed_mode
        self.registry = VersionRegistry()
        self.db_comparator = DatabaseComparator(ROOT)
        session = requests.Session()
        session.headers.update({"User-Agent": "Mozilla/5.0 (docmcp-knowledge-bot/2.0)"})
        self.http = HTTPChecker(session, self.state)
        self.rss = RSSChecker(session, self.state, seed_mode)
        self.vertex = VertexAISearchChecker(
            VERTEX_AI_PROJECT_ID, VERTEX_AI_SEARCH_APP_ID,
            VERTEX_AI_SEARCH_API_KEY, self.state, seed_mode,
        )
        self.google = GoogleSearchChecker("", "", self.state, seed_mode)  # DEPRECATED
        self.web_search_available = self.vertex.available
        self.openfda = OpenFDAChecker(FDA_API_KEY, self.state)
        self.ecfr = ECFRChecker(session, self.state)
        self.eurlex = EURLexChecker(session, self.state)
        self.mdcg_scraper = MDCGPageChecker(session, self.state, self.db_comparator)
        self.ec_latest = ECLatestUpdatesChecker(session, self.state)
        self.fda_safety = FDASafetyRecallChecker(FDA_API_KEY, self.state)
        self.fda_recall = FDARecallChecker(FDA_API_KEY, self.state)
        self.cdrh_news = CDRHNewsChecker(session, self.state)
        self.atom_feed = AtomFeedChecker(session, self.state, seed_mode)
        self.canada_recalls = CanadaRecallsChecker(session, self.state, seed_mode)
        self.pmda_whatsnew = PMDAWhatsNewChecker(session, self.state, seed_mode)
        self.pmda = PMDAChecker(session, self.state, seed_mode)
        self.pmda_recalls = PMDARecallsChecker(session, self.state, seed_mode)
        self.mfds = MFDSChecker(session, self.state, seed_mode)
        self.generic_page = GenericPageChecker(session, self.state)
        # Tier 2 checkers (Phase 3b)
        from tier2_checkers import (TGARSSChecker, SwissmedicChecker, SFDAChecker,
                                    ANVISAChecker, MedsafeChecker)
        self.tga_rss = TGARSSChecker(session, self.state, seed_mode)
        self.swissmedic = SwissmedicChecker(session, self.state, seed_mode)
        self.sfda = SFDAChecker(session, self.state, seed_mode)
        self.anvisa = ANVISAChecker(session, self.state, seed_mode)
        self.medsafe = MedsafeChecker(session, self.state, seed_mode)
        self.llm = LLMVersionAnalyzer(LLM_API_KEY, LLM_BASE_URL, LLM_MODEL)
        if self.vertex.available:
            print("INFO: Using Vertex AI Search (searchLite) for web queries.")
        else:
            print("INFO: No web search configured - set VERTEX_AI_PROJECT_ID + "
                  "VERTEX_AI_SEARCH_APP_ID + VERTEX_AI_SEARCH_API_KEY.")
        if not self.llm.available:
            print(f"INFO: LLM analysis not configured - set LLM_API_KEY "
                  f"(LLM_BASE_URL={LLM_BASE_URL}, LLM_MODEL={LLM_MODEL}).")

    def _load_state(self) -> dict:
        if self.state_file.exists():
            try:
                with open(self.state_file, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                pass
        return {}

    def _save_state(self):
        self.state_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.state_file, "w", encoding="utf-8") as f:
            json.dump(self.state, f, indent=2, ensure_ascii=False)

    def _web_search_check(self, source_id: str, source: dict) -> Optional[dict]:
        """Dispatch web search to Vertex AI (preferred), fallback to Google CSE."""
        if self.vertex.available:
            result = self.vertex.check(source_id, source)
            if result:
                return result
        if self.google.available:
            return self.google.check(source_id, source)
        return None

    def check_source(self, source_id: str, source: dict) -> Optional[dict]:
        check_type = source.get("check_type", "http_head")
        if check_type == "rss":
            return self.rss.check(source_id, source)
        elif check_type == "google_search":
            result = self._web_search_check(source_id, source)
            if result:
                result = self._apply_db_comparison(result)
            return result
        elif check_type == "ec_page_scrape":
            return self.mdcg_scraper.check(source_id, source)
        elif check_type == "ec_latest_updates":
            return self.ec_latest.check(source_id, source)
        elif check_type == "openfda_guidance":
            result = self.openfda.check(source_id, source)
            if result:
                result = self._apply_db_comparison(result)
            return result
        elif check_type == "ecfr_api":
            return self.ecfr.check(source_id, source)
        elif check_type == "fda_safety_page":
            return self.fda_safety.check(source_id, source)
        elif check_type == "openfda_enforcement":
            return self.fda_recall.check(source_id, source)
        elif check_type == "fda_cdrh_news":
            return self.cdrh_news.check(source_id, source)
        elif check_type == "atom_feed":
            return self.atom_feed.check(source_id, source)
        elif check_type == "canada_recalls":
            return self.canada_recalls.check(source_id, source)
        elif check_type == "pmda_whatsnew":
            return self.pmda_whatsnew.check(source_id, source)
        elif check_type == "pmda_page":
            return self.pmda.check(source_id, source)
        elif check_type == "pmda_recalls":
            return self.pmda_recalls.check(source_id, source)
        elif check_type == "mfds_page":
            return self.mfds.check(source_id, source)
        elif check_type == "tga_rss":
            return self.tga_rss.check(source_id, source)
        elif check_type == "swissmedic_csv":
            return self.swissmedic.check(source_id, source)
        elif check_type == "sfda_weekly":
            return self.sfda.check(source_id, source)
        elif check_type == "sfda_rss":
            return self.sfda.check(source_id, source)
        elif check_type == "anvisa_page":
            return self.anvisa.check(source_id, source)
        elif check_type == "medsafe_page":
            return self.medsafe.check(source_id, source)
        elif check_type == "generic_page":
            return self.generic_page.check(source_id, source)
        elif check_type == "eurlex_amendment":
            return self.eurlex.check(source_id, source)
        else:
            result = self.http.check(source_id, source)
            if source.get("google_query") and self.web_search_available:
                g_result = self._web_search_check(source_id + "_google", source)
                if g_result:
                    g_result = self._apply_db_comparison(g_result)
                    return g_result
            return result

    def _apply_db_comparison(self, update: dict) -> Optional[dict]:
        """Run DatabaseComparator on each new_item; keep only new/update items."""
        new_items = update.get("new_items", [])
        if not new_items:
            return update
        category = update.get("category", "")
        confirmed_items = []
        noise_filtered = 0
        for item in new_items:
            title = item.get("title", "")
            link = item.get("link", "")
            date = item.get("pub_date", "")
            classification, desc = self.db_comparator.classify(category, title, link, date)
            item["db_classification"] = classification
            item["db_description"] = desc
            if classification in ("new", "update"):
                confirmed_items.append(item)
            else:
                noise_filtered += 1
        update["noise_filtered"] = noise_filtered
        update["db_confirmed_items"] = confirmed_items
        if not confirmed_items:
            print(f"    INFO: All {len(new_items)} items filtered by DB comparison (noise)")
            return None
        update["new_items"] = confirmed_items
        update["note"] = (
            f"{len(confirmed_items)} DB-confirmed new item(s) "
            f"({noise_filtered} noise filtered from {len(new_items)} total)"
        )
        update["db_confirmed"] = True
        return update

    def check_regulation(self, regulation: str) -> list:
        if regulation not in SOURCES:
            print(f"Unknown regulation: {regulation}")
            return []
        updates = []
        sources = SOURCES[regulation]
        print(f"\nChecking {regulation} ({len(sources)} sources)...")
        for source_id, source in sources.items():
            full_id = f"{regulation}/{source_id}"
            print(f"  [{full_id}] {source['name']}")
            result = self.check_source(full_id, source)
            if result:
                updates.append(result)
                print(f"    -> UPDATE DETECTED: {result.get('note', '')}")
            else:
                print(f"    -> No changes")
            time.sleep(1.0)
        return updates

    def check_all(self) -> list:
        all_updates = []
        for regulation in SOURCES:
            updates = self.check_regulation(regulation)
            all_updates.extend(updates)
        return all_updates

    def analyze_versions(self, updates: list) -> list:
        if not self.llm.available:
            print("INFO: LLM analysis skipped (LLM_API_KEY not set)")
            return updates
        print("\nRunning LLM version analysis...")
        for update in updates:
            new_items = update.get("new_items", [])
            if not new_items:
                continue
            doc_id = update["source_id"]
            analysis = self.llm.analyze(doc_id, self.registry.get(doc_id), new_items)
            update["llm_analysis"] = analysis
            if analysis.get("is_update") and analysis.get("confidence", 0) > 0.7:
                update["confirmed_update"] = True
                update["new_version"] = analysis.get("new_version")
                update["new_url"] = analysis.get("new_url")
                print(f"  CONFIRMED: {doc_id} -> v{analysis.get('new_version')} "
                      f"({analysis.get('confidence', 0):.0%})")
            else:
                print(f"  UNCONFIRMED: {doc_id} - {analysis.get('reasoning','')[:80]}")
            time.sleep(0.5)
        return updates

    def generate_report(self, updates: list) -> dict:
        confirmed = [u for u in updates if u.get("confirmed_update")]
        db_confirmed = [u for u in updates if u.get("db_confirmed")]
        db_confirmed_new = len(db_confirmed)
        total_noise = sum(u.get("noise_filtered", 0) for u in updates)
        return {
            "checked_at": datetime.now().isoformat(),
            "updates_found": len(updates),
            "confirmed_updates": len(confirmed),
            "db_confirmed_new": db_confirmed_new,
            "noise_filtered_total": total_noise,
            "updates": updates,
            "db_stats": self.db_comparator.get_stats(),
            "summary": (
                f"{len(updates)} update(s) detected "
                f"({db_confirmed_new} DB-confirmed, {len(confirmed)} LLM-confirmed, "
                f"{total_noise} noise filtered) across "
                f"{len(set(u['category'] for u in updates))} categories"
                if updates else "No updates detected"
            ),
            "checkers_used": {
                "vertex_ai_search": self.vertex.available,
                "google_cse_legacy": self.google.available and not self.vertex.available,
                "ec_page_scraper": True,
                "openfda_api": True,
                "llm_analysis": self.llm.available,
                "db_comparator": True,
                "ecfr_api": True,
                "eurlex_checker": True,
            },
        }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Regulatory update checker (3-layer anti-scraping bypass)"
    )
    parser.add_argument("--check-all", action="store_true", help="Check all regulation groups")
    parser.add_argument("--check", metavar="GROUP",
                        help="Check specific group: eu_mdr / fda / nmpa / shared")
    parser.add_argument("--analyze-versions", action="store_true",
                        help="Run LLM version analysis on detected updates")
    parser.add_argument("--report", action="store_true",
                        help="Output JSON report (for GitHub Actions)")
    parser.add_argument("--output", metavar="FILE", help="Save report to file")
    parser.add_argument("--seed-news", action="store_true",
                        help="Seed mode: treat first run as news (not just baseline)")
    args = parser.parse_args()

    if not args.check_all and not args.check:
        parser.print_help()
        sys.exit(0)

    checker = UpdateChecker(seed_mode=args.seed_news)

    updates = []
    if args.check_all:
        updates = checker.check_all()
    elif args.check == "tier1_west":
        for grp in ("uk_mhra", "canada", "australia_tga"):
            updates.extend(checker.check_regulation(grp))
    elif args.check == "tier1_east":
        for grp in ("japan_pmda", "korea_mfds"):
            updates.extend(checker.check_regulation(grp))
    elif args.check == "tier2":
        for grp in ("switzerland", "brazil_anvisa", "saudi_sfda", "singapore_hsa", "india_cdsco"):
            updates.extend(checker.check_regulation(grp))
    elif args.check == "tier3":
        for grp in ("mexico_cofepris", "argentina_anmat", "taiwan_tfda",
                     "newzealand_medsafe", "indonesia_bpom", "malaysia_mda",
                     "thailand_fda", "israel_moh", "hongkong_mdco"):
            updates.extend(checker.check_regulation(grp))
    else:
        updates = checker.check_regulation(args.check)

    if args.analyze_versions:
        updates = checker.analyze_versions(updates)

    checker._save_state()
    checker.registry.save()

    report = checker.generate_report(updates)

    if args.report or args.output:
        report_json = json.dumps(report, indent=2, ensure_ascii=False)
        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(report_json)
            print(f"\nReport saved to: {args.output}")
        else:
            print("\n" + report_json)
    else:
        print(f"\n{'='*50}")
        print(f"Check complete: {report['summary']}")
        if updates:
            print("\nUpdates found:")
            for u in updates:
                print(f"  - [{u['category']}] {u['name']}")
                print(f"    {u['url']}")
                print(f"    {u.get('note', '')}")
        print(f"{'='*50}")

    if updates and args.report:
        sys.exit(1)


if __name__ == "__main__":
    main()
