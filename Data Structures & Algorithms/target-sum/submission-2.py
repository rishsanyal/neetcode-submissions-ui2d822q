class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        cache = {}

        def r(idx, curr_sum):
            if idx >= len(nums):
                return (curr_sum == target)

            if (idx, curr_sum) in cache:
                return cache[(idx, curr_sum)]

            cache[(idx, curr_sum)] = 0

            cache[(idx, curr_sum)] = r(idx+1, curr_sum+nums[idx]) + r(idx+1, curr_sum-nums[idx])

            return cache[(idx, curr_sum)]

        return r(0, 0)