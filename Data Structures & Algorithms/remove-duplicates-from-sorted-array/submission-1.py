class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if not nums or len(nums) == 1:
            return len(nums)


        i = 1

        while i < len(nums):
            if nums[i-1] == nums[i]:
                nums.pop(i)
            else:
                i += 1

        return len(nums)