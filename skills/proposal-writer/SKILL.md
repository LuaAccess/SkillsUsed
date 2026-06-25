---
name: proposal-writer
description: "Write a structured sales proposal or commercial proposal for any deal. Use when asked to write a proposal, sales proposal, commercial proposal, statement of work, or quote document. Produces a complete proposal with problem statement, solution, investment, and next steps. Do NOT use for battlecards, GTM plans, or renewal negotiations — use sales-battlecard, go-to-market, or renewal-playbook instead."
---

# Proposal Writer Skill

Writes commercial proposals that win business — structured around the prospect problem, not the product.

## Required Inputs
- **Prospect company and contact**
- **Their problem or goal** (from discovery — be specific)
- **Your proposed solution**
- **Commercial terms** (pricing, payment terms, contract length)
- **Timeline**
- **Key stakeholders** who will read this
- **Tone** (formal / conversational / technical)

## Output Structure

---

# Proposal: [Brief description of what you are solving]
**Prepared for:** [Contact, Title] | [Company]
**Prepared by:** [Name] | [Your Company]
**Date:** [Date] | **Valid until:** [Date]

---

### Understanding Your Situation
[2-3 paragraphs. Demonstrate you listened. Describe their situation, problem, and impact of not solving it in their words. This section should make them think "yes, exactly." Generic boilerplate here = proposal goes in the bin.]

**The key challenge:** [One sentence — the core problem]
**The impact:** [What this costs them]
**What you have tried:** [Acknowledge prior attempts]

---

### Our Proposed Approach

**What we will do** (3-5 deliverables or phases)

**Phase 1: [Name]** (Timeline: [Weeks 1-2])
[What happens, what is delivered, what customer input is needed]

**Phase 2: [Name]** (Timeline: [Weeks 3-6])

**What you will get** (outcomes, not features)
- [Outcome 1]
- [Outcome 2]

**What success looks like**
[How both parties know this worked]

---

### Why [Your Company]
[3-4 sentences. Specific to their situation. Reference similar customers. Generic "why us" sections are skipped.]

---

### Investment

| Item | Description | Investment |
|---|---|---|
| [Component 1] | [Description] | ₱/$/£[amount] |
| **Total** | | **₱/$/£[total]** |

**Payment terms:** [Terms]
**Included:** [What is in]
**Not included:** [What is out — prevents scope disputes]

---

### Timeline
| Milestone | Date |
|---|---|
| Contract signed | [Date] |
| Kickoff | [Date] |
| Delivery | [Date] |

---

### Next Steps
1. [Sign / reply / schedule] by [date]
2. We will send contract and confirm kickoff
3. [Any immediate action]

## Quality Checks

- [ ] "Understanding Your Situation" reflects what was learned in discovery (not generic)
- [ ] Outcomes are listed (not just deliverables or features)
- [ ] "Not included" section is explicit to prevent scope disputes later
- [ ] Next steps include a specific date and named action
- [ ] "Valid until" date is included to create urgency

## Anti-Patterns

- [ ] Do not lead with the solution before establishing problem understanding
- [ ] Do not use vague investment language — state a specific price or range
- [ ] Do not omit a "not included" section — undefined scope leads to disputes
- [ ] Do not forget a "valid until" date — proposals without expiry go stale
- [ ] Do not list next steps without naming who is responsible and the timeline

## Gotchas

**Trigger conflicts:**
- This skill produces a full commercial proposal document. If the request is for a competitive comparison or objection handling sheet, use `sales-battlecard` instead.
- If the ask is for a renewal negotiation document, use `renewal-playbook` — not this skill.

**Known failure modes:**
- Claude tends to write generic "Understanding Your Situation" sections when discovery context is thin. Always provide specific pain points from the discovery call, even as rough notes.
- Pricing tables may be formatted incorrectly for copy-paste into Word or email. Review table markdown before sending.
- "Valid until" date is sometimes omitted from output. Check before finalising — add it manually if missing.

**Filipino/Asian market specifics:**
- Philippine clients often share proposals internally before responding. Build the document to be self-explanatory to a reader who was not in the discovery call.
- Avoid aggressive "valid until" dates shorter than 14 days for Philippine enterprise accounts — it can feel pressuring and damage the relationship.
- Decision-making is often collective. Add a stakeholder summary section if multiple approvers are known.
- Peso pricing (₱) should be stated explicitly — do not assume USD unless confirmed.

## Example Trigger Phrases
- "Write a proposal for [prospect] to [solve their problem]"
- "Draft a statement of work for [project]"
- "Turn my discovery notes into a proposal"
