<script setup lang="ts">
import { ref, computed } from "vue";
import { useData } from "vitepress";
import FeatureBoard from "./FeatureBoard.vue";
import DiscussionWall from "./DiscussionWall.vue";

const { lang } = useData();
const isZh = computed(() => lang.value === "zh" || lang.value === "zh-CN");

const activeTab = ref<"features" | "discussions" | "roadmap">("features");

const tabs = computed(() => [
  {
    key: "features" as const,
    label: isZh.value ? "功能建议" : "Feature Board",
    icon: "M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z",
  },
  {
    key: "discussions" as const,
    label: isZh.value ? "讨论区" : "Discussions",
    icon: "M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z",
  },
  {
    key: "roadmap" as const,
    label: isZh.value ? "路线图" : "Roadmap",
    icon: "M9 20l-5.447-2.724A1 1 0 013 16.382V5.618a1 1 0 011.447-.894L9 7m0 13l6-3m-6 3V7m6 10l4.553 2.276A1 1 0 0021 18.382V7.618a1 1 0 00-.553-.894L15 4m0 13V4m0 0L9 7",
  },
]);
</script>

<template>
  <div class="rv-hub">
    <header class="rv-hub-header">
      <div class="rv-hub-header-inner">
        <div class="rv-hub-title-row">
          <h1 class="rv-hub-title">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
              <path d="M12 2L2 7l10 5 10-5-10-5z"/>
              <path d="M2 17l10 5 10-5"/>
              <path d="M2 12l10 5 10-5"/>
            </svg>
            Reguverse Hub
          </h1>
          <p class="rv-hub-subtitle">
            {{ isZh ? "RA 专业人士共建的社区平台" : "Community-driven platform for RA professionals" }}
          </p>
        </div>
      </div>
    </header>

    <nav class="rv-hub-tabs">
      <div class="rv-hub-tabs-inner">
        <button
          v-for="tab in tabs"
          :key="tab.key"
          class="rv-hub-tab"
          :class="{ active: activeTab === tab.key }"
          @click="activeTab = tab.key"
        >
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
            <path :d="tab.icon"/>
          </svg>
          {{ tab.label }}
        </button>
      </div>
    </nav>

    <main class="rv-hub-content">
      <div v-if="activeTab === 'features'" class="rv-hub-panel">
        <FeatureBoard />
      </div>
      <div v-else-if="activeTab === 'discussions'" class="rv-hub-panel">
        <DiscussionWall />
      </div>
      <div v-else class="rv-hub-panel rv-hub-roadmap">
        <div class="rv-roadmap-placeholder">
          <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="var(--vp-c-text-3)" stroke-width="1" stroke-linecap="round" stroke-linejoin="round">
            <path d="M9 20l-5.447-2.724A1 1 0 013 16.382V5.618a1 1 0 011.447-.894L9 7m0 13l6-3m-6 3V7m6 10l4.553 2.276A1 1 0 0021 18.382V7.618a1 1 0 00-.553-.894L15 4m0 13V4m0 0L9 7"/>
          </svg>
          <h3>{{ isZh ? "产品路线图" : "Product Roadmap" }}</h3>
          <p>{{ isZh ? "即将推出 -- 查看我们的开发计划和已完成的功能。" : "Coming soon -- view our development plans and completed features." }}</p>
        </div>
      </div>
    </main>
  </div>
</template>

<style scoped>
.rv-hub {
  min-height: calc(100vh - var(--vp-nav-height, 64px));
  background: var(--vp-c-bg);
}

.rv-hub-header {
  background: linear-gradient(135deg, var(--vp-c-brand-1), var(--vp-c-brand-2));
  color: white;
  padding: 40px 24px 32px;
}
.rv-hub-header-inner {
  max-width: 1200px;
  margin: 0 auto;
}
.rv-hub-title-row {
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.rv-hub-title {
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 28px;
  font-weight: 700;
  margin: 0;
  color: white;
  letter-spacing: -0.5px;
}
.rv-hub-subtitle {
  margin: 0;
  font-size: 16px;
  opacity: 0.9;
}

.rv-hub-tabs {
  position: sticky;
  top: var(--vp-nav-height, 64px);
  z-index: 10;
  background: var(--vp-c-bg);
  border-bottom: 1px solid var(--vp-c-divider);
  padding: 0 24px;
}
.rv-hub-tabs-inner {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  gap: 4px;
}
.rv-hub-tab {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 14px 20px;
  border: none;
  background: none;
  color: var(--vp-c-text-2);
  font-size: 15px;
  font-weight: 500;
  cursor: pointer;
  border-bottom: 2px solid transparent;
  transition: all 0.2s;
  white-space: nowrap;
}
.rv-hub-tab:hover {
  color: var(--vp-c-text-1);
  background: var(--vp-c-bg-soft);
}
.rv-hub-tab.active {
  color: var(--vp-c-brand-1);
  border-bottom-color: var(--vp-c-brand-1);
}

.rv-hub-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 24px;
}

.rv-hub-roadmap {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 300px;
}
.rv-roadmap-placeholder {
  text-align: center;
  color: var(--vp-c-text-3);
}
.rv-roadmap-placeholder h3 {
  margin: 16px 0 8px;
  font-size: 20px;
  color: var(--vp-c-text-2);
}
.rv-roadmap-placeholder p {
  margin: 0;
  font-size: 15px;
}

@media (max-width: 768px) {
  .rv-hub-header {
    padding: 24px 16px 20px;
  }
  .rv-hub-title {
    font-size: 22px;
  }
  .rv-hub-subtitle {
    font-size: 14px;
  }
  .rv-hub-tabs {
    padding: 0 16px;
    overflow-x: auto;
  }
  .rv-hub-tab {
    padding: 12px 14px;
    font-size: 14px;
  }
  .rv-hub-content {
    padding: 16px;
  }
}
</style>
