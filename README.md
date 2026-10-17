# Padhan Paper Desk — live scorecard

> **Paper trading only.** No wallet, no keys, no real money. Every trade is simulated on live Solana prices
> with realistic fees, slippage and rug-pull losses. Updated 2026-10-17 01:02 UTC · day 7.6

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
| Equity | $365.61 | $665.53 |
| Return | -63.44% | -33.45% |
| Closed trades | 209 | 104 |
| Win rate | 37.3% | 27.9% |
| Avg win / avg loss | +32.0% / -37.1% | +33.2% / -29.3% |
| Profit factor | 0.53 | 0.44 |
| Max drawdown | 63.5% | 34.5% |
| Profit without top 3 trades | $-715.85 | $-404.14 |
| Rug / liquidity-pull exits | 10 | 6 |
| Open positions now | 4 | 5 |

Tokens screened: **879,304** across 10,829 scans. Top reasons the safety agent (LUNA) said no:
dex (370,842), liq_low (235,736), too_old (122,050), odd_quote (74,441), lp_unlocked (15,767), too_new (5,764), fdv_liq_thin (4,152), titan_daily_loss_stop (4,102)

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
