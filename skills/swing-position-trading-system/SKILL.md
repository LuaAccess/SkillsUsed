---
name: swing-position-trading-system
description: Multi-day to multi-week ("Long" horizon) swing and position trading system — daily/weekly structure, overnight and weekend gap risk, options expiration/theta selection for multi-day holds, and catalyst-driven entries. Use whenever the user is holding or considering holding a position overnight, across multiple days, or through a catalyst like earnings; asks about swing trading, position trading, or the "Long" horizon tag; asks which expiration to choose for a multi-day hold; or asks whether to hold through an earnings report. Do NOT use for same-day-close intraday trades (5-min VWAP/9EMA entries that close before the bell) — those belong to vwap-ema-day-trading-system, which explicitly avoids overnight and earnings-week risk. This skill governs the opposite holding-period regime.
---

# Swing / Position Trading System (Long Horizon)

The multi-day counterpart to vwap-ema-day-trading-system. Where the intraday system is built to close flat every day and explicitly avoids earnings-week names, this system is built around holding through multiple sessions — including, deliberately, through catalysts like earnings when the thesis calls for it. Treat this as a different risk regime, not just "the same system on a bigger timeframe."

---

## 1. Core Differences from the Intraday System

| Dimension | Intraday (vwap-ema-day-trading-system) | Swing/Position (this skill) |
|---|---|---|
| Holding period | Closes same day | Days to weeks |
| Structure timeframe | 5-min, with 4H/1H/15min waterfall | Daily and weekly candles |
| Overnight/weekend risk | Avoided entirely | Explicitly accepted — must be sized for |
| Earnings | Avoid trading names with earnings that week | Can be a deliberate entry catalyst |
| Expiration selection | Closest available (0DTE/weekly) | Monthly or further-dated, sized for theta |
| Primary stop reference | 9 EMA / VWAP on 5-min | Daily swing high/low, daily 21/50 EMA |

---

## 2. Structure & Trend (Daily/Weekly)

- Use the **daily chart** as the primary structure timeframe (weekly for the broader trend context), not the 5-min.
- Key levels are the same categories as candlestick-price-action (§2–3: POI, S/R flips, CRT-style ranges) but drawn from daily/weekly swing highs and lows, not pre-market levels.
- Trend reference: daily 21 EMA and 50 EMA in place of the 9 EMA/VWAP pairing — price above both, both sloping up, is the swing-bullish equivalent of the intraday bullish state.
- A multi-day breakout-and-retest (candlestick-price-action §3, setup #1) is the primary entry pattern here, just read on the daily instead of the 5-min.

---

## 3. Options Selection for Multi-Day Holds

- **Avoid 0DTE/weekly-expiring-this-week contracts** for a thesis meant to play out over days — theta decay accelerates sharply in the final week and will bleed a correct directional read.
- Prefer **monthly expirations**, or at minimum 2–3 weeks out, so theta decay per day is a small fraction of the position's value.
- Favor **ATM or slightly ITM strikes** over far OTM for multi-day holds — far OTM contracts are theta- and IV-crush-sensitive in a way that can lose money even on a correct directional call if the move isn't fast enough.
- If holding through earnings deliberately (§4), account for **IV crush**: the position's IV is elevated pre-earnings and collapses after the print regardless of direction — a directional win can still be diluted or erased by the IV drop unless the strike/expiration was chosen with this in mind.

---

## 4. Catalyst-Driven Entries (the deliberate opposite of the intraday rule)

- Earnings, guidance updates, macro data (Fed decisions, CPI/jobs prints), and sector-rotation events are valid, sometimes primary, entry theses here — unlike the intraday system, which avoids earnings-week names entirely.
- A catalyst-driven entry still needs the same structure: a defined level, a defined invalidation, and a target — the catalyst is the *reason* for the thesis, not a replacement for technical confirmation.
- Distinguish **pre-catalyst positioning** (entering before the event, sized smaller to account for binary/gap risk) from **post-catalyst confirmation** (entering after the reaction, once the new level and trend are established) — these carry very different risk profiles and should be sized differently via risk-conviction-framework.

---

## 5. Risk Management for Multi-Day Holds

- **Gap risk is real and unhedged by intraday stops** — a stop-loss order does not protect against an overnight or weekend gap through it. Size assuming the worst realistic overnight gap for that name/sector, not just the stop distance on the daily chart.
- Position size should generally be **smaller as a % of account** than an equivalent-conviction intraday trade, specifically because of this unhedgeable gap exposure — run sizing through risk-conviction-framework, but treat the "max size per tier" as a ceiling that gap-prone setups (pre-earnings, small caps, biotech-style binary catalysts) should sit well under, not at.
- Stop-loss reference: a daily close beyond the invalidating swing high/low, or beyond the daily 21 EMA for trend-following positions — not an intraday wick.

---

## 6. Trade Management

- **Trailing stop**: ratchet the stop to the most recent daily swing low (long) or swing high (short) as the position develops — the daily-chart equivalent of the 9 EMA trail used intraday.
- **Partial profit-taking**: scale out at prior daily/weekly resistance (long) or support (short), or at Fibonacci extension levels (1.618, 2.0) off the initiating move — same "sell into strength, leave a runner" logic as vwap-ema-day-trading-system §7, just referenced against daily levels instead of intraday high-of-day.
- **Weekly review cadence**: this horizon is managed on a weekly check-in rhythm, not a candle-by-candle one — resist adjusting the thesis based on single-day intraday noise that doesn't change the daily structure.

---

## 7. Psychological Differences from Intraday Trading

- Patience is the primary discipline here — the same "cut fast on invalidation" reflex from intraday trading still applies, but the *evaluation window* is days, not minutes, so avoid re-litigating the thesis on every red intraday candle.
- Journal this horizon separately from intraday trades (see vwap-ema-day-trading-system §11 methodology, applied per-horizon) — mixing multi-day swing trade stats into an intraday win-rate journal will produce misleading segment conclusions in either direction.

---

## 8. Synthesis Template

When asked to build or evaluate a swing/position thesis:

1. **Daily/weekly trend** — above/below the 21/50 EMA, HTF structure intact or breaking.
2. **Catalyst** (if any) — pre- or post-event positioning, and what IV/theta implication that carries (§3–4).
3. **Level** — the daily/weekly key level or CRT-style range the thesis is built around.
4. **Expiration/strike selection** — monthly+, ATM/slightly ITM, per §3.
5. **Stop** — daily close beyond swing point or 21 EMA (§5).
6. **Target/trail** — prior level or Fib extension, trailing per §6.
7. **Size** — via risk-conviction-framework, discounted for gap risk if applicable (§5).
8. **Confidence caveat** — multi-day theses carry more macro/news uncertainty than intraday reads; state this plainly rather than presenting a swing thesis with intraday-level confidence.
