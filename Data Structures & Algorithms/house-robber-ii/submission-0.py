# Flag is False for last element
# but can be true IN some conditions

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def dfs(i, limit):
            if i >= limit:
                return 0

            return max(
                dfs(i+1, limit),
                nums[i] + dfs(i+2, limit)
            )

        return max(dfs(0, len(nums)-1), dfs(1, len(nums)))