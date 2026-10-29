# Padhan Paper Desk — live scorecard

> **Paper trading only.** No wallet, no keys, no real money. Every trade is simulated on live Solana prices
> with realistic fees, slippage and rug-pull losses. Updated 2026-10-29 23:56 UTC · day 20.6

## Verdict: **DO NOT INVEST — failed: profit, pf, dd, edge, luck**

| | Invest only if ALL of these hold (rules fixed before the test started) |
|---|---|
| ✅ | At least 14 days live and 100 closed desk trades |
| ❌ | Desk is net profitable after all fees, slippage and rugs |
| ❌ | Profit factor (gross wins / gross losses) is 1.3 or better |
| ❌ | Worst peak-to-trough drawdown is 30% or less |
| ❌ | Desk beats the random control book by 10+ percentage points |
| ❌ | Still profitable after removing its 3 best trades |

## Books (each started with $1,000 paper)

| | AI desk | Random control |
|---|---:|---:|
| Equity | $102.36 | $518.10 |
| Return | -89.76% | -48.19% |
| Closed trades | 363 | 199 |
| Win rate | 34.4% | 28.1% |
| Avg win / avg loss | +29.8% / -37.4% | +27.6% / -30.3% |
| Profit factor | 0.48 | 0.4 |
| Max drawdown | 89.9% | 48.8% |
| Profit without top 3 trades | $-979.37 | $-547.55 |
| Rug / liquidity-pull exits | 24 | 13 |
| Open positions now | 0 | 0 |

Tokens screened: **2,418,948** across 29,275 scans. Top reasons the safety agent (LUNA) said no:
dex (958,740), liq_low (609,545), too_old (339,468), odd_quote (262,190), lp_unlocked (29,464), too_new (15,553), titan_daily_loss_stop (15,390), rug_danger (14,889)

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
