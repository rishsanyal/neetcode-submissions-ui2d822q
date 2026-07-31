"""
Same as earlier but DIFFERENT

0,1,2,3,4
1,0,1,1,1




"""


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l+r)//2

            print(l, r, mid)
            

            if nums[mid] == target:
                return True

            if nums[l] == nums[mid] == nums[r]:
                r -= 1
                l += 1

            elif nums[mid] >= nums[l]:
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