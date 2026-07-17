---
name: go-to-market
description: "Create go-to-market assets for any product or feature. Use when asked for a GTM plan, positioning statement, product launch plan, messaging pillars, use cases, or feature/benefit list. Produces a full GTM pack: positioning statement, messaging pillars, feature-to-benefit mapping, and role-specific use cases. Do NOT use for a competitor-specific one-pager — use sales-battlecard instead. Do NOT use for deep competitive market analysis — use competitor-teardown instead. Do NOT use for an internal leadership briefing — use executive-update instead."
---

# Go-To-Market Skill

Produces a complete go-to-market asset pack for a product, feature, or initiative. Follows Geoffrey Moore's positioning framework and structures all outputs for use in sales decks, landing pages, launch emails, and internal alignment docs.

## Working from a brief

Always deliver the full GTM pack anyway — do not stop to ask questions and do not leave bracketed placeholders. Where a detail is missing, infer specific, realistic ones from the product description and target customer, and mark anything inferred as *(assumed — confirm)*.

## Inputs (infer any not provided — label assumptions)

- **Product/feature name**
- **One-line description** (what it does, technically)
- **Target customer** (role, company size, industry if relevant)
- **Primary problem it solves**
- **Key competitor or alternative** (what people do today without this)
- **Top 3 differentiators**

## Output Structure

### 1. Positioning Statement

Use the Geoffrey Moore format exactly:

> For **[target customer]** who **[has this problem or need]**, **[Product Name]** is a **[product category]** that **[key benefit/outcome]**. Unlike **[primary alternative or competitor]**, our product **[key differentiator]**.

Write one primary positioning statement, then offer a shorter tagline version (10 words or fewer).

---

### 2. Messaging Pillars

Generate 3–5 messaging pillars. Each pillar must include:
- **Pillar name** (2–4 words, bold)
- **One-sentence summary** of what this pillar claims
- **2–3 proof points** (specific; if no data was provided, infer a realistic one and mark it *(assumed)*)
- **Example use in copy** (one sentence as it would appear in a landing page or deck)

---

### 3. Feature & Functionality List

| Feature / Functionality | Buyer Benefit (what it means for the user) |
|---|---|
| [Technical capability] | [Outcome in plain language — start with a verb] |

Rules:
- Never list a feature without a corresponding benefit
- Benefits should reference the target customer's workflow or pain point
- Aim for 6–12 rows
- Avoid jargon in the benefit column

---

### 4. Use Cases

Generate 3–5 role-specific use cases. Each must follow this format:

**Use Case [N]: [Role] — [Scenario Title]**
- **Who:** [Job title / role]
- **Situation:** [The specific moment or trigger that leads them to use the product]
- **Before:** [What they had to do without this product]
- **With [Product Name]:** [What they do now — concrete action]
- **Outcome:** [Measurable or tangible result]

---

## Quality Checks

- [ ] Positioning statement follows Moore format exactly
- [ ] Tagline is 10 words or fewer
- [ ] Each pillar has at least 2 proof points (or flagged assumptions)
- [ ] Every feature has a benefit — no orphaned features
- [ ] Benefits start with action verbs
- [ ] Use cases include a Before/After structure

## Anti-Patterns

- [ ] Do not write feature descriptions instead of benefits
- [ ] Do not use the same messaging across all buyer personas
- [ ] Do not create a positioning statement that could apply to any competitor
- [ ] Do not list use cases without tying them to specific job titles

## Gotchas

**Trigger conflicts:**
- This skill produces GTM assets for launch or positioning. For a competitive one-pager for sales reps, use `sales-battlecard`. For a full competitive market analysis, use `competitor-teardown`.
- If the request is for an internal executive briefing rather than external GTM assets, use `executive-update`.

**Known failure modes:**
- Proof points in messaging pillars are often vague or assumed without being labelled. Prompt: "Mark any proof point that is inferred as *(assumed — verify)*."
- Positioning statement sometimes uses generic category descriptions ("a platform that helps you..."). Prompt: "Make the product category and differentiator as specific as possible — avoid generic platform language."
- Use cases are sometimes written for the same persona with minor variations. Prompt: "Cover at least 3 different roles in the use cases — include a technical buyer, a business buyer, and an end user."

**Filipino/Asian market specifics:**
- Philippine B2B buyers respond more to outcome-based messaging than feature lists. In the messaging pillars, lead with business outcomes (cost saved, risk reduced, time saved) over technical capabilities.
- Taglines and positioning statements that work in English may not resonate in Filipino-language markets. If your target includes local government or SME segments, note that a Tagalog or Taglish version may be needed.
- Use cases for Philippine enterprise accounts should reference local business contexts — not generic Western examples. Replace "Fortune 500" or "enterprise" with references to conglomerates, telcos, BPOs, or government agencies where relevant.

## Example Trigger Phrases
- "Create a positioning statement for [product]"
- "Write a GTM plan for [feature]"
- "Give me key pillars for [product name]"
- "Build a feature and use case list for [product]"
- "We're launching [X] — help me with the messaging"
