"""
At each point we have 2 options
Hold
Buy/Sell
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        cache = {}

        def r(idx, buy=True):
            if idx >= len(prices):
                return 0

            if (idx, buy) in cache:
                return cache[(idx, buy)]

            res = r(idx+1, buy)
            if buy:
                res = max(res, r(idx+1, not buy) - prices[idx])
            else:
                res = max(res, r(idx+2, not buy) + prices[idx])

            cache[(idx, buy)] = res

            return res

        return r(0)
        