# Padhan Paper Desk — live scorecard

> **Paper trading only.** No wallet, no keys, no real money. Every trade is simulated on live Solana prices
> with realistic fees, slippage and rug-pull losses. Updated 2026-10-24 04:38 UTC · day 14.8

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
| Equity | $167.68 | $543.63 |
| Return | -83.23% | -45.64% |
| Closed trades | 301 | 159 |
| Win rate | 34.6% | 25.8% |
| Avg win / avg loss | +31.2% / -37.3% | +30.2% / -30.0% |
| Profit factor | 0.49 | 0.4 |
| Max drawdown | 83.4% | 45.7% |
| Profit without top 3 trades | $-913.56 | $-519.99 |
| Rug / liquidity-pull exits | 22 | 12 |
| Open positions now | 1 | 1 |

Tokens screened: **1,730,002** across 21,011 scans. Top reasons the safety agent (LUNA) said no:
dex (696,730), liq_low (437,826), too_old (250,359), odd_quote (177,292), lp_unlocked (24,663), too_new (11,151), fdv_liq_thin (9,956), titan_daily_loss_stop (9,954)

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
