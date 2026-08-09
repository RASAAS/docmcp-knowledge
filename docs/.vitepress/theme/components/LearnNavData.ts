export type LearnTabKey = "join" | "host" | "workshop" | "practice";

export interface LearnTabDef {
  key: LearnTabKey;
  labelEn: string;
  labelZh: string;
}

export const LEARN_TABS: LearnTabDef[] = [
  { key: "join", labelEn: "Join Live", labelZh: "加入现场" },
  { key: "host", labelEn: "Host Session", labelZh: "主持场次" },
  { key: "workshop", labelEn: "Workshop", labelZh: "工作坊" },
  { key: "practice", labelEn: "Practice", labelZh: "自学练习" },
];

export function learnLabel(item: { labelEn: string; labelZh: string }, isZh: boolean): string {
  return isZh ? item.labelZh : item.labelEn;
}

export const LEARN_I18N = {
  title: { en: "Reguverse Learn", zh: "Reguverse Learn" },
  subtitle: {
    en: "Live speaker-controlled quizzes, workshops, and self-paced practice across courses.",
    zh: "跨课程的演讲者控题互动答题、工作坊协作与自学练习。",
  },
  sessionCode: { en: "Session code", zh: "会话码" },
  nickname: { en: "Nickname", zh: "昵称" },
  displayName: { en: "Name (optional)", zh: "姓名（可选）" },
  join: { en: "Join", zh: "加入" },
  waiting: { en: "Waiting for the next question…", zh: "等待演讲者推送下一题…" },
  submit: { en: "Submit answer", zh: "提交答案" },
  submitted: { en: "Answer submitted", zh: "已提交" },
  locked: { en: "Answering locked", zh: "已锁题" },
  reveal: { en: "Answer revealed", zh: "已揭晓" },
  create: { en: "Create session", zh: "创建场次" },
  push: { en: "Push next", zh: "推送下一题" },
  lock: { en: "Lock", zh: "锁题" },
  revealBtn: { en: "Reveal", zh: "揭晓" },
  lobby: { en: "Back to lobby", zh: "回到等待" },
  end: { en: "End session", zh: "结束场次" },
  participants: { en: "Participants", zh: "学员数" },
  answered: { en: "Answered", zh: "已作答" },
  hostTokenHint: {
    en: "Your host control is tied to this DocMCP account. Others cannot restore your session.",
    zh: "主持控制权绑定当前 DocMCP 账号，其他用户无法恢复你的场次。",
  },
  practiceStart: { en: "Start practice", zh: "开始练习" },
  practiceSubmit: { en: "Check answers", zh: "核对答案" },
  score: { en: "Score", zh: "得分" },
  multiHint: { en: "Select all that apply", zh: "多选题，可选多项" },
  error: { en: "Something went wrong", zh: "出错了" },
  copyLink: { en: "Copy join link", zh: "复制加入链接" },
  copied: { en: "Copied", zh: "已复制" },
  phase: { en: "Phase", zh: "阶段" },
  restoreHost: { en: "Restore my last session", zh: "恢复我的上次场次" },
  mySessions: { en: "My active sessions", zh: "我的进行中场次" },
  reclaim: { en: "Resume", zh: "继续主持" },
  noMySessions: {
    en: "No active sessions for this account.",
    zh: "当前账号没有进行中的场次。",
  },
  course: { en: "Course", zh: "课程" },
  selectCourse: { en: "Select a course", zh: "选择课程" },
  correct: { en: "Correct", zh: "正确" },
  incorrect: { en: "Incorrect", zh: "不正确" },
  scanToJoin: {
    en: "Scan with phone to join (mobile layout)",
    zh: "手机扫码加入（移动端自适应）",
  },
  orEnterCode: {
    en: "Or enter nickname below to join",
    zh: "或在下方填写昵称后加入",
  },
  showQrOnJoin: {
    en: "Show QR on Join tab",
    zh: "去「加入现场」展示二维码",
  },
  enterCodeForQr: {
    en: "Enter a session code to show the join QR code (for projection).",
    zh: "输入会话码后将显示加入二维码（可用于投影给学员扫码）。",
  },
  qrHostHint: {
    en: "Create a session first, then open Join Live to project the QR code.",
    zh: "请先创建场次，再切换到「加入现场」投影二维码给学员。",
  },
  loginRequired: {
    en: "A registered DocMCP account is required. Sign in with email OTP.",
    zh: "需注册 DocMCP 账号并登录（邮箱验证码）。",
  },
  hostLoginRequired: {
    en: "Hosting a live session requires DocMCP login.",
    zh: "主持场次需先登录 DocMCP 账号。",
  },
  workshopTitle: {
    en: "Workshop boards",
    zh: "工作坊看板",
  },
  workshopHint: {
    en: "Host creates blank groups. Each group designs its own sections and content — no built-in case.",
    zh: "由主持人创建空白小组；各组自行设计栏目与内容，不内置任何案例模板。",
  },
  workshopSave: { en: "Save group", zh: "保存本组" },
  workshopRefresh: { en: "Refresh boards", zh: "刷新各组看板" },
  workshopGroup: { en: "Group", zh: "组别" },
  workshopAddGroup: { en: "Add group", zh: "新建小组" },
  workshopDeleteGroup: { en: "Delete group", zh: "删除小组" },
  workshopGroupName: { en: "Group name", zh: "小组名称" },
  workshopGroupNamePh: { en: "e.g. Team A", zh: "例如：第一组" },
  workshopAddSection: { en: "Add section", zh: "添加栏目" },
  workshopRemoveSection: { en: "Remove", zh: "删除" },
  workshopSection: { en: "Section", zh: "栏目" },
  workshopSectionTitlePh: { en: "Section title", zh: "栏目标题" },
  workshopSectionBodyPh: { en: "Write this group’s content…", zh: "填写本组内容…" },
  workshopEmpty: {
    en: "No groups yet. The host should create groups first.",
    zh: "尚无小组。请主持人先创建小组。",
  },
  workshopHostOnly: {
    en: "Only the host can create or delete groups.",
    zh: "仅主持人可创建或删除小组。",
  },
  workshopMemberHint: {
    en: "Joined participants can edit the selected group’s content.",
    zh: "已加入的学员可编辑所选小组的内容。",
  },
  workshopNeedCode: {
    en: "Enter a session code or join a live session first.",
    zh: "请先填写会话码或加入现场会话。",
  },
  workshopPeerTitle: {
    en: "All groups (peer review)",
    zh: "各组看板（互评）",
  },
  workshopNoContent: {
    en: "No content yet.",
    zh: "暂无内容。",
  },
  workshopUnsaved: {
    en: "Unsaved changes — click Save group to keep them.",
    zh: "有未保存修改，请点击「保存本组」以免丢失。",
  },
  openWorkshop: {
    en: "Open workshop boards",
    zh: "打开工作坊看板",
  },
  hostBusy: { en: "Working…", zh: "处理中…" },
  logout: { en: "Sign out", zh: "退出登录" },
  signedInAs: { en: "Signed in as", zh: "已登录" },
  signIn: { en: "Sign in", zh: "登录" },
  registerHint: {
    en: "No account? Register at app.team-ra.org / app.reguverse.com first.",
    zh: "没有账号？请先在 app.team-ra.org / app.reguverse.com 注册。",
  },
} as const;

export function t(key: keyof typeof LEARN_I18N, isZh: boolean): string {
  const item = LEARN_I18N[key];
  return isZh ? item.zh : item.en;
}
