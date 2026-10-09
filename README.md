# Padhan Paper Desk — live scorecard

> **Paper trading only.** No wallet, no keys, no real money. Every trade is simulated on live Solana prices
> with realistic fees, slippage and rug-pull losses. Updated 2026-10-09 19:08 UTC · day 0.4

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
| Equity | $896.34 | $960.24 |
| Return | -10.37% | -3.98% |
| Closed trades | 17 | 9 |
| Win rate | 41.2% | 22.2% |
| Avg win / avg loss | +29.7% / -44.5% | +41.0% / -25.7% |
| Profit factor | 0.45 | 0.44 |
| Max drawdown | 11.1% | 4.2% |
| Profit without top 3 trades | $-148.62 | $-70.01 |
| Rug / liquidity-pull exits | 2 | 0 |
| Open positions now | 0 | 0 |

Tokens screened: **40,727** across 524 scans. Top reasons the safety agent (LUNA) said no:
dex (16,309), liq_low (13,509), too_old (5,154), odd_quote (4,219), rug_danger (266), too_new (217), titan_daily_loss_stop (160), lp_unlocked (34)

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
