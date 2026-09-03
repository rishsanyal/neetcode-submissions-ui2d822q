"""
- Multi-source BFS
- we can track the max time at every step

We take all the rotten oranges in a deque
we start iterating out from there

"""


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        res = 0

        neighbors = [
            (-1, 0),
            (0, -1),
            (1, 0),
            (0, 1)
        ]

        count = 0

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 2:
                    q.append((x, y, 0))
                    count += 1

                if grid[x][y] == 1:
                    count += 1

        
        while q:
            curr_x, curr_y, curr_time = q.popleft()

            if not (0 <= curr_x < len(grid)) or not (0 <= curr_y < len(grid[0])) or grid[curr_x][curr_y] == 0:
                continue

            count -= 1

            res = max(res, curr_time)
            grid[curr_x][curr_y] = 0

            for (dx, dy) in neighbors:
                q.append(
                    (curr_x+dx, curr_y+dy, curr_time+1)
                )

        return res if count == 0 else -1