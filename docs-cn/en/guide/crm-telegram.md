# CRM alerts: Telegram (overseas) and DingTalk (China)

After you sign in to [Reguverse CRM](https://crm.reguverse.com), you can still get short alerts when the tab is closed. The channel depends on where you work:

| Where you are | How you get alerts | Who sets it up |
|---|---|---|
| **Overseas** (team or client login) | Personal Telegram via official bot **@reguversebot** | You bind it in the sidebar |
| **Clients in China** | That client's **DingTalk group** | The **CRO adds the group bot on the client page**. Clients do not bind a bot themselves |

Alerts are a short summary plus a link into CRM. **Full confidential message text is never pushed.**

---

## Overseas: bind Telegram

This takes about a minute. Use Telegram on your phone or computer.

### Step 1: Open Notification Settings and tap Bind

1. At the **bottom-left** of CRM, open **Notification Settings** (bell).
2. Find **Telegram** and tap **Bind** on the right.

![Step 1: Bind in Notification Settings](/guide/crm-telegram/crm_tg_notify.png)

### Step 2: Copy your personal command

CRM shows a command that starts with `/start` (unique each time). **Copy the whole command.**  
You can also tap **Open Telegram to finish linking**. If the browser says the URL is invalid, tap OK, then open the bot with the steps below.

![Step 2: Copy the /start command](/guide/crm-telegram/crm_tg_bind.png)

One Telegram account can link **both** your team login and your client-portal login. Bind on the other side too, then paste the **new** command in the same bot chat.

### Step 3: Find the official bot in Telegram

Open Telegram, search for **Reguverse CRM**, and open **Reguverse CRM** — the username must be **@reguversebot**.

![Step 3: Search for Reguverse CRM / @reguversebot](/guide/crm-telegram/telegram_web_add.png)

### Step 4: Open the bot

On the bot profile:

- Mobile app: tap **START BOT**
- Telegram Web: you can tap **OPEN IN WEB**

![Step 4: START BOT or OPEN IN WEB](/guide/crm-telegram/crm_tg_open_in_web.png)

::: warning Do not rely on START BOT for a second login
If you already started this bot (for example you linked your team login and now want the client portal too), **do not only tap START BOT**. Go back to CRM, copy the new `/start ...` command, and paste it in the same chat.
:::

### Step 5: Start the chat

If the chat is empty, tap **START** at the bottom.

![Step 5: Tap START](/guide/crm-telegram/crm_tg_openbot.png)

### Step 6: Paste the command and wait for confirmation

Paste the `/start ...` command from Step 2 and send it. A reply like **Also linked...** means you are done. Later alerts are tagged **[CRO]** or **[Client portal]** so you can tell which login they belong to.

![Step 6: Linked successfully](/guide/crm-telegram/crm_tg_linked.png)

---

## China: the CRO adds a DingTalk group

Clients in China usually **do not** bind Telegram.

The CRO opens that client's **client detail** page and pastes the DingTalk custom-robot webhook and sign secret for **that client's group** (one group per client, not per project). Public-channel messages for that client's projects go to this group.

If client colleagues need the alerts, the CRO adds them to the DingTalk group.

---

## Related

- Desktop notifications, sound, and Web Push (closed tabs) are in the same Notification Settings panel.
- How Assistant and CRM relate: [Assistant vs CRM](./crm-and-assistant).
