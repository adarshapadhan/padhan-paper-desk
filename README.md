# Padhan Paper Desk — live scorecard

> **Paper trading only.** No wallet, no keys, no real money. Every trade is simulated on live Solana prices
> with realistic fees, slippage and rug-pull losses. Updated 2026-10-28 13:49 UTC · day 19.2

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
| Equity | $113.51 | $516.10 |
| Return | -88.65% | -48.39% |
| Closed trades | 357 | 193 |
| Win rate | 35.0% | 26.9% |
| Avg win / avg loss | +29.8% / -37.5% | +28.2% / -30.4% |
| Profit factor | 0.48 | 0.39 |
| Max drawdown | 88.6% | 48.5% |
| Profit without top 3 trades | $-968.23 | $-549.55 |
| Rug / liquidity-pull exits | 24 | 13 |
| Open positions now | 0 | 0 |

Tokens screened: **2,253,471** across 27,250 scans. Top reasons the safety agent (LUNA) said no:
dex (899,815), liq_low (568,092), too_old (319,141), odd_quote (243,085), lp_unlocked (28,047), too_new (14,526), rug_danger (14,508), titan_daily_loss_stop (13,779)

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
