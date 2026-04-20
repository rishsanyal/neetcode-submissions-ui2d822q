class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        if mid >= r:
            l = mid + 1
        elif mid <= l:
            r = mid - 1
        else:
            l < mid < r:
                r = mid - 1
        """

        l, r = 0, len(nums)-1
        res = 1001

        while l <= r:
            mid = (l+r)//2
            res = min(res, nums[mid])

            if nums[mid] < nums[r]:
                r = mid-1
            else:
                l = mid+1

        return res

            