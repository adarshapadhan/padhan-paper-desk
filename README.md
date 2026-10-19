# Padhan Paper Desk — live scorecard

> **Paper trading only.** No wallet, no keys, no real money. Every trade is simulated on live Solana prices
> with realistic fees, slippage and rug-pull losses. Updated 2026-10-19 10:35 UTC · day 10.0

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
| Equity | $328.60 | $645.39 |
| Return | -67.14% | -35.46% |
| Closed trades | 220 | 116 |
| Win rate | 37.3% | 27.6% |
| Avg win / avg loss | +32.1% / -37.5% | +32.1% / -28.2% |
| Profit factor | 0.52 | 0.43 |
| Max drawdown | 67.6% | 35.9% |
| Profit without top 3 trades | $-744.72 | $-420.45 |
| Rug / liquidity-pull exits | 12 | 6 |
| Open positions now | 6 | 5 |

Tokens screened: **1,182,920** across 14,246 scans. Top reasons the safety agent (LUNA) said no:
dex (484,584), liq_low (314,401), too_old (164,040), odd_quote (106,487), lp_unlocked (20,367), too_new (7,529), rugcheck_unavailable (6,175), titan_daily_loss_stop (6,161)

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
