class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l+r)//2

            if r-l == 1:
                if nums[l] < target < nums[r]:
                    return l+1
                elif target > nums[r]:
                    return r+1
                elif target < nums[l]:
                    return l
                else:
                    return -1

            if nums[mid] == target:
                return mid
            elif target < mid:
                r -= 1
            else:
                l += 1
        
        return -1