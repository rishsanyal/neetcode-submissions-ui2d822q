"""
For each number, we either add it or sutract it
Not sure how DP comes into play here yet

for each index, we either add or subtract

we could have a cache and then as we go on, we memoize it

[2, 2, 2] -> curr_sum, idx

curr_sum + 2, idx
curr_sum - 2, idx

return 0 if out of index and target != curr_sum
return 1 if out of idx and target == curr_sum
"""

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        def r(idx, curr_sum):
            
            if idx == len(nums):
                return (curr_sum == target)

            if (idx, curr_sum) in cache:
                return cache[(idx, curr_sum)]

            cache[(idx, curr_sum)] = r(idx+1, curr_sum+nums[idx]) + r(idx+1, curr_sum-nums[idx])

            return cache[(idx, curr_sum)]

        return r(0, 0)


        