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
        ans = 0

        def r(idx, curr_holding=0, curr_profit=0, buy=True):
            nonlocal ans

            print(idx, curr_holding, curr_profit, buy)
            if idx >= len(prices):
                cache[(idx, curr_holding)] = curr_profit if buy else 0
                ans = max(ans, cache[(idx, curr_holding)])
                return cache[(idx, curr_holding)]

            if (idx, curr_holding) in cache:
                return cache[(idx, curr_holding)]

            cache[(idx, curr_holding)] = 0
            res = 0
            
            if not buy:
                # sell
                if prices[idx] > curr_holding:
                    res = r(idx+2, 0, curr_profit + (prices[idx]-curr_holding), True)
            else:
                # buy
                res = r(idx+1, prices[idx], curr_profit, False)
            
            # HOLD
            res = max(res, r(idx+1, curr_holding, curr_profit, buy))

            cache[(idx, curr_holding)] = max(res, cache[(idx, curr_holding)])

            return cache[(idx, curr_holding)]

        r(0)

        print(cache)

        return ans