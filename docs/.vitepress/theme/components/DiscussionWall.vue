<script setup lang="ts">
import { ref, onMounted, computed, nextTick } from "vue";
import { useData } from "vitepress";
import {
  listDiscussions,
  createDiscussion,
  editDiscussion,
  deleteDiscussion,
  toggleLike,
  listComments,
  createComment,
  editComment,
  deleteComment,
  isLoggedIn,
  getUserId,
  getUserRole,
  loadTurnstileScript,
  renderTurnstile,
  type Discussion,
  type Comment,
} from "./HubApi";

const { lang } = useData();
const isZh = computed(() => lang.value === "zh" || lang.value === "zh-CN");
const EDIT_WINDOW_MS = 30 * 60 * 1000;

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

const turnstileRef = ref<HTMLElement | null>(null);
const turnstileToken = ref("");
const commentTurnstileRef = ref<HTMLElement | null>(null);
const commentTurnstileToken = ref("");

const currentUserId = computed(() => getUserId());
const isAdminUser = computed(() => ["admin", "super_admin"].includes(getUserRole()));

const editDiscId = ref<number | null>(null);
const editDiscTitle = ref("");
const editDiscBody = ref("");

const editCommentId = ref<number | null>(null);
const editCommentBody = ref("");

function canEditDisc(d: Discussion): boolean {
  if (isAdminUser.value) return true;
  if (!isLoggedIn() || !currentUserId.value) return false;
  if ((d as Record<string, unknown>).author_user_id !== currentUserId.value) return false;
  const created = new Date(d.created_at + "Z").getTime();
  return Date.now() - created < EDIT_WINDOW_MS;
}
function canDeleteDisc(d: Discussion): boolean {
  if (isAdminUser.value) return true;
  if (!isLoggedIn() || !currentUserId.value) return false;
  return (d as Record<string, unknown>).author_user_id === currentUserId.value;
}
function canEditCmt(c: Comment): boolean {
  if (isAdminUser.value) return true;
  if (!isLoggedIn() || !currentUserId.value) return false;
  if ((c as Record<string, unknown>).author_user_id !== currentUserId.value) return false;
  const created = new Date(c.created_at + "Z").getTime();
  return Date.now() - created < EDIT_WINDOW_MS;
}
function canDeleteCmt(c: Comment): boolean {
  if (isAdminUser.value) return true;
  if (!isLoggedIn() || !currentUserId.value) return false;
  return (c as Record<string, unknown>).author_user_id === currentUserId.value;
}

function startEditDisc(d: Discussion) {
  editDiscId.value = d.id; editDiscTitle.value = d.title; editDiscBody.value = d.body;
}
async function saveEditDisc(d: Discussion) {
  if (!editDiscTitle.value.trim() || !editDiscBody.value.trim()) return;
  try {
    await editDiscussion(d.id, { title: editDiscTitle.value.trim(), body: editDiscBody.value.trim() });
    d.title = editDiscTitle.value.trim(); d.body = editDiscBody.value.trim();
    editDiscId.value = null;
  } catch (e) { error.value = (e as Error).message; }
}
async function doDeleteDisc(d: Discussion) {
  const msg = isZh.value ? "确定删除此讨论？" : "Delete this discussion?";
  if (!confirm(msg)) return;
  try {
    await deleteDiscussion(d.id);
    discussions.value = discussions.value.filter((x) => x.id !== d.id);
    if (expandedId.value === d.id) expandedId.value = null;
  } catch (e) { error.value = (e as Error).message; }
}

function startEditCmt(c: Comment) {
  editCommentId.value = c.id; editCommentBody.value = c.body;
}
async function saveEditCmt(c: Comment) {
  if (!editCommentBody.value.trim()) return;
  try {
    await editComment(c.id, { body: editCommentBody.value.trim() });
    c.body = editCommentBody.value.trim();
    editCommentId.value = null;
  } catch (e) { error.value = (e as Error).message; }
}
async function doDeleteCmt(c: Comment) {
  const msg = isZh.value ? "确定删除此评论？" : "Delete this comment?";
  if (!confirm(msg)) return;
  try {
    await deleteComment(c.id);
    comments.value = comments.value.filter((x) => x.id !== c.id);
    if (expandedId.value) {
      const disc = discussions.value.find((d) => d.id === expandedId.value);
      if (disc) disc.comment_count = Math.max(0, disc.comment_count - 1);
    }
  } catch (e) { error.value = (e as Error).message; }
}

const channels = computed(() => [
  {
    value: "",
    label: isZh.value ? "# 全部频道" : "# all-channels",
    desc: isZh.value ? "查看所有讨论" : "View all discussions",
    icon: "M4 6h16M4 12h16M4 18h16",
  },
  {
    value: "regulatory_intelligence",
    label: isZh.value ? "# 法规情报" : "# regulatory-intel",
    desc: isZh.value ? "法规动态和政策解读" : "Updates and policy analysis",
    icon: "M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253",
  },
  {
    value: "best_practices",
    label: isZh.value ? "# 最佳实践" : "# best-practices",
    desc: isZh.value ? "合规经验分享和方法论" : "Compliance tips and methodology",
    icon: "M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z",
  },
  {
    value: "tool_tips",
    label: isZh.value ? "# 工具技巧" : "# tool-tips",
    desc: isZh.value ? "Reguverse 使用技巧" : "Reguverse usage tips",
    icon: "M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.066 2.573c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.573 1.066c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.066-2.573c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z",
  },
  {
    value: "general",
    label: isZh.value ? "# 综合讨论" : "# general",
    desc: isZh.value ? "自由话题" : "Open discussion",
    icon: "M17 8h2a2 2 0 012 2v6a2 2 0 01-2 2h-2v4l-4-4H9a1.994 1.994 0 01-1.414-.586m0 0L11 14h4a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2v4l.586-.586z",
  },
]);

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

async function initTurnstile() {
  if (isLoggedIn()) return;
  await loadTurnstileScript();
  if (turnstileRef.value) {
    try { turnstileToken.value = await renderTurnstile(turnstileRef.value); } catch { /* validated on submit */ }
  }
}

async function initCommentTurnstile() {
  if (isLoggedIn()) return;
  await loadTurnstileScript();
  if (commentTurnstileRef.value) {
    try { commentTurnstileToken.value = await renderTurnstile(commentTurnstileRef.value); } catch { /* validated on submit */ }
  }
}

async function submit() {
  if (!formTitle.value.trim() || !formBody.value.trim()) return;
  if (!isLoggedIn() && !turnstileToken.value) {
    error.value = isZh.value ? "请完成人机验证" : "Please complete the verification";
    return;
  }
  submitting.value = true;
  error.value = "";
  try {
    await createDiscussion({
      title: formTitle.value.trim(),
      body: formBody.value.trim(),
      category: formCategory.value,
      author_name: formName.value.trim() || undefined,
      turnstile_token: isLoggedIn() ? undefined : turnstileToken.value || undefined,
    });
    showForm.value = false;
    formTitle.value = "";
    formBody.value = "";
    formName.value = "";
    turnstileToken.value = "";
    page.value = 1;
    sort.value = "latest";
    await load();
  } catch (e) {
    error.value = (e as Error).message;
    turnstileToken.value = "";
    if (!isLoggedIn() && turnstileRef.value) initTurnstile();
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
      target_type: "discussion",
      target_id: expandedId.value,
      body: commentBody.value.trim(),
      author_name: commentName.value.trim() || undefined,
      turnstile_token: isLoggedIn() ? undefined : commentTurnstileToken.value || undefined,
    });
    commentBody.value = "";
    commentTurnstileToken.value = "";
    const data = await listComments("discussion", expandedId.value);
    comments.value = data.items;
    const disc = discussions.value.find((d) => d.id === expandedId.value);
    if (disc) disc.comment_count++;
    if (!isLoggedIn() && commentTurnstileRef.value) initCommentTurnstile();
  } catch (e) {
    error.value = (e as Error).message;
    commentTurnstileToken.value = "";
    if (!isLoggedIn() && commentTurnstileRef.value) initCommentTurnstile();
  } finally {
    commentSubmitting.value = false;
  }
}

function selectChannel(ch: string) {
  category.value = ch;
  page.value = 1;
  expandedId.value = null;
  load();
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
  <div class="dw">
    <div class="dw-layout">
      <!-- Channel Sidebar -->
      <aside class="dw-sidebar">
        <div class="dw-sidebar-header">
          <h3 class="dw-sidebar-title">{{ isZh ? "频道" : "Channels" }}</h3>
        </div>
        <nav class="dw-channel-list">
          <button
            v-for="ch in channels"
            :key="ch.value"
            class="dw-channel"
            :class="{ active: category === ch.value }"
            @click="selectChannel(ch.value)"
          >
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
              <path :d="ch.icon"/>
            </svg>
            <div class="dw-channel-text">
              <span class="dw-channel-name">{{ ch.label }}</span>
              <span class="dw-channel-desc">{{ ch.desc }}</span>
            </div>
          </button>
        </nav>
        <div class="dw-sidebar-footer">
          <div class="dw-sort-label">{{ isZh ? "排序" : "Sort" }}</div>
          <select v-model="sort" @change="page = 1; load()" class="dw-sort-select">
            <option value="latest">{{ isZh ? "最新" : "Latest" }}</option>
            <option value="likes">{{ isZh ? "最多点赞" : "Most Liked" }}</option>
          </select>
        </div>
      </aside>

      <!-- Main Content -->
      <div class="dw-main">
        <!-- Channel Header -->
        <div class="dw-main-header">
          <div class="dw-main-header-left">
            <h2 class="dw-main-title">
              {{ channels.find(c => c.value === category)?.label || (isZh ? "# 全部频道" : "# all-channels") }}
            </h2>
            <span class="dw-disc-count" v-if="total">{{ total }} {{ isZh ? "条讨论" : "discussions" }}</span>
          </div>
          <button class="dw-btn dw-btn-primary" @click="showForm = !showForm; if (!showForm) { turnstileToken = ''; } else { $nextTick(() => initTurnstile()); }">
            {{ showForm ? (isZh ? "取消" : "Cancel") : (isZh ? "+ 发起讨论" : "+ New Discussion") }}
          </button>
        </div>

        <!-- New Discussion Form -->
        <div v-if="showForm" class="dw-form">
          <div v-if="!loggedIn" class="dw-form-row">
            <input v-model="formName" :placeholder="isZh ? '您的姓名 *' : 'Your name *'" class="dw-input" />
          </div>
          <input v-model="formTitle" :placeholder="isZh ? '讨论标题 *' : 'Discussion title *'" class="dw-input dw-input-full" />
          <textarea v-model="formBody" :placeholder="isZh ? '分享您的想法...' : 'Share your thoughts...'" class="dw-textarea" rows="4"></textarea>
          <div v-if="!loggedIn" ref="turnstileRef" class="dw-turnstile"></div>
          <div class="dw-form-footer">
            <select v-model="formCategory" class="dw-sort-select">
              <option v-for="c in channels.slice(1)" :key="c.value" :value="c.value">{{ c.label }}</option>
            </select>
            <button
              class="dw-btn dw-btn-primary"
              :disabled="submitting || !formTitle.trim() || !formBody.trim() || (!loggedIn && !turnstileToken)"
              @click="submit"
            >
              {{ submitting ? (isZh ? "发布中..." : "Posting...") : (isZh ? "发布" : "Post") }}
            </button>
          </div>
        </div>

        <!-- Error -->
        <div v-if="error" class="dw-error">{{ error }}</div>

        <!-- Loading -->
        <div v-if="loading" class="dw-loading">
          <div class="dw-spinner"></div>
          {{ isZh ? "加载中..." : "Loading..." }}
        </div>

        <!-- Discussion List -->
        <div v-else class="dw-thread-list">
          <div v-if="discussions.length === 0" class="dw-empty">
            <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="var(--vp-c-text-3)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
              <path d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/>
            </svg>
            <p>{{ isZh ? "暂无讨论。发起第一个话题吧！" : "No discussions yet. Start one!" }}</p>
          </div>

          <div v-for="d in discussions" :key="d.id" class="dw-thread">
            <div class="dw-thread-main">
              <div class="dw-thread-avatar">
                {{ d.author_name ? d.author_name.charAt(0).toUpperCase() : "?" }}
              </div>
              <div class="dw-thread-content">
                <div class="dw-thread-header">
                  <span class="dw-thread-author">{{ d.author_name }}</span>
                  <span v-if="d.is_verified" class="dw-badge-verified" title="Verified Reguverse user">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="var(--vp-c-brand-1)"><path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                  </span>
                  <span class="dw-thread-tag">{{ d.category.replace(/_/g, " ") }}</span>
                  <span class="dw-thread-time">{{ timeAgo(d.created_at) }}</span>
                </div>
                <!-- Edit mode -->
                <template v-if="editDiscId === d.id">
                  <input v-model="editDiscTitle" class="dw-edit-input" :placeholder="isZh ? '标题' : 'Title'" />
                  <textarea v-model="editDiscBody" class="dw-edit-textarea" rows="3" :placeholder="isZh ? '内容' : 'Content'"></textarea>
                  <div class="dw-edit-actions">
                    <button class="dw-btn-sm dw-btn-save" @click="saveEditDisc(d)">{{ isZh ? '保存' : 'Save' }}</button>
                    <button class="dw-btn-sm dw-btn-cancel" @click="editDiscId = null">{{ isZh ? '取消' : 'Cancel' }}</button>
                  </div>
                </template>
                <!-- View mode -->
                <template v-else>
                  <h4 class="dw-thread-title">{{ d.title }}</h4>
                  <p class="dw-thread-body">{{ d.body }}</p>
                  <div class="dw-thread-actions">
                    <button class="dw-action" :class="{ active: d.user_liked }" @click="like(d)">
                      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M14 9V5a3 3 0 00-3-3l-4 9v11h11.28a2 2 0 002-1.7l1.38-9a2 2 0 00-2-2.3zM7 22H4a2 2 0 01-2-2v-7a2 2 0 012-2h3"/>
                      </svg>
                      {{ d.like_count }}
                    </button>
                    <button class="dw-action" :class="{ active: expandedId === d.id }" @click="toggleComments(d.id)">
                      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z"/>
                      </svg>
                      {{ d.comment_count }} {{ isZh ? "回复" : "replies" }}
                    </button>
                    <span v-if="canEditDisc(d) || canDeleteDisc(d)" class="dw-owner-actions">
                      <button v-if="canEditDisc(d)" class="dw-btn-icon" :title="isZh ? '编辑' : 'Edit'" @click.stop="startEditDisc(d)">
                        <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 4H4a2 2 0 00-2 2v14a2 2 0 002 2h14a2 2 0 002-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 013 3L12 15l-4 1 1-4 9.5-9.5z"/></svg>
                      </button>
                      <button v-if="canDeleteDisc(d)" class="dw-btn-icon dw-btn-danger" :title="isZh ? '删除' : 'Delete'" @click.stop="doDeleteDisc(d)">
                        <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="3 6 5 6 21 6"/><path d="M19 6v14a2 2 0 01-2 2H7a2 2 0 01-2-2V6m3 0V4a2 2 0 012-2h4a2 2 0 012 2v2"/></svg>
                      </button>
                    </span>
                  </div>
                </template>
              </div>
            </div>

            <!-- Comments Thread -->
            <div v-if="expandedId === d.id" class="dw-comments">
              <div v-if="commentLoading" class="dw-comments-loading">
                <div class="dw-spinner-sm"></div>
              </div>
              <div v-else>
                <div v-if="comments.length === 0" class="dw-comments-empty">
                  {{ isZh ? "暂无回复" : "No replies yet" }}
                </div>
                <div v-for="c in comments" :key="c.id" class="dw-comment">
                  <div class="dw-comment-avatar">{{ c.author_name ? c.author_name.charAt(0).toUpperCase() : "?" }}</div>
                  <div class="dw-comment-content">
                    <div class="dw-comment-header">
                      <span class="dw-comment-author">{{ c.author_name }}</span>
                      <span v-if="c.is_verified" class="dw-badge-verified-sm">
                        <svg width="12" height="12" viewBox="0 0 24 24" fill="var(--vp-c-brand-1)"><path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                      </span>
                      <span class="dw-comment-time">{{ timeAgo(c.created_at) }}</span>
                      <span v-if="canEditCmt(c) || canDeleteCmt(c)" class="dw-cmt-actions">
                        <button v-if="canEditCmt(c)" class="dw-btn-icon-sm" :title="isZh ? '编辑' : 'Edit'" @click="startEditCmt(c)">
                          <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 4H4a2 2 0 00-2 2v14a2 2 0 002 2h14a2 2 0 002-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 013 3L12 15l-4 1 1-4 9.5-9.5z"/></svg>
                        </button>
                        <button v-if="canDeleteCmt(c)" class="dw-btn-icon-sm dw-btn-danger" :title="isZh ? '删除' : 'Delete'" @click="doDeleteCmt(c)">
                          <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="3 6 5 6 21 6"/><path d="M19 6v14a2 2 0 01-2 2H7a2 2 0 01-2-2V6m3 0V4a2 2 0 012-2h4a2 2 0 012 2v2"/></svg>
                        </button>
                      </span>
                    </div>
                    <template v-if="editCommentId === c.id">
                      <input v-model="editCommentBody" class="dw-edit-input-sm" @keydown.enter="saveEditCmt(c)" />
                      <div class="dw-edit-actions-sm">
                        <button class="dw-btn-sm dw-btn-save" @click="saveEditCmt(c)">{{ isZh ? '保存' : 'Save' }}</button>
                        <button class="dw-btn-sm dw-btn-cancel" @click="editCommentId = null">{{ isZh ? '取消' : 'Cancel' }}</button>
                      </div>
                    </template>
                    <p v-else class="dw-comment-body">{{ c.body }}</p>
                  </div>
                </div>
              </div>
              <div class="dw-comment-form">
                <input
                  v-if="!loggedIn"
                  v-model="commentName"
                  :placeholder="isZh ? '您的姓名' : 'Your name'"
                  class="dw-input dw-input-sm"
                />
                <div v-if="!loggedIn" ref="commentTurnstileRef" class="dw-turnstile"></div>
                <div class="dw-comment-input-row">
                  <input
                    v-model="commentBody"
                    :placeholder="isZh ? '添加回复...' : 'Add a reply...'"
                    class="dw-input"
                    @keydown.enter="submitComment"
                  />
                  <button
                    class="dw-btn dw-btn-sm"
                    :disabled="commentSubmitting || !commentBody.trim() || (!loggedIn && !commentTurnstileToken)"
                    @click="submitComment"
                  >
                    {{ commentSubmitting ? "..." : (isZh ? "发送" : "Send") }}
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Pagination -->
        <div v-if="pages > 1" class="dw-pagination">
          <button :disabled="page <= 1" @click="page--; load()" class="dw-btn dw-btn-sm">
            {{ isZh ? "上一页" : "Prev" }}
          </button>
          <span class="dw-page-info">{{ page }} / {{ pages }}</span>
          <button :disabled="page >= pages" @click="page++; load()" class="dw-btn dw-btn-sm">
            {{ isZh ? "下一页" : "Next" }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.dw-layout {
  display: flex;
  gap: 0;
  min-height: 500px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 12px;
  overflow: hidden;
  background: var(--vp-c-bg);
}

/* Sidebar */
.dw-sidebar {
  width: 240px;
  flex-shrink: 0;
  background: var(--vp-c-bg-soft);
  border-right: 1px solid var(--vp-c-divider);
  display: flex;
  flex-direction: column;
}
.dw-sidebar-header {
  padding: 16px 16px 8px;
}
.dw-sidebar-title {
  font-size: 12px;
  font-weight: 600;
  text-transform: uppercase;
  color: var(--vp-c-text-3);
  letter-spacing: 0.5px;
  margin: 0;
}
.dw-channel-list {
  flex: 1;
  padding: 4px 8px;
}
.dw-channel {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  width: 100%;
  padding: 8px 10px;
  border: none;
  background: none;
  border-radius: 6px;
  cursor: pointer;
  text-align: left;
  color: var(--vp-c-text-2);
  transition: all 0.15s;
}
.dw-channel:hover {
  background: var(--vp-c-bg);
  color: var(--vp-c-text-1);
}
.dw-channel.active {
  background: var(--vp-c-brand-soft);
  color: var(--vp-c-brand-1);
}
.dw-channel svg {
  margin-top: 2px;
  flex-shrink: 0;
}
.dw-channel-text {
  display: flex;
  flex-direction: column;
  min-width: 0;
}
.dw-channel-name {
  font-size: 14px;
  font-weight: 500;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.dw-channel-desc {
  font-size: 11px;
  color: var(--vp-c-text-3);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.dw-channel.active .dw-channel-desc {
  color: var(--vp-c-brand-2);
}

.dw-sidebar-footer {
  padding: 12px 16px;
  border-top: 1px solid var(--vp-c-divider);
}
.dw-sort-label {
  font-size: 11px;
  font-weight: 600;
  text-transform: uppercase;
  color: var(--vp-c-text-3);
  letter-spacing: 0.5px;
  margin-bottom: 6px;
}
.dw-sort-select {
  width: 100%;
  padding: 6px 10px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 6px;
  background: var(--vp-c-bg);
  color: var(--vp-c-text-1);
  font-size: 13px;
}

/* Main content */
.dw-main {
  flex: 1;
  min-width: 0;
  display: flex;
  flex-direction: column;
}
.dw-main-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px 20px;
  border-bottom: 1px solid var(--vp-c-divider);
  background: var(--vp-c-bg);
}
.dw-main-header-left {
  display: flex;
  align-items: center;
  gap: 12px;
}
.dw-main-title {
  font-size: 16px;
  font-weight: 600;
  margin: 0;
  color: var(--vp-c-text-1);
}
.dw-disc-count {
  font-size: 13px;
  color: var(--vp-c-text-3);
}

/* Buttons */
.dw-btn {
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
.dw-btn:hover { border-color: var(--vp-c-brand-1); }
.dw-btn:disabled { opacity: 0.5; cursor: not-allowed; }
.dw-btn-primary {
  background: var(--vp-c-brand-1);
  color: white;
  border-color: var(--vp-c-brand-1);
}
.dw-btn-primary:hover { background: var(--vp-c-brand-2); }
.dw-btn-sm { padding: 5px 12px; font-size: 13px; }

/* Form */
.dw-form {
  padding: 16px 20px;
  border-bottom: 1px solid var(--vp-c-divider);
  background: var(--vp-c-bg-soft);
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.dw-form-row { display: flex; gap: 10px; }
.dw-input {
  padding: 9px 14px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  font-size: 14px;
  background: var(--vp-c-bg);
  color: var(--vp-c-text-1);
  width: 100%;
  transition: border-color 0.15s;
}
.dw-input:focus { border-color: var(--vp-c-brand-1); outline: none; }
.dw-input-full { width: 100%; }
.dw-input-sm { width: 200px; }
.dw-textarea {
  width: 100%;
  padding: 9px 14px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  font-size: 14px;
  resize: vertical;
  background: var(--vp-c-bg);
  color: var(--vp-c-text-1);
  font-family: inherit;
}
.dw-textarea:focus { border-color: var(--vp-c-brand-1); outline: none; }
.dw-turnstile {
  margin: 8px 0;
}
.dw-form-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.dw-error {
  color: var(--vp-c-danger-1);
  padding: 10px 20px;
  background: var(--vp-c-danger-soft);
  font-size: 14px;
}

.dw-loading {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  padding: 48px;
  color: var(--vp-c-text-2);
}
.dw-spinner, .dw-spinner-sm {
  border: 2px solid var(--vp-c-divider);
  border-top-color: var(--vp-c-brand-1);
  border-radius: 50%;
  animation: dw-spin 0.6s linear infinite;
}
.dw-spinner { width: 20px; height: 20px; }
.dw-spinner-sm { width: 16px; height: 16px; margin: 8px auto; }
@keyframes dw-spin { to { transform: rotate(360deg); } }

.dw-empty {
  text-align: center;
  padding: 60px 20px;
  color: var(--vp-c-text-3);
}
.dw-empty p { margin: 12px 0 0; font-size: 15px; }

/* Thread list */
.dw-thread-list {
  flex: 1;
  overflow-y: auto;
}
.dw-thread {
  border-bottom: 1px solid var(--vp-c-divider);
}
.dw-thread:last-child { border-bottom: none; }
.dw-thread-main {
  display: flex;
  gap: 14px;
  padding: 18px 20px;
  transition: background 0.15s;
}
.dw-thread-main:hover {
  background: var(--vp-c-bg-soft);
}
.dw-thread-avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--vp-c-brand-1), var(--vp-c-brand-2));
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  font-size: 16px;
  flex-shrink: 0;
}
.dw-thread-content {
  flex: 1;
  min-width: 0;
}
.dw-thread-header {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 4px;
  flex-wrap: wrap;
}
.dw-thread-author {
  font-size: 14px;
  font-weight: 600;
  color: var(--vp-c-text-1);
}
.dw-badge-verified, .dw-badge-verified-sm {
  display: inline-flex;
  align-items: center;
}
.dw-thread-tag {
  font-size: 11px;
  padding: 1px 7px;
  border-radius: 6px;
  background: var(--vp-c-bg-soft);
  color: var(--vp-c-text-3);
  border: 1px solid var(--vp-c-divider);
  text-transform: capitalize;
}
.dw-thread-time {
  font-size: 12px;
  color: var(--vp-c-text-3);
}
.dw-thread-title {
  font-size: 16px;
  font-weight: 600;
  margin: 0 0 6px;
  color: var(--vp-c-text-1);
}
.dw-thread-body {
  font-size: 14px;
  color: var(--vp-c-text-2);
  margin: 0 0 10px;
  line-height: 1.6;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.dw-thread-actions {
  display: flex;
  gap: 12px;
}
.dw-action {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  padding: 4px 10px;
  border: none;
  border-radius: 6px;
  background: var(--vp-c-bg-soft);
  color: var(--vp-c-text-3);
  cursor: pointer;
  font-size: 13px;
  transition: all 0.15s;
}
.dw-action:hover {
  background: var(--vp-c-bg);
  color: var(--vp-c-text-1);
}
.dw-action.active {
  color: var(--vp-c-brand-1);
  background: var(--vp-c-brand-soft);
}

/* Comments */
.dw-comments {
  padding: 0 20px 16px 74px;
  background: var(--vp-c-bg-soft);
  border-top: 1px solid var(--vp-c-divider);
}
.dw-comments-loading { text-align: center; padding: 12px; }
.dw-comments-empty {
  text-align: center;
  padding: 12px;
  color: var(--vp-c-text-3);
  font-size: 13px;
}
.dw-comment {
  display: flex;
  gap: 10px;
  padding: 10px 0;
  border-bottom: 1px solid var(--vp-c-divider);
}
.dw-comment:last-of-type { border-bottom: none; }
.dw-comment-avatar {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: var(--vp-c-bg);
  border: 1px solid var(--vp-c-divider);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 12px;
  font-weight: 600;
  color: var(--vp-c-text-2);
  flex-shrink: 0;
}
.dw-comment-content { flex: 1; min-width: 0; }
.dw-comment-header {
  display: flex;
  align-items: center;
  gap: 6px;
  margin-bottom: 3px;
}
.dw-comment-author {
  font-size: 13px;
  font-weight: 600;
  color: var(--vp-c-text-1);
}
.dw-comment-time {
  font-size: 11px;
  color: var(--vp-c-text-3);
}
.dw-comment-body {
  font-size: 13px;
  color: var(--vp-c-text-2);
  margin: 0;
  line-height: 1.5;
}
.dw-edit-input, .dw-edit-textarea {
  width: 100%; padding: 6px 10px; border: 1px solid var(--vp-c-divider);
  border-radius: 6px; font-size: 14px; margin-bottom: 4px;
  background: var(--vp-c-bg); color: var(--vp-c-text-1);
}
.dw-edit-textarea { resize: vertical; font-size: 13px; }
.dw-edit-actions, .dw-edit-actions-sm { display: flex; gap: 6px; margin-top: 4px; }
.dw-btn-sm {
  padding: 3px 10px; border: none; border-radius: 5px; font-size: 12px;
  cursor: pointer; font-weight: 500;
}
.dw-btn-save { background: var(--vp-c-brand-1); color: #fff; }
.dw-btn-save:hover { opacity: 0.9; }
.dw-btn-cancel { background: var(--vp-c-default-soft); color: var(--vp-c-text-2); }
.dw-owner-actions, .dw-cmt-actions {
  display: inline-flex; gap: 2px; margin-left: auto;
}
.dw-btn-icon, .dw-btn-icon-sm {
  background: none; border: none; cursor: pointer; padding: 2px 4px;
  color: var(--vp-c-text-3); border-radius: 4px; display: inline-flex; align-items: center;
}
.dw-btn-icon:hover, .dw-btn-icon-sm:hover { background: var(--vp-c-default-soft); color: var(--vp-c-text-1); }
.dw-btn-danger:hover { color: #e53e3e; background: #fed7d7; }
.dw-edit-input-sm {
  width: 100%; padding: 4px 8px; border: 1px solid var(--vp-c-divider);
  border-radius: 5px; font-size: 13px; margin-top: 4px;
  background: var(--vp-c-bg); color: var(--vp-c-text-1);
}
.dw-comment-form { margin-top: 12px; }
.dw-comment-input-row {
  display: flex;
  gap: 8px;
}

.dw-pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 16px;
  padding: 16px 20px;
  border-top: 1px solid var(--vp-c-divider);
}
.dw-page-info {
  font-size: 14px;
  color: var(--vp-c-text-2);
}

@media (max-width: 768px) {
  .dw-layout {
    flex-direction: column;
  }
  .dw-sidebar {
    width: 100%;
    border-right: none;
    border-bottom: 1px solid var(--vp-c-divider);
  }
  .dw-channel-list {
    display: flex;
    overflow-x: auto;
    gap: 4px;
    padding: 4px 8px 8px;
  }
  .dw-channel {
    white-space: nowrap;
    flex-shrink: 0;
  }
  .dw-channel-desc {
    display: none;
  }
  .dw-sidebar-footer {
    display: none;
  }
  .dw-comments {
    padding-left: 20px;
  }
}
</style>
