"""

2 pointer solution for swapping numbers

[1,2,3,4,5,6,7,8]
[5,6,7,8,1,2,3,4]

- reverse all
- reverse from 0 to k and so on ...

[1,2,3,4,5,6]
[3,4,5,6,1,2]

[1,2,3,4,5,6,7]
[7,6,5,4,3,2,1]
"""



class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if k == 0:
            return

        nums.reverse()

        k = k % len(nums)

        l = 0
        r = k-1

        while l < r:
            nums[l], nums[r] = nums[r], nums[l]

            l += 1
            r -= 1

        l = k
        r = len(nums) - 1

        while l < r:
            nums[l], nums[r] = nums[r], nums[l]

            l += 1
            r -= 1

        
        