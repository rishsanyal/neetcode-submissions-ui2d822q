"""
We know if x == m and y == n, we have 0
we know if x,y in (m-1, n) and (m, n-1), then we have 0

nums = r(m+1, n) + r(m, n+1)
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {
            (m-1, n-1): 1
        }

        def r(x, y):
            if (x >= m) or (y >= n):
                return 0

            if (x,y) in cache:
                return cache[(x,y)]

            cache[(x,y)] = r(x+1, y) + r(x, y+1)

            return cache[(x,y)]

        r(0, 0)

        return cache[(0, 0)]
            