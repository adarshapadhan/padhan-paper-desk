# Padhan Paper Desk — live scorecard

> **Paper trading only.** No wallet, no keys, no real money. Every trade is simulated on live Solana prices
> with realistic fees, slippage and rug-pull losses. Updated 2026-10-27 07:16 UTC · day 17.9

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
| Equity | $127.23 | $539.77 |
| Return | -87.28% | -46.02% |
| Closed trades | 338 | 178 |
| Win rate | 35.2% | 27.0% |
| Avg win / avg loss | +29.9% / -37.9% | +30.1% / -29.5% |
| Profit factor | 0.48 | 0.4 |
| Max drawdown | 87.5% | 46.7% |
| Profit without top 3 trades | $-954.52 | $-526.91 |
| Rug / liquidity-pull exits | 24 | 12 |
| Open positions now | 0 | 1 |

Tokens screened: **2,107,701** across 25,436 scans. Top reasons the safety agent (LUNA) said no:
dex (843,458), liq_low (530,155), too_old (300,102), odd_quote (226,595), lp_unlocked (26,957), rug_danger (13,772), too_new (13,572), titan_daily_loss_stop (12,966)

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
