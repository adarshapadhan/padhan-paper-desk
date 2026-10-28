# Padhan Paper Desk — live scorecard

> **Paper trading only.** No wallet, no keys, no real money. Every trade is simulated on live Solana prices
> with realistic fees, slippage and rug-pull losses. Updated 2026-10-28 01:57 UTC · day 18.7

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
| Equity | $117.94 | $525.45 |
| Return | -88.21% | -47.45% |
| Closed trades | 344 | 184 |
| Win rate | 35.2% | 27.7% |
| Avg win / avg loss | +29.7% / -37.7% | +28.8% / -30.2% |
| Profit factor | 0.48 | 0.4 |
| Max drawdown | 88.2% | 47.5% |
| Profit without top 3 trades | $-959.42 | $-535.56 |
| Rug / liquidity-pull exits | 24 | 13 |
| Open positions now | 6 | 4 |

Tokens screened: **2,205,033** across 26,545 scans. Top reasons the safety agent (LUNA) said no:
dex (878,837), liq_low (554,049), too_old (313,481), odd_quote (238,022), lp_unlocked (27,871), rug_danger (14,251), too_new (14,125), titan_daily_loss_stop (13,713)

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
