# Padhan Paper Desk — live scorecard

> **Paper trading only.** No wallet, no keys, no real money. Every trade is simulated on live Solana prices
> with realistic fees, slippage and rug-pull losses. Updated 2026-10-17 01:33 UTC · day 7.6

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
| Equity | $370.82 | $651.72 |
| Return | -62.92% | -34.83% |
| Closed trades | 209 | 106 |
| Win rate | 37.3% | 28.3% |
| Avg win / avg loss | +32.0% / -37.1% | +32.6% / -29.4% |
| Profit factor | 0.53 | 0.44 |
| Max drawdown | 63.8% | 34.9% |
| Profit without top 3 trades | $-715.85 | $-406.76 |
| Rug / liquidity-pull exits | 10 | 6 |
| Open positions now | 4 | 3 |

Tokens screened: **881,937** across 10,859 scans. Top reasons the safety agent (LUNA) said no:
dex (371,873), liq_low (236,374), too_old (122,470), odd_quote (74,813), lp_unlocked (15,840), too_new (5,782), fdv_liq_thin (4,152), titan_daily_loss_stop (4,120)

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
