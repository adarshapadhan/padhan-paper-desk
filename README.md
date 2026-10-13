# Padhan Paper Desk — live scorecard

> **Paper trading only.** No wallet, no keys, no real money. Every trade is simulated on live Solana prices
> with realistic fees, slippage and rug-pull losses. Updated 2026-10-13 05:34 UTC · day 3.8

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
| Equity | $646.12 | $839.44 |
| Return | -35.39% | -16.06% |
| Closed trades | 103 | 52 |
| Win rate | 38.8% | 32.7% |
| Avg win / avg loss | +33.5% / -37.2% | +27.2% / -26.6% |
| Profit factor | 0.56 | 0.49 |
| Max drawdown | 39.4% | 18.0% |
| Profit without top 3 trades | $-434.72 | $-220.00 |
| Rug / liquidity-pull exits | 5 | 1 |
| Open positions now | 1 | 0 |

Tokens screened: **445,443** across 5,399 scans. Top reasons the safety agent (LUNA) said no:
dex (182,019), liq_low (127,336), too_old (56,775), odd_quote (37,763), lp_unlocked (7,603), too_new (3,026), titan_daily_loss_stop (2,379), rug_danger (1,254)

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
