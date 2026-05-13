class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        There's a linkedlist cycle somehow

        where the slow ptr == fast ptr

        we get an element, we go to it's index
        """

        slow_idx, fast_idx = 0, 0

        while True:
            slow_idx = nums[slow_idx]
            fast_idx = nums[nums[fast_idx]]

            if slow_idx == fast_idx:
                break

        
        slow2 = 0
        while True:
            slow = nums[slow_idx]
            slow2 = nums[slow2]
            if slow_idx == slow2:
                return slow_idx

        return fast_idx
