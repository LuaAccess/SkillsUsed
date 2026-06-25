---
name: executive-update
description: "Transform detailed product or project updates into concise executive briefings. Use when asked to write an executive update, leadership update, product update for the exec team, or a C-suite briefing. Produces a structured 250-word briefing with headline, key metrics, progress, risks, decisions needed, and next steps."
---

# Executive Update Skill

Produce a stakeholder update that busy executives will actually read — structured around what they care about: decisions, risks, and numbers.

## Required Inputs

Ask the user for these if not provided:
- **Product update or notes** (raw input to transform — even bullet points work)
- **Audience** (CEO, board, specific exec, or general leadership)
- **Period** (this week / sprint / month / quarter)
- **Key metrics** (what numbers matter to this audience)

## Executive Communication Principles
- Lead with the headline, not the context
- Every update should answer: "So what does this mean for the business?"
- Flag decisions needed clearly — don't bury asks in paragraphs
- Be honest about risks — executives hate surprises more than bad news

## Process
1. Read the full update provided
2. Identify: key metric movements, decisions required, risks to flag, wins to celebrate
3. Write in reverse pyramid style — most important first
4. Limit to 250 words maximum for the main body
5. Add a "Decisions Needed" section with clear options and your recommendation

## Output Structure

### [Project/Product] Update — [Date / Sprint / Month]
**Headline:** [One sentence on the most important thing]

**By the Numbers:**
- [Metric 1]: [value] ([vs. target / last period])
- [Metric 2]: [value] ([vs. target / last period])
- [Metric 3]: [value] ([vs. target / last period])

**Progress This Period:**
[3-4 bullet points, outcome-focused not activity-focused]

**Risks & Watch Items:**
[2-3 bullets — be direct, include mitigation]

**Decisions Needed:**
1. [Decision] — Options: [A] or [B] — Recommendation: [your view] — Needed by: [date]

**What's Next:**
[2-3 bullets on next period priorities]

## Quality Checks

- [ ] Whole update is under 250 words (if not, cut ruthlessly)
- [ ] Every metric includes a comparison point (vs. target or last period)
- [ ] Every risk has a mitigation or watch action
- [ ] Every decision needed has at least two options and a recommendation
- [ ] Written for a CFO or CEO — no jargon, all outcomes

## Anti-Patterns

- [ ] Do not lead with context or background — lead with the headline
- [ ] Do not present metrics without a comparison point
- [ ] Do not soften or spin risks — executives rely on these for resource decisions
- [ ] Do not present a "Decisions Needed" item without a recommendation
- [ ] Do not exceed 250 words in the main body

## Gotchas

**Trigger conflicts:**
- This skill produces a short briefing document (250 words). For a full status report with KPIs and project health, use `operations:status-report` instead.
- If the audience is a customer (not internal), use `qbr-deck` or `proposal-writer`.

**Known failure modes:**
- Claude often exceeds 250 words on first pass. After generating, explicitly prompt: "Count the words in the main body — trim to 250 if over."
- Decisions Needed section is sometimes left as a single option with no recommendation. Prompt: "Add a second option and state your recommendation explicitly."
- Risk section is frequently sanitised — Claude defaults to soft language. Prompt: "Rewrite the risks section without softening — state the actual risk plainly."

**Filipino/Asian market specifics:**
- Philippine executives often share these updates with counterparts outside the organisation. Write as if it may be forwarded — do not include politically sensitive internal commentary.
- Hierarchy matters in how risks are framed. For briefings going to a Filipino CEO or board, frame risks as "areas we are managing" rather than "things that are wrong" — directness without confrontation is the register to hit.
- If the update is for a government-linked entity, avoid any language that implies criticism of past decisions — even implied criticism damages relationships in this context.

## Example Trigger Phrases
- "Write an executive update on [project/product] for this week"
- "Turn these notes into a leadership briefing"
- "Summarise this sprint for the C-suite"
