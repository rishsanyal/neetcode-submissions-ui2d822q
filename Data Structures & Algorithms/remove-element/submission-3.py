"""
We maintain a pointer for the last index
we start from the left
l = 0
r = len(nums) - 1
while l < r:
    if val == val:
        we switch
        we decrease r
    else:
        l += 1

"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
            else:
                l += 1

        return l+1