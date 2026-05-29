"""
What if we double the list and go on like that?

We have a curr_count and a global count

[2,3,-4]
curr_count = -1

[-2,4,-5,4,-5,9,4]

We could ifnd the min sum subarray and delete that from the total sum
O(N^2)

"""

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        c_max, c_min, g_max, g_min = float('-inf'), float('inf'), nums[0], nums[0]


        total = 0
        res = 0

        for num in nums:
            total += num
            c_max = max(num, c_max+num)
            c_min = min(num, c_min+num)

            g_max = max(g_max, c_max)
            g_min = min(g_min, c_min)

        return max(g_max, total-g_min)