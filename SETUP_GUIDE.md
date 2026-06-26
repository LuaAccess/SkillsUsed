# Pipeline Setup Guide
## LuaAccess Morning Briefing — GitHub Actions

---

## What This Guide Covers
Setting up the 4 GitHub Secrets needed to run both pipelines.
No secrets = pipelines fetch data but cannot deliver email or create Notion pages.

---

## Step 1 — Go to GitHub Secrets

1. Go to `https://github.com/LuaAccess/SkillsUsed`
2. Click **Settings** tab
3. Click **Secrets and variables** → **Actions**
4. Click **New repository secret** for each secret below

---

## Step 2 — Add These 4 Secrets

### Secret 1: RECIPIENT_EMAIL
Your Outlook email address where briefings will be delivered.

```
Name:  RECIPIENT_EMAIL
Value: your-email@yourdomain.com
```

---

### Secret 2: MS_GRAPH_TOKEN
Microsoft Graph API token — allows GitHub Actions to send email via your Outlook.

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

```
Name:  MS_GRAPH_TOKEN
Value: [your bearer token]
```

---

### Secret 3: NOTION_TOKEN
Notion integration token — allows GitHub Actions to create pages in your Notion.

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
The ID of the Notion database where intel brief pages will be created.

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

## Step 4 — Test the Pipeline Manually

1. Go to `https://github.com/LuaAccess/SkillsUsed/actions`
2. Click **Morning Intel Brief** workflow
3. Click **Run workflow** → **Run workflow**
4. Watch the logs — each step should show ✅
5. Check your Outlook inbox for the email
6. Check Notion for the new page

---

## Step 5 — Verify Gate Tests

| Check | Expected | How to verify |
|---|---|---|
| Workflow runs without errors | All steps green | GitHub Actions logs |
| Email arrives in Outlook | Subject: "🌏 Intel Brief — [Date]" | Outlook inbox |
| Notion page created | Title: "Intel Brief — [Date]" | Notion database |
| RSS data populated | At least 3 headlines visible | Email body |
| CVEs populated | At least 1 CVE listed | Email body |
| Forex rates shown | USD/PHP rate visible | Email body |

---

## Troubleshooting

| Error | Cause | Fix |
|---|---|---|
| `MS Graph 401` | Token expired or wrong | Re-generate token, update secret |
| `Notion 401` | Wrong token | Check NOTION_TOKEN value |
| `Notion 404` | Database not shared with integration | Step 3 above |
| `RSS empty` | Source temporarily down | Check source URL manually |
| `NVD timeout` | NVD API slow | Increase timeout in script or retry |

---

## Schedule

Intel Brief: Daily at 6:00 AM PHT (every day including weekends)
Work Brief: Monday-Friday at 6:00 AM PHT only

Cron reference:
- `0 22 * * *`   = 6AM PHT daily
- `0 22 * * 1-5` = 6AM PHT weekdays only

---

## After Setup — Use Live Data with Claude

When email arrives each morning:
1. Open the Intel Brief email
2. Copy the content
3. Go to Claude.ai
4. Paste content + type: **"intel brief on this"**
5. Claude applies full IT consulting analysis + PH opportunity radar

This is the full zero-cost pipeline — live data + AI analysis, ₱0 ongoing cost.
