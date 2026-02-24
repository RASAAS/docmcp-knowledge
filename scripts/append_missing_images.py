#!/usr/bin/env python3
import sys
import re
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
FULLTEXT_DIR = REPO_ROOT / "eu_mdr" / "mdcg" / "fulltext"
ZH_DIR = REPO_ROOT / "docs" / "zh" / "eu_mdr" / "mdcg"
EN_DIR = REPO_ROOT / "docs" / "en" / "eu_mdr" / "mdcg"

docs_with_images = [
    "mdcg-2019-15",
    "mdcg-2019-16",
    "mdcg-2020-1",
    "mdcg-2020-3",
    "mdcg-2021-6",
    "mdcg-2021-8",
    "mdcg-2022-5",
    "mdcg-2022-21",
    "mdcg-2023-1",
    "mdcg-2023-7",
    "mdcg-2024-10",
    "mdcg-2025-6",
    "mdcg-2025-9"
]

def process_doc(doc_id):
    # Get all extracted images for this doc_id
    img_dir = REPO_ROOT / "docs" / "public" / "images" / "mdcg"
    all_imgs = sorted([f.name for f in img_dir.glob(f"{doc_id}-fig*.png")])
    if not all_imgs:
        return
        
    def append_to_file(filepath):
        if not filepath.exists():
            return
        content = filepath.read_text(encoding="utf-8")
        
        # Check which images are NOT in the file
        missing_imgs = []
        for img_name in all_imgs:
            if img_name not in content:
                missing_imgs.append(img_name)
                
        if missing_imgs:
            print(f"[{doc_id}] {filepath.name}: {len(missing_imgs)} missing images appended.")
            # Append missing
            append_text = "\n\n## Additional Figures (Extracted)\n\n"
            for m in missing_imgs:
                append_text += f"\n![](/images/mdcg/{m})\n"
                
            # If <!-- fulltext-end --> exists, insert before it
            if "<!-- fulltext-end -->" in content:
                parts = content.split("<!-- fulltext-end -->", 1)
                new_content = parts[0] + append_text + "\n<!-- fulltext-end -->" + parts[1]
            else:
                new_content = content + append_text
                
            filepath.write_text(new_content, encoding="utf-8")

    # target files
    append_to_file(FULLTEXT_DIR / f"{doc_id}.md")
    append_to_file(ZH_DIR / f"{doc_id}.md")
    append_to_file(EN_DIR / f"{doc_id}.md")
    append_to_file(REPO_ROOT / "eu_mdr" / "mdcg" / f"{doc_id}.zh.md")
    append_to_file(REPO_ROOT / "eu_mdr" / "mdcg" / f"{doc_id}.en.md")

for d in docs_with_images:
    process_doc(d)
