# LuaAccess/SkillsUsed — Hardened IT Consulting Skills Library

Hardened fork of selected skills from [mohitagw15856/pm-claude-skills](https://github.com/mohitagw15856/pm-claude-skills), extended with IT consulting workflow skills, session management protocols, market/content skills, and personal trading systems.

**Maintained by:** LuaAccess
**Upstream:** `mohitagw15856/pm-claude-skills` (MIT License)
**Market context:** Philippines / Southeast Asia IT consulting and sales, plus personal trading and content workflows

---

## Skills Directory (`skills/`)

### Sales

| Skill | Purpose |
|---|---|
| `discovery-call-prep` | Pre-call research brief, hypothesis, question architecture |
| `proposal-writer` | Generic commercial proposals structured around client problems |
| `consulting-proposal` | IT consulting-specific proposal/SOW — RFP/RFQ response, pricing narrative, lost-deal restructuring |
| `sales-battlecard` | Generic competitive positioning and objection handling (one-pager for reps) |
| `it-consulting-battlecard` | IT consulting-specific battlecard — vs. other SIs, MSPs, tech vendors on a live bid |

### Account Management

| Skill | Purpose |
|---|---|
| `account-plan` | Strategic account planning with relationship map and 90-day actions |

### Client Intelligence & CRM

| Skill | Purpose |
|---|---|
| `meeting-intelligence` | Post-meeting debrief — hidden signals, power map, performance audit, next moves |
| `crm-hygiene` | Turns a debrief or call notes into concrete CRM updates (deal stage, contacts, tasks) |
| `client-relationship` | Reviews/acts on relationship and account health data across CRM and connected apps — deal status, portfolio health, at-risk flags |

### Client Success

| Skill | Purpose |
|---|---|
| `cs-health-scorecard` | Account health scoring with RAG status and renewal forecast |
| `renewal-playbook` | Renewal strategy, negotiation prep, objection responses, timeline |
| `qbr-deck` | Quarterly Business Review structure and talking points |
| `invoice-chase` | Overdue-invoice collection sequencing — escalating tone, timing cadence, relationship-preserving |

### Communication

| Skill | Purpose |
|---|---|
| `executive-update` | 250-word executive briefings structured for C-suite readers |
| `client-communication` | Outbound messages to clients/prospects — email, Teams, follow-up, LinkedIn — calibrated for tone and relationship stage |

### Strategy

| Skill | Purpose |
|---|---|
| `competitor-teardown` | Deep competitive analysis for strategy, product, or investor use |
| `ambiguity-resolver` | Turns vague briefs into structured problem statements |
| `go-to-market` | GTM assets: positioning statement, messaging pillars, use cases |
| `problem-solving-sequence` | Structured 5-stage sequence (Diagnose → Compare → Reframe → Create → Validate) across 20 named frameworks (Fishbone, 5 Whys, First Principles, SWOT, etc.) |

### Research

| Skill | Purpose |
|---|---|
| `user-research-guide` | User/client discovery interview guides with synthesis framework *(renamed from `discovery-interview-guide` — name collided with `discovery-call-prep`)* |

### Growth & Strategic Coaching

| Skill | Purpose |
|---|---|
| `virtual-self-ai` | Strategic thinking, decision analysis, and growth coaching for IT consulting/sales — MODE 1 (post-meeting debrief), MODE 2 (open challenge session), DAC multi-perspective panel |

### Content & Marketing

| Skill | Purpose |
|---|---|
| `content-writer` | Persuasive web/owned-media copy — ads, landing pages, lead magnets, email sequences |
| `social-content` | Platform-native social content — feed posts, reel/TikTok scripts, bios, hooks |

### Finance & Operations

| Skill | Purpose |
|---|---|
| `plan-payroll` | Payroll run planning — headcount cost modeling, statutory deduction estimates, calendar sequencing, variance flags |

### Daily Briefings

| Skill | Purpose |
|---|---|
| `morning-intel-briefing` | Daily intel briefing — global headlines, tech/cybersecurity developments, market signals, PH/SEA opportunity radar |
| `morning-work-briefing` | Daily work briefing pulled from connected apps — M365 calendar/email, HubSpot, Asana, Notion, Monday.com |

### Reference

| Skill | Purpose |
|---|---|
| `data-science-reference` | Quick-reference for data science/stats/ML/DL/LLM/GenAI concepts — formulas, decision guides, comparison tables |

### Trading Systems

| Skill | Purpose |
|---|---|
| `candlestick-price-action` | Reference library — candlestick patterns, SMC/ICT, CRT, multi-timeframe entries |
| `vwap-ema-day-trading-system` | Intraday options day-trading system — VWAP + 9 EMA, key levels, retest entries, sizing, journaling |
| `swing-position-trading-system` | Multi-day/week swing & position trading — gap risk, theta selection, catalyst entries |
| `reversal-mean-reversion-trading` | Counter-trend/mean-reversion playbook — exhaustion signals, divergence, fade setups |
| `risk-conviction-framework` | Position sizing, conviction scoring, risk-tier framework for options day/swing trades |

### Workflow & Session Management

| Skill | Purpose |
|---|---|
| `gated-phase-plan` | Phase-wise implementation plans with explicit pass/fail gate tests |
| `context-rot-protocol` | Session health management, handoff protocol, rewind procedure |
| `fresh-context-review` | Pre-execution review using a clean context to catch missed errors |
| `screenshot-debug` | Structured debug protocol using screenshots for visual/UI state capture |

---

## Skill Structure

Each skill follows this layout:

```
skills/
└── skill-name/
    └── SKILL.md        ← required: YAML frontmatter + skill body
```

Every SKILL.md contains:
- **YAML frontmatter** — `name` and `description` (triggers Claude to load the skill). **Any mutual-exclusion / "Do NOT use" logic must live in the description, not just the Gotchas section** — description + name is all Claude sees before deciding to fire a skill; exclusions buried only in the body don't prevent mis-triggering.
- **Required inputs** — what to provide for best output
- **Output structure** — the deliverable format
- **Quality checks** — pre-submit checklist
- **Anti-patterns** — what not to do
- **Gotchas** — trigger conflicts, known failure modes, Filipino/Asian market specifics

---

## Skill Routing (Mutual Exclusion)

Some skills have overlapping scope. Use this table to route correctly:

| Situation | Use this skill |
|---|---|
| New prospect, first call | `discovery-call-prep` |
| User research / problem validation interviews | `user-research-guide` |
| Write a generic commercial proposal | `proposal-writer` |
| Write an IT consulting proposal / SOW / RFP response | `consulting-proposal` |
| Quick one-page competitive cheat sheet, generic competitor | `sales-battlecard` |
| Competitive battlecard vs. an SI/MSP/tech vendor on a live IT bid | `it-consulting-battlecard` |
| Deep strategic competitive analysis | `competitor-teardown` |
| Existing customer account strategy | `account-plan` |
| Post-meeting analysis / debrief | `meeting-intelligence` |
| Update CRM after a meeting or call | `crm-hygiene` (run after `meeting-intelligence`) |
| Review account health / portfolio-wide relationship status | `client-relationship` |
| Upcoming renewal — commercial strategy | `renewal-playbook` (best after `cs-health-scorecard`) |
| Score account health first | `cs-health-scorecard` → then `renewal-playbook` |
| QBR presentation for customer | `qbr-deck` |
| Internal leadership briefing | `executive-update` |
| Outbound message to a client/prospect | `client-communication` |
| Overdue invoice / collections sequencing | `invoice-chase` |
| Product/feature launch positioning (not competitor-specific) | `go-to-market` |
| Vague brief needs structuring | `ambiguity-resolver` |
| Structured multi-framework problem-solving | `problem-solving-sequence` |
| Post-meeting strategic challenge / growth coaching / DAC panel | `virtual-self-ai` |
| Ad copy, landing page, lead magnet, email sequence | `content-writer` |
| Platform-native social post/script/bio | `social-content` |
| Payroll budget/cost modeling | `plan-payroll` |
| Daily world/tech/security intel scan | `morning-intel-briefing` |
| Daily pull from calendar/email/CRM/tasks | `morning-work-briefing` |
| Data science/ML/stats concept lookup | `data-science-reference` |
| Chart pattern / SMC / price action ID | `candlestick-price-action` |
| Intraday options trade plan | `vwap-ema-day-trading-system` |
| Multi-day/week swing or position trade plan | `swing-position-trading-system` |
| Fading a move / counter-trend setup | `reversal-mean-reversion-trading` |
| Position sizing / conviction scoring on a trade idea | `risk-conviction-framework` |
| Planning a multi-step build | `gated-phase-plan` |
| Session running long / picking up from previous session | `context-rot-protocol` |
| Review a plan before executing | `fresh-context-review` |
| Stuck and need visual/UI debugging (screenshot) | `screenshot-debug` |
| Code error, stack trace, backend logic bug (no visual component) | `engineering:debug` (built-in plugin, not in this repo) |

**⚠ Known unresolved collisions** — both skills in each pair currently share triggering phrases in their SKILL.md `description` field. This table documents intended routing, but it does not change what Claude actually sees when deciding which skill to fire — only editing the `description` fields themselves (adding "Do NOT use for X — use Y instead," as already done for `discovery-call-prep`/`user-research-guide`) will fully resolve it:
- `proposal-writer` vs. `consulting-proposal` — both currently fire on "write a proposal" / "draft an SOW"
- `sales-battlecard` vs. `it-consulting-battlecard` — both currently fire on "build a battlecard"

---

## Chained workflows

Some skills are designed to run in sequence rather than standalone:

```
meeting-intelligence → crm-hygiene → renewal-playbook / proposal-writer / consulting-proposal / account-plan
cs-health-scorecard → renewal-playbook
gated-phase-plan → fresh-context-review → (execute) → screenshot-debug (if stuck)
client-relationship → renewal-playbook / invoice-chase (if at-risk or past-due surfaced)
```

---

## Security Hardening Applied

- **GitHub Actions SHA-pinned** — no mutable tag references
- **Dependabot enabled** — weekly GitHub Actions updates
- **Full prompt injection scan** — all SKILL.md files audited, no malicious instructions found
- **No external URL calls** — all skills are pure markdown instruction sets
- **No hardcoded credentials** — confirmed clean
- **All files under 200 lines** — per hardening standard
- **Clean YAML frontmatter** — line 1 verified as `---` on all files

See [SECURITY.md](SECURITY.md) for full policy and verification commands.

---

## Verification

After any upload, verify a skill file is clean:

```bash
# Frontmatter check (must return ---)
curl -s https://raw.githubusercontent.com/LuaAccess/SkillsUsed/main/skills/<skill>/SKILL.md | head -1

# Existence check (must return 200)
curl -s -o /dev/null -w "%{http_code}" https://raw.githubusercontent.com/LuaAccess/SkillsUsed/main/skills/<skill>/SKILL.md

# Line count (must be under 200)
curl -s https://raw.githubusercontent.com/LuaAccess/SkillsUsed/main/skills/<skill>/SKILL.md | wc -l
```
