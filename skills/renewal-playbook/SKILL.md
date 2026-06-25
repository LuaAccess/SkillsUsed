---
name: renewal-playbook
description: "Build a structured renewal playbook for a customer account. Use when asked to plan a renewal, structure a renewal negotiation, prepare for an expansion conversation, or build a renewal strategy for at-risk or healthy accounts. Produces a renewal brief with health assessment, negotiation strategy, objection responses, expansion levers, and a timeline. Best used after cs-health-scorecard has been run. Do NOT use for new prospect proposals — use proposal-writer instead."
---

# Renewal Playbook Skill

Produces a complete renewal playbook for a specific customer account — health assessment, commercial strategy, negotiation preparation, expansion opportunity mapping, and a step-by-step timeline. Output is ready for the CSM or account team to execute 90–180 days before renewal.

## Required Inputs

Ask the user for these if not provided:
- **Account name**
- **Renewal date**
- **Current ARR** and proposed renewal ARR (if different)
- **Account health** — RAG status and main reasons (or describe the account situation)
- **Key stakeholders** — economic buyer, champion, and any detractors
- **Renewal risk factors** — budget pressure, low adoption, competitive threat, champion departure, etc.
- **Expansion opportunity** — any upsell or cross-sell potential?
- **Contract terms** — current plan, duration, and any terms up for renegotiation

## Output Structure

---

# Renewal Playbook: [Account Name]

**Renewal date:** [Date]
**Current ARR:** ₱/$/£[X]
**Target renewal ARR:** ₱/$/£[X — flat / +X% expansion / contraction risk]
**Health status:** [Green / Amber / Red]
**CSM:** [Name]
**Account executive:** [Name]
**Days to renewal:** [X days]

---

## 1. Account Health Snapshot

| Dimension | Score (1–5) | Evidence |
|---|---|---|
| **Product adoption** | [X/5] | [e.g. 3 of 5 purchased seats active; core feature used weekly] |
| **Business outcomes** | [X/5] | [e.g. Customer reports X% improvement in [metric]] |
| **Relationship depth** | [X/5] | [e.g. Strong champion in [name/role]; limited exec sponsorship] |
| **Support & satisfaction** | [X/5] | [e.g. 2 open P2 tickets; last NPS 7; no escalations in 6 months] |
| **Commercial engagement** | [X/5] | [e.g. Invoice paid on time; no discount pressure raised yet] |
| **Overall health** | [X/5 — weighted] | [Green / Amber / Red] |

**Renewal thesis:** [One sentence: why this account will renew — or what must change for it to renew.]

---

## 2. Stakeholder Map

| Stakeholder | Role | Influence | Sentiment | Our relationship |
|---|---|---|---|---|
| [Name] | Economic buyer | High | [Positive / Neutral / Negative] | [Warm / Cold / Unknown] |
| [Name] | Champion | High | [Positive] | [Warm] |
| [Name] | End user | Low | [Neutral] | [Limited] |
| [Name] | IT / procurement | Medium | [Neutral] | [Transactional] |

**Champion risk:** [Is our champion secure in their role? Any signals of departure or reorganisation?]

**Multi-thread plan:** [Who else do we need relationships with before renewal? How do we get there?]

---

## 3. Risk Register

| Risk | Likelihood (H/M/L) | Impact (H/M/L) | Mitigation |
|---|---|---|---|
| [Budget pressure / cost-cutting] | [H] | [H] | [Build ROI case 90 days out; identify budget holder's priorities] |
| [Low adoption in [department]] | [M] | [H] | [Run targeted enablement session; tie to champion's OKRs] |
| [Competitor evaluation] | [M] | [M] | [Request competitive intelligence; schedule exec-level call] |
| [Champion departure] | [L] | [H] | [Map two additional stakeholders; executive intro call] |

---

## 4. Value Story

**Headline result:** [e.g. "[Account] saved X hours/week or reduced [metric] by X% using [product]"]

**Evidence sources:**
- [ ] Product usage data (logins, features used, seat utilisation)
- [ ] Business metric improvement (pull from QBR deck or success plan)
- [ ] Support resolution time improvement
- [ ] Customer-provided testimonial or case study quotes

**Value gaps to close before renewal:** [Outcomes the customer expected but hasn't seen yet — and the plan to close them]

---

## 5. Expansion Opportunity

| Opportunity | Type | Estimated value | Likelihood | Timing |
|---|---|---|---|---|
| [Seat expansion — [dept]] | Upsell | [+₱/$/£X ARR] | [High] | [Renewal or +3M] |
| [Cross-sell — [Product B]] | Cross-sell | [+₱/$/£X ARR] | [Medium] | [+6M] |
| [Multi-year commitment] | Discount for term | [+₱/$/£X TCV] | [Low] | [At renewal] |

---

## 6. Commercial Strategy

**Renewal scenario planning:**

| Scenario | Probability | ARR outcome | Response strategy |
|---|---|---|---|
| **Flat renewal** | [X%] | [₱/$/£X] | [Accept; plant seeds for +6M expansion] |
| **Expansion** | [X%] | [₱/$/£X] | [Lead with ROI evidence; pitch seat or feature expansion] |
| **Contraction risk** | [X%] | [₱/$/£X] | [Propose phased commitment; demonstrate path to full adoption] |
| **Churn risk** | [X%] | [₱/$/£0] | [Escalate to leadership; executive sponsor engagement] |

**Discount guardrails:**
- Floor discount: [X% — do not go below without VP approval]
- Triggers for discount: [Multi-year / volume / reference customer commitment]
- What to ask for in return: [Reference case study / G2 review / executive intro]

---

## 7. Objection Responses

**"The price is too high"**
> Anchor on value delivered. If budget is genuinely constrained, explore: phased payment, reduction in scope, multi-year pricing.

**"We're not seeing enough adoption"**
> Acknowledge, then commit with a 60-day adoption plan with named owner.

**"We're evaluating [Competitor]"**
> Ask: "What's driving the evaluation?" Map gaps honestly. Get clarity on criteria and timeline before responding defensively.

**"We need to reduce spend this quarter"**
> Separate the commercial conversation from the value conversation. Offer reduced scope today with expansion trigger at a business milestone.

---

## 8. Renewal Timeline

| Week | Action | Owner | Notes |
|---|---|---|---|
| **W–16** | Internal renewal review — health, expansion, risk | CSM | Flag to leadership if Red |
| **W–12** | QBR / EBR — ROI evidence delivered | CSM + AE | Book 45–60 min with economic buyer |
| **W–10** | Champion 1:1 — pulse check | CSM | Uncover internal dynamics before commercial discussion |
| **W–8** | Expansion conversation — plant seeds, share roadmap | AE | Do not lead with pricing |
| **W–6** | Send renewal proposal | AE | Include multi-year option |
| **W–4** | Negotiation — address objections, finalise terms | AE + CSM | Escalate to VP if >X% discount required |
| **W–2** | Legal / procurement — contract redlines | AE + Legal | |
| **W–0** | Signed. Handoff to post-renewal success plan | CSM | Thank the champion; begin next cycle |

---

## 9. Success Criteria

- [ ] Renewal signed before deadline
- [ ] ARR outcome within target range
- [ ] Champion relationship maintained or improved
- [ ] At least one expansion conversation started
- [ ] ROI evidence documented and accepted by customer

## Quality Checks

- [ ] Stakeholder map includes the economic buyer — not just the champion
- [ ] Risk register has a mitigation for every H/H risk
- [ ] Value story uses product data and business outcomes — not feature lists
- [ ] Commercial strategy includes a floor discount and a reason-to-discount framework
- [ ] Timeline starts at least 90 days before renewal date
- [ ] Objection responses are specific to this account

## Anti-Patterns

- [ ] Do not start renewal conversations less than 90 days before the renewal date for accounts over $50K ARR
- [ ] Do not build a renewal strategy without first honestly assessing account health
- [ ] Do not treat all renewal objections as negotiating tactics — some signal genuine dissatisfaction
- [ ] Do not offer discounts as the first response to price objections
- [ ] Do not close the renewal without confirming the expansion opportunity

## Gotchas

**Trigger conflicts:**
- This skill and `cs-health-scorecard` are a chain. If you have not run a health scorecard yet, run it first — this playbook assumes you know the health status.
- This skill is for existing customer renewals only. For new prospect proposals, use `proposal-writer`.

**Known failure modes:**
- Objection responses are often written as generic scripts. Prompt: "Rewrite the objection responses using the specific account context I've provided."
- Timeline is sometimes compressed — Claude may default to a 30-day timeline. Always check that the timeline starts at W–16 (4 months out) for accounts above your ARR threshold.
- Expansion opportunity is often left blank when no explicit signals were provided. Prompt: "Based on the account profile, what are the most likely expansion opportunities even without explicit signals?"

**Filipino/Asian market specifics:**
- Philippine renewal conversations are often delayed by internal approval chains that are longer than Western equivalents. Build 2-3 extra weeks into the timeline for government-linked and conglomerate accounts.
- Do not raise price increases in the same conversation as the renewal ask. In Philippine accounts, this is perceived as a bait-and-switch and damages trust significantly.
- The champion may not have authority to approve the renewal — identify the economic buyer separately and plan a parallel engagement track.
- Verbal commitments ("oo, itutuloy namin") do not substitute for a signed PO. Always confirm the procurement process and who issues the PO.

## Example Trigger Phrases
- "Build a renewal playbook for [Account Name] renewing in [Month]"
- "Help me plan the renewal strategy for an at-risk customer"
- "Prepare a renewal brief for my QBR with [Company]"
- "What's my renewal strategy for a Red account coming up in 60 days?"
