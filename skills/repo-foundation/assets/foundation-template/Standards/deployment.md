# Deployment Standards — {{PROJECT_NAME}}

Default target: Render.com. If deploying elsewhere, translate these principles — don't skip them.

## Version pinning
- Pin the runtime version explicitly (`NODE_VERSION` or equivalent) in `render.yaml`/env config
- Never leave it on "latest" — silent version bumps break native dependencies (e.g. `better-sqlite3`) without warning

## Persistent state
- Any directory that must survive a redeploy (`DB_DIR`, uploaded files, etc.) MUST be a mounted persistent disk path
- It must NOT be a path inside the source tree — the source tree is wiped and replaced on every deploy
- Declare the disk explicitly in `render.yaml` (see the `disk:` block in the template) rather than configuring it only in the dashboard, so it's version-controlled and reviewable

## Environment variables
- Document every required env var in `README.md`, not just in the Render dashboard
- Secrets go in Render's env var UI, never committed — even in a private repo

## Provider portability (if applicable)
- If this platform is meant to be provider-agnostic (see Basestation's design goal), keep provider-specific config (like `render.yaml`) separate from the app's own logic — the app shouldn't need to know which PaaS it's running on
