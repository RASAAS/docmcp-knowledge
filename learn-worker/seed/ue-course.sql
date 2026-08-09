-- Seed: Usability Engineering foundation course (aligned with training #238 qids UE-01..)

INSERT OR IGNORE INTO courses (slug, title_en, title_zh, description_en, description_zh, published)
VALUES (
  'usability-engineering',
  'Usability Engineering Fundamentals',
  '可用性工程基础',
  'Interactive quiz for IEC 62366-1 process, RM I/O, Formative/Summative, and FDA/NMPA overlays.',
  '围绕 IEC 62366-1 过程、与风险管理互为输入输出、形成性/总结性评价，以及 FDA/NMPA 申报叠加层的互动题库。',
  1
);

-- UE-01
INSERT OR REPLACE INTO questions (course_id, qid, qtype, prompt_en, prompt_zh, options_json, correct_json, explanation_en, explanation_zh, tags_json, sort_order, published)
SELECT id, 'UE-01', 'single',
  'What is the primary question usability engineering answers?',
  '可用性工程主要回答的核心问题是？',
  '[{"id":"a","text_en":"Whether the UI looks modern","text_zh":"界面是否好看/现代化"},{"id":"b","text_en":"Whether users can correctly complete critical tasks and use-related risks are controlled","text_zh":"用户能否正确完成关键任务，并把使用相关风险控制到可接受"},{"id":"c","text_en":"Whether clinical efficacy is proven","text_zh":"临床有效性是否得到证明"},{"id":"d","text_en":"Whether the QMS has a CAPA procedure","text_zh":"质量体系是否有 CAPA 程序"}]',
  '["b"]',
  'UE focuses on safe and effective use under real users/environments/foreseeable misuse — not aesthetics alone.',
  '可用性工程关注真实用户/环境/可预见误用下能否安全有效使用，而不是界面美观本身。',
  '["lifecycle","basics"]', 10, 1
FROM courses WHERE slug='usability-engineering';

-- UE-02
INSERT OR REPLACE INTO questions (course_id, qid, qtype, prompt_en, prompt_zh, options_json, correct_json, explanation_en, explanation_zh, tags_json, sort_order, published)
SELECT id, 'UE-02', 'single',
  'Which statement best describes UE and risk management (ISO 14971)?',
  '关于可用性工程与风险管理（ISO 14971）的关系，哪项最准确？',
  '[{"id":"a","text_en":"Finish full RM first, then write a UE report at the end","text_zh":"先做完整 RM，最后补一份可用性报告"},{"id":"b","text_en":"They are parallel tracks that must exchange inputs/outputs","text_zh":"两条并行轨道，必须互喂输入/输出"},{"id":"c","text_en":"UE replaces RM for user interface hazards","text_zh":"对 UI 危害可用 UE 替代 RM"},{"id":"d","text_en":"Only Formative testing needs RM linkage","text_zh":"只有形成性评价需要与 RM 联动"}]',
  '["b"]',
  'UE and RM tell one safety story on two tracks; HRUS/controls/evaluation results require strong sync.',
  'UE 与 RM 是同一安全故事的两条轨道；HRUS/控制措施/评价结果等处必须强同步。',
  '["rm","io"]', 20, 1
FROM courses WHERE slug='usability-engineering';

-- UE-03
INSERT OR REPLACE INTO questions (course_id, qid, qtype, prompt_en, prompt_zh, options_json, correct_json, explanation_en, explanation_zh, tags_json, sort_order, published)
SELECT id, 'UE-03', 'single',
  'In IEC 62366-1 order, what typically comes first after concept/initiation?',
  '按 IEC 62366-1 推荐顺序，概念/立项后通常先完成哪一项？',
  '[{"id":"a","text_en":"Summative evaluation report","text_zh":"总结性评价报告"},{"id":"b","text_en":"Use Specification (5.1)","text_zh":"使用规范 Use Specification（5.1）"},{"id":"c","text_en":"FDA HF Submission Pack assembly","text_zh":"组装 FDA HF 申报包"},{"id":"d","text_en":"UER archival checklist only","text_zh":"仅做 UER 归档检查表"}]',
  '["b"]',
  'Use Specification defines users, use environments, and intended use — foundational for later UE and RM.',
  '使用规范定义用户、使用环境与预期使用，是后续 UE/RM 的基础输入。',
  '["62366","lifecycle"]', 30, 1
FROM courses WHERE slug='usability-engineering';

-- UE-04
INSERT OR REPLACE INTO questions (course_id, qid, qtype, prompt_en, prompt_zh, options_json, correct_json, explanation_en, explanation_zh, tags_json, sort_order, published)
SELECT id, 'UE-04', 'single',
  'Hazard-related use scenarios (HRUS) mainly support which purpose?',
  '危害相关使用场景（HRUS）的主要作用是？',
  '[{"id":"a","text_en":"Marketing claims for usability","text_zh":"用于可用性营销宣传"},{"id":"b","text_en":"Link use errors to hazardous situations and select scenarios for summative evaluation","text_zh":"把用错与危险情况关联，并筛选进入总结性评价的场景"},{"id":"c","text_en":"Replace biocompatibility testing","text_zh":"替代生物相容性试验"},{"id":"d","text_en":"Define notified body audit schedule","text_zh":"定义公告机构审核时间表"}]',
  '["b"]',
  'HRUS connect use errors to harm pathways and drive which scenarios enter summative evaluation.',
  'HRUS 连接用错与伤害路径，并驱动哪些场景进入总结性评价。',
  '["hrus","62366"]', 40, 1
FROM courses WHERE slug='usability-engineering';

-- UE-05
INSERT OR REPLACE INTO questions (course_id, qid, qtype, prompt_en, prompt_zh, options_json, correct_json, explanation_en, explanation_zh, tags_json, sort_order, published)
SELECT id, 'UE-05', 'single',
  'Which distinction is correct for Formative vs Summative evaluation?',
  '形成性评价与总结性评价的正确区分是？',
  '[{"id":"a","text_en":"Formative proves final residual risk; Summative only finds UI bugs early","text_zh":"形成性证明最终残余风险；总结性只用于早期找 UI bug"},{"id":"b","text_en":"Formative improves the UI iteratively; Summative validates selected HRUS on production-equivalent UI","text_zh":"形成性迭代改进 UI；总结性在生产等效 UI 上验证选定 HRUS"},{"id":"c","text_en":"They must be combined into one report always","text_zh":"二者必须永远合并成一份报告"},{"id":"d","text_en":"Only Summative is allowed under MDR","text_zh":"MDR 下只允许做总结性评价"}]',
  '["b"]',
  'Keep Formative and Summative separable as Studies; roles differ.',
  '形成性与总结性应可独立成 Study；角色不同，不可混为一谈。',
  '["formative","summative"]', 50, 1
FROM courses WHERE slug='usability-engineering';

-- UE-06
INSERT OR REPLACE INTO questions (course_id, qid, qtype, prompt_en, prompt_zh, options_json, correct_json, explanation_en, explanation_zh, tags_json, sort_order, published)
SELECT id, 'UE-06', 'single',
  'Type C safety information (e.g. warnings in IFU) is best treated as:',
  'Type C 安全信息（如 IFU 警告）最好被如何对待？',
  '[{"id":"a","text_en":"A residual-risk acceptance argument that never needs verification","text_zh":"无需验证的残余风险接受论据"},{"id":"b","text_en":"A risk control that still needs to be validated for effectiveness where relied upon","text_zh":"依赖它作为风险控制时，仍需验证其有效性"},{"id":"c","text_en":"Only a marketing leaflet requirement","text_zh":"仅是市场宣传页要求"},{"id":"d","text_en":"Irrelevant to usability engineering","text_zh":"与可用性工程无关"}]',
  '["b"]',
  'Information for safety is a control measure; if you rely on it, evaluate whether users notice/understand/act.',
  '安全信息是控制措施；若依赖它，需评价用户是否注意到、理解并按要求行动。',
  '["controls","ifu"]', 60, 1
FROM courses WHERE slug='usability-engineering';

-- UE-07
INSERT OR REPLACE INTO questions (course_id, qid, qtype, prompt_en, prompt_zh, options_json, correct_json, explanation_en, explanation_zh, tags_json, sort_order, published)
SELECT id, 'UE-07', 'single',
  'For an i-Check blood-gas analyzer case, which is most likely a Primary Operating Function concern?',
  '以 i-Check 血气分析仪为例，哪项最可能属于 Primary Operating Function 相关关注点？',
  '[{"id":"a","text_en":"Choosing office wall paint color","text_zh":"选择办公室墙面颜色"},{"id":"b","text_en":"Correct cartridge insertion and result interpretation under time pressure","text_zh":"在时间压力下正确插入测试卡并解读结果"},{"id":"c","text_en":"Annual financial audit of the manufacturer","text_zh":"制造商年度财务审计"},{"id":"d","text_en":"ISO 13485 clause numbering style","text_zh":"ISO 13485 条款编号风格"}]',
  '["b"]',
  'POFs are critical tasks for safe/effective use — e.g. cartridge handling and reading results.',
  'POF 是安全有效使用的关键任务，例如插卡与结果解读。',
  '["case","icheck","pof"]', 70, 1
FROM courses WHERE slug='usability-engineering';

-- UE-08
INSERT OR REPLACE INTO questions (course_id, qid, qtype, prompt_en, prompt_zh, options_json, correct_json, explanation_en, explanation_zh, tags_json, sort_order, published)
SELECT id, 'UE-08', 'single',
  'FDA HF/UE submission materials are best described as:',
  'FDA 人因/可用性申报材料最好被描述为？',
  '[{"id":"a","text_en":"A replacement for IEC 62366-1 process evidence","text_zh":"可替代 IEC 62366-1 过程证据"},{"id":"b","text_en":"A submission overlay assembled from the underlying UE/RM process","text_zh":"建立在底层 UE/RM 过程之上的申报叠加层"},{"id":"c","text_en":"Only required for software medical devices","text_zh":"仅软件医疗器械需要"},{"id":"d","text_en":"Identical to the EU UER index with no mapping needed","text_zh":"与欧盟 UER 索引完全相同无需映射"}]',
  '["b"]',
  'FDA Category/Content guidance shapes the dossier view; it does not replace the process standard.',
  'FDA Category/Content 指南塑造申报视角，并不替代过程标准本身。',
  '["fda","overlay"]', 80, 1
FROM courses WHERE slug='usability-engineering';

-- UE-09
INSERT OR REPLACE INTO questions (course_id, qid, qtype, prompt_en, prompt_zh, options_json, correct_json, explanation_en, explanation_zh, tags_json, sort_order, published)
SELECT id, 'UE-09', 'single',
  'NMPA usability engineering registration guidance is best used as:',
  'NMPA《医疗器械可用性工程注册审查指导原则》最好如何使用？',
  '[{"id":"a","text_en":"The only process standard, ignoring IEC 62366-1","text_zh":"作为唯一过程标准，忽略 IEC 62366-1"},{"id":"b","text_en":"A China registration path/overlay on top of a sound UE process","text_zh":"在健全 UE 过程之上的中国注册路径/叠加要求"},{"id":"c","text_en":"A substitute for clinical evaluation","text_zh":"替代临床评价"},{"id":"d","text_en":"Only for Class I devices","text_zh":"仅适用于一类器械"}]',
  '["b"]',
  'Treat NMPA guidance as registration expectations layered on process evidence.',
  '将 NMPA 指导原则视为叠加在过程证据之上的注册审查期望。',
  '["nmpa","overlay"]', 90, 1
FROM courses WHERE slug='usability-engineering';

-- UE-10
INSERT OR REPLACE INTO questions (course_id, qid, qtype, prompt_en, prompt_zh, options_json, correct_json, explanation_en, explanation_zh, tags_json, sort_order, published)
SELECT id, 'UE-10', 'multi',
  'Which outputs commonly feed FROM usability engineering INTO risk management? (select all that apply)',
  '下列哪些输出通常从可用性工程喂入风险管理？（多选）',
  '[{"id":"a","text_en":"Use errors and hazardous situations identified from task analysis","text_zh":"任务分析识别的用错与危险情况"},{"id":"b","text_en":"Summative results informing residual risk evaluation","text_zh":"总结性评价结果用于残余风险评价"},{"id":"c","text_en":"Stock price of competitors","text_zh":"竞争对手股价"},{"id":"d","text_en":"UI/information/training controls proposed for use-related risks","text_zh":"针对使用相关风险提出的 UI/信息/培训控制措施"}]',
  '["a","b","d"]',
  'UE feeds use-error pathways, control ideas, and evaluation outcomes into RM; market data is unrelated.',
  'UE 向 RM 提供用错路径、控制思路与评价结果；市场股价无关。',
  '["rm","io"]', 100, 1
FROM courses WHERE slug='usability-engineering';

-- UE-11
INSERT OR REPLACE INTO questions (course_id, qid, qtype, prompt_en, prompt_zh, options_json, correct_json, explanation_en, explanation_zh, tags_json, sort_order, published)
SELECT id, 'UE-11', 'single',
  'In Reguverse UEF terms, Document vs Study layers are intended to:',
  '在 Reguverse UEF 中，Document 层与 Study 层的意图是？',
  '[{"id":"a","text_en":"Document = one-off report; Study is unused","text_zh":"Document=一次性报告；Study 不用"},{"id":"b","text_en":"Separate enduring process artifacts from repeatable evaluation events","text_zh":"把持久过程产物与可重复的评价事件分开"},{"id":"c","text_en":"Replace the need for protocols","text_zh":"不再需要评价方案"},{"id":"d","text_en":"Only apply to FDA submissions","text_zh":"仅适用于 FDA 申报"}]',
  '["b"]',
  'Harness separates long-lived UEF documents from Formative/Summative studies with protocol+report pairs.',
  'Harness 将长期 UEF 文档与「方案+报告」成对的评价 Study 分开管理。',
  '["reguverse","uef"]', 110, 1
FROM courses WHERE slug='usability-engineering';

-- UE-12
INSERT OR REPLACE INTO questions (course_id, qid, qtype, prompt_en, prompt_zh, options_json, correct_json, explanation_en, explanation_zh, tags_json, sort_order, published)
SELECT id, 'UE-12', 'single',
  'After market launch, complaint/PMCF signals about use errors should primarily:',
  '上市后若投诉/PMCF 提示使用错误，首先应？',
  '[{"id":"a","text_en":"Ignore them if CE mark already exists","text_zh":"已有 CE 标志则可忽略"},{"id":"b","text_en":"Trigger local re-entry into UE/RM activities as needed","text_zh":"按需触发 UE/RM 活动的局部再进入"},{"id":"c","text_en":"Only update the marketing website","text_zh":"仅更新市场宣传网站"},{"id":"d","text_en":"Delete the previous Summative report","text_zh":"删除既往总结性评价报告"}]',
  '["b"]',
  'Post-market feedback can reopen parts of the UE/RM loop under change control.',
  '上市后反馈可在变更控制下重新进入 UE/RM 循环的局部环节。',
  '["pms","lifecycle"]', 120, 1
FROM courses WHERE slug='usability-engineering';
