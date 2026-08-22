"""

states
- buy -> idx+1
- sell -> idx+2

- We need to track the max profit
- We have to buy first
- At each step, we could either Do nothing OR we buy/sell

terminal case: We run out of stocks
    we return what we're holding

we add when we sell and - when we buy



    def r(idx=0, state=True):
        if idx >= len(prices):
            return 0

        if (idx, state) in cache:
            return cache[(idx, state)]

        res = r(idx+1, state)

        if state:
            res = max(res, prices[idx] + r(idx+1, not state))
        else:
            res = max(res, r(idx+1, not state) - prices[idx])

        return res

[2, 3, 4]

[3,4] - 2

    

"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        cache = {}

        def r(idx=0, state=True):
            if idx >= len(prices):
                return 0

            if (idx, state) in cache:
                return cache[(idx, state)]

            res = r(idx+1, state)

            if state:
                res = max(res, r(idx+1, not state) - prices[idx])
            else:
                res = max(res, r(idx+2, not state) + prices[idx])

            cache[(idx, state)] = res

            return cache[(idx, state)]
            
        return r(0)