# Padhan Paper Desk — live scorecard

> **Paper trading only.** No wallet, no keys, no real money. Every trade is simulated on live Solana prices
> with realistic fees, slippage and rug-pull losses. Updated 2026-11-03 07:12 UTC · day 24.9

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
| Equity | $92.97 | $499.54 |
| Return | -90.70% | -50.05% |
| Closed trades | 381 | 217 |
| Win rate | 35.2% | 27.6% |
| Avg win / avg loss | +29.0% / -37.4% | +26.8% / -30.2% |
| Profit factor | 0.48 | 0.39 |
| Max drawdown | 90.9% | 50.1% |
| Profit without top 3 trades | $-987.44 | $-565.15 |
| Rug / liquidity-pull exits | 24 | 13 |
| Open positions now | 1 | 1 |

Tokens screened: **2,931,392** across 35,375 scans. Top reasons the safety agent (LUNA) said no:
dex (1,168,647), liq_low (723,337), too_old (409,217), odd_quote (323,428), lp_unlocked (31,604), too_new (19,167), fdv_liq_thin (17,911), rug_danger (16,816)

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
