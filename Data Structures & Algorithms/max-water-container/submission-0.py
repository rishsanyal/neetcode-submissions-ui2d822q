"""
We could go greedy, but will that work?

[1,7,2,5,4,7,3,6]
l, r = 0, len(heights)-1
"""

class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l, r = 0, len(heights)-1
        res = 0

        while l < r:
            curr_area = min(heights[l], heights[r]) * (r-l)
            res = max(res, curr_area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return res
        