---
name: account-plan
description: "Build a structured account plan for any key customer or target account. Use when asked to create an account plan, key account strategy, strategic account review, or territory plan. Produces a complete account plan with relationship map, growth opportunities, risks, and 90-day action plan."
---

# Account Plan Skill

Produces a structured account plan — the document that separates account managers who grow accounts from those who just service them.

## Required Inputs
- **Account name**
- **Current ARR / revenue**
- **Contract renewal date**
- **Key contacts** (names, roles, relationship strength)
- **Products/services currently in use**
- **Known opportunities or expansion areas**
- **Known risks**
- **Planning horizon** (6 / 12 / 24 months)

## Output Structure

---

# Account Plan: [Account Name]
**Account Manager:** [Name] | **Period:** [Date range]

---

### Account Snapshot

| Metric | Current | Target (EOY) |
|---|---|---|
| ARR / Revenue | ₱/$/£[amount] | ₱/$/£[target] |
| NPS / Health score | [Score] | [Target] |
| Products in use | [List] | [Expansion targets] |
| Renewal date | [Date] | — |
| Risk level | Low / Medium / High | — |

---

### Relationship Map

| Name | Title | Influence | Relationship | Notes |
|---|---|---|---|---|
| [Name] | [Role] | Decision maker / Influencer / User | Strong / Neutral / Weak | [Insight] |

**Relationship gaps:** [Who we do not have access to that we should]
**Executive sponsor:** [Do we have one? If not — who could become one?]

---

### Why They Stay (Retention Anchors)
[2-3 specific reasons this account renews. If the list is short, that is the risk signal.]

---

### Growth Opportunities

| Opportunity | Product | Est. Value | Timeline | Next Action |
|---|---|---|---|---|
| [Opportunity] | [Product] | ₱/$/£[value] | [Q/Year] | [Specific action] |

**Whitespace:** What products do we have that this account does not use, and why?

---

### Risks and Mitigation

| Risk | Likelihood | Impact | Mitigation | Owner |
|---|---|---|---|---|
| [Risk] | H/M/L | H/M/L | [Action] | [Name] |

---

### 90-Day Action Plan

| Action | Why | Owner | Due |
|---|---|---|---|
| [Specific action] | [Why it matters] | [Name] | [Date] |

**Next QBR / EBR:** [Date — if no EBR cadence, flag as a risk]

---

### Success Criteria
At end of [period]:
- Renewed at or above current ARR
- [Expansion opportunity] progressed to [stage]
- Health score moved from [current] to [target]

## Anti-Patterns

- [ ] Do not list only executive contacts in the relationship map — champions and day-to-day users often influence renewal more than executives
- [ ] Do not set growth opportunity estimates without a basis — rough values are better than none
- [ ] Do not treat "no known risks" as acceptable — if no risks are identified, the plan hasn't been scrutinised honestly
- [ ] Do not write 90-day actions as vague aspirations — each must specify a call, meeting, or deliverable with a named owner

## Quality Checks

- [ ] Relationship map identifies decision-makers, influencers, and relationship gaps
- [ ] Risks all have mitigation actions and named owners
- [ ] Growth opportunities include estimated value (even roughly)
- [ ] 90-day actions are specific — not "have a call" but what call, with whom, to achieve what
- [ ] Success criteria are measurable at end of planning period

## Gotchas

**Trigger conflicts:**
- This skill is for existing accounts. For new prospects, use `discovery-call-prep`. For upcoming renewals specifically, use `renewal-playbook` which has a more detailed commercial strategy layer.
- If the request is for a QBR presentation rather than an internal strategy doc, use `qbr-deck` instead.

**Known failure modes:**
- Relationship map is often produced with only the primary contact. Push back if only one person is listed: "Map at least 3 stakeholders — include someone below the main contact who uses the product daily."
- Growth opportunities section is sometimes filled with wishful thinking rather than evidence-based signals. Ask: "What signals indicate this opportunity is real — usage data, conversations, or project announcements?"
- 90-day actions sometimes slip into generic language. If they read as vague, prompt: "Rewrite each action as a specific meeting or deliverable with a date."

**Filipino/Asian market specifics:**
- Relationship map must account for informal power — in Philippine enterprises, a mid-level IT manager or executive assistant often has more access and influence than their title suggests. Map these people explicitly.
- "Why they stay" anchors in Philippine accounts are often personal relationships with the AM, not just product value. If the AM leaves, so might the account. Document relationship depth honestly.
- Family-owned conglomerates (common in PH) have concentrated decision power. Identify the family member or trusted advisor who holds final authority — they rarely appear in official org charts.

## Example Trigger Phrases
- "Build an account plan for [account name]"
- "Create a key account strategy for [company]"
- "Help me plan my territory for [quarter/year]"
