"""

- We could use mergesort O(N*lgN)
- We could count all elements and update the list accordingly
    - Count Sort?

"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        counter = [0]*3

        for i in nums:
            counter[i] += 1

        ctr = 0

        for i in range(3):
            while counter[i]:
                nums[ctr] = i
                counter[i] -= 1
                ctr += 1

        