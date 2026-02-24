import re
from pathlib import Path

dir_path = Path("/Users/michael/Library/CloudStorage/OneDrive-个人/coding/docmcp-knowledge/eu_mdr/mdcg/fulltext")
for file_path in dir_path.glob("*.md"):
    content = file_path.read_text("utf-8")
    if "**Footnotes**" in content:
        footnotes_part = content.split("**Footnotes**")[1]
        links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', footnotes_part)
        if links:
            print(f"Found {len(links)} links in {file_path.name}")
            print(f"Example: [{links[0][0]}]({links[0][1]})")
