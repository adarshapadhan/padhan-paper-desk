# Padhan Paper Desk — live scorecard

> **Paper trading only.** No wallet, no keys, no real money. Every trade is simulated on live Solana prices
> with realistic fees, slippage and rug-pull losses. Updated 2026-10-12 05:19 UTC · day 2.8

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
| Equity | $673.65 | $841.74 |
| Return | -32.64% | -15.83% |
| Closed trades | 73 | 37 |
| Win rate | 34.2% | 29.7% |
| Avg win / avg loss | +35.7% / -37.4% | +25.9% / -27.4% |
| Profit factor | 0.49 | 0.39 |
| Max drawdown | 32.7% | 18.0% |
| Profit without top 3 trades | $-406.01 | $-198.71 |
| Rug / liquidity-pull exits | 4 | 1 |
| Open positions now | 0 | 3 |

Tokens screened: **323,966** across 3,959 scans. Top reasons the safety agent (LUNA) said no:
dex (130,901), liq_low (92,064), too_old (42,214), odd_quote (27,629), lp_unlocked (5,303), too_new (2,117), titan_daily_loss_stop (1,828), fdv_low (774)

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
