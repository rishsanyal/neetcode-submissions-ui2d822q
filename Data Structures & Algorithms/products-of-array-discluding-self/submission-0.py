"""
It's a prefix sum like question:

1. we take the product from the left side onwards and we take it right onwards
2. For each index we multiply left[i] with right [i+i]
3. There we have the answer

[1,2,4,6]
[1, 1, 2, 8, 48] i
[48, 48, 24, 6, 1] i+1
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = [1 for _ in range(len(nums)+1)], [1 for _ in range(len(nums)+1)]

        for i in range(1, len(nums)+1):
            left[i] = left[i-1] * nums[i-1]

        for i in range(len(nums)-1, -1, -1):
            right[i] = right[i+1]*nums[i]

        for i in range(len(nums)):
            left[i] = left[i] * right[i+1]

        return left[:-1]
