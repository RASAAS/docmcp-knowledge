from pathlib import Path
import re

content = Path("eu_mdr/mdcg/fulltext/mdcg-2019-16.md").read_text()

# 1. Investigate Annex IV
print("--- Annex IV ---")
match = re.search(r'Annex IV.*?relationship\n(.*?)\n\n\n', content, re.DOTALL | re.IGNORECASE)
if match:
    print(match.group(0)[:500])
else:
    print("Annex IV not found by regex")
    
# 1.1 try another way to find Annex IV
idx = content.find("Annex IV")
if idx != -1:
    print(content[idx:idx+1000])

# 2. Investigate Section 4.3 list
print("\n--- Section 4.3 ---")
idx = content.find("4.3. Information to be provided to healthcare providers")
if idx != -1:
    print(content[idx:idx+1500])

# 3. Investigate Figure 1
print("\n--- Figure 1 ---")
idx = content.find("Figure 1: Cybersecurity requirements")
if idx != -1:
    print(content[max(0, idx-500):idx+200])

