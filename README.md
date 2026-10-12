# Padhan Paper Desk — live scorecard

> **Paper trading only.** No wallet, no keys, no real money. Every trade is simulated on live Solana prices
> with realistic fees, slippage and rug-pull losses. Updated 2026-10-12 15:12 UTC · day 3.2

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
| Equity | $637.47 | $863.27 |
| Return | -36.25% | -13.67% |
| Closed trades | 84 | 42 |
| Win rate | 34.5% | 33.3% |
| Avg win / avg loss | +36.5% / -37.9% | +28.6% / -27.0% |
| Profit factor | 0.5 | 0.5 |
| Max drawdown | 36.5% | 18.0% |
| Profit without top 3 trades | $-443.02 | $-188.96 |
| Rug / liquidity-pull exits | 5 | 1 |
| Open positions now | 1 | 1 |

Tokens screened: **368,983** across 4,544 scans. Top reasons the safety agent (LUNA) said no:
dex (152,485), liq_low (102,806), too_old (47,808), odd_quote (32,219), lp_unlocked (6,271), too_new (2,462), titan_daily_loss_stop (1,892), fdv_low (1,204)

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
