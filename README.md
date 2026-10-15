# Padhan Paper Desk — live scorecard

> **Paper trading only.** No wallet, no keys, no real money. Every trade is simulated on live Solana prices
> with realistic fees, slippage and rug-pull losses. Updated 2026-10-15 02:16 UTC · day 5.7

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
| Equity | $464.04 | $719.41 |
| Return | -53.60% | -28.06% |
| Closed trades | 161 | 77 |
| Win rate | 36.0% | 27.3% |
| Avg win / avg loss | +33.2% / -35.8% | +32.7% / -28.8% |
| Profit factor | 0.53 | 0.43 |
| Max drawdown | 53.6% | 28.1% |
| Profit without top 3 trades | $-610.66 | $-343.19 |
| Rug / liquidity-pull exits | 7 | 3 |
| Open positions now | 3 | 5 |

Tokens screened: **652,890** across 8,054 scans. Top reasons the safety agent (LUNA) said no:
dex (270,089), liq_low (185,294), too_old (87,965), odd_quote (51,358), lp_unlocked (12,113), too_new (4,392), fdv_liq_thin (3,216), titan_daily_loss_stop (3,057)

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
