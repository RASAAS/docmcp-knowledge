import re
from pathlib import Path

content = Path('eu_mdr/mdcg/fulltext/mdcg-2025-4.md').read_text()

# 1. Strip glued headers first
content, n_glued = re.subn(
    r'^(?:#+\s*)?Medical Device(?:s)?\sCoordination Group Document(?:\sMDCG\s\d{4}-\d+[a-zA-Z0-9-]*)?(?:\s+rev\.\s*\d+)?\s+([a-z].*)$',
    r'\1',
    content,
    flags=re.MULTILINE | re.IGNORECASE
)
print(f"Glued headers fixed: {n_glued}")
if "required  information  about  traders" in content:
    print("Content preserved.")

# Also test standalone headers match
header_patterns = [
    re.compile(r'^(#+\s*)?(Medical Device(s)?(\sCoordination Group Document)?(\sMDCG\s\d{4}-\d+.*)?)$', re.IGNORECASE),
    re.compile(r'^(#+\s*)?(MDCG\s\d{4}-\d+.*)$', re.IGNORECASE), # e.g. MDCG 2019-15 rev.1
    re.compile(r'^(#+\s*)?(Page\s\d+\sof\s\d+)$', re.IGNORECASE),
]

standalone = "## Medical Device Coordination Group Document MDCG 2025-4"
for pat in header_patterns:
    if pat.match(standalone):
        print("Standalone header matches!")
        break

