<script setup lang="ts">
/**
 * Hub service-market CTA (#46 / CRM #20 / #44).
 * Links to the CRM public access-request page. No secrets / tokens in URL.
 */
import { computed } from "vue";
import { useData } from "vitepress";

const { lang } = useData();
const isZh = computed(() => lang.value === "zh" || lang.value === "zh-CN");

const CRM_APPLY_URL = "https://crm.reguverse.com/request-access";
const CRM_LOGIN_URL = "https://crm.reguverse.com/login";

const title = computed(() =>
  isZh.value ? "需要 CRO 法规服务或客户门户？" : "Need CRO regulatory services or a client portal?"
);
const body = computed(() =>
  isZh.value
    ? "提交准入申请，批准后可使用客户门户进行询价、项目协作与文档确认。"
    : "Request access to quote, collaborate, and confirm documents in the client portal."
);
const primary = computed(() =>
  isZh.value ? "申请门户访问" : "Request portal access"
);
const secondary = computed(() =>
  isZh.value ? "已有邀请？登录 CRM" : "Already invited? Sign in to CRM"
);
</script>

<template>
  <section class="rv-svc-cta" aria-labelledby="rv-svc-cta-title">
    <div class="rv-svc-cta-inner">
      <div class="rv-svc-cta-copy">
        <h2 id="rv-svc-cta-title" class="rv-svc-cta-title">{{ title }}</h2>
        <p class="rv-svc-cta-body">{{ body }}</p>
      </div>
      <div class="rv-svc-cta-actions">
        <a class="rv-svc-cta-primary" :href="CRM_APPLY_URL" target="_blank" rel="noopener noreferrer">
          {{ primary }}
        </a>
        <a class="rv-svc-cta-secondary" :href="CRM_LOGIN_URL" target="_blank" rel="noopener noreferrer">
          {{ secondary }}
        </a>
      </div>
    </div>
  </section>
</template>

<style scoped>
.rv-svc-cta {
  margin: 12px 16px 0;
  border: 1px solid var(--vp-c-divider);
  border-radius: 10px;
  background:
    linear-gradient(90deg, rgba(123, 104, 238, 0.1), transparent 42%),
    var(--vp-c-bg-soft);
}
.rv-svc-cta-inner {
  display: flex;
  flex-wrap: nowrap;
  gap: 0.75rem 1rem;
  align-items: center;
  justify-content: space-between;
  padding: 0.55rem 0.9rem;
}
.rv-svc-cta-copy {
  min-width: 0;
  flex: 1;
}
.rv-svc-cta-title {
  margin: 0;
  font-size: 0.92rem;
  font-weight: 650;
  color: var(--vp-c-text-1);
  line-height: 1.3;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.rv-svc-cta-body {
  margin: 0.15rem 0 0;
  font-size: 0.78rem;
  line-height: 1.35;
  color: var(--vp-c-text-2);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.rv-svc-cta-actions {
  display: flex;
  flex-wrap: nowrap;
  gap: 0.45rem;
  flex-shrink: 0;
}
.rv-svc-cta-primary,
.rv-svc-cta-secondary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0.35rem 0.7rem;
  border-radius: 7px;
  font-size: 0.78rem;
  font-weight: 600;
  text-decoration: none;
  transition: opacity 0.15s ease;
  white-space: nowrap;
}
.rv-svc-cta-primary {
  background: linear-gradient(135deg, #7b68ee, #5b4cdb);
  color: #fff;
}
.rv-svc-cta-secondary {
  border: 1px solid var(--vp-c-divider);
  background: var(--vp-c-bg);
  color: var(--vp-c-text-1);
}
.rv-svc-cta-primary:hover,
.rv-svc-cta-secondary:hover {
  opacity: 0.92;
}

@media (max-width: 860px) {
  .rv-svc-cta-inner {
    flex-wrap: wrap;
  }
  .rv-svc-cta-title,
  .rv-svc-cta-body {
    white-space: normal;
  }
  .rv-svc-cta-actions {
    width: 100%;
  }
}
</style>
