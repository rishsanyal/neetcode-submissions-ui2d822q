"""
we get the MAX Jump length from the arr index
but we can go for the shorter ones and update the target as we go along

We start from one, we keep going until we hit. target
we can update target meanwhile too with curr_idx + nums[curr_idx]

we start iterating, if the curr_index > target: we return False


[2,3,1,1,4]

"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = 0

        for idx, distance in enumerate(nums):
            if idx > target:
                return False

            target = max(target, idx + distance)

        print(target)

        return target >= len(nums)-1
        