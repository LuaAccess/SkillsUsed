---
name: content-writer
description: Write persuasive web and owned-media copy — ads, landing pages, lead magnets, and email sequences — parameterized by asset_type. Use when asked to draft ad copy, write a landing page, create a lead magnet, or write an email sequence. Does NOT fire for social media platform-native content such as feed posts, reel scripts, profile bios, or social hooks (see social-content) — EXCEPT LinkedIn native articles, which belong here despite publishing in-platform, because their long-form headline/body/CTA structure matches owned-media copy, not social-native constraints. Does NOT fire for SEO technical audits or ranking diagnostics (see brightdata-plugin:seo-audit) or for raw customer insight synthesis from interviews/tickets/surveys (see design:research-synthesis or product-management:synthesize-research) — this skill consumes those insights to produce copy, it does not generate them.
---

# Content Writer

## Purpose
One text-generation engine for web/owned-media copy, parameterized by `asset_type` (ad / landing page / lead magnet / email sequence / LinkedIn article) — replacing what would otherwise be four separate persona-labeled skills doing the identical "write persuasive short text" process.

## Gotchas
- **Regulated-client disclaimers are not evergreen text — don't hardcode wording.** If the client is in a BSP-regulated financial vertical, promotional copy may require specific disclaimer language (e.g., investment risk disclosures). This skill does NOT cache or emit specific disclaimer wording, because regulatory language changes and requires legal sign-off per instance. Instead: flag "regulated-client disclaimer required — confirm current required wording with compliance/legal before this copy is published," every time regulated status is confirmed or ambiguous.
- **This skill cannot independently determine if a client is regulated.** Don't assume based on client name. Either (a) ask the user directly when it's ambiguous, or (b) if a HubSpot CRM record for the client has a regulatory-status field populated, use that. Never silently proceed as "not regulated" by default when status is unconfirmed.
- **SEA market tone mismatch is a real risk, not a styling nitpick.** Aggressive Western-style urgency ("BUY NOW," hard countdown pressure) tends to underperform relative to value-first or social-proof framing in Philippine digital advertising. Treat this as a default tone adjustment, not an optional flourish — but don't hardcode a specific engagement-lift percentage, since that number isn't independently verified here.
- **Language mismatch suppresses PH B2B conversion — direction is real, magnitude isn't quantified here.** For PH B2B lead magnets, single-English-only copy can measurably underperform vs. Taglish or dual-language treatment for SME-owner or procurement-decision-maker segments. State the mechanism when relevant; don't invent a specific percentage drop unless the user supplies their own campaign data.
- **Claims that could read as investment advice, not just product promotion, are out of scope.** If output edges from "this product exists and here's why it's useful" into implied guaranteed-return or performance-prediction language, stop and flag for mandatory human/licensed-advisor review before use.

## Workflow
1. Identify `asset_type` (ad / landing page / lead magnet / email sequence / LinkedIn article) and where the output will live.
2. Confirm target audience segment and language directive (EN / Filipino / Taglish).
3. Confirm regulatory status of the client per the Gotchas rule above — ask directly if unclear, don't assume.
4. If regulated: flag the disclaimer requirement explicitly in the output; do not write disclaimer text yourself.
5. Draft: headline → body → CTA structure, tone-adjusted for SEA market defaults unless the user specifies otherwise.
6. Self-check before returning: word count fits the stated placement, disclaimer flag present if regulated, no unverified guaranteed-return or performance-prediction language.

## Output
Structured text block with labeled sections: `Headline`, `Body`, `CTA`, and `Compliance Flag` (present only if regulated-client status was confirmed or left ambiguous). Delivered via `message_compose_v1` when the deliverable is a message/email, or as plain structured text for ad/landing/lead-magnet copy.

## Liability / Scope-Out
Does not replace a licensed financial advisor or compliance/legal reviewer for regulated-client copy. Any output bordering on investment advice must be flagged for mandatory human review before publication, regardless of how the request was framed.
