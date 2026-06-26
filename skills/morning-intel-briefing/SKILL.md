---
name: morning-intel-briefing
description: "Deliver a structured daily intelligence briefing covering global headlines, technology developments, cybersecurity threats, market signals, and PH/SEA opportunity radar. Use when the user says 'intel brief', 'good morning intel', 'what's happening in the world', 'daily intel', or 'news brief'. Uses Claude knowledge base for strategic analysis — not live web data. For live data delivery use the GitHub Actions RSS pipeline. Do NOT use for work task briefings — use morning-work-briefing instead."
---

# Morning Intel Briefing Skill

Delivers a structured daily intelligence briefing — strategic analysis of global developments filtered through an IT consulting / Philippine market lens. Readable in under 5 minutes.

## Trigger Phrases
- "intel brief"
- "good morning intel"
- "what's happening in the world"
- "daily intel"
- "news brief"
- "intelligence briefing"

## Important Limitation

This skill uses Claude's knowledge base (cutoff August 2025) for strategic context and frameworks. It does NOT have access to today's live headlines unless:
- The GitHub Actions RSS pipeline has delivered today's data to your Outlook/Notion
- You paste today's headlines into the chat and ask Claude to analyse them

**When live data is available:** Paste the RSS email content → say "intel brief on this" → Claude applies full analysis framework to live data.

**When no live data:** Claude delivers strategic framing, trend analysis, and opportunity radar based on known context — clearly flagged as knowledge-based, not today's news.

## Output Format

---

```
════════════════════════════════
INTEL BRIEF — [Weekday], [Date]
════════════════════════════════
⚠️ [LIVE DATA / KNOWLEDGE-BASED] — flagged clearly

🌏 GLOBAL HEADLINES (Top 5)
• [Headline] | [Region] | Risk: [L/M/H]
  → IT consulting angle: [One line]

🤖 TECH & AI (Top 3)
• [Development] | [Vendor/Country]
  → Client conversation angle: [One line]

🔐 CYBER THREATS (Top 3)
• [Threat/CVE] | Severity: [L/M/H]
  → Action: [One line — patch/monitor/brief client]

📊 MARKET SIGNALS
• USD/PHP: [Rate or direction]
• Tech sector: [Sentiment signal]
• Crypto: [Top mover direction]

🇵🇭 PH / SEA WATCH (Top 3)
• [Local development relevant to IT consulting]
  → Opportunity: [One line]

⚡ OPPORTUNITY RADAR
This week's top 3 signals you can act on:
1. [Signal] — [Why relevant] — [Suggested action]
2. [Signal] — [Why relevant] — [Suggested action]
3. [Signal] — [Why relevant] — [Suggested action]

════════════════════════════════
INTELLIGENCE SUMMARY
Geopolitical risk: [L/M/H]
Cyber threat level: [L/M/H]
PH market outlook: [1 sentence]
Top opportunity this week: [1 sentence]
════════════════════════════════
```

## Analysis Framework

For every item apply:
- **Cause:** What triggered this development
- **IT consulting angle:** How this affects your clients or your deals
- **Risk level:** Low / Medium / High — based on probability × impact
- **Action signal:** Monitor / Brief client / Pitch angle / Ignore

## PH/SEA Lens (Apply Automatically)

Every section must be filtered through:
- Does this affect PH enterprise IT budgets?
- Does this create a security conversation with a client?
- Does this open a new technology pitch angle?
- Does this affect USD/PHP and therefore deal pricing?
- Is this relevant to BPO, fintech, telco, or government sectors in PH?

## Opportunity Radar Rules

The Opportunity Radar is the most important section — it must:
- Name a specific action Luther can take this week
- Be grounded in IT consulting reality — not generic advice
- Connect a global signal to a local PH/SEA client conversation
- Never be vague ("stay informed about AI") — always specific ("pitch network security audit to fintech clients after [specific CVE] — affects [specific system type] common in PH banking sector")

## Quality Checks

- [ ] Data source clearly flagged — LIVE or KNOWLEDGE-BASED
- [ ] Every headline has an IT consulting angle
- [ ] Cyber section has a specific action (not just awareness)
- [ ] Opportunity Radar has 3 specific actionable signals
- [ ] PH/SEA lens applied to every section
- [ ] Total output under 600 words

## Anti-Patterns

- [ ] Do not present knowledge-based analysis as today's live news
- [ ] Do not fill Opportunity Radar with generic advice
- [ ] Do not skip the IT consulting angle for any headline
- [ ] Do not rate everything as High risk — calibrate honestly
- [ ] Do not include social media trends — no reliable free source

## Gotchas

**Trigger conflicts:**
- This skill is for external intelligence only. For work tasks and CRM, use `morning-work-briefing`.
- If user pastes live RSS data into chat → apply this skill's framework to that data immediately.

**Known failure modes:**
- Without live data Claude may default to known major stories rather than recent developments — always flag with "knowledge-based as of August 2025."
- Opportunity Radar is the section most likely to become generic — if output feels vague, prompt: "Make each opportunity specific to IT consulting in the Philippines — name a sector and a client conversation angle."
- Market signals without live data will be directional only (USD/PHP trending, not exact rate) — flag this explicitly.

**Live data upgrade path:**
When GitHub Actions RSS pipeline is live:
1. Pipeline runs at 6AM PHT
2. Structured RSS data arrives in Outlook
3. Forward or paste into Claude
4. Say: "intel brief on this"
5. Claude applies full analysis framework to today's live data
6. Opportunity Radar becomes grounded in actual today's headlines

**Filipino/Asian market specifics:**
- PH fintech and BPO sectors are highly sensitive to US tech regulatory changes — flag any US AI or data regulation development as a PH client conversation signal.
- ASEAN cybersecurity developments (especially Singapore MAS advisories) directly affect PH financial sector clients — always include if available.
- USD/PHP rate movements above ₱1 in either direction in a week affect IT project budgets — flag when significant.

## Example Trigger

User: "intel brief"
→ Claude delivers full briefing flagged as KNOWLEDGE-BASED
→ Ends with: "Want me to go deeper on any section? Or paste today's RSS data for a live analysis."

User: [pastes RSS email] + "intel brief on this"
→ Claude applies full framework to live data
→ Output flagged as LIVE DATA — [today's date]
