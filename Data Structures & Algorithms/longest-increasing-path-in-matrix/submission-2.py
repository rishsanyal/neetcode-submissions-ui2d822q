class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        cache = {}

        diff = [
            (-1, 0),
            (0, -1),
            (1, 0),
            (0, 1),
        ]

        res = 0

        def r(x, y, prev_val):

            nonlocal res

            if not (0 <= x < len(matrix)) or not (0 <= y < len(matrix[0])) or (matrix[x][y] <= prev_val):
                return 0

            if (x,y) in cache:
                return cache[(x, y)]

            cache[(x, y)] = 0
            ans = 0

            for (dx, dy) in diff:
                ans = max(
                    ans,
                    r(x+dx, y+dy, matrix[x][y])
                )
            
            cache[(x,y)] = 1 + ans

            return 1 + ans

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = max(
                    res,
                    r(i, j, -1)
                )

        return res