# Padhan Paper Desk — live scorecard

> **Paper trading only.** No wallet, no keys, no real money. Every trade is simulated on live Solana prices
> with realistic fees, slippage and rug-pull losses. Updated 2026-10-09 14:50 UTC · day 0.2

## Verdict: **TOO EARLY — keep watching**

| | Invest only if ALL of these hold (rules fixed before the test started) |
|---|---|
| ❌ | At least 14 days live and 100 closed desk trades |
| ❌ | Desk is net profitable after all fees, slippage and rugs |
| ❌ | Profit factor (gross wins / gross losses) is 1.3 or better |
| ✅ | Worst peak-to-trough drawdown is 30% or less |
| ❌ | Desk beats the random control book by 10+ percentage points |
| ❌ | Still profitable after removing its 3 best trades |

## Books (each started with $1,000 paper)

| | AI desk | Random control |
|---|---:|---:|
| Equity | $890.74 | $961.17 |
| Return | -10.93% | -3.88% |
| Closed trades | 16 | 8 |
| Win rate | 43.8% | 25.0% |
| Avg win / avg loss | +29.7% / -48.8% | +41.0% / -29.4% |
| Profit factor | 0.46 | 0.45 |
| Max drawdown | 10.9% | 4.2% |
| Profit without top 3 trades | $-146.33 | $-59.98 |
| Rug / liquidity-pull exits | 2 | 0 |
| Open positions now | 1 | 1 |

Tokens screened: **21,767** across 284 scans. Top reasons the safety agent (LUNA) said no:
dex (8,631), liq_low (8,045), too_old (2,582), odd_quote (2,093), too_new (94), rug_danger (75), fdv_low (9), titan_daily_loss_stop (5)

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
