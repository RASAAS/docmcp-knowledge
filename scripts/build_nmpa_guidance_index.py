#!/usr/bin/env python3
"""Build NMPA guidance _index.json from the markdown list of 691 guidance documents.

Classification follows the CMDE official medical device classification catalog (22 categories)
plus cross-cutting/general categories.
"""

import json
import re
import hashlib
from pathlib import Path

GUIDANCE_MD = Path(__file__).parent.parent.parent / "reference" / "global_regulations" / "NMPA" / "NMPA指导原则清单_updated_2026.02.28.md"
OUTPUT = Path(__file__).parent.parent / "nmpa" / "guidance" / "_index.json"

CATEGORIES = {
    "general": {"zh": "通用指南", "en": "General / Cross-cutting Guidance"},
    "ivd": {"zh": "体外诊断试剂", "en": "In Vitro Diagnostics (IVD)"},
    "implant_ortho": {"zh": "骨科植入物", "en": "Orthopedic Implants"},
    "implant_cardio": {"zh": "心血管植入物与介入器械", "en": "Cardiovascular Implants & Interventional Devices"},
    "imaging": {"zh": "医用成像设备", "en": "Medical Imaging Equipment"},
    "respiratory": {"zh": "呼吸/麻醉/急救设备", "en": "Respiratory / Anesthesia / Emergency"},
    "surgical": {"zh": "手术器械与内窥镜", "en": "Surgical Instruments & Endoscopes"},
    "dental": {"zh": "口腔器械", "en": "Dental Devices"},
    "ophthalmic": {"zh": "眼科器械", "en": "Ophthalmic Devices"},
    "rehab_physio": {"zh": "康复理疗设备", "en": "Rehabilitation & Physiotherapy"},
    "wound_care": {"zh": "创面敷料/护理", "en": "Wound Care & Dressings"},
    "blood_transfusion": {"zh": "血液/输血/透析", "en": "Blood / Transfusion / Dialysis"},
    "infusion_injection": {"zh": "注输/护理器械", "en": "Infusion / Injection / Nursing Devices"},
    "sterilization": {"zh": "消毒灭菌设备", "en": "Sterilization & Disinfection"},
    "software_ai": {"zh": "医疗器械软件/AI", "en": "Medical Device Software / AI"},
    "tcm": {"zh": "中医器械", "en": "Traditional Chinese Medicine Devices"},
    "reproductive": {"zh": "辅助生殖/妇产科", "en": "Reproductive / Obstetrics & Gynecology"},
    "monitoring": {"zh": "监护/诊察设备", "en": "Patient Monitoring & Diagnostic Devices"},
    "radiation_therapy": {"zh": "放射治疗设备", "en": "Radiation Therapy Equipment"},
    "lab_equipment": {"zh": "实验室设备", "en": "Laboratory Equipment"},
    "other": {"zh": "其他专用器械", "en": "Other Specialized Devices"},
}

# Keyword-based classification rules (order matters - first match wins)
RULES = [
    # General / cross-cutting
    ("general", [
        "临床评价技术指导原则", "临床试验设计指导原则", "临床试验数据递交",
        "真实世界数据", "注册单元划分", "注册申请电子提交", "优先审批",
        "创新医疗器械", "附条件批准", "安全和性能基本原则", "受益-风险判定",
        "产品技术要求编写", "原材料变化评价", "稳定性研究指导", "有源医疗器械使用期限",
        "可用性工程", "网络安全注册", "光辐射安全", "已知可沥滤物",
        "临床评价等同性", "临床评价报告", "决策是否开展", "免于临床评价",
        "免于临床试验", "动物试验研究注册审查", "药械组合",
        "罕见病", "纳米材料", "境外临床试验数据",
        "移动医疗器械", "远程监测系统", "医疗器械软件注册", "人工智能医疗器械",
        "体外诊断试剂说明书编写", "体外诊断试剂临床试验技术",
        "体外诊断试剂变更注册", "体外诊断试剂主要原材料",
        "体外诊断试剂稳定性研究", "定量检测体外诊断试剂分析性能",
        "定性检测体外诊断试剂分析性能", "参考区间确定",
        "质控品注册", "来源于人的生物样本库",
        "家用体外诊断医疗器械", "增材制造", "3D打印",
        "个性化匹配骨植入物", "癌症筛查体外诊断试剂临床评价",
        "生物学评价", "含药医疗器械", "注册申报资料",
        "动物源性", "同种异体", "病毒灭活",
        "重组人源化胶原蛋白原材料", "真实世界研究设计",
        "人工智能辅助检测", "无源植入性医疗器械产品注册",
        "无源植入性医疗器械临床试验审批",
    ]),
    # IVD - very large category
    ("ivd", [
        "检测试剂", "测定试剂", "检测试剂盒", "分析仪注册审查",
        "IgM", "IgG", "抗体检测", "核酸检测", "基因检测", "基因分型",
        "基因突变检测", "伴随诊断", "PCR", "荧光原位杂交",
        "免疫层析", "酶联免疫", "化学发光", "胶体金",
        "血细胞分析仪", "凝血分析仪", "生化分析仪", "糖化血红蛋白分析仪",
        "尿液分析仪", "尿液有形成分", "电解质分析仪",
        "流式细胞仪", "液相色谱", "特定蛋白免疫分析仪",
        "实时荧光PCR", "基因测序仪", "微量元素分析仪",
        "血流变分析仪",
        "血型抗原检测", "血型分析仪", "人红细胞反定型",
        "鉴定试剂", "尿液分析试纸",
        "结直肠癌筛查体外诊断",
        "体外诊断试剂分析性能评估",
    ]),
    # Software / AI
    ("software_ai", [
        "辅助检测软件", "辅助诊断软件", "PACS", "中央监护软件",
    ]),
    # Orthopedic implants
    ("implant_ortho", [
        "骨科", "骨植入", "骨水泥", "髋关节", "膝关节", "肩关节", "肘关节",
        "椎间融合", "脊柱", "椎体成形", "椎板", "髓内钉", "接骨板",
        "金属接骨板", "骨针", "肌腱韧带", "骨外固定", "颅骨修补",
        "颅颌面", "漏斗胸", "人工韧带", "听小骨", "肋骨板", "胸骨捆扎",
        "可降解镁金属", "骨科植入物抗菌", "可吸收骨内固定",
        "金属缆线", "高强韧性纯钛",
        "人工颈椎间盘", "股骨柄", "I型胶原软骨修复",
        "硬脑（脊）膜补片", "脑积水分流器",
    ]),
    # Cardiovascular
    ("implant_cardio", [
        "冠状动脉", "心脏", "主动脉", "药物洗脱支架", "球囊扩张导管",
        "药物涂层球囊", "血管内导管", "血管内导丝", "血管内回收",
        "微导管", "体外膜", "ECMO", "左心室辅助", "起搏器",
        "射频消融导管", "电极导线", "颅内弹簧圈", "颅内取栓",
        "非血管自扩张金属支架", "带有润滑涂层", "经导管主动脉瓣膜",
        "血管夹", "球囊充压装置",
        "手术电极注册", "中心静脉导管", "体外循环管道",
        "膜式氧合器",
    ]),
    # Imaging
    ("imaging", [
        "X射线", "CT", "磁共振", "超声诊断", "正电子发射", "PET",
        "乳腺X射线", "骨密度仪", "眼科光学相干", "超声经颅多普勒",
        "影像型超声", "X射线计算机体层", "SPECT",
        "摄影X射线", "电动摄影平床",
    ]),
    # Respiratory / Anesthesia / Emergency
    ("respiratory", [
        "呼吸机", "麻醉机", "呼吸治疗", "正压通气", "高流量",
        "气管插管", "呼吸管路", "呼吸面罩", "呼吸道湿化",
        "呼吸系统过滤", "通气鼻贴", "输氧面罩", "空氧混合",
        "笑气", "人工复苏", "体外除颤", "体外同步复律", "经皮起搏",
        "麻醉面罩", "麻醉咽喉镜", "麻醉用针", "硬膜外麻醉",
        "支气管堵塞", "鼻氧管", "网式雾化", "医用雾化", "雾化面罩",
        "制氧机", "气腹机", "睡眠呼吸", "肺通气功能",
        "家用无创呼吸机",
        "口咽鼻咽通气道", "热湿交换器", "一氧化氮治疗",
        "喉罩", "外周神经阻滞穿刺针", "排痰机",
    ]),
    # Surgical instruments & endoscopes
    ("surgical", [
        "内窥镜", "腹腔镜", "手术动力", "手术显微镜", "高频手术",
        "超声软组织切割", "微波消融", "手术无影灯", "吻合器",
        "电动手术", "手术帽", "手术包", "手术衣", "切口保护",
        "活检针", "活检袋", "穿刺", "冲击波治疗",
        "冲洗器", "心脏固定器", "手术器械", "手术用剪",
        "电动气压止血", "包皮切割", "闭合夹", "硬性光学",
        "软性纤维内窥镜", "软性内窥镜用高频",
        "气管切开", "激光光纤", "尿道扩张",
        "骨组织手术设备", "活体取样钳", "微创筋膜闭合器",
        "取石网篮", "乳腺定位丝", "光固化机",
        "腹部穿刺器", "疝修补", "膀胱超声扫描",
        "定量剪切波超声", "激光治疗设备同品种",
        "电动洗胃机", "吻（缝）合器",
        "超声软组织手术设备",
    ]),
    # Dental
    ("dental", [
        "牙科", "口腔", "义齿", "种植体", "种植手术",
        "正畸", "牙根", "牙胶", "窝沟封闭", "根管",
        "合金产品", "牙基托", "矫治器", "牙科树脂",
        "光固化氢氧化钙间接盖髓", "牙科纤维桩",
        "合成树脂牙",
    ]),
    # Ophthalmic
    ("ophthalmic", [
        "眼科", "人工晶状体", "接触镜", "角膜", "视力",
        "裂隙灯", "视野计", "眼底照相", "验光仪", "弱视",
        "眼压计", "直接检眼镜",
    ]),
    # Rehab / Physiotherapy
    ("rehab_physio", [
        "低频电疗", "中频电疗", "短波治疗", "紫外治疗", "红外线治疗",
        "可见光谱治疗", "半导体激光治疗", "二氧化碳激光治疗",
        "磁疗", "肢体加压", "上下肢主被动", "步态训练",
        "冲击波治疗", "康复训练", "牵引", "超声理疗",
        "肌电生物反馈", "电针治疗", "激光脱毛", "射频美容",
        "强脉冲光", "轮椅", "蓝光治疗", "肠道水疗",
        "电动牵引", "医用臭氧妇科",
        "医用控温毯", "助听器", "听力计",
        "超声洁牙", "人工耳蜗",
    ]),
    # Wound care & dressings
    ("wound_care", [
        "敷料", "敷贴", "创面", "凡士林纱布", "水胶体",
        "藻酸盐", "凝胶敷料", "液体敷料", "疤痕修复",
        "热敷贴", "透明质酸钠创面", "重组胶原蛋白创面",
        "聚氨酯泡沫", "袜型医用压力", "粘合剂", "防粘连",
        "止血产品", "医用缝合针", "缝线", "导管固定",
        "妇科凝胶", "填充材料", "整形用面部", "乳房植入",
        "整形美容用透明质酸钠", "射线防护喷剂", "胃镜润滑液",
        "脱细胞基质",
        "骨填充材料", "口腔修复膜", "光固化氢氧化钙",
    ]),
    # Blood / Transfusion / Dialysis
    ("blood_transfusion", [
        "血液透析", "腹膜透析", "透析液过滤", "血浆",
        "血液成分分离", "血液融化", "血液浓缩",
        "采血管", "采血针", "采血器", "贮存袋",
        "胆红素血浆吸附", "血液分离",
    ]),
    # Infusion / Injection / Nursing
    ("infusion_injection", [
        "注射泵", "输液泵", "输注", "注射器", "注射笔",
        "输液器", "避光输液", "静脉留置针", "静脉营养",
        "高压造影", "导尿管", "引流", "侧孔钝针",
        "预充式导管冲洗", "输尿管", "尿量计", "尿动力",
        "电动病床", "防褥疮", "口罩", "防护服",
        "鼻饲", "胃管", "负压引流",
        "无针注射", "皮肤缝合",
        "纱布敷料", "吸痰管", "产包", "鼻镜",
        "肠营养", "胃肠道造影", "给药装置", "神经和肌肉刺激器",
        "腹膜透析导管", "动脉血样采集",
        "避孕套", "肠内营养泵",
    ]),
    # Sterilization & disinfection
    ("sterilization", [
        "灭菌器", "消毒", "耦合剂", "酸性氧化电位水",
        "医用洁净", "过氧化氢", "柠檬酸",
    ]),
    # TCM
    ("tcm", [
        "中医", "针灸", "三棱针", "拔罐", "小针刀",
        "熏蒸", "脉诊",
    ]),
    # Reproductive / Obstetrics
    ("reproductive", [
        "辅助生殖", "人工授精", "胚胎移植", "穿刺取卵",
        "宫内节育", "子宫", "阴道", "护脐", "胎儿",
        "宫颈球囊", "造影球囊导管",
        "人绒毛膜", "促卵泡", "泌乳素", "雌二醇",
        "孕酮检测", "促黄体",
    ]),
    # Patient monitoring
    ("monitoring", [
        "血压", "心电", "脑电", "体温计", "红外额温",
        "红外耳温", "听诊", "病人监护", "脉搏血氧",
        "动态血压", "动态心电", "电子血压",
        "血糖", "持续葡萄糖", "无创血糖",
        "有创血压", "有创压力传感",
        "房颤检测", "胰岛素泵",
        "脉搏波速度", "生物显微镜", "红外乳腺检查",
        "电动吸引器",
    ]),
    # Radiation therapy
    ("radiation_therapy", [
        "放射治疗", "质子", "碳离子", "射线束扫描",
        "激光定位", "图像引导系统",
    ]),
    # Lab equipment
    ("lab_equipment", [
        "二氧化碳培养箱", "生物安全柜", "低温保存箱",
        "医用气体", "中心供氧", "中心吸引",
        "医用空气压缩", "电子阴道显微镜",
        "非血管腔道导丝",
    ]),
]


def classify(title: str) -> str:
    for cat, keywords in RULES:
        for kw in keywords:
            if kw in title:
                return cat
    return "other"


def make_id(title: str) -> str:
    slug = re.sub(r"[^\w\u4e00-\u9fff]+", "-", title).strip("-").lower()
    if len(slug) > 80:
        slug = slug[:80]
    h = hashlib.md5(title.encode()).hexdigest()[:6]
    return f"nmpa-gp-{slug}-{h}"


def parse_md(path: Path) -> list[dict]:
    text = path.read_text("utf-8")
    entries = []
    for m in re.finditer(
        r"\|\s*(\d+)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|", text
    ):
        seq = m.group(1).strip()
        title = m.group(2).strip()
        doc_number = m.group(3).strip()
        if seq == "序号" or not seq.isdigit():
            continue
        entries.append({
            "seq": int(seq),
            "title": title,
            "doc_number": doc_number,
        })
    return entries


def main():
    if not GUIDANCE_MD.exists():
        print(f"Source not found: {GUIDANCE_MD}")
        return

    raw = parse_md(GUIDANCE_MD)
    print(f"Parsed {len(raw)} entries from markdown")

    cat_counts: dict[str, int] = {}
    indexed: list[dict] = []

    for r in raw:
        cat = classify(r["title"])
        cat_counts[cat] = cat_counts.get(cat, 0) + 1

        entry = {
            "id": make_id(r["title"]),
            "title": {"zh": r["title"], "en": ""},
            "status": "active",
            "source_url": "",
            "doc_number": r["doc_number"],
            "category": cat,
        }
        indexed.append(entry)

    categories_summary = {}
    for cat_id, names in CATEGORIES.items():
        cnt = cat_counts.get(cat_id, 0)
        if cnt > 0:
            categories_summary[cat_id] = {
                "name": names,
                "count": cnt,
            }

    index = {
        "category": "nmpa/guidance",
        "description": "NMPA medical device registration review guidance principles (CMDE classification)",
        "last_updated": "2026-04-09",
        "count": len(indexed),
        "categories": categories_summary,
        "entries": indexed,
    }

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=2)

    print(f"\nWrote {len(indexed)} entries to {OUTPUT}")
    print(f"\nCategory breakdown:")
    for cat_id in CATEGORIES:
        cnt = cat_counts.get(cat_id, 0)
        if cnt > 0:
            print(f"  {cat_id}: {cnt} ({CATEGORIES[cat_id]['zh']})")

    uncategorized = cat_counts.get("other", 0)
    if uncategorized:
        print(f"\n  WARNING: {uncategorized} entries classified as 'other'")
        for e in indexed:
            if e["category"] == "other":
                print(f"    - {e['title']['zh']}")


if __name__ == "__main__":
    main()
