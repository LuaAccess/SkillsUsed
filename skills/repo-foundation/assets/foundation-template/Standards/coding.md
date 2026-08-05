# Coding Standards — {{PROJECT_NAME}}

## String quoting in hand-edited files
Any file likely to be edited directly in the GitHub web UI (question banks, content arrays, config objects) should use double quotes for string values, not single quotes.

Why: single-quoted strings containing an apostrophe (contractions, possessives) break on the very next character and crash the deploy with a `SyntaxError`. This has happened multiple times on the assessment platform's `resultQuotes.js` from direct GitHub edits. Double quotes don't have this failure mode for the common case of English text containing apostrophes.

## Direct GitHub edits generally
If this project will be hand-edited on GitHub between sessions (not just through a full dev/PR flow):
- Prefer flat, simple data structures (arrays of objects) over anything requiring matched brackets across many lines — easier to spot a broken edit
- Run a syntax check after any direct edit before considering it safe (a simple `node -c file.js` or equivalent parse check catches most breakage before it reaches a deploy)
- Watch for duplicate IDs and missing commas specifically — the two most common failure modes from manual array edits

## General
- Favor explicit over clever — this repo will likely be edited by future-you with less context than present-you has right now
