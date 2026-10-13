# Padhan Paper Desk — live scorecard

> **Paper trading only.** No wallet, no keys, no real money. Every trade is simulated on live Solana prices
> with realistic fees, slippage and rug-pull losses. Updated 2026-10-13 19:27 UTC · day 4.4

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
| Equity | $568.06 | $773.40 |
| Return | -43.19% | -22.66% |
| Closed trades | 125 | 63 |
| Win rate | 37.6% | 31.7% |
| Avg win / avg loss | +33.7% / -37.3% | +29.5% / -29.9% |
| Profit factor | 0.54 | 0.45 |
| Max drawdown | 43.2% | 22.7% |
| Profit without top 3 trades | $-515.34 | $-286.10 |
| Rug / liquidity-pull exits | 7 | 3 |
| Open positions now | 0 | 1 |

Tokens screened: **508,558** across 6,224 scans. Top reasons the safety agent (LUNA) said no:
dex (207,633), liq_low (145,265), too_old (66,206), odd_quote (42,617), lp_unlocked (9,333), too_new (3,471), titan_daily_loss_stop (2,410), rug_danger (2,152)

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
