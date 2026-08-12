"""
Greedy + 2 pointers


we have a result tracking the max result
we have l and r, 0 and len(heights)

we get the result
we update res
we move the smaller or equal one
"""

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l, r = 0, len(heights)-1

        res = 0

        while l <= r:
            curr_res = min(heights[l], heights[r])*(r-l)
            res = max(res, curr_res)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return res