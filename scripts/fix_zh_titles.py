#!/usr/bin/env python3
"""Fix garbled and incorrect Chinese translations in FDA CDRH guidance files.

Phase 1: Fix completely garbled titles (manual corrections)
Phase 2: Systematic terminology replacements across all files

Usage:
    python scripts/fix_zh_titles.py --dry-run          # preview changes
    python scripts/fix_zh_titles.py                     # apply changes
    python scripts/fix_zh_titles.py --stats             # show statistics
"""

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ZH_DIR = ROOT / "docs" / "zh" / "fda" / "guidance"

# ── Phase 1: Manual title corrections for completely garbled titles ──────────

GARBLED_TITLE_FIXES: dict[str, str] = {
    "characterization-ultrahigh-molecular-weight-polyethylene-uhmwpe-used-orthopedic-devices":
        "骨科器械用超高分子量聚乙烯(UHMWPE)表征：行业与FDA工作人员指南",
    "factors-consider-when-making-benefit-risk-determinations-medical-device-premarket-approval-and-de":
        "医疗器械上市前批准和De Novo分类中受益-风险评估考量因素：行业与FDA工作人员指南",
    "surgical-sutures-performance-criteria-safety-and-performance-based-pathway":
        "外科缝合线 - 安全性与性能路径的性能标准：行业与FDA工作人员指南",
    "in-vitro-companion-diagnostic-devices":
        "体外伴随诊断器械：行业与FDA工作人员指南",
    "use-real-world-evidence-support-regulatory-decision-making-medical-devices":
        "利用真实世界证据支持医疗器械监管决策：行业与FDA工作人员指南",
    "assay-migration-studies-in-vitro-diagnostic-devices":
        "体外诊断器械的检测方法迁移研究：行业与FDA工作人员指南",
    "clinical-investigations-devices-indicated-treatment-urinary-incontinence-guidance-industry-and-fda":
        "用于尿失禁治疗的器械临床研究：行业与FDA工作人员指南",
    "coronary-and-carotid-embolic-protection-devices-premarket-notification-510k-submissions":
        "冠状动脉和颈动脉栓子保护器械 - 上市前通知[510(k)]提交：行业与FDA工作人员指南",
    "design-considerations-devices-intended-home-use":
        "家用器械设计考量：行业与FDA工作人员指南",
    "guidance-content-premarket-notifications-conventional-and-antimicrobial-foley-catheters":
        "常规和抗菌弗利导尿管上市前通知内容指南",
    "guidance-submission-premarket-notifications-photon-emitting-brachytherapy-sources-guidance-industry":
        "光子发射近距离放射治疗源上市前通知提交指南：行业指南",
    "modifications-devices-subject-premarket-approval-pma-pma-supplement-decision-making-process":
        "适用上市前批准(PMA)器械的变更 - PMA补充申请决策流程：行业与FDA工作人员指南",
    "submission-premarket-notifications-magnetic-resonance-diagnostic-devices":
        "磁共振诊断器械上市前通知提交：行业与FDA工作人员指南",
    "coronary-peripheral-and-neurovascular-guidewires-performance-tests-and-recommended-labeling":
        "冠状动脉、外周和神经血管导丝 - 性能测试和推荐标签：行业与FDA工作人员指南",
    "live-case-presentations-during-investigational-device-exemption-ide-clinical-trials":
        "研究用器械豁免(IDE)临床试验期间的实况病例演示：机构审查委员会、行业、临床研究者与FDA工作人员指南",
    "checklist-information-usually-submitted-investigational-device-exemptions-ide-application-refractive":
        "屈光手术激光器研究用器械豁免(IDE)申请通常提交的信息清单[准分子]",
    "applying-human-factors-and-usability-engineering-medical-devices":
        "将人因工程和可用性工程应用于医疗器械：行业与FDA工作人员指南",
    "general-wellness-policy-low-risk-devices":
        "一般健康：低风险器械政策：行业与FDA工作人员指南",
    "transitional-enforcement-policy-ethylene-oxide-sterilization-facility-changes-class-iii-devices":
        "III类器械环氧乙烷灭菌设施变更的过渡性执法政策：行业与FDA工作人员指南",
    # Additional garbled titles found during scan
    "content-and-format-premarket-notification-510k-submissions-liquid-chemical-sterilantshigh-level":
        "液体化学灭菌剂/高水平消毒剂上市前通知[510(k)]提交的内容和格式：行业与FDA审评人员指南",
    "content-investigational-device-exemption-ide-and-premarket-approval-pma-applications-artificial":
        "人工胰腺装置系统的研究用器械豁免(IDE)和上市前批准(PMA)申请内容：行业与FDA工作人员指南",
    "enforcement-policy-certain-supplements-approved-premarket-approval-pma-or-humanitarian-device":
        "已批准上市前批准(PMA)或人道主义器械豁免(HDE)申请的某些补充申请的执法政策：行业与FDA工作人员指南",
    "guidance-premarket-notification-510k-sterilizers-intended-use-health-care-facilities":
        "医疗保健设施用灭菌器上市前通知510(k)指南",
    "intent-exempt-certain-unclassified-medical-devices-premarket-notification-requirements":
        "拟豁免某些未分类医疗器械上市前通知要求：行业与FDA工作人员指南",
    "premarket-approval-application-and-humanitarian-device-exemption-modular-review":
        "上市前批准申请和人道主义器械豁免模块化审查：行业与FDA工作人员指南",
    "premarket-notification-510k-submissions-chemical-indicators-guidance-industry-and-fda-staff":
        "化学指示剂上市前通知[510(k)]提交：行业与FDA工作人员指南",
    "basic-safety-and-essential-performance-medical-electrical-equipment-medical-electrical-systems-and":
        "医用电气设备、医用电气系统和实验室医疗器械的基本安全和基本性能 - 认证符合性评估计划(ASCA)试点计划的具体信息：行业、认可机构、检测实验室与FDA工作人员指南",
    "clinical-considerations-investigational-device-exemption-ides-neurological-devices-targeting":
        "针对疾病进展和临床结局的神经系统研究用器械豁免(IDE)临床考量：行业与FDA工作人员指南",
    "consideration-uncertainty-making-benefit-risk-determinations-medical-device-premarket-approvals-de":
        "在医疗器械上市前批准、De Novo分类和人道主义器械豁免中受益-风险评估时考量不确定性：行业与FDA工作人员指南",
    "deciding-when-submit-510k-change-existing-device":
        "决定何时就现有器械的变更提交510(k)：行业与FDA工作人员指南",
    "determination-intended-use-510k-devices-guidance-cdrh-staff-update-k98-1":
        "510(k)器械预期用途的确定 - CDRH工作人员指南(更新至K98-1)",
    "device-labeling-guidance-g91-1-blue-book-memo":
        "器械标签指南#G91-1(蓝皮书备忘录)",
    "custom-device-exemption":
        "定制器械豁免：行业与FDA工作人员指南",
    "bundling-multiple-devices-or-multiple-indications-single-submission":
        "在单个提交中捆绑多个器械或多个适应症：行业与FDA工作人员指南",
    "center-devices-and-radiological-health-cdrh-appeals-processes-questions-and-answers-about-517a":
        "器械和放射卫生中心(CDRH)申诉流程：关于517A条的问答：行业与FDA工作人员指南",
    "center-devices-and-radiological-health-cdrh-appeals-processes":
        "器械和放射卫生中心(CDRH)申诉流程：行业与FDA工作人员指南",
    "breakthrough-devices-program":
        "突破性器械计划：行业与FDA工作人员指南",
    "clinical-considerations-studies-devices-intended-treat-opioid-use-disorder":
        "治疗阿片类药物使用障碍的器械临床考量：行业与FDA工作人员指南",
    "clinical-investigations-prostate-tissue-ablation-devices":
        "前列腺组织消融器械的临床研究：行业与FDA工作人员指南",
    "coordinated-development-antimicrobial-drugs-and-antimicrobial-susceptibility-test-devices":
        "抗菌药物和抗菌药敏试验器械的协调开发：行业与FDA工作人员指南",
    "criteria-significant-risk-investigations-magnetic-resonance-diagnostic-devices-guidance-industry-and":
        "磁共振诊断器械重大风险研究标准：行业与FDA工作人员指南",
    "dental-composite-resin-devices-premarket-notification-510k-submissions":
        "牙科复合树脂器械 - 上市前通知(510(k))提交：行业与FDA工作人员指南",
    "antimicrobial-susceptibility-test-ast-system-devices-updating-breakpoints-device-labeling":
        "抗菌药敏试验(AST)系统器械 - 更新器械标签中的折点：行业与FDA工作人员指南",
    "animal-studies-dental-bone-grafting-material-devices-premarket-notification-510k-submissions":
        "牙科骨移植材料器械的动物研究 - 上市前通知(510(k))提交：行业与FDA工作人员指南",
    "1-consolidated-annual-report-device-product-line-1-card-guidance-industry-and-cdrh-reviewers":
        "1-器械产品线综合年度报告(1-CARD)：行业与CDRH审评人员指南",
    "30-day-notices-135-day-premarket-approval-pma-supplements-and-75-day-humanitarian-device-exemption":
        "关于生产方法或工艺变更的30天通知、135天上市前批准(PMA)补充申请和75天人道主义器械豁免(HDE)补充申请：行业与FDA工作人员指南",
    "global-unique-device-identification-database-gudid":
        "全球唯一器械标识数据库(GUDID)：行业与FDA工作人员指南",
    "recognition-and-withdrawal-voluntary-consensus-standards":
        "自愿性协调标准的认可和撤销：行业与FDA工作人员指南",
    "medical-device-classification-product-codes-guidance-industry-and-food-and-drug-administration-staff":
        "医疗器械分类产品代码：行业与FDA工作人员指南",
    "logical-observation-identifiers-names-and-codes-in-vitro-diagnostic-tests":
        "体外诊断检测的逻辑观察标识符名称与代码(LOINC)：行业与FDA工作人员指南",
    "referencing-definition-device-federal-food-drug-and-cosmetic-act-guidance-regulatory-documents":
        "在指南、监管文件、通信和其他公开文件中引用《联邦食品药品和化妆品法》中的\"器械\"定义：行业与FDA工作人员指南",

    # ── Batch 2: remaining 设备->器械 and garbled title corrections ──
    "clinical-considerations-investigational-device-exemptions-ides-neurological-devices-targeting":
        "针对疾病进展和临床结局的神经系统器械研究用器械豁免(IDE)临床考量：行业与FDA工作人员指南",
    "enforcement-policy-non-invasive-remote-monitoring-devices-used-support-patient-monitoring":
        "用于支持患者监测的非侵入式远程监测器械执法政策：行业与FDA工作人员指南",
    "establishing-performance-characteristics-in-vitro-diagnostic-devices-detection-antibodies-borrelia":
        "确定伯氏疏螺旋体抗体检测用体外诊断器械的性能特性：行业与FDA工作人员指南",
    "establishing-performance-characteristics-in-vitro-diagnostic-devices-detection-or-detection-and-0":
        "确定人乳头瘤病毒检测或检测和分型用体外诊断器械的性能特性：行业与FDA工作人员指南",
    "establishing-performance-characteristics-in-vitro-diagnostic-devices-detection-or-detection-and":
        "确定流感病毒检测或检测和分型用体外诊断器械的性能特性：行业与FDA工作人员指南",
    "fda-categorization-investigational-device-exemption-ide-devices-assist-centers-medicare-and-medicaid":
        "FDA对研究用器械豁免(IDE)器械的分类以协助医疗保险和医疗补助服务中心(CMS)作出覆盖决策：申办者、临床研究者、行业、机构审查委员会与FDA工作人员指南",
    "fda-decisions-investigational-device-exemption-clinical-investigations":
        "FDA关于研究用器械豁免临床研究的决定：申办者、临床研究者、机构审查委员会与FDA工作人员指南",
    "frequently-asked-questions-about-reprocessing-and-reuse-single-use-devices-third-party-and-hospital-0":
        "第三方和医院再处理器对一次性使用器械的再处理和再使用常见问题 - 三个附加问题：行业、FDA工作人员、第三方和医院再处理器指南",
    "frequently-asked-questions-about-reprocessing-and-reuse-single-use-devices-third-party-and-hospital":
        "第三方和医院再处理器对一次性使用器械的再处理和再使用常见问题：行业与FDA工作人员最终指南",
    "guidance-dermabrasion-devices-guidance-industry":
        "皮肤磨削器械指南：行业指南",
    "guidance-document-dura-substitute-devices-guidance-industry":
        "硬脑膜替代器械指南：行业指南",
    "guidance-document-premarket-notification-submissions-nitric-oxide-delivery-apparatus-nitric-oxide":
        "一氧化氮输送装置、一氧化氮分析仪和二氧化氮分析仪上市前通知提交指南：行业与FDA审评人员指南",
    "guidance-document-preparation-premarket-notification-510k-applications-exercise-equipment":
        "运动设备上市前通知[510(K)]申请准备指南",
    "guidance-document-preparation-premarket-notification-510k-applications-heating-and-cooling-devices":
        "加热和冷却器械上市前通知[510(k)]申请准备指南",
    "guidance-industry-and-fda-staff-vocal-fold-medialization-devices-premarket-notification-510k":
        "声带内移器械 - 上市前通知[510(k)]提交：行业与FDA工作人员指南",
    "guidance-industry-and-food-and-drug-administration-staff-assemblers-guide-diagnostic-x-ray-equipment":
        "诊断X射线设备组装指南：行业与FDA工作人员指南",
    "guidance-informed-consent-in-vitro-diagnostic-device-studies-using-leftover-human-specimens-are-not":
        "使用非个人可识别的剩余人类样本进行体外诊断器械研究的知情同意指南：申办者、机构审查委员会与FDA工作人员指南",
    "guidance-resorbable-adhesion-barrier-devices-use-abdominal-andor-pelvic-surgery-guidance-industry":
        "用于腹部和/或盆腔手术的可吸收防粘连屏障器械指南：行业指南",
    "guidance-submission-510ks-solid-state-x-ray-imaging-devices":
        "固态X射线成像器械510(k)提交指南：行业与FDA工作人员指南",
    "guidance-submission-premarket-notifications-emission-computed-tomography-devices-and-accessories":
        "发射计算机断层扫描器械和附件(SPECT和PET)及核断层扫描系统上市前通知提交指南：行业指南",
    "highly-multiplexed-microbiologicalmedical-countermeasure-in-vitro-nucleic-acid-based-diagnostic-devices":
        "高通量多重微生物/医学对策体外核酸诊断器械：行业与FDA工作人员指南",
    "implanted-blood-access-devices-hemodialysis":
        "血液透析植入式血管通路器械：行业与FDA工作人员指南",
    "implanted-brain-computer-interface-bci-devices-patients-paralysis-or-amputation-non-clinical-testing":
        "瘫痪或截肢患者植入式脑机接口(BCI)器械 - 非临床测试和临床考量：行业与FDA工作人员指南",
    "investigational-device-exemptions-ides-devices-indicated-nocturnal-home-hemodialysis":
        "用于夜间家庭血液透析器械的研究用器械豁免(IDE)：行业与FDA工作人员指南",
    "investigational-device-exemptions-ides-early-feasibility-medical-device-clinical-studies-including":
        "早期可行性医疗器械临床研究的研究用器械豁免(IDE)，含某些首次人体(FIH)研究：行业与FDA工作人员指南",
    "investigational-medical-laser-significant-risk-device-laser-notice-31":
        "研究用医疗激光重大风险器械(激光通告31)",
    "labeling-recommendations-single-use-devices-reprocessed-third-parties-and-hospitals":
        "第三方和医院再处理的一次性使用器械的标签建议：行业与FDA最终指南",
    "manufacture-and-certification-laser-kits-laser-notice-13":
        "激光套件的制造和认证(激光通告13)",
    "medical-devices-containing-materials-derived-animal-sources-except-in-vitro-diagnostic-devices":
        "含有动物来源材料的医疗器械(体外诊断器械除外)：行业与FDA工作人员指南",
    "medical-x-ray-imaging-devices-conformance-iec-standards":
        "医疗X射线成像器械符合IEC标准：行业与FDA工作人员指南",
    "mouse-embryo-assay-assisted-reproduction-technology-devices":
        "辅助生殖技术器械的小鼠胚胎试验",
    "non-clinical-and-clinical-investigation-devices-used-treatment-benign-prostatic-hyperplasia-bph":
        "用于治疗良性前列腺增生(BPH)器械的非临床和临床研究：行业与FDA工作人员指南",
    "nonbinding-feedback-after-certain-fda-inspections-device-establishments":
        "FDA对器械生产机构特定检查后的非约束性反馈：行业与FDA工作人员指南",
    "notifying-fda-permanent-discontinuance-or-interruption-manufacturing-device-under-section-506j-fdc":
        "根据FD&C法第506J条通知FDA器械生产的永久停产或中断：行业与FDA工作人员指南",
    "pediatric-information-x-ray-imaging-device-premarket-notifications":
        "X射线成像器械上市前通知中的儿科信息：行业与FDA工作人员指南",
    "points-consider-cervical-cytology-devices":
        "宫颈细胞学器械注意要点",
    "policy-clarification-and-premarket-notification-510k-submissions-ultrasonic-diathermy-devices":
        "超声透热器械的政策澄清和上市前通知[510(k)]提交：行业与FDA工作人员指南",
    "policy-clarification-certain-fluoroscopic-equipment-requirements":
        "某些透视设备要求的政策澄清：行业与FDA工作人员指南",
    "pre-clinical-and-clinical-studies-neurothrombectomy-devices":
        "神经血栓切除器械的临床前和临床研究：行业与FDA工作人员指南",
    "premarket-notification-510k-submissions-electrosurgical-devices-general-surgery":
        "普通外科电外科器械上市前通知(510(k))提交：行业与FDA工作人员指南",
    "premarket-studies-implantable-minimally-invasive-glaucoma-surgical-migs-devices":
        "植入式微创青光眼手术(MIGS)器械的上市前研究：行业与FDA工作人员指南",
    "procedures-class-ii-device-exemptions-premarket-notification-guidance-industry-and-cdrh-staff":
        "II类器械免除上市前通知的程序：行业与CDRH工作人员指南",
    "process-request-review-fdas-decision-not-issue-certain-export-certificates-devices":
        "申请复审FDA不颁发某些器械出口证书决定的程序：行业与FDA工作人员指南",
    "radiation-biodosimetry-medical-countermeasure-devices":
        "放射生物剂量测定医学对策器械：行业与FDA工作人员指南",
    "radiation-safety-considerations-x-ray-equipment-designed-hand-held-use":
        "手持式X射线设备的辐射安全考量",

    # ── Batch 3: UDI and remaining device->器械 fixes ──
    "unique-device-identification-convenience-kits":
        "唯一器械标识：便利套件：行业与FDA工作人员指南",
    "unique-device-identification-direct-marking-devices":
        "唯一器械标识：器械直接标记：行业与FDA工作人员指南",
    "unique-device-identification-policy-regarding-compliance-dates-class-i-and-unclassified-devices":
        "唯一器械标识：关于I类和未分类器械合规日期、直接标记及某些器械全球唯一器械标识数据库要求的政策：行业与FDA工作人员指南",
    "unique-device-identification-system-form-and-content-unique-device-identifier-udi":
        "唯一器械标识系统：唯一器械标识符(UDI)的形式和内容：行业与FDA工作人员指南",
    "unique-device-identifier-system-frequently-asked-questions-vol-1":
        "唯一器械标识符系统常见问题(第1卷)",
    "technical-performance-assessment-quantitative-imaging-radiological-device-premarket-submissions":
        "放射学器械上市前提交中定量成像的技术性能评估：行业与FDA工作人员指南",
    "third-party-review-guidance-phacofragmentation-system-device-premarket-notification-510k":
        "超声乳化碎核系统器械上市前通知510(k)第三方审查指南",
    "third-party-review-guidance-vitreous-aspiration-and-cutting-device-premarket-notification-510k":
        "玻璃体抽吸和切割器械上市前通知510(k)第三方审查指南",
    "user-fees-and-refunds-premarket-approval-applications-and-device-biologics-license-applications":
        "上市前批准申请和器械生物制品许可申请的用户费和退款：行业与FDA工作人员指南",
    "utilizing-animal-studies-evaluate-organ-preservation-devices":
        "利用动物研究评估器官保存器械：行业与FDA工作人员指南",
    "submission-and-review-sterility-information-premarket-notification-510k-submissions-devices-labeled":
        "以无菌标记器械的上市前通知(510(k))提交中无菌信息的提交和审查：行业与FDA工作人员指南",
    "recommendations-clinical-laboratory-improvement-amendments-1988-clia-waiver-applications":
        "1988年临床实验室改进修正案(CLIA)体外诊断器械制造商豁免申请的建议：行业与FDA工作人员指南",
    "regulatory-requirements-hearing-aid-devices-and-personal-sound-amplification-products":
        "助听器械和个人声音放大产品的监管要求：行业与FDA工作人员指南",
    "technical-performance-assessment-digital-pathology-whole-slide-imaging-devices":
        "数字病理全切片成像器械的技术性能评估：行业与FDA工作人员指南",
}


# ── Phase 2: Systematic terminology replacements ────────────────────────────

# Order matters: more specific patterns first to avoid partial matches
TERMINOLOGY_REPLACEMENTS: list[tuple[str, str]] = [
    # Completely wrong terms
    ("实实世界", "真实世界"),
    ("乙烯氧化物", "环氧乙烷"),

    # Premarket terminology
    ("预销售通知", "上市前通知"),
    ("预销售许可", "上市前批准"),
    ("预销售批准", "上市前批准"),

    # Device terminology - specific compounds first
    ("人道主义设备豁免", "人道主义器械豁免"),
    ("实验设备豁免", "研究用器械豁免"),
    ("检查设备豁免", "研究用器械豁免"),
    ("突破性设备", "突破性器械"),
    ("医疗设备", "医疗器械"),

    # Regulatory process terms
    ("补充剂", "补充申请"),  # PMA supplements
    ("放射性健康中心", "放射卫生中心"),
    ("放射性健康", "放射卫生"),

    # IDE/HDE/PMA specific terms
    ("研究设备豁免", "研究用器械豁免"),
    ("调查设备豁免", "研究用器械豁免"),

    # UDI terminology
    ("唯一设备识别", "唯一器械标识"),
    ("设备识别器", "器械标识符"),

    # In vitro diagnostics
    ("内置诊断设备", "体外诊断器械"),
    ("直体诊断设备", "体外诊断器械"),
    ("体诊断设备", "体外诊断器械"),

    # COVID context: 冠状病毒 is correct for coronavirus
    # But: coronary = 冠状动脉, not 冠状病毒
    # (these are handled by GARBLED_TITLE_FIXES for specific files)

    # Title suffix standardization
    ("行业与食品药品管理局工作人员指南", "行业与FDA工作人员指南"),
    ("食品药品管理局工作人员", "FDA工作人员"),
    ("食品药品管理局", "FDA"),
]


def read_frontmatter(text: str) -> tuple[dict[str, str], str]:
    """Parse YAML frontmatter from markdown text.
    Returns (frontmatter_dict, rest_of_text).
    """
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---\n", 3)
    if end == -1:
        return {}, text
    fm_text = text[4:end]
    rest = text[end + 5:]
    fm = {}
    for line in fm_text.split("\n"):
        if ":" in line:
            key, val = line.split(":", 1)
            fm[key.strip()] = val.strip().strip('"')
    return fm, rest


def apply_terminology_fixes(text: str) -> str:
    """Apply systematic terminology replacements to text."""
    result = text
    for old, new in TERMINOLOGY_REPLACEMENTS:
        result = result.replace(old, new)
    return result


def fix_file(filepath: Path, dry_run: bool = False) -> dict:
    """Fix a single ZH guidance file. Returns change info."""
    slug = filepath.stem
    text = filepath.read_text(encoding="utf-8")
    original = text
    changes = []

    # Phase 1: Check for garbled title fix
    if slug in GARBLED_TITLE_FIXES:
        new_title = GARBLED_TITLE_FIXES[slug]
        # Replace title in frontmatter
        title_match = re.search(r'^title:\s*"(.+?)"', text, re.MULTILINE)
        if title_match:
            old_title = title_match.group(1)
            if old_title != new_title:
                text = text.replace(
                    f'title: "{old_title}"',
                    f'title: "{new_title}"',
                    1,
                )
                changes.append(f"TITLE: {old_title[:50]}... -> {new_title[:50]}...")

    # Phase 2: Apply terminology replacements to full text
    text = apply_terminology_fixes(text)

    if text != original:
        # Count actual changes
        for old, new in TERMINOLOGY_REPLACEMENTS:
            count = original.count(old) - text.count(old)  # not accurate for cascading
        if not changes:
            changes.append("terminology fixes applied")

        if not dry_run:
            filepath.write_text(text, encoding="utf-8")

    return {
        "file": slug,
        "changed": text != original,
        "changes": changes,
        "original_len": len(original),
        "new_len": len(text),
    }


def run_stats():
    """Show statistics about current ZH file quality."""
    files = sorted(ZH_DIR.glob("*.md"))
    print(f"Total ZH guidance files: {len(files)}")

    garbled_count = 0
    terminology_count = 0

    for f in files:
        text = f.read_text(encoding="utf-8")
        slug = f.stem

        if slug in GARBLED_TITLE_FIXES:
            title_match = re.search(r'^title:\s*"(.+?)"', text, re.MULTILINE)
            if title_match and title_match.group(1) != GARBLED_TITLE_FIXES[slug]:
                garbled_count += 1

        for old, _ in TERMINOLOGY_REPLACEMENTS:
            if old in text:
                terminology_count += 1
                break

    print(f"Files with garbled titles needing fix: {garbled_count}")
    print(f"Files with terminology issues: {terminology_count}")


def main():
    parser = argparse.ArgumentParser(description="Fix ZH translation quality")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without writing")
    parser.add_argument("--stats", action="store_true", help="Show statistics only")
    parser.add_argument("--file", type=str, help="Fix a single file (slug or filename)")
    args = parser.parse_args()

    if args.stats:
        run_stats()
        return

    files = sorted(ZH_DIR.glob("*.md"))

    if args.file:
        slug = args.file.replace(".md", "")
        target = ZH_DIR / f"{slug}.md"
        if not target.exists():
            print(f"File not found: {target}")
            sys.exit(1)
        files = [target]

    changed_count = 0
    title_fixes = 0
    term_fixes = 0

    for f in files:
        result = fix_file(f, dry_run=args.dry_run)
        if result["changed"]:
            changed_count += 1
            if any("TITLE:" in c for c in result["changes"]):
                title_fixes += 1
            else:
                term_fixes += 1
            if args.dry_run:
                print(f"  WOULD FIX: {result['file']}")
                for c in result["changes"]:
                    print(f"    {c}")

    action = "Would fix" if args.dry_run else "Fixed"
    print(f"\n{action} {changed_count} files ({title_fixes} title fixes, {term_fixes} terminology-only fixes)")
    print(f"Scanned {len(files)} files total")


if __name__ == "__main__":
    main()
