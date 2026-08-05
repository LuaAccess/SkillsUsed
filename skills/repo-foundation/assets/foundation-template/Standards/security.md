# Security Standards — {{PROJECT_NAME}}

Baseline for any platform with auth or user data. Not optional add-ons — build these in from the start, not after a phase-3 hardening pass.

## Authentication
- Passwords: bcrypt, never plaintext or a weak/fast hash
- Account lockout after repeated failed attempts
- Session-based auth with secure, httpOnly cookies

## Request protection
- `helmet` (or equivalent) for standard HTTP security headers
- Rate limiting (`express-rate-limit` or equivalent) on all public endpoints, tighter on auth endpoints specifically
- CSRF protection via double-submit cookie pattern (or framework equivalent) on all state-changing requests

## Audit
- Log sensitive actions (auth events, admin actions, data exports) with timestamp + actor
- Audit log itself should be append-only or otherwise tamper-resistant

## Credential hygiene
- Never paste real credentials into a chat session, commit message, or code comment
- If a real credential is ever exposed in plaintext (chat, terminal output, commit), rotate it — don't assume it's fine because "it's private"

## Common mistakes to avoid
- Adding security "later" once the feature works — it becomes a rewrite, not an addition
- Rate limiting only the login endpoint and forgetting registration/password-reset (equally abusable)
