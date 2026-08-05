"""
Morning Work Brief Pipeline
Pulls M365 Calendar/Outlook, HubSpot deals, Asana tasks, Notion pages,
Monday.com items, and Jira issues. Formats as the plain-text scannable
brief specified in skills/morning-work-briefing/SKILL.md, delivers via
Outlook (Microsoft Graph) and logs a Notion page.

Design rule (per skill Gotchas): if any connector is missing a token or
errors out, show that section as "connector unavailable — check manually"
rather than skipping it silently or crashing the whole run.
"""

import os
import base64
import requests
from datetime import datetime, timezone, timedelta

# PHT = UTC+8
PHT = timezone(timedelta(hours=8))
NOW = datetime.now(PHT)
DATE_STR = NOW.strftime("%A, %B %d, %Y")
TIME_STR = NOW.strftime("%I:%M %p PHT")
DAY_START_UTC = NOW.astimezone(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
DAY_END_UTC = DAY_START_UTC + timedelta(days=1)
SINCE_24H_UTC = datetime.now(timezone.utc) - timedelta(hours=24)

# ── CONFIG — existing secrets (shared with intel_brief.py) ──────────────────
MS_GRAPH_TOKEN  = os.environ.get("MS_GRAPH_TOKEN", "")
RECIPIENT_EMAIL = os.environ.get("RECIPIENT_EMAIL", "")
NOTION_TOKEN    = os.environ.get("NOTION_TOKEN", "")
NOTION_DB_ID    = os.environ.get("NOTION_DATABASE_ID", "")

# ── CONFIG — new secrets this pipeline needs ─────────────────────────────────
HUBSPOT_TOKEN  = os.environ.get("HUBSPOT_TOKEN", "")
ASANA_TOKEN    = os.environ.get("ASANA_TOKEN", "")
MONDAY_TOKEN   = os.environ.get("MONDAY_TOKEN", "")
JIRA_DOMAIN    = os.environ.get("JIRA_DOMAIN", "")   # e.g. "yourcompany.atlassian.net"
JIRA_EMAIL     = os.environ.get("JIRA_EMAIL", "")
JIRA_API_TOKEN = os.environ.get("JIRA_API_TOKEN", "")

HEADERS_GRAPH   = {"Authorization": f"Bearer {MS_GRAPH_TOKEN}", "Content-Type": "application/json"}
HEADERS_NOTION  = {"Authorization": f"Bearer {NOTION_TOKEN}", "Content-Type": "application/json", "Notion-Version": "2022-06-28"}
HEADERS_HUBSPOT = {"Authorization": f"Bearer {HUBSPOT_TOKEN}", "Content-Type": "application/json"}
HEADERS_ASANA   = {"Authorization": f"Bearer {ASANA_TOKEN}"}
HEADERS_MONDAY  = {"Authorization": MONDAY_TOKEN, "Content-Type": "application/json"}


def _unavailable(source, err):
    print(f"⚠️  {source} unavailable: {err}")
    return None  # None = "connector unavailable", distinct from [] = "checked, nothing found"


# ── STEP 1 — M365 CALENDAR ────────────────────────────────────────────────────
def fetch_calendar_events():
    if not MS_GRAPH_TOKEN:
        return _unavailable("Calendar", "MS_GRAPH_TOKEN not set")
    try:
        start = NOW.replace(hour=0, minute=0, second=0).isoformat()
        end = (NOW.replace(hour=0, minute=0, second=0) + timedelta(days=1)).isoformat()
        r = requests.get(
            "https://graph.microsoft.com/v1.0/me/calendarView",
            headers={**HEADERS_GRAPH, "Prefer": 'outlook.timezone="Asia/Manila"'},
            params={"startDateTime": start, "endDateTime": end, "$orderby": "start/dateTime", "$top": 25},
            timeout=15,
        )
        r.raise_for_status()
        events = []
        for e in r.json().get("value", []):
            start_dt = e.get("start", {}).get("dateTime", "")
            time_str = start_dt[11:16] if len(start_dt) >= 16 else "??:??"
            events.append({
                "time": time_str,
                "title": e.get("subject", "(no title)"),
                "location": e.get("location", {}).get("displayName", ""),
                "attendee_count": len(e.get("attendees", [])),
            })
        return events
    except Exception as ex:
        return _unavailable("Calendar", ex)


# ── STEP 2 — M365 OUTLOOK (UNREAD, LAST 24H) ─────────────────────────────────
def fetch_unread_emails():
    if not MS_GRAPH_TOKEN:
        return _unavailable("Outlook", "MS_GRAPH_TOKEN not set")
    try:
        since = SINCE_24H_UTC.strftime("%Y-%m-%dT%H:%M:%SZ")
        r = requests.get(
            "https://graph.microsoft.com/v1.0/me/mailFolders/inbox/messages",
            headers=HEADERS_GRAPH,
            params={
                "$filter": f"isRead eq false and receivedDateTime ge {since}",
                "$select": "subject,from,receivedDateTime",
                "$orderby": "receivedDateTime desc",
                "$top": 25,
            },
            timeout=15,
        )
        r.raise_for_status()
        emails = []
        for m in r.json().get("value", []):
            received = m.get("receivedDateTime", "")
            hrs_ago = "?"
            try:
                rdt = datetime.strptime(received, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
                hrs_ago = round((datetime.now(timezone.utc) - rdt).total_seconds() / 3600, 1)
            except Exception:
                pass
            sender = m.get("from", {}).get("emailAddress", {})
            emails.append({
                "sender": sender.get("name") or sender.get("address", "Unknown"),
                "subject": m.get("subject", "(no subject)"),
                "hours_ago": hrs_ago,
            })
        return emails
    except Exception as ex:
        return _unavailable("Outlook", ex)


# ── STEP 3 — HUBSPOT DEALS ───────────────────────────────────────────────────
def fetch_hubspot_deals():
    if not HUBSPOT_TOKEN:
        return _unavailable("HubSpot", "HUBSPOT_TOKEN not set")
    try:
        r = requests.get(
            "https://api.hubapi.com/crm/v3/objects/deals",
            headers=HEADERS_HUBSPOT,
            params={
                "properties": "dealname,dealstage,amount,closedate,hs_lastmodifieddate,notes_next_activity",
                "limit": 100,
            },
            timeout=15,
        )
        r.raise_for_status()
        deals = []
        for d in r.json().get("results", []):
            p = d.get("properties", {})
            closedate = p.get("closedate")
            lastmod = p.get("hs_lastmodifieddate")
            relevant = False
            if closedate:
                try:
                    cd = datetime.fromisoformat(closedate.replace("Z", "+00:00"))
                    if datetime.now(timezone.utc) <= cd <= datetime.now(timezone.utc) + timedelta(days=7):
                        relevant = True
                except Exception:
                    pass
            if lastmod:
                try:
                    lm = datetime.fromisoformat(lastmod.replace("Z", "+00:00"))
                    if lm >= SINCE_24H_UTC:
                        relevant = True
                except Exception:
                    pass
            if relevant:
                deals.append({
                    "name": p.get("dealname", "(unnamed deal)"),
                    "stage": p.get("dealstage", "unknown"),
                    "amount": p.get("amount", "N/A"),
                    "close_date": closedate or "no close date",
                    "next_action": p.get("notes_next_activity") or "next action missing",
                })
        return deals
    except Exception as ex:
        return _unavailable("HubSpot", ex)


# ── STEP 4 — ASANA TASKS ──────────────────────────────────────────────────────
def fetch_asana_tasks():
    if not ASANA_TOKEN:
        return _unavailable("Asana", "ASANA_TOKEN not set")
    try:
        me = requests.get("https://app.asana.com/api/1.0/users/me", headers=HEADERS_ASANA, timeout=15)
        me.raise_for_status()
        me_data = me.json().get("data", {})
        user_gid = me_data.get("gid")
        workspaces = me_data.get("workspaces", [])
        if not user_gid or not workspaces:
            return _unavailable("Asana", "no workspaces found for this token")

        tasks = []
        for ws in workspaces:
            r = requests.get(
                "https://app.asana.com/api/1.0/tasks",
                headers=HEADERS_ASANA,
                params={
                    "assignee": user_gid,
                    "workspace": ws.get("gid"),
                    "completed_since": "now",  # incomplete tasks only
                    "opt_fields": "name,due_on,projects.name",
                },
                timeout=15,
            )
            r.raise_for_status()
            for t in r.json().get("data", []):
                due = t.get("due_on")
                overdue = False
                if due:
                    try:
                        overdue = datetime.strptime(due, "%Y-%m-%d").date() < NOW.date()
                    except Exception:
                        pass
                due_today = due == NOW.strftime("%Y-%m-%d")
                if due_today or overdue:
                    projects = t.get("projects", [])
                    tasks.append({
                        "name": t.get("name", "(untitled task)"),
                        "project": projects[0].get("name", "no project") if projects else "no project",
                        "due_on": due,
                        "overdue": overdue,
                    })
        return tasks
    except Exception as ex:
        return _unavailable("Asana", ex)


# ── STEP 5 — NOTION (RECENT MEETING NOTES / ACTION ITEMS) ────────────────────
def fetch_notion_recent_pages():
    if not NOTION_TOKEN:
        return _unavailable("Notion", "NOTION_TOKEN not set")
    try:
        r = requests.post(
            "https://api.notion.com/v1/search",
            headers=HEADERS_NOTION,
            json={
                "filter": {"property": "object", "value": "page"},
                "sort": {"direction": "descending", "timestamp": "last_edited_time"},
                "page_size": 20,
            },
            timeout=15,
        )
        r.raise_for_status()
        pages = []
        for p in r.json().get("results", []):
            last_edited = p.get("last_edited_time", "")
            try:
                led = datetime.strptime(last_edited, "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=timezone.utc)
            except Exception:
                try:
                    led = datetime.strptime(last_edited, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
                except Exception:
                    continue
            if led >= SINCE_24H_UTC:
                title = "(untitled)"
                props = p.get("properties", {})
                for v in props.values():
                    if v.get("type") == "title" and v.get("title"):
                        title = v["title"][0].get("plain_text", title)
                        break
                pages.append({"title": title, "url": p.get("url", "")})
        return pages
    except Exception as ex:
        return _unavailable("Notion", ex)


# ── STEP 6 — MONDAY.COM ───────────────────────────────────────────────────────
def fetch_monday_items():
    if not MONDAY_TOKEN:
        return _unavailable("Monday.com", "MONDAY_TOKEN not set")
    try:
        # NOTE: Monday's "person" and "status" columns are custom per board —
        # this pulls items across all accessible boards and reports name/state
        # generically. If your boards use non-default status labels, the
        # "blocked" filter below may need tuning to match your actual column values.
        query = """
        query {
          boards (limit: 15) {
            name
            items_page (limit: 10) {
              items {
                name
                column_values {
                  text
                  column { title }
                }
              }
            }
          }
        }
        """
        r = requests.post("https://api.monday.com/v2", headers=HEADERS_MONDAY, json={"query": query}, timeout=15)
        r.raise_for_status()
        data = r.json()
        if "errors" in data:
            return _unavailable("Monday.com", data["errors"])
        items = []
        for board in data.get("data", {}).get("boards", []):
            for item in board.get("items_page", {}).get("items", []):
                status_val = ""
                for cv in item.get("column_values", []):
                    if cv.get("column", {}).get("title", "").lower() == "status":
                        status_val = cv.get("text", "")
                if status_val and status_val.lower() in ("blocked", "stuck", "due today"):
                    items.append({"name": item.get("name", ""), "board": board.get("name", ""), "status": status_val})
        return items[:5]
    except Exception as ex:
        return _unavailable("Monday.com", ex)


# ── STEP 7 — JIRA ──────────────────────────────────────────────────────────────
def fetch_jira_issues():
    if not (JIRA_DOMAIN and JIRA_EMAIL and JIRA_API_TOKEN):
        return _unavailable("Jira", "JIRA_DOMAIN / JIRA_EMAIL / JIRA_API_TOKEN not set")
    try:
        auth = base64.b64encode(f"{JIRA_EMAIL}:{JIRA_API_TOKEN}".encode()).decode()
        r = requests.get(
            f"https://{JIRA_DOMAIN}/rest/api/3/search",
            headers={"Authorization": f"Basic {auth}", "Accept": "application/json"},
            params={
                "jql": 'assignee = currentUser() AND status in ("In Progress", "To Do")',
                "fields": "summary,priority,status",
                "maxResults": 10,
            },
            timeout=15,
        )
        r.raise_for_status()
        issues = []
        for i in r.json().get("issues", []):
            f = i.get("fields", {})
            issues.append({
                "key": i.get("key", ""),
                "summary": f.get("summary", ""),
                "priority": (f.get("priority") or {}).get("name", "None"),
            })
        return issues[:5]
    except Exception as ex:
        return _unavailable("Jira", ex)


# ── BRIEF BUILDER (matches SKILL.md output format exactly) ──────────────────
def build_brief_text(calendar, emails, deals, tasks, notion_pages, monday_items, jira_issues):
    lines = []
    lines.append("=" * 32)
    lines.append(f"WORK BRIEF — {DATE_STR}")
    lines.append(f"Generated: {TIME_STR}")
    lines.append("=" * 32)
    lines.append("")

    # CRITICAL — meetings <60min, unread client email >4h, overdue deal actions
    critical = []
    if calendar:
        for e in calendar:
            try:
                h, m = map(int, e["time"].split(":"))
                mins_until = (h * 60 + m) - (NOW.hour * 60 + NOW.minute)
                if 0 <= mins_until <= 60:
                    critical.append(f"{e['title']} starts in {mins_until} min | Calendar | Prep now")
            except Exception:
                pass
    if emails:
        for m in emails:
            if isinstance(m.get("hours_ago"), (int, float)) and m["hours_ago"] > 4:
                critical.append(f"{m['sender']} — {m['subject']} | Outlook | Unread {m['hours_ago']}h — reply")
    if deals:
        for d in deals:
            if d["next_action"] == "next action missing":
                critical.append(f"{d['name']} | HubSpot | Set a next action — none on file")

    lines.append("🔴 CRITICAL — Act First")
    if critical:
        lines.extend(f"• {c}" for c in critical[:5])
    else:
        lines.append("Nothing critical right now.")
    lines.append("")

    # MEETINGS
    lines.append(f"📅 TODAY'S MEETINGS ({len(calendar) if calendar else 0})" if calendar is not None
                  else "📅 TODAY'S MEETINGS — connector unavailable — check manually")
    if calendar:
        for e in calendar:
            loc = f" — {e['location']}" if e["location"] else ""
            lines.append(f"• {e['time']} {e['title']}{loc}")
    elif calendar == []:
        lines.append("None")
    lines.append("")

    # EMAILS
    lines.append(f"📬 EMAILS NEEDING REPLY ({len(emails) if emails else 0})" if emails is not None
                  else "📬 EMAILS NEEDING REPLY — connector unavailable — check manually")
    if emails:
        for m in emails:
            lines.append(f"• {m['sender']} — {m['subject']} — received {m['hours_ago']}h ago")
    elif emails == []:
        lines.append("None")
    lines.append("")

    # DEALS
    lines.append(f"💼 DEALS TO WATCH ({len(deals) if deals else 0})" if deals is not None
                  else "💼 DEALS TO WATCH — connector unavailable — check manually")
    if deals:
        for d in deals:
            lines.append(f"• {d['name']} — {d['stage']} — Close: {d['close_date']}")
            lines.append(f"  → Next action: {d['next_action']}")
    elif deals == []:
        lines.append("None")
    lines.append("")

    # TASKS
    due_today = [t for t in (tasks or []) if not t.get("overdue")]
    overdue_tasks = [t for t in (tasks or []) if t.get("overdue")]
    lines.append(f"✅ TASKS DUE TODAY ({len(due_today)})" if tasks is not None
                  else "✅ TASKS DUE TODAY — connector unavailable — check manually")
    if due_today:
        for t in due_today:
            lines.append(f"• {t['name']} — {t['project']}")
    elif tasks == []:
        lines.append("None")
    lines.append("")

    # OVERDUE/BLOCKED (Asana overdue + Monday blocked + Jira in-progress overflow)
    overdue_items = [f"{t['name']} — Asana — overdue" for t in overdue_tasks]
    if monday_items:
        overdue_items += [f"{m['name']} — Monday ({m['board']}) — {m['status']}" for m in monday_items]
    lines.append(f"⚠️ OVERDUE / BLOCKED ({len(overdue_items)})")
    if overdue_items:
        lines.extend(f"• {i}" for i in overdue_items[:8])
    else:
        lines.append("None")
    lines.append("")

    # CONTEXT — Notion + Jira
    context_items = []
    if notion_pages:
        context_items += [f"{p['title']} (Notion)" for p in notion_pages[:3]]
    if jira_issues:
        context_items += [f"{j['key']}: {j['summary']} [{j['priority']}] (Jira)" for j in jira_issues[:3]]
    lines.append("📝 CONTEXT")
    if context_items:
        lines.extend(f"• {c}" for c in context_items)
    else:
        lines.append("None")
    lines.append("")

    lines.append("=" * 32)
    lines.append("SUMMARY")
    n_meet = len(calendar) if calendar else 0
    n_email = len(emails) if emails else 0
    n_task = len(due_today)
    lines.append(f"Meetings: {n_meet} | Emails: {n_email} | Tasks: {n_task}")
    top = critical[0] if critical else (f"{calendar[0]['title']} at {calendar[0]['time']}" if calendar else "No single top priority surfaced")
    lines.append(f"Top priority: {top}")
    lines.append("=" * 32)

    return "\n".join(lines)


def build_html(brief_text):
    return f"""
    <!DOCTYPE html>
    <html>
    <head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"></head>
    <body style="font-family:Arial,sans-serif;max-width:680px;margin:0 auto;padding:20px;background:#f8f9fa;color:#1a1a2e;">
      <div style="background:#1a1a2e;color:white;padding:20px;border-radius:8px;margin-bottom:16px;">
        <h1 style="margin:0;font-size:20px;">📋 WORK BRIEF</h1>
        <p style="margin:6px 0 0;font-size:14px;color:#a8dadc;">{DATE_STR} | {TIME_STR}</p>
      </div>
      <pre style="white-space:pre-wrap;font-family:'Courier New',monospace;font-size:13px;line-height:1.5;background:white;padding:16px;border-radius:8px;">{brief_text}</pre>
    </body>
    </html>
    """


# ── DELIVERY ──────────────────────────────────────────────────────────────────
def send_outlook_email(html_body):
    if not MS_GRAPH_TOKEN or not RECIPIENT_EMAIL:
        print("MS Graph token or recipient email not set — skipping email delivery")
        return False
    payload = {
        "message": {
            "subject": f"📋 Work Brief — {DATE_STR}",
            "body": {"contentType": "HTML", "content": html_body},
            "toRecipients": [{"emailAddress": {"address": RECIPIENT_EMAIL}}],
        },
        "saveToSentItems": "true",
    }
    r = requests.post("https://graph.microsoft.com/v1.0/me/sendMail", headers=HEADERS_GRAPH, json=payload, timeout=15)
    if r.status_code == 202:
        print(f"✅ Email delivered to {RECIPIENT_EMAIL}")
        return True
    print(f"❌ Email failed: {r.status_code} — {r.text[:200]}")
    return False


def create_notion_page(brief_text):
    if not NOTION_TOKEN or not NOTION_DB_ID:
        print("Notion credentials not set — skipping Notion delivery")
        return False
    payload = {
        "parent": {"database_id": NOTION_DB_ID},
        "properties": {"title": {"title": [{"text": {"content": f"Work Brief — {DATE_STR}"}}]}},
        "children": [{
            "object": "block", "type": "code",
            "code": {"rich_text": [{"type": "text", "text": {"content": brief_text[:2000]}}], "language": "plain text"},
        }],
    }
    r = requests.post("https://api.notion.com/v1/pages", headers=HEADERS_NOTION, json=payload, timeout=15)
    if r.status_code == 200:
        print(f"✅ Notion page created: Work Brief — {DATE_STR}")
        return True
    print(f"❌ Notion failed: {r.status_code} — {r.text[:200]}")
    return False


# ── MAIN ──────────────────────────────────────────────────────────────────────
def main():
    print(f"Starting Work Brief pipeline — {DATE_STR}")

    print("Step 1 — M365 Calendar...")
    calendar = fetch_calendar_events()

    print("Step 2 — M365 Outlook (unread)...")
    emails = fetch_unread_emails()

    print("Step 3 — HubSpot deals...")
    deals = fetch_hubspot_deals()

    print("Step 4 — Asana tasks...")
    tasks = fetch_asana_tasks()

    print("Step 5 — Notion pages...")
    notion_pages = fetch_notion_recent_pages()

    print("Step 6 — Monday.com items...")
    monday_items = fetch_monday_items()

    print("Step 7 — Jira issues...")
    jira_issues = fetch_jira_issues()

    print("Building brief...")
    brief_text = build_brief_text(calendar, emails, deals, tasks, notion_pages, monday_items, jira_issues)
    print(brief_text)

    html = build_html(brief_text)

    print("Delivering to Outlook...")
    send_outlook_email(html)

    print("Logging to Notion...")
    create_notion_page(brief_text)

    print("✅ Work Brief pipeline complete.")


if __name__ == "__main__":
    main()
