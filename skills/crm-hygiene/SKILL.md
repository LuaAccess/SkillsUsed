---
name: crm-hygiene
description: "Turn a meeting debrief, call notes, or raw client signals into concrete CRM updates — deal stage changes, contact/stakeholder record updates, activity logs, and follow-up tasks. Use after meeting-intelligence has produced a debrief, or any time you say 'update the CRM', 'log this in HubSpot', 'clean up this deal record', or 'what needs updating after that call'. Produces a specific, field-by-field change list (not a summary) ready to apply via the HubSpot connector, plus any Asana/monday.com follow-up tasks. Do NOT use this for the meeting analysis itself — that's meeting-intelligence, and should run first. Do NOT use this for renewal or proposal strategy — that's renewal-playbook or proposal-writer, and should run after this."
---

# CRM Hygiene Skill

The unglamorous middle step that most pipelines skip: turning a good meeting debrief into an actually-updated CRM. A debrief that stays in chat and never reaches HubSpot is worthless three weeks later when you can't remember why a deal stalled.

## Required Inputs

- **Source material** — meeting-intelligence output, raw notes, or a description of what happened
- **Account/deal name** in HubSpot (or enough detail to find it)
- **Current deal stage** (if known — otherwise this skill will flag it as unknown and ask)
- **Any explicit commitments made** (by you or the client) during the interaction

## What counts as CRM hygiene here

1. **Deal stage** — has anything happened that should move the stage forward, backward, or flag it at risk?
2. **Contact/stakeholder records** — new people identified, role changes, sentiment shifts, departures
3. **Activity log** — a factual, dated record of what happened (not the full debrief — a CRM-appropriate summary)
4. **Next steps as tasks** — every commitment becomes a task with an owner and a due date, not a note buried in an activity log
5. **Flags** — anything that should trigger a downstream skill (renewal risk → flag for `renewal-playbook`, new expansion signal → flag for `account-plan`)

## Output Structure

---

### CRM Update: [Account/Deal Name]

**Deal stage change:** [Current] → [Proposed] — *reason: [one sentence]* — *(flag if uncertain: "confirm before applying")*

**Contact record updates:**

| Contact | Field | Old value | New value | Source |
|---|---|---|---|---|
| [Name] | [Role / Sentiment / Influence] | [Old] | [New] | [What in the meeting justified this] |

**Activity log entry** (ready to paste into HubSpot):
> [Date] — [Meeting type] with [attendees]. [2-3 factual sentences: what was discussed, what was decided, what's open.]

**Follow-up tasks:**

| Task | Owner | Due | Tool |
|---|---|---|---|
| [Specific action] | [Name] | [Date] | Asana / monday.com / Outlook |

**Downstream flags:**
- [ ] Renewal risk identified → route to `renewal-playbook`
- [ ] Expansion signal identified → route to `account-plan`
- [ ] Health score should be re-run → route to `cs-health-scorecard`
- [ ] None — routine update only

---

## If Connectors Available

**HubSpot:** apply the deal stage change and contact field updates directly; log the activity entry against the deal/contact record. Confirm with the user before applying a deal-stage change if the source material left the reason ambiguous.

**Asana / monday.com:** create the follow-up tasks with owner and due date as separate items, not bundled into one note.

**Notion:** if a meeting-intelligence debrief note already exists, link this CRM update back to it rather than duplicating the analysis.

## Quality Checks

- [ ] Every proposed field change cites what in the source material justified it — no invented updates
- [ ] Deal stage change has a stated reason, or is explicitly flagged as unconfirmed
- [ ] Activity log entry is factual and dated — not a re-run of the full meeting-intelligence analysis
- [ ] Every commitment mentioned in the source material becomes a task with an owner and due date
- [ ] Downstream flags are checked, not left blank by default

## Anti-Patterns

- [ ] Do not paste the full meeting-intelligence debrief into the CRM activity log — summarize to what a future reader (possibly not you) needs
- [ ] Do not invent a deal-stage change without a stated trigger — if unclear, flag for confirmation instead of guessing
- [ ] Do not leave commitments as prose in the activity log instead of as tracked tasks
- [ ] Do not skip contact record updates just because the deal stage didn't change — sentiment and role changes matter even in a quiet quarter

## Gotchas

**Trigger conflicts:**
- This is the middle of a three-step chain: `meeting-intelligence` (analyze the meeting) → `crm-hygiene` (this skill — update the system of record) → `renewal-playbook` or `proposal-writer` (act on what the flags surface). Don't skip straight from analysis to strategy without this step, or the CRM silently goes stale.
- If there's no prior meeting-intelligence output and the user just wants a quick field update, that's fine — this skill works standalone too, it just won't have a debrief to draw signals from.

**Known failure modes:**
- Deal stage changes are the riskiest part — Claude may over-infer momentum from a merely polite meeting. If the source material is ambiguous, default to flagging for confirmation rather than advancing the stage.
- Contact sentiment updates are easy to get wrong from a single data point. Weight recent signals against the existing record rather than overwriting it outright.

**Filipino/Asian market specifics:**
- Politeness and warmth in a meeting (per meeting-intelligence's cultural signal notes) should not be read as deal momentum by itself — cross-check against concrete signals (a date confirmed, a document requested, a stakeholder introduced) before moving the deal stage.
- Contact role/influence updates should reflect real power (per meeting-intelligence's power map), not just org-chart title — this is often where CRM records are most out of date for Philippine conglomerate/family-owned accounts.

## Example Trigger Phrases
- "Update the CRM after that call with [account]"
- "Log this in HubSpot"
- "What needs updating in the deal record after that meeting?"
- "Clean up the [account] record — here's what happened"
