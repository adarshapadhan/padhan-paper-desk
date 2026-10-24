# Padhan Paper Desk — live scorecard

> **Paper trading only.** No wallet, no keys, no real money. Every trade is simulated on live Solana prices
> with realistic fees, slippage and rug-pull losses. Updated 2026-10-24 02:37 UTC · day 14.7

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
| Equity | $166.43 | $549.40 |
| Return | -83.36% | -45.06% |
| Closed trades | 300 | 155 |
| Win rate | 34.3% | 26.5% |
| Avg win / avg loss | +31.3% / -37.3% | +30.2% / -30.3% |
| Profit factor | 0.49 | 0.4 |
| Max drawdown | 83.4% | 45.2% |
| Profit without top 3 trades | $-915.28 | $-512.77 |
| Rug / liquidity-pull exits | 22 | 12 |
| Open positions now | 2 | 5 |

Tokens screened: **1,721,433** across 20,891 scans. Top reasons the safety agent (LUNA) said no:
dex (693,820), liq_low (435,413), too_old (248,808), odd_quote (176,298), lp_unlocked (24,663), too_new (11,060), fdv_liq_thin (9,956), titan_daily_loss_stop (9,880)

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
