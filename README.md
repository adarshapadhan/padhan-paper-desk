# Padhan Paper Desk — live scorecard

> **Paper trading only.** No wallet, no keys, no real money. Every trade is simulated on live Solana prices
> with realistic fees, slippage and rug-pull losses. Updated 2026-10-11 06:51 UTC · day 1.9

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
| Equity | $718.40 | $834.82 |
| Return | -28.16% | -16.52% |
| Closed trades | 50 | 29 |
| Win rate | 36.0% | 20.7% |
| Avg win / avg loss | +30.7% / -40.3% | +26.9% / -26.9% |
| Profit factor | 0.42 | 0.27 |
| Max drawdown | 28.2% | 16.8% |
| Profit without top 3 trades | $-339.51 | $-208.15 |
| Rug / liquidity-pull exits | 4 | 1 |
| Open positions now | 0 | 0 |

Tokens screened: **214,448** across 2,624 scans. Top reasons the safety agent (LUNA) said no:
dex (84,405), liq_low (64,760), too_old (26,790), odd_quote (18,052), lp_unlocked (2,432), titan_daily_loss_stop (1,424), too_new (1,383), rug_danger (423)

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
