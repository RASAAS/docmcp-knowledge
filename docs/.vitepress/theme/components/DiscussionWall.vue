<script setup lang="ts">
import { ref, onMounted, computed } from "vue";
import {
  listDiscussions,
  createDiscussion,
  toggleLike,
  listComments,
  createComment,
  isLoggedIn,
  type Discussion,
  type Comment,
} from "./HubApi";

const discussions = ref<Discussion[]>([]);
const total = ref(0);
const page = ref(1);
const pages = ref(1);
const loading = ref(false);
const error = ref("");

const category = ref("");
const sort = ref("latest");

const showForm = ref(false);
const formTitle = ref("");
const formBody = ref("");
const formCategory = ref("general");
const formName = ref("");
const submitting = ref(false);

const expandedId = ref<number | null>(null);
const comments = ref<Comment[]>([]);
const commentLoading = ref(false);
const commentBody = ref("");
const commentName = ref("");
const commentSubmitting = ref(false);

const categories = [
  { value: "", label: "All" },
  { value: "regulatory_intelligence", label: "Regulatory Intel" },
  { value: "best_practices", label: "Best Practices" },
  { value: "tool_tips", label: "Tool Tips" },
  { value: "general", label: "General" },
];

const loggedIn = computed(() => isLoggedIn());

async function load() {
  loading.value = true;
  error.value = "";
  try {
    const data = await listDiscussions({
      category: category.value || undefined,
      sort: sort.value,
      page: page.value,
    });
    discussions.value = data.items;
    total.value = data.total;
    pages.value = data.pages;
  } catch (e) {
    error.value = (e as Error).message;
  } finally {
    loading.value = false;
  }
}

async function like(d: Discussion) {
  try {
    const result = await toggleLike(d.id);
    d.user_liked = result.liked;
    d.like_count += result.liked ? 1 : -1;
  } catch (e) {
    error.value = (e as Error).message;
  }
}

async function submit() {
  if (!formTitle.value.trim() || !formBody.value.trim()) return;
  submitting.value = true;
  error.value = "";
  try {
    await createDiscussion({
      title: formTitle.value.trim(),
      body: formBody.value.trim(),
      category: formCategory.value,
      author_name: formName.value.trim() || undefined,
    });
    showForm.value = false;
    formTitle.value = "";
    formBody.value = "";
    formName.value = "";
    page.value = 1;
    sort.value = "latest";
    await load();
  } catch (e) {
    error.value = (e as Error).message;
  } finally {
    submitting.value = false;
  }
}

async function toggleComments(discId: number) {
  if (expandedId.value === discId) {
    expandedId.value = null;
    comments.value = [];
    return;
  }
  expandedId.value = discId;
  commentLoading.value = true;
  try {
    const data = await listComments("discussion", discId);
    comments.value = data.items;
  } catch (e) {
    error.value = (e as Error).message;
  } finally {
    commentLoading.value = false;
  }
}

async function submitComment() {
  if (!commentBody.value.trim() || expandedId.value === null) return;
  commentSubmitting.value = true;
  try {
    await createComment({
      target_type: "discussion",
      target_id: expandedId.value,
      body: commentBody.value.trim(),
      author_name: commentName.value.trim() || undefined,
    });
    commentBody.value = "";
    const data = await listComments("discussion", expandedId.value);
    comments.value = data.items;
    const disc = discussions.value.find((d) => d.id === expandedId.value);
    if (disc) disc.comment_count++;
  } catch (e) {
    error.value = (e as Error).message;
  } finally {
    commentSubmitting.value = false;
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
  <div class="hub-discussion-wall">
    <!-- Toolbar -->
    <div class="hub-toolbar">
      <div class="hub-filters">
        <select v-model="category" @change="page = 1; load()">
          <option v-for="c in categories" :key="c.value" :value="c.value">
            {{ c.label }}
          </option>
        </select>
        <select v-model="sort" @change="page = 1; load()">
          <option value="latest">Latest</option>
          <option value="likes">Most Liked</option>
        </select>
      </div>
      <button class="hub-btn hub-btn-primary" @click="showForm = !showForm">
        {{ showForm ? "Cancel" : "+ New Discussion" }}
      </button>
    </div>

    <!-- Submit Form -->
    <div v-if="showForm" class="hub-form">
      <div v-if="!loggedIn" class="hub-form-guest">
        <input v-model="formName" placeholder="Your name *" class="hub-input" />
      </div>
      <input
        v-model="formTitle"
        placeholder="Discussion title *"
        class="hub-input hub-input-full"
      />
      <textarea
        v-model="formBody"
        placeholder="Share your thoughts..."
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
          :disabled="submitting || !formTitle.trim() || !formBody.trim()"
          @click="submit"
        >
          {{ submitting ? "Posting..." : "Post" }}
        </button>
      </div>
    </div>

    <!-- Error -->
    <div v-if="error" class="hub-error">{{ error }}</div>

    <!-- Loading -->
    <div v-if="loading" class="hub-loading">Loading...</div>

    <!-- Discussion List -->
    <div v-else class="hub-list">
      <div v-if="discussions.length === 0" class="hub-empty">
        No discussions yet. Start one!
      </div>
      <div v-for="d in discussions" :key="d.id" class="hub-disc-card">
        <div class="hub-disc-main">
          <div class="hub-disc-header">
            <h3 class="hub-disc-title">{{ d.title }}</h3>
            <span v-if="d.is_verified" class="hub-badge hub-badge-verified">Verified</span>
          </div>
          <p class="hub-disc-body">{{ d.body }}</p>
          <div class="hub-disc-meta">
            <span class="hub-badge hub-badge-cat">{{ d.category }}</span>
            <span class="hub-meta-text">{{ d.author_name }}</span>
            <span class="hub-meta-text">{{ timeAgo(d.created_at) }}</span>
            <button
              class="hub-action-btn"
              :class="{ active: d.user_liked }"
              @click="like(d)"
            >
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/>
              </svg>
              {{ d.like_count }}
            </button>
            <button
              class="hub-action-btn"
              :class="{ active: expandedId === d.id }"
              @click="toggleComments(d.id)"
            >
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
              </svg>
              {{ d.comment_count }}
            </button>
          </div>
        </div>

        <!-- Comments Section -->
        <div v-if="expandedId === d.id" class="hub-comments">
          <div v-if="commentLoading" class="hub-loading-sm">Loading comments...</div>
          <div v-else>
            <div v-if="comments.length === 0" class="hub-comments-empty">
              No comments yet.
            </div>
            <div v-for="c in comments" :key="c.id" class="hub-comment">
              <div class="hub-comment-header">
                <span class="hub-comment-author">{{ c.author_name }}</span>
                <span v-if="c.is_verified" class="hub-badge hub-badge-verified-sm">V</span>
                <span class="hub-comment-time">{{ timeAgo(c.created_at) }}</span>
              </div>
              <p class="hub-comment-body">{{ c.body }}</p>
            </div>
          </div>
          <div class="hub-comment-form">
            <input
              v-if="!loggedIn"
              v-model="commentName"
              placeholder="Your name"
              class="hub-input hub-input-sm"
            />
            <div class="hub-comment-input-row">
              <input
                v-model="commentBody"
                placeholder="Add a comment..."
                class="hub-input"
                @keydown.enter="submitComment"
              />
              <button
                class="hub-btn hub-btn-sm"
                :disabled="commentSubmitting || !commentBody.trim()"
                @click="submitComment"
              >
                {{ commentSubmitting ? "..." : "Post" }}
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Pagination -->
    <div v-if="pages > 1" class="hub-pagination">
      <button :disabled="page <= 1" @click="page--; load()" class="hub-btn hub-btn-sm">Prev</button>
      <span class="hub-page-info">Page {{ page }} / {{ pages }}</span>
      <button :disabled="page >= pages" @click="page++; load()" class="hub-btn hub-btn-sm">Next</button>
    </div>
  </div>
</template>

<style scoped>
.hub-discussion-wall {
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
.hub-btn:hover { border-color: var(--vp-c-brand-1); }
.hub-btn:disabled { opacity: 0.5; cursor: not-allowed; }
.hub-btn-primary {
  background: var(--vp-c-brand-1);
  color: white;
  border-color: var(--vp-c-brand-1);
}
.hub-btn-primary:hover { background: var(--vp-c-brand-2); }
.hub-btn-sm { padding: 4px 10px; font-size: 13px; }
.hub-form {
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  padding: 16px;
  margin-bottom: 16px;
  background: var(--vp-c-bg-soft);
}
.hub-form-guest { display: flex; gap: 8px; margin-bottom: 8px; }
.hub-input {
  padding: 8px 12px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 6px;
  font-size: 14px;
  background: var(--vp-c-bg);
  color: var(--vp-c-text-1);
  width: 100%;
}
.hub-input-full { width: 100%; margin-bottom: 8px; }
.hub-input-sm { width: 200px; margin-bottom: 8px; }
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
.hub-loading { text-align: center; padding: 32px; color: var(--vp-c-text-2); }
.hub-loading-sm { text-align: center; padding: 12px; color: var(--vp-c-text-3); font-size: 13px; }
.hub-empty {
  text-align: center;
  padding: 48px 16px;
  color: var(--vp-c-text-3);
  font-size: 15px;
}
.hub-list { display: flex; flex-direction: column; gap: 8px; }
.hub-disc-card {
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  background: var(--vp-c-bg);
  overflow: hidden;
  transition: border-color 0.15s;
}
.hub-disc-card:hover { border-color: var(--vp-c-brand-1); }
.hub-disc-main { padding: 14px 16px; }
.hub-disc-header {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 4px;
}
.hub-disc-title {
  font-size: 15px;
  font-weight: 600;
  margin: 0;
  color: var(--vp-c-text-1);
}
.hub-disc-body {
  font-size: 13px;
  color: var(--vp-c-text-2);
  margin: 4px 0 8px;
  line-height: 1.5;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.hub-disc-meta {
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
.hub-badge-verified-sm {
  background: var(--vp-c-brand-soft);
  color: var(--vp-c-brand-1);
  font-size: 10px;
  padding: 0 4px;
  border-radius: 3px;
}
.hub-meta-text { font-size: 12px; color: var(--vp-c-text-3); }
.hub-action-btn {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 2px 8px;
  border: 1px solid transparent;
  border-radius: 4px;
  background: none;
  color: var(--vp-c-text-3);
  cursor: pointer;
  font-size: 12px;
  transition: all 0.15s;
}
.hub-action-btn:hover { color: var(--vp-c-brand-1); }
.hub-action-btn.active { color: var(--vp-c-brand-1); }
.hub-comments {
  border-top: 1px solid var(--vp-c-divider);
  padding: 12px 16px;
  background: var(--vp-c-bg-soft);
}
.hub-comments-empty {
  text-align: center;
  padding: 12px;
  color: var(--vp-c-text-3);
  font-size: 13px;
}
.hub-comment {
  padding: 8px 0;
  border-bottom: 1px solid var(--vp-c-divider);
}
.hub-comment:last-of-type { border-bottom: none; }
.hub-comment-header {
  display: flex;
  align-items: center;
  gap: 6px;
  margin-bottom: 4px;
}
.hub-comment-author {
  font-size: 13px;
  font-weight: 600;
  color: var(--vp-c-text-1);
}
.hub-comment-time { font-size: 11px; color: var(--vp-c-text-3); }
.hub-comment-body {
  font-size: 13px;
  color: var(--vp-c-text-2);
  margin: 0;
  line-height: 1.5;
}
.hub-comment-form {
  margin-top: 12px;
}
.hub-comment-input-row {
  display: flex;
  gap: 8px;
}
.hub-pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 12px;
  margin-top: 16px;
}
.hub-page-info { font-size: 13px; color: var(--vp-c-text-2); }
</style>
