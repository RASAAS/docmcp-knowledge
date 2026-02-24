import sys
from pathlib import Path
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.pipeline_options import PdfPipelineOptions
import yaml
import re

REPO_ROOT = Path(__file__).parent.parent
MDCG_DATA_DIR = REPO_ROOT / "eu_mdr" / "mdcg"

docs_with_missing_images = [
    "mdcg-2025-6"
]

def get_url(doc_id):
    md_file = MDCG_DATA_DIR / f"{doc_id}.zh.md"
    if not md_file.exists():
        return None
    content = md_file.read_text(encoding="utf-8")
    m = re.search(r'source_url:\s*(.+)$', content, re.M)
    if m:
        return m.group(1).strip()
    return None

import urllib3
urllib3.disable_warnings()

pipeline_options = PdfPipelineOptions()
pipeline_options.generate_picture_images = True
converter = DocumentConverter(format_options={'pdf': PdfFormatOption(pipeline_options=pipeline_options)})

def analyze(doc_id):
    print(f"\n--- {doc_id} ---")
    url = get_url(doc_id)
    if not url:
        print("No URL found")
        return
    try:
        conv_res = converter.convert(url)
        doc = conv_res.document
        items = list(doc.iterate_items())
        
        pic_count = 0
        for i, (element, level) in enumerate(items):
            if type(element).__name__ == "PictureItem":
                pic_count += 1
                
                # Get preceding 2 text items
                pre = []
                for j in range(i-1, max(-1, i-5), -1):
                    t = items[j][0]
                    if hasattr(t, "text") and t.text and len(t.text.strip()) > 5:
                        pre.insert(0, t.text.strip()[:100])
                        if len(pre) >= 2: break
                        
                # Get succeeding 2 text items
                post = []
                for j in range(i+1, min(len(items), i+5)):
                    t = items[j][0]
                    if hasattr(t, "text") and t.text and len(t.text.strip()) > 5:
                        post.append(t.text.strip()[:100])
                        if len(post) >= 2: break
                
                print(f"Image {pic_count}")
                if pre: print(f"  PRE : {pre[-1]}")
                else: print("  PRE : none")
                if post: print(f"  POST: {post[0]}")
                else: print("  POST: none")
                print()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    for d in docs_with_missing_images:
        analyze(d)
