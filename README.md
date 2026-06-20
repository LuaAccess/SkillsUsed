[README.md](https://github.com/user-attachments/files/29154843/README.md)
# Identified skills (LuaAccess hardened fork)

Hardened fork of selected skills from [mohitagw15856/pm-claude-skills](https://github.com/mohitagw15856/pm-claude-skills).

## Skills Included

| Skill | Category | Purpose |
|---|---|---|
| `discovery-call-prep` | Sales | Pre-call research brief, hypothesis, question architecture |
| `proposal-writer` | Sales | Commercial proposals structured around client problems |
| `sales-battlecard` | Sales | Competitive positioning and objection handling |
| `account-plan` | Account Management | Strategic account planning with relationship map |
| `cs-health-scorecard` | Client Success | Account health scoring with RAG status |
| `renewal-playbook` | Client Success | Renewal strategy, timeline, and objection responses |
| `qbr-deck` | Client Success | Quarterly Business Review structure and talking points |
| `executive-update` | Communication | 250-word executive briefings |
| `competitor-teardown` | Strategy | Structured competitive analysis |
| `ambiguity-resolver` | Strategy | Turns vague briefs into structured problem statements |
| `go-to-market` | Strategy | GTM assets: positioning, pillars, use cases |
| `discovery-interview-guide` | Research | User/client discovery interview guides |

## Security Hardening Applied

- **GitHub Actions SHA-pinned** — no mutable tag references
- **Dependabot enabled** — weekly GitHub Actions updates
- **`health_score.py` hardened** — added path traversal protection, `.json`-only file validation, 1MB file size cap
- **Full prompt injection scan** — all SKILL.md files audited, no malicious instructions found
- **No external URL calls** — all skills are pure markdown instruction sets with no network dependencies
- **No hardcoded credentials** — confirmed clean

## Source

Upstream: `mohitagw15856/pm-claude-skills` (MIT License)
Hardened by: LuaAccess
