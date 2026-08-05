# Pre-Launch Checklist — {{PROJECT_NAME}}

## Security
- [ ] Auth uses bcrypt (or equivalent) — no plaintext, no weak hashing
- [ ] Rate limiting on all public-facing endpoints
- [ ] CSRF protection on state-changing requests
- [ ] Audit log for sensitive actions
- [ ] No credentials committed to the repo (check history, not just HEAD)

## Deployment
- [ ] `render.yaml` disk path (if any) is outside the source tree and persists across deploys
- [ ] Node/runtime version pinned, not left on "latest"
- [ ] Environment variables documented in README, not just set ad-hoc in the dashboard

## Database (if applicable)
- [ ] `DB_DIR` or equivalent confirmed to point at mounted persistent storage
- [ ] Backup/restore procedure exists and has been tested at least once

## Code hygiene
- [ ] String content likely to be hand-edited on GitHub uses double quotes (see `Standards/coding.md`)
- [ ] No single-quoted strings containing apostrophes in data/config files

## Before first real user
- [ ] `DECISIONS.md` has at least one entry
- [ ] `ARCHITECTURE.md` reflects what was actually built, not the original plan
