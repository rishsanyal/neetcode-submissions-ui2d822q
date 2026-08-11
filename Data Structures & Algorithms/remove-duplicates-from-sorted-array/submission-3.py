"""
We have to remove it in place
We ONLY care about the first K elements

l, r = 0, len(nums)-1 - No because we'll have to switch that back

we could have l
find the next unique and greater number
switch that with l+1
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 0

        res = 1

        while l < len(nums):
            curr_num = nums[l]
            r = l + 1

            while r < len(nums) and nums[r] <= curr_num:
                r += 1

            if r < len(nums):
                nums[l+1], nums[r] = nums[r], nums[l+1]

            l += 1

        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                break
            res = i

        return res+1