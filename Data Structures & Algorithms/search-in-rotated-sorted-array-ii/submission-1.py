class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """
        - We need binary search because the list is ordered already 

        Assume ideal case and then everything else is covered under else.

        CORNER CASE - [1,0,1,1,1]
        """

        l, r = 0, len(nums)-1

        # while l<=r:
        #     mid = (l+r)//2

        #     if nums[mid] == target:
        #         return True
            
        #     if nums[mid] <= nums[r]:
        #         if nums[mid] < target <= nums[r]:
        #             # go right
        #             l = mid + 1
        #         else:
        #             r = mid - 1
        #     # elif nums[l] <= nums[mid]
        #     else:
        #         if nums[l] <= target < nums[mid]:
        #             r = mid - 1
        #         else:
        #             l = mid + 1
        
        # return False

        while l <= r:
            mid = (l+r)//2

            if nums[mid] == target:
                return True

            if nums[mid] <= nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

        return False
