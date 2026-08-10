# Reguverse Assistant vs CRM: What's the Difference?

Users who open the [CRM portal access request page](https://crm.reguverse.com/request-access) often ask: **Are Assistant and CRM two different platforms? If I already have an Assistant account, do I need to apply again? Are quotas mixed together?**  
This page explains the relationship and what existing Reguverse Assistant users should do.

## Short answer

| | **Reguverse Assistant** | **Reguverse CRM** |
|---|---|---|
| What it is | AI regulatory documentation tool (Word add-in / web) | CRO client collaboration and project operations portal |
| Primary users | RA / manufacturers building docs themselves | CRO teams and their clients |
| AI capability | Native workflows and document generation | **Calls the same Assistant API** (same generation engine) |
| Account | Reguverse account (email login) | **Same Reguverse account** (SSO) |
| "Request portal access" | N/A | Client onboarding to collaborate with a CRO — **not** a second Assistant purchase |

They are **not the same product surface**, but they share **identity and AI**. CRM does not replace Assistant, and applying for portal access is not "buying another unrelated AI product."

## What is Reguverse Assistant?

**Reguverse Assistant** (also referred to internally as docmcp) is the AI documentation product:

- Run AI workflows in Microsoft Word or on the web (clinical evaluation, risk management, GSPR, NMPA, and more)
- Plan tiers control features and **Credits**
- Built for manufacturers and consultants who use the tool directly

See [Plans & Pricing](./pricing) and [Quick Start](./get-started).

## What is Reguverse CRM?

**Reguverse CRM** ([crm.reguverse.com](https://crm.reguverse.com)) is the operations platform for **CRO / consulting firms**:

- Clients, projects, tasks, quotes, invoices, messaging, forms
- **Client portal**: progress, document confirmation, uploads, assigned tasks
- CRO users can trigger the same AI document capabilities via the Assistant API

The **CRO plan** in the Assistant pricing matrix additionally unlocks CRM (see [Plans & Pricing](./pricing)).  
A client's "portal access" request is for joining a **CRO collaboration space**, not for purchasing a standalone Assistant subscription.

## Already have an Assistant account?

1. Use the **same email** on [Request Portal Access](https://crm.reguverse.com/request-access).
2. After CRO / platform approval, accept the invite with your **existing** Reguverse password — no separate unrelated account.
3. You receive **client portal permissions** (projects, tasks, messages, document confirmation). This does **not** turn you into a CRO and does **not** replace your Assistant subscription.
4. If you only use Assistant yourself and do not need to collaborate with a CRO in CRM, you usually **do not** need to request portal access.

::: tip Login entry points
- Assistant: Word add-in / Assistant web (e.g. `app.reguverse.com`)
- CRM: `https://crm.reguverse.com` (same email; CRM uses email OTP as the second factor, separate from Authenticator TOTP on the Assistant channel)
:::

## How do Credits work?

Common confusion from support chats:

- **Using Assistant yourself**: workflows and document generation consume **your (or your org's) plan Credits**. Usage scales with workload (more literature / longer docs cost more). See [Plans & Pricing · Credits](./pricing#credits).
- **Generation via CRM by a CRO**: AI still uses the same Assistant API; billing follows the **account that initiates the call** (typically the CRO team's Credits). Requesting portal access itself does **not** spend Assistant Credits.
- **Fixed consulting contracts vs tool Credits**: A project-period / fixed-fee consulting agreement is a **commercial service arrangement**. Assistant Credits remain a **tool usage meter**. Do not treat service fees as unlimited AI, or Credits as the consulting quote.

::: info Document features on CRO collaboration projects
In the CRM client portal, project tasks created and run by the **CRO** can use the full advanced document capabilities of the CRO plan (Max-tier features + CRM). AI generation uses the **CRO team's Credits and permissions**, not the client's own Assistant tier. If a client separately uses their own Assistant account outside that collaboration, their own plan and Credits still apply.
:::

## FAQ

### Are these two platforms different?

**Different purpose, same AI engine.**  
Assistant = AI documentation tool; CRM = CRO operations + client portal. Generation capability is the same (CRM calls the Assistant API). Login uses the same Reguverse identity.

### I already have Assistant — should I still apply?

Only if you need to collaborate with a CRO / platform team in CRM. Use the same email when applying.

### Will portal access overwrite my Assistant subscription?

No. Portal access is a collaboration permission and is independent of your Assistant plan (unless you separately change subscriptions).

### Will CRM document generation drain my personal Assistant Credits?

No — requesting portal access does not spend Credits. When the CRO creates project tasks and generates documents in CRM, that uses the **CRO team's Credits and advanced feature permissions**. Your own plan Credits are only used when you operate Assistant under your own account.

## Related links

- [Request CRM portal access](https://crm.reguverse.com/request-access)
- [CRM login](https://crm.reguverse.com/login)
- [Plans & Pricing](./pricing)
- [Register & Login](./register)
- [Account Management](./account)
