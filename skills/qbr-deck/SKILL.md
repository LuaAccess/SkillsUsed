---
name: qbr-deck
description: "Build a Quarterly Business Review (QBR) deck structure and narrative for a customer account. Use when asked to prepare a QBR, business review meeting, executive review, or quarterly check-in with a customer. Produces a slide-by-slide QBR structure with talking points, metrics review, value narrative, and mutual next steps."
---

# QBR Deck Skill

Produce a complete Quarterly Business Review deck — structured, data-backed, and customer-focused. A good QBR demonstrates value delivered, aligns on goals for the next quarter, and strengthens the executive relationship. It should never feel like a product demo or a vendor update.

## Required Inputs

Ask for these if not already provided:
- **Account name**, CSM name, and customer stakeholders attending
- **Contract details** — ARR, contract start date, renewal date
- **Last quarter's goals** (from previous QBR or kickoff)
- **Usage and adoption data** — key metrics for the quarter
- **Support summary** — tickets raised, resolution time, any escalations
- **Business outcomes the customer cares about**
- **Product updates or new features** relevant to this customer
- **Goals for next quarter**
- **Any open commercial conversations** (expansion, renewal, at-risk signals)

## QBR Principles

- Lead with customer outcomes, not product features
- Every metric should connect to a business result the customer cares about
- The agenda is a conversation, not a presentation — build in time for customer input
- Close with mutual commitments, not just vendor actions

## Output Format

---

# QBR: [Account Name] × [Your Company]
**[Quarter] [Year] Business Review**

**Date:** [Date] | **Location / Call link:** [TBC]
**Customer attendees:** [Names and roles]
**[Your company] attendees:** [Names and roles]

---

## Slide 1: Agenda (5 min)

| Time | Topic | Owner |
|---|---|---|
| 0:00 | Welcome and introductions | CSM |
| 0:05 | [Last quarter] — how did we do? | CSM + Customer |
| 0:20 | Value delivered — business impact | CSM |
| 0:35 | What's coming — roadmap preview | CSM / Product |
| 0:45 | [Next quarter] — goals and priorities | Customer |
| 0:55 | Actions and mutual commitments | CSM |
| 1:00 | Close | |

---

## Slide 2: Where We Are Together (2 min)

- **Customer since:** [Date]
- **Contract value:** ₱/$/£[ARR]/year
- **Renewal date:** [Date]
- **Active users:** [N] of [N] licensed seats ([X]% adoption)
- **Products / modules active:** [List]

---

## Slide 3: Last Quarter — Goals We Set Together (5 min)

| Goal | Set in [Last QBR / Kickoff] | Status |
|---|---|---|
| [Goal 1] | [What we committed to] | ✅ Achieved / ⚠️ Partial / ❌ Missed |
| [Goal 2] | [What we committed to] | ✅ Achieved / ⚠️ Partial / ❌ Missed |

For any partial or missed goal: state what happened and what changes next quarter.

---

## Slide 4: Usage and Adoption (5 min)

| Metric | [Q-1] | [Q] | Change |
|---|---|---|---|
| Monthly active users | [N] | [N] | +/-X% |
| Sessions per user per week | [N] | [N] | +/-X% |
| [Key feature 1] adoption | [X]% | [X]% | +/-X% |

---

## Slide 5: Business Impact — Value Delivered (10 min)

**[Outcome 1: customer's primary success metric]**
- Before: [baseline]
- Now: [current state]
- Impact: [quantified business result]

> "[Quote from champion or user about value experienced]"

---

## Slide 6: Support Summary (3 min)

| Metric | This quarter | Last quarter | Trend |
|---|---|---|---|
| Tickets raised | [N] | [N] | ↑ / → / ↓ |
| Average resolution time | [X hrs] | [X hrs] | ↑ / → / ↓ |
| CSAT score | [X/10] | [X/10] | ↑ / → / ↓ |

---

## Slide 7: What's Coming — Roadmap Preview (5 min)

| Feature / Improvement | Expected | Why it matters to [Account Name] |
|---|---|---|
| [Feature 1] | [Q+1] | [Direct link to their goal or pain point] |

---

## Slide 8: Next Quarter — Your Goals (10 min)

Prompt questions:
- "What does success look like for your team in [next quarter]?"
- "What's the biggest challenge you're trying to solve in the next 90 days?"

| Goal for next quarter | Owner (customer) | How we'll support it | How we'll measure it |
|---|---|---|---|

---

## Slide 9: Mutual Commitments (5 min)

**[Your company] commits to:**
1. [Specific action — owner — by when]

**[Account Name] commits to:**
1. [Specific action — owner — by when]

**Next touchpoint:** [Date]

---

## Preparation Checklist

- [ ] Usage data pulled and QoQ comparison calculated
- [ ] Last QBR goals reviewed — status confirmed before the meeting
- [ ] Business outcomes framed in customer language
- [ ] Roadmap filtered to this account's specific use cases
- [ ] Executive sponsor briefed on any sensitive topics before the call
- [ ] Actions from previous QBR reviewed

## Quality Checks

- [ ] Every slide has a talking point, not just a title
- [ ] Value slide leads with business outcomes, not product activity
- [ ] Roadmap preview links each item to a customer goal
- [ ] Mutual commitments section has real owners on both sides
- [ ] Customer has at least 20 minutes of airtime in the agenda

## Anti-Patterns

- [ ] Do not fill the QBR with product activity metrics — lead with business outcomes
- [ ] Do not present a roadmap without linking items to customer goals
- [ ] Do not run a QBR as a one-sided presentation
- [ ] Do not close a QBR without documented mutual commitments
- [ ] Do not skip the "what's not working" slide — suppressing problems erodes trust

## Gotchas

**Trigger conflicts:**
- This skill produces a presentation structure. For the internal account strategy document, use `account-plan`. For the renewal negotiation, use `renewal-playbook`.
- If the meeting is the first meeting with a prospect (not existing customer), use `discovery-call-prep` instead.

**Known failure modes:**
- Slide 5 (Business Impact) is the most frequently underpopulated section — Claude will produce a framework with placeholders if no outcome data is provided. You must supply real numbers. Push back with: "Use the usage data I provided and infer what the business impact was."
- Roadmap preview is sometimes too long — Claude may include all roadmap items. Prompt: "Include only the 2-3 roadmap items most relevant to this customer's stated goals."
- Mutual commitments section is sometimes left as vendor-only actions. Prompt: "Add at least 2 specific commitments from the customer side."

**Filipino/Asian market specifics:**
- Philippine executive attendees often arrive late or send a delegate. Build the deck so the first 5 minutes can be skipped without losing the narrative — put the key headline on Slide 2, not Slide 5.
- Avoid highlighting missed goals too directly in front of senior Philippine executives — it can cause the client to lose face. Frame as "here's what we're adjusting" rather than "here's what we missed."
- QBRs in Philippine accounts are often attended by more people than expected. Design the deck for a mixed audience (executive + technical + end users) — avoid deep technical detail in the main flow, offer it as an appendix.
- "Mabuti naman" (loosely: "it's fine") as a response to your value narrative may signal politeness, not genuine satisfaction. Follow up with: "What would make this even more useful for your team?"

## Example Trigger Phrases
- "Build a QBR deck for [Account Name] for Q[X]"
- "Prepare my quarterly business review with [company]"
- "Help me structure my EBR for [account]"
