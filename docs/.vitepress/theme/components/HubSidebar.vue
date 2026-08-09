<script setup lang="ts">
import { computed } from "vue";
import { useData } from "vitepress";
import {
  HUB_TABS,
  HUB_ADMIN_TAB,
  FEATURE_CATEGORIES,
  DISCUSSION_CHANNELS,
  hubLabel,
  hubDesc,
  type HubTabKey,
} from "./HubNavData";

const props = defineProps<{
  activeTab: HubTabKey;
  featureCategory: string;
  discussionCategory: string;
  showAdmin?: boolean;
  mobileOpen?: boolean;
}>();

const emit = defineEmits<{
  "update:activeTab": [HubTabKey];
  "update:featureCategory": [string];
  "update:discussionCategory": [string];
  closeMobile: [];
}>();

const { lang } = useData();
const isZh = computed(() => lang.value === "zh" || lang.value === "zh-CN");

const tabs = computed(() =>
  props.showAdmin ? [...HUB_TABS, HUB_ADMIN_TAB] : HUB_TABS
);

const subItems = computed(() => {
  if (props.activeTab === "features" || props.activeTab === "billboard") {
    return FEATURE_CATEGORIES;
  }
  if (props.activeTab === "discussions") return DISCUSSION_CHANNELS;
  return [];
});

const subTitle = computed(() => {
  if (props.activeTab === "features" || props.activeTab === "billboard") {
    return isZh.value ? "模块" : "Modules";
  }
  if (props.activeTab === "discussions") return isZh.value ? "频道" : "Channels";
  return "";
});

const activeSub = computed(() => {
  if (props.activeTab === "features" || props.activeTab === "billboard") {
    return props.featureCategory;
  }
  if (props.activeTab === "discussions") return props.discussionCategory;
  return "";
});

function selectTab(key: HubTabKey) {
  emit("update:activeTab", key);
  emit("closeMobile");
}

function selectSub(value: string) {
  if (props.activeTab === "features" || props.activeTab === "billboard") {
    emit("update:featureCategory", value);
  } else if (props.activeTab === "discussions") {
    emit("update:discussionCategory", value);
  }
  emit("closeMobile");
}
</script>

<template>
  <aside class="hub-side" :class="{ 'hub-side-open': mobileOpen }">
    <div class="hub-side-brand">
      <span class="hub-side-brand-text">Reguverse Hub</span>
    </div>

    <nav class="hub-side-nav" aria-label="Hub modules">
      <button
        v-for="tab in tabs"
        :key="tab.key"
        type="button"
        class="hub-side-tab"
        :class="{ active: activeTab === tab.key }"
        @click="selectTab(tab.key)"
      >
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
          <path :d="tab.icon" />
        </svg>
        <span>{{ hubLabel(tab, isZh) }}</span>
      </button>
    </nav>

    <div v-if="subItems.length" class="hub-side-sub">
      <div class="hub-side-sub-title">{{ subTitle }}</div>
      <nav class="hub-side-sub-list" :aria-label="subTitle">
        <button
          v-for="item in subItems"
          :key="item.value || '__all__'"
          type="button"
          class="hub-side-sub-item"
          :class="{ active: activeSub === item.value }"
          :title="hubDesc(item, isZh) || undefined"
          @click="selectSub(item.value)"
        >
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
            <path :d="item.icon" />
          </svg>
          <span class="hub-side-sub-label">{{ hubLabel(item, isZh) }}</span>
        </button>
      </nav>
    </div>
  </aside>
</template>

<style scoped>
.hub-side {
  width: 260px;
  flex-shrink: 0;
  display: flex;
  flex-direction: column;
  gap: 4px;
  padding: 12px 10px 20px;
  background: var(--vp-c-bg-soft);
  border-right: 1px solid var(--vp-c-divider);
  position: sticky;
  top: var(--vp-nav-height, 64px);
  height: calc(100vh - var(--vp-nav-height, 64px));
  overflow-y: auto;
  z-index: 5;
}

.hub-side-brand {
  padding: 8px 10px 14px;
  border-bottom: 1px solid var(--vp-c-divider);
  margin-bottom: 8px;
}
.hub-side-brand-text {
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.02em;
  color: var(--vp-c-text-1);
}

.hub-side-nav {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.hub-side-tab {
  display: flex;
  align-items: center;
  gap: 10px;
  width: 100%;
  padding: 10px 12px;
  border: none;
  border-radius: 8px;
  background: transparent;
  color: var(--vp-c-text-2);
  font-size: 14px;
  font-weight: 550;
  cursor: pointer;
  text-align: left;
  transition: background 0.15s, color 0.15s;
}
.hub-side-tab:hover {
  background: var(--vp-c-bg);
  color: var(--vp-c-text-1);
}
.hub-side-tab.active {
  background: var(--vp-c-brand-soft);
  color: var(--vp-c-brand-1);
}
.hub-side-tab svg {
  flex-shrink: 0;
}

.hub-side-sub {
  margin-top: 12px;
  padding-top: 12px;
  border-top: 1px solid var(--vp-c-divider);
}
.hub-side-sub-title {
  padding: 0 12px 8px;
  font-size: 11px;
  font-weight: 650;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--vp-c-text-3);
}
.hub-side-sub-list {
  display: flex;
  flex-direction: column;
  gap: 1px;
}
.hub-side-sub-item {
  display: flex;
  align-items: center;
  gap: 8px;
  width: 100%;
  padding: 7px 12px;
  border: none;
  border-radius: 7px;
  background: transparent;
  color: var(--vp-c-text-2);
  font-size: 13px;
  cursor: pointer;
  text-align: left;
  transition: background 0.15s, color 0.15s;
}
.hub-side-sub-item:hover {
  background: var(--vp-c-bg);
  color: var(--vp-c-text-1);
}
.hub-side-sub-item.active {
  background: var(--vp-c-bg);
  color: var(--vp-c-brand-1);
  font-weight: 600;
}
.hub-side-sub-item svg {
  flex-shrink: 0;
  opacity: 0.85;
}
.hub-side-sub-label {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

@media (max-width: 960px) {
  .hub-side {
    position: fixed;
    left: 0;
    top: var(--vp-nav-height, 64px);
    bottom: 0;
    height: auto;
    width: min(280px, 86vw);
    transform: translateX(-105%);
    transition: transform 0.2s ease;
    box-shadow: 8px 0 24px rgba(0, 0, 0, 0.12);
    z-index: 40;
  }
  .hub-side.hub-side-open {
    transform: translateX(0);
  }
}
</style>
