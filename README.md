# Padhan Paper Desk — live scorecard

> **Paper trading only.** No wallet, no keys, no real money. Every trade is simulated on live Solana prices
> with realistic fees, slippage and rug-pull losses. Updated 2026-10-10 00:12 UTC · day 0.6

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
| Equity | $896.49 | $944.07 |
| Return | -10.35% | -5.59% |
| Closed trades | 17 | 10 |
| Win rate | 41.2% | 20.0% |
| Avg win / avg loss | +29.7% / -44.5% | +41.0% / -27.1% |
| Profit factor | 0.45 | 0.37 |
| Max drawdown | 11.3% | 5.7% |
| Profit without top 3 trades | $-148.62 | $-84.18 |
| Rug / liquidity-pull exits | 2 | 0 |
| Open positions now | 6 | 4 |

Tokens screened: **67,011** across 824 scans. Top reasons the safety agent (LUNA) said no:
dex (25,473), liq_low (21,788), too_old (8,843), odd_quote (6,156), titan_daily_loss_stop (441), too_new (404), lp_unlocked (355), rug_danger (343)

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
