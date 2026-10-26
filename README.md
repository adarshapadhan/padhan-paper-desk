# Padhan Paper Desk — live scorecard

> **Paper trading only.** No wallet, no keys, no real money. Every trade is simulated on live Solana prices
> with realistic fees, slippage and rug-pull losses. Updated 2026-10-26 01:25 UTC · day 16.6

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
| Equity | $141.51 | $538.17 |
| Return | -85.85% | -46.18% |
| Closed trades | 319 | 170 |
| Win rate | 34.5% | 26.5% |
| Avg win / avg loss | +30.7% / -37.8% | +30.1% / -29.8% |
| Profit factor | 0.48 | 0.4 |
| Max drawdown | 86.7% | 46.7% |
| Profit without top 3 trades | $-942.80 | $-525.22 |
| Rug / liquidity-pull exits | 24 | 12 |
| Open positions now | 4 | 3 |

Tokens screened: **1,957,211** across 23,666 scans. Top reasons the safety agent (LUNA) said no:
dex (788,079), liq_low (492,332), too_old (280,093), odd_quote (204,514), lp_unlocked (26,271), too_new (12,658), titan_daily_loss_stop (11,838), rug_danger (10,656)

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
