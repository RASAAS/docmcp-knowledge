<script setup lang="ts">
/**
 * Blank user-designed workshop boards (no built-in case templates).
 * Host creates groups; members fill freeform sections.
 */
import { computed, onMounted, onUnmounted, ref, watch } from "vue";
import {
  createWorkshopGroup,
  deleteWorkshopGroup,
  ensureParticipantKey,
  getWorkshop,
  updateWorkshopGroup,
  type WorkshopGroup,
  type WorkshopSection,
} from "./LearnApi";
import { t } from "./LearnNavData";

const props = defineProps<{
  isZh: boolean;
  sessionCode: string;
  hostToken: string;
  editorName: string;
  participantKey: string;
}>();

const emit = defineEmits<{
  error: [message: string];
}>();

const code = ref("");
const groups = ref<WorkshopGroup[]>([]);
const activeGroupId = ref<number | null>(null);
const newGroupName = ref("");
const loading = ref(false);
const draftName = ref("");
const draftSections = ref<WorkshopSection[]>([]);
/** Prevent poll/refresh from wiping in-progress edits */
const draftDirty = ref(false);
let pollTimer: ReturnType<typeof setInterval> | null = null;
let applyingRemote = false;

const activeGroup = computed(() => groups.value.find((g) => g.id === activeGroupId.value) || null);
const isHost = computed(() => !!props.hostToken);

function stopPoll() {
  if (pollTimer) {
    clearInterval(pollTimer);
    pollTimer = null;
  }
}

function markDirty() {
  if (!applyingRemote) draftDirty.value = true;
}

function loadDraft(g: WorkshopGroup | null) {
  applyingRemote = true;
  if (!g) {
    draftName.value = "";
    draftSections.value = [];
  } else {
    draftName.value = g.name;
    draftSections.value = g.sections.map((s) => ({ ...s }));
  }
  draftDirty.value = false;
  applyingRemote = false;
}

async function refresh(opts?: { forceDraft?: boolean }) {
  const c = (code.value || props.sessionCode || "").trim().toUpperCase();
  if (!c) return;
  code.value = c;
  try {
    const res = await getWorkshop(c);
    groups.value = res.groups;

    if (activeGroupId.value == null && res.groups.length) {
      activeGroupId.value = res.groups[0].id;
      if (!draftDirty.value || opts?.forceDraft) loadDraft(res.groups[0]);
      return;
    }

    const cur = res.groups.find((g) => g.id === activeGroupId.value);
    if (!cur) {
      if (res.groups.length) {
        activeGroupId.value = res.groups[0].id;
        if (!draftDirty.value || opts?.forceDraft) loadDraft(res.groups[0]);
      } else {
        activeGroupId.value = null;
        loadDraft(null);
      }
      return;
    }

    // Keep local unsaved edits; only refresh draft when clean or forced
    if (!draftDirty.value || opts?.forceDraft) {
      loadDraft(cur);
    }
  } catch (e) {
    emit("error", e instanceof Error ? e.message : t("error", props.isZh));
  }
}

async function addGroup() {
  if (!isHost.value) {
    emit("error", t("workshopHostOnly", props.isZh));
    return;
  }
  const c = code.value.trim().toUpperCase();
  if (!c) {
    emit("error", t("workshopNeedCode", props.isZh));
    return;
  }
  loading.value = true;
  try {
    const res = await createWorkshopGroup(c, {
      name:
        newGroupName.value.trim() ||
        (props.isZh ? `第 ${groups.value.length + 1} 组` : `Group ${groups.value.length + 1}`),
      host_token: props.hostToken,
    });
    groups.value = res.groups;
    newGroupName.value = "";
    if (res.groups.length) {
      activeGroupId.value = res.groups[res.groups.length - 1].id;
      loadDraft(res.groups[res.groups.length - 1]);
    }
  } catch (e) {
    emit("error", e instanceof Error ? e.message : t("error", props.isZh));
  } finally {
    loading.value = false;
  }
}

async function removeGroup(id: number) {
  if (!isHost.value) {
    emit("error", t("workshopHostOnly", props.isZh));
    return;
  }
  loading.value = true;
  try {
    const res = await deleteWorkshopGroup(code.value, id, props.hostToken);
    groups.value = res.groups;
    if (activeGroupId.value === id) {
      activeGroupId.value = res.groups[0]?.id ?? null;
      loadDraft(res.groups[0] || null);
    }
  } catch (e) {
    emit("error", e instanceof Error ? e.message : t("error", props.isZh));
  } finally {
    loading.value = false;
  }
}

function addSection() {
  const id = `s${Date.now().toString(36)}${Math.random().toString(36).slice(2, 6)}`;
  draftSections.value = [...draftSections.value, { id, title: "", body: "" }];
  markDirty();
}

function removeSection(sid: string) {
  draftSections.value = draftSections.value.filter((s) => s.id !== sid);
  markDirty();
}

async function saveActive() {
  if (!activeGroupId.value) return;
  const c = code.value.trim().toUpperCase();
  if (!c) {
    emit("error", t("workshopNeedCode", props.isZh));
    return;
  }
  loading.value = true;
  try {
    const res = await updateWorkshopGroup(c, activeGroupId.value, {
      name: draftName.value.trim(),
      sections: draftSections.value,
      updated_by: props.editorName || "editor",
      participant_key: props.participantKey || ensureParticipantKey(),
      host_token: props.hostToken || undefined,
    });
    groups.value = res.groups;
    const cur = res.groups.find((g) => g.id === activeGroupId.value);
    loadDraft(cur || null);
  } catch (e) {
    emit("error", e instanceof Error ? e.message : t("error", props.isZh));
  } finally {
    loading.value = false;
  }
}

watch(
  () => props.sessionCode,
  (v) => {
    if (v) {
      code.value = v.trim().toUpperCase();
      refresh({ forceDraft: !draftDirty.value });
    }
  }
);

watch(activeGroupId, (id, prev) => {
  if (id === prev) return;
  // Switching groups: discard dirty draft for previous group (explicit selection)
  const g = groups.value.find((x) => x.id === id) || null;
  loadDraft(g);
});

watch(draftName, () => markDirty());

onMounted(() => {
  code.value = (props.sessionCode || "").trim().toUpperCase();
  refresh({ forceDraft: true });
  // Poll peer boards; never wipe unsaved local draft
  pollTimer = setInterval(() => refresh(), 5000);
});

onUnmounted(stopPoll);
</script>

<template>
  <section class="learn-workshop">
    <h2 class="ws-title">{{ t("workshopTitle", isZh) }}</h2>
    <p class="hint">{{ t("workshopHint", isZh) }}</p>

    <div class="learn-form row">
      <label>
        {{ t("sessionCode", isZh) }}
        <input v-model="code" maxlength="8" class="input-lg" @change="refresh({ forceDraft: true })" />
      </label>
      <button type="button" class="learn-btn" @click="refresh({ forceDraft: !draftDirty })">
        {{ t("workshopRefresh", isZh) }}
      </button>
    </div>

    <div v-if="isHost" class="ws-host-create">
      <input
        v-model="newGroupName"
        maxlength="80"
        :placeholder="t('workshopGroupNamePh', isZh)"
      />
      <button type="button" class="learn-btn primary" :disabled="loading || !code" @click="addGroup">
        {{ t("workshopAddGroup", isZh) }}
      </button>
    </div>
    <p v-else class="hint">{{ t("workshopMemberHint", isZh) }}</p>

    <p v-if="draftDirty" class="ws-dirty">{{ t("workshopUnsaved", isZh) }}</p>

    <div v-if="!groups.length" class="ws-empty">
      {{ t("workshopEmpty", isZh) }}
    </div>

    <div v-else class="ws-layout">
      <aside class="ws-side">
        <button
          v-for="g in groups"
          :key="g.id"
          type="button"
          class="ws-side-item"
          :class="{ active: g.id === activeGroupId }"
          @click="activeGroupId = g.id"
        >
          <span>{{ g.name || `${t("workshopGroup", isZh)} ${g.sort_order}` }}</span>
          <button
            v-if="isHost"
            type="button"
            class="ws-del"
            :title="t('workshopDeleteGroup', isZh)"
            @click.stop="removeGroup(g.id)"
          >
            ×
          </button>
        </button>
      </aside>

      <div v-if="activeGroup" class="ws-editor">
        <label>
          {{ t("workshopGroupName", isZh) }}
          <input v-model="draftName" maxlength="80" @input="markDirty" />
        </label>

        <div v-for="(sec, idx) in draftSections" :key="sec.id" class="ws-section">
          <div class="ws-section-head">
            <strong>{{ t("workshopSection", isZh) }} {{ idx + 1 }}</strong>
            <button type="button" class="learn-btn sm" @click="removeSection(sec.id)">
              {{ t("workshopRemoveSection", isZh) }}
            </button>
          </div>
          <input
            v-model="sec.title"
            maxlength="120"
            :placeholder="t('workshopSectionTitlePh', isZh)"
            @input="markDirty"
          />
          <textarea
            v-model="sec.body"
            rows="4"
            :placeholder="t('workshopSectionBodyPh', isZh)"
            @input="markDirty"
          />
        </div>

        <div class="ws-actions">
          <button type="button" class="learn-btn" @click="addSection">
            {{ t("workshopAddSection", isZh) }}
          </button>
          <button type="button" class="learn-btn primary" :disabled="loading" @click="saveActive">
            {{ t("workshopSave", isZh) }}
          </button>
        </div>

        <p v-if="activeGroup.updated_at" class="hint">
          {{ activeGroup.updated_by || "—" }} · {{ activeGroup.updated_at }}
        </p>
      </div>
    </div>

    <div v-if="groups.length" class="ws-others">
      <h3>{{ t("workshopPeerTitle", isZh) }}</h3>
      <article v-for="g in groups" :key="`peer-${g.id}`" class="ws-peer">
        <header>
          <strong>{{ g.name }}</strong>
          <span class="hint">{{ g.updated_by || "—" }} · {{ g.updated_at || "" }}</span>
        </header>
        <div v-if="!g.sections.length" class="hint">{{ t("workshopNoContent", isZh) }}</div>
        <div v-for="s in g.sections" :key="s.id" class="ws-peer-sec">
          <strong>{{ s.title || "—" }}</strong>
          <pre class="ws-pre">{{ s.body || "" }}</pre>
        </div>
      </article>
    </div>
  </section>
</template>

<style scoped>
.learn-workshop {
  display: grid;
  gap: 0.85rem;
}
.ws-title {
  margin: 0;
  font-size: 1.25rem;
}
.hint {
  color: var(--vp-c-text-2);
  font-size: 0.9rem;
  margin: 0;
}
.ws-dirty {
  margin: 0;
  font-size: 0.85rem;
  color: #b54708;
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
.input-lg,
.ws-host-create input,
.ws-editor input,
.ws-editor textarea {
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  padding: 0.55rem 0.7rem;
  background: var(--vp-c-bg);
  color: var(--vp-c-text-1);
  font: inherit;
  width: 100%;
  box-sizing: border-box;
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
.learn-btn.sm {
  padding: 0.3rem 0.55rem;
  font-size: 0.85rem;
}
.learn-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
.ws-host-create {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
}
.ws-host-create input {
  flex: 1;
  min-width: 180px;
}
.ws-empty {
  padding: 1.5rem;
  border: 1px dashed var(--vp-c-divider);
  border-radius: 12px;
  text-align: center;
  color: var(--vp-c-text-2);
}
.ws-layout {
  display: grid;
  grid-template-columns: 200px 1fr;
  gap: 0.85rem;
}
.ws-side {
  display: grid;
  gap: 0.35rem;
  align-content: start;
}
.ws-side-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 0.35rem;
  text-align: left;
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  padding: 0.45rem 0.55rem;
  background: var(--vp-c-bg-soft);
  color: var(--vp-c-text-1);
  cursor: pointer;
}
.ws-side-item.active {
  border-color: var(--vp-c-brand-1);
  background: var(--vp-c-brand-soft);
}
.ws-del {
  border: none;
  background: transparent;
  color: #b42318;
  cursor: pointer;
  font-size: 1.1rem;
  line-height: 1;
}
.ws-editor {
  display: grid;
  gap: 0.75rem;
  border: 1px solid var(--vp-c-divider);
  border-radius: 12px;
  padding: 0.85rem;
}
.ws-editor label {
  display: grid;
  gap: 0.35rem;
  font-size: 0.92rem;
}
.ws-section {
  display: grid;
  gap: 0.4rem;
  padding: 0.65rem;
  border: 1px solid var(--vp-c-divider);
  border-radius: 10px;
  background: var(--vp-c-bg-soft);
}
.ws-section-head {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.ws-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}
.ws-others {
  margin-top: 0.5rem;
}
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
.ws-peer-sec {
  margin-top: 0.45rem;
}
.ws-pre {
  margin: 0.25rem 0 0;
  white-space: pre-wrap;
  word-break: break-word;
  font-size: 0.85rem;
  line-height: 1.4;
  max-height: 180px;
  overflow: auto;
  background: var(--vp-c-bg-soft);
  padding: 0.5rem;
  border-radius: 8px;
}
@media (max-width: 720px) {
  .ws-layout {
    grid-template-columns: 1fr;
  }
  .learn-form.row {
    grid-template-columns: 1fr;
  }
}
</style>
