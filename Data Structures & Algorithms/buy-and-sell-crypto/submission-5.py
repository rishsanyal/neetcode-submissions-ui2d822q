"""

- We need the MAX profit we can achieve
- At each point,
    - we can track the curr min and curr max
    - if the current min is reset, so is the curr max

- [10, 10], [1,1], [1,5], [1,6], [1,7], [1,1]

"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min = prices[0]
        curr_max = prices[0]

        res = 0

        for price in prices:
            if price <= curr_min:
                curr_min = price
                curr_max = price
            else:
                curr_max = max(curr_max, price)

            res = max(res, curr_max - curr_min)

        return res
        