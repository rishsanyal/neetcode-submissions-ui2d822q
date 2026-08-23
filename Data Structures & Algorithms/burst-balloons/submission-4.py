"""
Breaking down into sub problems
An oddysey

- At each level, we pick a balloon, pop it
- We need to return the maximum number of coins
- At each level, we have to track the max coins we can get, right?

- We're calculating this for a range between left and right

"""

class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        nums = [1] + nums + [1]

        cache = {}

        def dfs(l, r):
            if (l,r) in cache:
                return cache[(l,r)]

            if l > r:
                cache[(l,r)] = 0
                return 0

            cache[(l,r)] = 0

            for i in range(l, r+1):
                cache[(l,r)] = max(
                    cache[(l,r)],
                    dfs(l, i-1) + (nums[l-1]*nums[i]*nums[r+1]) + dfs(i+1, r)
                )

            return cache[(l,r)]

        return dfs(1, len(nums)-2)


        
        