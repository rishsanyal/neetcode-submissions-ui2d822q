"""
We can do BFS or DFS and track the number of connected cells at every point

We could mark visited islands with a unique key and iterate in the end
    to get the number of cells

Another thing could be to track while we iterate and have the bfs function return the number of islands

function returns number of islands visited
base case 1 island
"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        row, col = len(grid), len(grid[0])

        neighbors = [
            (0, -1),
            (0, 1),
            (-1, 0),
            (1, 0)
        ]

        def bfs(inp_row, inp_col):
            curr_island = 0
            tracker = deque([(inp_row, inp_col)])

            while tracker:
                curr_row, curr_col = tracker.pop()
                curr_island += 1

                for dr, dc in neighbors:
                    new_row, new_col = curr_row + dr, curr_col + dc

                    if 0 <= new_row < row and 0 <= new_col < col and grid[new_row][new_col] == 1:
                        tracker.append((new_row, new_col))
                
                grid[curr_row][curr_col] = 0

            return curr_island

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    res = max(res, bfs(r, c))

        return res

        