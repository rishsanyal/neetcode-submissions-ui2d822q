# Flag is False for last element
# but can be true IN some conditions

class Solution:
    def rob(self, nums: List[int]) -> int:

        cache = {}
        
        def dfs(i, limit):
            if i >= limit:
                return 0

            if (i, limit) in cache:
                return cache[(i, limit)]

            cache[(i, limit)] = max(
                dfs(i+1, limit),
                nums[i] + dfs(i+2, limit)
            )

            return cache[(i, limit)]

        return max(dfs(0, len(nums)-1), dfs(1, len(nums)))