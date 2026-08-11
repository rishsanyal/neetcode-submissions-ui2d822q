"""
- It is a sorted list, we could binary search for the number
- We could go from l - r, if l < r, else we reset l
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1

        while l < len(numbers):
            r = len(numbers)-1

            curr_target = target - numbers[l]

            while l < r and numbers[r] > curr_target:
                r -= 1

            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]

            l += 1

        return []