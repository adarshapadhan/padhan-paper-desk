# Padhan Paper Desk — live scorecard

> **Paper trading only.** No wallet, no keys, no real money. Every trade is simulated on live Solana prices
> with realistic fees, slippage and rug-pull losses. Updated 2026-10-14 03:48 UTC · day 4.7

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
| Equity | $557.14 | $765.45 |
| Return | -44.29% | -23.45% |
| Closed trades | 135 | 68 |
| Win rate | 38.5% | 30.9% |
| Avg win / avg loss | +32.9% / -37.2% | +32.7% / -30.1% |
| Profit factor | 0.55 | 0.48 |
| Max drawdown | 44.6% | 26.2% |
| Profit without top 3 trades | $-526.95 | $-296.43 |
| Rug / liquidity-pull exits | 7 | 3 |
| Open positions now | 3 | 2 |

Tokens screened: **550,226** across 6,719 scans. Top reasons the safety agent (LUNA) said no:
dex (224,278), liq_low (157,587), too_old (71,609), odd_quote (45,510), lp_unlocked (10,255), too_new (3,720), fdv_liq_thin (2,810), rug_danger (2,748)

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
