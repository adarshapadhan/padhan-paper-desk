# Padhan Paper Desk — live scorecard

> **Paper trading only.** No wallet, no keys, no real money. Every trade is simulated on live Solana prices
> with realistic fees, slippage and rug-pull losses. Updated 2026-10-28 00:26 UTC · day 18.6

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
| Equity | $122.66 | $536.59 |
| Return | -87.73% | -46.34% |
| Closed trades | 339 | 180 |
| Win rate | 35.4% | 27.8% |
| Avg win / avg loss | +29.7% / -37.9% | +29.3% / -29.5% |
| Profit factor | 0.48 | 0.4 |
| Max drawdown | 87.8% | 46.7% |
| Profit without top 3 trades | $-954.23 | $-525.76 |
| Rug / liquidity-pull exits | 24 | 12 |
| Open positions now | 6 | 5 |

Tokens screened: **2,197,912** across 26,455 scans. Top reasons the safety agent (LUNA) said no:
dex (876,008), liq_low (552,009), too_old (312,543), odd_quote (237,072), lp_unlocked (27,815), rug_danger (14,249), too_new (14,081), titan_daily_loss_stop (13,713)

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
