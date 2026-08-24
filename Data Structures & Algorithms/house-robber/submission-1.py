"""
for each house we have 2 options
we loot and move 2 houses down
we don't loot and move 1 house down

def r(idx):
    if idx >= len(nums):
        return 0

    if idx in cache:
        return cache[idx]

    cache[idx] = max(
        nums[idx] + r(idx+2),
        r(idx+1)
    )

    return cache[idx]

return r(0)
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        
        def r(idx):
            if idx >= len(nums):
                return 0

            if idx in cache:
                return cache[idx]

            cache[idx] = max(
                nums[idx] + r(idx+2),
                r(idx+1)
            )

            return cache[idx]

        return r(0)