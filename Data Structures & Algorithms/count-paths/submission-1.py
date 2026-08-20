"""
- We can either move down or right
- we start from (0, 0)
- we need to get to (m-1, n-1)

Simple formula
steps[a][b] = r(a+1, b) + r(a, b+1)

"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        cache = {}

        def r(x, y):
            if not (0 <= x < m) or not (0 <= y < n):
                return 0

            if (x, y) in cache:
                return cache[(x, y)]

            if (x == m-1) and (y == n-1):
                return 1

            cache[(x, y)] = 0

            cache[(x, y)] = r(x+1, y) + r(x, y+1)




            return cache[(x, y)]

        return r(0, 0)

        