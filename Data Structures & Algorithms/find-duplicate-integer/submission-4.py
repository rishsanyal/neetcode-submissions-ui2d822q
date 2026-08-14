"""

Initial solution:

- Iterate through the list
- we know which index we're visiting
- mark nums[nums[idx]] as -ve
    - if it's already -ve, we found the number
- if the current number is -ve, we ignore

[-1,-2,-3,2,2]

0, 1

[-1,-2,-3,-4,4] - 4

finding in O(1) time

slow pointer and fast pointer from every number

[1,2,3,4,4]

if slow_ptr == fast_ptr == idx: good
elif slow_ptr == fast_ptr, prev number?


"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        for idx, num in enumerate(nums):
            num = abs(num)

            if nums[num-1] < 0:
                return num

            nums[num-1] = -1*nums[num-1]

        return 0
