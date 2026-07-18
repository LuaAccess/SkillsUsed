---
name: reversal-mean-reversion-trading
description: Counter-trend / mean-reversion trading playbook — exhaustion signals, divergence, fading extended moves, and reversal-specific entry, stop, and target logic. Use whenever the user wants to fade a move, catch a top or bottom, trade against the prevailing trend, asks about RSI/MACD divergence, exhaustion candles (gravestone doji, shooting star, evening/morning star at extremes), or explicitly frames a trade as "reversal" or "counter-trend" rather than continuation. Do NOT use for trend-following/continuation entries (retest of a broken level in the direction of the trend, VWAP/9EMA bounce trades, breakout-and-retest) — those belong to vwap-ema-day-trading-system or candlestick-price-action instead. This skill governs the opposite edge type — trading against the current move, not with it.
---

# Reversal & Mean-Reversion Trading

The counter-trend companion to the momentum/continuation system (vwap-ema-day-trading-system). Reversal trades fight the prevailing move, so they require a materially different risk posture: lower win-rate expectation, tighter invalidation, and typically a lower conviction ceiling than continuation trades taken in the same direction as the trend (see risk-conviction-framework for how this affects tier and size).

**Standard caveat**: reversals are inherently lower-probability than continuation trades in a trending market — this system exists to filter for the subset of reversal setups worth taking, not to make counter-trend trading as reliable as trend-following.

---

## 1. When a Reversal Setup Is Even Worth Considering

Before looking for a reversal trigger, confirm the move is actually **extended**, not just moving:

| Signal | Threshold |
|---|---|
| Distance from VWAP or 9 EMA | Multiple ATRs away from the mean, not a normal pullback distance |
| RSI | Overbought (>70) or oversold (<30) on the working timeframe |
| Location | At a multi-tap key level, CRT high/low, or a supply/demand zone with prior reaction history (see candlestick-price-action §2, §4) |
| Volume | Climactic — a volume spike well above the recent average, suggesting exhaustion rather than fresh accumulation |

If a move is extended but **not** at a meaningful level, there is no reversal trade — an extended move in open space with no structure to react against usually keeps going. Skip it.

---

## 2. Exhaustion Confirmation (do not anticipate)

Require one of these on the working timeframe before entering, not before it fully forms:

- **Gravestone doji** at the top of a trend — long upper wick, close at/near the open, appearing after an extended up move. Treat as the single strongest single-candle reversal warning in this system.
- **Shooting star / bearish pin bar** (top) or **hammer / bullish pin bar** (bottom) with rejection wick at least 2x the body.
- **Evening star** (top, 3-bar) or **morning star** (bottom, 3-bar).
- **Bearish/bullish engulfing** at the extreme, ideally combined with a tweezer top/bottom (two candles sharing the same high/low) — see candlestick-price-action §1 for the full pattern reference.
- **Divergence**: price prints a higher high (top) or lower low (bottom) while RSI or MACD prints a *lower* high or *higher* low respectively. Divergence without a confirming candle is a warning, not a trigger — wait for both.

## 3. Liquidity Sweep / Fakeout Reversals

The highest-quality reversal subtype: price pokes beyond a key level to grab liquidity/stops, fails to hold, and snaps back inside the range.

- **Risky entry**: shorting/buying the wick itself, before it closes back inside the range.
- **Safe entry**: wait for the retrace back into the support/resistance area and a rejection candle *there* before entering (see candlestick-price-action §2 for the full fakeout playbook — this skill's job is only to flag when a fakeout should be read as the reversal trigger vs a false signal).

---

## 4. Stop Placement (tighter than continuation trades)

- Stop goes **beyond the exhaustion candle's extreme wick**, not beyond a wider structural level — reversal stops are inherently tighter because the entry is at the extreme, not at a retested flip level.
- If the required stop distance would force an oversized position to hit a meaningful dollar risk, that is a signal the setup is lower quality (the extreme wasn't clean) — skip rather than widen the stop to "make the math work."

---

## 5. Target Logic (revert to the mean, not extend)

- Primary target: **back to VWAP, the 9 EMA, or the midpoint of the recent range** — reversal trades target a *return to normal*, not a new extension.
- Secondary target (if momentum shifts convincingly, confirmed by a break of the minor structure against the prior trend): the opposite key level or CRT high/low.
- Do not carry a reversal trade with a continuation-sized target (e.g. a full trend-length move) — that mismatches the setup's actual edge.

---

## 6. Invalidation Rule — When to Not Take the Reversal At All

- If the higher-timeframe trend is strong (clean HTF momentum per vwap-ema-day-trading-system §4/§5 criteria, no HTF exhaustion signal present), **skip the reversal** even if a lower-timeframe exhaustion candle appears. A 15-min reversal candle inside a strong 4H/daily trend is usually just a pause, not a turn.
- Reversal setups scored through risk-conviction-framework §2 should rarely reach the "Conservative" tier on trend-alignment alone (they're fighting the HTF trend by definition) — expect most valid reversal trades to sit at Moderate or Aggressive tier, sized accordingly, unless multiple independent exhaustion signals stack (candle + divergence + climactic volume + key level, all at once).

---

## 7. Synthesis Template

When asked to evaluate a possible reversal:

1. **Is the move extended?** (§1) — if not, stop here, no trade.
2. **Confirmation present?** (§2/§3) — name the specific pattern, don't anticipate it.
3. **HTF trend check** (§6) — does the HTF context support even considering a reversal here?
4. **Stop** — placed beyond the extreme (§4).
5. **Target** — mean-reversion target, not extension (§5).
6. **Hand off to risk-conviction-framework** for scoring/sizing — do not size a reversal trade using continuation-trade assumptions.
