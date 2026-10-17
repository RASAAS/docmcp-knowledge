<script setup>
import { onMounted, ref } from "vue";

const API = "https://llm.reguverse.com/api/v1/surveys/public/deploy-choice";
const VOTER_KEY = "rv-survey-deploy-choice";

const options = [
  {
    id: "cloud",
    title: "方式一 · 网页或 Word",
    line: "现在就能用。原始文件会上传。",
    image: "/survey/01-cloud.png",
    points: ["整份文件上传后抽出文字", "文件本身不长期保存", "文字和报告留在云端"],
  },
  {
    id: "desktop",
    title: "方式二 · 电脑桌面端软件",
    line: "开发中。普通原件留在您的电脑。",
    image: "/survey/02-desktop-cloud.png",
    points: ["能复制文字的文件在本机抽取", "扫描件只在识别时上传，用完即删", "文字和报告仍在云端"],
  },
  {
    id: "local",
    title: "方式三 · 公司内网小主机",
    line: "计划中。产品资料默认不出公司。",
    image: "/survey/03-fully-local.png",
    points: ["需要一台放在公司内网的小主机", "原件、文字、报告和人工智能都在公司里", "查公开法规时只发出搜索词"],
  },
];

const priorities = [
  { id: "originals", label: "原始文件不要离开公司" },
  { id: "text", label: "抽出的文字也不要放到云端" },
  { id: "no_hardware", label: "先不要额外的设备" },
  { id: "familiar", label: "尽量接近现在的网页和 Word" },
  { id: "price", label: "价格" },
  { id: "speed", label: "生成速度" },
];

const diagrams = [
  ["三种方式对照", "/survey/10-overview.png"],
  ["方式一网络连接", "/survey/11-cloud-topology.png"],
  ["方式二网络连接", "/survey/12-desktop-topology.png"],
  ["方式三公司网络", "/survey/13-box-network.png"],
  ["方式三小主机内部", "/survey/14-box-architecture.png"],
  ["数据放在哪里", "/survey/15-data-residency.png"],
];

const choice = ref("");
const picked = ref([]);
const boxInterest = ref("");
const companySize = ref("");
const role = ref("");
const name = ref("");
const organization = ref("");
const email = ref("");
const comment = ref("");
const status = ref("");
const busy = ref(false);
const summary = ref(null);

function voterKey() {
  const saved = localStorage.getItem(VOTER_KEY);
  if (saved) return saved;
  const key = (crypto.randomUUID && crypto.randomUUID()) || `k${Date.now()}browserkey01`;
  const clean = key.replace(/[^A-Za-z0-9_-]/g, "").slice(0, 80);
  localStorage.setItem(VOTER_KEY, clean.length >= 16 ? clean : `${clean}browserkey0001`);
  return localStorage.getItem(VOTER_KEY);
}

function toggle(id) {
  picked.value = picked.value.includes(id)
    ? picked.value.filter((item) => item !== id)
    : picked.value.concat(id);
}

async function loadSummary() {
  try {
    const response = await fetch(`${API}/summary`);
    if (response.ok) summary.value = await response.json();
  } catch {
    summary.value = null;
  }
}

async function submit() {
  status.value = "";
  if (!choice.value) {
    status.value = "请先选择一种用法。";
    return;
  }
  busy.value = true;
  try {
    const response = await fetch(API, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        voter_key: voterKey(),
        choice: choice.value,
        priorities: picked.value,
        box_interest: boxInterest.value,
        company_size: companySize.value,
        role: role.value,
        name: name.value,
        organization: organization.value,
        email: email.value,
        comment: comment.value,
        website: "",
      }),
    });
    const data = await response.json().catch(() => ({}));
    if (!response.ok) {
      status.value = data.error === "请稍后再提交" ? "提交太频繁，请稍后再试。" : "暂时提交不了，请稍后再试。";
      return;
    }
    status.value = data.updated ? "已更新您之前的选择。" : "已记下。谢谢。";
    await loadSummary();
  } catch {
    status.value = "暂时连不上服务器，请稍后再试。";
  } finally {
    busy.value = false;
  }
}

function percent(count) {
  const total = summary.value && summary.value.total;
  if (!total) return "0%";
  return `${Math.round((count / total) * 100)}%`;
}

onMounted(loadSummary);
</script>

<template>
  <div class="survey">
    <p class="kicker">开发计划调研</p>
    <h1>三种用法，您需要哪种</h1>
    <p class="lead">
      为了满足不同用户的需求，Reguverse助手计划进行架构调整，欢迎制造商用户提供宝贵意见。
      请选择更适合您公司的 Reguverse 用法，并留下意见。结果只用于安排后续开发。
      我们计划了三种使用方式，差别主要在原始文件离不离开公司、写好的内容存在哪里。
      本次调研只用来安排后续开发，不会改变您现在的账号。
    </p>

    <section class="plan">
      <h2>目前的计划和进展</h2>
      <ol>
        <li><b>方式一已经在用。</b>网页和 Word 插件按这个方式工作。</li>
        <li><b>方式二正在准备开发。</b>电脑桌面端软件会先在本机抽出文字，再把文字发给云端。</li>
        <li><b>方式三仍在计划中。</b>公司里放一台小主机，产品资料默认留在内网。本次调研旨在了解有多少团队需要，再安排相应开发。</li>
      </ol>
    </section>

    <h2>请选择更接近您公司情况的一种</h2>
    <div class="cards">
      <button
        v-for="item in options"
        :key="item.id"
        type="button"
        class="card"
        :class="{ on: choice === item.id }"
        @click="choice = item.id"
      >
        <span class="pick">{{ choice === item.id ? "已选择" : "选择这个" }}</span>
        <strong>{{ item.title }}</strong>
        <span class="line">{{ item.line }}</span>
        <img :src="item.image" :alt="item.title">
        <ul>
          <li v-for="point in item.points" :key="point">{{ point }}</li>
        </ul>
      </button>
    </div>
    <button type="button" class="ghost" :class="{ on: choice === 'undecided' }" @click="choice = 'undecided'">
      {{ choice === "undecided" ? "已选择：还不确定" : "还不确定，先看看" }}
    </button>

    <h2>您更在意什么</h2>
    <p class="hint">可以多选。</p>
    <div class="chips">
      <button
        v-for="item in priorities"
        :key="item.id"
        type="button"
        class="chip"
        :class="{ on: picked.includes(item.id) }"
        @click="toggle(item.id)"
      >{{ item.label }}</button>
    </div>

    <h2>如果资料可以完全留在公司</h2>
    <div class="chips">
      <button type="button" class="chip" :class="{ on: boxInterest === 'yes' }" @click="boxInterest = 'yes'">愿意了解小主机</button>
      <button type="button" class="chip" :class="{ on: boxInterest === 'later' }" @click="boxInterest = 'later'">以后再说</button>
      <button type="button" class="chip" :class="{ on: boxInterest === 'no' }" @click="boxInterest = 'no'">不需要</button>
    </div>

    <h2>补充信息</h2>
    <div class="form">
      <label>预计使用人数
        <select v-model="companySize">
          <option value="">暂不填写</option>
          <option value="1-10">1–10 人</option>
          <option value="11-50">11–50 人</option>
          <option value="51-200">51–200 人</option>
          <option value="200+">200 人以上</option>
        </select>
      </label>
      <label>您的角色
        <input v-model="role" maxlength="80" placeholder="例如：法规、质量、IT等">
      </label>
      <label>单位
        <input v-model="organization" maxlength="120" placeholder="选填">
      </label>
      <label>姓名
        <input v-model="name" maxlength="80" placeholder="选填">
      </label>
      <label>邮箱
        <input v-model="email" maxlength="160" placeholder="选填，只用于回访">
      </label>
      <label class="wide">其他说明或需求
        <textarea v-model="comment" maxlength="2000" rows="4" placeholder="例如：必须留在公司的是哪类文件，或者希望先试用哪一种"></textarea>
      </label>
    </div>
    <button type="button" class="submit" :disabled="busy" @click="submit">{{ busy ? "提交中" : "提交选择" }}</button>
    <p v-if="status" class="status">{{ status }}</p>
    <p class="hint">同一浏览器再次提交会更新您的选择，不会重复计数。单位、姓名、邮箱和文字意见不会显示在这个页面上。</p>

    <section v-if="summary" class="tally">
      <h2>目前的选择比例</h2>
      <p class="hint">共 {{ summary.total }} 份。改选后这里会更新。</p>
      <div v-for="item in options" :key="item.id" class="bar">
        <span>{{ item.title }}</span>
        <span class="track"><i :style="{ width: percent(summary.choices[item.id] || 0) }"></i></span>
        <b>{{ summary.choices[item.id] || 0 }} · {{ percent(summary.choices[item.id] || 0) }}</b>
      </div>
      <div class="bar">
        <span>还不确定</span>
        <span class="track"><i :style="{ width: percent(summary.choices.undecided || 0) }"></i></span>
        <b>{{ summary.choices.undecided || 0 }} · {{ percent(summary.choices.undecided || 0) }}</b>
      </div>
    </section>

    <details class="more">
      <summary>网络连接、架构、拓扑示意图</summary>
      <p class="hint">下面这组图具体说明：数据放在哪、公司网络如何连接、小主机对内和对外的边界。</p>
      <figure v-for="item in diagrams" :key="item[1]">
        <figcaption>{{ item[0] }}</figcaption>
        <img :src="item[1]" :alt="item[0]">
      </figure>
    </details>
  </div>
</template>

<style scoped>
.survey { padding-bottom: 48px; }
.kicker { color: var(--vp-c-brand-1); font-weight: 650; letter-spacing: 0.04em; margin: 0 0 8px; }
h1 { font-size: 36px; line-height: 1.25; margin: 0 0 12px; border: 0; }
.lead, .hint { color: var(--vp-c-text-2); line-height: 1.6; }
.plan, .tally, .more {
  background: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-divider);
  border-radius: 12px;
  padding: 16px 18px;
  margin: 20px 0;
}
.plan ol { margin: 8px 0 0; padding-left: 1.2em; }
.plan li { margin: 8px 0; line-height: 1.55; }
h2 { font-size: 22px; margin: 28px 0 10px; border: 0; }
.cards { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 12px; }
.card, .ghost, .chip, .submit {
  font: inherit;
  text-align: left;
  cursor: pointer;
  color: var(--vp-c-text-1);
  background: var(--vp-c-bg);
}
.card {
  border: 2px solid var(--vp-c-divider);
  border-radius: 14px;
  padding: 12px;
}
.card.on, .ghost.on, .chip.on { border-color: var(--vp-c-brand-1); background: var(--vp-c-brand-soft); }
.card img, .more img { width: 100%; border-radius: 8px; border: 1px solid var(--vp-c-divider); }
.card strong { display: block; margin: 6px 0 2px; }
.line, .pick { display: block; color: var(--vp-c-text-2); font-size: 13px; }
.card ul { margin: 8px 0 0; padding-left: 1.1em; font-size: 14px; }
.card li { margin: 4px 0; }
.ghost, .submit {
  margin-top: 12px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 999px;
  padding: 8px 14px;
}
.submit { background: var(--vp-c-brand-1); color: #fff; border: 0; font-weight: 650; }
.submit:disabled { opacity: 0.6; cursor: default; }
.chips { display: flex; flex-wrap: wrap; gap: 8px; }
.chip { border: 1px solid var(--vp-c-divider); border-radius: 999px; padding: 8px 12px; }
.form { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
.form label { display: flex; flex-direction: column; gap: 6px; font-size: 14px; }
.form .wide { grid-column: 1 / -1; }
.form input, .form select, .form textarea {
  font: inherit;
  color: var(--vp-c-text-1);
  background: var(--vp-c-bg);
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  padding: 8px 10px;
}
.status { color: var(--vp-c-brand-1); font-weight: 650; }
.bar { display: grid; grid-template-columns: 180px 1fr 92px; gap: 8px; align-items: center; margin: 8px 0; font-size: 14px; }
.track { height: 8px; background: var(--vp-c-divider); border-radius: 99px; overflow: hidden; }
.track i { display: block; height: 100%; background: var(--vp-c-brand-1); }
.more summary { cursor: pointer; font-weight: 650; }
.more figure { margin: 16px 0; }
.more figcaption { margin-bottom: 6px; font-size: 14px; color: var(--vp-c-text-2); }
@media (max-width: 900px) {
  .cards, .form, .bar { grid-template-columns: 1fr; }
}
</style>
