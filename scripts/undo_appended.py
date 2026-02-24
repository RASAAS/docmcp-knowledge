from pathlib import Path
import re

REPO_ROOT = Path(__file__).parent.parent
docs_with_images = [
    "mdcg-2019-15", "mdcg-2019-16", "mdcg-2020-1", "mdcg-2020-3",
    "mdcg-2021-6", "mdcg-2021-8", "mdcg-2022-5", "mdcg-2022-21",
    "mdcg-2023-1", "mdcg-2023-7", "mdcg-2024-10", "mdcg-2025-6", "mdcg-2025-9"
]

def clean_file(filepath):
    if not filepath.exists(): return
    content = filepath.read_text(encoding="utf-8")
    if "## Additional Figures (Extracted)" in content:
        # Check if the file had <!-- fulltext-end -->
        had_marker = "<!-- fulltext-end -->" in content
        content = content.split("## Additional Figures (Extracted)")[0].strip()
        if had_marker and not content.endswith("<!-- fulltext-end -->"):
            content += "\n\n<!-- fulltext-end -->"
        content += "\n"
        filepath.write_text(content, encoding="utf-8")
        print(f"Cleaned {filepath.relative_to(REPO_ROOT)}")

for d in docs_with_images:
    clean_file(REPO_ROOT / "eu_mdr" / "mdcg" / "fulltext" / f"{d}.md")
    clean_file(REPO_ROOT / "docs" / "zh" / "eu_mdr" / "mdcg" / f"{d}.md")
    clean_file(REPO_ROOT / "docs" / "en" / "eu_mdr" / "mdcg" / f"{d}.md")
    clean_file(REPO_ROOT / "eu_mdr" / "mdcg" / f"{d}.zh.md")
    clean_file(REPO_ROOT / "eu_mdr" / "mdcg" / f"{d}.en.md")
