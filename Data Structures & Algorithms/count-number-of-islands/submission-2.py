"""
DFS works here
if we encounter a 1, we have found an island
any visited 1 should be turned into a 0

how would we do this with BFS?

- use a deque in the function
- go through all the neighbors for a x,y coordinate

"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0

        neighbors = [
            (-1, 0),
            (0, -1),
            (1, 0),
            (0, 1)
        ]

        def traverse(x, y):
            if not (0 <= x < len(grid)) or not (0 <= y < len(grid[0])) or grid[x][y] == "0":
                return

            grid[x][y] = "0"

            for (dx, dy) in neighbors:
                traverse(x+dx, y+dy)

            return

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "1":
                    res += 1

                traverse(x, y)

        return res


    

