---
name: vwap-ema-day-trading-system
description: Reference for a full intraday options day-trading system built on VWAP + 9 EMA trend rules, pre-market key levels, support/resistance flips, retest entries, EMA/level-based exits, position sizing, runner scaling math, risk management, trading psychology, and journaling. Use this whenever the user asks about VWAP bounces/rejects, 9 EMA rules, pre-market high/low retests, key-level marking (psychological/pre-market/other), entry or exit rules for a day trade, position sizing or risk-reward math, scaling out and holding runners, options Greeks basics (delta/gamma/theta), trade journaling methodology, or building a daily pre-market checklist/trade plan. Also use when reviewing a described trade for whether it followed a risk-based, rules-based process, or when the user references their own "system," "trade plan," or TradeSense strategy stack in the context of intraday stock/options trading.
---

# Day Trading System — VWAP + 9 EMA Method

A complete intraday options trading system (options basics, key levels, VWAP/9EMA trend rules, entries/exits, sizing, psychology, journaling). This mirrors terminology already used in the user's TradeSense dashboard — VWAP, 9 EMA, premarket high/low, S/R flip/retest, ATR-based sizing, conviction-based entries, runner strategies, horizon classification — so use consistent vocabulary and treat this as the rule-system layer that TradeSense's `computeTargets` engine and conviction scoring are meant to operationalize.

**Standard disclaimer when giving a live trade read:** this is a rules-based heuristic system, not a guarantee — confirmation (5-min close, retest, volume) always outranks anticipating a move.

---

## 1. Options Basics (quick reference)

- **Calls** = bet stock goes up. **Puts** = bet stock goes down.
- Options are leveraged: a 1% stock move can be a 30–100%+ move in a contract, which is why they're used to grow small accounts faster than shares — at the cost of more volatility/risk.
- **Strike selection**: buy slightly out-of-the-money (OTM), closest expiration available (0DTE on SPY/QQQ, weekly on individual names otherwise).
- **Greeks** (functional, not academic):
  - **Delta** — how much the contract moves per $1 move in the stock (e.g., delta 0.50 → stock +$1 → contract +$0.50, roughly).
  - **Gamma** — the rate of change of delta itself (delta accelerates as the option moves further in-the-money).
  - **Theta** — time decay; only matters if holding overnight.
- **In-the-money premium pump**: once a contract flips from OTM to ITM, extrinsic value converts to intrinsic value and the contract starts moving much better — this is why strike selection near the current price matters.

---

## 2. Reading Candles & Basic Chart Setup

- Preferred intraday timeframe: **5-minute chart**. Daily/weekly used only for higher-timeframe confluence (a daily pattern adds confidence to a 5-min setup).
- **Close is the most important price** on any candle — levels are judged by whether the candle *closed* above/below them, not by wicks alone.
- **Wicks read intent**: upper wicks in an up-formation = sellers stepping in (caution); lower wicks in a down-formation = buyers absorbing (caution on shorts).
- Quick bullish/bearish candle vocabulary used throughout this system: bullish/bearish engulfing, morning/evening star, hammer, gravestone doji (major reversal warning at the top of a trend — do not buy calls into one), double top/bottom, bull/bear flags (consolidation after an impulsive move, continuation pattern).

---

## 3. Key Levels — 3 Types (mark all of these before the session)

| Type | How to find it |
|---|---|
| **Pre-market high/low** | Mark the high and low of the 4:00am–9:30am session. This is the first reference level of the day. |
| **Psychological levels** | Round numbers — every $5/$10, with every $50/$100 being a major level. |
| **Other key levels (structural)** | Mark the top/bottom of consolidation/flag zones with **3+ taps or reaction points**. Price moves *level to level*, not randomly — these zones repeat as support/resistance. Also mark high-of-day/low-of-day as they form. |

### Support/Resistance Flip (core concept)
- A broken **resistance** becomes the new **support** (and vice versa for a broken support becoming resistance).
- Entries are taken on the **retest of the flipped level**, not on the initial breakout — the breakout candle itself is not the entry.
- **Trend read**: 5-min close above pre-market high → trend is up. 5-min close below pre-market low → trend is down.

---

## 4. VWAP Rules

VWAP = volume-weighted average price = the market's collective average entry price for the day. Treat it as a real psychological pivot, not just an indicator line.

- **Bullish VWAP bounce**: stock is above VWAP **and** above pre-market high (trend up) → wait for a dip back to VWAP with a rejection wick forming → enter calls off the bounce.
- **Bearish VWAP reject**: stock is below VWAP **and** below pre-market low (trend down) → wait for a bounce up to VWAP with a rejection wick forming → enter puts off the reject.
- **Hard rule**: never buy puts when price is over VWAP. Never buy calls when price is under VWAP.
- VWAP bullish retests are only valid when price is also above pre-market high; VWAP bearish retests are only valid when price is also below pre-market low. Trend + VWAP location must agree.
- Exit rule: if a position is held through a VWAP-based entry, a 5-minute close on the wrong side of VWAP invalidates the read.

---

## 5. 9 EMA Rules

The 9 EMA (exponential moving average, settings: length 9, "wait for timeframe close" checked, no bands, visible on all timeframes) is used for trend confirmation and tighter entries.

Three trend states:
1. **Bullish**: price above VWAP *and* above the 9 EMA, trending up → buy calls only.
2. **Bearish**: price below VWAP *and* below the 9 EMA, trending down → buy puts only.
3. **Chop ("Gucci snake")**: EMA/VWAP crisscrossing repeatedly, no clear direction → **no trades**. Chop is a stop-out machine; sit it out.

- **Trend = probability.** Don't fight a trending market on the other side.
- **Stop loss on a trend trade**: exit when the 9 EMA breaks (next candle closes on the wrong side of it).
- VWAP outranks the 9 EMA: a stock can be below the 9 EMA but still above VWAP — that is not yet a valid short, since VWAP is the higher-order pivot ("VWAP is king").

---

## 6. Entries

- **The only entry trigger in this system is the retest**, not the initial breakout candle.
- Sequence: mark pre-market high/low → wait for a 5-minute **close** beyond the level (confirms the break) → wait for price to come back and tap the level (the retest = the support/resistance flip in action) → enter as close to the level as possible.
- Rationale: entering tight to the retested level minimizes risk (a small stop) while the target is comparatively large — this is what produces a favorable risk:reward ratio.
- Same retest logic applies to VWAP and 9 EMA touches, not just pre-market levels.
- Minimum acceptable risk:reward for taking a trade: **1:2**. Typical target: 1:3.

---

## 7. Exits

Two exit mechanisms, used together:

1. **Level-based stop**: if price gives a 5-minute close back beyond the retested level (i.e., invalidates the retest), exit immediately — don't wait, don't hope.
2. **EMA-based stop** (for trend/runner positions): exit when the 9 EMA breaks (next 5-min candle closes on the wrong side of the EMA).

### Profit-taking — the "sell high/low of day, leave a runner" rule
- Take partial profits at new high-of-day (long) or new low-of-day (short) — don't sell 100% there.
- Leave a **runner** (remaining size) with its stop trailing the 9 EMA — let the trend keep paying as long as the EMA holds.
- Because partial profits were already locked in before the runner is decided, the runner's effective cost basis is reduced (often to near-zero or negative) — this is why holding the runner "risk-free" against house money is the core leverage mechanic of this system, not a separate gamble.

---

## 8. Position Sizing & Runner Math

| Account size | Position size (approx.) | Risk | Target reward |
|---|---|---|---|
| $1,000 | ~$300 | ~$100 (20–25%) | ~$200 (min 2:1) |
| $5,000 | ~$1,000 | ~$200 (20%) | ~$400 (min 2:1) |
| Larger/experienced (2+ yrs) | scale up proportionally | same 20–25% risk logic | same 2:1+ target |

- General rule of thumb: **~20–25% of account per trade, minimum 2:1 risk:reward.**
- A $1,000 account sized this way supports ~5 trades/day of "dry powder" — more than enough; most good traders take fewer than 3 trades a day.
- **Runner math** (why this matters): sell partial size at high/low-of-day for a locked gain (e.g., 40%) → hold the remainder against the 9 EMA stop → because the locked gain already "paid for" the runner contract, the runner's effective net cost is near zero, so a large % move on the runner (100–400%+) is disproportionately more profitable than the same % move on the full original size. This is the mechanism, not luck — always structure size so a runner is possible on trending days.

---

## 9. Risk Management Rules

- **Risk-first mindset, always.** Before entering, define the stop/invalidation point — never enter thinking about the profit target first.
- **Max daily loss**: a hard, pre-defined dollar amount for the day. Hit it → stop trading, no exceptions.
- **Two-red-trade rule**: after 2 consecutive losing trades, stop and take a 20–30 minute break minimum before considering another trade.
- **Never average down** into a losing position — the emotional pull to "lower the average cost" ignores that price action is telling you the read was wrong. Averaging *up* into a working position is acceptable; averaging down is not.
- **Never trade a stock with earnings that week** — options pricing (IV) gets distorted around earnings.
- Check pending economic data before entering — avoid opening new risk right before a scheduled data release.

---

## 10. Trading Psychology

- Trading emotions can't be eliminated, but **emotional traps** can and must be avoided: FOMO, revenge trading, "it did the opposite last time so I'll flip my rule," chasing a crowded trade.
- **Revenge trading** is the #1 account-killer — it stems from trying to "make back" a loss same-day. The system-level fix is the max daily loss + two-red-trade rules above, not willpower.
- **Reset daily**: treat each day's P&L as starting from zero, win or lose, long-run or short-run. Don't carry yesterday's (or last year's) losses into today's decision-making.
- **Grade yourself on execution, not on dollars.** Set goals around following the plan / only taking A+ setups / only taking 1:2+ trades — not around a dollar target. Dollar-amount goals produce worse outcomes than performance goals.
- **The best trader is the best at losing, not the best at winning.** Small losses, break-even trades, and small/big wins are all "winning trades" in the sense that they reflect the plan being followed.
- **Don't be blinded by other people's results** (social media flexing, huge documented wins) — it triggers goal-chasing and oversized risk-taking. Consistency compounds; chasing does not.
- **90% of traders fail from running out of money, not from lacking a strategy.** The entire point of the risk rules above is to keep enough capital in the game to let a working edge compound.

---

## 11. Journaling Methodology

Track, at minimum, per trade: date, time of day, ticker, setup type, expiration used, strike distance from spot, any relevant life/mood context, and any execution mistakes.

**What journaling is for**: finding what to cut and what to double down on — segment win rate and average win/loss by:
- **Ticker** (some names may have a bad edge for you specifically)
- **Time of day** (e.g., a trader might have a 0% win rate at the open but 50%+ later)
- **Expiration type** (e.g., 0DTE vs weekly — 0DTE often has worse risk:reward even with a similar win rate, due to smaller wins relative to losses)

Decision rule: if a segment (ticker/time/expiration) shows a poor win rate **or** a poor risk:reward (small avg win vs large avg loss), stop trading that segment — regardless of how it "feels." Journal weekly and monthly at minimum.

---

## 12. Daily Pre-Market Checklist

1. Find the day's strongest and weakest stocks (largest % movers) from the watchlist.
2. Mark pre-market high/low on the names being watched.
3. Check **confluence**: is the candidate stock outperforming/underperforming the index (SPY/QQQ) or its sector peers during pullbacks? Trading calls should show relative strength vs. the index; puts should show relative weakness.
4. Mark all key levels (pre-market, psychological, structural/other) for the strength/weakness candidates.
5. Review economic data releases scheduled for the session.
6. Confirm the stock does **not** have earnings this week.
7. Check the daily chart for any larger-timeframe pattern (flag, triangle, breakout base) for added confluence.

### Weekly prep (Sunday routine)
- Spend ~1–2 hours scanning daily charts across the core watchlist for patterns, bases, and key levels forming.
- Set price alerts at key levels so the market can "come to you" instead of guessing.

---

## 13. Building a Trade Plan (synthesis template)

When asked to build or evaluate a day's trade plan, use this structure:

1. **Trend** — is price trending up, down, or in chop ("Gucci snake")? If chop: no trade.
2. **Position relative to key levels** — above/below pre-market high/low, VWAP, 9 EMA (all three should agree for a high-conviction setup).
3. **If/then branches** — "if price breaks and closes beyond pre-market high, enter calls on the retest" / "if we miss that, look for a tight consolidation (flag) to enter off instead." Always have both a primary and a backup trigger.
4. **Entry** — retest only, sized per §8.
5. **Stop / invalidation** — level-based or EMA-based per §7.
6. **Profit-taking plan** — partial at high/low-of-day, runner held against the 9 EMA.
7. **Confidence caveat** — this is a rules-based read, not a certainty; always defer to the actual 5-minute close over anticipation.

Keep responses scannable (numbered/bulleted), matching how the user reviews their own TradeSense dashboard cards — not a wall of prose.
