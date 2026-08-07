# Admin-Controlled Multi-User Platform — Architecture Pattern & Build Playbook (v2)

**How to use this doc:** Reference/template, not an invocable skill — no trigger phrase, no auto-loading. Paste the relevant section(s) into a new session at the start of a project that fits the pattern below, or read it yourself before scaffolding. §12 (pitfalls) and §21 (starting checklist) are the two sections worth re-reading every time, even if you skim the rest.

**What changed in v2:** The original playbook (extracted from spmatrix) covered the core admin/user split, permissions, access control, and backup/restore. A later, more mature directory structure showed several layers that weren't in v1 at all: **monitoring/anomaly detection, telemetry (client + server), analytics, an optional SEO analysis engine, and a privacy/data-minimization layer** — plus a proper `tests/` structure. This version folds those in as their own pattern sections (§12–§16) rather than bolting them onto the existing ones, so v1 users can adopt them incrementally. Everything from v1 is preserved; nothing was removed.

---

## 1. When this pattern fits

Reach for this whenever a project has two audiences with an asymmetric trust relationship:

- One side (**admin**) needs to create accounts, control what each account can do, see everything that happened, and revoke access instantly.
- The other side (**user**) needs a locked-down, single-purpose interface that only exposes what the admin allowed — and must never see the underlying logic, other users' data, or manipulate their own permissions.

Signals it's the right fit: "admin should be able to control what the user sees," "track what users are doing," "different users should have different access," "time-limited access," "the user shouldn't see the formula/code."

The extended layers (§12–§16) are a separate signal: "I need to know if something suspicious is happening," "I want to detect unusual behavior, not just log it," "I need proof of what a session actually did," "this has a public-facing surface that needs SEO/content health tracking." Not every project needs these — see §21 for how to decide.

---

## 2. Core design principles

Priority order, unchanged from v1, plus one new principle at the end:

1. **Server-side enforcement, never client-side hiding.** Every permission check happens again on the server, on every request, reading from the database — never trusting a client-sent flag. If core logic (a formula, a proprietary algorithm) must be protected, it never ships to the client — the client sends raw inputs, the server computes, and returns only whitelisted fields.
2. **Permissions are data, not code branches.** A JSON column (`allowed_features`, `allowed_downloads`) holds the toggles. Adding a feature flag means adding a JSON key and a checkbox — not an `if` scattered across five files.
3. **Two independent access controls, both re-checked every request.** Duration (subscription-style) and window (time-of-day/day-of-week) are separate concerns, neither checked only at login.
4. **Admin and user are fully separate identity systems.** Separate tables, separate session flags. Compromising one can never escalate into the other.
5. **Every meaningful action gets logged** — who, when, from where, with enough structured detail to reconstruct what happened, without over-storing sensitive derived data.
6. **The schema heals itself on every boot**, not just at build time.
7. **Admin sees more detail than the user, by design, for the same underlying data.** One result, exported at different detail levels.
8. **NEW — Observability data never gates access decisions on its own.** Telemetry, analytics, and monitoring signals (device fingerprint, dwell time, anomaly scores, risk flags) inform a human admin or feed a *review queue* — they don't automatically lock, suspend, or degrade a user's access unless a human (or an explicitly-designed, auditable rule) decided that behavior in advance. This is the same lesson as "hard lockouts became pure flagging" in practice: detection and enforcement are different systems, and conflating them turns false positives into outages.

---

## 3. Directory structure template (expanded)

```
project/
├── README.md / ARCHITECTURE.md / DECISIONS.md / CHECKLIST.md
├── render.yaml (or equivalent deploy config)
├── .gitignore
├── package.json
│
├── docs/
│   ├── security.md, deployment.md, database.md, monitoring.md
│   ├── telemetry.md          # NEW — event taxonomy, what's collected & why
│   ├── privacy.md            # NEW — data collection, retention, minimization
│   └── admin/, user/          — role-specific quick-starts
│
├── config/
│   └── index.js               — one place for all env-driven config
│
├── middleware/
│   ├── auth.js                — requireAdmin / requireUser
│   ├── accessExpiry.js        — subscription-duration check, every request
│   ├── accessWindow.js        — time-of-day/weekday check, every request
│   ├── featureGate.js         — loads + exposes permission flags per request
│   ├── activityLogger.js      — logActivity() helper
│   └── security.js            — helmet, rate limiters, CSRF
│
├── shared/
│   └── <core-logic>.js        — protected formula/algorithm, framework-agnostic,
│                                 unit-testable alone, NEVER required by client code
│
├── storage/
│   ├── databases/, exports/, backups/  — persistent-disk-backed, gitignored
│
├── services/
│   └── platform/
│       ├── server.js, db.js, schema.js, bootstrap.js
│       │
│       ├── routes/
│       │   ├── auth.js, users.js, admin.js
│       │   ├── activity.js         — audit/activity endpoints
│       │   ├── telemetry.js        # NEW — browser telemetry ingestion
│       │   ├── analytics.js        # NEW — traffic/usage endpoints
│       │   ├── monitoring.js       # NEW — security/system monitoring endpoints
│       │   └── seo.js              # NEW — optional, public-facing platforms only
│       │
│       ├── controllers/
│       │   ├── authController.js, userController.js
│       │   ├── telemetryController.js    # NEW
│       │   ├── analyticsController.js    # NEW
│       │   ├── monitoringController.js   # NEW
│       │   └── seoController.js          # NEW, optional
│       │
│       ├── services/
│       │   ├── userService.js, inviteService.js, activityService.js
│       │   ├── backupService.js, restoreService.js, exportService.js
│       │   ├── securityEventService.js   # NEW
│       │   ├── telemetryService.js       # NEW — validates/processes incoming events
│       │   ├── analyticsService.js       # NEW
│       │   ├── performanceService.js     # NEW — web/API performance metrics
│       │   ├── seoService.js             # NEW, optional
│       │   ├── riskService.js            # NEW — turns signals into a risk score
│       │   └── alertService.js           # NEW — where alerts actually get sent
│       │
│       ├── monitoring/                   # NEW — detection engine, separate from services/
│       │   ├── eventProcessor.js         — routes incoming events to the right monitor
│       │   ├── securityMonitor.js
│       │   ├── behaviorMonitor.js        — anomalous usage patterns
│       │   ├── performanceMonitor.js
│       │   ├── anomalyDetector.js
│       │   └── riskScorer.js
│       │
│       ├── seo/                          # NEW, optional — public-facing pages only
│       │   ├── crawler.js, pageAnalyzer.js, metadataAnalyzer.js
│       │   ├── linkAnalyzer.js, sitemapAnalyzer.js, structuredDataAnalyzer.js
│       │
│       ├── utils/
│       │   ├── password.js, time.js
│       │   ├── userAgent.js              # NEW — device/browser parsing
│       │   ├── ip.js                     # NEW — IP/proxy handling
│       │   ├── geo.js                    # NEW — approximate IP geolocation
│       │   └── privacy.js                # NEW — masking, minimization, retention
│       │
│       └── public/
│           ├── admin/    — plain HTML/CSS/JS admin dashboard
│           └── user/     — plain HTML/CSS/JS locked-down user interface
│
├── client/
│   └── telemetry/                        # NEW — browser-side collection, ships to the user
│       ├── telemetry.js                  — main collector, batches + posts events
│       ├── performance.js                — Core Web Vitals / browser performance
│       ├── interaction.js                — approved interaction events only
│       └── session.js                    — client-side session/context tagging
│
├── scripts/
│   ├── migrate.js, backup.js, cleanup.js
│   ├── seo-crawl.js                       # NEW, optional
│   └── retention.js                       # NEW — enforces data/log retention windows
│
└── tests/                                 # NEW as an explicit, categorized structure
    ├── security/, authentication/, authorization/
    ├── telemetry/, monitoring/, analytics/, performance/
    └── seo/
```

The `monitoring/`, `seo/`, `client/telemetry/`, and their supporting `services/`, `routes/`, and `controllers/` files are **additive layers** — a project that only needs the v1 core (admin/user, permissions, access control, backup/restore) should not build these speculatively. See §21 for the decision rule.

---

## 4. Database schema template

Unchanged core five tables from v1 (`admins`, `users`, `invite_links`, `sessions_log`, `activity_log`) — see original playbook for full DDL and design notes. **New tables, only if the corresponding layer is adopted:**

```sql
-- Monitoring / risk (§12)
security_events (
  id, source ('server'|'client'), event_type, severity,
  user_id, admin_id, ip_address, detail TEXT,  -- JSON blob, structured
  risk_score, reviewed BOOLEAN DEFAULT 0, reviewed_by_admin_id, reviewed_at,
  created_at
)

-- Telemetry (§13) — high volume, keep lean, prune aggressively
telemetry_events (
  id, session_id, user_id, event_type, payload TEXT, -- JSON, whitelisted shape only
  client_ts, received_at
)

-- Analytics (§15) — usually rolled up, not stored raw indefinitely
analytics_rollups (
  id, metric_name, dimension, period_start, period_end, value, computed_at
)
```

Design notes carried forward from v1, still true here: JSON columns over normalized flag columns wherever the shape will keep growing; precompute what you can at write time rather than at every read; make "unresolved/not configured" an explicit stored value, not an absence that silently looks like success (v1's `sessions_log.location_status = 'unresolved'` pattern applies directly to `security_events.reviewed` and any geo/UA-derived field).

---

## 5. Security checklist

All v1 items apply unchanged (bcrypt, lockout, httpOnly/sameSite cookies, CSRF, rate limiting, helmet CSP, unguessable invite tokens). Additions for the extended layers:

- [ ] Telemetry/monitoring endpoints are **rate-limited and authenticated to a session**, same as any other write endpoint — an unauthenticated telemetry ingestion route is a free-form logging sink for anyone who finds it.
- [ ] Client-side telemetry payloads are validated against a strict allowed-shape schema server-side before storage — never trust the client to only send what the collector script intends to send.
- [ ] IP geolocation and user-agent parsing are treated as **approximate, not authoritative** — never used as the sole basis for a security decision (e.g., don't hard-block on "impossible travel" from a free geolocation dataset; flag for review instead).
- [ ] Retention windows exist and are enforced by a script (`scripts/retention.js`), not "we'll clean it up eventually" — telemetry and event tables grow fast and are the first thing to blow a free-tier disk quota.
- [ ] Anything in `security_events.detail` or `telemetry_events.payload` is checked against the same PII-minimization rule as activity logs: store what's operationally necessary, not everything technically available.

---

## 6–11. Permission gating, access control, invite links, backup/restore, detail-level export, self-healing schema

Unchanged from v1 — see the original playbook. These are the load-bearing patterns of the core admin/user split and nothing in the extended layers changes them.

---

## 12. Monitoring & anomaly detection pattern (NEW)

The distinction that matters: **logging** records that something happened; **monitoring** decides whether what happened is *unusual enough to matter*.

- `monitoring/eventProcessor.js` is the single entry point events flow through — both server-originated events (failed logins, permission changes, admin actions) and client-originated ones (relayed via `telemetryService.js` after validation). It fans out to the specific monitor(s) that care.
- Each monitor (`securityMonitor`, `behaviorMonitor`, `performanceMonitor`) is narrow and single-purpose — resist the urge to build one god-monitor that tries to score everything. A monitor either flags an event into `security_events` with a severity, or it doesn't; it does not itself decide what happens next.
- `riskScorer.js` turns accumulated signals (multiple failed logins, new device + new IP + odd hour, unusual download volume) into a numeric score attached to the event, not a binary block/allow. Thresholds live in config, not hardcoded, so they can be tuned without a deploy.
- `alertService.js` is the only place that actually notifies a human (email/webhook/dashboard badge) — keep it separate from the monitors themselves so "detect" and "notify" can be tuned independently (e.g., raise the detection threshold without changing who gets paged, or vice versa).
- **Per §2 principle 8:** nothing in this layer auto-terminates a session or auto-locks an account. It populates a review queue an admin looks at. If a project genuinely needs automated response, that's a distinct, explicitly-designed rule ("3 flagged events in 10 minutes → force re-auth") reviewed and signed off separately — not an emergent side effect of the scoring logic.

**Watch for:** a monitor that fires on every request (e.g., checking behavior on every page load) will dominate CPU/DB time on a free-tier host before it ever catches anything useful. Batch or debounce evaluation — score on a schedule or on session-end, not on every single event.

---

## 13. Telemetry pattern — client + server (NEW)

Two halves that have to agree on shape, or validation in §5 breaks silently.

**Client side (`client/telemetry/`):**
- `telemetry.js` batches events client-side and posts them periodically (not one HTTP request per event — this is the single biggest performance/cost lever in this layer).
- `interaction.js` is an **explicit allowlist** of event types the collector will ever emit — not a generic "log anything" function. If a new interaction needs tracking, it's a deliberate addition here, not a call site sprinkled with `track('whatever')` strings.
- `session.js` tags every batch with a client-generated session/context identifier so server-side correlation doesn't depend solely on cookies (useful when a session spans a tab that loses/regains focus, matching the kind of tab/focus/fullscreen detection used in proctoring-style monitoring).

**Server side:**
- `telemetryService.js` is the only code that writes to `telemetry_events` — it validates payload shape against the same allowlist the client uses, rejects anything outside it, and strips fields that shouldn't be stored (see §14).
- `performanceService.js` handles the narrower Core Web Vitals / API-latency subset separately from general interaction telemetry — different retention needs, different consumers (engineering vs. product).

**Watch for:** if the client and server allowlists drift (someone adds an event type in `interaction.js` without updating the server-side validator), events get silently dropped and it looks like "telemetry stopped working" with no error anywhere. Keep the allowed-event-type list in one shared place both sides import from, or duplicate it deliberately with a comment pointing at the other copy.

---

## 14. Privacy & data-minimization pattern (NEW)

This is the layer that keeps §12 and §13 from quietly becoming a surveillance system nobody consciously designed.

- `docs/privacy.md` states, in plain language, what's collected, why, and for how long — written *before* the telemetry/monitoring code, not reverse-engineered from it afterward. If it's hard to write a one-sentence justification for a field, that's a signal to not collect it.
- `utils/privacy.js` centralizes masking/truncation logic (partial IP storage, hashed rather than raw device fingerprints where a raw one isn't actually needed, truncated user-agent strings) — one function reused everywhere a sensitive field is about to be persisted, not ad hoc redaction scattered per-table.
- `scripts/retention.js` actually deletes or aggregates-and-drops raw rows past their retention window on a schedule. A retention *policy* that exists only in a doc and never runs as code is not a retention policy.
- Consent (as in the exam-platform proctoring pattern this generalizes from) belongs at the point of collection, not buried in a ToS — an explicit checkbox before telemetry starts, logged with a timestamp, itself one of the few things worth keeping indefinitely.

**Watch for:** "admin-only" detail views (§10's pattern) are exactly where privacy leaks first — an admin export that includes full raw telemetry payloads because it was easier than filtering is a policy violation even though the admin *is* authorized to see more. Apply the same detail-level parameterization from §10 to telemetry/monitoring exports, don't assume admin access means unfiltered access.

---

## 15. Analytics pattern (NEW)

Distinct from monitoring: analytics answers "what's happening in aggregate," not "is something wrong."

- `analyticsService.js` reads from `telemetry_events` (and server-side request logs) and writes rollups into `analytics_rollups` on a schedule — dashboards query the rollup table, never the raw event table directly. This keeps dashboard queries fast regardless of how much raw telemetry accumulates, and gives a natural place to apply retention to the raw table (§14) without losing historical trend data.
- Keep the rollup granularity explicit (`period_start`/`period_end`, `dimension`) rather than computing "last 7 days" ad hoc at query time — the same "derived not stored, computed fresh" principle from real-time state (protocol state, live session status) does *not* apply here; analytics is the one place precomputing and caching the aggregate is correct, because the underlying events are immutable history, not live state that can change under you.

---

## 16. SEO analysis engine pattern (NEW — optional, public-facing platforms only)

Only relevant if the platform has publicly crawlable pages (marketing site, public docs, a landing page in front of the admin/user app) — most internal admin/user tools won't need this at all.

- `seo/crawler.js` respects `robots.txt` and crawls only what's actually public — never authenticate as a user to "check SEO" behind a login wall; that's not SEO, that's just fetching pages.
- Each analyzer (`metadataAnalyzer`, `linkAnalyzer`, `sitemapAnalyzer`, `structuredDataAnalyzer`) is independently runnable and independently testable against a single fetched page — the crawler's job is only to gather pages, not to also judge them.
- `scripts/seo-crawl.js` runs this as a scheduled background job, not inline with a user-facing request — a live SEO crawl on demand can itself look like a denial-of-service pattern to the site being crawled, even if it's your own site.

---

## 17. Testing structure (NEW)

The expanded `tests/` layout (security, authentication, authorization, telemetry, monitoring, analytics, performance, seo) maps one-to-one to the layers above — the point isn't the folder names, it's that **each layer gets tests written against its own concerns**, not lumped into one generic `tests/` file that only exercises the happy path of the core admin/user flow.

Priority order if time is limited (matches how much damage a silent failure in each layer does):
1. **authorization** — a permission check that silently passes when it should fail is the worst-case bug in this entire pattern.
2. **security** — lockout, rate limiting, CSRF; these are the first things an attacker tests.
3. **authentication** — invite-link and session flows (this is where the v1 §8 route-prefix bug was hiding, and exactly the kind of thing a "follow the link end-to-end" integration test catches).
4. **telemetry/monitoring** — validate the allowlist rejection path (§13), not just the happy path where valid events get stored.
5. **analytics/seo/performance** — lowest stakes; a wrong dashboard number is annoying, not a security incident.

---

## 18. Known pitfalls actually hit in this build (v1, unchanged)

| Bug | Root cause | Fix |
|---|---|---|
| `SqliteError: no such table` on fresh deploy | Host ran `npm install` only, skipped the migrate step | Self-healing schema (§11) |
| Every generated invite link 404'd | Link built without the router's mount prefix | Follow the link end-to-end in a test, not just check link generation returns 200 |
| `finalApprovedPct` silently became `null` | `Number(undefined)` is `NaN`, and `typeof NaN === 'number'` fooled a typeof-based "was a value provided" check | Check "was it provided" via string/undefined check before converting with `Number()` |
| Backup could theoretically corrupt under load | Raw `fs.copyFile` on a live WAL-mode SQLite file | Use the driver's online-backup API |
| Admin-set permission changes didn't reach an already-open user tab | Permissions fetched once at login, never re-fetched | Poll periodically, re-apply the same render logic used at login |
| Batch export column count broke when a column was conditionally hidden | Error rows used a fixed colspan that didn't match the varying header length | Compute header AND colspan together, from the same condition, every time |

**General risks worth watching for in the extended layers (§12–§16) — not yet confirmed hit, flagged proactively based on the same failure shapes above:**

| Risk | Likely root cause | Mitigation |
|---|---|---|
| Telemetry/event tables exhaust free-tier disk | No retention job actually running, only documented | `scripts/retention.js` on a schedule, verified with an actual row-count check, not just "the script exists" |
| Monitors silently stop firing after a schema change | `eventProcessor.js` pattern-matches on event shape that drifted from the client allowlist | Shared allowlist source (§13), integration test that posts a real event through the full pipeline |
| Admin dashboard shows stale risk scores | `riskScorer.js` runs on a schedule, dashboard reads live-looking data with no "as of" timestamp | Always render "last computed at," same discipline as §10's persisted last-result pattern |

---

## 19. Tech stack (opinionated, for consistency across projects)

v1 core, unchanged: Express + `better-sqlite3` (or team's preferred embedded/managed DB) + `bcrypt` + `express-session` + `csurf` (or its actively-maintained successor) + `helmet` + `express-rate-limit` + `multer` + `exceljs`/`pdfkit` + `nanoid`. No ORM — plain prepared statements, every query grep-able.

**Additions for the extended layers:**
- `geoip-lite` — offline IP geolocation; avoids an external API dependency and keeps geolocation working even if a paid service lapses. Preferred default for §13/§14 unless a project specifically needs higher accuracy than an offline dataset provides.
- A user-agent parser (e.g. `ua-parser-js` or `express-useragent`) for `utils/userAgent.js` — don't hand-roll UA string parsing.
- A simple job scheduler (`node-cron` or equivalent) for `scripts/retention.js`, `scripts/seo-crawl.js`, and rollup computation in `analyticsService.js` — avoid standing up a separate queue/worker infra for a free-tier deployment unless volume genuinely requires it.

---

## 20. Deployment gotchas (Render-specific, but the principle generalizes)

Unchanged from v1 (Blueprint vs. manually-created service reading `render.yaml`; persistent disk paths must be an actually-mounted disk; pin the runtime version for native bindings). **One addition:** telemetry/event tables are the fastest-growing thing on a persistent disk in this whole pattern — check actual disk usage in the dashboard periodically, don't assume the retention script (§14) is running just because it's deployed; verify it's actually executed and actually deleting rows.

---

## 21. Requirement → Pattern → Files, quick reference (expanded)

| If the requirement is... | ...use this pattern | ...in these files |
|---|---|---|
| "Admin controls what each user can do" | JSON permission columns, §6 | `middleware/featureGate.js`, `services/userService.js` |
| "Time-limited access" | Duration + window, both re-checked every request, §7 | `middleware/accessExpiry.js`, `accessWindow.js` |
| "Admin generates a login link" | Single-use, superseding invite tokens, §8 | `services/inviteService.js` |
| "See what users did" | Structured activity/session logging | `middleware/activityLogger.js`, `services/activityService.js` |
| "User shouldn't see the logic" | Formula lives server-only | `shared/<core-logic>.js` |
| "Admin needs more detail than the user" | Parameterized export detail level + persisted last-result, §10 | `services/exportService.js`, DB columns on `users` |
| "Don't lose data on deploy" | Self-healing schema, §11; persistent disk, §20 | `services/platform/schema.js`, `db.js` |
| "Admin needs to back up / recover data" | Online-backup API, dashboard-triggered, row-level restore, §9 | `services/backupService.js`, `restoreService.js` |
| "Detect suspicious behavior, not just log it" | Monitoring/anomaly detection, §12 | `monitoring/*.js`, `services/riskService.js`, `services/alertService.js` |
| "Track what the browser/user is actually doing" | Client + server telemetry, §13 | `client/telemetry/*.js`, `services/telemetryService.js` |
| "Make sure we're not over-collecting" | Privacy/minimization, §14 | `utils/privacy.js`, `docs/privacy.md`, `scripts/retention.js` |
| "Show usage trends/dashboards" | Analytics rollups, §15 | `services/analyticsService.js`, `analytics_rollups` table |
| "Public pages need SEO health checks" | SEO crawler engine, §16 | `seo/*.js`, `scripts/seo-crawl.js` |

---

## 22. Starting checklist for a new project using this pattern (expanded)

**Core (do these regardless of project size — unchanged from v1):**
- [ ] Define `admins`, `users` first — permission JSON columns and access-control columns before any routes.
- [ ] Write the core protected logic (`shared/`) as pure, framework-free functions before touching Express.
- [ ] Build `schema.js` with `ensureColumn()` from day one.
- [ ] Middleware order: auth → access expiry → access window → load permissions → rate limit → route handler.
- [ ] Decide the export detail-level split (§10) before building export functions.
- [ ] Backup + restore go in before real user data accumulates.

**Extended layers — adopt only if the signal in §1 actually applies to this project:**
- [ ] If suspicious-behavior detection is a real requirement → scope §12 to 1–2 monitors first (`securityMonitor` covers most needs), not the full six-monitor set on day one.
- [ ] If client behavior tracking is needed → agree on the event allowlist (§13) in writing before writing the collector — this is the single hardest thing to change later without silently dropping historical data.
- [ ] Write `docs/privacy.md` (§14) before, not after, the first telemetry event ships.
- [ ] Only build `seo/` (§16) if there's an actual public-facing surface — this is the layer most likely to be built speculatively and then never used.
- [ ] Stand up `scripts/retention.js` in the same PR that adds the first high-volume table (`telemetry_events`, `security_events`) — retention added later means writing a one-time cleanup migration on top of a table that's already grown unbounded.
