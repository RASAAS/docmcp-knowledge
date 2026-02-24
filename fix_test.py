import re
from pathlib import Path

content = Path("eu_mdr/mdcg/fulltext/mdcg-2019-16.md").read_text()

# 1. fix diagram text in Figure 1 that looks like OCR mess
# This is highly specific.
content = re.sub(
    r'General safety and performance requirements with focus on cybersecurity.*?1nт 1\. Cahraanetar enmmlenmonta\n\n',
    '',
    content,
    flags=re.DOTALL
)

# 2. Fix the "Table 1: I" orphan header
content = re.sub(
    r'^Table 1:\s*I\n\nCorrespondence table between sections, relevant for this guidance, in MDR Annex I and IVDR Annex',
    'Table 1: Correspondence table between sections, relevant for this guidance, in MDR Annex I and IVDR Annex I',
    content,
    flags=re.MULTILINE
)

# 3. Numbered lists with weird bullets
content = re.sub(
    r'^(\d+\.)\s*(?:-\s*|[•➢o]\s+)+(.*)$',
    r'\1 \2',
    content,
    flags=re.MULTILINE
)

# 4. Abbreviations to table
# CE\n\nClinical Evaluation -> | CE | Clinical Evaluation |
import itertools
def repl_abbr(match):
    lines = [x.strip() for x in match.group(0).split('\n') if x.strip()]
    if len(lines) % 2 != 0:
        return match.group(0)
    out = ["| Abbreviation | Definition |", "|---|---|"]
    for i in range(0, len(lines), 2):
        out.append(f"| {lines[i]} | {lines[i+1]} |")
    return '\n'.join(out) + '\n\n'

# Only apply to the block under 1.5. Abbreviations up to the first markdown table or header
abbr_block_match = re.search(r'(###\s*1\.5\.\s*Abbreviations\n\n)(.*?)(?=\n\||\n#)', content, re.DOTALL)
if abbr_block_match:
    prefix = abbr_block_match.group(1)
    block = abbr_block_match.group(2)
    # the block contains pairs of lines. Some might be broken.
    lines = [l.strip() for l in block.split('\n') if l.strip()]
    out_table = ["| Abbreviation | Meaning |", "| --- | --- |"]
    for i in range(0, len(lines)-1, 2):
        out_table.append(f"| {lines[i]} | {lines[i+1]} |")
    content = content[:abbr_block_match.start()] + prefix + '\n'.join(out_table) + '\n\n' + content[abbr_block_match.end():]

# 5. Section 2.6.3 OCR mess
# "latest ess able a bug out the chine me cycle." -> delete
content = re.sub(r'latest ess able a bug out the chine me cycle\.\n\n', '', content)

# "Design and\n\nDevelopment version of software..." -> "Design and Development version of software..."
content = re.sub(r'Design and\n\nDevelopment version of software', 'Design and Development version of software', content)

# The cyclic diagram "Monitor\n\nMaintenance sub-cycle\n\nRelease" -> delete?
content = re.sub(r'Monitor\n\nMaintenance sub-cycle\n\nRelease\n\n', '', content)

# Annex I Section 4... list -> add bullets
content = re.sub(r'^(Annex I Section \d+.*?)$', r'- \1', content, flags=re.MULTILINE)


print("Testing regex replacements...")
path = Path("test_out.md")
path.write_text(content)
print("Done")
