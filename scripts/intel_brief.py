"""
Morning Intel Brief Pipeline
Fetches live data from free RSS/APIs, formats as HTML email,
delivers to Outlook via Microsoft Graph API + creates Notion page.
Zero cost. No Claude API needed for raw delivery.
"""

import os
import json
import requests
import xml.etree.ElementTree as ET
from datetime import datetime, timezone, timedelta

# PHT = UTC+8
PHT = timezone(timedelta(hours=8))
TODAY = datetime.now(PHT)
DATE_STR = TODAY.strftime("%A, %B %d, %Y")
TIME_STR = TODAY.strftime("%I:%M %p PHT")

# ── CONFIG ──────────────────────────────────────────────────────────────────
MS_GRAPH_TOKEN   = os.environ.get("MS_GRAPH_TOKEN", "")
RECIPIENT_EMAIL  = os.environ.get("RECIPIENT_EMAIL", "")
NOTION_TOKEN     = os.environ.get("NOTION_TOKEN", "")
NOTION_DB_ID     = os.environ.get("NOTION_DATABASE_ID", "")

HEADERS_GRAPH  = {"Authorization": f"Bearer {MS_GRAPH_TOKEN}", "Content-Type": "application/json"}
HEADERS_NOTION = {"Authorization": f"Bearer {NOTION_TOKEN}", "Content-Type": "application/json", "Notion-Version": "2022-06-28"}

# ── DATA SOURCES ─────────────────────────────────────────────────────────────
SOURCES = {
    "reuters":     "https://feeds.reuters.com/reuters/topNews",
    "bbc":         "https://feeds.bbci.co.uk/news/world/rss.xml",
    "cisa":        "https://www.cisa.gov/uscert/ncas/alerts.xml",
    "hackernews":  "https://hacker-news.firebaseio.com/v0/topstories.json",
    "coingecko":   "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=percent_change_24h_desc&per_page=5&page=1",
    "exchangerate":"https://open.er-api.com/v6/latest/USD",
    "ph_news":     "https://news.google.com/rss/search?q=philippines+technology+business&hl=en-PH&gl=PH&ceid=PH:en",
    "nvd":         "https://services.nvd.nist.gov/rest/json/cves/2.0?resultsPerPage=3&noRejected",
}

# ── FETCH FUNCTIONS ──────────────────────────────────────────────────────────
def fetch_rss(url, max_items=5):
    """Fetch and parse RSS/Atom feed, return list of {title, link, summary}"""
    items = []
    try:
        r = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
        r.raise_for_status()
        root = ET.fromstring(r.content)
        ns = {"atom": "http://www.w3.org/2005/Atom"}
        # RSS format
        for item in root.findall(".//item")[:max_items]:
            title = item.findtext("title", "").strip()
            link  = item.findtext("link", "").strip()
            desc  = item.findtext("description", "").strip()[:200]
            if title:
                items.append({"title": title, "link": link, "summary": desc})
    except Exception as e:
        items.append({"title": f"Source unavailable: {e}", "link": "", "summary": ""})
    return items

def fetch_hackernews(max_items=5):
    """Fetch top HackerNews stories"""
    items = []
    try:
        ids = requests.get(SOURCES["hackernews"], timeout=10).json()[:max_items]
        for story_id in ids:
            story = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json", timeout=5).json()
            if story and story.get("title"):
                items.append({
                    "title": story.get("title",""),
                    "link":  story.get("url","https://news.ycombinator.com"),
                    "summary": f"Score: {story.get('score',0)} | Comments: {story.get('descendants',0)}"
                })
    except Exception as e:
        items.append({"title": f"HackerNews unavailable: {e}", "link": "", "summary": ""})
    return items

def fetch_crypto():
    """Fetch top crypto movers from CoinGecko"""
    items = []
    try:
        r = requests.get(SOURCES["coingecko"], timeout=10)
        data = r.json()
        for coin in data[:3]:
            change = coin.get("price_change_percentage_24h", 0)
            direction = "▲" if change > 0 else "▼"
            items.append({
                "name":   coin.get("name",""),
                "symbol": coin.get("symbol","").upper(),
                "change": f"{direction} {abs(change):.2f}%",
                "price":  f"${coin.get('current_price',0):,.4f}"
            })
    except Exception as e:
        items.append({"name": f"CoinGecko unavailable: {e}", "symbol":"", "change":"", "price":""})
    return items

def fetch_forex():
    """Fetch USD/PHP and key rates from ExchangeRate API"""
    rates = {}
    try:
        r = requests.get(SOURCES["exchangerate"], timeout=10)
        data = r.json()
        base_rates = data.get("rates", {})
        for pair in ["PHP", "SGD", "JPY", "EUR", "GBP"]:
            rates[pair] = base_rates.get(pair, "N/A")
    except Exception as e:
        rates["error"] = str(e)
    return rates

def fetch_nvd_cves():
    """Fetch latest CVEs from NVD"""
    items = []
    try:
        r = requests.get(SOURCES["nvd"], timeout=15)
        data = r.json()
        for vuln in data.get("vulnerabilities", [])[:3]:
            cve = vuln.get("cve", {})
            cve_id = cve.get("id", "Unknown")
            desc_list = cve.get("descriptions", [])
            desc = next((d["value"] for d in desc_list if d["lang"] == "en"), "No description")[:200]
            metrics = cve.get("metrics", {})
            severity = "Unknown"
            if "cvssMetricV31" in metrics:
                severity = metrics["cvssMetricV31"][0].get("cvssData", {}).get("baseSeverity", "Unknown")
            elif "cvssMetricV2" in metrics:
                severity = metrics["cvssMetricV2"][0].get("baseSeverity", "Unknown")
            items.append({"id": cve_id, "severity": severity, "description": desc})
    except Exception as e:
        items.append({"id": f"NVD unavailable: {e}", "severity": "", "description": ""})
    return items

# ── HTML EMAIL BUILDER ────────────────────────────────────────────────────────
def build_html(headlines, bbc, tech_news, ph_news, cves, crypto, forex, cisa):
    """Build full HTML email"""

    def section(title, emoji, content_html):
        return f"""
        <div style="margin-bottom:24px;">
          <h2 style="color:#1a1a2e;border-bottom:2px solid #e63946;padding-bottom:6px;font-size:16px;">
            {emoji} {title}
          </h2>
          {content_html}
        </div>"""

    def news_items(items):
        html = "<ul style='padding-left:18px;margin:0;'>"
        for item in items:
            link = item.get("link","")
            title = item.get("title","")
            anchor = f'<a href="{link}" style="color:#457b9d;text-decoration:none;">{title}</a>' if link else title
            html += f"<li style='margin-bottom:8px;font-size:14px;'>{anchor}</li>"
        html += "</ul>"
        return html

    # Headlines
    hl_html = news_items(headlines[:5])

    # Tech
    tech_html = news_items(tech_news[:3])

    # Cyber CVEs
    cve_html = "<ul style='padding-left:18px;margin:0;'>"
    for cve in cves:
        severity_color = {"CRITICAL":"#e63946","HIGH":"#f4a261","MEDIUM":"#e9c46a","LOW":"#2a9d8f"}.get(cve.get("severity",""), "#666")
        cve_html += f"""
        <li style='margin-bottom:10px;font-size:14px;'>
          <strong style='color:{severity_color};'>{cve.get('id','')} [{cve.get('severity','')}]</strong><br>
          <span style='color:#444;'>{cve.get('description','')}</span>
        </li>"""
    cve_html += "</ul>"

    # CISA alerts
    cisa_html = news_items(cisa[:3])

    # Crypto
    crypto_html = "<ul style='padding-left:18px;margin:0;'>"
    for c in crypto:
        color = "#2a9d8f" if "▲" in c.get("change","") else "#e63946"
        crypto_html += f"<li style='margin-bottom:6px;font-size:14px;'><strong>{c.get('name','')} ({c.get('symbol','')})</strong> — <span style='color:{color};'>{c.get('change','')}</span> — {c.get('price','')}</li>"
    crypto_html += "</ul>"

    # Forex
    forex_html = "<ul style='padding-left:18px;margin:0;'>"
    for pair, rate in forex.items():
        if pair != "error":
            forex_html += f"<li style='margin-bottom:4px;font-size:14px;'><strong>USD/{pair}:</strong> {rate}</li>"
    forex_html += "</ul>"

    # PH/SEA
    ph_html = news_items(ph_news[:3])

    return f"""
    <!DOCTYPE html>
    <html>
    <head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"></head>
    <body style="font-family:Arial,sans-serif;max-width:680px;margin:0 auto;padding:20px;background:#f8f9fa;color:#1a1a2e;">

      <div style="background:#1a1a2e;color:white;padding:20px;border-radius:8px;margin-bottom:24px;">
        <h1 style="margin:0;font-size:20px;">🌏 INTEL BRIEF</h1>
        <p style="margin:6px 0 0;font-size:14px;color:#a8dadc;">{DATE_STR} | {TIME_STR}</p>
        <p style="margin:4px 0 0;font-size:12px;color:#e63946;">⚠️ SOURCE: Live RSS feeds — no AI analysis. Paste into Claude + say "intel brief on this" for full analysis.</p>
      </div>

      {section("GLOBAL HEADLINES", "🌏", hl_html)}
      {section("TECH & AI", "🤖", tech_html)}
      {section("CYBERSECURITY — CVEs", "🔐", cve_html)}
      {section("CYBERSECURITY — CISA ALERTS", "🚨", cisa_html)}
      {section("MARKET SIGNALS — CRYPTO", "📈", crypto_html)}
      {section("MARKET SIGNALS — FOREX (vs USD)", "💱", forex_html)}
      {section("PH / SEA WATCH", "🇵🇭", ph_html)}

      <div style="background:#e8f4f8;padding:16px;border-radius:8px;border-left:4px solid #457b9d;margin-top:24px;">
        <h3 style="margin:0 0 8px;font-size:14px;color:#1a1a2e;">⚡ NEXT STEP</h3>
        <p style="margin:0;font-size:13px;color:#444;">
          Forward this email to Claude or paste the content and say:<br>
          <strong>"intel brief on this"</strong><br>
          Claude will apply full IT consulting analysis + PH opportunity radar.
        </p>
      </div>

      <p style="font-size:11px;color:#999;margin-top:24px;text-align:center;">
        LuaAccess Intel Pipeline | GitHub Actions | Sources: Reuters, BBC, CISA, NVD, CoinGecko, ExchangeRate API, Google News
      </p>

    </body>
    </html>
    """

# ── DELIVERY FUNCTIONS ────────────────────────────────────────────────────────
def send_outlook_email(html_body):
    """Send email via Microsoft Graph API"""
    if not MS_GRAPH_TOKEN or not RECIPIENT_EMAIL:
        print("MS Graph token or recipient email not set — skipping email delivery")
        return False
    payload = {
        "message": {
            "subject": f"🌏 Intel Brief — {DATE_STR}",
            "body": {"contentType": "HTML", "content": html_body},
            "toRecipients": [{"emailAddress": {"address": RECIPIENT_EMAIL}}]
        },
        "saveToSentItems": "true"
    }
    r = requests.post(
        "https://graph.microsoft.com/v1.0/me/sendMail",
        headers=HEADERS_GRAPH,
        json=payload,
        timeout=15
    )
    if r.status_code == 202:
        print(f"✅ Email delivered to {RECIPIENT_EMAIL}")
        return True
    else:
        print(f"❌ Email failed: {r.status_code} — {r.text[:200]}")
        return False

def create_notion_page(html_body, headlines, cves, crypto):
    """Create Notion page with today's intel brief"""
    if not NOTION_TOKEN or not NOTION_DB_ID:
        print("Notion credentials not set — skipping Notion delivery")
        return False

    # Build Notion blocks from key sections
    blocks = [
        {
            "object": "block", "type": "callout",
            "callout": {
                "rich_text": [{"type": "text", "text": {"content": f"Live RSS data — {DATE_STR}. Paste into Claude + say 'intel brief on this' for full AI analysis."}}],
                "icon": {"emoji": "⚠️"}, "color": "yellow_background"
            }
        },
        {
            "object": "block", "type": "heading_2",
            "heading_2": {"rich_text": [{"type": "text", "text": {"content": "🌏 Global Headlines"}}]}
        }
    ]

    for item in headlines[:5]:
        blocks.append({
            "object": "block", "type": "bulleted_list_item",
            "bulleted_list_item": {
                "rich_text": [{"type": "text", "text": {"content": item.get("title",""), "link": {"url": item.get("link","")} if item.get("link") else None}}]
            }
        })

    blocks.append({
        "object": "block", "type": "heading_2",
        "heading_2": {"rich_text": [{"type": "text", "text": {"content": "🔐 Top CVEs"}}]}
    })

    for cve in cves:
        blocks.append({
            "object": "block", "type": "bulleted_list_item",
            "bulleted_list_item": {
                "rich_text": [{"type": "text", "text": {"content": f"{cve.get('id','')} [{cve.get('severity','')}] — {cve.get('description','')[:150]}"}}]
            }
        })

    payload = {
        "parent": {"database_id": NOTION_DB_ID},
        "properties": {
            "title": {"title": [{"text": {"content": f"Intel Brief — {DATE_STR}"}}]}
        },
        "children": blocks
    }

    r = requests.post(
        "https://api.notion.com/v1/pages",
        headers=HEADERS_NOTION,
        json=payload,
        timeout=15
    )
    if r.status_code == 200:
        print(f"✅ Notion page created: Intel Brief — {DATE_STR}")
        return True
    else:
        print(f"❌ Notion failed: {r.status_code} — {r.text[:200]}")
        return False

# ── MAIN ──────────────────────────────────────────────────────────────────────
def main():
    print(f"Starting Intel Brief pipeline — {DATE_STR}")

    print("Fetching Reuters headlines...")
    headlines = fetch_rss(SOURCES["reuters"], 5)

    print("Fetching BBC world news...")
    bbc = fetch_rss(SOURCES["bbc"], 5)

    print("Fetching HackerNews tech...")
    tech_news = fetch_hackernews(3)

    print("Fetching PH/SEA news...")
    ph_news = fetch_rss(SOURCES["ph_news"], 3)

    print("Fetching CISA alerts...")
    cisa = fetch_rss(SOURCES["cisa"], 3)

    print("Fetching NVD CVEs...")
    cves = fetch_nvd_cves()

    print("Fetching CoinGecko crypto...")
    crypto = fetch_crypto()

    print("Fetching ExchangeRate forex...")
    forex = fetch_forex()

    print("Building HTML email...")
    html = build_html(headlines, bbc, tech_news, ph_news, cves, crypto, forex, cisa)

    print("Delivering to Outlook...")
    send_outlook_email(html)

    print("Creating Notion page...")
    create_notion_page(html, headlines, cves, crypto)

    print("✅ Intel Brief pipeline complete.")

if __name__ == "__main__":
    main()
