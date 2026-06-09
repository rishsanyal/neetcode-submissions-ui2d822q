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

"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        cache = {}

        def r(idx, curr_holding=0, curr_profit=0, buy=True):
            if idx >= len(prices):
                return curr_profit if buy else -1

            if (idx, buy) in cache:
                return cache[(idx, buy)]
            
            cache[(idx, buy)] = 0
            res = 0
            
            if not buy:
                # sell
                res = r(idx+2, 0, curr_profit + (prices[idx]-curr_holding), True)
            else:
                # buy
                res = r(idx+1, prices[idx], curr_profit, False)
            
            # HOLD
            res = max(res, r(idx+1, curr_holding, curr_profit, buy))

            cache[(idx, buy)] = max(res, cache[(idx, buy)])

            return cache[(idx, buy)]

        return r(0)