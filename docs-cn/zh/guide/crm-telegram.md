# CRM 消息提醒：海外 Telegram 与国内钉钉

登录 [Reguverse CRM](https://crm.reguverse.com) 后，关闭网页也能收到项目消息摘要。渠道按地区分开：

| 您在哪里 | 怎么收提醒 | 谁来设置 |
|---|---|---|
| **海外**（团队成员或客户） | 个人 Telegram，官方 Bot **@reguversebot** | 您自己在侧栏绑定 |
| **国内客户** | 该客户的 **钉钉群** | **CRO 在客户详情页添加群机器人**，客户不用自己绑 Bot |

提醒只含摘要和打开 CRM 的链接，**不会**推送机密全文。

---

## 海外：绑定 Telegram

大约一分钟。手机或电脑上的 Telegram 都可以。

### 第 1 步：打开通知设置，点「绑定」

1. 在 CRM **左下角**点 **通知设置**（铃铛）。
2. 找到 **Telegram**，点右侧 **绑定**。

![第 1 步：通知设置里点绑定](/guide/crm-telegram/crm_tg_notify.png)

### 第 2 步：复制专属命令

绑定后会出现一段以 `/start` 开头的命令（每人每次都不一样）。**请整段复制**。  
也可以点 **打开 Telegram 完成绑定**。若浏览器提示「网址无效」，点「好」，然后按下面步骤手动打开 Bot。

![第 2 步：复制 /start 命令](/guide/crm-telegram/crm_tg_bind.png)

同一个 Telegram 可以同时绑定 **团队登录** 和 **客户门户**。另一侧也要再点一次绑定，并把**新命令**贴进同一个 Bot 对话。

### 第 3 步：在 Telegram 里搜索官方 Bot

打开 Telegram，在搜索框输入 **Reguverse CRM**，点搜索结果里的 **Reguverse CRM**（用户名必须是 **@reguversebot**）。

![第 3 步：搜索 Reguverse CRM / @reguversebot](/guide/crm-telegram/telegram_web_add.png)

### 第 4 步：打开 Bot

进入 Bot 主页后：

- 手机 App：点 **START BOT**
- 网页版：也可以点 **OPEN IN WEB**

![第 4 步：START BOT 或 OPEN IN WEB](/guide/crm-telegram/crm_tg_open_in_web.png)

::: warning 第二次绑定不要只点 START BOT
如果您已经和这个 Bot 聊过（例如团队账号绑过了，现在要再绑客户门户），**不要只点 START BOT**。必须回到 CRM 复制新的 `/start ...` 命令，贴进同一个对话。
:::

### 第 5 步：开始对话

如果聊天是空的，点底部的 **START**。

![第 5 步：点 START 开始对话](/guide/crm-telegram/crm_tg_openbot.png)

### 第 6 步：粘贴命令，看到确认

把第 2 步复制的 `/start ...` 整段粘贴发送。Bot 回复类似 **Also linked...** 即绑定成功。之后会收到带 **[CRO]** 或 **[客户门户]** 标记的摘要，方便区分是哪一侧登录。

![第 6 步：绑定成功](/guide/crm-telegram/crm_tg_linked.png)

---

## 国内：由 CRO 添加钉钉群

国内客户一般**不需要**绑定 Telegram。

CRO 打开该客户的 **客户详情页**，在「钉钉客户群」里粘贴该客户钉钉群的自定义机器人 Webhook 和加签密钥（一个客户一个群，不是一个项目一个群）。该客户名下项目的公开频道消息会进这个群。

客户若要在钉钉里看到提醒，请让 CRO 把相关同事拉进这个钉钉群即可。

---

## 相关说明

- 浏览器桌面通知、提示音、关闭标签后的 Web Push，仍可在同一「通知设置」里打开。
- 助手账号与 CRM 的关系见 [助手与 CRM 的区别](./crm-and-assistant)。
