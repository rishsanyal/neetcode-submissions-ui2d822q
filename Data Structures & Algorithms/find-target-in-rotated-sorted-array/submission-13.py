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


0,1,2,3,4,5,6
4,5,6,7,0,1,2

1

"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l+r)//2
            print(l, r, mid)

            if nums[mid] == target:
                return mid

            # Ideal case
            if nums[l] <= nums[mid]:
                # Ideal case
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                # Ideal case
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1