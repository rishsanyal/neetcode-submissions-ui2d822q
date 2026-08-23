"""
- We could trackp revious value (this is easier)
    - top down approach
- We could also only jump to a number greater
"""




class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        cache = {}

        diff = [
            (-1, 0),
            (0, -1),
            (1, 0),
            (0, 1),
        ]

        def r(x, y, prev_val):
            if not (0 <= x < len(matrix)) or not (0 <= y < len(matrix[0])) or matrix[x][y] <= prev_val:
                return 0

            if (x, y) in cache:
                return cache[(x, y)]

            cache[(x, y)] = 0

            for (dx, dy) in diff:
                cache[(x, y)] = max(
                    cache[(x, y)],
                    1 + r(x+dx, y+dy, matrix[x][y])
                )

            return cache[(x, y)]

        res = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = max(res, r(i, j, -1))

        return res

