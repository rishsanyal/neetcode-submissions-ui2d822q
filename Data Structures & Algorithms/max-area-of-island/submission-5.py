"""

- We find one island, we start iterating through it
- We start counting all the 1 blocks it's connected to and track the result
"""



class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0

        neighbors = [
            (-1, 0),
            (0, -1),
            (1, 0),
            (0, 1)
        ]

        def traverse(x, y):
            count = 0

            if not (0 <= x < len(grid)) or not (0 <= y < len(grid[0])) or grid[x][y] == 0:
                return count

            count += 1
            grid[x][y] = 0

            for (dx, dy) in neighbors:
                count += traverse(x+dx, y+dy)

            return count

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                res = max(
                    res,
                    traverse(x, y)
                )
        
        return res