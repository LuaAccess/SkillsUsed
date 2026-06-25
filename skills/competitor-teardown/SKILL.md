---
name: competitor-teardown
description: "Produce a structured competitive analysis for any product or market. Use when asked for a competitor analysis, competitive teardown, market comparison, SWOT, or positioning map. Generates a structured teardown with positioning map, feature comparison, messaging gaps, and strategic recommendations. Do NOT use for a quick sales one-pager — use sales-battlecard instead."
---

# Competitor Teardown Skill

Produces a complete competitive analysis document — structured for use in strategy decks, investor materials, sales enablement, or product planning sessions.

## Required Inputs

Ask the user for these if not provided:
- **Your product** (name + one-line description)
- **Competitors to analyse** (list 2–5 names; if not provided, ask)
- **Analysis depth** (quick overview / detailed teardown)
- **Primary use case** (sales enablement / investor deck / internal strategy / product planning)

## Output Structure

### 1. Competitive Landscape Overview
One paragraph summarising the market dynamic: key players, how the market is segmented, and where the white space sits. Keep under 150 words.

### 2. Positioning Map
Describe a 2x2 positioning map in text form:
- Define the two axes relevant to this market
- Place each competitor in one quadrant with a one-sentence rationale
- Place the user's product and highlight the strategic implication

### 3. Feature Comparison Table

| Feature / Capability | [Your Product] | [Competitor A] | [Competitor B] | [Competitor C] |
|---|---|---|---|---|
| [Feature] | ✅ / ❌ / 🟡 Partial | | | |

Use ✅ (has it), ❌ (doesn't have it), 🟡 (partial/limited). Add a "Strategic Notes" column for features where the difference is a significant selling point or risk.

Include 10–15 rows. Note which cells need verification if data was not provided.

### 4. Messaging Analysis

For each competitor:
- **Their primary claim:** [what they say they do]
- **Target audience signal:** [who they seem to be targeting]
- **Emotional hook:** [fear / aspiration / authority / speed / simplicity]
- **Gap or weakness in their messaging:** [what they don't address that your product could own]

### 5. SWOT Summary

- **Strengths:** [2–3 genuine differentiators]
- **Weaknesses:** [2–3 honest gaps or vulnerabilities]
- **Opportunities:** [2–3 market gaps or competitor weaknesses to exploit]
- **Threats:** [2–3 competitor moves or market shifts to watch]

### 6. Strategic Recommendations

3–5 actionable recommendations. Frame each as: **"Given [observation], [your product] should [action] to [outcome]."**

## Quality Checks

- [ ] Axes on positioning map are meaningful and specific to this market
- [ ] Feature table includes strategic notes on key differentiators
- [ ] Messaging analysis covers all named competitors
- [ ] SWOT is honest — Weaknesses and Threats should not be softened
- [ ] Recommendations are specific and actionable

## Anti-Patterns

- [ ] Do not mark feature presence as equivalent across competitors without noting quality differences
- [ ] Do not position the user's product in the most favourable quadrant without justification
- [ ] Do not soften Weaknesses or Threats in the SWOT
- [ ] Do not include unverifiable claims without flagging them as assumptions

## Gotchas

**Trigger conflicts:**
- This skill and `sales-battlecard` both cover competitor analysis. Use THIS skill for deep strategic analysis (product planning, investor prep, strategy decks). Use `sales-battlecard` for a one-page sales enablement tool reps can use on calls.
- Mutual exclusion: if the request says "quick cheat sheet," "one-pager," or "for reps to use on a call" → route to `sales-battlecard`.

**Known failure modes:**
- Feature comparison table cells are frequently left as assumptions. Prompt: "Mark every unverified feature with *(unverified — check)*."
- SWOT Weaknesses section is often sanitised. Prompt: "Be honest in the Weaknesses section — what would a sceptical investor challenge us on?"
- Positioning map can feel self-serving. Prompt: "If a competitor wrote this positioning map, where would they place us?"

**Filipino/Asian market specifics:**
- For Philippine market teardowns, pricing transparency from competitors is often limited. Mark pricing comparisons as estimated and suggest direct verification via sales engagements.
- Local competitors (Philippine-based vendors) often win on relationship and local support, not features. Include a "Relationship / Local Presence" row in the feature comparison table.
- Competitor intel gathered from clients in the Philippines is often incomplete due to face-saving norms — clients won't say a competitor is bad directly. Read between the lines of what features they ask about.

## Example Trigger Phrases
- "Do a competitor analysis of [Product] vs [Competitor A] and [Competitor B]"
- "Tear down [Competitor]'s positioning"
- "Give me a competitive landscape for [market]"
- "Build a SWOT for our product against [competitor]"
