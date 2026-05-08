"""
We get all the tresure cells -> O(mn)
we start bfs from those (if a land cell's been hit already, means we got a closer treasure cell)

Check the variable naming, treasures don't seem right
"""

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        treasures = deque()

        tracker = [[0] * len(grid[0]) for _ in range(len(grid))]

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    treasures.append((r, c, 0))

        while treasures:
            curr_r, curr_c, curr_dist = treasures.popleft()

            if not (0 <= (curr_r) < len(grid)) or not((0 <= (curr_c) < len(grid[0]))):
                continue

            if tracker[curr_r][curr_c] != 0:
                continue

            if grid[curr_r][curr_c] == -1:
                continue
            
            if grid[curr_r][curr_c] != 0:
                grid[curr_r][curr_c] = curr_dist
                tracker[curr_r][curr_c] = curr_dist

            for (dr, dc) in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                treasures.append((curr_r + dr, curr_c + dc, curr_dist+1))

        return
