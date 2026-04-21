class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        We go find the ideal cases and everything else is under the else statement

        We build our base case on the array being un-rotated
        """

        l, r = 0, len(nums)-1

        while l<=r:
            mid = (l+r)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] <= nums[r]:
                if nums[mid] < target <= nums[r]:
                    # go right
                    l = mid + 1
                else:
                    r = mid - 1
            # elif nums[l] <= nums[mid]
            else:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        
        return -1
