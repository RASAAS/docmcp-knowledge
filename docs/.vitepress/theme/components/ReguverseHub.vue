<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted } from "vue";
import { useData } from "vitepress";
import FeatureBoard from "./FeatureBoard.vue";
import HubBillboard from "./HubBillboard.vue";
import DiscussionWall from "./DiscussionWall.vue";
import AdminPanel from "./AdminPanel.vue";
import ServiceMarketCta from "./ServiceMarketCta.vue";
import HubSidebar from "./HubSidebar.vue";
import HubRoadmap from "./HubRoadmap.vue";
import { hubLabel, HUB_TABS, HUB_ADMIN_TAB, type HubTabKey } from "./HubNavData";
import { isLoggedIn, getDisplayName, getUserRole, logout, saveSession, verifyAuth } from "./HubApi";
import HubOtpLogin from "./HubOtpLogin.vue";

const { lang } = useData();
const isZh = computed(() => lang.value === "zh" || lang.value === "zh-CN");

const isEmbedMode = ref(false);
const mobileNavOpen = ref(false);

const activeTab = ref<HubTabKey>("features");
const featureCategory = ref("");
const discussionCategory = ref("");

const loggedIn = ref(false);
const showLoginDialog = ref(false);

const userName = ref("");
const userRole = ref("");
const isAdminUser = computed(() => ["admin", "super_admin"].includes(userRole.value));

const activeTabLabel = computed(() => {
  const all = isAdminUser.value ? [...HUB_TABS, HUB_ADMIN_TAB] : HUB_TABS;
  const tab = all.find((t) => t.key === activeTab.value);
  return tab ? hubLabel(tab, isZh.value) : "";
});

function onLoginSuccess(payload: { displayName: string; role?: string }) {
  loggedIn.value = true;
  userName.value = payload.displayName || getDisplayName() || "";
  userRole.value = payload.role || getUserRole();
  showLoginDialog.value = false;
}

function doLogout() {
  logout();
  loggedIn.value = false;
  userName.value = "";
  userRole.value = "";
  showLoginDialog.value = false;
  if (activeTab.value === "admin") activeTab.value = "features";
}

async function checkLogin() {
  loggedIn.value = isLoggedIn();
  if (loggedIn.value) {
    userName.value = getDisplayName();
    userRole.value = getUserRole();
    try {
      const result = await verifyAuth();
      if (result.verified) {
        userName.value = result.display_name || userName.value;
        userRole.value = (result as Record<string, unknown>).role as string || userRole.value;
      } else {
        logout();
        loggedIn.value = false;
        userName.value = "";
        userRole.value = "";
      }
    } catch {
      // keep as logged in with cached name
    }
  }
}

const ALLOWED_EMBED_ORIGINS = [
  "https://app.team-ra.org",
  "https://app-test.team-ra.org",
  "https://app.reguverse.com",
  "https://app-test.reguverse.com",
  "https://localhost:3003",
  "https://localhost:3000",
];

function handlePostMessage(event: MessageEvent) {
  if (!isEmbedMode.value) return;
  if (!ALLOWED_EMBED_ORIGINS.includes(event.origin)) return;
  const data = event.data;
  if (data?.type === "reguverse-hub-sso" && data.hub_token) {
    saveSession(
      data.hub_token,
      data.display_name || "",
      data.user_id,
      data.role,
    );
    loggedIn.value = true;
    userName.value = data.display_name || "";
    userRole.value = data.role || "";
  }
}

function setHubPageClass(on: boolean) {
  if (typeof document === "undefined") return;
  document.documentElement.classList.toggle("hub-page-active", on);
}

onMounted(() => {
  if (typeof window !== "undefined") {
    const params = new URLSearchParams(window.location.search);
    if (params.get("embed") === "true") {
      isEmbedMode.value = true;
      document.documentElement.classList.add("hub-embed-mode");
    } else {
      setHubPageClass(true);
    }
    window.addEventListener("message", handlePostMessage);
  }
  checkLogin();
});

onUnmounted(() => {
  if (typeof window !== "undefined") {
    window.removeEventListener("message", handlePostMessage);
    document.documentElement.classList.remove("hub-embed-mode");
    setHubPageClass(false);
  }
});
</script>

<template>
  <div class="rv-hub" :class="{ 'rv-hub-embed': isEmbedMode }">
    <header v-if="!isEmbedMode" class="rv-hub-header">
      <div class="rv-hub-header-inner">
        <div class="rv-hub-title-row">
          <div class="rv-hub-title-left">
            <h1 class="rv-hub-title">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                <path d="M12 2L2 7l10 5 10-5-10-5z"/>
                <path d="M2 17l10 5 10-5"/>
                <path d="M2 12l10 5 10-5"/>
              </svg>
              Reguverse Hub
            </h1>
            <p class="rv-hub-subtitle">
              {{ isZh ? "RA 专业人士共建的社区平台" : "Community-driven platform for RA professionals" }}
            </p>
          </div>
          <div class="rv-hub-auth">
            <template v-if="loggedIn">
              <span class="rv-hub-auth-badge">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                {{ userName || (isZh ? "已验证" : "Verified") }}
              </span>
              <button class="rv-hub-auth-btn rv-hub-auth-logout" @click="doLogout">
                {{ isZh ? "退出" : "Logout" }}
              </button>
            </template>
            <template v-else>
              <button class="rv-hub-auth-btn" @click="showLoginDialog = true">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M15 3h4a2 2 0 012 2v14a2 2 0 01-2 2h-4M10 17l5-5-5-5M15 12H3"/>
                </svg>
                {{ isZh ? "Reguverse 用户验证" : "Verify Reguverse Account" }}
              </button>
            </template>
          </div>
        </div>
      </div>
    </header>

    <div v-if="isEmbedMode" class="rv-hub-embed-bar">
      <template v-if="loggedIn">
        <span class="rv-embed-badge">
          <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor"><path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
          {{ userName || (isZh ? "已验证" : "Verified") }}
        </span>
      </template>
      <template v-else>
        <span class="rv-embed-hint">{{ isZh ? "未登录 -- 以访客身份参与" : "Guest mode" }}</span>
      </template>
    </div>

    <HubOtpLogin
      :open="showLoginDialog"
      :is-zh="isZh"
      variant="hub"
      @close="showLoginDialog = false"
      @success="onLoginSuccess"
    />

    <div class="rv-hub-body">
      <div
        v-if="mobileNavOpen"
        class="hub-side-backdrop"
        @click="mobileNavOpen = false"
      />

      <HubSidebar
        v-model:active-tab="activeTab"
        v-model:feature-category="featureCategory"
        v-model:discussion-category="discussionCategory"
        :show-admin="isAdminUser"
        :mobile-open="mobileNavOpen"
        @close-mobile="mobileNavOpen = false"
      />

      <div class="rv-hub-main">
        <div class="rv-hub-mobile-bar">
          <button type="button" class="rv-hub-menu-btn" @click="mobileNavOpen = !mobileNavOpen">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round">
              <path d="M4 6h16M4 12h16M4 18h16"/>
            </svg>
            {{ activeTabLabel }}
          </button>
        </div>

        <ServiceMarketCta v-if="!isEmbedMode" />

        <main class="rv-hub-content">
          <div v-if="activeTab === 'features'" class="rv-hub-panel">
            <FeatureBoard :category="featureCategory" />
          </div>
          <div v-else-if="activeTab === 'billboard'" class="rv-hub-panel">
            <HubBillboard :category="featureCategory" />
          </div>
          <div v-else-if="activeTab === 'discussions'" class="rv-hub-panel">
            <DiscussionWall :category="discussionCategory" />
          </div>
          <div v-else-if="activeTab === 'roadmap'" class="rv-hub-panel rv-hub-roadmap">
            <HubRoadmap />
          </div>
          <div v-else-if="activeTab === 'admin' && isAdminUser" class="rv-hub-panel rv-hub-admin">
            <AdminPanel />
          </div>
        </main>
      </div>
    </div>
  </div>
</template>

<style scoped>
.rv-hub {
  min-height: calc(100vh - var(--vp-nav-height, 64px));
  background: var(--vp-c-bg);
  position: relative;
  z-index: 1;
}

.rv-hub-header {
  background: linear-gradient(135deg, var(--vp-c-brand-1), var(--vp-c-brand-2));
  color: white;
  padding: 28px 24px 22px;
}
.rv-hub-header-inner {
  max-width: 1400px;
  margin: 0 auto;
}
.rv-hub-title-row {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 16px;
}
.rv-hub-title-left {
  display: flex;
  flex-direction: column;
  gap: 6px;
}
.rv-hub-title {
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 26px;
  font-weight: 700;
  margin: 0;
  color: white;
  letter-spacing: -0.5px;
}
.rv-hub-subtitle {
  margin: 0;
  font-size: 15px;
  opacity: 0.9;
}

.rv-hub-body {
  display: flex;
  align-items: stretch;
  width: 100%;
  min-height: calc(100vh - var(--vp-nav-height, 64px) - 120px);
  position: relative;
}

.rv-hub-main {
  flex: 1;
  min-width: 0;
  display: flex;
  flex-direction: column;
  max-width: 1100px;
}

.rv-hub-content {
  padding: 16px 24px 32px;
}

.hub-side-backdrop {
  display: none;
}

.rv-hub-mobile-bar {
  display: none;
  padding: 10px 16px 0;
}

.rv-hub-menu-btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 8px 12px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  background: var(--vp-c-bg-soft);
  color: var(--vp-c-text-1);
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
}

/* Auth */
.rv-hub-auth {
  display: flex;
  align-items: center;
  gap: 10px;
  flex-shrink: 0;
}
.rv-hub-auth-badge {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  padding: 5px 12px;
  border-radius: 20px;
  background: rgba(255,255,255,0.2);
  color: white;
  font-size: 13px;
  font-weight: 500;
}
.rv-hub-auth-btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 7px 16px;
  border: 1.5px solid rgba(255,255,255,0.5);
  border-radius: 8px;
  background: rgba(255,255,255,0.1);
  color: white;
  font-size: 13px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
  white-space: nowrap;
}
.rv-hub-auth-btn:hover {
  background: rgba(255,255,255,0.2);
  border-color: rgba(255,255,255,0.8);
}
.rv-hub-auth-logout {
  padding: 5px 12px;
  font-size: 12px;
  opacity: 0.8;
}
.rv-hub-auth-logout:hover {
  opacity: 1;
}

/* Embed mode */
.rv-hub-embed {
  min-height: auto;
}
.rv-hub-embed .rv-hub-body {
  min-height: auto;
}
.rv-hub-embed :deep(.hub-side) {
  top: 0;
  height: 100vh;
}
.rv-hub-embed-bar {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  padding: 6px 16px;
  background: var(--vp-c-bg-soft);
  border-bottom: 1px solid var(--vp-c-divider);
  min-height: 28px;
}
.rv-embed-badge {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 2px 10px;
  border-radius: 12px;
  background: rgba(12, 206, 107, 0.12);
  color: #0cce6b;
  font-size: 12px;
  font-weight: 500;
}
.rv-embed-hint {
  font-size: 12px;
  color: var(--vp-c-text-3);
}

@media (max-width: 960px) {
  .hub-side-backdrop {
    display: block;
    position: fixed;
    inset: 0;
    top: var(--vp-nav-height, 64px);
    background: rgba(0, 0, 0, 0.35);
    z-index: 35;
  }
  .rv-hub-mobile-bar {
    display: block;
  }
  .rv-hub-content {
    padding: 12px 16px 24px;
  }
}

@media (max-width: 768px) {
  .rv-hub-header {
    padding: 20px 16px 16px;
  }
  .rv-hub-title-row {
    flex-direction: column;
  }
  .rv-hub-title {
    font-size: 22px;
  }
  .rv-hub-subtitle {
    font-size: 14px;
  }
}
</style>
