---
name: problem-solving-sequence
description: Run a structured 5-stage problem-solving sequence (Diagnose → Compare → Reframe → Create → Validate) using 20 named frameworks (Fishbone, 5 Whys, First Principles, Force Field, Decision Matrix, Cost-Benefit, MECE, Six Thinking Hats, Inversion, Lateral Thinking, Analogous Reasoning, Counterfactual Reasoning, SCAMPER, TRIZ, Blue Ocean, Prototyping, Hypothesis Testing, Pre-Mortem, OODA Loop, SWOT). Use this whenever the user wants to brainstorm a decision, analyze a data/prediction system, evaluate multiple candidate strategies or approaches, or explicitly says "run the sequence," "diagnose this," "let's brainstorm this properly," or references any of the 20 named frameworks above. Especially trigger when the user has real data/backtest results and wants to decide which of several approaches actually wins, rather than picking by preference. ALSO trigger in Quick Ideation Mode, a lighter single-pass path rather than the full 5 stages, when the user wants fast idea generation instead of rigorous decision analysis, "quick brainstorm," "give me ideas fast," "master brainstorm," "trend intersection," "competitor gap," "content ideas for [platform]," or "business opportunity brainstorm." Mutual exclusion, if the user wants speed over rigor, route to Quick Ideation Mode and skip Stages 1-5, do not run both for the same request.
---

# Problem-Solving Sequence

A 5-stage framework for structured brainstorming and decision analysis. The point: **generate wide, then let evidence — not preference — decide what survives.**

## When to use this

- User wants to brainstorm or work through a decision, system design, or open problem
- User has multiple candidate approaches/strategies and needs to pick one
- User is debugging why something (a model, a plan, a system) isn't performing
- User explicitly invokes a stage or framework name (e.g., "run a pre-mortem on this")

If the user just wants a quick answer to a simple question, don't force the full sequence — use judgment. This is for genuine brainstorming/decision-support requests.

## The 5 Stages

Run in order. Each stage produces an output that feeds the next. Don't skip Stage 1 — solving the wrong problem well is worse than not solving it.

### Stage 1 — Diagnose the Real Issue
Find the true root cause before generating solutions.

| Framework | Use it to... |
|---|---|
| **Fishbone Diagram** | Bucket likely causes across People, Process, Tools, Environment |
| **5 Whys** | Ask "why" repeatedly until you hit a structural cause, not a symptom |
| **First Principles** | Strip the problem to bare facts, real constraints, and named assumptions |
| **Force Field Analysis** | List forces helping vs. blocking the goal |

**Output:** a short list of *real*, evidenced causes — not guesses.

### Stage 2 — Compare Options
Rank existing/obvious candidate approaches objectively.

| Framework | Use it to... |
|---|---|
| **Decision Matrix** | Score each option on cost, speed, risk, impact |
| **Cost-Benefit Analysis** | Weigh benefits vs. costs and reversibility |
| **MECE Principle** | Split the issue into non-overlapping, complete buckets |
| **Six Thinking Hats** | Force passes through facts, risk, upside, emotion, and process |

**Output:** a ranked shortlist — not one instinctive favorite.

### Stage 3 — Reframe the Problem
Break out of the first framing, which is usually too narrow.

| Framework | Use it to... |
|---|---|
| **Inversion** | Ask what would guarantee failure, then design against exactly that |
| **Lateral Thinking** | Force 5 non-obvious solutions using the same constraints |
| **Analogous Reasoning** | Borrow a solution pattern from an unrelated field |
| **Counterfactual Reasoning** | "If this assumption were false, what changes?" |

**Output:** a proper baseline/null hypothesis to beat, plus a wider solution space than the first instinct.

### Stage 4 — Create Better Solutions
Generate genuinely new candidates, not just tweaks.

| Framework | Use it to... |
|---|---|
| **SCAMPER** | Substitute, Combine, Adapt, Modify, Repurpose an existing idea |
| **TRIZ** | Resolve the core contradiction without trading off quality |
| **Blue Ocean Strategy** | Decide what to remove, reduce, raise, create |
| **Prototyping** | Build the fastest rough test instead of debating in the abstract |

**Output:** actual new candidates to test, not just parameter tweaks on old ones.

### Stage 5 — Validate Before Committing
Stress-test before committing resources. This is where "who wins" gets decided.

| Framework | Use it to... |
|---|---|
| **Hypothesis Testing** | Define the test, metric, and pass/fail threshold *before* running it |
| **Pre-Mortem Analysis** | Assume it failed in 90 days — work backward on why |
| **OODA Loop** | Observe → Orient → Decide → Act, then repeat |
| **SWOT Analysis** | Strengths, Weaknesses, Opportunities, Threats → turn each into an action |

## How "who wins" gets decided

Don't let the most articulate-sounding idea win by default. Instead:

1. Every candidate from Stages 2–4 gets evaluated against the **same criteria/test** (a backtest, a cost model, a real metric — whatever fits the domain)
2. Score using **one consistent metric** — flag if two candidates are being compared using different definitions of "success"
3. Anything that doesn't beat the Stage 3 baseline gets cut, regardless of how clever the technique that produced it
4. Log which framework produced the winning idea — useful for noticing which techniques are actually generative for this user over time

## Quick Ideation Mode (skip the 5 stages)

For fast idea generation where speed beats rigor — a pitch angle, a content idea, a quick gap check. Don't run Stages 1-5 for these; one pass is the point. Each row is a self-contained prompt structure, not a multi-step process.

| Framework | Use it to... | Prompt shape |
|---|---|---|
| **Master Brainstorm System** | Generate a full idea set in one pass when objective, audience, and constraints are all known upfront | "Goal: [OBJECTIVE]. Audience: [TARGET USERS]. Constraints: [LIMITATIONS]." → generate, rank by ROI/scalability/effort, pick top 10 |
| **Trend Intersection** | Find novel combos by overlapping two unrelated topics/trends | "Brainstorm ideas at the intersection of [TOPIC A] + [TOPIC B]" → surface hybrid/unexpected combinations |
| **Competitor Gap** | Spot positioning openings fast | "Topic: [TOPIC]. Identify competitors, strengths/weaknesses, gaps they leave open" → cheap differentiation angles |
| **Content Brainstorm** | Fill a content calendar by platform/audience | "Generate content ideas around [TOPIC]. Audience: [AUDIENCE]. Platform: [PLATFORM]." → mix of educational, story, case-study formats |
| **Business Opportunity Brainstorm** | Frame a raw idea as a startup-style opportunity | "Topic: [TOPIC]. Generate business opportunities: SaaS, agency, consulting, marketplace, subscription angles" → estimate size, difficulty, growth potential |

**When NOT to use Quick Mode:** if the user has real data to validate against, multiple candidates competing for resources, or explicitly wants rigor — route to the full 5-stage sequence instead. Quick Mode skips Stage 5 validation entirely, so nothing generated here should be treated as decided — only as raw material to feed into Stage 2+ if it needs to survive scrutiny.

## How to run this conversationally

- Move through stages in order but keep it scannable — short headers, not walls of text
- Don't run all 4 frameworks per stage if 1–2 clearly suffice for a simple case; use judgment on depth vs. speed
- At Stage 5, always push for a concrete, falsifiable test — vague validation ("this seems solid") defeats the purpose
- If the user has real data available, prefer computing the Stage 5 comparison directly (e.g., via code execution) over reasoning about it abstractly
- End by stating clearly which option won, why, and what would have to be true to reverse that call
