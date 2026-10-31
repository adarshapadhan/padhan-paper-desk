# Padhan Paper Desk — live scorecard

> **Paper trading only.** No wallet, no keys, no real money. Every trade is simulated on live Solana prices
> with realistic fees, slippage and rug-pull losses. Updated 2026-10-31 10:36 UTC · day 22.0

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
| Equity | $98.59 | $510.93 |
| Return | -90.14% | -48.91% |
| Closed trades | 370 | 206 |
| Win rate | 34.6% | 27.7% |
| Avg win / avg loss | +29.5% / -37.3% | +27.9% / -30.3% |
| Profit factor | 0.48 | 0.4 |
| Max drawdown | 90.5% | 48.9% |
| Profit without top 3 trades | $-983.15 | $-554.72 |
| Rug / liquidity-pull exits | 24 | 13 |
| Open positions now | 0 | 0 |

Tokens screened: **2,596,697** across 31,315 scans. Top reasons the safety agent (LUNA) said no:
dex (1,029,396), liq_low (650,754), too_old (365,270), odd_quote (284,744), lp_unlocked (30,414), too_new (16,614), titan_daily_loss_stop (15,394), rug_danger (15,053)

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
