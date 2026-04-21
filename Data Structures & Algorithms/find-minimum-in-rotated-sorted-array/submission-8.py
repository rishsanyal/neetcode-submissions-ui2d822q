class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        if mid >= r:
            # go right
            l = mid + 1
        else:
            # go left
            r = mid - 1
        """

        l, r = 0, len(nums)-1
        ans = nums[l]

        while l <= r:
            mid = (l+r)//2
            ans = min(ans,nums[mid])

            if nums[mid] < nums[r]:
                r = mid - 1
            else:
                l = mid + 1

        return ans