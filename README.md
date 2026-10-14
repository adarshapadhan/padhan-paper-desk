# Padhan Paper Desk — live scorecard

> **Paper trading only.** No wallet, no keys, no real money. Every trade is simulated on live Solana prices
> with realistic fees, slippage and rug-pull losses. Updated 2026-10-14 12:07 UTC · day 5.1

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
| Equity | $519.62 | $742.67 |
| Return | -48.04% | -25.73% |
| Closed trades | 151 | 74 |
| Win rate | 37.7% | 28.4% |
| Avg win / avg loss | +33.2% / -36.4% | +32.7% / -28.8% |
| Profit factor | 0.55 | 0.45 |
| Max drawdown | 48.0% | 26.2% |
| Profit without top 3 trades | $-562.09 | $-322.93 |
| Rug / liquidity-pull exits | 7 | 3 |
| Open positions now | 0 | 0 |

Tokens screened: **585,311** across 7,214 scans. Top reasons the safety agent (LUNA) said no:
dex (241,007), liq_low (167,035), too_old (77,020), odd_quote (47,460), lp_unlocked (10,761), too_new (3,990), fdv_liq_thin (3,156), rug_danger (2,950)

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
