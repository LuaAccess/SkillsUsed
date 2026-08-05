# Database Standards — {{PROJECT_NAME}}

Written for SQLite/`better-sqlite3` (current default) — if using something else, keep the persistence rule, adapt the rest.

## The one rule that matters most
`DB_DIR` (or equivalent data path) must point to a mounted persistent disk path — e.g. `/var/{{PROJECT_NAME}}-data` — and never anywhere inside the project's source tree.

This was learned the expensive way: the assessment platform lost all registered examinees on every deploy because its data path was inside the source tree, which Render wipes and replaces on each deploy. Don't repeat this.

## Driver compatibility
- `better-sqlite3` (or other native modules) require the Node version to be pinned — see `Standards/deployment.md`
- Test a fresh deploy (not just local dev) before trusting that persistence works — local dev never exercises the "source tree gets wiped" failure mode

## Backup
- Have a backup/restore procedure before there's real user data to lose, not after
- If the free tier doesn't support persistent disks for this project, evaluate an external option (e.g. Turso for SQLite-compatible external hosting) before launch, not after data loss
