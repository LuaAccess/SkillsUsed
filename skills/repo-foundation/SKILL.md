[SKILL.md](https://github.com/user-attachments/files/30750422/SKILL.md)
---
name: repo-foundation
description: "Scaffold a new full-stack platform repository from a standards-based template — architecture doc, security/deployment/database standards, pre-launch checklist, and a decisions log. Use when starting a new platform, repo, or project from scratch, when the user says 'new platform', 'scaffold a new repo', 'set up a new project', 'start a new LuaAccess build', or 'I need a foundation for this'. Bakes in hard-won Render/Node/SQLite lessons (persistent disk paths, Node version pinning, double-quote string safety) so new projects don't repeat known failure modes. Do NOT use for adding a feature to an existing repo (Basestation or the assessment platform) — this is for net-new project setup only."
---

# Repo Foundation Skill

Scaffolds a new platform repository the same way every time, with your accumulated standards baked in from the start rather than bolted on after the first production incident.

## When to use this vs. not

- **Use for:** a brand-new platform/repo that doesn't exist yet — a third LuaAccess product, a client project, a personal tool.
- **Do NOT use for:** Basestation or the assessment platform — those already exist. Adding a feature to either is a normal edit, not a scaffold.
- If the user is vague about scope ("I need this designed"), confirm project name and one-line purpose before generating anything — don't scaffold blind.

## What gets created

Run `scripts/scaffold.py` (see below) to copy `assets/foundation-template/` into a new project directory with these pieces:

```
<project-name>/
├── README.md              — project overview stub
├── ARCHITECTURE.md         — purpose, components, data flow, deploy target
├── DECISIONS.md            — running log of "why we chose X over Y"
├── CHECKLIST.md            — pre-launch gate checklist
├── render.yaml             — Render blueprint with persistent disk pre-declared
├── .gitignore
└── Standards/
    ├── security.md         — auth, rate limiting, CSRF, audit log baseline
    ├── deployment.md       — Render specifics, Node pinning, env var handling
    ├── database.md         — SQLite/better-sqlite3 conventions, persistent disk rule
    └── coding.md           — string-quoting and direct-edit safety rules
```

## Standards baked into the template (why these specific ones)

These aren't generic — they're lessons already paid for on Basestation and the assessment platform, generalized so the next project inherits them for free instead of relearning them:

- **`DB_DIR` must point to a mounted persistent disk path, never inside the source tree** — the assessment platform lost registered examinees on every deploy until this was fixed. `render.yaml` in the template pre-declares the disk so this can't be forgotten on day one.
- **Node version pinned** — required for `better-sqlite3` compatibility on Render; unpinned versions cause silent build mismatches.
- **Double-quote strings in any file likely to be hand-edited on GitHub** — single-quoted strings with apostrophes caused repeated `SyntaxError` crashes on deploy when editing directly in the GitHub web UI. `Standards/coding.md` states this as a rule, not a one-off fix.
- **Security-first, not security-later** — bcrypt, rate limiting, CSRF, audit log go in `Standards/security.md` as the default baseline for any new auth-bearing platform, matching how Basestation's security layer was eventually built as a dedicated phase — except now it's phase one instead of phase three.

## Usage

```bash
python scripts/scaffold.py --name my-new-platform --target /path/to/parent/dir
```

This copies the template, replaces `{{PROJECT_NAME}}` placeholders with the given name, and prints the next manual steps (git init, GitHub repo creation, Render service setup).

## Quality checks before considering the foundation "done"

- [ ] `ARCHITECTURE.md` actually describes this project, not left as placeholder text
- [ ] `render.yaml` disk path is confirmed correct for this project's `DB_DIR` equivalent (if it uses SQLite)
- [ ] Node version in `render.yaml` matches what the chosen DB driver (if any) requires
- [ ] `DECISIONS.md` has at least one real entry before first deploy — don't let it sit empty
- [ ] `CHECKLIST.md` reviewed line-by-line before first production deploy, not skimmed

## Anti-patterns

- Don't scaffold and then ignore `Standards/` — the point is that new code follows these by default, not that they exist as unread files.
- Don't copy the template for a project that isn't repo-based (e.g., a one-off script or a static export) — this skill assumes an ongoing, deployed, versioned platform.
- Don't skip `DECISIONS.md` because "it's obvious right now" — it stops being obvious in six months, which is the entire point of the file.

## Gotchas

- If the new project won't use SQLite at all, `Standards/database.md` and the disk declaration in `render.yaml` still apply generically to *any* persistent-state requirement — swap "SQLite" for whatever the real datastore is, don't delete the file.
- If deploying somewhere other than Render (per Basestation's provider-agnostic goal), `Standards/deployment.md` and `render.yaml` need a parallel file for that provider — the standards concept transfers, the specific file doesn't.
