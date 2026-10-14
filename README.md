# Padhan Paper Desk — live scorecard

> **Paper trading only.** No wallet, no keys, no real money. Every trade is simulated on live Solana prices
> with realistic fees, slippage and rug-pull losses. Updated 2026-10-14 01:47 UTC · day 4.7

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
| Equity | $571.13 | $747.67 |
| Return | -42.89% | -25.23% |
| Closed trades | 128 | 66 |
| Win rate | 38.3% | 30.3% |
| Avg win / avg loss | +33.2% / -37.3% | +29.5% / -30.1% |
| Profit factor | 0.55 | 0.43 |
| Max drawdown | 44.3% | 25.3% |
| Profit without top 3 trades | $-513.39 | $-309.48 |
| Rug / liquidity-pull exits | 7 | 3 |
| Open positions now | 6 | 3 |

Tokens screened: **540,846** across 6,599 scans. Top reasons the safety agent (LUNA) said no:
dex (220,065), liq_low (155,080), too_old (70,378), odd_quote (44,676), lp_unlocked (10,129), too_new (3,661), fdv_liq_thin (2,703), rug_danger (2,605)

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
