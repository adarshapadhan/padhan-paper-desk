# Padhan Paper Desk — live scorecard

> **Paper trading only.** No wallet, no keys, no real money. Every trade is simulated on live Solana prices
> with realistic fees, slippage and rug-pull losses. Updated 2026-10-18 01:16 UTC · day 8.6

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
| Equity | $326.32 | $654.82 |
| Return | -67.37% | -34.52% |
| Closed trades | 219 | 110 |
| Win rate | 37.0% | 28.2% |
| Avg win / avg loss | +31.7% / -37.5% | +32.2% / -29.2% |
| Profit factor | 0.51 | 0.43 |
| Max drawdown | 67.6% | 35.5% |
| Profit without top 3 trades | $-754.24 | $-415.88 |
| Rug / liquidity-pull exits | 12 | 6 |
| Open positions now | 1 | 5 |

Tokens screened: **1,005,183** across 12,269 scans. Top reasons the safety agent (LUNA) said no:
dex (419,872), liq_low (267,764), too_old (139,791), odd_quote (88,904), lp_unlocked (18,528), too_new (6,589), titan_daily_loss_stop (5,015), fdv_liq_thin (4,209)

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
