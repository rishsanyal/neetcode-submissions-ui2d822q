"""

We swap everything in a window - STUPID
l = 0, r = k
swap until r hits the end?


[1,2,3,4] 1 -> [4,1,2,3]

[4,3,2,1] -> [4,1,2,3]

[1,2,3,4,5,6,7,8]

[8,7,6,5,1,2,3,4] - reverse first k
[5,6,7,8,1,2,3,4]


[1,2,3,4,5,6,7] - 3 -> [5,6,7,1,2,3,4]
[7,6,5,4,3,2,1] - reverse all
[5,6,7,1,2,3,4] - reverse first k and then reverse the rest

[1000,2,4,-3], k = 2
[-3,4,2,1000] - reverse all
[4,-3,1000,2] - reverse first k and then the rest
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k =  k % len(nums)

        # reverse all
        i = 0
        j = len(nums)-1

        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        i = 0
        j = k-1

        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        i = k
        j = len(nums)-1


        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        nums = nums
        