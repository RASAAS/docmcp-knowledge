import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent

# We exclude mdcg-2025-6 because we deleted those dummy checkmarks.
docs_with_images = [
    "mdcg-2019-15", "mdcg-2019-16", "mdcg-2020-1", "mdcg-2020-3",
    "mdcg-2021-6", "mdcg-2022-5", "mdcg-2022-21", "mdcg-2024-10", "mdcg-2025-9"
]

def clean_text_for_search(text):
    if not text: return ""
    return re.sub(r'\s+', ' ', text).strip()

def find_best_insert_pos(content, pre, post):
    content_clean = re.sub(r'\s+', ' ', content)
    
    # Try post match first (putting image before post text)
    if post and len(post.strip()) > 5:
        post_clean = clean_text_for_search(post)
        idx = content_clean.find(post_clean)
        # Verify it is not matching the front-matter/title
        if idx != -1 and idx > 200:
            partial = post_clean[:20] if len(post_clean) > 20 else post_clean
            partial_esc = re.escape(partial).replace(r'\ ', r'\s+')
            m = re.search(partial_esc, content)
            if m: return m.start(), "before_post"
                
    # Try pre match (putting image after pre text)
    if pre and len(pre.strip()) > 5:
        pre_clean = clean_text_for_search(pre)
        idx = content_clean.find(pre_clean)
        if idx != -1:
            partial = pre_clean[-20:] if len(pre_clean) > 20 else pre_clean
            partial_esc = re.escape(partial).replace(r'\ ', r'\s+')
            m = re.search(partial_esc, content)
            if m: return m.end(), "after_pre"
                
    return -1, "none"

for doc_id in docs_with_images:
    json_file = REPO_ROOT / f"{doc_id}_img_contexts.json"
    if not json_file.exists(): continue
    contexts = json.loads(json_file.read_text("utf-8"))
        
    md_file = REPO_ROOT / "eu_mdr" / "mdcg" / "fulltext" / f"{doc_id}.md"
    
    if not md_file.exists(): continue
    content = md_file.read_text("utf-8")
    modifications = []
    
    for context in contexts:
        img_name = context["image"]
        if img_name in content: continue
            
        pos, strat = find_best_insert_pos(content, context["pre"], context["post"])
        if pos != -1:
            modifications.append({
                "pos": pos,
                "strat": strat,
                "text": f"\n\n![](/images/mdcg/{img_name})\n\n"
            })
    
    if modifications:
        modifications.sort(key=lambda x: x["pos"], reverse=True)
        for mod in modifications:
            pos = mod["pos"]
            content = content[:pos] + mod["text"] + content[pos:]
        md_file.write_text(content, "utf-8")
        print(f"Updated {md_file.relative_to(REPO_ROOT)}")
