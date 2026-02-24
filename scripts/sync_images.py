import re
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
docs_with_images = [
    "mdcg-2019-15", "mdcg-2019-16", "mdcg-2020-1", "mdcg-2020-3",
    "mdcg-2021-6", "mdcg-2022-5", "mdcg-2022-21", "mdcg-2024-10", "mdcg-2025-9",
    "mdcg-2025-6"
]

FULLTEXT_MARKER = "<!-- fulltext-start -->"
FULLTEXT_END_MARKER = "<!-- fulltext-end -->"

for doc_id in docs_with_images:
    fulltext_file = REPO_ROOT / "eu_mdr" / "mdcg" / "fulltext" / f"{doc_id}.md"
    if not fulltext_file.exists(): continue
    fulltext_content = fulltext_file.read_text("utf-8")
    
    # 按照 embed_fulltext_and_gen_en 的格式包装
    replacement_block = f"""{FULLTEXT_MARKER}

---

## 官方文件全文

{fulltext_content}

{FULLTEXT_END_MARKER}"""

    # We need to update:
    # 1. eu_mdr/mdcg/{doc_id}.zh.md
    # 2. eu_mdr/mdcg/{doc_id}.en.md
    # 3. docs/zh/eu_mdr/mdcg/{doc_id}.md
    # 4. docs/en/eu_mdr/mdcg/{doc_id}.md
    
    files_to_sync = [
        REPO_ROOT / "eu_mdr" / "mdcg" / f"{doc_id}.zh.md",
        REPO_ROOT / "eu_mdr" / "mdcg" / f"{doc_id}.en.md",
        REPO_ROOT / "docs" / "zh" / "eu_mdr" / "mdcg" / f"{doc_id}.md",
        REPO_ROOT / "docs" / "en" / "eu_mdr" / "mdcg" / f"{doc_id}.md",
    ]
    
    for f in files_to_sync:
        if not f.exists(): continue
        content = f.read_text("utf-8")
        if FULLTEXT_MARKER in content and FULLTEXT_END_MARKER in content:
            # We replace everything from FULLTEXT_MARKER to FULLTEXT_END_MARKER inclusive
            new_content = re.sub(
                f"{FULLTEXT_MARKER}.*?{FULLTEXT_END_MARKER}", 
                replacement_block, 
                content, 
                flags=re.DOTALL
            )
            f.write_text(new_content, "utf-8")
            print(f"Synced {f.relative_to(REPO_ROOT)}")
