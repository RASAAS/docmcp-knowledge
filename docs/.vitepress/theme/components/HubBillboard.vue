<script setup lang="ts">
/**
 * Priority Billboard -- Admin curates items; visitors/users vote + comment.
 */
import { ref, computed, watch, onMounted, nextTick } from "vue";
import { useData } from "vitepress";
import {
  listBillboard,
  createBillboardItem,
  createBillboardFromFeature,
  editBillboardItem,
  deleteBillboardItem,
  toggleBillboardVote,
  listComments,
  createComment,
  listFeatures,
  isLoggedIn,
  getUserRole,
  loadTurnstileScript,
  renderTurnstile,
  type BillboardItem,
  type Comment,
  type Feature,
} from "./HubApi";
import { FEATURE_CATEGORIES, hubLabel } from "./HubNavData";

const props = withDefaults(defineProps<{ category?: string }>(), { category: "" });

const { lang } = useData();
const isZh = computed(() => lang.value === "zh" || lang.value === "zh-CN");
const loggedIn = computed(() => isLoggedIn());
const isAdmin = computed(() => ["admin", "super_admin"].includes(getUserRole()));

const items = ref<BillboardItem[]>([]);
const total = ref(0);
const page = ref(1);
const pages = ref(1);
const loading = ref(false);
const error = ref("");
const sort = ref("votes");

const voteEmail = ref("");

const showAdminForm = ref(false);
const formTitle = ref("");
const formDesc = ref("");
const formCategory = ref("general");
const formStatus = ref("planned");
const formPublished = ref(true);
const submitting = ref(false);

const editingId = ref<number | null>(null);
const editTitle = ref("");
const editDesc = ref("");
const editCategory = ref("general");
const editStatus = ref("planned");
const editPublished = ref(true);

const showImport = ref(false);
const importCandidates = ref<Feature[]>([]);
const importLoading = ref(false);
const importingId = ref<number | null>(null);

const expandedId = ref<number | null>(null);
const comments = ref<Comment[]>([]);
const commentLoading = ref(false);
const commentBody = ref("");
const commentName = ref("");
const commentSubmitting = ref(false);
const commentTurnstileRef = ref<HTMLElement | null>(null);
const commentTurnstileToken = ref("");

const categories = computed(() =>
  FEATURE_CATEGORIES.filter((c) => c.value).map((c) => ({
    value: c.value,
    label: hubLabel(c, isZh.value),
  }))
);

const statusLabels: Record<string, { en: string; zh: string; color: string }> = {
  planned: { en: "Planned", zh: "已规划", color: "#0070f3" },
  in_progress: { en: "In Progress", zh: "开发中", color: "#f5a623" },
  completed: { en: "Completed", zh: "已完成", color: "#0cce6b" },
  deferred: { en: "Deferred", zh: "暂缓", color: "#999" },
};

async function load() {
  loading.value = true;
  error.value = "";
  try {
    const data = await listBillboard({
      category: props.category || undefined,
      sort: sort.value,
      page: page.value,
      include_drafts: isAdmin.value,
    });
    items.value = data.items;
    total.value = data.total;
    pages.value = data.pages;
  } catch (e) {
    error.value = (e as Error).message;
  } finally {
    loading.value = false;
  }
}

watch(
  () => props.category,
  () => {
    page.value = 1;
    expandedId.value = null;
    load();
  }
);

async function vote(item: BillboardItem) {
  try {
    const result = await toggleBillboardVote(item.id, {
      author_email: voteEmail.value || undefined,
    });
    item.user_voted = result.voted;
    const delta = loggedIn.value ? 2 : 1;
    item.vote_count += result.voted ? delta : -delta;
    if (sort.value === "votes") await load();
  } catch (e) {
    error.value = (e as Error).message;
  }
}

async function submitCreate() {
  if (!formTitle.value.trim()) return;
  submitting.value = true;
  error.value = "";
  try {
    await createBillboardItem({
      title: formTitle.value.trim(),
      description: formDesc.value.trim(),
      category: formCategory.value,
      status: formStatus.value,
      is_published: formPublished.value,
    });
    showAdminForm.value = false;
    formTitle.value = "";
    formDesc.value = "";
    await load();
  } catch (e) {
    error.value = (e as Error).message;
  } finally {
    submitting.value = false;
  }
}

function startEdit(item: BillboardItem) {
  editingId.value = item.id;
  editTitle.value = item.title;
  editDesc.value = item.description;
  editCategory.value = item.category;
  editStatus.value = item.status;
  editPublished.value = !!item.is_published;
}

async function saveEdit(item: BillboardItem) {
  if (!editTitle.value.trim()) return;
  try {
    await editBillboardItem(item.id, {
      title: editTitle.value.trim(),
      description: editDesc.value,
      category: editCategory.value,
      status: editStatus.value,
      is_published: editPublished.value,
    });
    editingId.value = null;
    await load();
  } catch (e) {
    error.value = (e as Error).message;
  }
}

async function doDelete(item: BillboardItem) {
  const msg = isZh.value ? "确定从榜单删除此项？" : "Remove this item from the billboard?";
  if (!confirm(msg)) return;
  try {
    await deleteBillboardItem(item.id);
    items.value = items.value.filter((x) => x.id !== item.id);
    total.value = Math.max(0, total.value - 1);
  } catch (e) {
    error.value = (e as Error).message;
  }
}

async function openImport() {
  showImport.value = !showImport.value;
  if (!showImport.value) return;
  importLoading.value = true;
  try {
    const data = await listFeatures({ sort: "votes", page: 1 });
    const onBoard = new Set(
      items.value.map((b) => b.source_feature_id).filter((id): id is number => !!id)
    );
    importCandidates.value = data.items.filter((f) => !onBoard.has(f.id));
  } catch (e) {
    error.value = (e as Error).message;
  } finally {
    importLoading.value = false;
  }
}

async function importFeature(f: Feature) {
  importingId.value = f.id;
  error.value = "";
  try {
    await createBillboardFromFeature(f.id);
    importCandidates.value = importCandidates.value.filter((x) => x.id !== f.id);
    await load();
  } catch (e) {
    error.value = (e as Error).message;
  } finally {
    importingId.value = null;
  }
}

async function initCommentTurnstile() {
  if (isLoggedIn()) return;
  await loadTurnstileScript();
  if (commentTurnstileRef.value) {
    try {
      commentTurnstileToken.value = await renderTurnstile(commentTurnstileRef.value);
    } catch {
      /* validated on submit */
    }
  }
}

async function toggleComments(id: number) {
  if (expandedId.value === id) {
    expandedId.value = null;
    comments.value = [];
    return;
  }
  expandedId.value = id;
  commentLoading.value = true;
  try {
    const data = await listComments("billboard", id);
    comments.value = data.items;
  } catch (e) {
    error.value = (e as Error).message;
  } finally {
    commentLoading.value = false;
    if (!isLoggedIn()) nextTick(() => initCommentTurnstile());
  }
}

async function submitComment() {
  if (!commentBody.value.trim() || expandedId.value === null) return;
  if (!isLoggedIn() && !commentTurnstileToken.value) {
    error.value = isZh.value ? "请完成人机验证" : "Please complete the verification";
    return;
  }
  commentSubmitting.value = true;
  try {
    await createComment({
      target_type: "billboard",
      target_id: expandedId.value,
      body: commentBody.value.trim(),
      author_name: commentName.value.trim() || undefined,
      turnstile_token: isLoggedIn() ? undefined : commentTurnstileToken.value || undefined,
    });
    commentBody.value = "";
    commentTurnstileToken.value = "";
    const data = await listComments("billboard", expandedId.value);
    comments.value = data.items;
    const item = items.value.find((b) => b.id === expandedId.value);
    if (item) item.comment_count++;
    if (!isLoggedIn() && commentTurnstileRef.value) initCommentTurnstile();
  } catch (e) {
    error.value = (e as Error).message;
  } finally {
    commentSubmitting.value = false;
  }
}

function rankClass(rank?: number): string {
  if (rank === 1) return "bb-rank-1";
  if (rank === 2) return "bb-rank-2";
  if (rank === 3) return "bb-rank-3";
  return "";
}

onMounted(load);
</script>

<template>
  <div class="bb">
    <div class="bb-header">
      <div class="bb-header-left">
        <h2 class="bb-title">
          {{ isZh ? "优先级榜单" : "Priority Board" }}
          <span v-if="total" class="bb-count">{{ total }}</span>
        </h2>
        <p class="bb-intro">
          {{ isZh
            ? "由团队整理的计划功能榜单。票数越高，开发优先级越高。访客与用户可投票和留言；仅管理员可维护榜单。"
            : "Admin-curated planned features. Higher votes mean higher priority. Visitors and users can vote and comment; only admins manage the board." }}
        </p>
      </div>
      <div class="bb-header-actions">
        <select v-model="sort" class="bb-select" @change="page = 1; load()">
          <option value="votes">{{ isZh ? "最多投票" : "Most Voted" }}</option>
          <option value="newest">{{ isZh ? "最新" : "Newest" }}</option>
          <option value="updated">{{ isZh ? "最近更新" : "Updated" }}</option>
        </select>
        <template v-if="isAdmin">
          <button class="bb-btn" @click="openImport">
            {{ showImport ? (isZh ? "关闭导入" : "Close Import") : (isZh ? "从建议导入" : "Import Suggestions") }}
          </button>
          <button class="bb-btn bb-btn-primary" @click="showAdminForm = !showAdminForm">
            {{ showAdminForm ? (isZh ? "取消" : "Cancel") : (isZh ? "+ 新建榜单项" : "+ New Item") }}
          </button>
        </template>
      </div>
    </div>

    <div v-if="!loggedIn" class="bb-vote-hint">
      <input
        v-model="voteEmail"
        type="email"
        class="bb-input"
        :placeholder="isZh ? '投票邮箱（访客必填）' : 'Email required for guest votes'"
      />
    </div>

    <!-- Admin create form -->
    <div v-if="isAdmin && showAdminForm" class="bb-form">
      <input v-model="formTitle" class="bb-input bb-input-full" :placeholder="isZh ? '标题 *' : 'Title *'" />
      <textarea v-model="formDesc" class="bb-textarea" rows="3" :placeholder="isZh ? '说明（可选）' : 'Description (optional)'" />
      <div class="bb-form-row">
        <select v-model="formCategory" class="bb-select">
          <option v-for="c in categories" :key="c.value" :value="c.value">{{ c.label }}</option>
        </select>
        <select v-model="formStatus" class="bb-select">
          <option v-for="(s, key) in statusLabels" :key="key" :value="key">{{ isZh ? s.zh : s.en }}</option>
        </select>
        <label class="bb-check">
          <input v-model="formPublished" type="checkbox" />
          {{ isZh ? "立即发布" : "Publish" }}
        </label>
        <button class="bb-btn bb-btn-primary" :disabled="submitting || !formTitle.trim()" @click="submitCreate">
          {{ submitting ? (isZh ? "保存中..." : "Saving...") : (isZh ? "创建" : "Create") }}
        </button>
      </div>
    </div>

    <!-- Import from Feature Board -->
    <div v-if="isAdmin && showImport" class="bb-import">
      <h3 class="bb-import-title">{{ isZh ? "从功能建议导入" : "Import from Feature Board" }}</h3>
      <div v-if="importLoading" class="bb-loading">{{ isZh ? "加载中..." : "Loading..." }}</div>
      <div v-else-if="importCandidates.length === 0" class="bb-empty-sm">
        {{ isZh ? "暂无可导入的建议（或均已在榜）" : "No suggestions to import (or all already listed)" }}
      </div>
      <div v-else class="bb-import-list">
        <div v-for="f in importCandidates" :key="f.id" class="bb-import-row">
          <div class="bb-import-meta">
            <strong>{{ f.title }}</strong>
            <span>{{ f.vote_count }} {{ isZh ? "票" : "votes" }} · {{ f.category }}</span>
          </div>
          <button
            class="bb-btn bb-btn-primary"
            :disabled="importingId === f.id"
            @click="importFeature(f)"
          >
            {{ importingId === f.id ? "..." : (isZh ? "加入榜单" : "Add") }}
          </button>
        </div>
      </div>
    </div>

    <div v-if="error" class="bb-error">{{ error }}</div>

    <div v-if="loading" class="bb-loading">
      <div class="bb-spinner" />
      {{ isZh ? "加载中..." : "Loading..." }}
    </div>

    <div v-else class="bb-list">
      <div v-if="items.length === 0" class="bb-empty">
        <p>{{ isZh ? "榜单暂无条目。管理员可从功能建议导入或手动创建。" : "No billboard items yet. Admins can import suggestions or create items." }}</p>
      </div>

      <article v-for="item in items" :key="item.id" class="bb-card" :class="{ 'bb-draft': !item.is_published }">
        <div class="bb-rank" :class="rankClass(item.rank)">#{{ item.rank }}</div>
        <button class="bb-vote" :class="{ voted: item.user_voted }" @click="vote(item)">
          <svg width="14" height="14" viewBox="0 0 16 16" fill="currentColor"><path d="M8 4l4 5H4l4-5z"/></svg>
          <span>{{ item.vote_count }}</span>
        </button>
        <div class="bb-body">
          <template v-if="editingId === item.id">
            <input v-model="editTitle" class="bb-input bb-input-full" />
            <textarea v-model="editDesc" class="bb-textarea" rows="2" />
            <div class="bb-form-row">
              <select v-model="editCategory" class="bb-select">
                <option v-for="c in categories" :key="c.value" :value="c.value">{{ c.label }}</option>
              </select>
              <select v-model="editStatus" class="bb-select">
                <option v-for="(s, key) in statusLabels" :key="key" :value="key">{{ isZh ? s.zh : s.en }}</option>
              </select>
              <label class="bb-check">
                <input v-model="editPublished" type="checkbox" />
                {{ isZh ? "已发布" : "Published" }}
              </label>
              <button class="bb-btn bb-btn-primary" @click="saveEdit(item)">{{ isZh ? "保存" : "Save" }}</button>
              <button class="bb-btn" @click="editingId = null">{{ isZh ? "取消" : "Cancel" }}</button>
            </div>
          </template>
          <template v-else>
            <div class="bb-card-top">
              <h3 class="bb-card-title">{{ item.title }}</h3>
              <span
                v-if="statusLabels[item.status]"
                class="bb-status"
                :style="{ '--st': statusLabels[item.status].color }"
              >
                {{ isZh ? statusLabels[item.status].zh : statusLabels[item.status].en }}
              </span>
              <span v-if="!item.is_published" class="bb-draft-tag">{{ isZh ? "草稿" : "Draft" }}</span>
            </div>
            <p v-if="item.description" class="bb-card-desc">{{ item.description }}</p>
            <div class="bb-card-footer">
              <span class="bb-tag">{{ item.category.replace(/_/g, " ") }}</span>
              <span v-if="item.source_feature_id" class="bb-tag bb-tag-src">
                {{ isZh ? `来自建议 #${item.source_feature_id}` : `From suggestion #${item.source_feature_id}` }}
              </span>
              <button class="bb-link" @click="toggleComments(item.id)">
                {{ item.comment_count }} {{ isZh ? "条留言" : "comments" }}
              </button>
              <span v-if="isAdmin" class="bb-admin-actions">
                <button class="bb-link" @click="startEdit(item)">{{ isZh ? "编辑" : "Edit" }}</button>
                <button class="bb-link bb-danger" @click="doDelete(item)">{{ isZh ? "删除" : "Delete" }}</button>
              </span>
            </div>
          </template>

          <div v-if="expandedId === item.id" class="bb-comments">
            <div v-if="commentLoading" class="bb-loading">{{ isZh ? "加载留言..." : "Loading comments..." }}</div>
            <div v-else>
              <div v-for="c in comments" :key="c.id" class="bb-cmt">
                <strong>{{ c.author_name }}</strong>
                <span>{{ c.body }}</span>
              </div>
              <div v-if="comments.length === 0" class="bb-empty-sm">{{ isZh ? "暂无留言" : "No comments yet" }}</div>
            </div>
            <div class="bb-cmt-form">
              <input
                v-if="!loggedIn"
                v-model="commentName"
                class="bb-input"
                :placeholder="isZh ? '您的姓名 *' : 'Your name *'"
              />
              <textarea
                v-model="commentBody"
                class="bb-textarea"
                rows="2"
                :placeholder="isZh ? '写下你的看法...' : 'Share your thoughts...'"
              />
              <div v-if="!loggedIn" ref="commentTurnstileRef" class="bb-turnstile" />
              <button
                class="bb-btn bb-btn-primary"
                :disabled="commentSubmitting || !commentBody.trim()"
                @click="submitComment"
              >
                {{ commentSubmitting ? (isZh ? "发送中..." : "Posting...") : (isZh ? "留言" : "Comment") }}
              </button>
            </div>
          </div>
        </div>
      </article>
    </div>

    <div v-if="pages > 1" class="bb-pagination">
      <button class="bb-btn" :disabled="page <= 1" @click="page--; load()">{{ isZh ? "上一页" : "Prev" }}</button>
      <span>{{ page }} / {{ pages }}</span>
      <button class="bb-btn" :disabled="page >= pages" @click="page++; load()">{{ isZh ? "下一页" : "Next" }}</button>
    </div>
  </div>
</template>

<style scoped>
.bb-header {
  display: flex;
  justify-content: space-between;
  gap: 16px;
  flex-wrap: wrap;
  margin-bottom: 16px;
}
.bb-title {
  display: flex;
  align-items: center;
  gap: 10px;
  margin: 0 0 6px;
  font-size: 20px;
  font-weight: 650;
  color: var(--vp-c-text-1);
}
.bb-count {
  min-width: 24px;
  height: 24px;
  padding: 0 8px;
  border-radius: 12px;
  background: var(--vp-c-bg-soft);
  color: var(--vp-c-text-2);
  font-size: 13px;
  font-weight: 500;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.bb-intro {
  margin: 0;
  max-width: 44rem;
  font-size: 13px;
  line-height: 1.5;
  color: var(--vp-c-text-2);
}
.bb-header-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  align-items: flex-start;
}
.bb-vote-hint {
  margin-bottom: 12px;
  max-width: 320px;
}
.bb-form,
.bb-import {
  margin-bottom: 16px;
  padding: 14px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 10px;
  background: var(--vp-c-bg-soft);
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.bb-form-row {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  align-items: center;
}
.bb-import-title {
  margin: 0;
  font-size: 14px;
  font-weight: 600;
}
.bb-import-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.bb-import-row {
  display: flex;
  justify-content: space-between;
  gap: 12px;
  align-items: center;
  padding: 8px 10px;
  border-radius: 8px;
  background: var(--vp-c-bg);
}
.bb-import-meta {
  display: flex;
  flex-direction: column;
  gap: 2px;
  min-width: 0;
  font-size: 13px;
}
.bb-import-meta span {
  color: var(--vp-c-text-3);
  font-size: 12px;
}
.bb-input,
.bb-textarea,
.bb-select {
  padding: 7px 10px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 7px;
  background: var(--vp-c-bg);
  color: var(--vp-c-text-1);
  font-size: 13px;
}
.bb-input-full,
.bb-textarea {
  width: 100%;
  box-sizing: border-box;
}
.bb-btn {
  padding: 7px 12px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  background: var(--vp-c-bg);
  color: var(--vp-c-text-1);
  font-size: 13px;
  font-weight: 500;
  cursor: pointer;
}
.bb-btn-primary {
  border-color: transparent;
  background: var(--vp-c-brand-1);
  color: #fff;
}
.bb-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
.bb-check {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 13px;
  color: var(--vp-c-text-2);
}
.bb-error {
  color: var(--vp-c-danger-1);
  font-size: 13px;
  margin-bottom: 12px;
}
.bb-loading,
.bb-empty,
.bb-empty-sm {
  color: var(--vp-c-text-3);
  font-size: 14px;
  padding: 12px 0;
}
.bb-spinner {
  width: 18px;
  height: 18px;
  border: 2px solid var(--vp-c-divider);
  border-top-color: var(--vp-c-brand-1);
  border-radius: 50%;
  display: inline-block;
  animation: bbspin 0.7s linear infinite;
  margin-right: 8px;
  vertical-align: middle;
}
@keyframes bbspin { to { transform: rotate(360deg); } }

.bb-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.bb-card {
  display: flex;
  gap: 12px;
  padding: 14px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 12px;
  background: var(--vp-c-bg);
}
.bb-card.bb-draft {
  opacity: 0.72;
  border-style: dashed;
}
.bb-rank {
  flex-shrink: 0;
  width: 42px;
  height: 42px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 750;
  font-size: 14px;
  color: var(--vp-c-text-2);
  background: var(--vp-c-bg-soft);
}
.bb-rank-1 { background: rgba(245, 166, 35, 0.18); color: #c47d00; }
.bb-rank-2 { background: rgba(148, 163, 184, 0.22); color: #64748b; }
.bb-rank-3 { background: rgba(180, 120, 80, 0.18); color: #9a6a3a; }
.bb-vote {
  flex-shrink: 0;
  width: 48px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 2px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 10px;
  background: var(--vp-c-bg-soft);
  color: var(--vp-c-text-2);
  cursor: pointer;
  font-weight: 650;
  font-size: 13px;
  padding: 6px 0;
}
.bb-vote.voted {
  border-color: var(--vp-c-brand-1);
  color: var(--vp-c-brand-1);
  background: var(--vp-c-brand-soft);
}
.bb-body { flex: 1; min-width: 0; }
.bb-card-top {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
}
.bb-card-title {
  margin: 0;
  font-size: 16px;
  font-weight: 650;
  color: var(--vp-c-text-1);
}
.bb-status {
  font-size: 11px;
  font-weight: 600;
  padding: 2px 8px;
  border-radius: 999px;
  color: var(--st);
  background: color-mix(in srgb, var(--st) 14%, transparent);
}
.bb-draft-tag {
  font-size: 11px;
  padding: 2px 8px;
  border-radius: 999px;
  background: var(--vp-c-bg-soft);
  color: var(--vp-c-text-3);
}
.bb-card-desc {
  margin: 6px 0 0;
  font-size: 13px;
  line-height: 1.5;
  color: var(--vp-c-text-2);
}
.bb-card-footer {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  align-items: center;
  margin-top: 10px;
  font-size: 12px;
}
.bb-tag {
  padding: 2px 8px;
  border-radius: 999px;
  background: var(--vp-c-bg-soft);
  color: var(--vp-c-text-3);
}
.bb-tag-src { color: var(--vp-c-brand-1); }
.bb-link {
  border: none;
  background: none;
  color: var(--vp-c-brand-1);
  cursor: pointer;
  font-size: 12px;
  padding: 0;
}
.bb-danger { color: var(--vp-c-danger-1); }
.bb-admin-actions {
  display: inline-flex;
  gap: 10px;
  margin-left: auto;
}
.bb-comments {
  margin-top: 12px;
  padding-top: 12px;
  border-top: 1px solid var(--vp-c-divider);
}
.bb-cmt {
  display: flex;
  flex-direction: column;
  gap: 2px;
  padding: 6px 0;
  font-size: 13px;
  color: var(--vp-c-text-2);
}
.bb-cmt strong { color: var(--vp-c-text-1); font-size: 12px; }
.bb-cmt-form {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin-top: 8px;
}
.bb-turnstile { min-height: 20px; }
.bb-pagination {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-top: 16px;
  font-size: 13px;
  color: var(--vp-c-text-2);
}
</style>
