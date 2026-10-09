"""Offline end-to-end test: a fake Solana meme-coin market drives the desk for 8 simulated hours."""
import json
import math
import os
import random
import shutil
import sys
import tempfile
import urllib.error

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "desk"))
import desk  # noqa: E402

T0 = 1_790_000_000.0


class Market:
    def __init__(self, seed=7):
        self.r = random.Random(seed)
        self.t = T0
        self.tokens = {}
        self.n = 0
        for _ in range(40):
            self.spawn(age_min=self.r.uniform(5, 3000))

    def spawn(self, age_min=0.0):
        self.n += 1
        mint = f"Mint{self.n:04d}pump"
        kind = self.r.choices(["rug", "pump", "drift", "dump"], [0.25, 0.2, 0.4, 0.15])[0]
        self.tokens[mint] = {
            "kind": kind, "price": self.r.uniform(1e-5, 1e-2), "liq": self.r.uniform(10_000, 400_000),
            "created": self.t - age_min * 60, "dex": self.r.choice(["raydium", "pumpswap", "pumpfun", "meteora"]),
            "danger": self.r.random() < 0.3, "lp": self.r.choice([100, 100, 95, 40, None]),
            "rug_at": self.t + self.r.uniform(600, 6 * 3600), "boost": self.r.random() < 0.3,
            "m5": 0.0, "h1": 0.0, "hist": [],
        }

    def step(self, dt):
        self.t += dt
        if self.r.random() < dt / 300:
            self.spawn()
        for m, k in self.tokens.items():
            mu = {"pump": 0.00003, "drift": -0.000005, "dump": -0.00004, "rug": 0.00001, "dead": -0.0002}[k["kind"]] * dt
            k["price"] *= math.exp(mu + self.r.gauss(0, 0.004 * math.sqrt(dt)))
            if k["kind"] == "rug" and self.t > k["rug_at"]:
                k["liq"] = max(200.0, k["liq"] * 0.02)
                k["price"] *= 0.05
                k["kind"] = "dead"
            k["hist"].append((self.t, k["price"]))
            k["hist"] = [h for h in k["hist"] if self.t - h[0] <= 3600]

    def chg(self, k, sec):
        old = [p for t, p in k["hist"] if self.t - t >= sec - 30]
        base = old[-1] if old else k["hist"][0][1]
        return (k["price"] / base - 1) * 100

    def pair(self, m):
        k = self.tokens[m]
        b = self.r.randint(5, 80)
        s = self.r.randint(5, 70)
        return {
            "chainId": "solana", "dexId": k["dex"], "url": "https://dexscreener.com/solana/" + m,
            "pairAddress": "P" + m, "baseToken": {"address": m, "symbol": m[:8]},
            "priceUsd": str(k["price"]), "liquidity": {"usd": k["liq"]},
            "fdv": k["liq"] * self.r.uniform(2, 30), "pairCreatedAt": int(k["created"] * 1000),
            "txns": {"m5": {"buys": b, "sells": s}},
            "volume": {"m5": self.r.uniform(1e3, 3e4), "h1": self.r.uniform(1e4, 2e5)},
            "priceChange": {"m5": round(self.chg(k, 300), 2), "h1": round(self.chg(k, 3600), 2)},
            "info": {"socials": [{"type": "twitter"}] if self.r.random() < 0.6 else [], "websites": [1]},
            "boosts": {"active": 1 if k["boost"] else 0},
        }

    def fetch(self, url, headers=None):
        if self.r.random() < 0.02:
            raise urllib.error.URLError("flaky")
        if "/token-profiles/" in url or "/token-boosts/" in url:
            ms = self.r.sample(list(self.tokens), 15)
            return [{"chainId": "solana", "tokenAddress": m} for m in ms] + [{"chainId": "base", "tokenAddress": "0xabc"}]
        if "geckoterminal" in url:
            ms = self.r.sample(list(self.tokens), 10)
            return {"data": [{"relationships": {"base_token": {"data": {"id": "solana_" + m}}}} for m in ms]}
        if "/tokens/v1/solana/" in url:
            ms = url.rsplit("/", 1)[1].split(",")
            out = []
            for m in ms:
                if m in self.tokens and not (self.tokens[m]["kind"] == "dead" and self.r.random() < 0.5):
                    out.append(self.pair(m))
            return out
        if "rugcheck" in url:
            m = url.split("/tokens/")[1].split("/")[0]
            k = self.tokens.get(m)
            if not k:
                raise urllib.error.HTTPError(url, 404, "nf", {}, None)
            risks = [{"name": "Mint Authority still enabled", "level": "danger"}] if k["danger"] else \
                [{"name": "Low amount of LP Providers", "level": "warn"}]
            # rug tokens look clean on rugcheck half the time — realistic
            return {"risks": risks, "lpLockedPct": k["lp"], "score": 500}
        raise AssertionError("unexpected url " + url)


def main():
    mk = Market()
    d = tempfile.mkdtemp()
    desk.FETCH = mk.fetch
    desk.NOW = lambda: mk.t
    desk.SLEEP = lambda s: mk.step(s)
    desk.run(d, minutes=8 * 60, seed=1)

    st = json.load(open(os.path.join(d, "state.json")))
    trades = open(os.path.join(d, "trades.csv")).read().strip().splitlines()
    eq = open(os.path.join(d, "equity.csv")).read().strip().splitlines()
    print("\n--- RESULT ---")
    print("trades closed:", len(trades) - 1, "| equity rows:", len(eq) - 1)
    for name, b in st["books"].items():
        print(name, "cash", round(b["cash"], 2), "open", len(b["positions"]), "trades", b["trades"],
              "realized", round(b["realized"], 2), "maxDD", round(b["max_dd"] * 100, 1), "%")
    print("rejections:", st["stats"]["rejections"])
    reasons = {}
    for line in trades[1:]:
        r = line.split(",")[11]
        reasons[r] = reasons.get(r, 0) + 1
    print("exit reasons:", reasons)

    # invariants
    assert len(trades) > 5, "desk should have traded"
    for b in st["books"].values():
        assert b["cash"] >= -1e-6, "cash went negative"
        basis = sum(p["cost"] - p["proceeds"] for p in b["positions"].values())
        assert abs(b["cash"] + basis - (desk.CFG["start_cash"] + b["realized"])) < 1e-6, "accounting mismatch"
        assert len(b["positions"]) <= desk.CFG["max_positions"]
    # no token that failed rugcheck danger may ever be bought
    bought = {line.split(",")[1] for line in trades[1:]}
    for b in st["books"].values():
        bought |= set(b["positions"])
    bad = [m for m in bought if mk.tokens[m]["danger"] or mk.tokens[m]["dex"] == "pumpfun"
           or (mk.tokens[m]["lp"] is not None and mk.tokens[m]["lp"] < 80)]
    assert not bad, f"safety gate leaked: {bad}"
    # cost model sanity: a round trip at flat price must lose money
    q, _, cost = desk.fill_buy(1.0, 40, 100_000)
    back = desk.fill_sell(1.0, q, 100_000)
    rt = (back / cost - 1) * 100
    print(f"round-trip cost at flat price on $40 / $100k pool: {rt:.2f}%")
    assert -8 < rt < -2
    # state reload keeps running
    desk.run(d, minutes=30, seed=2)
    print("restart from saved state: OK")
    shutil.rmtree(d)
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
