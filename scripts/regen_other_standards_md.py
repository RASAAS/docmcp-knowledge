#!/usr/bin/env python3
"""
Regenerate VitePress markdown pages for EU MDR other-standards from JSON data.

Reads all eu_mdr/other_standards/standards-*.json and regenerates:
  - docs/zh/eu_mdr/other-standards/<category>.md
  - docs/en/eu_mdr/other-standards/<category>.md
"""

import json
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
JSON_DIR = REPO / "eu_mdr" / "other_standards"
ZH_OUT = REPO / "docs" / "zh" / "eu_mdr" / "other-standards"
EN_OUT = REPO / "docs" / "en" / "eu_mdr" / "other-standards"

CATEGORY_LABELS = {
    "active_implants": {"en": "Active Implants", "zh": "有源植入物"},
    "additive_manufacturing": {"en": "Additive Manufacturing (3D Printing)", "zh": "增材制造(3D打印)"},
    "ai_ml": {"en": "AI and Machine Learning", "zh": "AI与机器学习"},
    "anaesthesia": {"en": "Anaesthesia Equipment", "zh": "麻醉设备"},
    "annex_xvi": {"en": "Annex XVI (Non-medical Purpose)", "zh": "Annex XVI (非医疗目的)"},
    "assistive_technology": {"en": "Assistive Technology", "zh": "辅助技术"},
    "audiology": {"en": "Audiology", "zh": "听力学"},
    "biocompatibility": {"en": "Biocompatibility", "zh": "生物相容性"},
    "biological_materials": {"en": "Biological Materials", "zh": "生物来源材料"},
    "breathing_gas_pathways": {"en": "Breathing Gas Pathways", "zh": "呼吸气路"},
    "cardiology": {"en": "Cardiology", "zh": "心血管"},
    "clinical_investigation": {"en": "Clinical Investigation", "zh": "临床调查"},
    "connectors": {"en": "Small-bore Connectors", "zh": "小口径连接器"},
    "cybersecurity": {"en": "Cybersecurity", "zh": "网络安全"},
    "dental": {"en": "Dental", "zh": "牙科"},
    "diagnostic_imaging": {"en": "Diagnostic Imaging", "zh": "诊断成像"},
    "dialysis": {"en": "Dialysis", "zh": "透析"},
    "digital_health_wearables": {"en": "Digital Health & Wearables", "zh": "数字健康与可穿戴"},
    "drug_device_combination": {"en": "Drug-Device Combination", "zh": "药械组合"},
    "electrical_safety": {"en": "Electrical Safety & EMC", "zh": "电气安全与EMC"},
    "endoscopy": {"en": "Endoscopy", "zh": "内窥镜"},
    "environmental_testing": {"en": "Environmental Testing", "zh": "环境测试"},
    "home_healthcare": {"en": "Home Healthcare", "zh": "家用医疗"},
    "implant_materials": {"en": "Implant Materials", "zh": "植入材料"},
    "implant_testing": {"en": "Implant Testing", "zh": "植入物测试"},
    "infusion_transfusion": {"en": "Infusion & Transfusion", "zh": "输液与输血"},
    "ivd": {"en": "In Vitro Diagnostics", "zh": "体外诊断"},
    "labelling": {"en": "Labelling & Symbols", "zh": "标签与符号"},
    "laser_surgery": {"en": "Laser Surgery", "zh": "激光手术"},
    "lithotripsy": {"en": "Lithotripsy", "zh": "碎石术"},
    "mechanical_testing": {"en": "Mechanical Testing", "zh": "机械测试"},
    "medical_gloves": {"en": "Medical Gloves", "zh": "医用手套"},
    "mri_safety": {"en": "MRI Safety", "zh": "MRI 安全"},
    "neonatal": {"en": "Neonatal", "zh": "新生儿"},
    "needles_syringes": {"en": "Needles & Syringes", "zh": "针头与注射器"},
    "neurology": {"en": "Neurology", "zh": "神经学"},
    "nuclear_medicine": {"en": "Nuclear Medicine", "zh": "核医学"},
    "ophthalmic": {"en": "Ophthalmic", "zh": "眼科"},
    "packaging": {"en": "Packaging", "zh": "包装"},
    "patient_monitoring": {"en": "Patient Monitoring", "zh": "患者监护"},
    "patient_warming": {"en": "Patient Warming", "zh": "患者加温"},
    "phototherapy": {"en": "Phototherapy", "zh": "光疗"},
    "physiotherapy": {"en": "Physiotherapy", "zh": "物理治疗"},
    "pms": {"en": "Post-market Surveillance", "zh": "上市后监督"},
    "point_of_care_testing": {"en": "Point-of-Care Testing (POCT)", "zh": "即时检验(POCT)"},
    "ppe_barrier": {"en": "PPE & Barrier", "zh": "防护设备"},
    "quality_management": {"en": "Quality Management", "zh": "质量管理"},
    "radiation_protection": {"en": "Radiation Protection", "zh": "辐射防护"},
    "regulatory_references": {"en": "Regulatory References", "zh": "法规参考"},
    "reprocessing": {"en": "Reprocessing", "zh": "再处理"},
    "respiratory_anaesthesia": {"en": "Respiratory & Anaesthesia", "zh": "呼吸与麻醉"},
    "risk_management": {"en": "Risk Management", "zh": "风险管理"},
    "robotic_surgery": {"en": "Robotic Surgery", "zh": "手术机器人"},
    "software": {"en": "Software & Usability", "zh": "软件与可用性"},
    "sterilization": {"en": "Sterilization", "zh": "灭菌"},
    "surgical_implants": {"en": "Surgical Implants", "zh": "外科植入物"},
    "surgical_instruments": {"en": "Surgical Instruments", "zh": "手术器械"},
    "therapeutic_ultrasound": {"en": "Therapeutic Ultrasound", "zh": "治疗超声"},
    "tissue_engineering": {"en": "Tissue Engineering", "zh": "组织工程"},
    "urogenital": {"en": "Urogenital", "zh": "泌尿生殖"},
    "usability": {"en": "Usability Engineering", "zh": "可用性工程"},
    "vascular_devices": {"en": "Vascular Devices", "zh": "血管器械"},
    "wound_care": {"en": "Wound Care", "zh": "伤口护理"},
}


def json_key_to_md_slug(key: str) -> str:
    return key.replace("_", "-")


def generate_zh_page(category_key: str, standards: list) -> str:
    label = CATEGORY_LABELS.get(category_key, {}).get("zh", category_key)
    lines = [
        f"# {label} - 相关国际标准",
        "",
        f"以下是与 **{label}** 相关的非协调国际标准，供 EU MDR 合规参考。",
        "",
        "| 标准号 | 标题 | 状态 | 适用GSPRs | 官方链接 |",
        "|--------|------|------|-----------|----------|",
    ]
    for s in standards:
        number = s.get("number", "")
        title_zh = s.get("title", {})
        if isinstance(title_zh, dict):
            title = title_zh.get("zh", title_zh.get("en", ""))
        else:
            title = str(title_zh)
        title = title.replace("|", "/")
        status = s.get("status", "active")
        gsprs = s.get("applicable_gsprs", [])
        if isinstance(gsprs, list):
            gsprs_str = ", ".join(str(g) for g in gsprs)
        else:
            gsprs_str = str(gsprs)
        url = s.get("source_url", "")
        lines.append(f"| {number} | {title} | {status} | {gsprs_str} | [官方链接]({url}) |")
    lines.append("")
    return "\n".join(lines)


def generate_en_page(category_key: str, standards: list) -> str:
    label = CATEGORY_LABELS.get(category_key, {}).get("en", category_key)
    lines = [
        f"# {label} - Related International Standards",
        "",
        f"The following non-harmonised international standards are related to **{label}** for EU MDR compliance reference.",
        "",
        "| Standard | Title | Status | GSPRs | Link |",
        "|----------|-------|--------|-------|------|",
    ]
    for s in standards:
        number = s.get("number", "")
        title_obj = s.get("title", {})
        if isinstance(title_obj, dict):
            title = title_obj.get("en", title_obj.get("zh", ""))
        else:
            title = str(title_obj)
        title = title.replace("|", "/")
        status = s.get("status", "active")
        gsprs = s.get("applicable_gsprs", [])
        if isinstance(gsprs, list):
            gsprs_str = ", ".join(str(g) for g in gsprs)
        else:
            gsprs_str = str(gsprs)
        url = s.get("source_url", "")
        lines.append(f"| {number} | {title} | {status} | {gsprs_str} | [Link]({url}) |")
    lines.append("")
    return "\n".join(lines)


def main():
    ZH_OUT.mkdir(parents=True, exist_ok=True)
    EN_OUT.mkdir(parents=True, exist_ok=True)

    json_files = sorted(JSON_DIR.glob("standards-*.json"))
    total_standards = 0
    categories_updated = 0

    for jf in json_files:
        category_key = jf.stem.replace("standards-", "")
        slug = json_key_to_md_slug(category_key)

        try:
            data = json.loads(jf.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError) as e:
            print(f"  [ERROR] {jf.name}: {e}")
            continue

        standards = data.get("standards", [])
        count = len(standards)
        total_standards += count

        zh_path = ZH_OUT / f"{slug}.md"
        en_path = EN_OUT / f"{slug}.md"

        zh_content = generate_zh_page(category_key, standards)
        en_content = generate_en_page(category_key, standards)

        zh_path.write_text(zh_content, encoding="utf-8")
        en_path.write_text(en_content, encoding="utf-8")

        categories_updated += 1
        print(f"  [{count:3d}] {slug}")

    print(f"\nDone: {categories_updated} categories, {total_standards} total standards.")


if __name__ == "__main__":
    main()
