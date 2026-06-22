"""
[3,4,5,6,1,2]


"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l+r)//2

            if nums[mid] == target:
                return mid
            elif nums[l] <= target < nums[mid]:
                if target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if target < nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1

        return r


