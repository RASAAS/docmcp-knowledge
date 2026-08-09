export type LearnTabKey = "join" | "host" | "practice";

export interface LearnTabDef {
  key: LearnTabKey;
  labelEn: string;
  labelZh: string;
}

export const LEARN_TABS: LearnTabDef[] = [
  { key: "join", labelEn: "Join Live", labelZh: "加入现场" },
  { key: "host", labelEn: "Host Session", labelZh: "主持场次" },
  { key: "practice", labelEn: "Practice", labelZh: "自学练习" },
];

export function learnLabel(item: { labelEn: string; labelZh: string }, isZh: boolean): string {
  return isZh ? item.labelZh : item.labelEn;
}

export const LEARN_I18N = {
  title: { en: "Reguverse Learn", zh: "Reguverse Learn" },
  subtitle: {
    en: "Live speaker-controlled quizzes and self-paced practice.",
    zh: "演讲者控题的现场互动答题，以及随时自学练习。",
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
    en: "Save the host token — it is shown only once when creating a session.",
    zh: "请保存主持令牌（仅在创建场次时显示一次）。",
  },
  practiceStart: { en: "Start practice", zh: "开始练习" },
  practiceSubmit: { en: "Check answers", zh: "核对答案" },
  score: { en: "Score", zh: "得分" },
  multiHint: { en: "Select all that apply", zh: "多选题，可选多项" },
  error: { en: "Something went wrong", zh: "出错了" },
  copyLink: { en: "Copy join link", zh: "复制加入链接" },
  copied: { en: "Copied", zh: "已复制" },
  phase: { en: "Phase", zh: "阶段" },
  restoreHost: { en: "Restore last host session", zh: "恢复上次主持场次" },
  correct: { en: "Correct", zh: "正确" },
  incorrect: { en: "Incorrect", zh: "不正确" },
} as const;

export function t(
  key: keyof typeof LEARN_I18N,
  isZh: boolean
): string {
  const item = LEARN_I18N[key];
  return isZh ? item.zh : item.en;
}
