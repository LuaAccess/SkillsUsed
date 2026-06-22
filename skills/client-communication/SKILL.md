
---
name: client-communication
description: Draft outbound messages to clients or prospects — emails, Teams messages, follow-up notes, meeting invites, or LinkedIn messages. Use when you need to write any message to a client, prospect, or stakeholder and want it calibrated for tone, relationship stage, and Filipino/Asian business culture. Trigger phrases include "draft an email to", "write a follow-up to", "message [client] about", "how do I say this to the client", "send a meeting invite for", "write a check-in to", "follow up on my proposal", or "I need to reach out to [person]". Do NOT use for internal status reports (operations:status-report), customer support ticket responses (customer-support:draft-response), or proposal documents (consulting-proposal).
argument-hint: "<recipient, purpose, key points to include>"
---

# /client-communication

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Draft professional, culturally-calibrated outbound messages to clients and prospects — written for real relationships, not templates.

## Usage

```
/client-communication $ARGUMENTS
```

Examples:
- `/client-communication Follow up on proposal sent to Metrobank IT head 5 days ago — no response yet`
- `/client-communication Email to reschedule discovery call — client cancelled last minute`
- `/client-communication Check-in to a client we haven't spoken to in 6 weeks`
- `/client-communication Introduce myself to a referred contact at a fintech startup`
- `/client-communication Deliver bad news — project will be delayed by 2 weeks`

---

## Workflow

### 1. Situation Intake

Parse or ask for:

- **Recipient:** Name, title, company, your relationship with them
- **Purpose:** What outcome do you need from this message
- **Relationship stage:** Cold / warm / existing client / lapsed / escalated
- **Channel:** Email / Teams / SMS / LinkedIn / WhatsApp
- **Tone needed:** Formal / professional / warm / urgent / diplomatic
- **Cultural context:** Filipino enterprise / MNC local / government / executive level
- **Constraints:** Anything sensitive, timing-dependent, or politically complex about this message

---

### 2. Cultural Calibration

Apply automatically based on relationship and cultural context:

| Context | Calibration Applied |
|---------|-------------------|
| Filipino enterprise client | Warmer opener, acknowledge relationship before business, avoid bluntness |
| Senior executive (C-level / VP) | Lead with business outcome, short and direct, no over-explanation |
| Government or public sector | Formal salutation, reference any official context, patience signal in closing |
| MNC local subsidiary | Match their corporate communication style — usually more direct than local PH norms |
| First contact / cold outreach | Credibility anchor early, specific not generic, clear and low-pressure ask |
| Follow-up after silence | No guilt language, no "just checking in" — lead with value or new information |
| Delivering bad news | Acknowledge impact first, take ownership, action plan before apology |
| Winning back a lapsed contact | Acknowledge the gap, skip over-explanation, lead with relevance to them now |

---

### 3. Draft Output

```markdown
## Message Draft

**To:** [Name, Title, Company]
**Channel:** [Email / Teams / LinkedIn / SMS]
**Subject (if email):** [Subject line]
**Tone:** [Warm / Professional / Formal / Urgent / Diplomatic]
**Relationship stage:** [Cold / Warm / Existing / Escalated]

---

[Draft message]

---

### Notes (internal — do not send)
- **Why this approach:** [Rationale for structure and tone]
- **What to verify before sending:** [Any facts, names, or context to confirm]
- **Sensitivity flags:** [Anything to handle carefully]
- **Expected response:** [What outcome this message is designed to produce]
- **If no response in X days:** [Suggested follow-up approach]
```

---

### 4. Message Variants

After the primary draft, offer variants when relevant:

- **Shorter version** — for mobile-first recipients or when brevity signals confidence
- **More formal version** — for government, senior executives, or first-contact scenarios
- **Taglish version** — for established relationships where Filipino language builds warmth
- **Translated version** — if recipient communicates primarily in Filipino

---

### 5. Subject Line Options (for emails)

Generate 3 subject line options with different framing:

```
Option A (direct): [States the purpose clearly]
Option B (value-first): [Opens with what's in it for them]
Option C (relationship): [References your shared context or history]
```

---

## Message Types Reference

### Follow-up After No Response
- Never open with "Just following up" or "I wanted to check in" — these signal low confidence
- Lead with a new piece of value, a relevant update, or a specific question
- Make it easy to respond with one sentence
- In PH business culture: allow more time before following up (3–5 business days vs 2)

### Proposal Follow-up
- Reference the proposal briefly — don't re-summarise it
- Offer a specific, low-pressure next step (15-min call, one question answered)
- Acknowledge they are busy — give permission to be honest if the timing has changed

### Meeting Request
- State clearly what the meeting is for and what you need from them
- Offer specific times — don't make them do the scheduling work
- Keep it to 30 minutes unless complexity justifies more
- In PH business culture: in-person or video beats async for relationship-stage decisions

### Delivering Bad News
- State the news in the first paragraph — do not bury it
- Own the situation — no passive voice, no blame transfer
- Action plan in the same message — never just deliver bad news without a path forward
- Offer a conversation — bad news delivered in writing alone feels like avoidance

### Cold Outreach / Introduction
- One credibility anchor — referral name, shared connection, or specific relevant context
- State why you're reaching out in terms of their world, not yours
- Single clear ask — a call, a question, a referral — not multiple options
- No attachments on first contact

### Re-engaging Lapsed Contacts
- Acknowledge the gap without over-explaining it
- Lead with something genuinely relevant to them now — not "I wanted to reconnect"
- Make the ask small and easy

---

## If Connectors Available

**Microsoft 365 / Outlook:**
- Pull prior email thread with this contact for context and tone matching
- Draft directly into compose window
- Schedule send for optimal time

**HubSpot:**
- Pull contact record and interaction history
- Log sent message as CRM activity
- Set follow-up task if needed

**Microsoft 365 / Teams:**
- Draft as a Teams message for internal or client channels

**Microsoft 365 / Calendar:**
- Generate meeting invite with agenda for meeting request messages

---

## Communication Quality Checks

Before finalising any draft:

- [ ] Does the opening line give them a reason to keep reading?
- [ ] Is the purpose of the message clear within the first 2 sentences?
- [ ] Is there exactly one clear ask or next step?
- [ ] Is the tone appropriate for this person and this relationship stage?
- [ ] Have you removed any filler phrases ("hope this finds you well", "just wanted to reach out")?
- [ ] Is the length appropriate for the channel and the stakes?
- [ ] Does it sound like you — or like a template?
- [ ] For PH context: is the warmth level calibrated correctly for this relationship?

---

## Tips

1. **The subject line is the message.** If the subject line doesn't earn the open, the draft doesn't matter.
2. **One ask per message.** Multiple asks create decision paralysis. Pick the most important one.
3. **Short is a power move.** A 4-sentence email from someone confident in their value beats a 12-sentence email that justifies itself.
4. **In Filipino business culture:** a message that references shared context (last meeting, a mutual contact, something they mentioned) outperforms any perfectly-crafted cold template. Personalisation signals respect.
5. **Taglish is not unprofessional.** For established relationships, a message in Taglish or Filipino can strengthen rapport more than a formal English email. Match their communication style, not a corporate standard.
