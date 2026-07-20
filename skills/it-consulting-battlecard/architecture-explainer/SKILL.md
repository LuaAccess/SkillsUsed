---
name: architecture-explainer
description: Teach technical or system architecture concepts (web stacks, APIs, infrastructure, scaling) using progressive mind-map style diagrams that start high-level and drill down on request, grounded in real well-known company examples, and a "build now vs add when triggered" framework for what infrastructure actually needs to exist yet. Use this whenever the user wants to understand a technical concept visually, asks for a mind map or diagram of a system, wants to compare their stack to real companies (e.g. Facebook, Instagram, Twitter/X, Telegram), needs to explain a technical roadmap to a non-technical stakeholder (CEO, client, investor) for buy-in or funding, or is deciding what to build now versus defer until scale demands it. Especially useful in IT consulting or sales contexts where translating technical depth into simple, decision-ready visuals for non-technical decision-makers is the actual deliverable.
---

# Architecture Explainer

Teaches technical architecture by layering understanding, not by dumping everything into one diagram or one wall of text. The pattern: **overview mind map → drill into one branch at a time → ground it in real companies → decide what's actually worth building now.**

## Step 1 — Start with an overview mind map, not a wall of text

When a concept has multiple parts (a stack, a system, a process), open with ONE compact mind-map-style diagram:
- Central node = the whole concept
- 3–4 branch nodes = the major categories (not more — this is a hard visual limit, not a style preference)
- Each branch gets a short subtitle (≤5 words) listing its components, not an explanation

Use the Visualizer's `diagram` module for this (structural or flowchart type). Make every branch node clickable via `sendPrompt` so the person can drill in without having to type a new question. Text explanation goes in the response around the diagram, never inside it.

Do not try to show every sub-detail in the first diagram. If the user's request lists 5+ components, that's a signal to decompose into an overview + focused sub-diagrams — never cram it all into one.

## Step 2 — Drill into one branch per turn

When the person taps a branch or asks to go deeper on one category:
- Build a NEW diagram focused only on that branch (flowchart for sequential/process concepts, structural for containment/architecture, illustrative for abstract mechanisms that benefit from a visual metaphor)
- Keep the same visual language (same color-per-category convention) as the overview so it reads as one connected mental model across turns, not disconnected one-offs
- Close with plain-language prose that explains what the diagram shows and connects it back to the bigger picture — never repeat the diagram's content in text, add to it

## Step 3 — Ground it with real, well-known examples

Abstract layers click faster when tied to companies the person already knows. When appropriate:
- Pick 2–4 well-known companies/products relevant to the domain
- Show what they actually used or use (acknowledge stacks change and aren't always fully public — frame as directionally accurate, not a live audit)
- Pull out the pattern that generalizes, not just trivia — the goal is a transferable principle (e.g. "they all started ordinary and only replaced pieces after hitting a measured bottleneck"), not a list of facts

## Step 4 — Apply the "build now vs add when triggered" framework

This is the core decision lens for any scaling/infrastructure question. Split every relevant layer into two tables:

**Build now regardless of size** — cheap today, expensive or risky to retrofit later (security holes, lost history, leaked secrets, broken trust). Examples: HTTPS, auth, version control, environment config, basic logging.

**Add only when triggered** — costs nothing to wait, and building early is speculative effort with no current payoff. Pair each item with the concrete signal that justifies adding it (e.g. "CDN → users complaining about slow loads, or traffic outside your home region"), not a vague "once you scale."

The organizing question to state explicitly: *does waiting cost more than doing it now?* That's the test, not "is this simple" or "is this common."

## Step 5 — Reframe for the audience if this is headed to a non-technical decision-maker

If the person mentions a CEO, investor, client, or funding ask:
- Lead with outcomes and risk, not mechanism ("your site could go down under real traffic" — not "DNS propagation delay")
- Flag if a text-to-image tool (Midjourney, DALL·E, etc.) was suggested for the diagram — these are unreliable at rendering multiple accurate text labels and risk visibly wrong content in front of a decision-maker. Recommend the Visualizer or the pptx skill for anything presentation-critical instead, and offer to build the actual deliverable (slide deck, one-pager) rather than just a chat visual.

## Notes

- Keep node/category counts small per diagram (≤4 branches, ≤3 sub-items per branch) — this is a hard constraint from the diagramming tool, not optional advice.
- Reuse a consistent color-per-category scheme across an entire explanation thread (e.g. one color for "client/frontend" concerns, another for "logic/backend," another for "data," another for "infrastructure") so diagrams built across multiple turns still read as one coherent model.
- Don't turn this into a lecture. One diagram, then prose, then stop and let the person direct where to go next — they may only want one branch, not the whole tree.
