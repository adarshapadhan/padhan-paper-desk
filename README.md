# Padhan Paper Desk — live scorecard

> **Paper trading only.** No wallet, no keys, no real money. Every trade is simulated on live Solana prices
> with realistic fees, slippage and rug-pull losses. Updated 2026-10-12 19:14 UTC · day 3.4

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
| Equity | $632.29 | $858.55 |
| Return | -36.77% | -14.15% |
| Closed trades | 85 | 43 |
| Win rate | 34.1% | 32.6% |
| Avg win / avg loss | +36.5% / -37.6% | +28.6% / -27.2% |
| Profit factor | 0.5 | 0.48 |
| Max drawdown | 36.8% | 18.0% |
| Profit without top 3 trades | $-449.40 | $-196.90 |
| Rug / liquidity-pull exits | 5 | 1 |
| Open positions now | 0 | 0 |

Tokens screened: **389,933** across 4,784 scans. Top reasons the safety agent (LUNA) said no:
dex (160,495), liq_low (108,642), too_old (50,406), odd_quote (33,862), lp_unlocked (6,756), too_new (2,643), titan_daily_loss_stop (2,110), fdv_low (1,204)

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
