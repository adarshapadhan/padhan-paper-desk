# Padhan Paper Desk — live scorecard

> **Paper trading only.** No wallet, no keys, no real money. Every trade is simulated on live Solana prices
> with realistic fees, slippage and rug-pull losses. Updated 2026-10-22 06:09 UTC · day 12.8

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
| Equity | $207.49 | $589.21 |
| Return | -79.25% | -41.08% |
| Closed trades | 268 | 143 |
| Win rate | 35.1% | 27.3% |
| Avg win / avg loss | +31.7% / -38.0% | +30.6% / -28.8% |
| Profit factor | 0.49 | 0.42 |
| Max drawdown | 79.3% | 41.1% |
| Profit without top 3 trades | $-874.21 | $-476.42 |
| Rug / liquidity-pull exits | 18 | 9 |
| Open positions now | 0 | 0 |

Tokens screened: **1,511,889** across 18,251 scans. Top reasons the safety agent (LUNA) said no:
dex (617,732), liq_low (389,858), too_old (215,287), odd_quote (150,690), lp_unlocked (22,714), too_new (9,716), titan_daily_loss_stop (8,353), fdv_liq_thin (8,258)

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
