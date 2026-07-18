---
name: risk-conviction-framework
description: Position sizing, conviction scoring, and risk-tier framework (conservative/moderate/aggressive) for options day/swing trades. Use whenever the user asks how big to size a trade, what risk tier a setup falls into, how to score conviction/confidence on a trade idea, what minimum risk:reward to require, how many confluences a setup needs before taking it, or how to compare a "safe" vs "aggressive" version of the same trade. This is the sizing/scoring layer that other trading skills (candlestick-price-action, vwap-ema-day-trading-system, reversal-mean-reversion-trading, swing-position-trading-system) should point to instead of restating sizing rules — apply this whenever position size, stop distance, or conviction score is part of the question, regardless of which pattern or horizon skill also fires.
---

# Risk & Conviction Framework

The sizing/scoring overlay shared across every other trading skill in this set. Pattern-recognition and horizon-specific skills (candlestick/SMC, day-trading VWAP/EMA, reversal, swing) tell you *what* the setup is and *where* the level is — this skill tells you *how much* to risk and *how confident* to be, tying directly into TradeSense's conviction scoring and ATR-based sizing engine.

**Core principle (non-negotiable): position size is always derived from stop-loss distance, never from instrument price.** Raw share/contract price is not a valid sizing proxy — two trades at the same price can have wildly different risk if their stops sit at different distances.

---

## 1. Position Sizing Formula

```
Risk$ = Account size × Risk tier %  (see §3 for tier %)
Contracts/Shares = Risk$ ÷ (Entry price − Stop price)
```

- For options, use the **premium** distance (entry premium − stop premium), not the underlying's stop distance, unless you're sizing off a delta-adjusted equivalent.
- Never size to "how much I want to make" — size to "how much I'm willing to lose if the stop hits." Reward is a function of R:R applied *after* size is set from risk, not the other way around.
- If a computed size would exceed the account's max-size-per-trade cap (§3), size is capped — do not override the risk tier to fit a desired dollar amount into a trade.

---

## 2. Conviction Scoring Rubric (0–10)

Score every setup before sizing it. Points are additive; a setup with a low score should either be skipped or sized at the conservative tier regardless of how good it "feels."

| Factor | Points |
|---|---|
| Higher-timeframe trend alignment (setup agrees with 4H/daily bias) | +2 |
| Key-level confluence (POI/S-R/CRT high-low all line up at the same zone) | +2 |
| Candlestick/price-action confirmation present (not anticipated) | +2 |
| Volume confirms the move (expansion on trigger candle) | +1 |
| Multiple timeframe agreement (e.g. 4H→1H→15min all agree, per the multi-timeframe framework) | +2 |
| Calibrated historical hit-rate ≥55% for this strategy, **only once 15+ closed trades exist for it** — otherwise this factor is scored 0 (neutral), not guessed | +1 |

**Total /10.** Below 15 closed trades for a strategy, treat the max obtainable score as 9 and don't let the missing calibration point silently lower every score — flag it explicitly as "uncalibrated" rather than scoring it as a penalty.

---

## 3. Risk Tiers

| Tier | Conviction score required | Min R:R | Max size per trade (% of account) | Max concurrent correlated positions |
|---|---|---|---|---|
| **Conservative** | 8–10 | 1:3 | 10–15% | 1 |
| **Moderate** | 6–7 | 1:2.5 | 15–20% | 2 |
| **Aggressive** | 4–5 | 1:2 (hard floor) | 20–25% | 2, only if uncorrelated |
| **Skip** | 0–3 | — | 0% | — |

- **1:2 is the floor for any tier** — a setup that can't clear 1:2 R:R is not a trade regardless of conviction score (matches the vwap-ema-day-trading-system entry rule).
- "Correlated positions" = same underlying, same sector, or same macro driver (e.g. two AI-chip names on the same catalyst count as one exposure, not two).
- A user who explicitly says "I want to be conservative/aggressive on this one" is choosing a tier directly — still enforce that tier's min R:R and max size, don't let stated risk appetite override the floor.

---

## 4. Applying the Framework

When asked to size or score a trade:
1. Compute the conviction score (§2), showing each factor's contribution.
2. State the resulting tier (§3) and whether the trade's actual R:R clears that tier's minimum.
3. Compute size using §1's formula, capped at the tier's max %.
4. If the trade fails the tier's R:R floor, say so explicitly and either suggest a tighter stop / better entry to fix the ratio, or say to skip it — do not round up a 1:1.8 to "close enough."
5. Flag correlation exposure if this position would be the 2nd+ correlated position open.

### Output template

```
Conviction score: X/10 (breakdown: ...)
Tier: Conservative / Moderate / Aggressive / Skip
R:R check: [actual ratio] vs [tier minimum] → pass/fail
Position size: Risk$ ÷ stop distance = N contracts/shares (capped at tier max %)
Correlation flag: [none / already holding correlated position in X]
```

---

## 5. Interaction with Runners (vwap-ema-day-trading-system)

When a position includes a scaled runner (see vwap-ema-day-trading-system §7–8), size the **initial full position** using this framework's tier rules — the runner's reduced effective cost basis after partial profit-taking is a *management* outcome, not a separate sizing decision at entry.

---

## 6. Common Misapplications to Flag

- Sizing off account "feel" ("I have room, I'll just add more") instead of recomputing Risk$ from the tier %.
- Upgrading a tier after entry because the trade is working — the tier and size were set at entry; scaling in further is a new sizing decision requiring its own conviction score, not a continuation of the original one.
- Treating "high conviction" as an excuse to skip a stop loss — even a 10/10 setup gets a defined stop; conviction changes size and R:R requirement, never removes the stop.
