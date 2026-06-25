---
name: screenshot-debug
description: "Debug a stuck, broken, or unexpected situation by capturing and sharing a screenshot of the current state. Use when text descriptions of an error are not resolving the issue, when Claude needs to see what you're seeing, when UI behavior is unexpected, or when you're stuck and a screenshot would give more information than a text description. Triggers on: 'I'm stuck', 'it's not working', 'here's a screenshot', 'can you see what's wrong', or any situation where visual state matters more than a text description."
---

# Screenshot Debug Skill

When text descriptions of a problem fail to resolve it, a screenshot provides ground truth. This skill structures when and how to use screenshots effectively in debugging sessions.

## When to Use a Screenshot

**Use a screenshot when:**
- An error message appears on screen that is hard to transcribe accurately
- UI behavior is not matching what was expected from instructions
- A file, form, or interface is not displaying as expected
- You've described a problem twice and the suggested fix hasn't worked
- The issue involves a GitHub web editor, a tool UI, or a browser-based workflow
- You want to verify that a setup or configuration looks correct before proceeding

**Skip the screenshot when:**
- The error is a text log output — paste the text directly instead (more reliable than a screenshot of text)
- The issue is a code logic error — paste the code directly
- The error is in a terminal or CLI — paste the output directly

## How to Take a Useful Screenshot

### Capture the Right Area
Include in the screenshot:
- The error message or unexpected state (centred, fully visible)
- Enough surrounding context to identify where in the interface this is
- Any relevant URL bar if it's a web tool
- Any status indicators (green/red icons, checkboxes, loading states)

Do NOT crop so tightly that the surrounding context is lost.

### Annotate Before Sharing (Optional but Recommended)
If the screenshot has multiple things happening:
- Draw a red circle or arrow pointing to the specific problem
- Add a text note if the problem area is ambiguous

### On Android (Your Primary Device)
- Screenshot: Press Power + Volume Down simultaneously
- Share: Use the Share button in the screenshot preview → Claude app
- Alternatively: Screenshot → Gallery → share to Claude

## How to Share the Screenshot with Claude

In Claude.ai (web or mobile):
1. Take the screenshot
2. In the chat input, tap the attachment/paperclip icon
3. Select the screenshot from your gallery
4. Add a message: "Here is a screenshot of the issue. [Brief description of what you expected vs. what you see]"

**Format your message as:**
> "Expected: [what should have happened]
> Actual: [what is happening — point to it in the screenshot]
> Last action taken: [what you did right before this state appeared]"

## What Claude Does With the Screenshot

On receiving a screenshot, Claude will:
1. Identify the specific error, unexpected state, or discrepancy
2. Compare it against the expected state from the current plan
3. Diagnose the most likely cause
4. Provide a specific fix — not a generic suggestion

## Debug Log Protocol

Before sharing a screenshot, build a brief debug log to give Claude full context:

```
## Debug Log
Task: [What were you trying to do?]
Step: [Which step of the plan were you on?]
Last action: [Exactly what you did before the problem appeared]
Expected result: [What should have happened]
Actual result: [What happened instead — describe AND attach screenshot]
Already tried: [Any fixes you've already attempted]
```

Paste the debug log with the screenshot. This combination resolves most issues in one exchange instead of multiple back-and-forths.

## Common Screenshot Scenarios

### GitHub Web Editor Issues
Capture: the full editor window including the file path breadcrumb, the content area, and any error banners at the top of the page.

### YAML Frontmatter Artifact
Capture: the raw file view starting from line 1 — the screenshot should show whether line 1 is `---` or contains extra content before it.

### MCP Connector Errors
Capture: the error message in full, including the connector name and any error code visible.

### Unexpected Claude Output
Take a screenshot of the conversation rather than trying to describe the output — this gives exact context including what was said before the unexpected response.

## Quality Checks

- [ ] Screenshot includes enough context to identify where in the interface the issue is
- [ ] Debug log is included alongside the screenshot
- [ ] "Expected vs. Actual" is stated explicitly in the message
- [ ] Text-based errors (logs, terminal output, code) are pasted as text, not screenshotted

## Gotchas

**Known failure modes:**
- Screenshots of text (error logs, code, terminal output) are less reliable than pasting the text directly — Claude can miss characters in low-contrast screenshots. Always paste text output as text.
- Screenshots without context (cropped to just the error) often lack enough information to diagnose. Include the surrounding UI.
- On Android, screenshots sometimes include the notification bar — this is fine and doesn't affect the debug.

**Integration:**
- Use this skill when a `gated-phase-plan` phase gate fails and the failure reason is unclear from text description alone
- Use when `fresh-context-review` identifies a potential issue and you need to confirm whether it's actually present in the live state

## Example Trigger Phrases
- "I'm stuck — here's a screenshot"
- "It's not working — let me show you"
- "Can you see what's wrong with this?"
- "Here's what I'm seeing — does this look right?"
- "The UI isn't matching what you described — screenshot attached"
