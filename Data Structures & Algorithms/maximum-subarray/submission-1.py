"""
we need the largest sum
at every point we can either add or start a new one

[-2,1,-3,4,-1,2,1,-5,4]


"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = 0
        ans = nums[0]

        for num in nums:
            res = max(res+num, num)
            ans = max(res, ans)


        return ans
        