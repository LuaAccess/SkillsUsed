---
name: gated-phase-plan
description: "Create a phase-wise gated implementation plan with explicit pass/fail tests for each phase gate. Use when planning any multi-step initiative, project, or workflow build that requires structured execution with verification checkpoints. Triggers on: 'build a plan', 'plan this out', 'phase this project', 'create an implementation plan', or any request to structure a multi-step task before executing it. Produces a phased plan where each phase has a gate test that must pass before the next phase begins."
---

# Gated Phase Plan Skill

Produces implementation plans where progress is gated — each phase must pass a defined test before the next phase begins. Prevents context rot from accumulating on a broken foundation.

## When to Use This Skill

Use before executing any task that involves:
- More than 3 steps
- Multiple files, systems, or connectors
- Risk of one step's failure breaking a later step
- Work that will span multiple sessions

Do NOT just list steps. Every phase requires a gate test.

## Required Inputs

- **What are we building or doing?** (one sentence)
- **End state definition** — what does "done" look like?
- **Known constraints** (tools available, time, zero-cost only, etc.)
- **Risk areas** — what's most likely to go wrong?

## Output Structure

---

# Gated Phase Plan: [Initiative Name]

**Goal:** [One sentence — what success looks like]
**End state:** [Specific, verifiable outcome]
**Constraints:** [List]
**Session approach:** [Single session / Multi-session — flag if context rot is a risk]

---

## Phase 0: Pre-flight Checks
**What:** Verify all prerequisites exist before starting
**Actions:**
- [ ] [Prerequisite 1] — verify with: [specific check]
- [ ] [Prerequisite 2] — verify with: [specific check]

**Gate test:** All prerequisites confirmed. If any fail, stop and resolve before Phase 1.

---

## Phase 1: [Name]
**What:** [What this phase accomplishes]
**Why first:** [Why this must come before Phase 2]
**Actions:**
- [ ] [Specific action 1]
- [ ] [Specific action 2]

**Gate test:** [Specific, verifiable condition that confirms Phase 1 is complete and correct]
- Pass condition: [What you expect to see]
- Fail condition: [What indicates something went wrong]
- If fail: [What to do — do NOT proceed to Phase 2]

---

## Phase 2: [Name]
**Depends on:** Phase 1 gate passed
**What:** [What this phase accomplishes]
**Actions:**
- [ ] [Specific action 1]
- [ ] [Specific action 2]

**Gate test:** [Specific, verifiable condition]
- Pass condition: [What you expect to see]
- Fail condition: [What indicates something went wrong]
- If fail: [Rollback or fix instruction]

---

## Phase N: [Final Phase]
**What:** Final delivery or integration
**Actions:**
- [ ] [Final action]

**Gate test:** End state verification
- Pass condition: [The "done" definition from the top of this plan is met]
- Fail condition: [What partial completion looks like — not done]

---

## Session Boundary Markers

If this plan spans multiple sessions, mark re-entry points:

| Re-entry point | How to verify where you are | First action on re-entry |
|---|---|---|
| After Phase 1 | [Check to confirm Phase 1 is complete] | [First action of Phase 2] |
| After Phase 2 | [Check to confirm Phase 2 is complete] | [First action of Phase 3] |

See `context-rot-protocol` skill for full session management guidance.

---

## Risk Register

| Risk | Phase it affects | Mitigation |
|---|---|---|
| [Risk 1] | Phase [N] | [Mitigation] |

## Quality Checks

- [ ] Every phase has a gate test with explicit pass AND fail conditions
- [ ] No phase depends on assumptions from a previous phase — gate tests eliminate assumptions
- [ ] Session boundary markers included if plan spans multiple sessions
- [ ] End state is specific and verifiable — not "it works" but a measurable condition
- [ ] Pre-flight phase exists and checks all dependencies

## Anti-Patterns

- [ ] Do not write phases without gate tests — a phase list without tests is just a to-do list
- [ ] Do not allow "looks right" as a gate test — every test must produce a specific observable output
- [ ] Do not proceed to the next phase if the gate test fails — stop, diagnose, fix, re-test
- [ ] Do not skip the pre-flight phase to save time — unverified prerequisites are the most common source of mid-plan failure

## Gotchas

**Known failure modes:**
- Gate tests are often written as subjective checks ("verify it works"). Push back: every gate test must specify what command to run, what URL to check, what file to verify, or what output to expect.
- Plans are often written without fail conditions. The fail condition is as important as the pass condition — without it, you don't know when to stop.
- Multi-session plans without re-entry markers cause context rot when returning to a half-complete plan. Always include the session boundary section for any plan with more than 4 phases.

**Integration with other skills:**
- After generating this plan, use `fresh-context-review` to review it in a new session before executing.
- During execution, use `context-rot-protocol` to manage session boundaries.
- If a phase fails and the path forward is unclear, use `screenshot-debug` to capture the failure state before asking for help.

## Example Trigger Phrases
- "Plan the build for [initiative] with phase gates"
- "Create a gated implementation plan for [task]"
- "Phase this out before we start building"
- "Build me a plan with checkpoints for [project]"
