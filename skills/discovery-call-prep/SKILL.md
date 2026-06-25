---
name: discovery-call-prep
description: "Prepare a structured discovery call plan for any prospect. Use when asked to prepare for a sales call, discovery call, prospect meeting, or first call with a potential customer. Produces a call brief with research, hypotheses, questions, and success criteria. Do NOT use for renewal conversations, QBRs, or post-sale meetings — use renewal-playbook or qbr-deck instead."
---

# Discovery Call Prep Skill

Produces a complete discovery call brief — research summary, call hypothesis, structured questions, and success criteria — so every call starts with context and ends with a clear next step.

## Required Inputs
- **Prospect company name**
- **Contact name and role**
- **Any known context** (how they found you, prior interaction)
- **Your product/solution** (one line)
- **Call duration** (15 / 30 / 45 / 60 min)

## Output Structure

---

# Discovery Call Brief
**Prospect:** [Company] | **Contact:** [Name, Title] | **Duration:** [X min]

---

### Research Summary
- What they do: [Product/service, customer, business model]
- Size: [Headcount, revenue if public]
- Stage: [Startup / Scaleup / Enterprise]
- Recent news: [Funding, launches, leadership changes — last 90 days]
- Contact background: [Role tenure, previous companies, LinkedIn activity]
- Likely priorities for someone in this role: [Based on title and stage]

---

### Call Hypothesis
Before the call write your best guess:
- **Their most likely pain:** [What someone in this role at this company probably has]
- **Why they would care about us:** [Specific connection to your value]
- **Biggest risk to the deal:** [What might make this not a fit]

Write it down — then test it on the call.

---

### Call Agenda
"Here is what I was thinking for our [X] minutes:
- 2 min: Quick intros
- [X] min: Learn more about your situation
- [X] min: Share how we have helped similar companies
- 5 min: Next steps
Does that work? Anything specific you would like to cover?"

---

### Discovery Questions

Open with context (not a pitch):
- "What prompted you to take this call today?"
- "What does [relevant area] look like for you at the moment?"

Go deeper on pain:
- "How long has [problem] been an issue?"
- "What have you tried to solve it?"
- "What is the impact of not solving this?"

Understand buying context:
- "Who else would be involved in a decision like this?"
- "Have you looked at other solutions?"
- "Is there a reason you are exploring this now?"

Qualify on budget:
- "Have you set aside budget for this kind of initiative?"

Close discovery:
- "Based on what you have told me, it sounds like [summary]. Is that right?"

---

### Success Criteria
This call is successful if we leave with:
- Understanding of specific pain and business impact
- Knowledge of buying process and key stakeholders
- A clear agreed next step (demo / proposal / intro)
- Sense of timeline

This call is NOT successful if we only pitched and got "sounds interesting, send me some info."

---

### Suggested Next Step
"Based on what we discussed, the logical next step would be [specific]. Does [day/time] work?"

## Quality Checks

- [ ] Research summary includes recent news (last 90 days) — not just LinkedIn bio
- [ ] Call hypothesis is written before the call (not post-rationalised after)
- [ ] Discovery questions progress from context → pain → business impact → buying process
- [ ] Success criteria define what "not successful" looks like (not just the ideal outcome)
- [ ] A specific next step is proposed (not "let's stay in touch")

## Anti-Patterns

- [ ] Do not write the call hypothesis after the call
- [ ] Do not open with a product pitch before establishing the prospect's problem
- [ ] Do not use closed questions in the discovery phase
- [ ] Do not skip the "not successful" definition in success criteria
- [ ] Do not treat all prospect research equally — recent news beats static facts

## Gotchas

**Trigger conflicts:**
- This skill and `discovery-interview-guide` both involve structured questioning. Use THIS skill for sales/prospect calls with new prospects. Use `discovery-interview-guide` for user research and problem validation interviews with existing users.
- If the contact is an existing customer, stop — use `renewal-playbook` or `qbr-deck` instead.

**Known failure modes:**
- Claude may generate generic questions not tailored to the specific industry or role. If output feels generic, add the prospect's industry, company stage, and your specific solution to your input.
- Research summary may hallucinate recent news. Always verify funding/news claims before the call.
- Hypothesis section is sometimes skipped when input is sparse. If it's missing, prompt: "Write the call hypothesis even with limited information — label assumptions."

**Filipino/Asian market specifics:**
- "We'll think about it" often signals internal hierarchy approval is needed, not genuine interest. Do not treat it as a soft yes.
- First calls in Philippine enterprise accounts are often relationship-building, not qualification. Do not push hard BANT qualification in call 1 — it reads as transactional and damages rapport.
- Indirect responses to budget questions are normal. Rephrase as: "What does the approval process look like for something like this?"
- Silence after a proposal is not rejection — follow up gently after 3-5 business days.

## Example Trigger Phrases
- "Prepare me for a discovery call with [company/contact]"
- "Build a call brief for my meeting with [name] at [company]"
- "What questions should I ask in a discovery call for [use case]?"
