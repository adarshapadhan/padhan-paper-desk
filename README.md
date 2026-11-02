# Padhan Paper Desk — live scorecard

> **Paper trading only.** No wallet, no keys, no real money. Every trade is simulated on live Solana prices
> with realistic fees, slippage and rug-pull losses. Updated 2026-11-02 05:37 UTC · day 23.8

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
| Equity | $91.77 | $502.17 |
| Return | -90.82% | -49.78% |
| Closed trades | 378 | 214 |
| Win rate | 34.9% | 27.6% |
| Avg win / avg loss | +29.0% / -37.4% | +27.2% / -30.2% |
| Profit factor | 0.48 | 0.39 |
| Max drawdown | 90.8% | 49.8% |
| Profit without top 3 trades | $-988.97 | $-562.61 |
| Rug / liquidity-pull exits | 24 | 13 |
| Open positions now | 1 | 1 |

Tokens screened: **2,806,426** across 33,864 scans. Top reasons the safety agent (LUNA) said no:
dex (1,115,427), liq_low (694,017), too_old (394,783), odd_quote (311,730), lp_unlocked (31,039), too_new (18,213), fdv_liq_thin (16,055), rug_danger (15,487)

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
