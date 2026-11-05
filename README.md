# Padhan Paper Desk — live scorecard

> **Paper trading only.** No wallet, no keys, no real money. Every trade is simulated on live Solana prices
> with realistic fees, slippage and rug-pull losses. Updated 2026-11-05 12:24 UTC · day 27.1

## Verdict: **DO NOT INVEST — failed: profit, pf, dd, edge, luck**

| | Invest only if ALL of these hold (rules fixed before the test started) |
|---|---|
| ✅ | At least 14 days live and 100 closed desk trades |
| ❌ | Desk is net profitable after all fees, slippage and rugs |
| ❌ | Profit factor (gross wins / gross losses) is 1.3 or better |
| ❌ | Worst peak-to-trough drawdown is 30% or less |
| ❌ | Desk beats the random control book by 10+ percentage points |
| ❌ | Still profitable after removing its 3 best trades |

## Books (each started with $1,000 paper)

| | AI desk | Random control |
|---|---:|---:|
| Equity | $89.71 | $494.03 |
| Return | -91.03% | -50.60% |
| Closed trades | 386 | 222 |
| Win rate | 35.0% | 27.0% |
| Avg win / avg loss | +29.0% / -37.2% | +26.8% / -30.0% |
| Profit factor | 0.48 | 0.39 |
| Max drawdown | 91.0% | 50.6% |
| Profit without top 3 trades | $-992.02 | $-571.62 |
| Rug / liquidity-pull exits | 24 | 13 |
| Open positions now | 0 | 0 |

Tokens screened: **3,209,113** across 38,525 scans. Top reasons the safety agent (LUNA) said no:
dex (1,266,750), liq_low (789,513), too_old (446,468), odd_quote (361,611), lp_unlocked (32,719), too_new (21,051), fdv_liq_thin (19,708), rug_danger (17,743)

## How it works
Six agents, one job each — **RADAR** finds new tokens · **LUNA** blocks unsafe ones (liquidity, age, RugCheck: mint/freeze
authority, LP lock, holder concentration; fails closed) · **ATLAS** reads buy/sell pressure and volume acceleration ·
**VEGA** reads attention (socials, boosts, trending) · **ORION** reads momentum · **TITAN** sizes (4–6% of equity, ≤1% of pool,
max 6 positions, −10% daily stop) · **NOVA** simulates fills (pool price impact + 1% slippage + 0.25% DEX fee + $0.30
priority fee per side). Exits: −25% stop, sell half at +40%, 20% trailing stop on the rest, 4-hour time limit,
emergency exit if liquidity drops 50%.

The **control book** buys a *random* token that passed the same safety gate every time the desk buys, same size, same exits.
If the desk can't beat random picks, the "AI" adds nothing.

Files: `data/trades.csv` (every closed trade) · `data/equity.csv` (5-minute equity) · `data/state.json` (open positions).
