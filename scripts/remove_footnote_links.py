import re
from pathlib import Path

dir_path = Path("/Users/michael/Library/CloudStorage/OneDrive-个人/coding/docmcp-knowledge/eu_mdr/mdcg/fulltext")

# Regex to match Markdown links: [text](url) -> keep text
markdown_link_pattern = re.compile(r'\[([^\]]*)\]\([^)]+\)')
# Regex to match raw URLs: http://... or https://...
raw_url_pattern = re.compile(r'https?://\S+')

def clean_footnotes(text):
    if "**Footnotes**" not in text:
        return text
    
    parts = text.split("**Footnotes**")
    pre_footnotes = parts[0]
    footnotes = parts[1]
    
    # Process footnotes line by line
    cleaned_lines = []
    for line in footnotes.split('\n'):
        # 1. Replace [text](url) with just text
        line = markdown_link_pattern.sub(r'\1', line)
        # 2. Remove raw URLs
        line = raw_url_pattern.sub('', line)
        
        # strip excessive spaces that might have been left
        line = line.replace(' :', ':').replace(' ,', ',').replace(' .', '.')
        cleaned_lines.append(line)
        
    return pre_footnotes + "**Footnotes**" + '\n'.join(cleaned_lines)

changed_files = 0
for file_path in dir_path.glob("*.md"):
    content = file_path.read_text("utf-8")
    new_content = clean_footnotes(content)
    if new_content != content:
        file_path.write_text(new_content, "utf-8")
        changed_files += 1

print(f"Processed {dir_path}")
print(f"Removed footnote links in {changed_files} files.")
