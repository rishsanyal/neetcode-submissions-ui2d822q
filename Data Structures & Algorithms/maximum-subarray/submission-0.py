"""
we need the largest sum
at every point we can either add or start a new one
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = 0

        for num in nums:
            res = max(res+num, num)

        return res
        