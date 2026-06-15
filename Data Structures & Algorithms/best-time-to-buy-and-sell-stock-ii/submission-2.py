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

        def r(idx, curr_holding, curr_profit=0):
            
            key = (idx, curr_holding, curr_profit)

            if idx == len(prices):
                return curr_profit if (curr_holding is None) else 0

            if key in cache:
                return cache[key]

            res = 0

            if curr_holding is None:
                res = max(
                    # SOLD on the same day as bought
                    r(idx+1, None, curr_profit),

                    # Holding the new bought price
                    r(idx+1, prices[idx], curr_profit)
                )
            else:
                res = max(
                    # Sold previously holding price
                    r(idx+1, None, curr_profit + prices[idx] - curr_holding),

                    # Still holding the same price
                    r(idx+1, curr_holding, curr_profit)
                )

            cache[key] = res

            return cache[key]

        return(r(0, None, 0))