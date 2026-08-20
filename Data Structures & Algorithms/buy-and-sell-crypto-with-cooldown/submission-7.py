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

        def r(curr_idx, op, curr_profit):
            nonlocal res

            if curr_idx >= len(prices):
                return curr_profit

            if (curr_idx, op) in cache:
                cache[(curr_idx, op)] = max(cache[(curr_idx, op)], curr_profit)
                return cache[(curr_idx, op)]

            cache[(curr_idx, op)] = 0

            if op == "buy":
                cache[(curr_idx, op)] = max(
                    r(curr_idx+1, "sell", curr_profit-prices[curr_idx]),
                    r(curr_idx+1, "hold", curr_profit-prices[curr_idx]),
                )
            if op == "hold":
                cache[(curr_idx, op)] = max(
                    r(curr_idx+1, "buy", curr_profit),
                    r(curr_idx+1, "hold", curr_profit),
                )
            if op == "sell":
                cache[(curr_idx, op)] = max(
                    r(curr_idx+1, "hold", curr_profit+prices[curr_idx]),
                    cache[(curr_idx, op)]
                )

            res = max(res, cache[(curr_idx, op)])

            return cache[(curr_idx, op)]

        
        for (idx, price) in enumerate(prices):
            print(r(idx, "buy", 0))

        return res

                