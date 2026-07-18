---
name: candlestick-price-action
description: Reference library for candlestick patterns, Smart Money Concepts (SMC/ICT), price action setups, Candle Range Theory (CRT), and multi-timeframe entry method. Use this whenever the user shares a chart/screenshot and asks "what pattern is this," asks to identify a setup, asks about candlestick meaning (engulfing, pin bar, hammer, doji, morning/evening star, etc.), asks about POI/BMS/MSS/mitigation/liquidity/fakeout/supply-demand zones, asks to classify daily bias, wants help building a trade thesis from a chart, or references terms from their TradeSense Strategy Library (VWAP, S/R flip/retest, BOS/ChoCH, conviction scoring). Also use for building or reviewing entries against a structured price-action checklist, or explaining why a candle/pattern implies bullish/bearish continuation vs reversal.
---

# Trading Pattern Recognition

A structured reference for reading candlestick patterns, Smart Money Concepts (SMC), and price-action setups, and turning them into a trade thesis with entry, invalidation, and target logic. This mirrors the terminology used in the user's TradeSense dashboard (VWAP, 9 EMA, S/R flip/retest, conviction scoring, horizon tags) — use consistent vocabulary so pattern calls can map directly onto existing Strategy Library categories.

**Standard disclaimer to include when giving a live trade read:** these are pattern-recognition heuristics, not guarantees — confirmation (volume, retest, close beyond level) always outranks the raw shape.

---

## How to use this skill

1. **Identify what's being asked**: single candle ID, multi-candle combo, SMC structure (POI/BMS/MSS), a full setup (breakout-retest, pullback, fakeout), daily bias, or a "build me a thesis from this chart" request.
2. **Read top-down**: bias/trend (HTF) → structure/zone (POI, S/R, supply/demand) → trigger candle/pattern → confirmation → invalidation (SL) → target.
3. **Always state confidence, not certainty.** Attach a rough historical-reliability note when available (see §4).
4. **Cross-reference TradeSense vocabulary** where relevant: POI ≈ their S/R zones; BMS/MSS ≈ their BOS/ChoCH; mitigation ≈ retest.

---

## 1. Single & Combo Candlestick Patterns

### Reversal patterns (bullish)
| Pattern | Shape | Why it signals reversal |
|---|---|---|
| Bullish Engulfing | Small red candle fully engulfed by a larger green candle | Buyers overwhelm the prior sellers in one bar |
| Hammer | Small body, long lower wick, little/no upper wick | Sellers pushed price down, buyers rejected it back up |
| Inverted Hammer | Small body, long upper wick, at bottom of downtrend | Buying pressure emerging at lower levels |
| Bullish Pin Bar | Long lower wick, close near the high | Strong rejection of lower prices |
| Piercing Line | Red candle, then green candle closing above the red candle's midpoint | Bulls reverse mid-body |
| Morning Star | Red candle → small indecision candle → strong green candle | 3-bar reversal after a downtrend |
| Bullish Harami | Small green candle contained inside the prior red candle's body | Momentum stalling, indecision before reversal |
| Three White Soldiers | 3 consecutive green candles, each closing higher | Strong bullish continuation (not reversal) |

### Reversal patterns (bearish)
| Pattern | Shape | Why it signals reversal |
|---|---|---|
| Bearish Engulfing | Small green candle fully engulfed by a larger red candle | Sellers overwhelm buyers in one bar |
| Hanging Man | Small body, long lower wick, appears after an uptrend | Warns of weakening buying pressure |
| Shooting Star | Small body, long upper wick, appears after an uptrend | Rejection of higher prices |
| Bearish Pin Bar | Long upper wick, close near the low | Strong rejection of higher prices |
| Dark Cloud Cover | Green candle, then red candle closing below its midpoint | Bears reverse mid-body |
| Evening Star | Green candle → small indecision candle → strong red candle | 3-bar reversal after an uptrend |
| Bearish Harami | Small red candle contained inside the prior green candle's body | Momentum stalling before reversal |
| Three Black Crows | 3 consecutive red candles, each closing lower | Strong bearish continuation |
| Tweezer Top | Two candles sharing the same high, rejected from resistance | Bearish reversal at resistance |

### High-reliability combos (backtested reversal rates — treat as rough historical tendencies, not live odds)
| Pattern | Type | Approx. reversal rate |
|---|---|---|
| Three Line Strike (Bullish) | Continuation-break reversal | ~84% bullish |
| Matching Low | Reversal | ~84% bullish |
| Three Black Crows | Continuation | ~78% bearish |
| Two Black Gapping | Continuation | ~78% bearish |
| Three Line Strike (Bearish) | Reversal | ~65% bearish |
| Abandoned Baby (Bullish) | Reversal | ~70% bullish |

**Combo rule of thumb**: Bearish Engulfing + Tweezer Top stacked at the same resistance level = high-confidence SELL signal. Same logic in reverse (Bullish Engulfing + Tweezer Bottom at support) = high-confidence BUY.

### Momentum reading from candle anatomy
- **Strongest bullish/bearish**: full body, minimal wicks, strong close in the direction of the move.
- **Weakening momentum**: growing wicks opposite the close (rejection), balanced wicks (indecision), or a weak close near the open.
- Use this to grade *conviction* of a move, not just its direction — maps to TradeSense's conviction scoring.

---

## 2. Smart Money Concepts (SMC / ICT-style)

| Term | Definition | TradeSense equivalent |
|---|---|---|
| **POI (Point of Interest)** | A zone where smart money previously showed strong interest and reversed price | S/R zone |
| **Initial Break** | First move away from a POI, often manipulative (liquidity grab) | — |
| **BMS (Break of Market Structure)** | Price breaks a prior swing high/low, confirming a shift in direction | BOS |
| **MSS (Market Structure Shift)** | The structural pivot point marking trend change | ChoCH |
| **Mitigation** | Price returns to the POI to "fill orders" before continuing in the original direction | Retest |
| **Leg Completion** | Price finishes a bullish/bearish leg after sweeping liquidity, before the next move | — |
| **Swing Low/High** | The extreme point where sellers/buyers exhaust and price reverses | — |
| **Supply Zone** | Area of potential bearish reversal (sell zone) | Resistance |
| **Demand Zone** | Area of potential bullish reversal (buy zone) | Support |
| **Liquidity Sweep / Fakeout** | Price pokes above resistance / below support to trigger stops, then reverses | False breakout |

### Reading the full SMC sequence (top-down)
1. Price reacts hard at a **POI** → mark the zone.
2. **Initial Break** away from POI (often looks like a breakout — be skeptical).
3. **BMS** confirms structure has shifted (swing high/low broken).
4. Price often returns for **Mitigation** (retest of the POI/broken structure).
5. **Leg Completion** — a full impulsive move plays out.
6. New **Swing Low/High** forms, and the cycle can repeat.

### Fakeout / Liquidity Sweep logic
- Clean bullish move → approaches resistance → **fake breakout** wick above resistance → price snaps back inside the range = liquidity grab, not a real breakout.
- **Risky entry**: shorting immediately at the wick (before confirmation).
- **Safe entry**: wait for price to return to the support/resistance area and show a rejection candle there before entering.
- Rule: fakeouts exist to grab liquidity — never chase the breakout candle itself, wait for the retrace.

### Supply & Demand Zone playbook
1. Price consolidates (basing) before breakout.
2. Breaks into a supply or demand zone.
3. Reaction pattern at the zone confirms direction:
   - Demand zone + Bullish Pinbar or Morning Star → BUY signal.
   - Supply zone + Bearish Engulfing or Evening Star → SELL signal.
4. Wait for **re-test & confirmation** of the zone before entering — don't front-run it.

---

## 3. Price Action Setups (4 core patterns)

| # | Setup | Structure | Entry | Bias |
|---|---|---|---|---|
| 1 | **Breakout & Retest** | Price breaks resistance with momentum, comes back to retest it as new support | Buy on retest | Bullish |
| 2 | **Pullback** | Strong primary trend, healthy pullback, trend continues | Buy in trend direction after pullback | Bullish (or bearish mirrored) |
| 3 | **Break of Structure** | Uptrend of higher-highs/higher-lows breaks — signals possible reversal | Sell on break, wait for confirmation | Bearish |
| 4 | **False Breakout** | Price breaks resistance to grab liquidity, fails to hold, reverses down | Sell after rejection | Bearish |

### Complex Pullback (6-step method)
Use for entries after a deep/irregular retracement (commonly forms as a bearish flag or triangle):
1. **Skip the first leg up** — don't chase the initial impulsive move.
2. Look for a **reversal candlestick pattern** within the pullback.
3. **Wait for confirmation** — don't anticipate the reversal.
4. **Entry**: above the first candle's close (can also use the 0.214 Fib retracement level as an entry trigger).
5. **Stop loss**: below the second candle of the pattern.
6. **Take profit**: using the 1.618 extension or the 2.0 Fib retracement level.

### Rectangle & Bullish Flag continuation
- Price ranges inside a rectangle (support/resistance), consolidates into a descending bullish flag, then breaks resistance.
- **Wait for confirmation** of the resistance break before entering — don't anticipate.
- Target projected using the height of the prior impulsive move.

---

## 4. Candle Range Theory (CRT)

CRT reads a small cluster of candles (2-candle, 3-candle, multi-candle, or inside-bar models) as a mini high/low range that acts like a micro support/resistance:

| Model | Structure |
|---|---|
| 2-candle CRT | One green + one red candle define CRT high/low |
| 3-candle CRT | Three candles define the range, middle candle often smaller |
| Multiple-candle CRT | An extended run of candles where the first candle's high/low frames the whole range |
| Inside-bar CRT | A smaller candle range nested fully inside the prior candle's range |

**Rules:**
- **BUY bias**: price approaches the CRT low and starts moving up.
- **SELL bias**: price approaches the CRT high and starts moving down.
- CRT high acts as resistance; CRT low acts as support — same logic as any S/R flip, just defined over a tight candle cluster instead of a swing point.

---

## 5. Daily Bias Guide (2-candle read)

Quick read of the most recent 2 candles to set directional bias — useful as a fast pre-market or pre-session check:

- **Bullish**: strong green candle closing near its high with minimal wick, or a green candle engulfing/dominating the prior red candle → buyers in control.
- **Bearish**: strong red candle closing near its low, or a red candle engulfing/dominating the prior green candle → sellers in control.
- **Avoid / no trade**: candles show balanced, overlapping wicks with no clear dominance (indecision) → market uncertain, best to stay flat until a clear break.

---

## 6. Multi-Timeframe Entry Framework

A top-down waterfall for narrowing from bias to trigger (maps directly onto the user's horizon classification: long → short → scalp):

| Timeframe | Role |
|---|---|
| **4H** | Direction, trend, key levels, support/demand |
| **1H** | Central reference — breaks, order blocks (OB), fair value gaps (FVG), liquidity |
| **15min** | Reversal/confirmation and trigger for entry |

Sequence: establish HTF (4H) bias and levels → drop to 1H to find the specific structural feature (OB/FVG/liquidity pool) reacting to that level → drop to 15min for the confirmation candle/pattern that triggers the actual entry. RSI/MACD on the 1H can be used as secondary confirmation of momentum agreeing with the structural read, not as a standalone signal.

---

## 7. Building a Trade Thesis (synthesis template)

When asked to "read this chart" or "what's the setup here," respond using this structure:

1. **Bias** (HTF trend + daily bias read)
2. **Key level** (POI / supply-demand / CRT high-low / prior swing)
3. **Structure signal** (BMS/MSS, break of structure, or none yet)
4. **Trigger pattern** (name the candlestick pattern precisely, note wick/body anatomy)
5. **Confirmation needed** (retest/mitigation, close beyond level, or already present)
6. **Invalidation** (where the read is wrong — stop level)
7. **Target** (next opposing level, Fib extension, or measured move)
8. **Confidence caveat** — note this is pattern-based, not a certainty; historical reversal rates (§1) are approximate.

Keep the response as a scannable structure like the above, not a wall of prose — mirrors how the user reviews their own dashboard cards.
