# CRM 消息提醒：海外 Telegram 与国内钉钉

登录 [Reguverse CRM](https://crm.reguverse.com) 后，关闭网页也能收到项目消息摘要。渠道按地区分开：

| 您在哪里 | 怎么收提醒 | 谁来设置 |
|---|---|---|
| **海外**（团队成员或客户） | 个人 Telegram，官方 Bot **@reguversebot** | 您自己在侧栏绑定 |
| **国内客户** | 该客户的 **钉钉群** | **CRO 在客户详情页添加群机器人**，客户不用自己绑 Bot |

提醒只含摘要和打开 CRM 的链接，**不会**推送机密全文。

---

## 海外：绑定 Telegram

大约一分钟。手机 App 或 Telegram 网页版都可以。

::: info 网页版请先登录 Telegram
如果您准备在 **Telegram 网页版** 里完成绑定，请先打开网页版并 **登录**，再回到 CRM 点「绑定」。还没登录时，绑定链接往往打不开。手机 App 不需要这一步。
:::

### 第 1 步：打开通知设置，点「绑定」

1. 在 CRM **左下角**点 **通知设置**（铃铛）。
2. 找到 **Telegram**，点右侧 **绑定**。

![第 1 步：通知设置里点绑定](/guide/crm-telegram/crm_tg_notify.png)

### 第 2 步：打开 Telegram，用 /start 完成绑定

点 **打开 Telegram 完成绑定**。多数情况下，进入 Bot 对话后直接点 **START**，或自己输入 `/start` 发送即可。

**`/start` 后面没有一串代码：** 说明这个 Telegram 目前只绑这一个 CRM 账号。直接点 START 或输入 `/start`，不要再贴别的内容。

**`/start` 后面带着一串字符（专属命令）：** 只有 **多个 CRM 账号共用同一个 Telegram** 时才会出现（例如团队登录和客户门户都要收提醒）。这时必须把整段专属命令贴进同一个 Bot 对话，不能只点 START。

![第 2 步：打开 Telegram 完成绑定](/guide/crm-telegram/crm_tg_bind.png)

### 第 3 步：网页版点不开绑定链接时，改为搜索官方 Bot

如果无法直接打开绑定链接（例如浏览器提示网址无效），不要反复点链接。改为打开 Telegram，搜索 **Reguverse CRM**，点 **Reguverse CRM**（用户名必须是 **@reguversebot**），再按后面步骤点 START。

![第 3 步：搜索官方 Bot @reguversebot](/guide/crm-telegram/telegram_web_add.png)

### 第 4 步：打开 Bot

进入 Bot 主页后：

- 手机 App：点 **START BOT**
- 网页版：也可以点 **OPEN IN WEB**

![第 4 步：START BOT 或 OPEN IN WEB](/guide/crm-telegram/crm_tg_open_in_web.png)

### 第 5 步：点 START，或输入 /start

如果聊天是空的，点底部的 **START**。单账号绑定到这里就够了。

![第 5 步：点 START 或输入 /start](/guide/crm-telegram/crm_tg_openbot.png)

### 第 6 步：看到确认（仅多账号需要专属命令）

单账号：点 START 后，Bot 确认已绑定即可。

多账号共用同一个 Telegram：把第 2 步里带代码的整段 `/start ...` 贴进对话。Bot 回复类似 **Also linked...** 表示这个 Telegram 已同时接收多个登录的提醒，摘要会标注 **[CRO]** 或 **[客户门户]**。

![第 6 步：多账号绑定时看到 Also linked](/guide/crm-telegram/crm_tg_linked.png)

---

## 国内：由 CRO 添加钉钉群

国内客户一般**不需要**绑定 Telegram。

CRO 打开该客户的 **客户详情页**，在「钉钉客户群」里粘贴该客户钉钉群的自定义机器人 Webhook 和加签密钥（一个客户一个群，不是一个项目一个群）。该客户名下项目的公开频道消息会进这个群。

客户若要在钉钉里看到提醒，请让 CRO 把相关同事拉进这个钉钉群即可。

---

## 相关说明

- 浏览器桌面通知、提示音、关闭标签后的 Web Push，仍可在同一「通知设置」里打开。
- 助手账号与 CRM 的关系见 [助手与 CRM 的区别](./crm-and-assistant)。
