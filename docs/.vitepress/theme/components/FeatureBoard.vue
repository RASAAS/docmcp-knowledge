<script setup lang="ts">
import { ref, onMounted, computed } from "vue";
import { useData } from "vitepress";
import {
  listFeatures,
  createFeature,
  toggleVote,
  isLoggedIn,
  type Feature,
} from "./HubApi";

const { lang } = useData();
const isZh = computed(() => lang.value === "zh" || lang.value === "zh-CN");

const features = ref<Feature[]>([]);
const total = ref(0);
const page = ref(1);
const pages = ref(1);
const loading = ref(false);
const error = ref("");

const category = ref("");
const sort = ref("votes");

const showForm = ref(false);
const formTitle = ref("");
const formDesc = ref("");
const formCategory = ref("general");
const formName = ref("");
const formEmail = ref("");
const submitting = ref(false);

const categories = computed(() => [
  { value: "", label: isZh.value ? "全部" : "All" },
  { value: "ce_workflow", label: isZh.value ? "临床评价" : "Clinical Evaluation" },
  { value: "risk_management", label: isZh.value ? "风险管理" : "Risk Management" },
  { value: "pms_pmcf", label: "PMS / PMCF" },
  { value: "gspr", label: "GSPR" },
  { value: "ai_tools", label: isZh.value ? "AI 工具" : "AI Tools" },
  { value: "knowledge_base", label: isZh.value ? "知识库" : "Knowledge Base" },
  { value: "general", label: isZh.value ? "通用" : "General" },
]);

const statusLabels: Record<string, { text: string; textZh: string; color: string }> = {
  under_review: { text: "Under Review", textZh: "审核中", color: "#666" },
  planned: { text: "Planned", textZh: "已规划", color: "#0070f3" },
  in_progress: { text: "In Progress", textZh: "开发中", color: "#f5a623" },
  completed: { text: "Completed", textZh: "已完成", color: "#0cce6b" },
  declined: { text: "Declined", textZh: "已拒绝", color: "#e00" },
};

const loggedIn = computed(() => isLoggedIn());

async function load() {
  loading.value = true;
  error.value = "";
  try {
    const data = await listFeatures({
      category: category.value || undefined,
      sort: sort.value,
      page: page.value,
    });
    features.value = data.items;
    total.value = data.total;
    pages.value = data.pages;
  } catch (e) {
    error.value = (e as Error).message;
  } finally {
    loading.value = false;
  }
}

async function vote(f: Feature) {
  try {
    const result = await toggleVote(f.id, {
      author_email: formEmail.value || undefined,
    });
    f.user_voted = result.voted;
    f.vote_count += result.voted ? (loggedIn.value ? 2 : 1) : -(loggedIn.value ? 2 : 1);
  } catch (e) {
    error.value = (e as Error).message;
  }
}

async function submit() {
  if (!formTitle.value.trim() || !formDesc.value.trim()) return;
  submitting.value = true;
  error.value = "";
  try {
    await createFeature({
      title: formTitle.value.trim(),
      description: formDesc.value.trim(),
      category: formCategory.value,
      author_name: formName.value.trim() || undefined,
      author_email: formEmail.value.trim() || undefined,
    });
    showForm.value = false;
    formTitle.value = "";
    formDesc.value = "";
    formName.value = "";
    page.value = 1;
    sort.value = "newest";
    await load();
  } catch (e) {
    error.value = (e as Error).message;
  } finally {
    submitting.value = false;
  }
}

function timeAgo(dateStr: string): string {
  const now = Date.now();
  const then = new Date(dateStr + "Z").getTime();
  const diff = now - then;
  const mins = Math.floor(diff / 60000);
  if (mins < 1) return isZh.value ? "刚刚" : "just now";
  if (mins < 60) return isZh.value ? `${mins}分钟前` : `${mins}m ago`;
  const hours = Math.floor(mins / 60);
  if (hours < 24) return isZh.value ? `${hours}小时前` : `${hours}h ago`;
  const days = Math.floor(hours / 24);
  if (days < 30) return isZh.value ? `${days}天前` : `${days}d ago`;
  return new Date(dateStr).toLocaleDateString();
}

onMounted(load);
</script>

<template>
  <div class="fb">
    <!-- Header bar -->
    <div class="fb-header">
      <div class="fb-header-left">
        <h2 class="fb-section-title">
          {{ isZh ? "功能建议板" : "Feature Board" }}
          <span class="fb-count" v-if="total">{{ total }}</span>
        </h2>
      </div>
      <button class="fb-btn fb-btn-primary" @click="showForm = !showForm">
        {{ showForm ? (isZh ? "取消" : "Cancel") : (isZh ? "+ 提交建议" : "+ Submit Idea") }}
      </button>
    </div>

    <!-- Filters -->
    <div class="fb-filters">
      <div class="fb-filter-group">
        <button
          v-for="c in categories"
          :key="c.value"
          class="fb-filter-chip"
          :class="{ active: category === c.value }"
          @click="category = c.value; page = 1; load()"
        >
          {{ c.label }}
        </button>
      </div>
      <select v-model="sort" @change="page = 1; load()" class="fb-sort-select">
        <option value="votes">{{ isZh ? "最多投票" : "Most Voted" }}</option>
        <option value="newest">{{ isZh ? "最新" : "Newest" }}</option>
        <option value="updated">{{ isZh ? "最近更新" : "Recently Updated" }}</option>
      </select>
    </div>

    <!-- Submit Form -->
    <div v-if="showForm" class="fb-form">
      <div class="fb-form-grid">
        <div v-if="!loggedIn" class="fb-form-row">
          <input v-model="formName" :placeholder="isZh ? '您的姓名 *' : 'Your name *'" class="fb-input" />
          <input v-model="formEmail" :placeholder="isZh ? '邮箱（用于投票追踪）' : 'Email (for vote tracking)'" class="fb-input" />
        </div>
        <input
          v-model="formTitle"
          :placeholder="isZh ? '功能标题 *' : 'Feature title *'"
          class="fb-input fb-input-full"
        />
        <textarea
          v-model="formDesc"
          :placeholder="isZh ? '描述您想要的功能...*' : 'Describe the feature you\'d like to see... *'"
          class="fb-textarea"
          rows="4"
        ></textarea>
        <div class="fb-form-actions">
          <select v-model="formCategory" class="fb-sort-select">
            <option v-for="c in categories.slice(1)" :key="c.value" :value="c.value">{{ c.label }}</option>
          </select>
          <button
            class="fb-btn fb-btn-primary"
            :disabled="submitting || !formTitle.trim() || !formDesc.trim()"
            @click="submit"
          >
            {{ submitting ? (isZh ? "提交中..." : "Submitting...") : (isZh ? "提交" : "Submit") }}
          </button>
        </div>
      </div>
    </div>

    <!-- Error -->
    <div v-if="error" class="fb-error">{{ error }}</div>

    <!-- Loading -->
    <div v-if="loading" class="fb-loading">
      <div class="fb-spinner"></div>
      {{ isZh ? "加载中..." : "Loading..." }}
    </div>

    <!-- Feature Grid -->
    <div v-else class="fb-grid">
      <div v-if="features.length === 0" class="fb-empty">
        <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="var(--vp-c-text-3)" stroke-width="1.5">
          <path d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        <p>{{ isZh ? "暂无功能建议。成为第一个提交建议的人！" : "No feature requests yet. Be the first to submit one!" }}</p>
      </div>

      <div v-for="f in features" :key="f.id" class="fb-card">
        <div class="fb-card-vote" @click="vote(f)">
          <button class="fb-vote-btn" :class="{ voted: f.user_voted }" :title="f.user_voted ? 'Remove vote' : 'Upvote'">
            <svg width="14" height="14" viewBox="0 0 16 16" fill="currentColor"><path d="M8 4l4 5H4l4-5z"/></svg>
          </button>
          <span class="fb-vote-num">{{ f.vote_count }}</span>
        </div>
        <div class="fb-card-content">
          <div class="fb-card-top">
            <h3 class="fb-card-title">{{ f.title }}</h3>
            <span
              v-if="statusLabels[f.status]"
              class="fb-status"
              :style="{ '--status-color': statusLabels[f.status].color }"
            >
              {{ isZh ? statusLabels[f.status].textZh : statusLabels[f.status].text }}
            </span>
          </div>
          <p class="fb-card-desc">{{ f.description }}</p>
          <div class="fb-card-footer">
            <span class="fb-tag">{{ f.category.replace(/_/g, " ") }}</span>
            <span v-if="f.is_verified" class="fb-verified">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="var(--vp-c-brand-1)"><path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
              Verified
            </span>
            <span class="fb-meta">{{ f.author_name }}</span>
            <span class="fb-meta fb-meta-dot">{{ timeAgo(f.created_at) }}</span>
            <span class="fb-meta fb-meta-dot">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z"/></svg>
              {{ f.comment_count }}
            </span>
          </div>
        </div>
      </div>
    </div>

    <!-- Pagination -->
    <div v-if="pages > 1" class="fb-pagination">
      <button :disabled="page <= 1" @click="page--; load()" class="fb-btn fb-btn-sm">
        {{ isZh ? "上一页" : "Prev" }}
      </button>
      <span class="fb-page-info">{{ page }} / {{ pages }}</span>
      <button :disabled="page >= pages" @click="page++; load()" class="fb-btn fb-btn-sm">
        {{ isZh ? "下一页" : "Next" }}
      </button>
    </div>
  </div>
</template>

<style scoped>
.fb-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
}
.fb-section-title {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 20px;
  font-weight: 600;
  margin: 0;
  color: var(--vp-c-text-1);
}
.fb-count {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 24px;
  height: 24px;
  padding: 0 8px;
  border-radius: 12px;
  background: var(--vp-c-bg-soft);
  color: var(--vp-c-text-2);
  font-size: 13px;
  font-weight: 500;
}

.fb-filters {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 12px;
  margin-bottom: 20px;
  flex-wrap: wrap;
}
.fb-filter-group {
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
}
.fb-filter-chip {
  padding: 5px 12px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 16px;
  background: var(--vp-c-bg);
  color: var(--vp-c-text-2);
  font-size: 13px;
  cursor: pointer;
  transition: all 0.15s;
  white-space: nowrap;
}
.fb-filter-chip:hover {
  border-color: var(--vp-c-brand-1);
  color: var(--vp-c-brand-1);
}
.fb-filter-chip.active {
  background: var(--vp-c-brand-soft);
  border-color: var(--vp-c-brand-1);
  color: var(--vp-c-brand-1);
  font-weight: 500;
}
.fb-sort-select {
  padding: 6px 10px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 6px;
  background: var(--vp-c-bg);
  color: var(--vp-c-text-1);
  font-size: 13px;
}

.fb-btn {
  padding: 7px 16px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  cursor: pointer;
  font-size: 14px;
  font-weight: 500;
  background: var(--vp-c-bg);
  color: var(--vp-c-text-1);
  transition: all 0.15s;
}
.fb-btn:hover { border-color: var(--vp-c-brand-1); }
.fb-btn:disabled { opacity: 0.5; cursor: not-allowed; }
.fb-btn-primary {
  background: var(--vp-c-brand-1);
  color: white;
  border-color: var(--vp-c-brand-1);
}
.fb-btn-primary:hover { background: var(--vp-c-brand-2); }
.fb-btn-sm { padding: 5px 12px; font-size: 13px; }

.fb-form {
  border: 1px solid var(--vp-c-divider);
  border-radius: 12px;
  padding: 20px;
  margin-bottom: 20px;
  background: var(--vp-c-bg-soft);
}
.fb-form-grid {
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.fb-form-row { display: flex; gap: 10px; }
.fb-input {
  padding: 9px 14px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  font-size: 14px;
  background: var(--vp-c-bg);
  color: var(--vp-c-text-1);
  width: 100%;
  transition: border-color 0.15s;
}
.fb-input:focus { border-color: var(--vp-c-brand-1); outline: none; }
.fb-input-full { width: 100%; }
.fb-textarea {
  width: 100%;
  padding: 9px 14px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  font-size: 14px;
  resize: vertical;
  background: var(--vp-c-bg);
  color: var(--vp-c-text-1);
  font-family: inherit;
  transition: border-color 0.15s;
}
.fb-textarea:focus { border-color: var(--vp-c-brand-1); outline: none; }
.fb-form-actions {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.fb-error {
  color: var(--vp-c-danger-1);
  padding: 10px 14px;
  background: var(--vp-c-danger-soft);
  border-radius: 8px;
  margin-bottom: 16px;
  font-size: 14px;
}

.fb-loading {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  padding: 48px;
  color: var(--vp-c-text-2);
  font-size: 15px;
}
.fb-spinner {
  width: 20px;
  height: 20px;
  border: 2px solid var(--vp-c-divider);
  border-top-color: var(--vp-c-brand-1);
  border-radius: 50%;
  animation: spin 0.6s linear infinite;
}
@keyframes spin { to { transform: rotate(360deg); } }

.fb-empty {
  text-align: center;
  padding: 60px 20px;
  color: var(--vp-c-text-3);
}
.fb-empty p { margin: 12px 0 0; font-size: 15px; }

.fb-grid {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.fb-card {
  display: flex;
  gap: 16px;
  padding: 18px 20px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 12px;
  background: var(--vp-c-bg);
  transition: all 0.2s;
}
.fb-card:hover {
  border-color: var(--vp-c-brand-1);
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.06);
}

.fb-card-vote {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  min-width: 48px;
  cursor: pointer;
  user-select: none;
}
.fb-vote-btn {
  width: 40px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  background: var(--vp-c-bg-soft);
  color: var(--vp-c-text-3);
  cursor: pointer;
  transition: all 0.15s;
}
.fb-vote-btn:hover, .fb-vote-btn.voted {
  border-color: var(--vp-c-brand-1);
  color: var(--vp-c-brand-1);
  background: var(--vp-c-brand-soft);
}
.fb-vote-num {
  font-size: 15px;
  font-weight: 600;
  color: var(--vp-c-text-2);
}

.fb-card-content {
  flex: 1;
  min-width: 0;
}
.fb-card-top {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  margin-bottom: 6px;
}
.fb-card-title {
  font-size: 16px;
  font-weight: 600;
  margin: 0;
  color: var(--vp-c-text-1);
  flex: 1;
}
.fb-status {
  font-size: 11px;
  padding: 2px 8px;
  border: 1px solid var(--status-color);
  color: var(--status-color);
  border-radius: 6px;
  white-space: nowrap;
  font-weight: 500;
  flex-shrink: 0;
}
.fb-card-desc {
  font-size: 14px;
  color: var(--vp-c-text-2);
  margin: 0 0 10px;
  line-height: 1.6;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.fb-card-footer {
  display: flex;
  gap: 10px;
  align-items: center;
  flex-wrap: wrap;
}
.fb-tag {
  font-size: 11px;
  padding: 2px 8px;
  border-radius: 6px;
  background: var(--vp-c-bg-soft);
  color: var(--vp-c-text-2);
  border: 1px solid var(--vp-c-divider);
  text-transform: capitalize;
}
.fb-verified {
  display: inline-flex;
  align-items: center;
  gap: 3px;
  font-size: 11px;
  color: var(--vp-c-brand-1);
  font-weight: 500;
}
.fb-meta {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-size: 12px;
  color: var(--vp-c-text-3);
}
.fb-meta-dot::before {
  content: "";
  display: inline-block;
  width: 3px;
  height: 3px;
  border-radius: 50%;
  background: var(--vp-c-text-3);
  margin-right: 2px;
}

.fb-pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 16px;
  margin-top: 20px;
}
.fb-page-info {
  font-size: 14px;
  color: var(--vp-c-text-2);
}
</style>
