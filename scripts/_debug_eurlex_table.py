#!/usr/bin/env python3
"""Simulate _layout_table_to_text on the actual EUR-Lex Article 2 table."""
import sys, os, re
import httpx
from bs4 import BeautifulSoup, Tag

CELEX = "32017R0745"
URL = f"https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:{CELEX}"

resp = httpx.get(URL, follow_redirects=True, timeout=60)
soup = BeautifulSoup(resp.text, "html.parser")
body = soup.find("div", id="TexteOnly") or soup.find("body")
art2 = body.find("p", class_="oj-ti-art", string=re.compile(r"Article\s*2"))
table = art2.find_next("table")
while table and table.find_parent("table"):
    table = table.find_next("table")

# Simulate current _layout_table_to_text
print("=== CURRENT _layout_table_to_text (recursive find_all('tr')) ===")
for i, row in enumerate(table.find_all("tr")):
    cells = row.find_all(["td", "th"])
    parts = [c.get_text(strip=True)[:60] for c in cells]
    parts = [p for p in parts if p]
    print(f"  Row {i}: {len(cells)} cells (direct), parts={parts}")

# Better approach: only process direct rows, handle nested tables recursively
print("\n=== PROPOSED: recursive table walker ===")
def walk_table(tbl, depth=0):
    prefix = "  " * depth
    # Get direct rows only
    tbody = tbl.find("tbody", recursive=False)
    container = tbody if tbody else tbl
    rows = [c for c in container.children if isinstance(c, Tag) and c.name == "tr"]
    
    for row in rows:
        cells = row.find_all(["td", "th"], recursive=False)
        if not cells:
            continue
        
        # For each cell, separate direct text from nested tables
        for cell in cells:
            inner_tables = cell.find_all("table", recursive=False)
            
            # Get text excluding nested tables
            direct_text = ""
            for child in cell.children:
                if isinstance(child, Tag) and child.name == "table":
                    continue
                if isinstance(child, Tag):
                    direct_text += child.get_text(" ", strip=False)
                else:
                    direct_text += str(child)
            direct_text = re.sub(r"\s+", " ", direct_text).strip()
            
            if direct_text:
                print(f"{prefix}TEXT: '{direct_text[:100]}'")
            
            for it in inner_tables:
                walk_table(it, depth + 1)

walk_table(table)
