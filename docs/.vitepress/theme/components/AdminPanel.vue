<script setup lang="ts">
import { ref, onMounted, computed } from "vue";
import { useData } from "vitepress";
import {
  getAdminRecent,
  hideFeature,
  hideDiscussion,
  hideComment,
  deleteFeature,
  deleteDiscussion,
  deleteComment,
  updateFeatureStatus,
  batchDelete,
  type AdminRecentData,
} from "./HubApi";

const { lang } = useData();
const isZh = computed(() => lang.value === "zh" || lang.value === "zh-CN");

const loading = ref(false);
const error = ref("");
const data = ref<AdminRecentData | null>(null);
const activeSection = ref<"features" | "discussions" | "comments">("features");

const selectedFeatures = ref<Set<number>>(new Set());
const selectedDiscussions = ref<Set<number>>(new Set());
const selectedComments = ref<Set<number>>(new Set());
const batchDeleting = ref(false);

const currentSelected = computed(() => {
  if (activeSection.value === "features") return selectedFeatures.value;
  if (activeSection.value === "discussions") return selectedDiscussions.value;
  return selectedComments.value;
});

const allChecked = computed(() => {
  if (!data.value) return false;
  const items = activeSection.value === "features" ? data.value.features
    : activeSection.value === "discussions" ? data.value.discussions
    : data.value.comments;
  return items.length > 0 && currentSelected.value.size === items.length;
});

function toggleItem(id: number) {
  const s = currentSelected.value;
  if (s.has(id)) s.delete(id);
  else s.add(id);
}

function toggleAll() {
  if (!data.value) return;
  const items = activeSection.value === "features" ? data.value.features
    : activeSection.value === "discussions" ? data.value.discussions
    : data.value.comments;
  const s = currentSelected.value;
  if (s.size === items.length) {
    s.clear();
  } else {
    for (const item of items) s.add(item.id);
  }
}

function clearSelections() {
  selectedFeatures.value.clear();
  selectedDiscussions.value.clear();
  selectedComments.value.clear();
}

async function load() {
  loading.value = true;
  error.value = "";
  try {
    data.value = await getAdminRecent();
    clearSelections();
  } catch (e) {
    error.value = (e as Error).message;
  } finally {
    loading.value = false;
  }
}

async function doBatchDelete() {
  const count = currentSelected.value.size;
  if (count === 0) return;
  const msg = isZh.value
    ? `确认批量删除 ${count} 条内容？此操作不可撤销。`
    : `Delete ${count} selected items? This cannot be undone.`;
  if (!confirm(msg)) return;

  batchDeleting.value = true;
  error.value = "";
  try {
    const payload: { features?: number[]; discussions?: number[]; comments?: number[] } = {};
    if (activeSection.value === "features") payload.features = [...selectedFeatures.value];
    else if (activeSection.value === "discussions") payload.discussions = [...selectedDiscussions.value];
    else payload.comments = [...selectedComments.value];
    await batchDelete(payload);
    await load();
  } catch (e) {
    error.value = (e as Error).message;
  } finally {
    batchDeleting.value = false;
  }
}

async function doHideFeature(id: number) {
  try { await hideFeature(id); load(); } catch (e) { error.value = (e as Error).message; }
}
async function doDeleteFeature(id: number) {
  if (!confirm(isZh.value ? "确认删除？" : "Confirm delete?")) return;
  try { await deleteFeature(id); load(); } catch (e) { error.value = (e as Error).message; }
}
async function doSetStatus(id: number, status: string) {
  try { await updateFeatureStatus(id, status); load(); } catch (e) { error.value = (e as Error).message; }
}
async function doHideDisc(id: number) {
  try { await hideDiscussion(id); load(); } catch (e) { error.value = (e as Error).message; }
}
async function doDeleteDisc(id: number) {
  if (!confirm(isZh.value ? "确认删除？" : "Confirm delete?")) return;
  try { await deleteDiscussion(id); load(); } catch (e) { error.value = (e as Error).message; }
}
async function doHideCmt(id: number) {
  try { await hideComment(id); load(); } catch (e) { error.value = (e as Error).message; }
}
async function doDeleteCmt(id: number) {
  if (!confirm(isZh.value ? "确认删除？" : "Confirm delete?")) return;
  try { await deleteComment(id); load(); } catch (e) { error.value = (e as Error).message; }
}

function timeAgo(ts: string): string {
  const d = new Date(ts + "Z");
  const diff = (Date.now() - d.getTime()) / 1000;
  if (diff < 60) return isZh.value ? "刚刚" : "just now";
  if (diff < 3600) return `${Math.floor(diff / 60)}m`;
  if (diff < 86400) return `${Math.floor(diff / 3600)}h`;
  return `${Math.floor(diff / 86400)}d`;
}

onMounted(load);
</script>

<template>
  <div class="adm-panel">
    <div class="adm-header">
      <h3 class="adm-title">{{ isZh ? "内容管理" : "Content Management" }}</h3>
      <button class="adm-refresh" @click="load" :disabled="loading">
        {{ isZh ? "刷新" : "Refresh" }}
      </button>
    </div>

    <div v-if="error" class="adm-error">{{ error }}</div>
    <div v-if="loading" class="adm-loading">Loading...</div>

    <div v-if="data && !loading" class="adm-content">
      <div class="adm-tabs">
        <button
          v-for="sec in [
            { key: 'features', label: isZh ? `功能建议 (${data.features.length})` : `Features (${data.features.length})` },
            { key: 'discussions', label: isZh ? `讨论 (${data.discussions.length})` : `Discussions (${data.discussions.length})` },
            { key: 'comments', label: isZh ? `评论 (${data.comments.length})` : `Comments (${data.comments.length})` },
          ]"
          :key="sec.key"
          class="adm-tab"
          :class="{ active: activeSection === sec.key }"
          @click="activeSection = sec.key as typeof activeSection"
        >
          {{ sec.label }}
        </button>
      </div>

      <!-- Batch toolbar -->
      <div v-if="currentSelected.size > 0" class="adm-batch-bar">
        <span class="adm-batch-count">
          {{ isZh ? `已选 ${currentSelected.size} 项` : `${currentSelected.size} selected` }}
        </span>
        <button class="adm-btn adm-btn-danger" @click="doBatchDelete" :disabled="batchDeleting">
          {{ batchDeleting
            ? (isZh ? "删除中..." : "Deleting...")
            : (isZh ? `批量删除 (${currentSelected.size})` : `Delete Selected (${currentSelected.size})`) }}
        </button>
        <button class="adm-btn adm-btn-clear" @click="currentSelected.clear()">
          {{ isZh ? "取消选择" : "Clear" }}
        </button>
      </div>

      <!-- Features -->
      <div v-if="activeSection === 'features'" class="adm-list">
        <div class="adm-list-header">
          <label class="adm-checkbox-label">
            <input type="checkbox" :checked="allChecked" @change="toggleAll" class="adm-checkbox" />
            <span>{{ isZh ? "全选" : "All" }}</span>
          </label>
        </div>
        <div v-for="f in data.features" :key="f.id" class="adm-item" :class="{ selected: selectedFeatures.has(f.id) }">
          <input type="checkbox" :checked="selectedFeatures.has(f.id)" @change="toggleItem(f.id)" class="adm-checkbox" />
          <div class="adm-item-main">
            <span class="adm-item-title">{{ f.title }}</span>
            <span class="adm-item-meta">{{ f.author_name }} | {{ timeAgo(f.created_at) }} | {{ f.status }}</span>
          </div>
          <div class="adm-item-actions">
            <select @change="(e: Event) => doSetStatus(f.id, (e.target as HTMLSelectElement).value)" class="adm-select">
              <option value="" disabled selected>{{ isZh ? "状态" : "Status" }}</option>
              <option value="open">Open</option>
              <option value="planned">Planned</option>
              <option value="in_progress">In Progress</option>
              <option value="completed">Completed</option>
              <option value="declined">Declined</option>
            </select>
            <button class="adm-btn adm-btn-warn" @click="doHideFeature(f.id)">{{ isZh ? "隐藏" : "Hide" }}</button>
            <button class="adm-btn adm-btn-danger" @click="doDeleteFeature(f.id)">{{ isZh ? "删除" : "Del" }}</button>
          </div>
        </div>
      </div>

      <!-- Discussions -->
      <div v-if="activeSection === 'discussions'" class="adm-list">
        <div class="adm-list-header">
          <label class="adm-checkbox-label">
            <input type="checkbox" :checked="allChecked" @change="toggleAll" class="adm-checkbox" />
            <span>{{ isZh ? "全选" : "All" }}</span>
          </label>
        </div>
        <div v-for="d in data.discussions" :key="d.id" class="adm-item" :class="{ hidden: d.is_hidden, selected: selectedDiscussions.has(d.id) }">
          <input type="checkbox" :checked="selectedDiscussions.has(d.id)" @change="toggleItem(d.id)" class="adm-checkbox" />
          <div class="adm-item-main">
            <span class="adm-item-title">{{ d.title }}</span>
            <span class="adm-item-meta">
              {{ d.author_name }} | {{ timeAgo(d.created_at) }}
              <span v-if="d.is_hidden" class="adm-badge-hidden">{{ isZh ? "已隐藏" : "Hidden" }}</span>
            </span>
          </div>
          <div class="adm-item-actions">
            <button class="adm-btn adm-btn-warn" @click="doHideDisc(d.id)">{{ isZh ? "隐藏" : "Hide" }}</button>
            <button class="adm-btn adm-btn-danger" @click="doDeleteDisc(d.id)">{{ isZh ? "删除" : "Del" }}</button>
          </div>
        </div>
      </div>

      <!-- Comments -->
      <div v-if="activeSection === 'comments'" class="adm-list">
        <div class="adm-list-header">
          <label class="adm-checkbox-label">
            <input type="checkbox" :checked="allChecked" @change="toggleAll" class="adm-checkbox" />
            <span>{{ isZh ? "全选" : "All" }}</span>
          </label>
        </div>
        <div v-for="c in data.comments" :key="c.id" class="adm-item" :class="{ hidden: c.is_hidden, selected: selectedComments.has(c.id) }">
          <input type="checkbox" :checked="selectedComments.has(c.id)" @change="toggleItem(c.id)" class="adm-checkbox" />
          <div class="adm-item-main">
            <span class="adm-item-title">{{ c.body?.slice(0, 80) }}{{ (c.body?.length ?? 0) > 80 ? "..." : "" }}</span>
            <span class="adm-item-meta">
              {{ c.author_name }} | {{ c.target_type }} #{{ c.target_id }} | {{ timeAgo(c.created_at) }}
              <span v-if="c.is_hidden" class="adm-badge-hidden">{{ isZh ? "已隐藏" : "Hidden" }}</span>
            </span>
          </div>
          <div class="adm-item-actions">
            <button class="adm-btn adm-btn-warn" @click="doHideCmt(c.id)">{{ isZh ? "隐藏" : "Hide" }}</button>
            <button class="adm-btn adm-btn-danger" @click="doDeleteCmt(c.id)">{{ isZh ? "删除" : "Del" }}</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.adm-panel { padding: 4px 0; }
.adm-header { display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px; }
.adm-title { font-size: 18px; font-weight: 600; color: var(--vp-c-text-1); margin: 0; }
.adm-refresh {
  padding: 5px 14px; border: 1px solid var(--vp-c-divider); border-radius: 6px;
  background: var(--vp-c-bg); color: var(--vp-c-text-2); cursor: pointer; font-size: 13px;
}
.adm-refresh:hover { background: var(--vp-c-default-soft); }
.adm-error { padding: 8px 12px; background: #fed7d7; color: #e53e3e; border-radius: 6px; margin-bottom: 12px; font-size: 13px; }
.adm-loading { text-align: center; color: var(--vp-c-text-3); padding: 24px; }

.adm-tabs { display: flex; gap: 4px; margin-bottom: 12px; border-bottom: 1px solid var(--vp-c-divider); }
.adm-tab {
  padding: 8px 16px; border: none; background: none; cursor: pointer;
  font-size: 13px; color: var(--vp-c-text-2); border-bottom: 2px solid transparent;
}
.adm-tab.active { color: var(--vp-c-brand-1); border-bottom-color: var(--vp-c-brand-1); font-weight: 500; }
.adm-tab:hover { color: var(--vp-c-text-1); }

.adm-batch-bar {
  display: flex; align-items: center; gap: 10px;
  padding: 8px 12px; margin-bottom: 8px;
  background: var(--vp-c-default-soft); border-radius: 6px;
  border: 1px solid var(--vp-c-brand-soft);
}
.adm-batch-count { font-size: 13px; font-weight: 500; color: var(--vp-c-brand-1); }

.adm-list { display: flex; flex-direction: column; gap: 6px; }
.adm-list-header {
  display: flex; align-items: center; padding: 4px 12px;
  font-size: 12px; color: var(--vp-c-text-3);
}
.adm-checkbox-label { display: flex; align-items: center; gap: 6px; cursor: pointer; user-select: none; font-size: 12px; color: var(--vp-c-text-3); }
.adm-checkbox {
  width: 15px; height: 15px; cursor: pointer; flex-shrink: 0;
  accent-color: var(--vp-c-brand-1);
}
.adm-item {
  display: flex; align-items: center; justify-content: space-between;
  padding: 8px 12px; border: 1px solid var(--vp-c-divider); border-radius: 6px;
  background: var(--vp-c-bg-soft); gap: 8px;
}
.adm-item.hidden { opacity: 0.5; }
.adm-item.selected { border-color: var(--vp-c-brand-soft); background: var(--vp-c-brand-dimm); }
.adm-item-main { flex: 1; min-width: 0; }
.adm-item-title { display: block; font-size: 13px; color: var(--vp-c-text-1); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.adm-item-meta { display: block; font-size: 11px; color: var(--vp-c-text-3); margin-top: 2px; }
.adm-badge-hidden { background: #fed7d7; color: #e53e3e; padding: 1px 6px; border-radius: 4px; font-size: 10px; margin-left: 4px; }
.adm-item-actions { display: flex; gap: 4px; margin-left: 4px; flex-shrink: 0; }
.adm-select {
  padding: 3px 6px; border: 1px solid var(--vp-c-divider); border-radius: 4px;
  font-size: 11px; background: var(--vp-c-bg); color: var(--vp-c-text-2);
}
.adm-btn {
  padding: 3px 8px; border: none; border-radius: 4px; font-size: 11px;
  cursor: pointer; font-weight: 500;
}
.adm-btn-warn { background: #fefcbf; color: #d69e2e; }
.adm-btn-warn:hover { background: #fef08a; }
.adm-btn-danger { background: #fed7d7; color: #e53e3e; }
.adm-btn-danger:hover { background: #fc8181; color: #fff; }
.adm-btn-clear { background: var(--vp-c-bg); color: var(--vp-c-text-2); border: 1px solid var(--vp-c-divider); }
.adm-btn-clear:hover { background: var(--vp-c-default-soft); }
.adm-btn:disabled { opacity: 0.5; cursor: not-allowed; }
</style>
