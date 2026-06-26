#!/usr/bin/env python3
"""Regenerate all other-standards Markdown display pages from JSON data files.
Ensures URLs in display layer match the corrected data layer.
"""
import json, glob, os, re

def truncate(s, maxlen=120):
    if not s:
        return ''
    s = s.replace('|', ' ').replace('\n', ' ').strip()
    return s[:maxlen] + '...' if len(s) > maxlen else s

def generate_md_table(standards, lang='en'):
    """Generate a markdown table from standards list."""
    if lang == 'zh':
        headers = "| 标准号 | 标题 | 状态 | 适用GSPRs | 官方链接 |"
        separator = "|--------|------|------|-----------|----------|"
    else:
        headers = "| Standard | Title | Status | GSPRs | Link |"
        separator = "|----------|-------|--------|-------|------|"
    
    rows = [headers, separator]
    for std in standards:
        number = std.get('number', '')
        title_obj = std.get('title', {})
        if isinstance(title_obj, dict):
            title = title_obj.get(lang, '') or title_obj.get('en', '')
        else:
            title = str(title_obj)
        title = truncate(title, 120)
        
        status = std.get('status', 'active')
        gsprs = ', '.join(std.get('applicable_gsprs', []))
        url = std.get('source_url', '')
        
        if url:
            if lang == 'zh':
                link = f"[官方链接]({url})"
            else:
                link = f"[Link]({url})"
        else:
            link = '-'
        
        rows.append(f"| {number} | {title} | {status} | {gsprs} | {link} |")
    
    return '\n'.join(rows)

def main():
    json_files = sorted(glob.glob('eu_mdr/other_standards/standards-*.json'))
    
    generated = 0
    for jf in json_files:
        with open(jf) as f:
            data = json.load(f)
        
        standards = data.get('standards', [])
        if not standards:
            continue
        
        # Derive category slug from filename
        cat_slug = jf.split('standards-')[-1].replace('.json', '')
        # Convert underscore to hyphen for URL
        page_slug = cat_slug.replace('_', '-')
        
        # Category display name
        cat_name = cat_slug.replace('_', ' ').title()
        
        for lang in ['zh', 'en']:
            md_dir = f"docs/{lang}/eu_mdr/other-standards"
            os.makedirs(md_dir, exist_ok=True)
            md_path = f"{md_dir}/{page_slug}.md"
            
            if lang == 'zh':
                title = f"# {cat_name} - 相关国际标准\n\n"
                intro = f"以下是与 **{cat_name}** 相关的非协调国际标准，供 EU MDR 合规参考。\n\n"
            else:
                title = f"# {cat_name} - Related International Standards\n\n"
                intro = f"The following non-harmonised international standards are related to **{cat_name}** for EU MDR compliance reference.\n\n"
            
            table = generate_md_table(standards, lang)
            
            content = title + intro + table + '\n'
            
            with open(md_path, 'w') as f:
                f.write(content)
            generated += 1
    
    print(f"Regenerated {generated} Markdown pages from {len(json_files)} JSON files.")

if __name__ == '__main__':
    main()
