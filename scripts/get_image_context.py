import sys
import re
import json
from pathlib import Path
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.pipeline_options import PdfPipelineOptions

import urllib3
urllib3.disable_warnings()

REPO_ROOT = Path(__file__).parent.parent
MDCG_DATA_DIR = REPO_ROOT / "eu_mdr" / "mdcg"

docs_with_images = [
    "mdcg-2019-15", "mdcg-2019-16", "mdcg-2020-1", "mdcg-2020-3",
    "mdcg-2021-6", "mdcg-2022-5", "mdcg-2022-21", "mdcg-2024-10", "mdcg-2025-9"
] # EXCLUDING 2025-6 which are just table checkmarks

def get_url(doc_id):
    md_file = MDCG_DATA_DIR / f"{doc_id}.zh.md"
    if not md_file.exists(): return None
    content = md_file.read_text(encoding="utf-8")
    m = re.search(r'source_url:\s*(.+)$', content, re.M)
    return m.group(1).strip() if m else None

pipeline_options = PdfPipelineOptions()
pipeline_options.generate_picture_images = True
converter = DocumentConverter(format_options={'pdf': PdfFormatOption(pipeline_options=pipeline_options)})

def analyze(doc_id):
    url = get_url(doc_id)
    if not url: return
    try:
        doc = converter.convert(url).document
        items = list(doc.iterate_items())
        
        pic_count = 0
        img_contexts = []
        for i, (element, level) in enumerate(items):
            if type(element).__name__ == "PictureItem":
                pic_count += 1
                
                pre_text = ""
                for j in range(i-1, max(-1, i-5), -1):
                    t = items[j][0]
                    if hasattr(t, "text") and t.text and len(t.text.strip()) > 5:
                        pre_text = t.text.strip()
                        break
                        
                post_text = ""
                for j in range(i+1, min(len(items), i+5)):
                    t = items[j][0]
                    if hasattr(t, "text") and t.text and len(t.text.strip()) > 5:
                        post_text = t.text.strip()
                        break
                
                img_contexts.append({
                    "image": f"{doc_id}-fig{pic_count:02d}.png",
                    "pre": pre_text,
                    "post": post_text
                })
        
        # Save to JSON
        with open(REPO_ROOT / f"{doc_id}_img_contexts.json", "w", encoding="utf-8") as f:
            json.dump(img_contexts, f, indent=2, ensure_ascii=False)
            
    except Exception as e:
        print(f"Error for {doc_id}: {e}")

if __name__ == "__main__":
    for d in docs_with_images:
        print(f"Analyzing {d}...")
        analyze(d)
