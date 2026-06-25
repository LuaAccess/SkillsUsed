# LuaAccess/SkillsUsed — Hardened IT Consulting Skills Library

Hardened fork of selected skills from [mohitagw15856/pm-claude-skills](https://github.com/mohitagw15856/pm-claude-skills), extended with IT consulting workflow skills and session management protocols.

**Maintained by:** LuaAccess  
**Upstream:** `mohitagw15856/pm-claude-skills` (MIT License)  
**Market context:** Philippines / Southeast Asia IT consulting and sales

---

## Skills Directory (`skills/`)

### Sales

| Skill | Purpose |
|---|---|
| `discovery-call-prep` | Pre-call research brief, hypothesis, question architecture |
| `proposal-writer` | Commercial proposals structured around client problems |
| `sales-battlecard` | Competitive positioning and objection handling (one-pager for reps) |

### Account Management

| Skill | Purpose |
|---|---|
| `account-plan` | Strategic account planning with relationship map and 90-day actions |

### Client Success

| Skill | Purpose |
|---|---|
| `cs-health-scorecard` | Account health scoring with RAG status and renewal forecast |
| `renewal-playbook` | Renewal strategy, negotiation prep, objection responses, timeline |
| `qbr-deck` | Quarterly Business Review structure and talking points |

### Communication

| Skill | Purpose |
|---|---|
| `executive-update` | 250-word executive briefings structured for C-suite readers |

### Strategy

| Skill | Purpose |
|---|---|
| `competitor-teardown` | Deep competitive analysis for strategy, product, or investor use |
| `ambiguity-resolver` | Turns vague briefs into structured problem statements |
| `go-to-market` | GTM assets: positioning statement, messaging pillars, use cases |

### Research

| Skill | Purpose |
|---|---|
| `discovery-interview-guide` | User/client discovery interview guides with synthesis framework |

### Workflow & Session Management *(new)*

| Skill | Purpose |
|---|---|
| `gated-phase-plan` | Phase-wise implementation plans with explicit pass/fail gate tests |
| `context-rot-protocol` | Session health management, handoff protocol, rewind procedure |
| `fresh-context-review` | Pre-execution review using a clean context to catch missed errors |
| `screenshot-debug` | Structured debug protocol using screenshots for visual state capture |

---

## Skill Structure

Each skill follows this layout:

```
skills/
└── skill-name/
    └── SKILL.md        ← required: YAML frontmatter + skill body
```

Every SKILL.md contains:
- **YAML frontmatter** — `name` and `description` (triggers Claude to load the skill)
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
| User research / problem validation interviews | `discovery-interview-guide` |
| Write a commercial proposal | `proposal-writer` |
| Quick one-page competitive cheat sheet for reps | `sales-battlecard` |
| Deep strategic competitive analysis | `competitor-teardown` |
| Existing customer account strategy | `account-plan` |
| Upcoming renewal — commercial strategy | `renewal-playbook` |
| Score account health first | `cs-health-scorecard` → then `renewal-playbook` |
| QBR presentation for customer | `qbr-deck` |
| Internal leadership briefing | `executive-update` |
| Vague brief needs structuring | `ambiguity-resolver` |
| Planning a multi-step build | `gated-phase-plan` |
| Session running long / picking up from previous session | `context-rot-protocol` |
| Review a plan before executing | `fresh-context-review` |
| Stuck and need visual debugging | `screenshot-debug` |

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
