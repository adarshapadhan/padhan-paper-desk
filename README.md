# Padhan Paper Desk — live scorecard

> **Paper trading only.** No wallet, no keys, no real money. Every trade is simulated on live Solana prices
> with realistic fees, slippage and rug-pull losses. Updated 2026-10-26 00:24 UTC · day 16.6

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
| Equity | $140.80 | $533.61 |
| Return | -85.92% | -46.64% |
| Closed trades | 315 | 167 |
| Win rate | 34.3% | 25.7% |
| Avg win / avg loss | +30.7% / -37.5% | +29.4% / -29.8% |
| Profit factor | 0.48 | 0.39 |
| Max drawdown | 85.9% | 46.7% |
| Profit without top 3 trades | $-937.11 | $-528.64 |
| Rug / liquidity-pull exits | 23 | 12 |
| Open positions now | 6 | 6 |

Tokens screened: **1,952,539** across 23,606 scans. Top reasons the safety agent (LUNA) said no:
dex (785,933), liq_low (491,035), too_old (279,613), odd_quote (204,031), lp_unlocked (26,268), too_new (12,621), titan_daily_loss_stop (11,833), rug_danger (10,536)

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
