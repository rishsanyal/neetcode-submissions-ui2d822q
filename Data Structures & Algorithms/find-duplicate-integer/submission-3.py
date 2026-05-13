class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        There's a linkedlist cycle somehow

        where the slow ptr == fast ptr

        we get an element, we go to it's index
        """

        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

        return 0
