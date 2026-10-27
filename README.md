# Padhan Paper Desk — live scorecard

> **Paper trading only.** No wallet, no keys, no real money. Every trade is simulated on live Solana prices
> with realistic fees, slippage and rug-pull losses. Updated 2026-10-27 12:04 UTC · day 18.1

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
| Equity | $127.23 | $539.51 |
| Return | -87.28% | -46.05% |
| Closed trades | 338 | 179 |
| Win rate | 35.2% | 27.4% |
| Avg win / avg loss | +29.9% / -37.9% | +29.7% / -29.5% |
| Profit factor | 0.48 | 0.4 |
| Max drawdown | 87.5% | 46.7% |
| Profit without top 3 trades | $-954.52 | $-526.14 |
| Rug / liquidity-pull exits | 24 | 12 |
| Open positions now | 0 | 0 |

Tokens screened: **2,130,223** across 25,721 scans. Top reasons the safety agent (LUNA) said no:
dex (851,136), liq_low (536,026), too_old (304,245), odd_quote (229,903), lp_unlocked (27,014), rug_danger (14,057), too_new (13,715), titan_daily_loss_stop (13,037)

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
