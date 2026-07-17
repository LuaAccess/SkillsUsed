---
name: social-content
description: Write platform-native social media content — feed posts, reel/TikTok scripts, profile bios, and social-specific hooks — parameterized by platform and asset_type. Use when asked to create, draft, or optimize content for Facebook, Instagram, TikTok, LinkedIn, or Twitter/X feeds, reels, bios, or captions. Does NOT fire for web/owned-media copy such as ads, landing pages, lead magnets, or email sequences (see content-writer) — EXCEPT that LinkedIn native articles belong to content-writer despite being social-platform-hosted, because their long-form structure matches owned-media copy, not short-form social-native constraints. Does NOT fire for thumbnail/image generation (currently blocked — no image-gen tool confirmed active) or for style-cloning from a user-supplied writing-sample corpus (that would be a separate Voice Builder skill, not built — this skill uses standard tone parameters only, no corpus-based cloning).
---

# Social Content

## Purpose
One text-generation engine for social-platform-native assets, parameterized by `platform` (Facebook / Instagram / TikTok / LinkedIn / Twitter-X) and `asset_type` (post / reel script / profile bio / comment hook) — replacing four persona-labeled reskins of the identical "write short text for social" process.

## Gotchas
- **Facebook Philippines suppresses posts with raw external links in the caption body.** If a post includes a URL directly in the caption text (e.g., "Click here: https://..."), FB's PH algorithm materially reduces reach. Route CTAs to "link in bio," comments, or a Messenger prompt instead — this is a structural output rule, not a stylistic preference, and must be enforced in every FB post draft.
- **Reel/TikTok hooks in PH markets often autoplay silently for the first ~1.5 seconds.** A hook that relies purely on spoken audio with no visual/text reinforcement risks catastrophic early drop-off. Reel scripts must be structured so the hook is comprehensible from on-screen text or visual framing alone, independent of sound.
- **Hashtag conventions diverge sharply by platform — do not apply one heuristic across all of them.** Instagram tolerates a higher hashtag count with less penalty; TikTok's algorithm has historically treated heavy hashtag stuffing as a lower-quality signal and suppressed reach accordingly. Because platform algorithm behavior shifts without notice, this skill should default to a conservative hashtag count on TikTok and flag to the user that current platform behavior should be spot-checked rather than relying on a fixed historical rule.
- **This skill cannot independently determine if a client is regulated.** Same rule as `content-writer`: don't assume based on client name. Ask directly when ambiguous, or check a HubSpot CRM regulatory-status field if one exists.
- **Financial claims in social captions carry the same liability weight as ad copy, even though the format feels casual.** A caption like "earn X% returns" is a compliance issue regardless of platform informality — flag for human/compliance review before publishing if the client is regulated or the claim resembles a performance guarantee.

## Workflow
1. Identify `platform` and `asset_type`.
2. Confirm language directive (EN / Filipino / Taglish) and tone.
3. Confirm regulatory status of the client per the Gotchas rule — ask if unclear.
4. Load platform-specific structural constraints (character limits, hashtag conventions, reel beat structure) before drafting — don't apply a single generic template across all platforms.
5. Draft the asset.
6. Self-check before returning: no raw URL in an FB caption body, reel hook is visually/textually comprehensible without audio, hashtag count is conservative on TikTok specifically, and any financial-claim language is flagged if regulatory status is confirmed or ambiguous.

## Output
Structured text block with the asset content plus a platform metadata block: `Suggested Hashtags`, `Format Notes` (e.g., "CTA routed to bio link per FB reach rule"), and a `Compliance Flag` if applicable. Delivered via `message_compose_v1` or as plain structured text depending on destination.

## Liability / Scope-Out
No regulatory filing weight on its own, but any financial-claim language for a regulated client must be flagged for human/compliance review before publishing, regardless of platform or format.
