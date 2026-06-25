---
name: fresh-context-review
description: "Review a plan, code, document, or output using a fresh context perspective — catching errors the original session missed. Use when you want a second-pass review of anything produced in the current or a previous session, before executing or submitting it. Triggers on: 'review this before I run it', 'second opinion on this plan', 'check this for errors', 'fresh eyes on this', or any request to review a deliverable with no prior session context. Also triggers automatically after gated-phase-plan is produced and before execution begins."
---

# Fresh Context Review Skill

A fresh context catches errors the original session missed because it carries no assumptions, no sunk cost, and no prior reasoning that led to the output. This skill structures a clean, adversarial review of any plan, document, code, or output before it is executed or submitted.

## When to Use This Skill

**Always use before:**
- Executing a gated phase plan
- Committing code or files to a repository
- Sending a proposal, executive update, or client-facing document
- Running an automation or workflow for the first time

**Especially use when:**
- The original session was long (>30 min of active work)
- The output was produced under time pressure
- You made corrections to the output mid-session

## How to Run a Fresh Context Review

### Option A: New Session (Recommended)
1. End the current session
2. Open a new conversation
3. Paste ONLY the item to review — do not include the backstory of how it was produced
4. Say: "Review this [plan/code/document] as if you've never seen it before. Find problems."

### Option B: In-Session Review (Acceptable for short outputs)
1. Say: "Ignore everything we've discussed. Review only what I'm about to paste as if seeing it for the first time."
2. Paste the output
3. Claude will attempt a fresh-context review, but note: this is less reliable than a true new session because prior context is still present

## Review Framework

When reviewing any output, apply these four lenses:

### Lens 1: Assumption Check
- What assumptions are baked into this output that were never stated explicitly?
- Which assumptions, if wrong, would make this plan / document / code fail?
- Flag each assumption as: [LOW RISK — likely true] / [MEDIUM RISK — should verify] / [HIGH RISK — verify before proceeding]

### Lens 2: Gap Detection
- What is missing that should be here?
- What edge cases are not handled?
- What happens when the first thing that can go wrong, goes wrong?
- Is there a step that assumes something was done in a previous step that wasn't explicitly verified?

### Lens 3: Logic Check
- Does the sequence of steps make sense?
- Does each step's output feed correctly into the next step?
- Are there any circular dependencies or steps in the wrong order?
- Is the end state definition specific enough to know when it's been reached?

### Lens 4: Execution Risk
- What is the single most likely point of failure in this output?
- If this fails silently (no error message), how would you know?
- What is the cost of this failing mid-execution vs. not starting?

## Output Format

```
## Fresh Context Review: [Item reviewed]
Reviewed: [Date]

### Assumptions Found
1. [Assumption] — Risk: [LOW / MEDIUM / HIGH] — Recommendation: [verify / accept / address]

### Gaps Found
1. [Gap description] — Severity: [BLOCKING / IMPORTANT / MINOR]

### Logic Issues
1. [Logic issue description] — Location: [Where in the output]

### Top Execution Risk
[Single highest-risk failure point and how to mitigate it]

### Verdict
[ ] PASS — ready to execute
[ ] PASS WITH CONDITIONS — execute after addressing: [list conditions]
[ ] FAIL — do not execute until the following are resolved: [list blockers]
```

## Quality Checks

- [ ] Review was done with no context from the original session (or explicitly noted if in-session)
- [ ] All four lenses applied — not just a surface read
- [ ] Every HIGH RISK assumption has a recommended action
- [ ] Every BLOCKING gap has a resolution before execution
- [ ] Verdict is explicit — not "looks mostly okay"

## Anti-Patterns

- [ ] Do not skip fresh context review on long plans to save time — the time saved is less than the time lost to a mid-execution failure
- [ ] Do not accept "looks good to me" as a review outcome — every review must produce at least one finding or explain why none were found
- [ ] Do not review your own work in the same session that produced it — you will miss what you missed the first time

## Gotchas

**Known failure modes:**
- In-session reviews often miss the same errors as the original because the reasoning context is still active. For anything with real consequences (code commits, client documents, live deployments), always use a new session.
- Reviews sometimes produce only positive findings. Prompt: "Find at least one problem with this — if you cannot, explain why each of the four lenses returned no issues."
- Verdict is sometimes omitted. The verdict is the whole point — always end with an explicit PASS / PASS WITH CONDITIONS / FAIL.

**Integration:**
- Use after `gated-phase-plan` produces a plan, before execution begins
- Use after `proposal-writer` or `executive-update` before sending to a client or executive
- Use after any skill that produces a file before committing to GitHub

## Example Trigger Phrases
- "Review this plan before I run it"
- "Fresh eyes on this — what did I miss?"
- "Second opinion on this proposal before I send it"
- "Check this code/plan/document for errors I might have missed"
