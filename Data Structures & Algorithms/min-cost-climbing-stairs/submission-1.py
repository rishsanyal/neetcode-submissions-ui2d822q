"""






"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        cache = {}
        
        def __helper(idx):
            if idx >= len(cost):
                return 0

            if idx in cache:
                return cache[idx]

            cache[idx] = cost[idx] + min(__helper(idx+2), __helper(idx+1))

            return cache[idx]

        return min(__helper(0), __helper(1))