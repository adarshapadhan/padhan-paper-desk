# Padhan Paper Desk — live scorecard

> **Paper trading only.** No wallet, no keys, no real money. Every trade is simulated on live Solana prices
> with realistic fees, slippage and rug-pull losses. Updated 2026-10-28 01:26 UTC · day 18.6

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
| Equity | $121.45 | $525.69 |
| Return | -87.85% | -47.43% |
| Closed trades | 343 | 184 |
| Win rate | 35.3% | 27.7% |
| Avg win / avg loss | +29.7% / -37.7% | +28.8% / -30.2% |
| Profit factor | 0.48 | 0.4 |
| Max drawdown | 88.1% | 47.4% |
| Profit without top 3 trades | $-957.21 | $-535.56 |
| Rug / liquidity-pull exits | 24 | 13 |
| Open positions now | 6 | 4 |

Tokens screened: **2,202,737** across 26,515 scans. Top reasons the safety agent (LUNA) said no:
dex (877,837), liq_low (553,416), too_old (313,176), odd_quote (237,702), lp_unlocked (27,871), rug_danger (14,249), too_new (14,110), titan_daily_loss_stop (13,713)

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
