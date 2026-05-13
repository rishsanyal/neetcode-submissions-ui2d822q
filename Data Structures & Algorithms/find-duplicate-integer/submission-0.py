class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        There's a linkedlist cycle somehow

        where the slow ptr == fast ptr

        we get an element, we go to it's index
        """

        slow_idx, fast_idx = 0, 1

        while nums[slow_idx] != nums[fast_idx]:
            slow_idx = nums[slow_idx]
            fast_idx = nums[nums[fast_idx]]

        return nums[fast_idx]
