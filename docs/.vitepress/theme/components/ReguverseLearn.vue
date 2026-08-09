<script setup lang="ts">
import { computed, onMounted, onUnmounted, ref, watch } from "vue";
import { useData } from "vitepress";
import QRCode from "qrcode";
import {
  buildJoinUrl,
  createLiveSession,
  ensureParticipantKey,
  getLiveState,
  getPractice,
  getWorkshop,
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
  saveWorkshop,
  submitLiveAnswer,
  submitPractice,
  verifyLearnAuth,
  type CourseSummary,
  type HostView,
  type LiveQuestion,
  type WorkshopGroup,
} from "./LearnApi";
import { getDisplayName, isLoggedIn, logout as hubLogout } from "./HubApi";
import HubOtpLogin from "./HubOtpLogin.vue";
import { LEARN_TABS, learnLabel, t, type LearnTabKey } from "./LearnNavData";

const { lang } = useData();
const isZh = computed(() => lang.value === "zh" || lang.value === "zh-CN");

const activeTab = ref<LearnTabKey>("join");
const joinOnlyMode = ref(false);
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
const hostView = ref<HostView | null>(null);
const hostQuestionList = ref<NonNullable<HostView["question_list"]>>([]);
const hostActionBusy = ref(false);
const copied = ref(false);
let hostPoll: ReturnType<typeof setInterval> | null = null;
let hostListLoaded = false;

// --- Workshop ---
const workshopCode = ref("");
const workshopGroup = ref(1);
const workshopGroups = ref<WorkshopGroup[]>([]);
const workshopDraft = ref({
  task1: {
    users: "",
    environment: "",
    intended_use: "",
    pof_candidates: "",
    foreseeable_misuse: "",
  },
  task2: { use_errors: "", summative_candidates: "", primary_hrus: "" },
  task3: {
    inherent_safety: "",
    protective: "",
    information_for_safety: "",
    needs_ue_eval: "",
  },
  task4: {
    formative_needed: "",
    summative_needed: "",
    success_criteria: "",
    failure_reentry: "",
  },
});
let workshopPoll: ReturnType<typeof setInterval> | null = null;

/** Session code used for audience QR (Join tab). Prefer join form code, fallback host code. */
const qrSessionCode = computed(() => {
  const c = (joinCode.value || hostCode.value || "").trim().toUpperCase();
  return c.length >= 4 ? c : "";
});
const audienceJoinUrl = computed(() =>
  qrSessionCode.value ? buildJoinUrl(qrSessionCode.value, isZh.value) : ""
);
/** Project QR on Join tab; hide for students who already arrived via ?mode=join */
const showJoinQr = computed(
  () => !!audienceJoinUrl.value && !joined.value && !joinOnlyMode.value
);
const qrDataUrl = ref("");

watch(
  [audienceJoinUrl, showJoinQr],
  async ([url, show]) => {
    if (typeof window === "undefined" || !show || !url) {
      qrDataUrl.value = "";
      return;
    }
    try {
      qrDataUrl.value = await QRCode.toDataURL(url, {
        width: 280,
        margin: 2,
        errorCorrectionLevel: "M",
        color: { dark: "#111111", light: "#ffffff" },
      });
    } catch (e) {
      console.error("QR generate failed", e);
      qrDataUrl.value = "";
    }
  },
  { immediate: true }
);

// --- Practice + login (shared Hub OTP dialog) ---
const practiceLoggedIn = ref(false);
const practiceUserName = ref("");
const showLoginDialog = ref(false);

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
function stopWorkshopPoll() {
  if (workshopPoll) {
    clearInterval(workshopPoll);
    workshopPoll = null;
  }
}

function applyHostView(view: HostView, opts?: { keepList?: boolean }) {
  const prevList = hostQuestionList.value;
  hostView.value = view;
  if (view.question_list?.length) {
    hostQuestionList.value = view.question_list;
    hostListLoaded = true;
  } else if (!opts?.keepList && !hostListLoaded) {
    hostQuestionList.value = prevList;
  }
}

async function refreshAuth() {
  if (!isLoggedIn()) {
    practiceLoggedIn.value = false;
    practiceUserName.value = "";
    return;
  }
  const v = await verifyLearnAuth();
  practiceLoggedIn.value = v.verified;
  practiceUserName.value = v.display_name || getDisplayName() || "";
  if (!v.verified) {
    hubLogout();
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

async function refreshHost(opts?: { full?: boolean }) {
  if (!hostCode.value || !hostToken.value) return;
  try {
    const needFull = opts?.full || !hostListLoaded;
    const view = await hostGet(hostCode.value, hostToken.value, { light: !needFull });
    applyHostView(view, { keepList: true });
  } catch (e) {
    errorMsg.value = e instanceof Error ? e.message : t("error", isZh.value);
  }
}

function requireLogin(messageKey: "loginRequired" | "hostLoginRequired" = "loginRequired") {
  errorMsg.value = t(messageKey, isZh.value);
  showLoginDialog.value = true;
}

async function onLoginSuccess(payload: { displayName: string }) {
  showLoginDialog.value = false;
  errorMsg.value = "";
  practiceUserName.value = payload.displayName || getDisplayName() || "";
  // Confirm token is accepted by learn-api (same HUB_TOKEN_SECRET as hub-api)
  await refreshAuth();
  if (!practiceLoggedIn.value) {
    errorMsg.value = isZh.value
      ? "登录成功，但 Learn 服务未能验证会话。请刷新后重试，或联系管理员检查 HUB_TOKEN_SECRET。"
      : "Signed in, but Learn could not verify the session. Refresh and retry, or check HUB_TOKEN_SECRET.";
  }
}

async function doCreateHost() {
  if (!practiceLoggedIn.value) {
    requireLogin("hostLoginRequired");
    return;
  }
  errorMsg.value = "";
  loading.value = true;
  try {
    const res = await createLiveSession({
      course_slug: "usability-engineering",
      title: hostTitle.value.trim(),
      create_secret: hostCreateSecret.value.trim() || undefined,
    });
    hostCode.value = res.code;
    joinCode.value = res.code;
    workshopCode.value = res.code;
    hostToken.value = res.host_token;
    hostListLoaded = false;
    saveHostSession(res.code, res.host_token);
    await refreshHost({ full: true });
    stopHostPoll();
    hostPoll = setInterval(() => refreshHost({ full: false }), 4000);
    activeTab.value = "join";
    joinOnlyMode.value = false;
  } catch (e) {
    const msg = e instanceof Error ? e.message : t("error", isZh.value);
    if (msg === "LOGIN_REQUIRED" || msg.includes("401")) {
      doLogout();
      requireLogin("hostLoginRequired");
    } else {
      errorMsg.value = msg;
    }
  } finally {
    loading.value = false;
  }
}

function restoreHost() {
  if (!practiceLoggedIn.value) {
    requireLogin("hostLoginRequired");
    return;
  }
  const saved = loadHostSession();
  if (!saved) return;
  hostCode.value = saved.code;
  joinCode.value = saved.code;
  workshopCode.value = saved.code;
  hostToken.value = saved.host_token;
  hostListLoaded = false;
  refreshHost({ full: true });
  stopHostPoll();
  hostPoll = setInterval(() => refreshHost({ full: false }), 4000);
}

function goJoinShowQr() {
  if (hostCode.value && !joinCode.value) joinCode.value = hostCode.value;
  joinOnlyMode.value = false;
  activeTab.value = "join";
}

async function runHost(action: "push" | "lock" | "reveal" | "waiting" | "end", qid?: string) {
  if (!hostCode.value || !hostToken.value || hostActionBusy.value) return;
  errorMsg.value = "";
  hostActionBusy.value = true;
  // Optimistic phase hint for push/lock/reveal
  if (hostView.value && action === "push") {
    hostView.value = { ...hostView.value, phase: "open" };
  } else if (hostView.value && action === "lock") {
    hostView.value = { ...hostView.value, phase: "locked" };
  } else if (hostView.value && action === "reveal") {
    hostView.value = { ...hostView.value, phase: "reveal" };
  }
  try {
    let view: HostView;
    if (action === "push") view = await hostPush(hostCode.value, hostToken.value, qid ? { qid } : undefined);
    else if (action === "lock") view = await hostLock(hostCode.value, hostToken.value);
    else if (action === "reveal") view = await hostReveal(hostCode.value, hostToken.value);
    else if (action === "waiting") view = await hostWaiting(hostCode.value, hostToken.value);
    else view = await hostEnd(hostCode.value, hostToken.value);
    applyHostView(view, { keepList: true });
  } catch (e) {
    errorMsg.value = e instanceof Error ? e.message : t("error", isZh.value);
    await refreshHost({ full: false });
  } finally {
    hostActionBusy.value = false;
  }
}

function loadDraftFromGroup(g: WorkshopGroup | undefined) {
  if (!g) return;
  workshopDraft.value = {
    task1: { ...workshopDraft.value.task1, ...(g.task1 as object) },
    task2: { ...workshopDraft.value.task2, ...(g.task2 as object) },
    task3: { ...workshopDraft.value.task3, ...(g.task3 as object) },
    task4: { ...workshopDraft.value.task4, ...(g.task4 as object) },
  } as typeof workshopDraft.value;
}

async function refreshWorkshop() {
  const code = (workshopCode.value || joinCode.value || hostCode.value || "").trim().toUpperCase();
  if (!code) return;
  workshopCode.value = code;
  try {
    const res = await getWorkshop(code);
    workshopGroups.value = res.groups;
    const mine = res.groups.find((g) => g.group_no === workshopGroup.value);
    loadDraftFromGroup(mine);
  } catch (e) {
    errorMsg.value = e instanceof Error ? e.message : t("error", isZh.value);
  }
}

async function saveWorkshopBoard() {
  const code = workshopCode.value.trim().toUpperCase();
  if (!code) {
    errorMsg.value = isZh.value ? "请先填写会话码或加入现场" : "Enter session code or join live first";
    return;
  }
  loading.value = true;
  errorMsg.value = "";
  try {
    const res = await saveWorkshop(code, workshopGroup.value, {
      ...workshopDraft.value,
      updated_by: nickname.value || practiceUserName.value || `G${workshopGroup.value}`,
      participant_key: participantKey.value || ensureParticipantKey(),
      host_token: hostToken.value || undefined,
    });
    workshopGroups.value = res.groups;
  } catch (e) {
    errorMsg.value = e instanceof Error ? e.message : t("error", isZh.value);
  } finally {
    loading.value = false;
  }
}

watch(workshopGroup, () => {
  const mine = workshopGroups.value.find((g) => g.group_no === workshopGroup.value);
  loadDraftFromGroup(mine);
});

async function copyJoinLink() {
  const url =
    audienceJoinUrl.value ||
    (hostCode.value ? buildJoinUrl(hostCode.value, isZh.value) : "");
  if (!url) return;
  await navigator.clipboard.writeText(url);
  copied.value = true;
  setTimeout(() => (copied.value = false), 1500);
}

function doLogout() {
  hubLogout();
  practiceLoggedIn.value = false;
  practiceUserName.value = "";
  practiceQs.value = [];
  practiceResult.value = null;
  showLoginDialog.value = false;
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
  if (!practiceLoggedIn.value) {
    requireLogin("loginRequired");
    return;
  }
  practiceResult.value = null;
  practiceAnswers.value = {};
  loading.value = true;
  try {
    const res = await getPractice(practiceSlug.value);
    practiceQs.value = res.questions;
  } catch (e) {
    const msg = e instanceof Error ? e.message : t("error", isZh.value);
    if (msg === "LOGIN_REQUIRED" || msg.includes("401")) {
      doLogout();
      requireLogin("loginRequired");
    } else {
      errorMsg.value = msg;
    }
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
  if (!practiceLoggedIn.value) {
    requireLogin("loginRequired");
    return;
  }
  loading.value = true;
  errorMsg.value = "";
  try {
    practiceResult.value = await submitPractice(practiceSlug.value, {
      participant_key: ensureParticipantKey(),
      nickname: practiceUserName.value || nickname.value.trim() || "learner",
      answers: practiceAnswers.value,
    });
  } catch (e) {
    errorMsg.value = e instanceof Error ? e.message : t("error", isZh.value);
  } finally {
    loading.value = false;
  }
}

const visibleTabs = computed(() =>
  joinOnlyMode.value ? LEARN_TABS.filter((x) => x.key === "join") : LEARN_TABS
);

watch(activeTab, (tab) => {
  if (tab !== "join") stopPoll();
  if (tab !== "host") stopHostPoll();
  if (tab !== "workshop") stopWorkshopPoll();
  if (tab === "host") {
    refreshAuth();
    if (hostCode.value && hostToken.value) {
      refreshHost({ full: !hostListLoaded });
      hostPoll = setInterval(() => refreshHost({ full: false }), 4000);
    }
  }
  if (tab === "join" && joined.value) {
    pollTimer = setInterval(refreshLive, 2500);
  }
  if (tab === "workshop") {
    if (!workshopCode.value) workshopCode.value = joinCode.value || hostCode.value || "";
    refreshWorkshop();
    workshopPoll = setInterval(refreshWorkshop, 5000);
  }
  if (tab === "practice") {
    loadCourses();
    refreshAuth();
  }
});

onMounted(async () => {
  participantKey.value = ensureParticipantKey();
  const params = new URLSearchParams(window.location.search);
  const code = params.get("code");
  const mode = params.get("mode");
  if (code) {
    joinCode.value = code.toUpperCase();
    workshopCode.value = code.toUpperCase();
    activeTab.value = "join";
  }
  if (mode === "join" || code) {
    joinOnlyMode.value = mode === "join" || window.matchMedia("(max-width: 768px)").matches;
  }
  await refreshAuth();
  loadCourses();
});

onUnmounted(() => {
  stopPoll();
  stopHostPoll();
  stopWorkshopPoll();
});
</script>

<template>
  <div class="learn-root" :class="{ 'join-focus': joinOnlyMode || activeTab === 'join' }">
    <header class="learn-header">
      <div class="learn-title-row">
        <div>
          <h1>{{ t("title", isZh) }}</h1>
          <p class="learn-sub">{{ t("subtitle", isZh) }}</p>
        </div>
        <div v-if="!joinOnlyMode" class="learn-auth">
          <template v-if="practiceLoggedIn">
            <span class="learn-auth-badge">{{ practiceUserName || t("signedInAs", isZh) }}</span>
            <button type="button" class="learn-btn sm" @click="doLogout">{{ t("logout", isZh) }}</button>
          </template>
          <button v-else type="button" class="learn-btn primary sm" @click="showLoginDialog = true">
            {{ t("signIn", isZh) }}
          </button>
        </div>
      </div>
    </header>

    <HubOtpLogin
      :open="showLoginDialog"
      :is-zh="isZh"
      variant="learn"
      @close="showLoginDialog = false"
      @success="onLoginSuccess"
    />

    <nav v-if="visibleTabs.length > 1 || !joinOnlyMode" class="learn-tabs">
      <button
        v-for="tab in visibleTabs"
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

    <!-- Join (audience-facing: QR + session code + form) -->
    <section v-if="activeTab === 'join'" class="learn-panel">
      <div v-if="!joined" class="join-form">
        <div v-if="showJoinQr" class="qr-panel">
          <p class="qr-title">{{ t("scanToJoin", isZh) }}</p>
          <img
            v-if="qrDataUrl"
            class="qr-img"
            :src="qrDataUrl"
            :alt="t('scanToJoin', isZh)"
            width="280"
            height="280"
          />
          <p v-else class="hint">{{ isZh ? "正在生成二维码…" : "Generating QR…" }}</p>
          <div class="code-under-qr">{{ qrSessionCode }}</div>
          <p class="hint">{{ t("orEnterCode", isZh) }}</p>
          <p class="join-url-line">{{ audienceJoinUrl }}</p>
        </div>
        <p v-else-if="!joinOnlyMode" class="hint enter-code-hint">{{ t("enterCodeForQr", isZh) }}</p>
        <p v-if="joinOnlyMode && joinCode" class="join-banner">
          {{ isZh ? "已识别会话，请填写昵称后加入" : "Session detected — enter a nickname to join" }}
        </p>
        <div class="learn-form">
          <label>
            {{ t("sessionCode", isZh) }}
            <input v-model="joinCode" maxlength="8" autocomplete="off" class="input-lg" inputmode="text" />
          </label>
          <label>
            {{ t("nickname", isZh) }}
            <input v-model="nickname" maxlength="40" autocomplete="nickname" class="input-lg" />
          </label>
          <label>
            {{ t("displayName", isZh) }}
            <input v-model="displayName" maxlength="80" autocomplete="name" class="input-lg" />
          </label>
          <button
            type="button"
            class="learn-btn primary btn-lg"
            :disabled="loading || !joinCode || !nickname"
            @click="doJoin"
          >
            {{ t("join", isZh) }}
          </button>
        </div>
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
            class="learn-btn primary btn-lg"
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
      <div v-if="!practiceLoggedIn" class="learn-form login-box">
        <p class="login-required">{{ t("hostLoginRequired", isZh) }}</p>
        <p class="hint">{{ t("registerHint", isZh) }}</p>
        <button type="button" class="learn-btn primary" @click="showLoginDialog = true">
          {{ t("signIn", isZh) }}
        </button>
      </div>

      <template v-else>
        <div class="auth-bar">
          <span>{{ t("signedInAs", isZh) }}: <strong>{{ practiceUserName }}</strong></span>
          <button type="button" class="learn-btn sm" @click="doLogout">{{ t("logout", isZh) }}</button>
        </div>

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
            <span v-if="hostActionBusy">{{ t("hostBusy", isZh) }}</span>
          </div>
          <p class="hint">{{ t("qrHostHint", isZh) }}</p>
          <p class="hint">{{ t("hostTokenHint", isZh) }}</p>
          <div class="host-actions">
            <button type="button" class="learn-btn primary" @click="goJoinShowQr">
              {{ t("showQrOnJoin", isZh) }}
            </button>
            <button
              type="button"
              class="learn-btn primary"
              :disabled="hostActionBusy"
              @click="runHost('push')"
            >
              {{ t("push", isZh) }}
            </button>
            <button type="button" class="learn-btn" :disabled="hostActionBusy" @click="runHost('lock')">
              {{ t("lock", isZh) }}
            </button>
            <button type="button" class="learn-btn" :disabled="hostActionBusy" @click="runHost('reveal')">
              {{ t("revealBtn", isZh) }}
            </button>
            <button type="button" class="learn-btn" :disabled="hostActionBusy" @click="runHost('waiting')">
              {{ t("lobby", isZh) }}
            </button>
            <button type="button" class="learn-btn" @click="copyJoinLink">
              {{ copied ? t("copied", isZh) : t("copyLink", isZh) }}
            </button>
            <button type="button" class="learn-btn danger" :disabled="hostActionBusy" @click="runHost('end')">
              {{ t("end", isZh) }}
            </button>
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

          <div v-if="hostQuestionList.length" class="qid-list">
            <button
              v-for="q in hostQuestionList"
              :key="q.id"
              type="button"
              class="learn-btn sm"
              :disabled="hostActionBusy"
              @click="runHost('push', q.qid)"
            >
              {{ q.qid }}
            </button>
          </div>
        </div>
      </template>
    </section>

    <!-- Workshop -->
    <section v-if="activeTab === 'workshop'" class="learn-panel">
      <h2 class="ws-title">{{ t("workshopTitle", isZh) }}</h2>
      <p class="hint">{{ t("workshopHint", isZh) }}</p>
      <div class="learn-form row">
        <label>
          {{ t("sessionCode", isZh) }}
          <input v-model="workshopCode" maxlength="8" class="input-lg" />
        </label>
        <label>
          {{ t("workshopGroup", isZh) }}
          <select v-model.number="workshopGroup">
            <option :value="1">1</option>
            <option :value="2">2</option>
            <option :value="3">3</option>
            <option :value="4">4</option>
          </select>
        </label>
        <button type="button" class="learn-btn" @click="refreshWorkshop">{{ t("workshopRefresh", isZh) }}</button>
        <button type="button" class="learn-btn primary" :disabled="loading" @click="saveWorkshopBoard">
          {{ t("workshopSave", isZh) }}
        </button>
      </div>

      <div class="ws-grid">
        <fieldset class="ws-card">
          <legend>{{ isZh ? "任务1 迷你使用规范" : "Task 1 Use specification" }}</legend>
          <label>Users / 用户<textarea v-model="workshopDraft.task1.users" rows="2" /></label>
          <label>Environment / 环境<textarea v-model="workshopDraft.task1.environment" rows="2" /></label>
          <label>Intended use / 预期用途<textarea v-model="workshopDraft.task1.intended_use" rows="2" /></label>
          <label>POF candidates / 主要操作功能候选<textarea v-model="workshopDraft.task1.pof_candidates" rows="2" /></label>
          <label>Foreseeable misuse / 可预见误用<textarea v-model="workshopDraft.task1.foreseeable_misuse" rows="2" /></label>
        </fieldset>
        <fieldset class="ws-card">
          <legend>{{ isZh ? "任务2 用错与 HRUS" : "Task 2 Use errors & HRUS" }}</legend>
          <label>Use errors / 潜在用错 (≥5)<textarea v-model="workshopDraft.task2.use_errors" rows="3" /></label>
          <label>Summative candidates<textarea v-model="workshopDraft.task2.summative_candidates" rows="2" /></label>
          <label>Primary HRUS<textarea v-model="workshopDraft.task2.primary_hrus" rows="3" /></label>
        </fieldset>
        <fieldset class="ws-card">
          <legend>{{ isZh ? "任务3 控制措施草图" : "Task 3 Controls" }}</legend>
          <label>Inherent safety / 本质安全<textarea v-model="workshopDraft.task3.inherent_safety" rows="2" /></label>
          <label>Protective / 防护<textarea v-model="workshopDraft.task3.protective" rows="2" /></label>
          <label>Information for safety / 安全信息<textarea v-model="workshopDraft.task3.information_for_safety" rows="2" /></label>
          <label>Needs UE evaluation?<textarea v-model="workshopDraft.task3.needs_ue_eval" rows="2" /></label>
        </fieldset>
        <fieldset class="ws-card">
          <legend>{{ isZh ? "任务4 评价策略" : "Task 4 Evaluation strategy" }}</legend>
          <label>Formative needed?<textarea v-model="workshopDraft.task4.formative_needed" rows="2" /></label>
          <label>Summative needed?<textarea v-model="workshopDraft.task4.summative_needed" rows="2" /></label>
          <label>Success criteria<textarea v-model="workshopDraft.task4.success_criteria" rows="2" /></label>
          <label>Failure re-entry step<textarea v-model="workshopDraft.task4.failure_reentry" rows="2" /></label>
        </fieldset>
      </div>

      <div class="ws-others">
        <h3>{{ isZh ? "各组看板（互评）" : "All groups (peer review)" }}</h3>
        <article v-for="g in workshopGroups" :key="g.group_no" class="ws-peer">
          <header>
            <strong>{{ t("workshopGroup", isZh) }} {{ g.group_no }}</strong>
            <span class="hint">{{ g.updated_by || "—" }} · {{ g.updated_at || "" }}</span>
          </header>
          <pre class="ws-pre">{{ JSON.stringify({ t1: g.task1, t2: g.task2, t3: g.task3, t4: g.task4 }, null, 2) }}</pre>
        </article>
      </div>
    </section>

    <!-- Practice (login required) -->
    <section v-if="activeTab === 'practice'" class="learn-panel">
      <div v-if="!practiceLoggedIn" class="learn-form login-box">
        <p class="login-required">{{ t("loginRequired", isZh) }}</p>
        <p class="hint">{{ t("registerHint", isZh) }}</p>
        <button type="button" class="learn-btn primary" @click="showLoginDialog = true">
          {{ t("signIn", isZh) }}
        </button>
      </div>

      <template v-else>
        <div class="auth-bar">
          <span>{{ t("signedInAs", isZh) }}: <strong>{{ practiceUserName }}</strong></span>
          <button type="button" class="learn-btn sm" @click="doLogout">{{ t("logout", isZh) }}</button>
        </div>

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
      </template>
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
.learn-root.join-focus {
  max-width: 560px;
}
.learn-title-row {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 1rem;
  flex-wrap: wrap;
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
.learn-auth {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  flex-shrink: 0;
  margin-top: 0.25rem;
}
.learn-auth-badge {
  font-size: 0.9rem;
  color: var(--vp-c-text-2);
  max-width: 180px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
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
.learn-form select,
.input-lg {
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  padding: 0.55rem 0.7rem;
  background: var(--vp-c-bg);
  color: var(--vp-c-text-1);
  font-size: 1rem;
}
.input-lg {
  min-height: 48px;
  font-size: 1.1rem;
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
.btn-lg {
  min-height: 48px;
  font-size: 1.05rem;
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
.qr-panel {
  text-align: center;
  padding: 1.25rem 1rem;
  margin-bottom: 1.25rem;
  border: 1px solid var(--vp-c-divider);
  border-radius: 14px;
  background: var(--vp-c-bg-soft);
}
.qr-title {
  margin: 0 0 0.75rem;
  font-weight: 650;
}
.qr-img {
  display: block;
  margin: 0 auto;
  width: min(280px, 70vw);
  height: auto;
  background: #fff;
  border-radius: 8px;
  padding: 8px;
}
.code-under-qr {
  margin-top: 0.85rem;
  font-size: clamp(1.8rem, 6vw, 2.4rem);
  font-weight: 750;
  letter-spacing: 0.18em;
  font-variant-numeric: tabular-nums;
}
.join-url-line {
  font-size: 0.75rem;
  color: var(--vp-c-text-3);
  word-break: break-all;
  margin: 0.35rem 0 0;
}
.join-banner {
  padding: 0.65rem 0.8rem;
  border-radius: 8px;
  background: var(--vp-c-brand-soft);
  margin: 0 0 0.75rem;
}
.enter-code-hint {
  margin: 0 0 0.75rem;
}
.code-lg {
  font-size: 1.25rem;
  letter-spacing: 0.12em;
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
  padding: 0.85rem 0.9rem;
  background: var(--vp-c-bg);
  color: var(--vp-c-text-1);
  cursor: pointer;
  min-height: 48px;
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
.login-box {
  border: 1px solid var(--vp-c-divider);
  border-radius: 12px;
  padding: 1rem;
}
.login-required {
  margin: 0;
  font-weight: 650;
}
.auth-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 0.75rem;
  margin-bottom: 1rem;
  flex-wrap: wrap;
}
.ws-title { margin: 0 0 0.35rem; font-size: 1.25rem; }
.ws-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.75rem;
  margin: 1rem 0;
}
.ws-card {
  border: 1px solid var(--vp-c-divider);
  border-radius: 10px;
  padding: 0.65rem 0.75rem 0.85rem;
  margin: 0;
}
.ws-card legend { padding: 0 0.35rem; font-weight: 650; }
.ws-card label {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
  font-size: 0.85rem;
  margin-top: 0.45rem;
}
.ws-card textarea {
  width: 100%;
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  padding: 0.45rem 0.55rem;
  font: inherit;
  background: var(--vp-c-bg);
  color: var(--vp-c-text-1);
  resize: vertical;
}
.ws-others { margin-top: 1.25rem; }
.ws-peer {
  border: 1px solid var(--vp-c-divider);
  border-radius: 10px;
  padding: 0.65rem 0.75rem;
  margin-bottom: 0.65rem;
}
.ws-peer header {
  display: flex;
  justify-content: space-between;
  gap: 0.5rem;
  flex-wrap: wrap;
  margin-bottom: 0.35rem;
}
.ws-pre {
  margin: 0;
  white-space: pre-wrap;
  word-break: break-word;
  font-size: 0.78rem;
  line-height: 1.35;
  max-height: 220px;
  overflow: auto;
  background: var(--vp-c-bg-soft);
  padding: 0.5rem;
  border-radius: 8px;
}
@media (max-width: 900px) {
  .ws-grid { grid-template-columns: 1fr; }
}
@media (max-width: 640px) {
  .learn-form.row {
    grid-template-columns: 1fr;
  }
  .learn-header h1 {
    font-size: 1.4rem;
  }
  .learn-tabs {
    position: sticky;
    top: 0;
    z-index: 5;
    background: var(--vp-c-bg);
    padding: 0.35rem 0;
  }
}
</style>
