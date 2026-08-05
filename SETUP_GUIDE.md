# Pipeline Setup Guide
## LuaAccess Morning Briefing — GitHub Actions

---

## What This Guide Covers
Setting up the GitHub Secrets needed to run both pipelines:
- **Intel Brief** — 4 secrets (unchanged)
- **Work Brief** — reuses `MS_GRAPH_TOKEN` + `NOTION_TOKEN`/`NOTION_DATABASE_ID`, plus **6 new secrets** for HubSpot, Asana, Monday.com, and Jira

No secrets = pipelines fetch what they can and cannot deliver email/Notion.
For Work Brief specifically: **missing an individual secret does not break the run** — that section just prints "connector unavailable — check manually" instead of real data. Add secrets one at a time and re-run to confirm each section lights up.

---

## Step 1 — Go to GitHub Secrets

1. Go to `https://github.com/LuaAccess/SkillsUsed`
2. Click **Settings** tab
3. Click **Secrets and variables** → **Actions**
4. Click **New repository secret** for each secret below

---

## Step 2 — Intel Brief Secrets (4, unchanged)

### Secret 1: RECIPIENT_EMAIL
Your Outlook email address where briefings will be delivered.

```
Name:  RECIPIENT_EMAIL
Value: your-email@yourdomain.com
```

---

### Secret 2: MS_GRAPH_TOKEN
Microsoft Graph API token — allows GitHub Actions to send email via your Outlook, and now also read your Calendar and Inbox for Work Brief.

**How to get it:**

Option A — Azure App Registration (permanent, recommended):
1. Go to `https://portal.azure.com`
2. Azure Active Directory → App registrations → New registration
3. Name: "LuaAccess Morning Brief"
4. Supported account types: Single tenant
5. Register
6. API permissions → Add permission → Microsoft Graph → Delegated
7. Add: `Mail.Send`, `Calendars.Read`, `Mail.Read`
8. Grant admin consent
9. Certificates & secrets → New client secret → Copy value
10. Use client credentials flow to get bearer token

Option B — Use existing Microsoft 365 MCP token (temporary):
Your Microsoft 365 MCP connector already has a token.
Check `https://claude.ai/settings/connectors` → Microsoft 365 → connection details.
Note: This token expires — Option A is more reliable long-term.

**Note:** the scopes above (`Mail.Send`, `Calendars.Read`, `Mail.Read`) already cover everything `work_brief.py` needs — no separate M365 token required.

```
Name:  MS_GRAPH_TOKEN
Value: [your bearer token]
```

---

### Secret 3: NOTION_TOKEN
Notion integration token — allows GitHub Actions to create pages in your Notion. Used by both pipelines.

**How to get it:**
1. Go to `https://www.notion.so/my-integrations`
2. Click **New integration**
3. Name: "LuaAccess Morning Brief"
4. Select your workspace
5. Permissions: Read content, Insert content, Update content
6. Submit → Copy the **Internal Integration Token**

```
Name:  NOTION_TOKEN
Value: secret_xxxxxxxxxxxx
```

---

### Secret 4: NOTION_DATABASE_ID
The ID of the Notion database where brief pages will be created. Used by both pipelines — Intel Brief and Work Brief pages land in the same database, distinguished by title prefix ("Intel Brief —" vs "Work Brief —").

**How to get it:**
1. Open Notion → create a new database called "Morning Intel Briefs"
2. Open the database as a full page
3. Copy the URL — it looks like:
   `https://www.notion.so/yourworkspace/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX?v=...`
4. The 32-character string after the last `/` and before `?` is the database ID

```
Name:  NOTION_DATABASE_ID
Value: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

## Step 3 — Share Notion Database with Integration

1. Open your "Morning Intel Briefs" database in Notion
2. Click **...** (top right) → **Connections**
3. Find "LuaAccess Morning Brief" integration → Connect

Without this step, the Notion token works but cannot access the database.

---

## Step 4 — Work Brief Secrets (6 new)

Each of these is independent — add one, re-run the workflow, confirm that section of the brief goes from "connector unavailable" to real data, then move to the next.

### Secret 5: HUBSPOT_TOKEN
HubSpot Private App access token — read-only on deals.

**How to get it:**
1. In HubSpot, click the **Settings** gear icon
2. Left sidebar → **Integrations** → **Private Apps**
3. **Create a private app** → Name: "LuaAccess Morning Brief"
4. **Scopes** tab → add `crm.objects.deals.read`
5. Create app → Copy the **Access Token** (shown once)

```
Name:  HUBSPOT_TOKEN
Value: pat-xxxxxxxxxxxxxxxxxxxx
```

---

### Secret 6: ASANA_TOKEN
Asana Personal Access Token (PAT).

**How to get it:**
1. Go to `https://app.asana.com/0/my-apps`
2. **Create new token** → Name: "LuaAccess Morning Brief"
3. Copy the token immediately — Asana only shows it once

```
Name:  ASANA_TOKEN
Value: 2/xxxxxxxxx/xxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

### Secret 7: MONDAY_TOKEN
Monday.com API v2 personal token.

**How to get it:**
1. In monday.com, click your avatar (bottom-left) → **Administration** (or **Developers**)
2. Find **API** in the left menu
3. Copy your **API v2 Token**

⚠️ This token carries your full account access scope in Monday's model — there's no read-only/deals-only equivalent to HubSpot's private app scopes. Treat it like a password.

```
Name:  MONDAY_TOKEN
Value: eyJhbGc...
```

**Heads up:** Monday's "status" column labels and structure are custom per board. The script scans every board's "Status" column for `blocked`/`stuck`/`due today` — if your boards use different labels, that section may come back empty even with a valid token. Tell me your actual board/column names and I'll tune the query.

---

### Secrets 8–10: JIRA_DOMAIN, JIRA_EMAIL, JIRA_API_TOKEN
Atlassian API token, paired with your account email and workspace domain.

**How to get it:**
1. Go to `https://id.atlassian.com/manage-profile/security/api-tokens`
2. **Create API token** → Name: "LuaAccess Morning Brief" → Copy it
3. `JIRA_EMAIL` = the Atlassian account email you used to create the token
4. `JIRA_DOMAIN` = your workspace subdomain only — e.g. `yourcompany.atlassian.net` — **no `https://`, no trailing slash**

```
Name:  JIRA_DOMAIN
Value: yourcompany.atlassian.net

Name:  JIRA_EMAIL
Value: your-email@yourdomain.com

Name:  JIRA_API_TOKEN
Value: ATATTxxxxxxxxxxxxxxxx
```

---

## Step 5 — Test the Pipelines Manually

1. Go to `https://github.com/LuaAccess/SkillsUsed/actions`
2. Click **Morning Intel Brief** workflow → **Run workflow** → **Run workflow**
   - Watch logs, check Outlook + Notion
3. Click **Morning Work Brief** workflow → **Run workflow** → **Run workflow**
   - Watch logs — each of the 7 steps prints its own status line
   - Any section without a secret set will log `⚠️ [Source] unavailable: ... not set` — this is expected, not a failure
   - Check Outlook inbox and Notion for the Work Brief

---

## Step 6 — Verify Gate Tests

| Check | Expected | How to verify |
|---|---|---|
| Intel Brief workflow runs without errors | All steps green | GitHub Actions logs |
| Intel email arrives | Subject: "🌏 Intel Brief — [Date]" | Outlook inbox |
| Intel Notion page created | Title: "Intel Brief — [Date]" | Notion database |
| RSS data populated | At least 3 headlines visible | Email body |
| CVEs populated | At least 1 CVE listed | Email body |
| Forex rates shown | USD/PHP rate visible | Email body |
| Work Brief workflow runs without errors | All steps green (⚠️ warnings for unset secrets are OK) | GitHub Actions logs |
| Work email arrives | Subject: "📋 Work Brief — [Date]" | Outlook inbox |
| Work Notion page created | Title: "Work Brief — [Date]" | Notion database |
| Each section shows data OR "connector unavailable" | Never blank, never crashes the run | Email body |
| Calendar times are in PHT, not UTC | Meeting times match your actual day | Email body vs. real calendar |

---

## Troubleshooting

| Error | Cause | Fix |
|---|---|---|
| `MS Graph 401` | Token expired or wrong | Re-generate token, update secret |
| `Notion 401` | Wrong token | Check NOTION_TOKEN value |
| `Notion 404` | Database not shared with integration | Step 3 above |
| `RSS empty` | Source temporarily down | Check source URL manually |
| `NVD timeout` | NVD API slow | Increase timeout in script or retry |
| `HubSpot 401` | Private app token wrong or scope missing | Regenerate in HubSpot → Private Apps, confirm `crm.objects.deals.read` scope |
| `Asana 401` | PAT revoked or mistyped | Regenerate at `app.asana.com/0/my-apps` |
| Monday section empty despite valid token | Board/column names don't match script's assumptions | Send actual board + status column names for tuning |
| `Jira 401` | JIRA_EMAIL doesn't match the account that made the token | Confirm the pairing |
| `Jira 404` | Wrong JIRA_DOMAIN format | Must be exactly `yoursite.atlassian.net` — no protocol, no slash |
| A section reads "connector unavailable — check manually" | That secret just isn't set yet | Add the missing secret — this is the script degrading gracefully, not an error |

---

## Schedule

Intel Brief: Daily at 6:00 AM PHT (every day including weekends)
Work Brief: Monday–Friday at 6:00 AM PHT only

Cron reference:
- `0 22 * * *`   = 6AM PHT daily
- `0 22 * * 1-5` = 6AM PHT weekdays only

---

## After Setup — Use Live Data with Claude

**Intel Brief** (raw RSS, needs AI analysis):
1. Open the Intel Brief email → copy the content
2. Go to Claude.ai → paste content + type: **"intel brief on this"**
3. Claude applies full IT consulting analysis + PH opportunity radar

**Work Brief** (already structured, ready to act on):
1. Open the Work Brief email
2. It's already prioritized and scannable — no AI pass required
3. Optionally paste it into Claude with a specific ask ("help me draft a reply to the flagged client email") if you want to act on one item

This is the full zero-cost pipeline — live data + AI analysis, ₱0 ongoing cost.
