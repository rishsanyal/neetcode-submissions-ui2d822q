class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """
        - We need binary search because the list is ordered already 

        Assume ideal case and then everything else is covered under else.

        CORNER CASE - [1,0,1,1,1]

        Double numbers complicate it,
        We could find the min and double the list - O(N) space though
        """

        # rotated_idx = -1

        # for i in range(1, len(nums)):
        #     if nums[i-1] > nums[i]:
        #         rotated_idx = i
        #         break

        # nums += nums[:rotated_idx]

        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l+r)//2

            if nums[mid] == target:
                return True

            if nums[l] == nums[mid] == nums[r]:
                l += 1
                r -= 1
                continue
            elif nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return False
