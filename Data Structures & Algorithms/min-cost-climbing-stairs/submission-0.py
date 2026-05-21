class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        def r(step):
            if step > (len(cost)):
                return 0

            if step in cache:
                return cache[step]

            cache[step] = cost[step] + min(r(step+1), r(step+2))

            return cache[step]

        """

        cache = {}

        def r(step):
            if step >= len(cost):
                return 0

            if step in cache:
                return cache[step]

            cache[step] = cost[step] + min(r(step+1), r(step+2))

            return cache[step]

        r(0)

        return min(cache[0], cache[1])