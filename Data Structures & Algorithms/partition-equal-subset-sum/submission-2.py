"""
We can cache by track (idx, left_sum)

def r(idx, left_sum, right_sum):
    if idx == len(nums):
        return left_sum == right_sum

    if (idx, left_sum) in cache:
        return cache[(idx, left_sum)]

    cache[(idx, left_sum)] = r(idx+1, left_sum+nums[idx], right_sum) or r(idx+1, left_sum, right_sum+nums[idx])

    return cache[(idx, left_sum)]
"""


class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        cache = {}
        
        def r(idx, left_sum, right_sum):
            if idx == len(nums):
                return left_sum == right_sum

            if (idx, left_sum) in cache:
                return cache[(idx, left_sum)]

            cache[(idx, left_sum)] = r(idx+1, left_sum+nums[idx], right_sum) or r(idx+1, left_sum, right_sum+nums[idx])

            return cache[(idx, left_sum)]

        return r(0, 0, 0)

        