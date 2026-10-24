# Padhan Paper Desk — live scorecard

> **Paper trading only.** No wallet, no keys, no real money. Every trade is simulated on live Solana prices
> with realistic fees, slippage and rug-pull losses. Updated 2026-10-24 17:01 UTC · day 15.3

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
| Equity | $167.85 | $543.00 |
| Return | -83.21% | -45.70% |
| Closed trades | 302 | 160 |
| Win rate | 34.4% | 25.6% |
| Avg win / avg loss | +31.2% / -37.1% | +30.2% / -30.0% |
| Profit factor | 0.49 | 0.4 |
| Max drawdown | 83.4% | 45.7% |
| Profit without top 3 trades | $-913.87 | $-522.64 |
| Rug / liquidity-pull exits | 22 | 12 |
| Open positions now | 0 | 0 |

Tokens screened: **1,787,245** across 21,746 scans. Top reasons the safety agent (LUNA) said no:
dex (719,782), liq_low (450,115), too_old (258,795), odd_quote (182,813), lp_unlocked (25,030), too_new (11,595), titan_daily_loss_stop (10,612), rug_danger (10,181)

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
