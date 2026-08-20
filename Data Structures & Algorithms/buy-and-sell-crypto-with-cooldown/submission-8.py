"""
states - buy, sell, wait (wait means you've sold)
cache = (idx, state)
curr_profit

- We have to start with buy, could be on any index though
- if prev_state buy -> hold/sell
- prev_state == sell: hold
- prev_state == hold: buy

for (idx, price) in enumerate(prices):
    r(idx, "buy", 0)

def r(curr_idx, op, curr_profit):
    if curr_idx >= len(prices):
        return 0

    if (curr_idx, op) in cache:
        cache[(curr_idx, op)] = max(cache[(curr_idx, op)], curr_profit)
        return cache[(curr_idx, op)]

    cache[(curr_idx, op)] = 0

    if op == "buy":
        cache[(curr_idx, op)] = max(
            r(curr_idx+1, "sell", curr_profit-prices[curr_idx]),
            r(curr_idx+1, "hold", curr_profit-prices[curr_idx]),
        )
    elif op == "hold":
        cache[(curr_idx, op)] = max(
            r(curr_idx+1, "buy", curr_profit),
            r(curr_idx+1, "hold", curr_profit),
        )
    elif op == "sell":
        cache[(curr_idx, op)] = max(
            r(curr_idx+1, "buy", curr_profit+prices[curr_idx]),
            r(curr_idx+1, "hold", curr_profit),
        )

    return cache[(curr_idx, op)]



we return the max profit
what is the profit? sold - bought
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        cache = {}
        res = 0

        def r(curr_idx, op, curr_profit, curr_holding=True):
            nonlocal res

            if curr_idx >= len(prices):
                return curr_profit

            cache_key = (curr_idx, op, curr_holding)

            if cache_key in cache:
                cache[cache_key] = max(cache[cache_key], curr_profit)
                return cache[cache_key]

            cache[cache_key] = 0

            if op == "buy":
                cache[cache_key] = max(
                    r(curr_idx+1, "sell", curr_profit-prices[curr_idx], True),
                    r(curr_idx+1, "hold", curr_profit-prices[curr_idx], True),
                )

            if op == "hold":
                if not curr_holding:
                    cache[cache_key] = max(
                        r(curr_idx+1, "buy", curr_profit, False),
                        r(curr_idx+1, "hold", curr_profit, False),
                    )
                else:
                    cache[cache_key] = max(
                        r(curr_idx+1, "sell", curr_profit, True),
                        r(curr_idx+1, "hold", curr_profit, True),
                    )

            if op == "sell":
                cache[cache_key] = max(
                    r(curr_idx+1, "hold", curr_profit+prices[curr_idx], False),
                    cache[cache_key]
                )

            res = max(res, cache[cache_key])

            return cache[cache_key]

        
        for (idx, price) in enumerate(prices):
            r(idx, "buy", 0, False)

        print(cache)

        return res

                