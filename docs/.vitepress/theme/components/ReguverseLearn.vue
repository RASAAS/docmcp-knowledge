<script setup lang="ts">
import { computed, onMounted, onUnmounted, ref, watch } from "vue";
import { useData } from "vitepress";
import {
  createLiveSession,
  ensureParticipantKey,
  getLiveState,
  getPractice,
  hostEnd,
  hostGet,
  hostLock,
  hostPush,
  hostReveal,
  hostWaiting,
  joinLiveSession,
  listCourses,
  loadHostSession,
  saveHostSession,
  submitLiveAnswer,
  submitPractice,
  type CourseSummary,
  type LiveQuestion,
} from "./LearnApi";
import { LEARN_TABS, learnLabel, t, type LearnTabKey } from "./LearnNavData";

const { lang } = useData();
const isZh = computed(() => lang.value === "zh" || lang.value === "zh-CN");

const activeTab = ref<LearnTabKey>("join");
const errorMsg = ref("");
const loading = ref(false);

// --- Join ---
const joinCode = ref("");
const nickname = ref("");
const displayName = ref("");
const participantKey = ref("");
const joined = ref(false);
const liveState = ref<Awaited<ReturnType<typeof getLiveState>> | null>(null);
const selected = ref<string[]>([]);
const answerBusy = ref(false);
let pollTimer: ReturnType<typeof setInterval> | null = null;

// --- Host ---
const hostCode = ref("");
const hostToken = ref("");
const hostTitle = ref("");
const hostCreateSecret = ref("");
const hostView = ref<Awaited<ReturnType<typeof hostGet>> | null>(null);
const copied = ref(false);
let hostPoll: ReturnType<typeof setInterval> | null = null;

// --- Practice ---
const courses = ref<CourseSummary[]>([]);
const practiceSlug = ref("usability-engineering");
const practiceQs = ref<LiveQuestion[]>([]);
const practiceAnswers = ref<Record<string, string[]>>({});
const practiceResult = ref<Awaited<ReturnType<typeof submitPractice>> | null>(null);

function promptOf(q: LiveQuestion) {
  return isZh.value ? q.prompt_zh : q.prompt_en;
}
function optText(o: { text_en: string; text_zh: string }) {
  return isZh.value ? o.text_zh : o.text_en;
}
function explOf(q: { explanation_en?: string; explanation_zh?: string }) {
  return isZh.value ? q.explanation_zh || "" : q.explanation_en || "";
}

function stopPoll() {
  if (pollTimer) {
    clearInterval(pollTimer);
    pollTimer = null;
  }
}
function stopHostPoll() {
  if (hostPoll) {
    clearInterval(hostPoll);
    hostPoll = null;
  }
}

async function refreshLive() {
  if (!joined.value || !joinCode.value) return;
  try {
    liveState.value = await getLiveState(joinCode.value, participantKey.value);
    if (liveState.value.my_answer) selected.value = [...liveState.value.my_answer];
  } catch (e) {
    errorMsg.value = e instanceof Error ? e.message : t("error", isZh.value);
  }
}

async function doJoin() {
  errorMsg.value = "";
  loading.value = true;
  try {
    participantKey.value = ensureParticipantKey();
    const res = await joinLiveSession(joinCode.value.trim().toUpperCase(), {
      nickname: nickname.value.trim(),
      display_name: displayName.value.trim(),
      participant_key: participantKey.value,
    });
    participantKey.value = res.participant_key;
    joinCode.value = res.session_code;
    joined.value = true;
    await refreshLive();
    stopPoll();
    pollTimer = setInterval(refreshLive, 2000);
  } catch (e) {
    errorMsg.value = e instanceof Error ? e.message : t("error", isZh.value);
  } finally {
    loading.value = false;
  }
}

function toggleOption(q: LiveQuestion, id: string) {
  if (!liveState.value?.can_answer) return;
  if (q.qtype === "single") {
    selected.value = [id];
    return;
  }
  if (selected.value.includes(id)) selected.value = selected.value.filter((x) => x !== id);
  else selected.value = [...selected.value, id];
}

async function doSubmitAnswer() {
  if (!liveState.value?.can_answer || selected.value.length === 0) return;
  answerBusy.value = true;
  errorMsg.value = "";
  try {
    await submitLiveAnswer(joinCode.value, {
      participant_key: participantKey.value,
      answer: selected.value,
    });
    await refreshLive();
  } catch (e) {
    errorMsg.value = e instanceof Error ? e.message : t("error", isZh.value);
  } finally {
    answerBusy.value = false;
  }
}

async function refreshHost() {
  if (!hostCode.value || !hostToken.value) return;
  try {
    hostView.value = await hostGet(hostCode.value, hostToken.value);
  } catch (e) {
    errorMsg.value = e instanceof Error ? e.message : t("error", isZh.value);
  }
}

async function doCreateHost() {
  errorMsg.value = "";
  loading.value = true;
  try {
    const res = await createLiveSession({
      course_slug: "usability-engineering",
      title: hostTitle.value.trim(),
      create_secret: hostCreateSecret.value.trim() || undefined,
    });
    hostCode.value = res.code;
    hostToken.value = res.host_token;
    saveHostSession(res.code, res.host_token);
    await refreshHost();
    stopHostPoll();
    hostPoll = setInterval(refreshHost, 2500);
  } catch (e) {
    errorMsg.value = e instanceof Error ? e.message : t("error", isZh.value);
  } finally {
    loading.value = false;
  }
}

function restoreHost() {
  const saved = loadHostSession();
  if (!saved) return;
  hostCode.value = saved.code;
  hostToken.value = saved.host_token;
  refreshHost();
  stopHostPoll();
  hostPoll = setInterval(refreshHost, 2500);
}

async function runHost(action: "push" | "lock" | "reveal" | "waiting" | "end", qid?: string) {
  if (!hostCode.value || !hostToken.value) return;
  errorMsg.value = "";
  try {
    if (action === "push") await hostPush(hostCode.value, hostToken.value, qid ? { qid } : undefined);
    else if (action === "lock") await hostLock(hostCode.value, hostToken.value);
    else if (action === "reveal") await hostReveal(hostCode.value, hostToken.value);
    else if (action === "waiting") await hostWaiting(hostCode.value, hostToken.value);
    else await hostEnd(hostCode.value, hostToken.value);
    await refreshHost();
  } catch (e) {
    errorMsg.value = e instanceof Error ? e.message : t("error", isZh.value);
  }
}

async function copyJoinLink() {
  if (!hostCode.value) return;
  const url = `${window.location.origin}${isZh.value ? "/zh" : "/en"}/learn/?code=${hostCode.value}`;
  await navigator.clipboard.writeText(url);
  copied.value = true;
  setTimeout(() => (copied.value = false), 1500);
}

async function loadCourses() {
  try {
    const res = await listCourses();
    courses.value = res.items || [];
  } catch {
    courses.value = [];
  }
}

async function startPractice() {
  errorMsg.value = "";
  practiceResult.value = null;
  practiceAnswers.value = {};
  loading.value = true;
  try {
    const res = await getPractice(practiceSlug.value);
    practiceQs.value = res.questions;
  } catch (e) {
    errorMsg.value = e instanceof Error ? e.message : t("error", isZh.value);
  } finally {
    loading.value = false;
  }
}

function setPracticeAnswer(q: LiveQuestion, id: string) {
  const cur = practiceAnswers.value[q.qid] || [];
  if (q.qtype === "single") {
    practiceAnswers.value = { ...practiceAnswers.value, [q.qid]: [id] };
    return;
  }
  const next = cur.includes(id) ? cur.filter((x) => x !== id) : [...cur, id];
  practiceAnswers.value = { ...practiceAnswers.value, [q.qid]: next };
}

async function checkPractice() {
  loading.value = true;
  errorMsg.value = "";
  try {
    practiceResult.value = await submitPractice(practiceSlug.value, {
      participant_key: ensureParticipantKey(),
      nickname: nickname.value.trim() || "learner",
      answers: practiceAnswers.value,
    });
  } catch (e) {
    errorMsg.value = e instanceof Error ? e.message : t("error", isZh.value);
  } finally {
    loading.value = false;
  }
}

watch(activeTab, (tab) => {
  if (tab !== "join") stopPoll();
  if (tab !== "host") stopHostPoll();
  if (tab === "host" && hostCode.value && hostToken.value) {
    hostPoll = setInterval(refreshHost, 2500);
  }
  if (tab === "join" && joined.value) {
    pollTimer = setInterval(refreshLive, 2000);
  }
  if (tab === "practice") loadCourses();
});

onMounted(() => {
  participantKey.value = ensureParticipantKey();
  const params = new URLSearchParams(window.location.search);
  const code = params.get("code");
  if (code) {
    joinCode.value = code.toUpperCase();
    activeTab.value = "join";
  }
  loadCourses();
});

onUnmounted(() => {
  stopPoll();
  stopHostPoll();
});
</script>

<template>
  <div class="learn-root">
    <header class="learn-header">
      <h1>{{ t("title", isZh) }}</h1>
      <p class="learn-sub">{{ t("subtitle", isZh) }}</p>
    </header>

    <nav class="learn-tabs">
      <button
        v-for="tab in LEARN_TABS"
        :key="tab.key"
        type="button"
        class="learn-tab"
        :class="{ active: activeTab === tab.key }"
        @click="activeTab = tab.key"
      >
        {{ learnLabel(tab, isZh) }}
      </button>
    </nav>

    <p v-if="errorMsg" class="learn-error">{{ errorMsg }}</p>

    <!-- Join -->
    <section v-if="activeTab === 'join'" class="learn-panel">
      <div v-if="!joined" class="learn-form">
        <label>
          {{ t("sessionCode", isZh) }}
          <input v-model="joinCode" maxlength="8" autocomplete="off" />
        </label>
        <label>
          {{ t("nickname", isZh) }}
          <input v-model="nickname" maxlength="40" autocomplete="nickname" />
        </label>
        <label>
          {{ t("displayName", isZh) }}
          <input v-model="displayName" maxlength="80" autocomplete="name" />
        </label>
        <button type="button" class="learn-btn primary" :disabled="loading || !joinCode || !nickname" @click="doJoin">
          {{ t("join", isZh) }}
        </button>
      </div>

      <div v-else class="learn-live">
        <div class="learn-meta">
          <span>{{ t("sessionCode", isZh) }}: <strong>{{ liveState?.code || joinCode }}</strong></span>
          <span>{{ t("phase", isZh) }}: {{ liveState?.phase }}</span>
          <span>{{ t("participants", isZh) }}: {{ liveState?.participant_count ?? 0 }}</span>
        </div>

        <div v-if="!liveState?.question || liveState.phase === 'waiting'" class="learn-waiting">
          {{ t("waiting", isZh) }}
        </div>

        <div v-else class="learn-question">
          <div class="qid">{{ liveState.question.qid }}</div>
          <h2>{{ promptOf(liveState.question) }}</h2>
          <p v-if="liveState.question.qtype === 'multi'" class="hint">{{ t("multiHint", isZh) }}</p>
          <div class="options">
            <button
              v-for="opt in liveState.question.options"
              :key="opt.id"
              type="button"
              class="opt"
              :class="{
                selected: selected.includes(opt.id),
                correct: liveState.phase === 'reveal' && liveState.question.correct?.includes(opt.id),
              }"
              :disabled="!liveState.can_answer"
              @click="toggleOption(liveState.question!, opt.id)"
            >
              <span class="oid">{{ opt.id.toUpperCase() }}</span>
              <span>{{ optText(opt) }}</span>
            </button>
          </div>

          <button
            v-if="liveState.can_answer"
            type="button"
            class="learn-btn primary"
            :disabled="answerBusy || selected.length === 0"
            @click="doSubmitAnswer"
          >
            {{ t("submit", isZh) }}
          </button>
          <p v-else-if="liveState.my_answer" class="status-ok">{{ t("submitted", isZh) }}</p>
          <p v-if="liveState.phase === 'locked'" class="status">{{ t("locked", isZh) }}</p>
          <div v-if="liveState.phase === 'reveal'" class="reveal-box">
            <p><strong>{{ t("reveal", isZh) }}</strong></p>
            <p>{{ explOf(liveState.question) }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Host -->
    <section v-if="activeTab === 'host'" class="learn-panel">
      <div v-if="!hostToken" class="learn-form">
        <label>
          {{ isZh ? "场次标题（可选）" : "Session title (optional)" }}
          <input v-model="hostTitle" maxlength="120" />
        </label>
        <label>
          {{ isZh ? "创建密钥（若已配置）" : "Create secret (if configured)" }}
          <input v-model="hostCreateSecret" type="password" autocomplete="off" />
        </label>
        <button type="button" class="learn-btn primary" :disabled="loading" @click="doCreateHost">
          {{ t("create", isZh) }}
        </button>
        <button type="button" class="learn-btn" @click="restoreHost">{{ t("restoreHost", isZh) }}</button>
      </div>

      <div v-else class="learn-host">
        <div class="learn-meta">
          <span>{{ t("sessionCode", isZh) }}: <strong class="code-lg">{{ hostCode }}</strong></span>
          <span>{{ t("participants", isZh) }}: {{ hostView?.participant_count ?? 0 }}</span>
          <span>{{ t("answered", isZh) }}: {{ hostView?.answered ?? 0 }}</span>
          <span>{{ t("phase", isZh) }}: {{ hostView?.phase }}</span>
        </div>
        <p class="hint">{{ t("hostTokenHint", isZh) }}</p>
        <div class="host-actions">
          <button type="button" class="learn-btn primary" @click="runHost('push')">{{ t("push", isZh) }}</button>
          <button type="button" class="learn-btn" @click="runHost('lock')">{{ t("lock", isZh) }}</button>
          <button type="button" class="learn-btn" @click="runHost('reveal')">{{ t("revealBtn", isZh) }}</button>
          <button type="button" class="learn-btn" @click="runHost('waiting')">{{ t("lobby", isZh) }}</button>
          <button type="button" class="learn-btn" @click="copyJoinLink">
            {{ copied ? t("copied", isZh) : t("copyLink", isZh) }}
          </button>
          <button type="button" class="learn-btn danger" @click="runHost('end')">{{ t("end", isZh) }}</button>
        </div>

        <div v-if="hostView?.question" class="learn-question">
          <div class="qid">{{ hostView.question.qid }}</div>
          <h2>{{ promptOf(hostView.question) }}</h2>
          <ul class="stat-list">
            <li v-for="opt in hostView.question.options" :key="opt.id">
              <strong>{{ opt.id.toUpperCase() }}</strong>
              {{ optText(opt) }}
              — {{ hostView.option_counts?.[opt.id] || 0 }}
            </li>
          </ul>
          <p v-if="hostView.phase === 'reveal' && hostView.correct_count != null">
            {{ t("correct", isZh) }}: {{ hostView.correct_count }} / {{ hostView.answered }}
          </p>
          <p v-if="hostView.phase === 'reveal'">{{ explOf(hostView.question) }}</p>
        </div>

        <div v-if="hostView?.question_list?.length" class="qid-list">
          <button
            v-for="q in hostView.question_list"
            :key="q.id"
            type="button"
            class="learn-btn sm"
            @click="runHost('push', q.qid)"
          >
            {{ q.qid }}
          </button>
        </div>
      </div>
    </section>

    <!-- Practice -->
    <section v-if="activeTab === 'practice'" class="learn-panel">
      <div class="learn-form row">
        <label>
          {{ isZh ? "课程" : "Course" }}
          <select v-model="practiceSlug">
            <option v-for="c in courses" :key="c.slug" :value="c.slug">
              {{ isZh ? c.title_zh : c.title_en }}
            </option>
            <option v-if="!courses.length" value="usability-engineering">
              {{ isZh ? "可用性工程基础" : "Usability Engineering Fundamentals" }}
            </option>
          </select>
        </label>
        <button type="button" class="learn-btn primary" :disabled="loading" @click="startPractice">
          {{ t("practiceStart", isZh) }}
        </button>
      </div>

      <div v-if="practiceQs.length" class="practice-list">
        <article v-for="q in practiceQs" :key="q.qid" class="learn-question">
          <div class="qid">{{ q.qid }}</div>
          <h3>{{ promptOf(q) }}</h3>
          <p v-if="q.qtype === 'multi'" class="hint">{{ t("multiHint", isZh) }}</p>
          <div class="options">
            <button
              v-for="opt in q.options"
              :key="opt.id"
              type="button"
              class="opt"
              :class="{
                selected: (practiceAnswers[q.qid] || []).includes(opt.id),
                correct: practiceResult && practiceResult.detail.find((d) => d.qid === q.qid)?.expected.includes(opt.id),
              }"
              :disabled="!!practiceResult"
              @click="setPracticeAnswer(q, opt.id)"
            >
              <span class="oid">{{ opt.id.toUpperCase() }}</span>
              <span>{{ optText(opt) }}</span>
            </button>
          </div>
          <p v-if="practiceResult" class="reveal-box">
            {{
              practiceResult.detail.find((d) => d.qid === q.qid)?.correct
                ? t("correct", isZh)
                : t("incorrect", isZh)
            }}
            — {{ explOf(practiceResult.detail.find((d) => d.qid === q.qid) || {}) }}
          </p>
        </article>

        <button
          v-if="!practiceResult"
          type="button"
          class="learn-btn primary"
          :disabled="loading"
          @click="checkPractice"
        >
          {{ t("practiceSubmit", isZh) }}
        </button>
        <p v-else class="score">
          {{ t("score", isZh) }}: {{ practiceResult.score }} / {{ practiceResult.total }}
        </p>
      </div>
    </section>
  </div>
</template>

<style scoped>
.learn-root {
  max-width: 820px;
  margin: 0 auto;
  padding: 1.25rem 1rem 3rem;
  font-family: "Source Sans 3", "Noto Sans SC", system-ui, sans-serif;
}
.learn-header h1 {
  margin: 0;
  font-size: 1.75rem;
  letter-spacing: -0.02em;
}
.learn-sub {
  color: var(--vp-c-text-2);
  margin: 0.35rem 0 1rem;
}
.learn-tabs {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
  margin-bottom: 1rem;
}
.learn-tab {
  border: 1px solid var(--vp-c-divider);
  background: var(--vp-c-bg-soft);
  color: var(--vp-c-text-1);
  border-radius: 8px;
  padding: 0.45rem 0.85rem;
  cursor: pointer;
}
.learn-tab.active {
  border-color: var(--vp-c-brand-1);
  background: var(--vp-c-brand-soft);
}
.learn-error {
  color: #b42318;
  background: #fef3f2;
  padding: 0.6rem 0.8rem;
  border-radius: 8px;
}
.learn-form {
  display: grid;
  gap: 0.75rem;
}
.learn-form.row {
  grid-template-columns: 1fr auto;
  align-items: end;
}
.learn-form label {
  display: grid;
  gap: 0.35rem;
  font-size: 0.92rem;
}
.learn-form input,
.learn-form select {
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  padding: 0.55rem 0.7rem;
  background: var(--vp-c-bg);
  color: var(--vp-c-text-1);
}
.learn-btn {
  border: 1px solid var(--vp-c-divider);
  background: var(--vp-c-bg-soft);
  color: var(--vp-c-text-1);
  border-radius: 8px;
  padding: 0.55rem 0.9rem;
  cursor: pointer;
}
.learn-btn.primary {
  background: var(--vp-c-brand-1);
  border-color: var(--vp-c-brand-1);
  color: #fff;
}
.learn-btn.danger {
  border-color: #f04438;
  color: #b42318;
}
.learn-btn.sm {
  padding: 0.3rem 0.55rem;
  font-size: 0.85rem;
}
.learn-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
.learn-meta {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem 1.25rem;
  margin-bottom: 0.75rem;
  font-size: 0.92rem;
}
.code-lg {
  font-size: 1.35rem;
  letter-spacing: 0.08em;
}
.learn-waiting {
  padding: 2rem 1rem;
  text-align: center;
  color: var(--vp-c-text-2);
  border: 1px dashed var(--vp-c-divider);
  border-radius: 12px;
}
.learn-question {
  margin-top: 0.75rem;
}
.qid {
  font-size: 0.8rem;
  color: var(--vp-c-text-2);
  letter-spacing: 0.04em;
}
.options {
  display: grid;
  gap: 0.5rem;
  margin: 0.75rem 0 1rem;
}
.opt {
  display: flex;
  gap: 0.65rem;
  text-align: left;
  border: 1px solid var(--vp-c-divider);
  border-radius: 10px;
  padding: 0.7rem 0.8rem;
  background: var(--vp-c-bg);
  color: var(--vp-c-text-1);
  cursor: pointer;
}
.opt.selected {
  border-color: var(--vp-c-brand-1);
  background: var(--vp-c-brand-soft);
}
.opt.correct {
  border-color: #12b76a;
  background: #ecfdf3;
}
.oid {
  font-weight: 700;
  min-width: 1.2rem;
}
.hint {
  color: var(--vp-c-text-2);
  font-size: 0.9rem;
}
.reveal-box {
  margin-top: 0.75rem;
  padding: 0.75rem;
  border-radius: 8px;
  background: var(--vp-c-bg-soft);
}
.host-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin: 0.75rem 0 1rem;
}
.qid-list {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
  margin-top: 1rem;
}
.stat-list {
  padding-left: 1.1rem;
}
.score {
  font-size: 1.15rem;
  font-weight: 650;
}
.status-ok {
  color: #027a48;
}
@media (max-width: 640px) {
  .learn-form.row {
    grid-template-columns: 1fr;
  }
}
</style>
