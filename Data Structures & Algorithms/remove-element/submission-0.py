class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        ctr = 0


        while idx < len(nums):
            print(nums)
            if nums[idx] == val:
                nums.pop(idx)
                ctr += 1
            else:
                idx += 1

        return len(nums)