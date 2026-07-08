<script setup lang="ts">
import { ref, onMounted, computed } from "vue";
import {
  listFeatures,
  createFeature,
  toggleVote,
  isLoggedIn,
  type Feature,
} from "./HubApi";

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

const categories = [
  { value: "", label: "All" },
  { value: "ce_workflow", label: "Clinical Evaluation" },
  { value: "risk_management", label: "Risk Management" },
  { value: "pms_pmcf", label: "PMS / PMCF" },
  { value: "gspr", label: "GSPR" },
  { value: "ai_tools", label: "AI Tools" },
  { value: "knowledge_base", label: "Knowledge Base" },
  { value: "general", label: "General" },
];

const statusLabels: Record<string, { text: string; color: string }> = {
  under_review: { text: "Under Review", color: "#666" },
  planned: { text: "Planned", color: "#0070f3" },
  in_progress: { text: "In Progress", color: "#f5a623" },
  completed: { text: "Completed", color: "#0cce6b" },
  declined: { text: "Declined", color: "#e00" },
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
  if (mins < 60) return `${mins}m ago`;
  const hours = Math.floor(mins / 60);
  if (hours < 24) return `${hours}h ago`;
  const days = Math.floor(hours / 24);
  if (days < 30) return `${days}d ago`;
  return new Date(dateStr).toLocaleDateString();
}

onMounted(load);
</script>

<template>
  <div class="hub-feature-board">
    <!-- Toolbar -->
    <div class="hub-toolbar">
      <div class="hub-filters">
        <select v-model="category" @change="page = 1; load()">
          <option v-for="c in categories" :key="c.value" :value="c.value">
            {{ c.label }}
          </option>
        </select>
        <select v-model="sort" @change="page = 1; load()">
          <option value="votes">Most Voted</option>
          <option value="newest">Newest</option>
          <option value="updated">Recently Updated</option>
        </select>
      </div>
      <button class="hub-btn hub-btn-primary" @click="showForm = !showForm">
        {{ showForm ? "Cancel" : "+ Submit Idea" }}
      </button>
    </div>

    <!-- Submit Form -->
    <div v-if="showForm" class="hub-form">
      <div v-if="!loggedIn" class="hub-form-guest">
        <input
          v-model="formName"
          placeholder="Your name *"
          class="hub-input"
        />
        <input
          v-model="formEmail"
          placeholder="Email (for vote tracking)"
          class="hub-input"
        />
      </div>
      <input
        v-model="formTitle"
        placeholder="Feature title *"
        class="hub-input hub-input-full"
      />
      <textarea
        v-model="formDesc"
        placeholder="Describe the feature you'd like to see... *"
        class="hub-textarea"
        rows="4"
      ></textarea>
      <div class="hub-form-footer">
        <select v-model="formCategory" class="hub-select-small">
          <option v-for="c in categories.slice(1)" :key="c.value" :value="c.value">
            {{ c.label }}
          </option>
        </select>
        <button
          class="hub-btn hub-btn-primary"
          :disabled="submitting || !formTitle.trim() || !formDesc.trim()"
          @click="submit"
        >
          {{ submitting ? "Submitting..." : "Submit" }}
        </button>
      </div>
    </div>

    <!-- Error -->
    <div v-if="error" class="hub-error">{{ error }}</div>

    <!-- Loading -->
    <div v-if="loading" class="hub-loading">Loading...</div>

    <!-- Feature List -->
    <div v-else class="hub-list">
      <div v-if="features.length === 0" class="hub-empty">
        No feature requests yet. Be the first to submit one!
      </div>
      <div
        v-for="f in features"
        :key="f.id"
        class="hub-card"
      >
        <div class="hub-vote-col" @click="vote(f)">
          <button
            class="hub-vote-btn"
            :class="{ voted: f.user_voted }"
            :title="f.user_voted ? 'Remove vote' : 'Upvote'"
          >
            <svg width="16" height="16" viewBox="0 0 16 16" fill="currentColor">
              <path d="M8 4l4 5H4l4-5z"/>
            </svg>
          </button>
          <span class="hub-vote-count">{{ f.vote_count }}</span>
        </div>
        <div class="hub-card-body">
          <div class="hub-card-header">
            <h3 class="hub-card-title">{{ f.title }}</h3>
            <span
              v-if="statusLabels[f.status]"
              class="hub-status"
              :style="{ color: statusLabels[f.status].color, borderColor: statusLabels[f.status].color }"
            >
              {{ statusLabels[f.status].text }}
            </span>
          </div>
          <p class="hub-card-desc">{{ f.description }}</p>
          <div class="hub-card-meta">
            <span class="hub-badge hub-badge-cat">{{ f.category }}</span>
            <span v-if="f.is_verified" class="hub-badge hub-badge-verified" title="Verified Reguverse user">Verified</span>
            <span class="hub-meta-text">{{ f.author_name }}</span>
            <span class="hub-meta-text">{{ timeAgo(f.created_at) }}</span>
            <span class="hub-meta-text">{{ f.comment_count }} comments</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Pagination -->
    <div v-if="pages > 1" class="hub-pagination">
      <button
        :disabled="page <= 1"
        @click="page--; load()"
        class="hub-btn hub-btn-sm"
      >
        Prev
      </button>
      <span class="hub-page-info">Page {{ page }} / {{ pages }}</span>
      <button
        :disabled="page >= pages"
        @click="page++; load()"
        class="hub-btn hub-btn-sm"
      >
        Next
      </button>
    </div>
  </div>
</template>

<style scoped>
.hub-feature-board {
  max-width: 800px;
  margin: 0 auto;
}
.hub-toolbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 12px;
  margin-bottom: 16px;
  flex-wrap: wrap;
}
.hub-filters {
  display: flex;
  gap: 8px;
}
.hub-filters select,
.hub-select-small {
  padding: 6px 10px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 6px;
  background: var(--vp-c-bg);
  color: var(--vp-c-text-1);
  font-size: 14px;
}
.hub-btn {
  padding: 6px 14px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 6px;
  cursor: pointer;
  font-size: 14px;
  background: var(--vp-c-bg);
  color: var(--vp-c-text-1);
  transition: all 0.15s;
}
.hub-btn:hover {
  border-color: var(--vp-c-brand-1);
}
.hub-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
.hub-btn-primary {
  background: var(--vp-c-brand-1);
  color: white;
  border-color: var(--vp-c-brand-1);
}
.hub-btn-primary:hover {
  background: var(--vp-c-brand-2);
}
.hub-btn-sm {
  padding: 4px 10px;
  font-size: 13px;
}
.hub-form {
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  padding: 16px;
  margin-bottom: 16px;
  background: var(--vp-c-bg-soft);
}
.hub-form-guest {
  display: flex;
  gap: 8px;
  margin-bottom: 8px;
}
.hub-input {
  padding: 8px 12px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 6px;
  font-size: 14px;
  background: var(--vp-c-bg);
  color: var(--vp-c-text-1);
  width: 100%;
}
.hub-input-full {
  width: 100%;
  margin-bottom: 8px;
}
.hub-textarea {
  width: 100%;
  padding: 8px 12px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 6px;
  font-size: 14px;
  resize: vertical;
  background: var(--vp-c-bg);
  color: var(--vp-c-text-1);
  margin-bottom: 8px;
  font-family: inherit;
}
.hub-form-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.hub-error {
  color: var(--vp-c-danger-1);
  padding: 8px 12px;
  background: var(--vp-c-danger-soft);
  border-radius: 6px;
  margin-bottom: 12px;
  font-size: 14px;
}
.hub-loading {
  text-align: center;
  padding: 32px;
  color: var(--vp-c-text-2);
}
.hub-empty {
  text-align: center;
  padding: 48px 16px;
  color: var(--vp-c-text-3);
  font-size: 15px;
}
.hub-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.hub-card {
  display: flex;
  gap: 12px;
  padding: 14px 16px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  background: var(--vp-c-bg);
  transition: border-color 0.15s;
}
.hub-card:hover {
  border-color: var(--vp-c-brand-1);
}
.hub-vote-col {
  display: flex;
  flex-direction: column;
  align-items: center;
  min-width: 44px;
  cursor: pointer;
  user-select: none;
}
.hub-vote-btn {
  width: 36px;
  height: 28px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px solid var(--vp-c-divider);
  border-radius: 6px;
  background: var(--vp-c-bg-soft);
  color: var(--vp-c-text-3);
  cursor: pointer;
  transition: all 0.15s;
}
.hub-vote-btn:hover,
.hub-vote-btn.voted {
  border-color: var(--vp-c-brand-1);
  color: var(--vp-c-brand-1);
  background: var(--vp-c-brand-soft);
}
.hub-vote-count {
  font-size: 14px;
  font-weight: 600;
  color: var(--vp-c-text-2);
  margin-top: 2px;
}
.hub-card-body {
  flex: 1;
  min-width: 0;
}
.hub-card-header {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 4px;
}
.hub-card-title {
  font-size: 15px;
  font-weight: 600;
  margin: 0;
  color: var(--vp-c-text-1);
}
.hub-status {
  font-size: 11px;
  padding: 1px 6px;
  border: 1px solid;
  border-radius: 4px;
  white-space: nowrap;
  font-weight: 500;
}
.hub-card-desc {
  font-size: 13px;
  color: var(--vp-c-text-2);
  margin: 4px 0 8px;
  line-height: 1.5;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.hub-card-meta {
  display: flex;
  gap: 8px;
  align-items: center;
  flex-wrap: wrap;
}
.hub-badge {
  font-size: 11px;
  padding: 1px 6px;
  border-radius: 4px;
  font-weight: 500;
}
.hub-badge-cat {
  background: var(--vp-c-bg-soft);
  color: var(--vp-c-text-2);
  border: 1px solid var(--vp-c-divider);
}
.hub-badge-verified {
  background: var(--vp-c-brand-soft);
  color: var(--vp-c-brand-1);
}
.hub-meta-text {
  font-size: 12px;
  color: var(--vp-c-text-3);
}
.hub-pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 12px;
  margin-top: 16px;
}
.hub-page-info {
  font-size: 13px;
  color: var(--vp-c-text-2);
}
</style>
