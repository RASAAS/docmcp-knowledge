import re
from pathlib import Path

content = Path('eu_mdr/mdcg/fulltext/mdcg-2019-16.md').read_text()

# test figure 1
def repl_fig1(m):
    images = re.findall(r'(?:<!-- image -->|!\[.*?\]\(.*?\))', m.group(0))
    return '\n\n'.join(images) + '\n\n'
    
content = re.sub(
    r'General safety and performance requirements with focus on cybersecurity.*?1nт 1\. Cahraanetar enmmlenmonta\n+',
    repl_fig1,
    content,
    flags=re.DOTALL
)
if '![](/images/mdcg/mdcg-2019-16-fig01.png)' in content:
    print("Fig 1 image PRESERVED")

# test annex 4
def repl_annex4(m):
    images = re.findall(r'(?:<!-- image -->|!\[.*?\]\(.*?\))', m.group(0))
    rest = '\n\n'.join(images) + '\n\n'
    return 'The following figure illustrates the relationship between processes for cybersecurity risk management and safety risk management.\n\n' + rest

content = re.sub(
    r'Cybersecurity\n+Risk Evaluation\n+The following figure illustrates.*?Safety controls that\n+',
    repl_annex4,
    content,
    flags=re.DOTALL | re.IGNORECASE
)
if "Cybersecurity\n\nRisk Evaluation" not in content and '![](/images/mdcg/mdcg-2019-16-fig07.png)' in content:
    print("Annex 4 PRESERVED FIG 7 and removed noise")

# test 4.3 numbering
content, num_changes = re.subn(
    r'(A description of the methods.*?)\n+9\.\s*Where\s*appropriate,\s*risks',
    r'\1\n\n11. Where appropriate, risks',
    content,
    flags=re.DOTALL
)
if num_changes > 0:
    print("4.3 Numbering changed")
