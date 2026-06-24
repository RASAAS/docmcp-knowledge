#!/usr/bin/env python3
"""Test EUR-Lex URL accessibility for all regulations in _index.json.

Maps each regulation to its CELEX number and HTML URL, then tests accessibility.
"""
import json
import sys
from pathlib import Path

import requests

KNOWLEDGE_ROOT = Path(__file__).parent.parent
INDEX_FILE = KNOWLEDGE_ROOT / "eu_mdr" / "regulations" / "_index.json"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Accept": "text/html,*/*",
}

# Manual CELEX mapping for regulations with /eli/ URLs (no CELEX in URL)
ELI_TO_CELEX = {
    "eu-reg-directive-2011-65-eu-rohs-2": "32011L0065",
    "eu-reg-regulation-ec-no-1907-2006-reach": "32006R1907",
    "eu-reg-regulation-ec-no-1272-2008-clp": "32008R1272",
    "eu-reg-directive-2012-19-eu-weee": "32012L0019",
    "eu-reg-council-directive-2013-59-euratom": "32013L0059",
    "eu-reg-regulation-eu-2023-1542-battery-regulation": "32023R1542",
    "eu-reg-regulation-eu-722-2012-tse": "32012R0722",
    "eu-reg-regulation-eu-2024-2847-cyber-resilience-act": "32024R2847",
    "eu-reg-directive-eu-2022-2555-nis2": "32022L2555",
    "eu-reg-regulation-eu-2024-1689-ai-act": "32024R1689",
    "eu-reg-regulation-eu-2023-988-gpsr": "32023R0988",
    "eu-reg-regulation-eu-2024-1781-espr": "32024R1781",
    "eu-reg-regulation-eu-2025-40-ppwr": "32025R0040",
    "eu-reg-directive-2014-53-eu-red": "32014L0053",
    "eu-reg-regulation-eu-2023-1230-machinery-regulation": "32023R1230",
    "eu-reg-directive-2001-83-ec-medicinal-products": "32001L0083",
    "eu-reg-directive-eu-2022-2557-cer-directive": "32022L2557",
}

CELEX_FROM_URL = {
    "eu-mdr-2017-745": "32017R0745",
    "eu-ivdr-2017-746": "32017R0746",
}


def main():
    with open(INDEX_FILE, "r") as f:
        data = json.load(f)

    results = []
    for doc in data["documents"]:
        eid = doc["id"]
        source_url = doc.get("source_url", "")

        if not source_url or "eur-lex" not in source_url:
            print(f"SKIP (no EUR-Lex URL): {eid}")
            continue

        celex = CELEX_FROM_URL.get(eid) or ELI_TO_CELEX.get(eid)
        if not celex:
            import re
            m = re.search(r"CELEX[:%](\d+\w+)", source_url)
            if m:
                celex = m.group(1)

        if not celex:
            print(f"WARN: No CELEX mapping for {eid} ({source_url})")
            continue

        html_url = f"https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:{celex}"
        title = doc.get("title", {})
        if isinstance(title, dict):
            display = title.get("en", "")[:60]
        else:
            display = str(title)[:60]

        results.append({
            "id": eid,
            "celex": celex,
            "html_url": html_url,
            "title": display,
            "number": doc.get("number", ""),
        })

    print(f"\nTotal regulations with EUR-Lex CELEX: {len(results)}\n")
    print(f"{'ID':<55} {'CELEX':<15} {'Number':<40}")
    print("-" * 110)
    for r in results:
        print(f"{r['id']:<55} {r['celex']:<15} {r['number']:<40}")

    print(f"\n--- Testing URL accessibility (first 3) ---\n")
    for r in results[:3]:
        try:
            resp = requests.head(r["html_url"], headers=HEADERS, timeout=15,
                                 allow_redirects=True)
            status = resp.status_code
            size = resp.headers.get("content-length", "?")
            print(f"  {r['celex']}: HTTP {status} (size={size})")
        except Exception as e:
            print(f"  {r['celex']}: FAILED ({e})")

    print("\n--- slug suggestions ---\n")
    for r in results:
        slug = r["id"]
        print(f'  "{r["id"]}": slug="{slug}", celex="{r["celex"]}"')


if __name__ == "__main__":
    main()
