# Security Policy

## Repository: LuaAccess/SkillsUsed

Hardened fork of `mohitagw15856/pm-claude-skills` (MIT License).  
Maintained by: LuaAccess

---

## Hardening Standards Applied

### Supply Chain
- GitHub Actions are SHA-pinned — no mutable tag references (e.g. `@v3`)
- Dependabot enabled — weekly GitHub Actions dependency updates
- All upstream identity fields (author, plugin name, repo URL) updated to LuaAccess before use
- No third-party scripts or external dependencies introduced

### Credential & Data Safety
- No hardcoded credentials anywhere in this repository
- No API keys, tokens, secrets, or environment variables in any SKILL.md file
- No external URL calls — all skills are pure markdown instruction sets with no network dependencies

### Content Safety
- Full prompt injection scan applied to all SKILL.md files — no malicious instructions found
- No skill instructs Claude to exfiltrate data, call external services, or bypass safety guidelines
- Skills are read-only instruction sets — they do not execute code or make network requests

### File Integrity
- All SKILL.md files verified: line 1 must be `---` (clean YAML frontmatter, no upload artifacts)
- All skill files under 200 lines per hardening standard
- `health_score.py` hardened: path traversal protection, `.json`-only file validation, 1MB file size cap

---

## Supported Versions

This repository does not use versioned releases. All skills on the `main` branch are considered current and maintained.

---

## Reporting a Vulnerability

If you discover a security issue in this repository — including prompt injection, credential exposure, or supply chain risk — please report it via:

**GitHub:** Open a private security advisory at `https://github.com/LuaAccess/SkillsUsed/security/advisories/new`

Do not open a public issue for security vulnerabilities.

Expected response time: within 7 days.

---

## Out of Scope

- Vulnerabilities in the upstream `mohitagw15856/pm-claude-skills` repository — report those to the upstream maintainer
- Claude.ai platform vulnerabilities — report those to Anthropic at `https://www.anthropic.com/security`
- General questions about how skills work — open a regular issue

---

## Verification Commands

To verify the integrity of any skill file after upload:

```bash
# Check clean frontmatter (line 1 must be ---)
curl -s https://raw.githubusercontent.com/LuaAccess/SkillsUsed/main/skills/<skill-name>/SKILL.md | head -1

# Check file exists and returns 200
curl -s -o /dev/null -w "%{http_code}" https://raw.githubusercontent.com/LuaAccess/SkillsUsed/main/skills/<skill-name>/SKILL.md

# Check line count (must be under 200)
curl -s https://raw.githubusercontent.com/LuaAccess/SkillsUsed/main/skills/<skill-name>/SKILL.md | wc -l
```
