"""
We need to check all sums
if it's equal, we still go ahead and check the next element

we iterate
we have index and current sum
curr_sum == goal: great, still check the next one
if not: we check the next one


but we have to start from all indices, right?
"""

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        res = 0

        def __helper(idx, curr_sum):
            if idx >= len(nums):
                return 0

            if (curr_sum+nums[idx]) >= goal:
                return int((curr_sum+nums[idx]) == goal) + __helper(idx+1, curr_sum+nums[idx])

            return __helper(idx+1, curr_sum+nums[idx])

        for idx in range(len(nums)):
            res += (idx, __helper(idx, 0))[1]

        return res