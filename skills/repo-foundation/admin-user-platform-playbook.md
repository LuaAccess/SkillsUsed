# Admin-Controlled Multi-User Platform — Architecture Pattern & Build Playbook

> **How to use this doc:** This is a reference/template, not an invocable
> skill — there's no trigger phrase, no auto-loading. Paste the relevant
> section(s) into a new Claude session at the start of a project that fits
> the pattern below, or just read it yourself before scaffolding. Treat §12
> (pitfalls actually hit) and §16 (starting checklist) as the two sections
> worth re-reading every time, even if you skim the rest.

Extracted from `LuaAccess/spmatrix`. This isn't a description of that one
project — it's the reusable *pattern* underneath it, generalized so it can
be the starting point for the next platform that needs "an admin who
controls exactly what each user can see/do, and full visibility into what
they did with it." Salary calculators, exam platforms, client portals,
internal tools — the shape repeats.

---

## 1. When this pattern fits

Reach for this whenever a project has **two audiences with an asymmetric
trust relationship**:

- One side (admin) needs to create accounts, control what each account can
  do, see everything that happened, and revoke access instantly.
- The other side (user) needs a locked-down, single-purpose interface that
  only exposes what the admin allowed — and must never be able to see the
  underlying logic, other users' data, or manipulate their own permissions.

Signals it's the right fit: "admin should be able to control what the user
sees," "track what users are doing," "different users should have different
access," "time-limited access," "the user shouldn't see the formula/code."

---

## 2. Core design principles

These are the decisions that mattered most, in priority order:

1. **Server-side enforcement, never client-side hiding.** Every permission
   check happens again on the server, on every request, reading from the
   database — never trusting a client-sent flag. Hiding a button in JS is
   UX, not security. If the core logic (a formula, a proprietary algorithm)
   must be protected from the user, it never ships to the client at all —
   the client sends raw inputs, the server computes, and returns only the
   fields the admin has whitelisted.

2. **Permissions are data, not code branches.** A JSON column
   (`allowed_features`, `allowed_downloads`) holds the toggles. Adding a new
   feature flag means adding a JSON key and a checkbox — not an `if`
   scattered across five files. This is the single highest-leverage decision
   in the whole pattern; everything else builds on it.

3. **Two independent access controls, both re-checked every request.**
   *Duration* (subscription-style: expires after N days/weeks/months) and
   *window* (time-of-day / day-of-week restriction) are separate concerns.
   Neither is checked only at login — both re-run on every authenticated
   request, so an admin action (terminate, narrow the window) takes effect
   on the user's very next request, not whenever their session happens to end.

4. **Admin and user are fully separate identity systems.** Separate tables,
   separate session flags (`session.adminId` vs `session.userId`).
   Compromising one can never escalate into the other.

5. **Every meaningful action gets logged**, tied to who, when, from where,
   and (for downloads/computes) with enough structured detail to reconstruct
   what happened — without over-storing sensitive derived data outside what's
   operationally necessary.

6. **The schema heals itself on every boot**, not just at build time. This
   sounds like a small thing until a host runs `npm install` without your
   migration step and the app 500s on a fresh deploy. See §11.

7. **Admin sees more detail than the user, by design, for the same
   underlying data.** Not two data models — one result, exported at
   different detail levels depending on who's asking. See §10.

---

## 3. Directory structure template

```
project/
├── README.md / ARCHITECTURE.md / DECISIONS.md / CHECKLIST.md
├── render.yaml (or equivalent deploy config)
├── .gitignore
├── package.json
├── docs/
│   ├── security.md, deployment.md, database.md, monitoring.md
│   └── admin/, user/  — role-specific quick-starts
├── config/
│   └── index.js               — one place for all env-driven config
├── middleware/
│   ├── auth.js                — requireAdmin / requireUser
│   ├── accessExpiry.js        — subscription-duration check, every request
│   ├── accessWindow.js        — time-of-day/weekday check, every request
│   ├── featureGate.js         — loads + exposes permission flags per request
│   ├── activityLogger.js      — logActivity() helper
│   └── security.js            — helmet, rate limiters, CSRF
├── shared/
│   └── <core-logic>.js        — the protected formula/algorithm, framework-agnostic,
│                                 unit-testable alone, NEVER required by client code
├── storage/
│   ├── databases/, exports/, backups/  — persistent-disk-backed, gitignored
├── services/
│   └── platform/
│       ├── server.js, db.js, schema.js, bootstrap.js
│       ├── routes/       — thin, just wiring
│       ├── controllers/  — request/response glue
│       ├── services/     — business logic (userService, inviteService,
│       │                   activityService, backupService, restoreService,
│       │                   exportService)
│       ├── utils/         — password.js, time.js
│       └── public/
│           ├── admin/    — plain HTML/CSS/JS admin dashboard
│           └── user/     — plain HTML/CSS/JS locked-down user interface
└── scripts/
    ├── migrate.js, backup.js, cleanup.js
```

---

## 4. Database schema template

Five tables cover almost every version of this pattern:

```sql
admins (
  id, username UNIQUE, password_hash,
  failed_attempts, locked_until           -- lockout, see §5
)

users (
  id, username UNIQUE, password_hash, full_name, status,  -- active|suspended|terminated
  access_start_at, access_expires_at, access_duration_type, access_duration_value,
  allowed_features TEXT DEFAULT '{}',      -- JSON: the permission-gating pattern, §6
  allowed_downloads TEXT DEFAULT '{}',
  access_days TEXT DEFAULT '[...]',        -- JSON array: weekday restriction
  access_start_time, access_end_time,      -- time-of-day restriction
  timezone,
  created_by_admin_id, terminated_at,
  failed_attempts, locked_until,
  last_single_result, last_single_meta, last_single_computed_at,  -- §10
  last_batch_result, last_batch_computed_at
)

invite_links (
  id, token UNIQUE, user_id, created_by_admin_id,
  expires_at, used_at, revoked             -- single-use pattern, §8
)

sessions_log (
  id, user_id, login_at, logout_at, ip_address, user_agent,
  location_city, location_country, location_status  -- 'unresolved' until a geo provider is wired
)

activity_log (
  id, user_id, session_id, action_type, detail, ip_address, created_at
)
```

Design notes worth carrying forward:
- `allowed_features` / `allowed_downloads` as JSON, not normalized columns —
  new toggles need zero migrations.
- `access_expires_at` is **precomputed** at create/update time, not derived
  at read time — every query that checks expiry is a plain string
  comparison, no date math repeated per-request.
- `sessions_log.location_*` defaults to `'unresolved'` — don't let a
  half-built geolocation feature silently look like it's working when no
  provider key is configured. Say so explicitly in the data.

---

## 5. Security checklist

- [ ] Passwords: bcrypt, 10-12+ rounds, **minimum-strength policy enforced
  server-side** (length + not-all-digit at minimum) — don't just discourage
  weak passwords, reject them. `"111"` should be a 400, not a warning.
- [ ] A random-password generator in the admin UI (`crypto.getRandomValues`),
  so nobody has to think one up.
- [ ] Account lockout after N failed attempts, both admin and user, independently.
- [ ] Session cookies: `httpOnly`, `sameSite: strict`, `secure` in production.
- [ ] CSRF: double-submit cookie pattern. Frontend fetches a token before any
  state-changing request; state-changing multipart uploads still need the
  token as a header (can't rely on body parsing before multer runs).
- [ ] Rate limiting: tighter on login endpoints than general API traffic.
- [ ] `helmet` with a real CSP, not the defaults left wide open.
- [ ] Invite tokens (`nanoid(32)` or equivalent) are **never derived from or
  related to** anything else — not the password, not the user id, not
  anything guessable. Verify this explicitly if anyone raises the concern;
  don't just assert it.

---

## 6. The permission-gating pattern, precisely

```js
// middleware/featureGate.js
function loadPermissions(req, res, next) {
  req.allowedFeatures = JSON.parse(req.currentUser.allowed_features);
  req.allowedDownloads = JSON.parse(req.currentUser.allowed_downloads);
  next();
}
```

Every downstream controller reads `req.allowedFeatures`, never
`req.body.someFlag`. The client-side UI reads the *same* permission object
(fetched from `GET /api/user/permissions`) purely to decide what to render —
that's UX, and it's allowed to be wrong or stale for a few seconds; the
server-side check is what's actually load-bearing and is never stale beyond
the current request.

**Default semantics matter and must be consistent everywhere a feature is
checked.** Decide per-feature whether "not set" means on or off, and apply
that same rule in every function that reads it — a feature that defaults ON
in one function and OFF (because it checked for `undefined` differently) in
another is a subtle, hard-to-spot bug class. Write the default check once,
as a named function, and reuse it.

**Live permission updates without re-login:** if the user-facing page stays
open across an admin's change, poll `GET /.../permissions` every ~10s and
re-apply the same "which UI elements show" logic used at login. Otherwise
"admin changed a setting" and "user's screen reflects it" can be minutes or
hours apart depending on session length — worth fixing proactively rather
than waiting for someone to report it as a bug.

---

## 7. Access control pattern

Duration and window are orthogonal and both belong in middleware that runs
on **every** authenticated request:

```js
// Runs first — is the account even still valid at all?
enforceAccessExpiry   // status !== active/suspended/terminated, access_expires_at

// Runs second — is *right now* an allowed time to use it?
enforceAccessWindow    // access_days, access_start_time/end_time, in the user's own timezone
```

Evaluate the time window in the **user's configured timezone**, not server
time — if this platform ever has users outside one timezone, server-time
checks will be wrong for some of them silently.

---

## 8. Invite-link / passwordless-handoff pattern

- Admin-generated, single-use, short expiry (default 24h, configurable).
- Generating a new link for a user **revokes any previous unused link** for
  that same user — only the newest admin-issued link is ever valid.
- Consuming a link establishes a session exactly like a password login would.
- **Get the route prefix right the first time.** This bit us: the route was
  registered under `/api/auth/login/invite/:token` but the link-generation
  code built the URL without the `/api/auth` prefix, so every generated
  link 404'd. Write a small integration test (or at minimum, a curl check)
  that actually *follows* a generated link end-to-end before calling this
  feature done — don't just check that link generation returns 200.

---

## 9. Backup & restore pattern

- **Never `fs.copyFile` a live database file in WAL mode.** It can produce
  an inconsistent snapshot if a write is in-flight. Use the driver's proper
  online-backup API (`better-sqlite3`'s `.backup()`, or the equivalent for
  whatever engine — Postgres has `pg_dump`, etc.) — safe to call while the
  app keeps serving traffic.
- Expose backup as **both** a CLI script and an admin-dashboard button. The
  dashboard button matters most for teams without shell/SSH access to
  their host (Render, most PaaS) — "admin can trigger a backup" only
  actually helps if it doesn't require a terminal.
- **Restore is genuinely dangerous — build the safety net in, don't bolt it
  on:**
  - Validate the uploaded file actually has the expected schema before
    touching anything live.
  - Take a fresh backup of *current* data automatically, immediately before
    restoring — so a wrong-file mistake is itself recoverable the same way.
  - Restore row-by-row into the *already-open* live connection inside one
    transaction (delete children before parents, insert parents before
    children, to respect foreign keys) — don't close and swap the
    underlying file out from under an active connection.
  - Require an explicit typed confirmation (not just a click) before a
    destructive action like this fires.
  - **Destroy the current session after restoring.** The restored data may
    reference a different admin account (different id, different
    credentials) than the one currently logged in — force a fresh login
    rather than continuing on a session that might now be stale or, worse,
    valid for the wrong account.
  - Test this by actually wiping the live data and restoring from a backup
    taken beforehand — don't just review the restore code. The row-order/
    foreign-key logic is exactly the kind of thing that looks right and
    isn't.

---

## 10. Detail-level export pattern

When admin needs the full derivation (audit, HR review, debugging) but the
end user should only see the outcome (protects the underlying logic, avoids
overwhelming a non-technical user with intermediate math):

- One export function, parameterized by a `detailLevel` (`'summary'` |
  `'full'`), not two separate export functions that will drift apart over
  time.
- User-facing download endpoints always request `'summary'`.
- A **separate admin-only endpoint**, scoped to a specific user's most
  recent result, always requests `'full'`.
- This requires **persisting** the last computed result somewhere durable
  (a DB column, not just the requesting user's session) — otherwise admin
  has no way to retrieve a specific user's result independent of whether
  that user's session is even still active.
- Batch/tabular exports need the header row and any error-row `colspan`
  computed dynamically from the same `detailLevel`, or you'll get column-count
  mismatches between the "all fields" and "fewer fields" versions.

---

## 11. Self-healing schema pattern

```js
// db.js — applied on EVERY connection open, not just at build/deploy time
require('./schema').applySchema(db);
```

```js
// schema.js
const SCHEMA_SQL = `CREATE TABLE IF NOT EXISTS ... ;`; // idempotent by construction

function applySchema(db) {
  db.exec(SCHEMA_SQL);
  ensureColumn(db, 'users', 'new_column', 'TEXT'); // see below
}

// ALTER TABLE ADD COLUMN is NOT idempotent in SQLite — guard it
function ensureColumn(db, table, column, definition) {
  const cols = db.prepare(`PRAGMA table_info(${table})`).all();
  if (!cols.some((c) => c.name === column)) {
    db.exec(`ALTER TABLE ${table} ADD COLUMN ${column} ${definition}`);
  }
}
```

**Why this matters more than it seems:** a PaaS host's dashboard can be
configured to run a bare `npm install` as the build command instead of
`npm install && npm run migrate` — invisibly, without anyone noticing,
especially if the service was created by clicking "New Web Service" instead
of going through a Blueprint/IaC flow that actually reads your deploy
config file. This happened twice in this build before the schema was made
self-applying. Don't rely on a separate migration step ever actually
running — make correctness independent of it.

---

## 12. Known pitfalls actually hit in this build (worth scanning before you repeat them)

| Bug | Root cause | Fix |
|---|---|---|
| `SqliteError: no such table` on fresh deploy | Host ran `npm install` only, skipped the migrate step | Self-healing schema (§11) |
| Every generated invite link 404'd | Link built without the router's mount prefix | Follow the link end-to-end in a test, not just check link generation returns 200 |
| `finalApprovedPct` silently became `null` | `Number(undefined)` is `NaN`, and `typeof NaN === 'number'` — a "was a value provided" check based on `typeof` was fooled | Check "was it provided" via string/undefined check *before* converting with `Number()`, not by inspecting `typeof` after |
| Backup could theoretically corrupt under load | Raw `fs.copyFile` on a live WAL-mode SQLite file | Use the driver's online-backup API |
| Admin-set permission changes didn't reach an already-open user tab | Permissions fetched once at login, never re-fetched | Poll periodically, re-apply the same render logic used at login |
| Batch export column count broke when a column was conditionally hidden | Error rows used a fixed `colspan` that didn't match the varying header length | Compute header AND colspan together, from the same condition, every time |

---

## 13. Tech stack (opinionated, for consistency across projects)

Express (ESM or CJS, pick one and stay consistent across your projects) +
`better-sqlite3` (or your team's preferred embedded/managed DB) + `bcrypt` +
`express-session` (+ a session store backed by the same DB, so there's no
second piece of infra to operate) + `csurf` (or an actively-maintained
successor if it's deprecated by the time you read this — check first) +
`helmet` + `express-rate-limit` + `multer` for uploads + `exceljs`/`pdfkit`
for exports + `nanoid` for tokens. No ORM — plain prepared statements, every
query grep-able.

---

## 14. Deployment gotchas (Render-specific, but the principle generalizes)

- **A deploy config file (`render.yaml`, `Procfile`, etc.) is only read if
  the service was created through the platform's actual "read this config"
  flow** (Render: Blueprint). A manually-created service uses whatever build
  command is in the dashboard, silently ignoring your file. Confirm which
  flow was used before debugging why a build command "isn't working."
- Persistent storage paths (`DB_DIR`, `EXPORTS_DIR`, `BACKUPS_DIR`) must
  point at an actually-mounted persistent disk, never inside the source
  tree — source-tree paths get wiped on every deploy. This is the single
  most common way "my data disappeared after an update" happens, and it's
  worth checking directly in the dashboard, not just trusting a
  config file that says the right thing.
- Pin the runtime version (`NODE_VERSION` / `.node-version`) if any
  dependency ships native bindings (`better-sqlite3`, `bcrypt`) — a minor
  runtime version bump can break the native build on the next deploy.

---

## 15. Requirement → Pattern → Files, quick reference

| If the requirement is... | ...use this pattern | ...in these files |
|---|---|---|
| "Admin controls what each user can do" | JSON permission columns, §6 | `middleware/featureGate.js`, `services/userService.js` |
| "Time-limited access" | Duration + window, both re-checked every request, §7 | `middleware/accessExpiry.js`, `accessWindow.js` |
| "Admin generates a login link" | Single-use, superseding invite tokens, §8 | `services/inviteService.js` |
| "See what users did" | Structured activity/session logging | `middleware/activityLogger.js`, `services/activityService.js` |
| "User shouldn't see the logic" | Formula lives server-only; client sends inputs, gets only whitelisted outputs | `shared/<core-logic>.js` |
| "Admin needs more detail than the user" | Parameterized export detail level + persisted last-result, §10 | `services/exportService.js`, DB columns on `users` |
| "Don't lose data on deploy" | Self-healing schema, §11; persistent disk, §14 | `services/platform/schema.js`, `db.js` |
| "Admin needs to back up / recover data" | Online-backup API, dashboard-triggered, row-level restore, §9 | `services/backupService.js`, `restoreService.js` |

---

## 16. Starting checklist for a new project using this pattern

- [ ] Define the two tables that matter most first: `admins`, `users` — get
  the permission JSON columns and access-control columns right before
  writing any routes.
- [ ] Write the core protected logic (`shared/`) as pure, framework-free
  functions before touching Express — unit-test it in isolation.
- [ ] Build `schema.js` with `ensureColumn()` from day one, even if there's
  only one migration so far — retrofitting this after several ALTER TABLEs
  have already happened by hand is much more annoying.
- [ ] Middleware order: auth → access expiry → access window → load
  permissions → rate limit → route handler. Get this order right once, reuse
  the composed middleware stack everywhere.
- [ ] Decide the export detail-level split (§10) before building the export
  functions, not after — retrofitting a `detailLevel` parameter into an
  already-shipped single-purpose export function is exactly the kind of
  "shouldn't have needed a rewrite" moment this playbook exists to prevent.
- [ ] Backup + restore go in before real user data accumulates, not after
  the first "we lost data" incident.
