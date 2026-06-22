
---
name: consulting-proposal
description: Draft, structure, or review an IT consulting proposal or statement of work. Use when writing a new proposal for a client engagement, responding to an RFP or RFQ, packaging a solution recommendation into a formal document, building a pricing narrative, or restructuring a proposal that lost traction. Trigger phrases include "write a proposal", "draft an SOW", "we need to respond to this RFP", "package this solution", "help me price this engagement", "proposal for [client]", or "why did my proposal lose". Do NOT use for internal project status reports (operations:status-report), contract review (legal:review-contract), or competitive analysis (it-consulting-battlecard).
argument-hint: "<client name, engagement type, key requirements>"
---

# /consulting-proposal

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Draft a winning IT consulting proposal — structured to match how clients actually decide, not how vendors like to present.

## Usage

```
/consulting-proposal $ARGUMENTS
```

Examples:
- `/consulting-proposal BDO — network infrastructure assessment, 3-month engagement`
- `/consulting-proposal RFP response — government agency, cloud migration, deadline Friday`
- `/consulting-proposal Review this proposal draft and tell me why it will lose`
- `/consulting-proposal Package our managed services offer for a mid-size fintech`

---

## Workflow

### 1. Engagement Intake

Gather or infer:

- **Client:** Name, industry, size, decision-maker profile
- **Engagement type:** Assessment / Implementation / Managed Services / Advisory / Staff Augmentation
- **Known pain:** What problem triggered this proposal request
- **Budget signals:** Any indication of budget range, procurement process, or approval level
- **Competition:** Known or likely competitors in this bid
- **Relationship stage:** Cold RFP / warm referral / existing client / renewal
- **Cultural context:** Filipino enterprise, MNC local subsidiary, government agency, or other — adjust formality, hierarchy acknowledgment, and relationship framing accordingly

---

### 2. Proposal Structure

Produce a complete proposal draft using this structure:

```markdown
# [Engagement Title]
## Prepared for: [Client Name]
## Prepared by: [Your Name / Company]
## Date: [Date] | Version: [1.0]

---

### Executive Summary
[3–5 sentences. Written for the decision-maker, not the technical evaluator.
Lead with the client's problem, not your capabilities. End with the specific outcome you are committing to deliver.]

---

### Understanding of the Situation
[Demonstrate that you understand their real problem — not just the stated requirement.
Reference anything they told you. Name the business impact, not just the technical gap.
In Filipino business culture: acknowledge their current effort and frame your proposal as a complement, not a criticism of what they've done.]

---

### Proposed Approach

#### Phase 1 — [Name] | [Duration]
- Objective:
- Activities:
- Deliverables:
- Your involvement required:

#### Phase 2 — [Name] | [Duration]
[repeat]

---

### Deliverables

| Deliverable | Format | Delivery Date | Acceptance Criteria |
|-------------|--------|---------------|---------------------|
| [Item] | [Doc / Report / System / Workshop] | [Date] | [How you'll know it's done] |

---

### Team and Credentials
[Name key people. For Philippine clients: include relevant local experience and any client references in the same industry or size tier. Hierarchy matters — show who the senior person accountable is.]

---

### Investment Summary

| Item | Quantity | Rate | Subtotal |
|------|----------|------|----------|
| [Role / Deliverable] | [Days / Units] | [Rate] | [Amount] |
| **Total** | | | **[Total]** |

**Payment terms:** [Milestone-based / Monthly / Upfront split]
**Validity:** This proposal is valid until [date]

---

### Why [Your Company]
[3 bullet points maximum. Grounded in specifics — not generic "we are committed to excellence" language.
Each point should address a real concern the client likely has but hasn't said aloud.]

---

### Next Steps

| Step | Owner | Date |
|------|-------|------|
| Proposal walkthrough call | [You] | [Proposed date] |
| Client Q&A and clarifications | [Client] | [Date] |
| Commercial sign-off | [Client] | [Date] |
| Engagement kickoff | [Both] | [Date] |
```

---

### 3. Pricing Narrative

After the proposal, generate a separate pricing narrative — the internal logic you use to justify your numbers in a client conversation:

```
## Pricing Narrative

**Your anchor number:** [Total]
**Justification framing:** [Value delivered, not hours spent]
**Expected pushback point:** [Where client will negotiate]
**Your floor:** [Minimum acceptable — do not share with client]
**Concession strategy:** [What you can give vs. what you must protect]
**Philippine market calibration:** [Is this priced for local market, MNC budget, or government procurement norms?]
```

---

### 4. Proposal Risk Flags

Before finalising, check:

- [ ] Does the executive summary lead with their problem — not your company name?
- [ ] Is every deliverable described in outcome language, not activity language?
- [ ] Is the pricing framed as investment-to-outcome, not cost-of-effort?
- [ ] Have you named the specific senior person accountable — Filipino clients want to know who to call?
- [ ] Is the timeline realistic — or optimistic to win, with risk of failure during delivery?
- [ ] Does the "Why us" section address unstated concerns (stability, local presence, post-delivery support)?
- [ ] Is there a clear, low-friction next step that makes it easy for them to say yes?

---

## If Connectors Available

**Microsoft 365 / Word:**
- Output the final proposal as a formatted .docx file

**HubSpot:**
- Log proposal as a deal activity
- Update deal stage to "Proposal Sent"
- Set follow-up reminder

**Box:**
- Save the proposal to the client's folder
- Generate a shareable link

**Outlook:**
- Draft the cover email to send with the proposal

---

## Proposal Quality Principles

1. **The proposal is a sales document, not a technical spec.** Write for the person who signs, not the person who evaluates.
2. **Lead with their pain, not your capability.** Every opening line should prove you understand their situation.
3. **Deliverables over activities.** "Infrastructure audit report with prioritised remediation plan" beats "conduct interviews and analyse current state."
4. **Pricing tells a story.** The number is the last thing — the value justification comes first.
5. **In Philippine business culture:** A proposal sent cold rarely wins. The proposal confirms a conversation already had. If you haven't had the relationship conversation, write the proposal but prioritise getting the walkthrough meeting first.
6. **Short beats long for first proposals.** A 4-page proposal that answers the real question beats a 20-page deck that proves how hard you worked.
