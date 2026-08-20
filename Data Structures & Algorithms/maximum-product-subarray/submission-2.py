"""
We need to find the largest subarray from index -> max(i*subarray(i+1), subarray(i+1))

we should probably track the most and least at every point

- at every point, a subarray starts from this index or it includes the prev number or it has the previous negative number



"""


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        c_max, c_min = 1, 1

        ans = float('-inf')

        for i in nums:
            temp = c_max * i

            c_max = max(
                i*c_max,
                i*c_min,
                i
            )

            c_min = min(
                temp,
                i*c_min,
                i
            )

            ans = max(
                c_max, ans
            )

        return ans