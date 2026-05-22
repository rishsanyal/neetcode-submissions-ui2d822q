"""
At every house we have two options
We either take the current house or we take the next one?

[2,9,8,3,6]
- 2+8+6
9+3

9 + 6

9,0,3,9

cache[idx] = max(curr_num + r(idx+2), r(idx+1))
"""

class Solution:
    def rob(self, nums: List[int]) -> int:

        cache = {}

        def r(idx):
            if idx >= len(nums):
                return 0

            if idx in cache:
                return cache[idx]

            cache[idx] = max(nums[idx] + r(idx+2), r(idx+1))

            return cache[idx]

        r(0)

        return cache[0]
        