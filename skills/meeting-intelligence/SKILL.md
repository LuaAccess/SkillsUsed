[Uploading meeting-intelligence_SKILL.md…]()
---
name: meeting-intelligence
description: Post-meeting debrief and analysis for IT consulting and sales meetings. Use when pasting meeting notes, transcript, or pipeline output after a client call, discovery session, stakeholder meeting, or sales meeting — especially when you want to extract hidden signals, decode client behaviour, map power dynamics, identify next moves, or audit your own performance. Trigger phrases include "MODE 1", "meeting debrief", "what just happened in that meeting", "analyse my meeting notes", "what did I miss", "decode this client", or any paste of raw meeting output for analysis. Do NOT use for scheduling meetings, drafting agendas, or preparing for a future meeting — those go to client-communication or legal:meeting-briefing.
argument-hint: "<paste meeting notes, transcript, or pipeline output>"
---

# /meeting-intelligence

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Analyse a completed client meeting. Extract hidden signals, map power dynamics, surface blind spots, and produce clear next actions — with Filipino/Asian business culture intelligence applied automatically.

## Usage

```
/meeting-intelligence $ARGUMENTS
```

Examples:
- `/meeting-intelligence [paste raw notes from discovery call with BDO IT team]`
- `/meeting-intelligence MODE 1 — here is my meeting output: [paste Stage 5–7]`
- `/meeting-intelligence [paste Teams transcript — CFO alignment meeting]`

---

## Workflow

### 1. Parse the Input

Extract from the raw notes or transcript:

- **Attendees** — titles, who spoke most, who went quiet, who deferred to whom
- **Stated objectives** — what the meeting was officially about
- **Actual agenda** — what was really being decided or evaluated
- **Decisions made** — explicit and implicit
- **Commitments given** — by client, by you, by anyone else
- **Unresolved items** — what was left open intentionally or not

---

### 2. Signal Extraction

Surface non-obvious signals from the meeting:

**Verbal signals:**
- Hedge language: "we'll see", "we'll circle back", "interesting" → decode probable meaning
- Repetition: topics the client returned to unprompted → what they actually care about
- Deflection patterns: questions answered with questions, topic changes, vague timelines

**Non-verbal / structural signals:**
- Who spoke first and last
- Who was invited but barely spoke → observer or evaluator role
- Energy shifts: where did momentum increase or drop
- Off-topic moments: relationship-building or avoidance?

**Cultural signals (Filipino / Asian business context — always apply):**
- "We'll think about it" / "We'll coordinate internally" → likely soft no or unresolved internal conflict — flag explicitly
- Excessive agreement with no specifics → surface-level buy-in, not commitment
- Code-switching moments (English → Filipino mid-sentence) → mark as emotionally significant
- Who was deferred to in the room vs. who holds the title → real power vs. org chart power
- Indirect criticism of past vendors or current situation → direct statement about what they need
- Laughter and off-topic tangents → relationship-building signal, NOT time-wasting

---

### 3. Power Map

```
## Power Map

| Person | Title | Real Role | Influence Level | Signal Observed |
|--------|-------|-----------|-----------------|-----------------|
| [Name] | [Title] | [Decision-maker / Evaluator / Blocker / Champion] | [High/Med/Low] | [What tipped you off] |
```

- Identify who controls budget, who controls access, who controls timing
- Flag anyone present whose role you cannot explain — they matter
- Map visible vs. hidden objections: who pushed back openly vs. who went quiet

---

### 4. Performance Audit

Rate the meeting participant (you) on:

| Dimension | Observed Behaviour | Score (1–5) | Gap to Target |
|-----------|-------------------|-------------|---------------|
| Active listening | [What you did] | [Score] | [What a 5 looks like] |
| Emotional regulation | [What you did] | [Score] | [What a 5 looks like] |
| Question quality | [What you asked] | [Score] | [What a 5 looks like] |
| Cultural reading | [What you picked up vs. missed] | [Score] | [What a 5 looks like] |
| Positioning | [How you framed your value] | [Score] | [What a 5 looks like] |
| Commitment clarity | [What you committed to] | [Score] | [What a 5 looks like] |

Flag: linear thinking patterns, effort-based responses, missed leverage moments.

---

### 5. Strategic Options

Generate 2–4 next-move options ranked by leverage:

```
## Option [N]: [Name]

**Mechanism:** What you do and how it works
**Leverage point:** Why this move is disproportionately effective
**Failure mode:** What breaks this option
**Cultural fit:** Does this work in a Filipino/Asian business context — and how must it be adapted
**Timing:** When to execute
```

---

### 6. Immediate Actions

```
## Next Actions

| Action | Owner | Channel | Deadline | Why It Matters |
|--------|-------|---------|----------|----------------|
| [Action] | [You / Client / Both] | [Email / Teams / Call] | [Date] | [Stakes] |
```

---

## If Connectors Available

**Microsoft 365 / Outlook:**
- Pull the meeting invite for attendee list and stated agenda
- Cross-reference any prior emails with this client for context drift

**HubSpot:**
- Update deal stage and contact notes from this meeting
- Log key signals as CRM activity
- Flag if follow-up sequence needs to be triggered

**Notion:**
- Save debrief output as a meeting intelligence note
- Link to client or deal page

**Asana / monday.com:**
- Create follow-up tasks from the Next Actions table
- Assign owners and deadlines

---

## Cultural Intelligence Reference

Apply these automatically — do not wait to be asked:

| Signal | Common Surface Reading | Probable Real Meaning |
|--------|----------------------|----------------------|
| "We'll circle back" | Delay | Soft no, or unresolved internal politics |
| "Very interesting" (no follow-up) | Engagement | Polite deflection |
| Extended small talk | Inefficiency | Trust-building — critical in PH business culture |
| Silent senior attendee | Observer | Evaluator — their reaction matters most |
| Indirect reference to past vendor problems | Background context | Direct statement of current pain — this is the real requirement |
| Code-switch to Filipino | Normal conversation | Emotional register shift — take note of what triggered it |
| Agreement with no specifics | Buy-in | Surface compliance — probe for actual commitment |

---

## Tips

1. **The meeting you saw is not the meeting that happened.** The real meeting is in the signals — who deferred, who deflected, who went quiet.
2. **Silence is data.** A senior person who says nothing for 45 minutes chose not to speak. Understand why before your next move.
3. **Relationship before transaction** — in Filipino business culture, the off-topic 10 minutes of small talk is not wasted time. It is the meeting. Factor this into your read of rapport and readiness.
4. **Your EQ blind spots are highest under pressure.** If the meeting felt difficult, assume you missed 2–3 signals you would have caught if relaxed.
