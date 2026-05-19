"""
We iterate through and set the min price and max price
every time we get a lower price, we reset the tracker
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        min_price, max_price = prices[0], prices[0]
        res = 0

        for price in prices:
            if price < min_price:
                res = min(res, max_price - min_price)
                max_price = price
                min_price = price
            else:
                max_price = max(max_price, price)


        return max(res, max_price - min_price)


        