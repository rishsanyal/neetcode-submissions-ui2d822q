"""


We either (buy or hold)/sell OR Sell/Hold

We need the highest price

index, curr_holding=None|int, curr_profit

if idx == len(prices):
    return curr_profit

if curr_holding is None:
    we buy
    we sell
    we hold
else:
    we sell
    or we hold


"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        cache = {}

        def r(idx, bought):
            
            key = (idx, bought)

            if idx == len(prices):
                cache[key] = 0
                return cache[key]

            if key in cache:
                return cache[key]

            res = r(idx+1, bought)

            if not bought:
                res = max(
                    # SOLD on the same day as bought
                    r(idx+1, True) - prices[idx],
                    # Holding the new bought price
                    res
                )
            else:
                res = max(
                    # Sold previously holding price
                    r(idx+1, False) + prices[idx],
                    res
                )

            cache[key] = res
            return cache[key]

        return r(0, False)