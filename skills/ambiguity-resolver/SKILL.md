---
name: ambiguity-resolver
description: "Structure vague opportunities and unclear briefs into actionable one-page problem statements. Use when asked to clarify a vague brief, frame an undefined problem, make sense of an unclear opportunity, or when the user says 'we need to figure out what to do about X' or 'I've been asked to look into Y'. Produces a structured problem brief with reframed questions, scoped boundaries, and a minimum viable research plan."
---

# Ambiguity Resolver Skill

Turn vague briefs and half-formed opportunities into structured, actionable problem statements — so you can reply with clarity instead of asking for three more meetings.

## Required Inputs

Ask the user for these if not provided:
- **The vague brief or opportunity description** (even a single sentence is enough)
- **Who asked for this** (stakeholder context shapes the framing)
- **Known constraints** (timeline, budget, team size — if any are known)

## Three-Stage Process

### Stage 1: Reframe
- Restate the vague input as 3-5 explicit questions that need answering
- Identify the unstated assumptions hidden in the brief
- Surface the real decision this feeds into

### Stage 2: Scope
- Define what is explicitly IN scope
- Define what is explicitly OUT of scope
- Identify the deadline pressure: urgent/important, important/not urgent, or unclear?
- Name who owns the final decision and who needs to be consulted

### Stage 3: Action
- Define the minimum viable research: 2-3 activities maximum
- Time estimate for each activity
- What each activity would tell you (and what it wouldn't)
- Proposed check-in point: when to regroup before committing to more

## Output Structure

### Problem Brief: [Opportunity Area]

**Restated as questions:**
1. [Question 1]
2. [Question 2]
3. [Question 3]

**Unstated assumptions we should surface:**
- [Assumption 1]
- [Assumption 2]

**In scope:** [Clear boundary]
**Out of scope:** [Clear boundary]
**Decision owner:** [Name/role]
**Timeline:** [Real deadline if known, or "unclear — recommend setting one"]

**Minimum viable research:**
| Activity | Time required | What it tells us | What it won't tell us |
|---|---|---|---|
| [activity] | [time] | [insight] | [limitation] |

**Proposed check-in:** After [activity], regroup to decide whether to proceed or pivot.

## Quality Checks

- [ ] Every reframed question is specific enough to research
- [ ] Scope boundaries name something concrete that is excluded
- [ ] Research activities are achievable within the stated timeline
- [ ] Decision owner is identified — not "leadership" but a specific person or role

## Anti-Patterns

- [ ] Do not reframe the brief into questions that are still too broad to research
- [ ] Do not list a research activity without stating what it would NOT tell you
- [ ] Do not leave the decision owner as "leadership" or "the team"
- [ ] Do not omit an explicit out-of-scope boundary

## Gotchas

**Trigger conflicts:**
- This skill is for structuring unclear problems before execution. If the brief is already clear and the ask is for a plan, use `gated-phase-plan` instead.
- If the vague brief is about a competitive landscape, route to `competitor-teardown` after running this skill to structure the question.

**Known failure modes:**
- Reframed questions are sometimes still too broad ("What is the best approach?"). Prompt: "Make each reframed question answerable by a specific research activity — if it's not researchable, it's too broad."
- Scope boundaries are often vague ("everything related to X"). Prompt: "Name one specific thing that is explicitly out of scope for this brief."
- Decision owner is frequently left as "the team" or "management." Prompt: "Who specifically will be making the final call? Name a role or person."

**Filipino/Asian market specifics:**
- In Philippine corporate culture, vague briefs often come from a superior who does not want to be seen as not knowing the answer. The real question is often unstated because asking it directly would be uncomfortable. Probe the brief with: "What decision is this feeding into — and who will be in the room when that decision is made?"
- "Let's explore options" from a Philippine executive often means "I already have a preferred option but want validation." Identify the preferred option early and test it explicitly in your reframing.
- Scope definition is culturally harder in Philippine teams because saying "that's out of scope" can feel like a refusal. Frame scope boundaries as focus, not refusal: "To give you the best answer on X, we'll focus here first."

## Example Trigger Phrases
- "Help me make sense of this brief: [paste brief]"
- "We need to figure out what to do about [topic]"
- "I've been asked to look into [area] — where do I start?"
- "This is unclear — can you help me structure it?"
