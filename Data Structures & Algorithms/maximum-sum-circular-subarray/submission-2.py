class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = 0
        c_min, c_max = float('inf'), float('-inf')
        g_min, g_max = nums[0], nums[0]

        for num in nums:
            total += num

            c_max = max(num, c_max + num)
            c_min = min(num, c_min + num)

            g_max = max(g_max, c_max)
            g_min = min(g_min, c_min)

        if g_max > 0:
            return max(g_max, total - g_min)
        
        return g_max