---
name: context-rot-protocol
description: "Manage session context health, detect context rot, and execute clean session handoffs. Use when a session is running long, when outputs start feeling inconsistent, when picking up a task from a previous session, or when you want to start a new session without losing progress. Triggers on: 'start a new session', 'context is getting long', 'pick up where we left off', 'session handoff', 'rewind', or any sign that the current session has drifted from clean reasoning. Also triggers automatically when a gated-phase-plan spans multiple sessions."
---

# Context Rot Protocol Skill

Context rot occurs when a session accumulates enough prior turns that Claude's reasoning begins to drift, repeat patterns, or silently ignore earlier instructions. This skill manages session health, detects rot signals, and executes clean handoffs.

## Context Rot Warning Signs

Rot is likely if any of the following are true:
- The session has been running for more than 60-90 minutes of active work
- Output quality has noticeably declined from earlier in the session
- Claude is repeating suggestions it already made
- Instructions from earlier in the session are being silently ignored
- Estimated token count is approaching 300-400k (in Claude Code: visible in session stats)
- You've made more than 3 corrections to the same type of error in one session

**Rule:** When in doubt, start a fresh session. A 2-minute handoff is cheaper than an hour of degraded output.

## Session Health Checkpoints

Run a checkpoint every 30-45 minutes of active work:

### Checkpoint Questions
1. Is the output quality consistent with the start of this session?
2. Have I had to repeat or re-explain any instruction more than once?
3. Am I more than halfway through the current gated phase plan?
4. Has anything unexpected happened that wasn't in the original plan?

If any answer is YES → run the Session Handoff Protocol below.

## Session Handoff Protocol

### Step 1: Capture Current State
Before ending the session, produce a State Snapshot:

```
## Session State Snapshot
Date: [Date/Time]
Plan: [Link to gated-phase-plan or brief description]
Last completed phase: Phase [N] — [Name]
Gate test result: [Pass / Fail / Partial]
Current status: [One sentence — exactly where we are]
Next action: [The very first thing to do in the new session]
Open issues: [Anything unresolved or uncertain]
Files changed: [List any files created or modified this session]
Verified URLs/paths: [Any URLs or file paths confirmed working this session]
Do NOT redo: [Anything that was completed and verified — list explicitly]
```

### Step 2: Save the Snapshot
- In claude.ai: paste the snapshot into a new Notion page or Outlook note before closing the session
- In Claude Code: save to `SESSION_STATE.md` in the repo root

### Step 3: Start Fresh
Open a new conversation. Begin with:

> "Continuing from previous session. Here is the state snapshot: [paste snapshot]
> Starting at: [Next action from snapshot]"

Do NOT summarise the entire previous session in the new context. Only include the snapshot — keep re-entry context under 200 words.

## Rewind Protocol

If a session has produced a bad output or gone in the wrong direction:

**In Claude Code:** Use `/rewind` to roll back to before the failed attempt.

**In claude.ai:** Do NOT try to correct the bad output in the same session — the bad reasoning is already in context. Instead:
1. Identify the last good state (the last output you trusted)
2. Write a State Snapshot from that point
3. Start a fresh session from the last good state
4. Explicitly tell the new session: "Do NOT do [what went wrong] — here's why it failed: [brief explanation]"

**Rule:** Correcting inside a rotted session contaminates the correction. Rewind > correct.

## Zero-Cost Session Management

Since you are on claude.ai (not Claude Code):
- No `/rewind` command available — use the fresh session method above
- No token counter visible — use time elapsed and output quality as proxies
- No session persistence — rely on State Snapshots saved to Notion or Outlook via MCP

## Quick Reference

| Situation | Action |
|---|---|
| Session running > 60 min | Run checkpoint questions |
| Output quality declining | Start handoff protocol now |
| Bad output produced | Rewind — fresh session from last good state |
| Returning to a previous task | Start with State Snapshot re-entry |
| Moving between gated phases across sessions | Use session boundary markers from gated-phase-plan |
| Unsure if context is rotted | Ask in the current session: "Summarise what we've done so far" — if the summary is wrong or incomplete, the context is rotted |

## Quality Checks

- [ ] State Snapshot is specific enough for a fresh session to resume without re-reading the full previous session
- [ ] "Next action" in the snapshot is the single, specific first action — not a phase name
- [ ] "Do NOT redo" section is filled in — prevents re-running completed work
- [ ] Snapshot is saved outside Claude (Notion, Outlook, file) before closing the session

## Gotchas

**Known failure modes:**
- State snapshots are often too vague. The test: could a different Claude instance pick up from this snapshot alone, without reading anything else? If not, it's not specific enough.
- "Next action" is often written as a phase name rather than a specific command or step. Write it as: "Run [specific command]" or "Open [specific file] and [specific action]."
- The "Do NOT redo" section is frequently skipped, causing wasted time re-running completed work in the new session. Always fill it in.

## Example Trigger Phrases
- "Start a new session — here's where we are"
- "Save our progress before I close this"
- "Context is getting long — let's do a handoff"
- "Pick up where we left off on [task]"
- "Something went wrong — let's rewind"
