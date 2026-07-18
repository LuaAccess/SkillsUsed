---
name: client-relationship
description: Review, update, or act on client relationship and account health data across your CRM and connected apps. Use when checking where a deal stands, reviewing account health across your portfolio, planning follow-ups, identifying at-risk relationships, logging a client interaction, or doing a weekly account review. Trigger phrases include "how are my accounts", "where is [client] in the pipeline", "which clients need follow-up", "log this interaction", "account health check", "update HubSpot", "who haven't I spoken to", "CRM update", or "weekly account review". Do NOT use for drafting emails (client-communication), writing proposals (consulting-proposal), or customer support tickets (customer-support bundle).
metadata:
  argument-hint: "[all accounts | specific client name | deal stage | this week's review]"
---

# /client-relationship-tracker

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Review and manage your client relationships and sales pipeline — surfacing at-risk accounts, stale deals, and next-action gaps before they cost you.

## Usage

```
/client-relationship-tracker $ARGUMENTS
```

Examples:
- `/client-relationship-tracker weekly review — all active accounts`
- `/client-relationship-tracker log interaction — BDO IT team, discovery call today`
- `/client-relationship-tracker which deals have had no activity in 14+ days`
- `/client-relationship-tracker account health check — [Client Name]`

---

## Workflow

### 1. Determine Review Type

| Mode | What It Does |
|------|-------------|
| **Portfolio review** | Full account health sweep across all active clients |
| **Single account** | Deep-dive on one client — history, status, next move |
| **Interaction log** | Record a touchpoint and update CRM fields |
| **Stale deal scan** | Find deals with no activity past a threshold |
| **Follow-up plan** | Generate prioritised outreach list for the week |

---

### 2. Portfolio Review Output

```markdown
## Account Health Review — [Date]

### 🔴 Needs Immediate Attention
| Client | Issue | Last Contact | Recommended Action |
|--------|-------|--------------|-------------------|
| [Name] | [At-risk signal] | [Date] | [Action] |

### 🟡 Watch List
| Client | Signal | Last Contact | Recommended Action |
|--------|--------|--------------|-------------------|
| [Name] | [Soft signal] | [Date] | [Action] |

### 🟢 On Track
| Client | Stage | Last Contact | Next Step |
|--------|-------|--------------|-----------|
| [Name] | [Stage] | [Date] | [Action] |

### 📋 Deals by Stage
| Stage | Count | Total Value | Oldest Deal |
|-------|-------|-------------|-------------|
| Discovery | [N] | [₱/$ value] | [Days old] |
| Proposal Sent | [N] | [Value] | [Days old] |
| Negotiation | [N] | [Value] | [Days old] |
| Closed Won | [N] | [Value] | — |
| Closed Lost | [N] | [Value] | — |
```

---

### 3. Single Account Deep-Dive

```markdown
## Account: [Client Name]

**Industry:** [Industry]
**Key contacts:** [Name, Title] / [Name, Title]
**Deal stage:** [Current stage]
**Estimated value:** [Amount]
**Relationship age:** [How long you've known them]

### Interaction History (Last 90 Days)
| Date | Type | Summary | Outcome |
|------|------|---------|---------|
| [Date] | [Call/Email/Meeting] | [What happened] | [Result or next step] |

### Health Signals
- Last meaningful contact: [Date] — [🟢 Recent / 🟡 Aging / 🔴 Stale]
- Client engagement level: [High / Medium / Low / Unknown]
- Open commitments: [What you owe them / What they owe you]
- Relationship temperature: [Warm / Neutral / Cold / Unknown]

### Cultural Notes
[Any relationship dynamics specific to this account — hierarchy, who the real decision-maker is, relationship history, communication preferences, sensitivity areas]

### Recommended Next Move
[Single most important action with rationale and timing]
```

---

### 4. Interaction Log

When logging a new touchpoint, capture:

```
Client: [Name]
Date: [Today]
Channel: [Call / Email / Meeting / Teams / In-person]
Attendees: [Who was there]
Summary: [2–3 sentences — what was discussed, decided, or left open]
Commitments made by you: [What you said you'd do]
Commitments made by client: [What they said they'd do]
Sentiment read: [Warm / Neutral / Cautious / Positive / Concerned]
Next step: [Action + Owner + Date]
CRM fields to update: [Stage / Value / Close date / Contact notes]
```

---

### 5. At-Risk Signals Checklist

Flag accounts that show any of these:

- [ ] No contact in 21+ days (active deal) or 45+ days (existing client)
- [ ] Client missed a scheduled call or meeting without rescheduling
- [ ] Proposal sent 14+ days ago with no response
- [ ] Client stopped responding to emails after 2+ attempts
- [ ] Champion contact left or changed roles
- [ ] Client mentioned a competitor in conversation
- [ ] Payment overdue or billing question unresolved
- [ ] Scope creep or delivery issue not yet resolved
- [ ] Key stakeholder went quiet after previously being engaged

**Philippine market additions:**
- Client cancelled a face-to-face meeting twice → declining interest signal, not scheduling conflict
- Response language shifted from warm/personal to formal → relationship cooling
- Introductions to other internal stakeholders stopped → gating access, reassessing fit

---

## If Connectors Available

**HubSpot:**
- Pull all active deals and contact records
- Log new interaction as CRM activity
- Update deal stage, close date, and contact notes
- Set follow-up tasks and reminders
- Flag deals with no activity past threshold

**Microsoft 365 / Outlook:**
- Scan recent emails from client contacts for sentiment and open items
- Surface any unanswered emails

**Microsoft 365 / Calendar:**
- Check scheduled meetings with each account
- Identify accounts with no upcoming touchpoints

**Asana / monday.com:**
- Surface open tasks linked to client accounts
- Flag overdue deliverables that may affect relationship health

**Notion:**
- Pull or update client meeting notes and relationship context

---

## Weekly Account Review Protocol

Run this every Monday (or your start-of-week day):

1. **Pull all active deals** — stage, value, last activity date
2. **Flag stale deals** — no activity in 14+ days
3. **Check open commitments** — what did you promise to send or do last week
4. **Identify this week's priority contacts** — who needs a touchpoint
5. **Generate outreach plan** — ordered by urgency and deal value
6. **Update CRM** — close date, stage, and notes current

---

## Tips

1. **Consistency beats intensity.** A short check-in every 2 weeks beats a deep-dive every 3 months. Clients notice absence.
2. **Log immediately after every interaction.** Memory degrades fast — especially for cultural signals and soft commitments.
3. **Relationship health is not the same as deal health.** A deal can be progressing while the relationship is cooling. Track both.
4. **In Philippine business culture:** the relationship IS the pipeline. A warm client who trusts you will create opportunities. A transactional client who doesn't will stall every deal at procurement.
