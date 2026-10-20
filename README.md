# Padhan Paper Desk — live scorecard

> **Paper trading only.** No wallet, no keys, no real money. Every trade is simulated on live Solana prices
> with realistic fees, slippage and rug-pull losses. Updated 2026-10-20 03:31 UTC · day 10.7

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
| Equity | $279.34 | $634.33 |
| Return | -72.07% | -36.57% |
| Closed trades | 244 | 129 |
| Win rate | 36.5% | 29.5% |
| Avg win / avg loss | +31.5% / -37.3% | +31.0% / -27.9% |
| Profit factor | 0.51 | 0.45 |
| Max drawdown | 72.4% | 37.2% |
| Profit without top 3 trades | $-801.94 | $-426.38 |
| Rug / liquidity-pull exits | 13 | 7 |
| Open positions now | 2 | 3 |

Tokens screened: **1,258,086** across 15,251 scans. Top reasons the safety agent (LUNA) said no:
dex (517,041), liq_low (333,765), too_old (173,586), odd_quote (115,648), lp_unlocked (21,539), too_new (8,040), titan_daily_loss_stop (6,400), fdv_liq_thin (6,296)

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
