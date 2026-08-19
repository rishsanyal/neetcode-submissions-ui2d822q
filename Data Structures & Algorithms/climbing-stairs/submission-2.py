class Solution:
    def climbStairs(self, n: int) -> int:

        cache = {1:1, 2:2}

        def __helper(steps):
            if steps in cache:
                return cache[steps]

            cache[steps] = __helper(steps-1) + __helper(steps-2)

            return cache[steps]

        return __helper(n)

        