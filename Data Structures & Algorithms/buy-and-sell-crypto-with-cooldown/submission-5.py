"""
At every point you have 2 options
buy/sell OR hold

we track the index, curr holding and curr profit


- Should we wait to buy at the lowest? Not necessary, we could just hold (not buy) from the start

prices = [1,3,4,0,4]


Edge cases:
- empty list
- one element
- negative prices (not possible)

cache -> idx, buy and value is curr_profit
O(idx*2) -> O(N)

[2, 1, 4] -> 3
1, True



[3,2,6,5,0,3]
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        cache = {}

        def r(idx, buy=True):

            cache_key = (idx, buy)

            if idx >= len(prices):
                return 0

            if cache_key in cache:
                return cache[cache_key]

            # HOLD
            res = r(idx+1, buy)

            if not buy:
                # sell
                res = max(res, r(idx+2, True) + prices[idx])
            else:
                # buy
                res = max(res, r(idx+1, False) - prices[idx])

            cache[cache_key] = res

            return cache[cache_key]

        r(0)

        return cache[(0, True)]