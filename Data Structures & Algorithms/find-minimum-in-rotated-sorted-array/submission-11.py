"""
If number is between l and r -> go left
if number < l -> go left: r = mid
if number > r -> go right: l = mid + 1

0,1,2,3,4,5
3,4,5,6,1,2

0,1,2,3,4,5
4,5,0,1,2,3

"""


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        res = nums[l]

        while l < r:
            mid = (l+r)//2
            res = min(res, nums[mid])

            if nums[mid] <= nums[r]:
                r = mid - 1
            elif nums[mid] >= nums[r]:
                l = mid + 1

        return res