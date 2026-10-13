# Padhan Paper Desk — live scorecard

> **Paper trading only.** No wallet, no keys, no real money. Every trade is simulated on live Solana prices
> with realistic fees, slippage and rug-pull losses. Updated 2026-10-13 14:41 UTC · day 4.2

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
| Equity | $648.85 | $804.89 |
| Return | -35.11% | -19.51% |
| Closed trades | 113 | 57 |
| Win rate | 39.8% | 33.3% |
| Avg win / avg loss | +34.3% / -36.9% | +29.7% / -30.1% |
| Profit factor | 0.59 | 0.48 |
| Max drawdown | 39.4% | 22.3% |
| Profit without top 3 trades | $-424.09 | $-255.00 |
| Rug / liquidity-pull exits | 5 | 3 |
| Open positions now | 3 | 3 |

Tokens screened: **486,507** across 5,939 scans. Top reasons the safety agent (LUNA) said no:
dex (199,108), liq_low (139,240), too_old (62,547), odd_quote (40,633), lp_unlocked (8,672), too_new (3,315), titan_daily_loss_stop (2,379), rug_danger (1,864)

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
