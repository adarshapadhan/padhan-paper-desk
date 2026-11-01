# Padhan Paper Desk — live scorecard

> **Paper trading only.** No wallet, no keys, no real money. Every trade is simulated on live Solana prices
> with realistic fees, slippage and rug-pull losses. Updated 2026-11-01 12:23 UTC · day 23.1

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
| Equity | $97.12 | $503.57 |
| Return | -90.29% | -49.64% |
| Closed trades | 376 | 212 |
| Win rate | 35.1% | 27.4% |
| Avg win / avg loss | +29.0% / -37.3% | +27.5% / -30.1% |
| Profit factor | 0.48 | 0.39 |
| Max drawdown | 90.5% | 49.6% |
| Profit without top 3 trades | $-984.11 | $-560.88 |
| Rug / liquidity-pull exits | 24 | 13 |
| Open positions now | 2 | 2 |

Tokens screened: **2,721,439** across 32,844 scans. Top reasons the safety agent (LUNA) said no:
dex (1,080,504), liq_low (675,264), too_old (383,672), odd_quote (301,911), lp_unlocked (30,845), too_new (17,680), titan_daily_loss_stop (15,394), rug_danger (15,326)

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
