#!/usr/bin/env python3
"""Rebuild fda/guidance/_index.json from the official FDA guidance search catalog.

Filter: CDRH + Final + (Guidance Document | Special Controls).
Never Draft. Skip CPG / Memorandum / SECG.

Usage:
    python scripts/build_fda_guidance_catalog.py \\
        --catalog /workspace/fda-search-guidance.json
"""
from __future__ import annotations

import argparse
import html
import json
import re
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CATALOG = Path("/workspace/fda-search-guidance.json")
OUTPUT = ROOT / "fda" / "guidance" / "_index.json"

KEEP_TYPES = {"Guidance Document", "Special Controls Document"}
SKIP_TYPE_SUBSTR = ("CPG", "Compliance Policy", "Memorandum", "Small Entity")

PRESERVE_BY_URL_SLUG = {
    "cybersecurity-medical-devices-quality-management-system-considerations-and-content-premarket": {
        "slug": "cybersecurity-premarket",
        "id": "fda-cybersecurity-premarket-2026",
        "title_zh": "医疗器械网络安全：质量管理体系考量与上市前提交内容",
    },
    "postmarket-management-cybersecurity-medical-devices": {
        "slug": "postmarket-cybersecurity",
        "id": "fda-postmarket-cybersecurity-2016",
        "title_zh": "医疗器械网络安全的上市后管理",
    },
    "remanufacturing-medical-devices": {
        "slug": "remanufacturing",
        "id": "fda-remanufacturing-2024",
        "title_zh": "医疗器械再制造指南",
    },
}

FDA_CATEGORIES = [
    "digital_health_cyber",
    "premarket",
    "quality_manufacturing",
    "ivd",
    "labeling_udi",
    "postmarket",
    "radiation_imaging",
    "clinical_rwe",
    "other",
]

# First match wins. Keywords searched in title + topics + product (lowercase).
CATEGORY_KEYWORDS = [
    (
        "digital_health_cyber",
        (
            "cyber",
            "digital health",
            "software",
            "artificial intelligence",
            "machine learning",
            "samd",
            "mobile medical",
            "interoperab",
            "computer-assisted",
            "computer assisted",
            "clinical decision support",
            "predetermined change control",
            "off-the-shelf software",
            "device software",
            "medical device data system",
            "connected health",
            "wireless medical",
            "ai/ml",
            "ai-enabled",
            "pcdp",
        ),
    ),
    (
        "premarket",
        (
            "510(k)",
            "510k",
            "premarket",
            "pre-market",
            "premarket approval",
            "premarket notification",
            "premarket submission",
            "de novo",
            "investigational device exemption",
            r"\bides\b",
            r"\bide\b",
            "humanitarian device",
            "breakthrough device",
            "estar",
            "refuse to accept",
            "special 510",
            "abbreviated 510",
            "pma order",
            "pma supplement",
            "pma application",
        ),
    ),
    (
        "quality_manufacturing",
        (
            "qmsr",
            "quality system",
            "quality management",
            "quality assurance",
            "good manufacturing",
            "current good manufacturing",
            "cgmp",
            "iso 13485",
            "remanufactur",
            "reprocess",
            "manufacturing site",
            "inspection and field testing",
            "computer software assurance",
            "qms ",
        ),
    ),
    (
        "ivd",
        (
            "in vitro",
            "ivd",
            "companion diagnostic",
            "clia",
            "laboratory test",
            "nucleic acid",
            "next generation sequenc",
            "ngs-based",
            "diagnostic reagent",
            "in-vitro",
        ),
    ),
    (
        "labeling_udi",
        (
            "labeling",
            "labelling",
            "unique device ident",
            "gudid",
            r"\budi\b",
            "instructions for use",
            "patient labeling",
            "device labeling",
        ),
    ),
    (
        "postmarket",
        (
            "postmarket",
            "post-market",
            "post market",
            "recall",
            "medical device report",
            "emdr",
            "maude",
            "adverse event",
            "vigilance",
            "device tracking",
            "surveillance and detention",
            "corrections and removals",
            "dear doctor",
            "malfunction summary",
            "voluntary malfunction",
        ),
    ),
    (
        "radiation_imaging",
        (
            "radiological",
            "radiation",
            "x-ray",
            "xray",
            "laser notice",
            "laser product",
            "laser light",
            "mammograph",
            "fluoroscop",
            "magnetic resonance",
            "nuclear medicine",
            "tanning",
            "mercury vapor",
            "diagnostic imaging",
            "radiology",
            "ultrasound diagnostic",
            "computed tomography",
        ),
    ),
    (
        "clinical_rwe",
        (
            "clinical trial",
            "clinical investigation",
            "clinical study",
            "real-world",
            "real world",
            "bayesian",
            "biostatistic",
            "investigational study",
            "clinical evidence",
        ),
    ),
]

HREF_RE = re.compile(r'href=["\']([^"\']+)["\']', re.I)
MEDIA_RE = re.compile(r'/media/\d+/download', re.I)
DOCKET_RE = re.compile(r'FDA-\d{4}-[A-Z]-\d+')
TAG_RE = re.compile(r'<[^>]+>')


def strip_html(value: str) -> str:
    text = TAG_RE.sub('', value or '')
    text = html.unescape(text)
    text = text.replace('\xa0', ' ')
    return re.sub(r'\s+', ' ', text).strip()


def first_href(value: str) -> str:
    m = HREF_RE.search(value or '')
    return html.unescape(m.group(1)) if m else ''


def abs_fda_url(path: str) -> str:
    if not path:
        return ''
    if path.startswith('http://') or path.startswith('https://'):
        return path
    if not path.startswith('/'):
        path = '/' + path
    return 'https://www.fda.gov' + path


def parse_issue_date(value: str) -> str:
    raw = strip_html(value)
    if not raw:
        return ''
    for fmt in ('%m/%d/%Y', '%Y-%m-%d', '%m/%d/%y'):
        try:
            return datetime.strptime(raw, fmt).date().isoformat()
        except ValueError:
            continue
    m = re.search(r'(\d{4})-(\d{2})-(\d{2})', raw)
    if m:
        return f'{m.group(1)}-{m.group(2)}-{m.group(3)}'
    return ''


def split_topics(value: str) -> list[str]:
    parts = []
    for token in re.split(r'[,;]', value or ''):
        t = token.strip()
        if t:
            parts.append(t)
    # de-dupe preserving order
    seen = set()
    out = []
    for p in parts:
        key = p.lower()
        if key not in seen:
            seen.add(key)
            out.append(p)
    return out


NOISE_PHRASES = (
    "center for devices and radiological health",
    "food and drug administration staff",
    "guidance for industry and fda staff",
    "guidance for industry and food and drug administration staff",
    "guidance for industry",
)


def _haystack(title: str, topics: list[str], product: str = "") -> str:
    hay = f"{title} {' '.join(topics)} {product}".lower()
    for phrase in NOISE_PHRASES:
        hay = hay.replace(phrase, " ")
    hay = hay.replace("510(k)", "510k").replace("in vitro diagnostic", "ivd")
    hay = re.sub(r"\s+", " ", hay)
    return hay


def _kw_match(hay: str, kw: str) -> bool:
    if kw.startswith(r"\b") or kw.endswith(r"\b"):
        return re.search(kw, hay, flags=re.I) is not None
    return kw in hay


def classify(title: str, topics: list[str], product: str = "") -> str:
    hay = _haystack(title, topics, product)
    for cat, keywords in CATEGORY_KEYWORDS:
        for kw in keywords:
            if _kw_match(hay, kw):
                return cat
    return "other"


def extract_row(raw: dict) -> dict | None:
    center = raw.get('field_center') or ''
    if 'Center for Devices and Radiological Health' not in center:
        return None
    status = (raw.get('field_final_guidance_1') or '').strip()
    if status != 'Final':
        return None
    comm_type = (raw.get('field_communication_type') or '').strip()
    if comm_type not in KEEP_TYPES:
        return None
    if any(s.lower() in comm_type.lower() for s in SKIP_TYPE_SUBSTR):
        return None

    title_html = raw.get('title') or ''
    title = strip_html(title_html)
    href = first_href(title_html)
    if not title or not href:
        return None
    # SECG sometimes labeled as Guidance Document
    if 'small entity compliance guide' in title.lower():
        return None
    source_url = abs_fda_url(href)
    url_slug = source_url.rstrip('/').split('/')[-1]

    media_html = raw.get('field_associated_media_2') or ''
    media_path = ''
    m = MEDIA_RE.search(media_html)
    if m:
        media_path = m.group(0)
    pdf_url = abs_fda_url(media_path) if media_path else ''

    docket_html = raw.get('field_docket_number') or ''
    docket_m = DOCKET_RE.search(docket_html)
    docket = docket_m.group(0) if docket_m else strip_html(docket_html)

    topics_raw = ', '.join([
        raw.get('field_topics') or '',
        raw.get('term_node_tid') or '',
    ])
    topics = split_topics(strip_html(topics_raw))
    product = strip_html(raw.get('field_regulated_product_field') or '')
    published = parse_issue_date(raw.get('field_issue_datetime') or '')

    preserved = PRESERVE_BY_URL_SLUG.get(url_slug, {})
    slug = preserved.get('slug') or url_slug
    eid = preserved.get('id') or f'fda-{url_slug}'
    title_zh = preserved.get('title_zh', '')

    guidance_type = 'Special Controls' if 'Special Controls' in comm_type else 'Guidance Document'
    fda_category = classify(title, topics, product)

    return {
        'id': eid,
        'title': {'en': title, 'zh': title_zh},
        'slug': slug,
        'status': 'active',
        'source_url': source_url,
        'pdf_url': pdf_url,
        'published_date': published,
        'fda_category': fda_category,
        'guidance_type': guidance_type,
        'docket': docket,
        'topics': topics,
    }


def load_existing_preserve() -> dict:
    """Keep zh titles / ids if catalog URL still matches an existing entry."""
    if not OUTPUT.exists():
        return {}
    try:
        data = json.loads(OUTPUT.read_text(encoding='utf-8'))
    except Exception:
        return {}
    by_url = {}
    for e in data.get('entries', []):
        url = (e.get('source_url') or '').rstrip('/')
        if url:
            by_url[url] = e
    return by_url


def build(catalog_path: Path) -> dict:
    raw_rows = json.loads(catalog_path.read_text(encoding='utf-8'))
    existing_by_url = load_existing_preserve()
    entries = []
    seen_slugs = set()
    for raw in raw_rows:
        entry = extract_row(raw)
        if not entry:
            continue
        url = entry['source_url'].rstrip('/')
        prev = existing_by_url.get(url)
        if prev:
            # Preserve existing slug/id/zh if this URL was already in the index
            if prev.get('slug'):
                entry['slug'] = prev['slug']
            if prev.get('id'):
                entry['id'] = prev['id']
            prev_title = prev.get('title') or {}
            if isinstance(prev_title, dict) and prev_title.get('zh') and not entry['title']['zh']:
                entry['title']['zh'] = prev_title['zh']
        slug = entry['slug']
        if slug in seen_slugs:
            suffix = entry['published_date'][:4] or 'dup'
            entry['slug'] = f'{slug}-{suffix}'
        seen_slugs.add(entry['slug'])
        entries.append(entry)

    def sort_key(e):
        return (e.get('published_date') or '', e.get('title', {}).get('en', ''))

    entries.sort(key=sort_key, reverse=True)

    return {
        'category': 'fda/guidance',
        'description': (
            'Currently effective FDA CDRH Final guidance documents '
            '(Guidance Document and Special Controls). Draft, CPG, '
            'Memorandum, and SECG are excluded.'
        ),
        'last_updated': date.today().isoformat(),
        'count': len(entries),
        'entries': entries,
    }


def main():
    parser = argparse.ArgumentParser(description='Build FDA CDRH Final guidance index')
    parser.add_argument('--catalog', default=str(DEFAULT_CATALOG),
                        help='Path to official search-fda-guidance JSON')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()

    catalog_path = Path(args.catalog)
    if not catalog_path.exists():
        raise SystemExit(f'Catalog not found: {catalog_path}')

    data = build(catalog_path)
    counts = {}
    for e in data['entries']:
        counts[e['fda_category']] = counts.get(e['fda_category'], 0) + 1
    pdfs = sum(1 for e in data['entries'] if e.get('pdf_url'))
    print(f"Catalog: {data['count']} CDRH Final Guidance/Special Controls")
    print(f"With pdf_url: {pdfs}")
    for cat in FDA_CATEGORIES:
        print(f"  {cat}: {counts.get(cat, 0)}")

    if args.dry_run:
        print('DRY RUN: not writing')
        return

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'Wrote {OUTPUT}')


if __name__ == '__main__':
    main()
