"""
if num == mid:
    return mid
if num > mid or < r:
    go right
    l = mid + 1
else:
    go left
    r = mid -1


return -1


0,1,2,3,4,5
1,2,3,4,5,0

1

"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l+r)//2

            if nums[mid] == target:
                return mid
            elif (nums[mid] > target) or (nums[mid] <= nums[r]):
                l = mid + 1
            else:
                r = mid - 1

        return -1