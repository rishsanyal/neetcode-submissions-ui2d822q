"""

At index 0, we can either add 0 or subtract 0
we stop when we're over the last index: target == curr_sum

0, add
0, subtract

op, idx, = curr_sum 

at each index
we either add the current number
or we subtract the current number

when we go over len(nums): we return curr_sum == target

def r(idx, curr_sum):
    if idx == len(nums):
        return int(curr_sum == target)

    if (idx, curr_sum) in cache:
        return cache[(idx, curr_sum)]

    cache[(idx, curr_sum)] = 0

    for i in [nums[idx], -nums[idx]]:
        cache[(idx, curr_sum)] += r(idx+1, curr_sum + i)
    
    return cache[(idx, curr_sum)]

return r(0, 0)





"""


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        def r(idx, curr_sum):
            if idx == len(nums):
                return int(curr_sum == target)

            if (idx, curr_sum) in cache:
                return cache[(idx, curr_sum)]

            cache[(idx, curr_sum)] = 0

            for i in [nums[idx], -nums[idx]]:
                cache[(idx, curr_sum)] += r(idx+1, curr_sum + i)
            
            return cache[(idx, curr_sum)]

        return r(0, 0)
