<script setup lang="ts">
import { computed } from "vue";
import { useData } from "vitepress";

const { lang } = useData();
const isZh = computed(() => lang.value === "zh" || lang.value === "zh-CN");

const roadmapData = [
  {
    id: "phase1",
    status: "completed",
    titleEn: "Phase 1 -- Core EU MDR Compliance",
    titleZh: "Phase 1 -- EU MDR 核心合规",
    timeline: "2025 Q3 - 2026 Q1",
    itemsEn: [
      "Clinical Evaluation workflow (CEP/CER/DCR generation)",
      "GSPR compliance analysis with Annex I requirements",
      "Risk Management workflow (RMP/RMR/RM Analysis)",
      "Literature search integration (PubMed, Embase)",
      "FDA MAUDE & EU Vigilance safety data analysis",
      "Regulatory knowledge base with full-text search",
      "Multi-language support (English / Chinese)",
      "Word document export with professional formatting",
    ],
    itemsZh: [
      "临床评价工作流（CEP/CER/DCR 文档生成）",
      "GSPR 合规分析（Annex I 基本安全与性能要求）",
      "风险管理工作流（RMP/RMR/风险分析表）",
      "文献检索集成（PubMed、Embase）",
      "FDA MAUDE 和 EU 警戒系统安全数据分析",
      "法规知识库全文检索",
      "多语言支持（英文 / 中文）",
      "Word 文档导出（专业排版格式）",
    ],
  },
  {
    id: "phase2",
    status: "completed",
    titleEn: "Phase 2 -- Platform & Enterprise",
    titleZh: "Phase 2 -- 平台化与企业服务",
    timeline: "2026 Q1 - Q2",
    itemsEn: [
      "Web platform (browser-based, no Office dependency)",
      "User authentication with TOTP 2FA",
      "Subscription tiers (Trial/Basic/Pro/Max/CRO)",
      "PMS Plan, PMCF Plan/Report, PSUR workflows",
      "Biocompatibility evaluation (BEP/BER)",
      "Device Description structured data management",
      "SSCP (Summary of Safety & Clinical Performance)",
      "Equivalent device analysis workflow",
      "Global regulatory news monitoring (30+ countries)",
      "CRM system for CRO organizations",
    ],
    itemsZh: [
      "Web 平台（浏览器端，无需 Office 依赖）",
      "用户认证与 TOTP 双因素验证",
      "订阅层级（试用/基础/专业/旗舰/CRO）",
      "PMS 计划、PMCF 计划/报告、PSUR 工作流",
      "生物相容性评价（BEP/BER）",
      "器械描述结构化数据管理",
      "SSCP（安全与临床性能摘要）",
      "等效器械分析工作流",
      "全球法规速递监控（30+ 国家/地区）",
      "CRO 组织客户关系管理系统",
    ],
  },
  {
    id: "phase3",
    status: "in_progress",
    titleEn: "Phase 3 -- Multi-Regulation & Intelligence",
    titleZh: "Phase 3 -- 多法规体系与智能化",
    timeline: "2026 Q2 - Q3",
    itemsEn: [
      "NMPA (China) registration compliance workflows",
      "FDA 510(k) pre-submission support",
      "Technical Documentation cover letter generation",
      "Manufacturer Information document assembly",
      "AI-powered context-aware document generation",
      "Cross-document consistency validation",
      "Reguverse Hub community platform",
    ],
    itemsZh: [
      "NMPA（中国）注册合规工作流",
      "FDA 510(k) 预提交支持",
      "技术文档封面信生成",
      "制造商信息文档自动组装",
      "AI 驱动的上下文感知文档生成",
      "跨文档一致性校验",
      "Reguverse Hub 社区平台",
    ],
  },
  {
    id: "phase4",
    status: "planned",
    titleEn: "Phase 4 -- Advanced Features",
    titleZh: "Phase 4 -- 高级功能",
    timeline: "2026 Q3 - Q4",
    itemsEn: [
      "BYOK (Bring Your Own Key) LLM API support",
      "Total Product Life Cycle (TPLC) management",
      "eQMS integration capabilities",
      "Automated regulatory change impact assessment",
      "Multi-team collaboration and review workflows",
      "International payment (Stripe) integration",
      "Advanced analytics and compliance dashboards",
    ],
    itemsZh: [
      "BYOK（自带密钥）LLM API 支持",
      "全产品生命周期（TPLC）管理",
      "eQMS 电子质量管理系统集成",
      "法规变更自动化影响评估",
      "多团队协作与审批工作流",
      "国际支付（Stripe）集成",
      "高级数据分析与合规仪表盘",
    ],
  },
];

function statusLabel(status: string): string {
  if (status === "completed") return isZh.value ? "已完成" : "Completed";
  if (status === "in_progress") return isZh.value ? "进行中" : "In Progress";
  return isZh.value ? "规划中" : "Planned";
}
</script>

<template>
  <div class="rv-roadmap-container">
    <p class="rv-roadmap-intro">
      {{ isZh
        ? "Reguverse Assistant 的开发路线图。我们持续改进产品以满足全球医疗器械合规需求。"
        : "Development roadmap for Reguverse Assistant. We continuously improve to meet global medical device regulatory compliance needs." }}
    </p>
    <div
      v-for="phase in roadmapData"
      :key="phase.id"
      class="rv-roadmap-phase"
      :class="'rv-phase-' + phase.status"
    >
      <div class="rv-phase-header">
        <span class="rv-phase-badge" :class="'rv-badge-' + phase.status">
          {{ statusLabel(phase.status) }}
        </span>
        <h3 class="rv-phase-title">{{ isZh ? phase.titleZh : phase.titleEn }}</h3>
        <span class="rv-phase-timeline">{{ phase.timeline }}</span>
      </div>
      <ul class="rv-phase-items">
        <li
          v-for="(item, idx) in (isZh ? phase.itemsZh : phase.itemsEn)"
          :key="idx"
          class="rv-phase-item"
        >
          <svg v-if="phase.status === 'completed'" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#0cce6b" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
          <svg v-else-if="phase.status === 'in_progress'" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#f5a623" stroke-width="2"><circle cx="12" cy="12" r="4" fill="#f5a623"/></svg>
          <svg v-else width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="var(--vp-c-text-3)" stroke-width="2"><circle cx="12" cy="12" r="5"/></svg>
          <span>{{ item }}</span>
        </li>
      </ul>
    </div>
  </div>
</template>

<style scoped>
.rv-roadmap-container {
  max-width: 800px;
  margin: 0 auto;
}
.rv-roadmap-intro {
  color: var(--vp-c-text-2);
  font-size: 15px;
  margin-bottom: 32px;
  line-height: 1.6;
}
.rv-roadmap-phase {
  margin-bottom: 28px;
  border-left: 3px solid var(--vp-c-divider);
  padding-left: 20px;
  position: relative;
}
.rv-roadmap-phase::before {
  content: "";
  position: absolute;
  left: -7px;
  top: 6px;
  width: 11px;
  height: 11px;
  border-radius: 50%;
  background: var(--vp-c-divider);
}
.rv-phase-completed::before { background: #0cce6b; }
.rv-phase-completed { border-left-color: #0cce6b; }
.rv-phase-in_progress::before { background: #f5a623; }
.rv-phase-in_progress { border-left-color: #f5a623; }
.rv-phase-planned::before { background: var(--vp-c-text-3); }
.rv-phase-header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 12px;
  flex-wrap: wrap;
}
.rv-phase-badge {
  font-size: 11px;
  font-weight: 600;
  padding: 2px 10px;
  border-radius: 10px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  flex-shrink: 0;
}
.rv-badge-completed { background: rgba(12,206,107,0.12); color: #0cce6b; }
.rv-badge-in_progress { background: rgba(245,166,35,0.12); color: #f5a623; }
.rv-badge-planned { background: var(--vp-c-bg-soft); color: var(--vp-c-text-3); }
.rv-phase-title {
  margin: 0;
  font-size: 17px;
  font-weight: 600;
  color: var(--vp-c-text-1);
}
.rv-phase-timeline {
  font-size: 13px;
  color: var(--vp-c-text-3);
  margin-left: auto;
}
.rv-phase-items {
  list-style: none;
  margin: 0;
  padding: 0;
}
.rv-phase-item {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 5px 0;
  font-size: 14px;
  color: var(--vp-c-text-2);
  line-height: 1.5;
}
.rv-phase-item svg {
  flex-shrink: 0;
}
</style>
