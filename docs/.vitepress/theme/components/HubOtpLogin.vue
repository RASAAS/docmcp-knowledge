<script setup lang="ts">
/**
 * Shared DocMCP / Hub email-OTP login dialog (used by Hub + Learn).
 */
import { ref, watch } from "vue";
import {
  mapOtpSendError,
  mapOtpVerifyError,
  saveSession,
  sendOtp,
  verifyOtp,
} from "./HubApi";

const props = withDefaults(
  defineProps<{
    open: boolean;
    isZh: boolean;
    /** Footer note: hub (optional verify) vs learn (account required) */
    variant?: "hub" | "learn";
  }>(),
  { variant: "hub" }
);

const emit = defineEmits<{
  close: [];
  success: [payload: { displayName: string; userId?: string; role?: string }];
}>();

const loginStep = ref<"email" | "code">("email");
const loginEmail = ref("");
const loginCode = ref("");
const loginError = ref("");
const loginLoading = ref(false);
const cooldown = ref(0);
let cooldownTimer: ReturnType<typeof setInterval> | null = null;

function clearCooldown() {
  if (cooldownTimer) {
    clearInterval(cooldownTimer);
    cooldownTimer = null;
  }
  cooldown.value = 0;
}

function resetForm() {
  loginStep.value = "email";
  loginEmail.value = "";
  loginCode.value = "";
  loginError.value = "";
  loginLoading.value = false;
  clearCooldown();
}

function startCooldown(seconds: number) {
  cooldown.value = seconds;
  if (cooldownTimer) clearInterval(cooldownTimer);
  cooldownTimer = setInterval(() => {
    cooldown.value--;
    if (cooldown.value <= 0) clearCooldown();
  }, 1000);
}

watch(
  () => props.open,
  (v) => {
    if (!v) resetForm();
  }
);

function onCancel() {
  emit("close");
  resetForm();
}

async function doSendOtp() {
  const email = loginEmail.value.trim();
  if (!email) return;
  loginLoading.value = true;
  loginError.value = "";
  try {
    const result = await sendOtp(email);
    if (result.error) {
      loginError.value = mapOtpSendError(result.error, props.isZh);
      return;
    }
    loginStep.value = "code";
    startCooldown(60);
  } catch {
    loginError.value = props.isZh ? "网络错误，请稍后重试" : "Network error, please retry";
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
      loginError.value = mapOtpVerifyError(result.error, props.isZh, result.attempts_remaining);
      return;
    }
    if (result.verified && result.hub_token) {
      const userId = result.user_id;
      const role = result.role;
      saveSession(result.hub_token, result.display_name || "", userId, role);
      emit("success", {
        displayName: result.display_name || loginEmail.value.trim(),
        userId,
        role,
      });
      resetForm();
    } else {
      loginError.value = props.isZh ? "验证失败，请重试" : "Verification failed, please retry";
    }
  } catch {
    loginError.value = props.isZh ? "网络错误，请稍后重试" : "Network error, please retry";
  } finally {
    loginLoading.value = false;
  }
}

const noteText = () => {
  if (props.variant === "learn") {
    return props.isZh
      ? "没有账号？请先在 app.team-ra.org / app.reguverse.com 注册 DocMCP 账号。"
      : "No account? Register at app.team-ra.org / app.reguverse.com first.";
  }
  return props.isZh
    ? "未注册？无需验证也可以参与讨论和投票。验证后可获得 Verified 标识。"
    : "Not registered? You can participate without verification. Verified users get a badge.";
};
</script>

<template>
  <div v-if="open" class="rv-login-overlay" @click.self="onCancel">
    <div class="rv-login-dialog" role="dialog" aria-modal="true">
      <h3 class="rv-login-title">
        <svg
          width="20"
          height="20"
          viewBox="0 0 24 24"
          fill="none"
          stroke="var(--vp-c-brand-1)"
          stroke-width="2"
          stroke-linecap="round"
          stroke-linejoin="round"
          aria-hidden="true"
        >
          <path
            d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"
          />
        </svg>
        {{ isZh ? "Reguverse 用户验证" : "Verify Reguverse Account" }}
      </h3>

      <template v-if="loginStep === 'email'">
        <p class="rv-login-desc">
          {{
            isZh
              ? "输入您的 Reguverse 注册邮箱，我们将发送一个验证码到该邮箱。"
              : "Enter your Reguverse account email. We will send a verification code."
          }}
        </p>
        <input
          v-model="loginEmail"
          type="email"
          autocomplete="email"
          :placeholder="isZh ? '输入注册邮箱...' : 'Enter your email...'"
          class="rv-login-input"
          @keydown.enter="doSendOtp"
        />
        <div v-if="loginError" class="rv-login-error">{{ loginError }}</div>
        <div class="rv-login-actions">
          <button type="button" class="rv-login-cancel" @click="onCancel">
            {{ isZh ? "取消" : "Cancel" }}
          </button>
          <button
            type="button"
            class="rv-login-submit"
            :disabled="loginLoading || !loginEmail.trim()"
            @click="doSendOtp"
          >
            {{
              loginLoading
                ? isZh
                  ? "发送中..."
                  : "Sending..."
                : isZh
                  ? "发送验证码"
                  : "Send Code"
            }}
          </button>
        </div>
      </template>

      <template v-else>
        <p class="rv-login-desc">
          {{
            isZh
              ? `验证码已发送至 ${loginEmail}，请查收邮件。`
              : `Code sent to ${loginEmail}. Check your inbox.`
          }}
        </p>
        <input
          v-model="loginCode"
          type="text"
          inputmode="numeric"
          maxlength="6"
          autocomplete="one-time-code"
          :placeholder="isZh ? '输入6位验证码' : 'Enter 6-digit code'"
          class="rv-login-input rv-login-code-input"
          @keydown.enter="doVerifyOtp"
        />
        <div v-if="loginError" class="rv-login-error">{{ loginError }}</div>
        <div class="rv-login-resend">
          <button
            type="button"
            class="rv-login-resend-btn"
            :disabled="cooldown > 0 || loginLoading"
            @click="doSendOtp"
          >
            {{
              cooldown > 0
                ? isZh
                  ? `${cooldown}s 后可重新发送`
                  : `Resend in ${cooldown}s`
                : isZh
                  ? "重新发送验证码"
                  : "Resend code"
            }}
          </button>
          <button
            type="button"
            class="rv-login-back-btn"
            @click="
              loginStep = 'email';
              loginError = '';
            "
          >
            {{ isZh ? "更换邮箱" : "Change email" }}
          </button>
        </div>
        <div class="rv-login-actions">
          <button type="button" class="rv-login-cancel" @click="onCancel">
            {{ isZh ? "取消" : "Cancel" }}
          </button>
          <button
            type="button"
            class="rv-login-submit"
            :disabled="loginLoading || loginCode.trim().length !== 6"
            @click="doVerifyOtp"
          >
            {{
              loginLoading
                ? isZh
                  ? "验证中..."
                  : "Verifying..."
                : isZh
                  ? "验证"
                  : "Verify"
            }}
          </button>
        </div>
      </template>

      <p class="rv-login-note">{{ noteText() }}</p>
    </div>
  </div>
</template>

<style scoped>
.rv-login-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
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
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
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
  color: var(--vp-c-danger-1, #b42318);
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
  .rv-login-dialog {
    padding: 24px;
  }
}
</style>
