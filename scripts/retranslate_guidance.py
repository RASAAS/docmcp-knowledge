#!/usr/bin/env python3
"""Retranslate FDA CDRH guidance fulltext with medical device regulatory terminology.

Reads English fulltext from EN guidance files, translates section-by-section
via LLM API, and replaces the ZH file's fulltext content.

Usage:
    python scripts/retranslate_guidance.py --slug general-wellness-policy-low-risk-devices --dry-run
    python scripts/retranslate_guidance.py --slug general-wellness-policy-low-risk-devices
    python scripts/retranslate_guidance.py --batch slugs.txt
"""

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path

try:
    import httpx
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "httpx"])
    import httpx

ROOT = Path(__file__).resolve().parent.parent
EN_DIR = ROOT / "docs" / "en" / "fda" / "guidance"
ZH_DIR = ROOT / "docs" / "zh" / "fda" / "guidance"

FULLTEXT_MARKER = "<!-- fulltext-start -->"

API_URL = os.getenv("LLM_PROXY_BASE_URL", "https://api.team-ra.org/v1")
API_KEY = os.getenv("LLM_PROXY_API_KEY", os.getenv("OPENAI_API_KEY", ""))
MODEL = os.getenv("LLM_PROXY_DEFAULT_MODEL", "reguverse-llm")

MAX_CHARS_PER_CHUNK = 12000  # ~3K tokens input, well within context
MAX_RETRIES = 2
RETRY_DELAY = 5

SYSTEM_PROMPT = """你是一位资深医疗器械法规翻译专家，精通FDA CDRH法规文件的中文翻译。

翻译要求：
1. 使用医疗器械合规领域的标准专业术语，不能直译
2. 核心术语对照：
   - medical device = 医疗器械（不是"医疗设备"）
   - premarket notification = 上市前通知
   - premarket approval (PMA) = 上市前批准(PMA)
   - 510(k) = 510(k)（保留原文）
   - De Novo = De Novo（保留原文）
   - Investigational Device Exemption (IDE) = 研究用器械豁免(IDE)
   - Humanitarian Device Exemption (HDE) = 人道主义器械豁免(HDE)
   - breakthrough device = 突破性器械
   - substantial equivalence = 实质等同
   - predicate device = 参比器械
   - intended use = 预期用途
   - indications for use = 适用范围
   - labeling = 标签/标签标识
   - postmarket surveillance = 上市后监督
   - adverse event = 不良事件
   - FDA = FDA（保留缩写）
   - CDRH = CDRH（保留缩写）
   - ethylene oxide = 环氧乙烷
   - biocompatibility = 生物相容性
   - clinical investigation = 临床研究
   - risk-benefit = 受益-风险
   - human factors = 人因工程
   - usability = 可用性
   - real-world evidence = 真实世界证据
   - in vitro diagnostic = 体外诊断
   - software as a medical device (SaMD) = 作为医疗器械的软件(SaMD)
   - quality system = 质量体系
   - design controls = 设计控制
   - verification and validation = 验证与确认
   - corrective and preventive action (CAPA) = 纠正和预防措施(CAPA)
   - unique device identification (UDI) = 唯一器械标识(UDI)

3. 格式要求：
   - 保持所有Markdown格式（标题层级、粗体、列表、表格等）
   - 保持所有URL链接原封不动
   - 保持法规编号原文（21 CFR Part 820, Section 513(f)(2)等）
   - 表格结构必须与原文一致（同样的列数和行数）
   - 脚注编号保持原文

4. 翻译风格：
   - 使用正式的法规文件语体
   - 句式流畅自然，避免翻译腔
   - 长句适当拆分，保持中文阅读节奏
   - 不添加原文没有的内容"""

USER_PROMPT_TEMPLATE = """请将以下FDA CDRH指南文件的英文内容翻译为中文。严格遵循系统提示中的术语对照表和翻译要求。

只输出翻译后的中文内容，不要添加任何说明、注释或翻译备注。保持原文的Markdown格式。

英文原文：
---
{content}
---"""


def extract_fulltext(filepath: Path) -> str:
    """Extract content after <!-- fulltext-start --> marker."""
    text = filepath.read_text(encoding="utf-8")
    marker_pos = text.find(FULLTEXT_MARKER)
    if marker_pos == -1:
        return ""
    return text[marker_pos + len(FULLTEXT_MARKER):].strip()


def extract_pre_fulltext(filepath: Path) -> str:
    """Extract content before and including <!-- fulltext-start --> marker."""
    text = filepath.read_text(encoding="utf-8")
    marker_pos = text.find(FULLTEXT_MARKER)
    if marker_pos == -1:
        return text
    return text[:marker_pos + len(FULLTEXT_MARKER)]


def split_into_sections(text: str) -> list[dict]:
    """Split markdown text into sections at ## headings."""
    sections = []
    current_heading = ""
    current_content = []
    
    for line in text.split("\n"):
        if re.match(r'^#{1,3}\s+', line) and current_content:
            content = "\n".join(current_content).strip()
            if content:
                sections.append({
                    "heading": current_heading,
                    "content": content,
                })
            current_heading = line
            current_content = [line]
        else:
            current_content.append(line)
    
    if current_content:
        content = "\n".join(current_content).strip()
        if content:
            sections.append({
                "heading": current_heading,
                "content": content,
            })
    
    return sections


def split_large_section(text: str, max_chars: int) -> list[str]:
    """Split a large section into smaller pieces at paragraph boundaries."""
    paragraphs = re.split(r'\n\n+', text)
    chunks = []
    current = []
    current_size = 0
    
    for para in paragraphs:
        if current_size + len(para) > max_chars and current:
            chunks.append("\n\n".join(current))
            current = [para]
            current_size = len(para)
        else:
            current.append(para)
            current_size += len(para)
    
    if current:
        chunks.append("\n\n".join(current))
    
    return chunks


def merge_small_sections(sections: list[dict], max_chars: int = MAX_CHARS_PER_CHUNK) -> list[str]:
    """Merge small sections into chunks that fit within max_chars.
    
    Sections larger than max_chars are further split at paragraph boundaries.
    """
    chunks = []
    current_chunk = []
    current_size = 0
    
    for section in sections:
        content = section["content"]
        
        # If a single section exceeds max_chars, split it further
        if len(content) > max_chars:
            # Flush current buffer first
            if current_chunk:
                chunks.append("\n\n".join(current_chunk))
                current_chunk = []
                current_size = 0
            # Split the large section
            sub_chunks = split_large_section(content, max_chars)
            chunks.extend(sub_chunks)
        elif current_size + len(content) > max_chars and current_chunk:
            chunks.append("\n\n".join(current_chunk))
            current_chunk = [content]
            current_size = len(content)
        else:
            current_chunk.append(content)
            current_size += len(content)
    
    if current_chunk:
        chunks.append("\n\n".join(current_chunk))
    
    return chunks


def translate_chunk(chunk: str, chunk_idx: int, total_chunks: int) -> str:
    """Translate a single chunk via LLM API."""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": USER_PROMPT_TEMPLATE.format(content=chunk)},
        ],
        "max_tokens": 16000,
        "temperature": 0.3,
        "enable_thinking": False,
    }
    
    for attempt in range(MAX_RETRIES + 1):
        try:
            print(f"  Translating chunk {chunk_idx+1}/{total_chunks} "
                  f"({len(chunk)} chars)...", end="", flush=True)
            
            with httpx.Client(timeout=300) as client:
                resp = client.post(
                    f"{API_URL}/chat/completions",
                    headers=headers,
                    json=payload,
                )
                resp.raise_for_status()
                data = resp.json()
            
            content = data["choices"][0]["message"]["content"]
            # Strip any markdown code fence wrapping
            if content.startswith("```") and content.endswith("```"):
                lines = content.split("\n")
                content = "\n".join(lines[1:-1])
            
            print(f" OK ({len(content)} chars)")
            return content
            
        except Exception as e:
            print(f" ERROR: {e}")
            if attempt < MAX_RETRIES:
                print(f"  Retrying in {RETRY_DELAY}s...")
                time.sleep(RETRY_DELAY)
            else:
                print(f"  FAILED after {MAX_RETRIES + 1} attempts")
                return f"[翻译失败: {e}]\n\n{chunk}"
    
    return chunk


def retranslate_file(slug: str, dry_run: bool = False) -> bool:
    """Retranslate a single guidance file."""
    en_file = EN_DIR / f"{slug}.md"
    zh_file = ZH_DIR / f"{slug}.md"
    
    if not en_file.exists():
        print(f"EN file not found: {en_file}")
        return False
    if not zh_file.exists():
        print(f"ZH file not found: {zh_file}")
        return False
    
    # Extract EN fulltext
    en_fulltext = extract_fulltext(en_file)
    if not en_fulltext:
        print(f"No fulltext marker in EN file: {slug}")
        return False
    
    print(f"\n{'='*60}")
    print(f"Retranslating: {slug}")
    print(f"EN fulltext: {len(en_fulltext)} chars")
    
    # Split into sections and merge into chunks
    sections = split_into_sections(en_fulltext)
    chunks = merge_small_sections(sections)
    
    print(f"Split into {len(sections)} sections, merged into {len(chunks)} chunks")
    
    if dry_run:
        for i, chunk in enumerate(chunks):
            print(f"  Chunk {i+1}: {len(chunk)} chars")
        print("(dry-run, skipping translation)")
        return True
    
    # Filter out near-empty chunks (< 50 chars) and merge them into adjacent chunks
    filtered_chunks = []
    for chunk in chunks:
        if len(chunk.strip()) < 50 and filtered_chunks:
            filtered_chunks[-1] = filtered_chunks[-1] + "\n\n" + chunk
        elif len(chunk.strip()) < 50:
            pass  # Skip leading empty chunks
        else:
            filtered_chunks.append(chunk)
    chunks = filtered_chunks
    
    print(f"After filtering: {len(chunks)} chunks")
    
    # Translate each chunk
    translated_chunks = []
    for i, chunk in enumerate(chunks):
        translated = translate_chunk(chunk, i, len(chunks))
        translated_chunks.append(translated)
        if i < len(chunks) - 1:
            time.sleep(2)  # Rate limiting
    
    # Assemble translated fulltext
    translated_fulltext = "\n\n".join(translated_chunks)
    
    # Clean up any leading/trailing "---" that LLM may add
    translated_fulltext = re.sub(r'^\s*---\s*\n', '', translated_fulltext)
    translated_fulltext = translated_fulltext.strip()
    
    # Get ZH pre-fulltext (frontmatter + metadata)
    zh_pre = extract_pre_fulltext(zh_file)
    
    # Write the new ZH file
    new_zh_content = zh_pre + "\n\n---\n\n" + translated_fulltext + "\n"
    zh_file.write_text(new_zh_content, encoding="utf-8")
    
    print(f"Written: {zh_file} ({len(new_zh_content)} chars)")
    return True


def main():
    parser = argparse.ArgumentParser(description="Retranslate FDA guidance fulltext")
    parser.add_argument("--slug", type=str, help="Single file slug to retranslate")
    parser.add_argument("--batch", type=str, help="File containing slugs (one per line)")
    parser.add_argument("--dry-run", action="store_true", help="Preview without translating")
    args = parser.parse_args()
    
    if not API_KEY:
        print("ERROR: No API key found. Set LLM_PROXY_API_KEY or OPENAI_API_KEY")
        sys.exit(1)
    
    slugs = []
    if args.slug:
        slugs = [args.slug]
    elif args.batch:
        with open(args.batch) as f:
            slugs = [line.strip() for line in f if line.strip() and not line.startswith("#")]
    else:
        print("ERROR: Specify --slug or --batch")
        sys.exit(1)
    
    success = 0
    for slug in slugs:
        if retranslate_file(slug, dry_run=args.dry_run):
            success += 1
    
    print(f"\n{'='*60}")
    print(f"Completed: {success}/{len(slugs)} files")


if __name__ == "__main__":
    main()
