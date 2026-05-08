class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0

        def __dfs(r, c):
            if not (0 <= r < len(grid)) or not (0 <= c < len(grid[0])) or grid[r][c] == 0:
                return 0

            area = 1
            grid[r][c] = 0

            for new_r, new_c in [(-1, 0), (1, 0), (0, 1), (0,-1)]:
                area += __dfs(r+new_r, c+new_c)

            return area

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                res = max(res, __dfs(row, col))

        return res