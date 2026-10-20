# Padhan Paper Desk — live scorecard

> **Paper trading only.** No wallet, no keys, no real money. Every trade is simulated on live Solana prices
> with realistic fees, slippage and rug-pull losses. Updated 2026-10-20 08:05 UTC · day 10.9

## Verdict: **TOO EARLY — keep watching**

| | Invest only if ALL of these hold (rules fixed before the test started) |
|---|---|
| ❌ | At least 14 days live and 100 closed desk trades |
| ❌ | Desk is net profitable after all fees, slippage and rugs |
| ❌ | Profit factor (gross wins / gross losses) is 1.3 or better |
| ❌ | Worst peak-to-trough drawdown is 30% or less |
| ❌ | Desk beats the random control book by 10+ percentage points |
| ❌ | Still profitable after removing its 3 best trades |

## Books (each started with $1,000 paper)

| | AI desk | Random control |
|---|---:|---:|
| Equity | $276.38 | $630.12 |
| Return | -72.36% | -36.99% |
| Closed trades | 246 | 132 |
| Win rate | 36.2% | 28.8% |
| Avg win / avg loss | +31.5% / -37.0% | +31.0% / -27.8% |
| Profit factor | 0.51 | 0.44 |
| Max drawdown | 72.5% | 37.2% |
| Profit without top 3 trades | $-805.34 | $-435.52 |
| Rug / liquidity-pull exits | 13 | 7 |
| Open positions now | 0 | 0 |

Tokens screened: **1,279,092** across 15,521 scans. Top reasons the safety agent (LUNA) said no:
dex (526,596), liq_low (338,292), too_old (175,994), odd_quote (118,594), lp_unlocked (21,606), too_new (8,191), titan_daily_loss_stop (6,657), fdv_liq_thin (6,437)

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
