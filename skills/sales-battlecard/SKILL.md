---
name: sales-battlecard
description: "Create a competitive sales battlecard for any competitor. Use when asked to build a battlecard, competitive comparison, sales cheat sheet, or objection handling guide for a specific competitor. Produces a one-page battlecard with positioning, differentiators, objection responses, and landmines. Do NOT use for full strategic competitive analysis — use competitor-teardown instead."
---

# Sales Battlecard Skill

Produces a practical one-page competitive battlecard that sales reps can use live on calls — not a theoretical analysis.

## Required Inputs
- **Your product/company**
- **Competitor name**
- **Your target customer** (ICP)
- **Your top 3 differentiators** vs this competitor
- **Common objections** when competing against them
- **Known competitor weaknesses**

## Output Structure

---

# Battlecard: [Your Product] vs [Competitor]
Updated: [Date] — Review quarterly

---

### In One Sentence
When a prospect mentions [Competitor], say: "[Your positioning in one sentence]"

---

### Why Customers Choose [Competitor]
(Be honest about their genuine strengths)
- [Strength 1]
- [Strength 2]

---

### Why Customers Choose Us
(Specific differentiators with proof points)
- **[Differentiator 1]:** [Proof point — customer outcome or capability]
- **[Differentiator 2]:** [Proof point]

---

### Objection Responses

**"[Competitor] is cheaper"**
"You are right their list price is lower. What our customers find is [specific TCO difference]. [Customer] saw [result]. Should we explore total cost of ownership?"

**"We already use [Competitor]"**
"That is helpful. What is working well? [Listen] And what is one thing you wish was better?"

**"[Competitor] has [feature] you do not"**
"You are right. What problem are you solving with that feature? [Listen] Here is how our customers solve that..."

---

### Landmines to Plant
- "How do you currently handle [area where competitor is weak]?"
- "What happens when you need to [scenario competitor struggles with]?"

---

### Traps to Avoid
- Never badmouth [Competitor] directly
- Do not lead with features — lead with the prospect problem
- Do not claim you do everything better — be specific about where you win

---

### When We Win / When We Lose
We win when: [Scenario — e.g. customer prioritises outcome over price]
We lose when: [Honest scenario — e.g. primary driver is lowest upfront cost]

## Quality Checks

- [ ] Competitor strengths are listed honestly (not minimised)
- [ ] Differentiators have proof points (not just claims)
- [ ] Objection responses are conversational (not scripted-sounding)
- [ ] Landmine questions are natural and non-confrontational
- [ ] "When we lose" is included and honest
- [ ] Battlecard has a review date

## Anti-Patterns

- [ ] Do not minimise genuine competitor strengths — unprepared reps lose credibility
- [ ] Do not write differentiators without proof points — a claim without evidence is marketing
- [ ] Do not make the battlecard exhaustive — it is a one-page cheat sheet, not a full analysis
- [ ] Do not include a "When we lose" section that is dishonestly optimistic
- [ ] Do not skip the review date — an outdated battlecard is worse than no battlecard

## Gotchas

**Trigger conflicts:**
- This skill and `competitor-teardown` both involve competitor analysis. Use THIS skill for a quick sales enablement one-pager for a specific rep use case. Use `competitor-teardown` for a deep strategic analysis for product planning or investor materials.
- Mutual exclusion: if the request mentions SWOT, positioning map, or messaging gaps analysis → route to `competitor-teardown`, not here.

**Known failure modes:**
- Claude may write objection responses that sound scripted. If they feel unnatural, ask: "Rewrite these as conversational — how a good rep would actually say it."
- "When we lose" section is sometimes softened or omitted. If missing, explicitly prompt: "Add a 'When we lose' section — be honest about loss scenarios."
- Battlecard may become too long (over 1 page when printed). Trim ruthlessly — battlecards longer than 1 page are not used on live calls.

**Filipino/Asian market specifics:**
- Direct competitor badmouthing is more culturally damaging in Philippine accounts than in Western markets. Landmine questions must be framed as genuine curiosity, not attacks.
- Price objections in Philippine SME and mid-market accounts are often real budget constraints, not negotiating tactics. Provide a TCO or phased payment angle, not just a value pitch.
- Relationship-based competitors (vendors who have a personal relationship with the client) are harder to displace on logic alone. Flag when a competitor has a relationship advantage — the sales approach shifts.

## Example Trigger Phrases
- "Build a battlecard against [competitor]"
- "Create a competitive cheat sheet for [competitor]"
- "Write objection handling for [competitor] comparisons"
