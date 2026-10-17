# Padhan Paper Desk — live scorecard

> **Paper trading only.** No wallet, no keys, no real money. Every trade is simulated on live Solana prices
> with realistic fees, slippage and rug-pull losses. Updated 2026-10-17 02:48 UTC · day 7.7

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
| Equity | $359.31 | $650.41 |
| Return | -64.07% | -34.96% |
| Closed trades | 211 | 107 |
| Win rate | 37.4% | 28.0% |
| Avg win / avg loss | +31.9% / -37.1% | +32.6% / -29.4% |
| Profit factor | 0.53 | 0.43 |
| Max drawdown | 64.1% | 35.0% |
| Profit without top 3 trades | $-717.90 | $-411.75 |
| Rug / liquidity-pull exits | 10 | 6 |
| Open positions now | 2 | 2 |

Tokens screened: **888,424** across 10,934 scans. Top reasons the safety agent (LUNA) said no:
dex (374,425), liq_low (238,094), too_old (123,472), odd_quote (75,605), lp_unlocked (15,990), too_new (5,831), titan_daily_loss_stop (4,162), fdv_liq_thin (4,152)

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
