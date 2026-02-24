#!/usr/bin/env python3
import sys
import re
from pathlib import Path

try:
    from docling.document_converter import DocumentConverter, PdfFormatOption
    from docling.datamodel.pipeline_options import PdfPipelineOptions
except ImportError:
    print("pip install docling first!")
    sys.exit(1)

REPO_ROOT = Path(__file__).parent.parent
FULLTEXT_DIR = REPO_ROOT / "eu_mdr" / "mdcg" / "fulltext"
ZH_DIR = REPO_ROOT / "docs" / "zh" / "eu_mdr" / "mdcg"
EN_DIR = REPO_ROOT / "docs" / "en" / "eu_mdr" / "mdcg"
IMG_PUB_DIR = REPO_ROOT / "docs" / "public" / "images" / "mdcg"
ASSET_DIR = REPO_ROOT / "assets" / "images" / "mdcg"

def get_source_url(doc_id):
    zh_file = ZH_DIR / f"{doc_id}.md"
    if not zh_file.exists():
        zh_file = REPO_ROOT / "eu_mdr" / "mdcg" / f"{doc_id}.zh.md"
        if not zh_file.exists():
            return None
    content = zh_file.read_text(encoding="utf-8")
    for line in content.split("\n"):
        if line.startswith("source_url:"):
            url = line.split("source_url:", 1)[1].strip()
            return url
    return None

def process_doc(doc_id):
    url = get_source_url(doc_id)
    if not url:
        print(f"Skipping {doc_id}: no source url found")
        return

    print(f"\nProcessing {doc_id} from {url}")
    
    pipeline_options = PdfPipelineOptions()
    pipeline_options.do_ocr = False
    pipeline_options.do_table_structure = True
    pipeline_options.images_scale = 2.0
    pipeline_options.generate_picture_images = True

    converter = DocumentConverter(
        format_options={"pdf": PdfFormatOption(pipeline_options=pipeline_options)}
    )
    try:
        result = converter.convert(url)
    except Exception as e:
        print(f"Failed to fetch or convert {url}: {e}")
        return
        
    doc = result.document

    IMG_PUB_DIR.mkdir(parents=True, exist_ok=True)
    
    img_list = []
    
    img_idx = 0
    for element, _level in doc.iterate_items():
        elem_type = type(element).__name__
        if elem_type == "PictureItem" and hasattr(element, "image") and element.image:
            img_idx += 1
            img_filename = f"{doc_id}-fig{img_idx:02d}.png"
            img_path = IMG_PUB_DIR / img_filename
            try:
                element.image.pil_image.save(img_path, format="PNG")
                ASSET_DIR.mkdir(parents=True, exist_ok=True)
                element.image.pil_image.save(ASSET_DIR / img_filename, format="PNG")
                img_url = f"/images/mdcg/{img_filename}"
                img_list.append(img_url)
                print(f"  Saved {img_filename}")
            except Exception as e:
                print(f"  Failed to save {img_filename}: {e}")
                
    if not img_list:
        print(f"  No images found in docling parsed doc for {doc_id}")
        return

    def replace_in_file(file_path):
        if not file_path.exists():
            return
        content = file_path.read_text(encoding="utf-8")
        if "<!-- image -->" not in content:
            return
            
        print(f"  Replacing in {file_path.name}")
        iter_imgs = iter(img_list)
        def repl(m):
            try:
                img_url = next(iter_imgs)
                return f"![]({img_url})"
            except StopIteration:
                print(f"  WARNING: More <!-- image --> markers than extracted images in {file_path.name}!")
                return m.group(0) # Not enough images extracted
        
        new_content = re.sub(r'<!-- image -->', repl, content)
        
        # Check if there are remaining images
        remaining = list(iter_imgs)
        if remaining:
            print(f"  WARNING: Extracted {len(img_list)} images, but only used {len(img_list) - len(remaining)} in {file_path.name}")
            
        file_path.write_text(new_content, encoding="utf-8")
        
    replace_in_file(FULLTEXT_DIR / f"{doc_id}.md")
    replace_in_file(ZH_DIR / f"{doc_id}.md")
    replace_in_file(EN_DIR / f"{doc_id}.md")
    replace_in_file(REPO_ROOT / "eu_mdr" / "mdcg" / f"{doc_id}.zh.md")
    replace_in_file(REPO_ROOT / "eu_mdr" / "mdcg" / f"{doc_id}.en.md")
    
    # Let's also copy the images to assets/images/mdcg if needed? doc:build copies assets/images to docs/public/images
    # So actually, it's better to save directly to assets/images/mdcg! Let's do that.
    
if __name__ == "__main__":
    docs_with_images = [
        "mdcg-2019-15",
        "mdcg-2019-16",
        "mdcg-2020-1",
        "mdcg-2020-3",
        "mdcg-2021-6",
        "mdcg-2021-8",
        "mdcg-2022-5",
        "mdcg-2022-21",
        "mdcg-2023-1",
        "mdcg-2023-7",
        "mdcg-2024-10",
        "mdcg-2025-6",
        "mdcg-2025-9"
    ]
    for doc in docs_with_images:
        process_doc(doc)
