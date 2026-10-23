# Padhan Paper Desk — live scorecard

> **Paper trading only.** No wallet, no keys, no real money. Every trade is simulated on live Solana prices
> with realistic fees, slippage and rug-pull losses. Updated 2026-10-23 01:06 UTC · day 13.6

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
| Equity | $198.62 | $571.49 |
| Return | -80.14% | -42.85% |
| Closed trades | 272 | 145 |
| Win rate | 35.3% | 26.9% |
| Avg win / avg loss | +31.3% / -38.3% | +30.6% / -29.5% |
| Profit factor | 0.49 | 0.41 |
| Max drawdown | 80.5% | 42.9% |
| Profit without top 3 trades | $-883.29 | $-489.84 |
| Rug / liquidity-pull exits | 19 | 10 |
| Open positions now | 5 | 5 |

Tokens screened: **1,609,184** across 19,376 scans. Top reasons the safety agent (LUNA) said no:
dex (653,419), liq_low (409,267), too_old (230,429), odd_quote (162,958), lp_unlocked (23,466), too_new (10,279), fdv_liq_thin (9,813), titan_daily_loss_stop (9,188)

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
