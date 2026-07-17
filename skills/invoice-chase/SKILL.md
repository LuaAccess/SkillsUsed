---
name: invoice-chase
description: Draft and sequence overdue-invoice collection messages with escalating tone, timing cadence, and relationship-preserving language. Use when a client invoice is past due, when planning a dunning/collections sequence, when deciding how firm a follow-up should be given days overdue and client relationship value, or when a client has gone silent on payment. Triggers include "chase this invoice", "follow up on payment", "client hasn't paid", "overdue invoice", "collections email", "payment reminder", "dunning sequence". Does NOT cover invoice creation, generating the invoice document itself, revenue recognition, or journal entries — see finance:financial-statements or finance:journal-entry-prep for those. Does NOT cover legal demand letters or formal collections/legal action — see legal:legal-risk-assessment or a licensed collections attorney once a matter escalates past Stage 4.
---

# Invoice Chase

## Purpose
Produce the right message, at the right firmness, at the right time — without either (a) writing the same generic "just checking in" email every stage, or (b) torching a relationship-first client relationship (see: Filipino/Asian business culture — relationship precedes transaction, and public firmness reads as face-loss, not urgency).

## Gotchas
- **Firmness is not linear with lateness.** A 90-day-late client you've worked with for 5 years gets a different Stage 3 message than a 90-day-late new client. Relationship tenure and deal size change the curve — always ask if unknown, don't assume.
- **Never escalate tone and escalate channel at the same time.** Moving from email → call → CC'ing their manager is itself an escalation. Doing it in the same step as harsher language compounds the face-loss and can backfire in hierarchy-sensitive accounts (e.g., BSP-adjacent, government-linked).
- **Silence ≠ refusal.** In Filipino business communication, no response often means an internal blocker (budget approval stuck, wrong stakeholder, embarrassment about the delay) — not a refusal to pay. Stage 2+ messages should offer a face-saving out ("let us know if there's anything blocking approval on your end") rather than assuming bad faith.
- **CC escalation is a power move — treat it as one.** CC'ing a superior should be flagged as a deliberate hierarchy-signal decision, not a default step, and should be confirmed with the user before drafting.
- **Don't mix currencies/payment terms assumptions.** Confirm currency, payment terms (net 30/60), and any PO number references before drafting — wrong references undermine credibility.

## Escalation Stages

| Stage | Timing | Tone | Channel default |
|---|---|---|---|
| 1 — Friendly reminder | 1–7 days overdue | Warm, assumes oversight | Email |
| 2 — Direct follow-up | 8–30 days overdue | Clear, still warm, asks for status | Email |
| 3 — Firm inquiry | 31–60 days overdue | Direct, names the impact, requests a specific date | Email + optional call |
| 4 — Final notice | 61–90 days overdue | Formal, states consequence (hold on services/deliverables), still professional | Email, CC decision-maker if approved by user |
| 5 — Pre-escalation | 90+ days overdue | Neutral, factual, signals next step is account review/legal | Formal email only — hand off to legal review beyond this stage |

## Workflow
1. Ask (if not given): days overdue, amount, currency, client relationship tenure/value, prior stage already used, any known blocker.
2. Map days overdue → stage using table above, but let relationship value shift it ±1 stage.
3. Draft using `message_compose_v1` tool with 2 variants when stage ≥ 3: a "hold firm" and a "preserve relationship" version, since these genuinely trade off outcomes at that firmness level.
4. Flag any planned channel escalation (CC, phone call) as a separate confirmed decision, never bundled silently into the draft.
5. If client has gone silent for 2+ follow-ups, suggest a lower-effort/lower-face-loss channel switch (e.g., a phone call instead of a third email) before jumping straight to Stage 4 language.

## Output
- Draft message(s) via `message_compose_v1`
- One-line stage rationale ("Stage 3 — 45 days overdue, but 3-year relationship pulled tone down from 'final notice' to 'firm inquiry'")
- Flag if the situation has crossed into territory requiring `legal:legal-risk-assessment` (typically 90+ days with no response, or explicit non-payment refusal)
