class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        2 -> rotten fruit

        Multi source BFS - always needs a visited set
            - track the rotten oranges and count the number of fresh oranges for the result
            - Do BFS from the rotten oranges
            
        """

        fresh_orange_count = 0
        tracker = deque()
        visited = set()
        res = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh_orange_count += 1

                elif grid[r][c] == 2:
                    tracker.append((r, c, 0))

        while tracker:
            row, col, time = tracker.popleft()

            if not (0<=row<len(grid)) or not (0<=col<len(grid[0])):
                continue

            if grid[row][col] == 0 or grid[row][col] == -1:
                continue

            if grid[row][col] == 1:
                res = max(res, time)
                fresh_orange_count -= 1

            grid[row][col] = -1

            for dr, dc in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                tracker.append((row+dr, col+dc,time+1))


        return res if fresh_orange_count == 0 else -1
            