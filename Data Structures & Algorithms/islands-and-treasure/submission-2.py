class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        Multi Source BFS
        - We track all treasures
        - we maintain a visited set, so we don't enter the same room twice
        - We BFS out from each
        - whichever room was visited first has our min distance
        """

        visited = [[0] * len(grid[0]) for _ in range(len(grid))]
        tracker = deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    tracker.append((r,c,0))

        while tracker:
            row, col, dist = tracker.popleft()

            # OOB
            if not (0 <= row < len(grid)) or not (0 <= col < len(grid[0])):
                continue

            # Water OR visited
            if (visited[row][col] != 0) or (grid[row][col] == -1):
                continue

            # Reset if not treasure
            if grid[row][col] != 0:
                grid[row][col] = dist

            visited[row][col] = 1

            # traverse neighbors
            for dr, dc in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                tracker.append((row+dr, col+dc, dist+1))

        return