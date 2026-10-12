# Padhan Paper Desk — live scorecard

> **Paper trading only.** No wallet, no keys, no real money. Every trade is simulated on live Solana prices
> with realistic fees, slippage and rug-pull losses. Updated 2026-10-12 02:48 UTC · day 2.7

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
| Equity | $689.55 | $844.59 |
| Return | -31.05% | -15.54% |
| Closed trades | 65 | 35 |
| Win rate | 33.8% | 25.7% |
| Avg win / avg loss | +37.0% / -38.5% | +27.1% / -27.4% |
| Profit factor | 0.48 | 0.34 |
| Max drawdown | 32.7% | 18.0% |
| Profit without top 3 trades | $-389.28 | $-211.77 |
| Rug / liquidity-pull exits | 4 | 1 |
| Open positions now | 4 | 3 |

Tokens screened: **312,574** across 3,809 scans. Top reasons the safety agent (LUNA) said no:
dex (125,085), liq_low (89,180), too_old (40,981), odd_quote (26,770), lp_unlocked (4,991), too_new (2,019), titan_daily_loss_stop (1,828), fdv_low (624)

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
