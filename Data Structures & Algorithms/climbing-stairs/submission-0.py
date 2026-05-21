class Solution:
    def climbStairs(self, n: int) -> int:
        
        res = 0
        cache = {0:1, 1:1}

        def r(steps):
            if steps in cache:
                return cache[steps]

            if steps <= 0:
                return (steps == 0)

            cache[steps] = r(steps-2) + r(steps-1)

            return cache[steps]

        r(n)

        return cache[n]