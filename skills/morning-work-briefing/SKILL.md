---
name: morning-work-briefing
description: "Pull a structured daily work briefing from all connected apps. Use when the user says 'work brief', 'good morning work', 'start my day', 'what do I have today', or 'morning briefing'. Pulls Microsoft 365 calendar and email, HubSpot deals, Asana tasks, Notion meeting notes, Monday.com project status, and Atlassian Jira issues. Delivers a single scannable briefing prioritised by urgency. Do NOT use for intel or news briefings — use morning-intel-briefing instead."
---

# Morning Work Briefing Skill

Delivers a single scannable work briefing from all connected apps — prioritised by urgency, mobile-optimised, readable in under 2 minutes.

## Trigger Phrases
- "work brief"
- "good morning work"
- "start my day"
- "what do I have today"
- "morning briefing"
- "show me my day"

## Pull Sequence

Execute in this exact order — most urgent data first:

### Step 1 — Microsoft 365 Calendar
Pull: All events for today (date = current date PHT)
Extract: Start time, title, attendees, location/link
Flag: Any meeting starting within 60 minutes — mark 🔴

### Step 2 — Microsoft 365 Outlook
Pull: Unread emails received in last 24 hours
Filter: Prioritise emails from known client domains and direct reports
Flag: Any email older than 4 hours unread from a client — mark 🔴

### Step 3 — HubSpot
Pull: Deals with activity in last 24 hours + deals with close date within 7 days
Extract: Deal name, stage, amount, next action
Flag: Any deal overdue on next action — mark 🔴

### Step 4 — Asana
Pull: Tasks assigned to me due today + overdue tasks
Extract: Task name, project, due date
Flag: Overdue tasks — mark ⚠️

### Step 5 — Notion
Pull: Pages updated in last 24 hours tagged as meeting notes or action items
Extract: Page title, key action items if visible

### Step 6 — Monday.com
Pull: Items assigned to me that are blocked or due today
Extract: Item name, board, status

### Step 7 — Atlassian Jira
Pull: Issues assigned to me with status In Progress or To Do
Extract: Issue key, summary, priority

## Output Format

Deliver in this exact structure — headers, short lines, mobile-optimised:

---

```
════════════════════════════════
WORK BRIEF — [Weekday], [Date]
Generated: [Time] PHT
════════════════════════════════

🔴 CRITICAL — Act First
• [Item] | [Source] | [Action]
(If none: "Nothing critical right now.")

📅 TODAY'S MEETINGS ([N] total)
• [HH:MM] [Title] — [Location/Link]
• [HH:MM] [Title] — [Attendees if <4 people]
(Prep note if meeting is within 60 min)

📬 EMAILS NEEDING REPLY ([N])
• [Sender] — [Subject] — [Received X hrs ago]
(Flag client emails separately)

💼 DEALS TO WATCH ([N])
• [Deal Name] — [Stage] — [Close: Date]
  → Next action: [What needs to happen]

✅ TASKS DUE TODAY ([N])
• [Task] — [Project]

⚠️ OVERDUE / BLOCKED ([N])
• [Item] — [Source] — [X days overdue]

📝 CONTEXT
• [Notion page or action item worth noting]

════════════════════════════════
SUMMARY
Meetings: [N] | Emails: [N] | Tasks: [N]
Top priority: [Single most important thing]
════════════════════════════════
```

## Rules

- If a section has no items → show it with "None" — do not hide empty sections
- Never exceed 400 words total output
- Every item must have a source label (Outlook / HubSpot / Asana / Notion / Monday / Jira)
- CRITICAL section = items that will damage a deal, client relationship, or deadline if not handled in the next 2 hours
- Do not summarise emails — show sender + subject line only
- Time must always be in PHT (UTC+8)

## Quality Checks

- [ ] Calendar shows today's date in PHT — not UTC
- [ ] CRITICAL section is honest — not everything is critical
- [ ] Deal next actions are specific — not "follow up"
- [ ] Total output under 400 words
- [ ] Summary line names one single top priority

## Gotchas

**Trigger conflicts:**
- This skill is for work apps only. For news and intelligence, use `morning-intel-briefing`.
- If user says just "good morning" without "work" — confirm which briefing they want before running.

**Known failure modes:**
- Microsoft 365 calendar sometimes returns UTC times — always convert to PHT (UTC+8) before displaying.
- HubSpot may return deals with no next action set — flag these as "next action missing" rather than skipping them.
- Asana may return completed tasks if filter is not applied — only show incomplete tasks.
- If any connector returns an error — show the section header with "connector unavailable — check manually" rather than silently skipping.
- Monday.com and Jira tend to have the most items — cap each at 5 items maximum, sorted by urgency.

**Filipino/Asian work context:**
- Client emails received late night (10PM-6AM PHT) should be flagged — Philippine clients who email outside hours often have urgent issues they are too polite to call about.
- "No response needed" emails from Philippine clients are often not — if a client sends any update, a brief acknowledgement is expected within the same business day.
- Meetings with no agenda attached are common in PH enterprise — flag these so you can set expectations before joining.

## Example Output Trigger

User: "work brief"
→ Claude executes Steps 1-7 in sequence
→ Delivers formatted briefing
→ Ends with: "Anything you want me to dig into from the above?"
