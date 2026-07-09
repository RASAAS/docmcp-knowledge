<script setup lang="ts">
import { ref, computed, onMounted } from "vue";
import { useData } from "vitepress";
import FeatureBoard from "./FeatureBoard.vue";
import DiscussionWall from "./DiscussionWall.vue";
import { isLoggedIn, loginWithToken, logout, verifyAuth } from "./HubApi";

const { lang } = useData();
const isZh = computed(() => lang.value === "zh" || lang.value === "zh-CN");

const activeTab = ref<"features" | "discussions" | "roadmap">("features");
const loggedIn = ref(false);
const showLoginDialog = ref(false);
const loginToken = ref("");
const loginError = ref("");
const loginLoading = ref(false);

const tabs = computed(() => [
  {
    key: "features" as const,
    label: isZh.value ? "功能建议" : "Feature Board",
    icon: "M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z",
  },
  {
    key: "discussions" as const,
    label: isZh.value ? "讨论区" : "Discussions",
    icon: "M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z",
  },
  {
    key: "roadmap" as const,
    label: isZh.value ? "路线图" : "Roadmap",
    icon: "M9 20l-5.447-2.724A1 1 0 013 16.382V5.618a1 1 0 011.447-.894L9 7m0 13l6-3m-6 3V7m6 10l4.553 2.276A1 1 0 0021 18.382V7.618a1 1 0 00-.553-.894L15 4m0 13V4m0 0L9 7",
  },
]);

async function checkLogin() {
  loggedIn.value = isLoggedIn();
  if (loggedIn.value) {
    try {
      const token = typeof window !== "undefined" ? localStorage.getItem("reguverse_hub_token") : null;
      if (token) {
        const result = await verifyAuth(token);
        if (result.verified) {
          userName.value = result.display_name || "";
        } else {
          logout();
          loggedIn.value = false;
        }
      }
    } catch {
      // keep as logged in, name unknown
    }
  }
}

const userName = ref("");

async function doLogin() {
  const token = loginToken.value.trim();
  if (!token) return;
  loginLoading.value = true;
  loginError.value = "";
  try {
    const result = await verifyAuth(token);
    if (!result.verified) {
      loginError.value = isZh.value ? "Token 无效或已过期" : "Invalid or expired token";
      return;
    }
    loginWithToken(token);
    loggedIn.value = true;
    userName.value = result.display_name || "";
    showLoginDialog.value = false;
    loginToken.value = "";
  } catch {
    loginError.value = isZh.value ? "验证失败，请重试" : "Verification failed, please retry";
  } finally {
    loginLoading.value = false;
  }
}

function doLogout() {
  logout();
  loggedIn.value = false;
}

onMounted(checkLogin);
</script>

<template>
  <div class="rv-hub">
    <header class="rv-hub-header">
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

    <!-- Login Dialog -->
    <div v-if="showLoginDialog" class="rv-login-overlay" @click.self="showLoginDialog = false">
      <div class="rv-login-dialog">
        <h3 class="rv-login-title">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--vp-c-brand-1)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/>
          </svg>
          {{ isZh ? "Reguverse 用户验证" : "Verify Reguverse Account" }}
        </h3>
        <p class="rv-login-desc">
          {{ isZh
            ? "输入您的 Reguverse 账户 JWT Token 以获得 Verified 身份标识。您可以在 Reguverse Assistant 插件的 Account 页面找到您的 Token。"
            : "Enter your Reguverse JWT Token to get a Verified badge. You can find your Token on the Account page of the Reguverse Assistant plugin." }}
        </p>
        <input
          v-model="loginToken"
          type="password"
          :placeholder="isZh ? '粘贴您的 JWT Token...' : 'Paste your JWT Token...'"
          class="rv-login-input"
          @keydown.enter="doLogin"
        />
        <div v-if="loginError" class="rv-login-error">{{ loginError }}</div>
        <div class="rv-login-actions">
          <button class="rv-login-cancel" @click="showLoginDialog = false; loginError = ''">
            {{ isZh ? "取消" : "Cancel" }}
          </button>
          <button class="rv-login-submit" :disabled="loginLoading || !loginToken.trim()" @click="doLogin">
            {{ loginLoading ? (isZh ? "验证中..." : "Verifying...") : (isZh ? "验证" : "Verify") }}
          </button>
        </div>
        <p class="rv-login-note">
          {{ isZh
            ? "未注册？无需登录也可以参与讨论和投票。验证后可获得 Verified 标识。"
            : "Not registered? You can participate without logging in. Verification gives you a Verified badge." }}
        </p>
      </div>
    </div>

    <nav class="rv-hub-tabs">
      <div class="rv-hub-tabs-inner">
        <button
          v-for="tab in tabs"
          :key="tab.key"
          class="rv-hub-tab"
          :class="{ active: activeTab === tab.key }"
          @click="activeTab = tab.key"
        >
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
            <path :d="tab.icon"/>
          </svg>
          {{ tab.label }}
        </button>
      </div>
    </nav>

    <main class="rv-hub-content">
      <div v-if="activeTab === 'features'" class="rv-hub-panel">
        <FeatureBoard />
      </div>
      <div v-else-if="activeTab === 'discussions'" class="rv-hub-panel">
        <DiscussionWall />
      </div>
      <div v-else class="rv-hub-panel rv-hub-roadmap">
        <div class="rv-roadmap-placeholder">
          <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="var(--vp-c-text-3)" stroke-width="1" stroke-linecap="round" stroke-linejoin="round">
            <path d="M9 20l-5.447-2.724A1 1 0 013 16.382V5.618a1 1 0 011.447-.894L9 7m0 13l6-3m-6 3V7m6 10l4.553 2.276A1 1 0 0021 18.382V7.618a1 1 0 00-.553-.894L15 4m0 13V4m0 0L9 7"/>
          </svg>
          <h3>{{ isZh ? "产品路线图" : "Product Roadmap" }}</h3>
          <p>{{ isZh ? "即将推出 -- 查看我们的开发计划和已完成的功能。" : "Coming soon -- view our development plans and completed features." }}</p>
        </div>
      </div>
    </main>
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
  padding: 40px 24px 32px;
}
.rv-hub-header-inner {
  max-width: 1200px;
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
  gap: 8px;
}
.rv-hub-title {
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 28px;
  font-weight: 700;
  margin: 0;
  color: white;
  letter-spacing: -0.5px;
}
.rv-hub-subtitle {
  margin: 0;
  font-size: 16px;
  opacity: 0.9;
}

.rv-hub-tabs {
  position: sticky;
  top: var(--vp-nav-height, 64px);
  z-index: 10;
  background: var(--vp-c-bg);
  border-bottom: 1px solid var(--vp-c-divider);
  padding: 0 24px;
}
.rv-hub-tabs-inner {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  gap: 4px;
}
.rv-hub-tab {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 14px 20px;
  border: none;
  background: none;
  color: var(--vp-c-text-2);
  font-size: 15px;
  font-weight: 500;
  cursor: pointer;
  border-bottom: 2px solid transparent;
  transition: all 0.2s;
  white-space: nowrap;
}
.rv-hub-tab:hover {
  color: var(--vp-c-text-1);
  background: var(--vp-c-bg-soft);
}
.rv-hub-tab.active {
  color: var(--vp-c-brand-1);
  border-bottom-color: var(--vp-c-brand-1);
}

.rv-hub-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 24px;
}

.rv-hub-roadmap {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 300px;
}
.rv-roadmap-placeholder {
  text-align: center;
  color: var(--vp-c-text-3);
}
.rv-roadmap-placeholder h3 {
  margin: 16px 0 8px;
  font-size: 20px;
  color: var(--vp-c-text-2);
}
.rv-roadmap-placeholder p {
  margin: 0;
  font-size: 15px;
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

/* Login Dialog */
.rv-login-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0,0,0,0.5);
  z-index: 100;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
}
.rv-login-dialog {
  background: var(--vp-c-bg);
  border-radius: 16px;
  padding: 32px;
  max-width: 460px;
  width: 100%;
  box-shadow: 0 20px 60px rgba(0,0,0,0.3);
}
.rv-login-title {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 18px;
  font-weight: 600;
  margin: 0 0 12px;
  color: var(--vp-c-text-1);
}
.rv-login-desc {
  font-size: 14px;
  color: var(--vp-c-text-2);
  line-height: 1.6;
  margin: 0 0 16px;
}
.rv-login-input {
  width: 100%;
  padding: 10px 14px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  font-size: 14px;
  background: var(--vp-c-bg-soft);
  color: var(--vp-c-text-1);
  font-family: monospace;
  box-sizing: border-box;
}
.rv-login-input:focus {
  border-color: var(--vp-c-brand-1);
  outline: none;
}
.rv-login-error {
  color: var(--vp-c-danger-1);
  font-size: 13px;
  margin-top: 8px;
}
.rv-login-actions {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
  margin-top: 20px;
}
.rv-login-cancel {
  padding: 8px 20px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  background: var(--vp-c-bg);
  color: var(--vp-c-text-2);
  cursor: pointer;
  font-size: 14px;
}
.rv-login-cancel:hover {
  border-color: var(--vp-c-text-3);
}
.rv-login-submit {
  padding: 8px 24px;
  border: none;
  border-radius: 8px;
  background: var(--vp-c-brand-1);
  color: white;
  cursor: pointer;
  font-size: 14px;
  font-weight: 500;
}
.rv-login-submit:hover {
  background: var(--vp-c-brand-2);
}
.rv-login-submit:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
.rv-login-note {
  font-size: 12px;
  color: var(--vp-c-text-3);
  margin: 16px 0 0;
  line-height: 1.5;
}

@media (max-width: 768px) {
  .rv-hub-header {
    padding: 24px 16px 20px;
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
  .rv-hub-auth {
    margin-top: 4px;
  }
  .rv-hub-tabs {
    padding: 0 16px;
    overflow-x: auto;
  }
  .rv-hub-tab {
    padding: 12px 14px;
    font-size: 14px;
  }
  .rv-hub-content {
    padding: 16px;
  }
  .rv-login-dialog {
    padding: 24px;
  }
}
</style>
