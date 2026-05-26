"""
At each level, we can either add a number to subset1 or to subset2

When there's no more numbers left, we compare

cache - ?

def r(subset1 sum, subset2 sum, idx):
    if idx > nums:
        return subset1 == subset2

    return r(subset1 + nums[idx], subset2, idx+1) or  r(subset1, subset2 + nums[idx], idx+1)
"""

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        cache = {}

        def r(subset1_sum, subset2_sum, idx):
            if idx >= len(nums):
                return subset1_sum == subset2_sum

            if (subset1_sum, subset2_sum, idx) in cache:
                return cache[(subset1_sum, subset2_sum, idx)]

            cache[(subset1_sum, subset2_sum, idx)] = r(subset1_sum + nums[idx], subset2_sum, idx+1) or r(subset1_sum, subset2_sum + nums[idx], idx+1)

            return cache[(subset1_sum, subset2_sum, idx)]


        return r(0, 0, 0)

