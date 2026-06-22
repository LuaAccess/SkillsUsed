[it-consulting-battlecard_SKILL.md](https://github.com/user-attachments/files/29187646/it-consulting-battlecard_SKILL.md)
---
name: it-consulting-battlecard
description: Build a competitive battlecard or positioning guide for an IT consulting bid or sales situation. Use when competing against another system integrator, MSP, or technology vendor on a specific deal, when preparing for a competitive sales conversation, when a client mentions a competitor by name, or when you need to sharpen your differentiation for a specific account or segment. Trigger phrases include "we're competing against", "client mentioned [competitor]", "how do we beat [competitor]", "build a battlecard for", "competitive positioning for", "what's our edge vs", or "they also talked to [other vendor]". Do NOT use for general market research (superclaude:deep-research), full proposal writing (consulting-proposal), or brand monitoring (brightdata-plugin:brand-listening).
argument-hint: "<competitor name or deal context>"
---

# /it-consulting-battlecard

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Build a sharp, deal-specific competitive battlecard for an IT consulting or managed services bid — grounded in how clients in the Philippine and Asian market actually decide.

## Usage

```
/it-consulting-battlecard $ARGUMENTS
```

Examples:
- `/it-consulting-battlecard Competing against Accenture for a network modernisation bid at a local bank`
- `/it-consulting-battlecard Client mentioned they're also talking to Globe Business and PLDT Enterprise`
- `/it-consulting-battlecard Build a general battlecard vs large SIs for mid-market PH clients`
- `/it-consulting-battlecard How do we position against a cheaper local competitor with existing client relationship`

---

## Workflow

### 1. Competitive Context Intake

Parse or ask for:

- **Competitor(s):** Who you're up against — name, type (global SI / local MSP / telco / freelance / in-house IT team)
- **Deal context:** Client industry, size, engagement type, decision timeline
- **Your current positioning:** How has the client framed your solution so far
- **Known competitor strengths:** What you know they're leading with
- **Client's likely evaluation criteria:** Price / brand / local presence / technical depth / relationship / speed
- **Relationship dynamics:** Do they already have a relationship with the competitor

---

### 2. Competitor Profile

```markdown
## Competitor: [Name]

**Type:** [Global SI / Regional SI / Telco / Local MSP / Boutique / In-house IT]
**Known strengths in PH market:**
- [Strength 1]
- [Strength 2]

**Known weaknesses / common client complaints:**
- [Weakness 1]
- [Weakness 2]

**Typical pricing posture:** [Premium / Mid-market / Low-cost / Bundle-dependent]
**Relationship footprint:** [Deep enterprise / SMB-focused / Government / Telco-tied]
**How they typically win:** [Brand / Price / Relationships / Bundled services / Incumbency]
**How they typically lose:** [Slow delivery / Offshore resource quality / Lack of local support / Over-engineering]
```

---

### 3. Head-to-Head Comparison

```markdown
## Comparison: [Your Company] vs. [Competitor]

| Dimension | You | Competitor | Client Relevance |
|-----------|-----|------------|-----------------|
| Local presence and support | [Your position] | [Their position] | [Why this matters to this client] |
| Technical depth (this engagement type) | | | |
| Delivery track record (similar projects) | | | |
| Pricing model | | | |
| Speed to mobilise | | | |
| Client references in this industry | | | |
| Post-delivery support | | | |
| Senior-level involvement | | | |
| Cultural fit / communication style | | | |
```

---

### 4. Positioning Strategy

```markdown
## Your Positioning

**Core differentiation (1 sentence):**
[What you offer that they genuinely cannot — not a generic claim]

**Proof point:**
[Specific example, client name (if shareable), or measurable outcome]

**Land mines to plant:**
[Questions or requirements you can introduce that naturally expose the competitor's weaknesses — without attacking them directly]

**Traps to avoid:**
[Claims or comparison points that make you look weak or desperate]
```

---

### 5. Objection Responses

Generate responses to the 5 most likely competitive objections:

```markdown
## Objection Handling

**"[Competitor] has more resources / is a bigger company"**
Response: [Your answer — reframe size as a liability for this engagement type, not an asset]

**"[Competitor] quoted lower"**
Response: [Do not match price. Reframe to total cost of engagement, risk of under-delivery, and value of what you're actually comparing]

**"We already have a relationship with them"**
Response: [Acknowledge the relationship. Reframe the question: is this the right engagement to test a new approach, or is the status quo what the client really wants to protect?]

**"[Competitor] has done this for bigger clients"**
Response: [Scale of past projects ≠ fit for this engagement. Redirect to relevant match — right-sized team, local support, faster decision-making]

**"We need to run a full procurement process / get 3 quotes"**
Response: [Don't fight the process. Position to be the reference point they compare others against — not one of three generic bids]
```

---

### 6. Cultural Power Dynamics in Competitive Bids

Apply to every battlecard — do not skip this section:

```markdown
## Cultural Competitive Intelligence

**Incumbent advantage:**
In Philippine business culture, replacing an incumbent vendor requires more than being better — it requires giving the client a face-saving reason to change. Frame your proposal as "complementing and upgrading" not "replacing."

**Relationship vs. capability:**
If the competitor has a stronger personal relationship with the client, winning on technical merit alone will fail. Identify your relationship entry points — mutual contacts, existing touchpoints, anyone who can vouch for you internally.

**Brand perception:**
Global SI brands carry prestige in PH enterprise — especially in banking, telco, and government. Counter this by reframing brand as risk: "Large SIs rotate resources. We give you the same senior team throughout."

**Price sensitivity:**
PH clients often negotiate as a ritual, not a signal of disqualification. Know your floor. Do not collapse on price — it signals that your original price was inflated, which destroys trust.

**Decision-maker mapping:**
Technical evaluators rarely have final say in PH enterprise. Map the real decision path: who signs off, who has veto power, who is politically invested in the incumbent.
```

---

### 7. Deal-Specific Battleplan

```markdown
## Battleplan for This Deal

**Your strongest move:** [Single highest-leverage action right now]
**Timing:** [When to execute]
**Who to reach in the account:** [Your target contact for next conversation]
**Message to land:** [The one thing they should believe about you vs. the competitor after your next conversation]
**Red flags to watch for:** [Signs this deal is moving toward the competitor despite positive signals]
```

---

## If Connectors Available

**HubSpot:**
- Log competitive intelligence to deal record
- Tag deal with competitor name for pipeline analysis
- Update deal risk level

**Microsoft 365 / Teams or Outlook:**
- Draft internal briefing for your team before a competitive presentation

**Notion:**
- Save battlecard to your competitive intelligence knowledge base

---

## Philippine IT Consulting Competitive Landscape — Common Patterns

| Competitor Type | How They Win | How They Lose | Your Counter |
|----------------|--------------|---------------|--------------|
| Global SI (Accenture, IBM, Deloitte) | Brand, enterprise cred, large team | Slow, expensive, offshore delivery, junior-heavy on-site | Speed, senior local team, right-sized engagement |
| Telco bundlers (Globe Business, PLDT Ent) | Existing relationship, bundled pricing | Scope is narrow, IT consulting depth is thin | Depth of expertise, vendor-neutral advice |
| Local MSPs | Price, local relationships, Filipino-owned | Resource depth, enterprise project experience | Proven delivery, scalability, structured methodology |
| Regional SIs (regional APAC firms) | Competitive pricing + enterprise process | Less local presence, cultural gap | Local-first team, faster escalation path |
| Freelancers / small IT shops | Cheap, flexible, fast | Risk, accountability, no SLA | Formal engagement, risk mitigation, accountability structure |
| In-house IT team (as alternative) | Zero cost, internal knowledge | Capacity, skill gaps, political cover if it fails | Risk-transfer argument, speed, specialist depth |

---

## Tips

1. **Never attack a competitor directly.** In Philippine business culture, speaking negatively of a competitor signals insecurity and is considered poor form. Let your positioning make the comparison without you saying the words.
2. **Winning the evaluation ≠ winning the deal.** You can score highest on a technical evaluation and still lose because someone senior prefers the relationship they have. Map the real decision early.
3. **Your best competitive weapon is specificity.** Generic claims cancel out. "We've delivered a network modernisation for a Tier 2 bank in 90 days with zero downtime" beats "We have extensive banking experience."
4. **Reframe price competition.** If you're being compared on price, you've already lost the differentiation battle. Return the conversation to outcomes, risk, and post-delivery accountability.
5. **The competitor's relationship is your intelligence source.** Ask the client what they like about working with that vendor — it tells you exactly what they value and what you need to match or exceed.
