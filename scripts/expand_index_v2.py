"""Expand index with valid guidance documents from _unmatched/ directory.

Filters out:
- Drafts (征求意见稿)
- Catalog content (目录, 清单)
- Non-guidance docs (征集表, 调研问卷, etc.)
- Documents already matching existing entries (title similarity >= 0.5)
- Old versions of already-indexed documents (same core title, different year)
"""

import json
import re
import shutil
import hashlib
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fetch_nmpa_fulltext import (
    extract_actual_title, _title_similarity, fulltext_exists,
    content_matches_title, is_draft_content, is_catalog_content,
    FULLTEXT_DIR, INDEX_PATH
)

ROOT = Path(__file__).resolve().parent.parent
UNMATCHED_DIR = ROOT / "nmpa" / "guidance" / "_unmatched"

NOT_GUIDANCE_PATTERNS = [
    r'征集表',
    r'标准目录',
    r'调研问卷',
    r'修改内容说明',
    r'征求意见$',
    r'质量管理规范',
    r'现场检查指导',
    r'免于.*目录',
    r'参与单位信息',
    r'主任专题会',
    r'汇报稿',
    r'药品.*指导',
    r'临床研究技术指导原则$',
]
NOT_GUIDANCE_RE = re.compile('|'.join(NOT_GUIDANCE_PATTERNS))


def strip_year_revision(title: str) -> str:
    """Remove year/revision markers and normalize suffix."""
    t = re.sub(r'[（(]\d{4}年?\s*修订版[）)]', '', title)
    t = re.sub(r'注册技术审查指导原则', '注册审查指导原则', t)
    t = re.sub(r'注册技术指导原则', '注册审查指导原则', t)
    t = re.sub(r'技术审查指导原则', '审查指导原则', t)
    return t.strip()


def title_to_slug(title: str) -> str:
    """Generate slug from Chinese title."""
    h = hashlib.md5(title.encode()).hexdigest()[:6]
    short = title[:20].replace(' ', '-').replace('/', '-')
    return f"nmpa-gp-{short}-{h}"


def categorize_title(title: str) -> str:
    """Guess category from title keywords."""
    cats = {
        "ivd": ["体外诊断", "试剂", "测定", "检测", "诊断试剂", "标志物", "基因",
                "免疫", "抗体", "抗原", "核酸", "血型", "生化"],
        "surgical": ["手术", "内窥镜", "腹腔镜", "气腹", "电凝", "刀", "钳",
                     "穿刺"],
        "implant_ortho": ["骨", "关节", "脊柱", "椎体", "髓内", "假体", "植入",
                          "钉", "板", "螺钉"],
        "implant_cardio": ["心脏", "血管", "支架", "导管", "瓣膜", "起搏",
                           "心肺", "体外循环", "ECMO"],
        "dental": ["牙科", "口腔", "义齿", "牙", "种植"],
        "imaging": ["超声", "X射线", "CT", "MRI", "影像", "内窥镜"],
        "monitoring": ["监护", "血压", "体温", "血氧", "生命体征"],
        "respiratory": ["呼吸", "麻醉", "雾化", "通气", "吸引"],
        "infusion_injection": ["输液", "输注", "注射", "穿刺", "导管"],
        "wound_care": ["敷料", "创面", "凡士林纱布"],
        "rehab_physio": ["康复", "理疗", "电疗", "生物反馈", "训练", "加压",
                         "防褥疮"],
        "ophthalmic": ["眼科", "视网膜", "角膜", "飞秒"],
        "blood_transfusion": ["血液", "血浆", "输血", "血型", "采血"],
        "reproductive": ["宫内", "辅助生殖", "胚胎", "妇科"],
        "sterilization": ["灭菌", "消毒", "生物相容"],
        "lab_equipment": ["实验室", "分析仪", "培养箱"],
        "radiation_therapy": ["放射", "质子", "碳离子", "加速器"],
        "software_ai": ["软件", "人工智能", "AI", "算法"],
    }
    for cat, keywords in cats.items():
        for kw in keywords:
            if kw in title:
                return cat
    return "general"


def main():
    with open(INDEX_PATH) as f:
        data = json.load(f)
    entries = data.get("entries", [])

    all_titles = {}
    for e in entries:
        t = e.get("title", {})
        zh = t.get("zh", "") if isinstance(t, dict) else str(t)
        all_titles[e["id"]] = zh

    all_titles_stripped = {eid: strip_year_revision(t) for eid, t in all_titles.items()}

    unmatched_files = sorted(UNMATCHED_DIR.glob("*.md"))
    print(f"Unmatched files: {len(unmatched_files)}")
    print(f"Current index entries: {len(entries)}")

    added = 0
    skipped_dup = 0
    skipped_draft = 0
    skipped_catalog = 0
    skipped_non_guidance = 0
    skipped_old_version = 0

    for f in unmatched_files:
        text = f.read_text(encoding="utf-8")
        title = extract_actual_title(text[:3000]) or f.stem

        if is_draft_content(text[:5000]):
            skipped_draft += 1
            continue

        if is_catalog_content(text[:5000]):
            skipped_catalog += 1
            continue

        if NOT_GUIDANCE_RE.search(title):
            skipped_non_guidance += 1
            continue

        best_sim = 0
        for eid, t in all_titles.items():
            sim = _title_similarity(title, t)
            if sim > best_sim:
                best_sim = sim

        if best_sim >= 0.5:
            skipped_dup += 1
            continue

        title_stripped = strip_year_revision(title)
        for eid, t_stripped in all_titles_stripped.items():
            sim = _title_similarity(title_stripped, t_stripped)
            if sim >= 0.7:
                skipped_old_version += 1
                break
        else:
            cat = categorize_title(title)
            eid = f"nmpa-gp-{hashlib.md5(title.encode()).hexdigest()[:12]}"
            slug = title_to_slug(title)

            new_entry = {
                "id": eid,
                "title": {"zh": title, "en": ""},
                "doc_number": "",
                "category": cat,
                "slug": slug,
            }
            entries.append(new_entry)
            all_titles[eid] = title
            all_titles_stripped[eid] = strip_year_revision(title)

            dest = FULLTEXT_DIR / f"{slug}.zh.md"
            shutil.copy2(f, dest)
            f.unlink()

            added += 1
            print(f"  ADD [{cat}]: {title[:60]} -> {slug}")

    print(f"\nResults:")
    print(f"  Added to index: {added}")
    print(f"  Skipped (duplicate title): {skipped_dup}")
    print(f"  Skipped (draft): {skipped_draft}")
    print(f"  Skipped (catalog): {skipped_catalog}")
    print(f"  Skipped (non-guidance): {skipped_non_guidance}")
    print(f"  Skipped (old version): {skipped_old_version}")

    if added > 0:
        data["entries"] = entries
        with open(INDEX_PATH, "w") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"\nSaved index with {len(entries)} entries")


if __name__ == "__main__":
    main()
