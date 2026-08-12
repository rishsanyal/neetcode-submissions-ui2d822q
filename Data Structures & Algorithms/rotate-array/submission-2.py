"""

2 pointer solution for swapping numbers

[1,2,3,4,5,6,7,8]
[5,6,7,8,1,2,3,4]

- reverse all
- reverse from 0 to k and so on ...

[1,2,3,4,5,6]
[3,4,5,6,1,2]
"""



class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        nums.reverse()

        for l in range(0, len(nums), k):
            r = min(len(nums), (l+k)) - 1

            while l < r:
                nums[l], nums[r] = nums[r], nums[l]

                l += 1
                r -= 1

        
        