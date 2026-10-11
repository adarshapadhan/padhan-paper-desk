# Padhan Paper Desk — live scorecard

> **Paper trading only.** No wallet, no keys, no real money. Every trade is simulated on live Solana prices
> with realistic fees, slippage and rug-pull losses. Updated 2026-10-11 22:15 UTC · day 2.5

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
| Equity | $708.57 | $825.81 |
| Return | -29.14% | -17.42% |
| Closed trades | 54 | 30 |
| Win rate | 35.2% | 20.0% |
| Avg win / avg loss | +32.2% / -39.5% | +26.9% / -27.0% |
| Profit factor | 0.44 | 0.26 |
| Max drawdown | 29.1% | 17.4% |
| Profit without top 3 trades | $-350.04 | $-217.15 |
| Rug / liquidity-pull exits | 4 | 1 |
| Open positions now | 0 | 0 |

Tokens screened: **289,467** across 3,539 scans. Top reasons the safety agent (LUNA) said no:
dex (114,812), liq_low (83,985), too_old (37,397), odd_quote (24,728), lp_unlocked (4,386), too_new (1,860), titan_daily_loss_stop (1,748), rug_danger (492)

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
