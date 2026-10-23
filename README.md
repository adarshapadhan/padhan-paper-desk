# Padhan Paper Desk — live scorecard

> **Paper trading only.** No wallet, no keys, no real money. Every trade is simulated on live Solana prices
> with realistic fees, slippage and rug-pull losses. Updated 2026-10-23 08:26 UTC · day 13.9

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
| Equity | $196.56 | $561.33 |
| Return | -80.34% | -43.87% |
| Closed trades | 286 | 152 |
| Win rate | 35.0% | 26.3% |
| Avg win / avg loss | +31.7% / -37.2% | +30.6% / -29.7% |
| Profit factor | 0.49 | 0.4 |
| Max drawdown | 81.2% | 44.1% |
| Profit without top 3 trades | $-885.24 | $-504.29 |
| Rug / liquidity-pull exits | 21 | 11 |
| Open positions now | 0 | 0 |

Tokens screened: **1,637,942** across 19,811 scans. Top reasons the safety agent (LUNA) said no:
dex (664,842), liq_low (416,023), too_old (235,604), odd_quote (166,746), lp_unlocked (23,492), too_new (10,472), fdv_liq_thin (9,818), titan_daily_loss_stop (9,188)

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
