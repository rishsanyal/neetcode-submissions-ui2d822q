"""
Find the recursive case
Find how you can break the problem down into smaller steps

In this case,
- We need to find the unique paths
- it's path from right + path from the cell below
- It's 0 from the bottom cell because there's nowhere else to go

- cache the bottom cell to 0
- If we go OOB, we return 0 because there's nowhere to go from there either
- we can cache be the coordinates of the grid
- Everytime we reach the destination, we get 1 path


"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        cache = {(m-1, n-1): 1}

        def r(x, y):
            if not (0 <= x < m) or not (0 <= y < n):
                return 0

            if (x, y) in cache:
                return cache[(x, y)]

            cache[(x, y)] = 0

            for (dx,dy) in [(0,1), (1, 0)]:
                cache[(x, y)] += r(x+dx, y+dy)

            return cache[(x, y)]

        return r(0, 0)


        