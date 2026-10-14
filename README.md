# Padhan Paper Desk — live scorecard

> **Paper trading only.** No wallet, no keys, no real money. Every trade is simulated on live Solana prices
> with realistic fees, slippage and rug-pull losses. Updated 2026-10-14 07:34 UTC · day 4.9

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
| Equity | $555.75 | $763.51 |
| Return | -44.43% | -23.65% |
| Closed trades | 143 | 70 |
| Win rate | 38.5% | 30.0% |
| Avg win / avg loss | +33.5% / -36.8% | +32.7% / -29.2% |
| Profit factor | 0.56 | 0.47 |
| Max drawdown | 46.2% | 26.2% |
| Profit without top 3 trades | $-532.18 | $-301.11 |
| Rug / liquidity-pull exits | 7 | 3 |
| Open positions now | 0 | 1 |

Tokens screened: **567,539** across 6,944 scans. Top reasons the safety agent (LUNA) said no:
dex (231,924), liq_low (162,611), too_old (73,834), odd_quote (46,981), lp_unlocked (10,483), too_new (3,835), fdv_liq_thin (3,021), rug_danger (2,941)

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
