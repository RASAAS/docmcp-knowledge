<script setup lang="ts">
import { ref, computed, onMounted } from "vue";
import { useData } from "vitepress";
import FeatureBoard from "./FeatureBoard.vue";
import DiscussionWall from "./DiscussionWall.vue";
import { isLoggedIn, getDisplayName, saveSession, logout, sendOtp, verifyOtp, verifyAuth } from "./HubApi";

const { lang } = useData();
const isZh = computed(() => lang.value === "zh" || lang.value === "zh-CN");

const activeTab = ref<"features" | "discussions" | "roadmap">("features");
const loggedIn = ref(false);
const showLoginDialog = ref(false);
const loginStep = ref<"email" | "code">("email");
const loginEmail = ref("");
const loginCode = ref("");
const loginError = ref("");
const loginLoading = ref(false);
const otpSent = ref(false);
const cooldown = ref(0);
let cooldownTimer: ReturnType<typeof setInterval> | null = null;

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

const userName = ref("");

function startCooldown(seconds: number) {
  cooldown.value = seconds;
  if (cooldownTimer) clearInterval(cooldownTimer);
  cooldownTimer = setInterval(() => {
    cooldown.value--;
    if (cooldown.value <= 0 && cooldownTimer) {
      clearInterval(cooldownTimer);
      cooldownTimer = null;
    }
  }, 1000);
}

async function doSendOtp() {
  const email = loginEmail.value.trim();
  if (!email) return;
  loginLoading.value = true;
  loginError.value = "";
  try {
    const result = await sendOtp(email);
    if (result.error) {
      const errMap: Record<string, string> = {
        TOO_MANY_REQUESTS: isZh.value ? "请求过于频繁，请稍后再试" : "Too many requests, please try later",
        OTP_RATE_LIMITED: isZh.value ? "发送过于频繁，请10分钟后再试" : "Too many OTPs sent, wait 10 minutes",
        EMAIL_NOT_CONFIGURED: isZh.value ? "邮件服务暂不可用" : "Email service unavailable",
        EMAIL_SEND_FAILED: isZh.value ? "邮件发送失败，请稍后重试" : "Failed to send email, please retry",
      };
      loginError.value = errMap[result.error] || result.error;
      return;
    }
    otpSent.value = true;
    loginStep.value = "code";
    startCooldown(60);
  } catch {
    loginError.value = isZh.value ? "网络错误，请稍后重试" : "Network error, please retry";
  } finally {
    loginLoading.value = false;
  }
}

async function doVerifyOtp() {
  const code = loginCode.value.trim();
  if (!code || code.length !== 6) return;
  loginLoading.value = true;
  loginError.value = "";
  try {
    const result = await verifyOtp(loginEmail.value.trim(), code);
    if (result.error) {
      const errMap: Record<string, string> = {
        INVALID_OR_EXPIRED_CODE: isZh.value ? "验证码无效或已过期" : "Invalid or expired code",
        WRONG_CODE: isZh.value
          ? `验证码错误，剩余 ${result.attempts_remaining ?? "?"} 次`
          : `Wrong code, ${result.attempts_remaining ?? "?"} attempts left`,
        TOO_MANY_ATTEMPTS: isZh.value ? "尝试过多，请重新获取验证码" : "Too many attempts, request a new code",
        USER_NOT_FOUND: isZh.value ? "用户不存在" : "User not found",
      };
      loginError.value = errMap[result.error] || result.error;
      return;
    }
    if (result.verified && result.hub_token) {
      saveSession(result.hub_token, result.display_name || "");
      loggedIn.value = true;
      userName.value = result.display_name || "";
      showLoginDialog.value = false;
      resetLoginForm();
    }
  } catch {
    loginError.value = isZh.value ? "网络错误，请稍后重试" : "Network error, please retry";
  } finally {
    loginLoading.value = false;
  }
}

function resetLoginForm() {
  loginStep.value = "email";
  loginEmail.value = "";
  loginCode.value = "";
  loginError.value = "";
  otpSent.value = false;
  if (cooldownTimer) { clearInterval(cooldownTimer); cooldownTimer = null; }
  cooldown.value = 0;
}

function doLogout() {
  logout();
  loggedIn.value = false;
  userName.value = "";
}

async function checkLogin() {
  loggedIn.value = isLoggedIn();
  if (loggedIn.value) {
    userName.value = getDisplayName();
    try {
      const result = await verifyAuth();
      if (result.verified) {
        userName.value = result.display_name || userName.value;
      } else {
        logout();
        loggedIn.value = false;
        userName.value = "";
      }
    } catch {
      // keep as logged in with cached name
    }
  }
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

    <!-- Login Dialog: Email + OTP -->
    <div v-if="showLoginDialog" class="rv-login-overlay" @click.self="showLoginDialog = false; resetLoginForm()">
      <div class="rv-login-dialog">
        <h3 class="rv-login-title">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--vp-c-brand-1)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/>
          </svg>
          {{ isZh ? "Reguverse 用户验证" : "Verify Reguverse Account" }}
        </h3>

        <!-- Step 1: Email -->
        <template v-if="loginStep === 'email'">
          <p class="rv-login-desc">
            {{ isZh
              ? "输入您的 Reguverse 注册邮箱，我们将发送一个验证码到该邮箱。"
              : "Enter your Reguverse account email. We will send a verification code." }}
          </p>
          <input
            v-model="loginEmail"
            type="email"
            :placeholder="isZh ? '输入注册邮箱...' : 'Enter your email...'"
            class="rv-login-input"
            @keydown.enter="doSendOtp"
          />
          <div v-if="loginError" class="rv-login-error">{{ loginError }}</div>
          <div class="rv-login-actions">
            <button class="rv-login-cancel" @click="showLoginDialog = false; resetLoginForm()">
              {{ isZh ? "取消" : "Cancel" }}
            </button>
            <button class="rv-login-submit" :disabled="loginLoading || !loginEmail.trim()" @click="doSendOtp">
              {{ loginLoading ? (isZh ? "发送中..." : "Sending...") : (isZh ? "发送验证码" : "Send Code") }}
            </button>
          </div>
        </template>

        <!-- Step 2: OTP Code -->
        <template v-else>
          <p class="rv-login-desc">
            {{ isZh
              ? `验证码已发送至 ${loginEmail}，请查收邮件。`
              : `Code sent to ${loginEmail}. Check your inbox.` }}
          </p>
          <input
            v-model="loginCode"
            type="text"
            inputmode="numeric"
            maxlength="6"
            :placeholder="isZh ? '输入6位验证码' : 'Enter 6-digit code'"
            class="rv-login-input rv-login-code-input"
            @keydown.enter="doVerifyOtp"
          />
          <div v-if="loginError" class="rv-login-error">{{ loginError }}</div>
          <div class="rv-login-resend">
            <button
              class="rv-login-resend-btn"
              :disabled="cooldown > 0 || loginLoading"
              @click="doSendOtp"
            >
              {{ cooldown > 0
                ? (isZh ? `${cooldown}s 后可重新发送` : `Resend in ${cooldown}s`)
                : (isZh ? "重新发送验证码" : "Resend code") }}
            </button>
            <button class="rv-login-back-btn" @click="loginStep = 'email'; loginError = ''">
              {{ isZh ? "更换邮箱" : "Change email" }}
            </button>
          </div>
          <div class="rv-login-actions">
            <button class="rv-login-cancel" @click="showLoginDialog = false; resetLoginForm()">
              {{ isZh ? "取消" : "Cancel" }}
            </button>
            <button class="rv-login-submit" :disabled="loginLoading || loginCode.trim().length !== 6" @click="doVerifyOtp">
              {{ loginLoading ? (isZh ? "验证中..." : "Verifying...") : (isZh ? "验证" : "Verify") }}
            </button>
          </div>
        </template>

        <p class="rv-login-note">
          {{ isZh
            ? "未注册？无需验证也可以参与讨论和投票。验证后可获得 Verified 标识。"
            : "Not registered? You can participate without verification. Verified users get a badge." }}
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
.rv-login-code-input {
  font-size: 24px;
  letter-spacing: 8px;
  text-align: center;
  font-family: monospace;
  font-weight: 600;
}
.rv-login-resend {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-top: 12px;
}
.rv-login-resend-btn,
.rv-login-back-btn {
  background: none;
  border: none;
  color: var(--vp-c-brand-1);
  cursor: pointer;
  font-size: 13px;
  padding: 0;
}
.rv-login-resend-btn:disabled {
  color: var(--vp-c-text-3);
  cursor: default;
}
.rv-login-back-btn {
  color: var(--vp-c-text-2);
}
.rv-login-back-btn:hover {
  color: var(--vp-c-text-1);
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
