import re
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
FULLTEXT_DIR = REPO_ROOT / "eu_mdr" / "mdcg" / "fulltext"
FULLTEXT_MARKER = "<!-- fulltext-start -->"
FULLTEXT_END_MARKER = "<!-- fulltext-end -->"

def main():
    synced_count = 0
    for fulltext_file in FULLTEXT_DIR.glob("*.md"):
        doc_id = fulltext_file.stem
        fulltext_content = fulltext_file.read_text("utf-8")
        
        files_to_sync = [
            (REPO_ROOT / "eu_mdr" / "mdcg" / f"{doc_id}.zh.md", "zh"),
            (REPO_ROOT / "eu_mdr" / "mdcg" / f"{doc_id}.en.md", "en"),
            (REPO_ROOT / "docs" / "zh" / "eu_mdr" / "mdcg" / f"{doc_id}.md", "zh"),
            (REPO_ROOT / "docs" / "en" / "eu_mdr" / "mdcg" / f"{doc_id}.md", "en"),
        ]
        
        for f, lang in files_to_sync:
            if not f.exists(): 
                continue
            
            heading = "官方文件全文" if lang == "zh" else "Official Full Text"
            replacement_block = f"{FULLTEXT_MARKER}\n\n---\n\n## {heading}\n\n{fulltext_content}\n\n{FULLTEXT_END_MARKER}"
            
            content = f.read_text("utf-8")
            if FULLTEXT_MARKER in content and FULLTEXT_END_MARKER in content:
                new_content = re.sub(
                    f"{FULLTEXT_MARKER}.*?{FULLTEXT_END_MARKER}", 
                    replacement_block, 
                    content, 
                    flags=re.DOTALL
                )
                if content != new_content:
                    f.write_text(new_content, "utf-8")
                    print(f"Synced {f.relative_to(REPO_ROOT)}")
                    synced_count += 1
    
    print(f"\nSuccessfully synced {synced_count} files across all translated MDs.")

if __name__ == '__main__':
    main()
