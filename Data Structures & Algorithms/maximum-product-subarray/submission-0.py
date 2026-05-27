"""
At each level, we either include the next number or start from scratch

[1,2,-3,4]

[5, 2, -1, 10, -3, 4]

we maintain a min, max for recursion
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        c_max, c_min = 1, 1

        ans = float('-inf')

        for i in nums:
            c_max = max(
                i*c_max,
                i*c_min,
                i
            )

            c_min = min(
                i*c_max,
                i*c_min,
                i
            )

            ans = max(c_max, ans)


        return ans
        
