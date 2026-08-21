"""
DFS

- We have to minimize the route
- If we go OOB, return 201 - since that's the max we can go to
- if we reach the bottom left, we can return the ans


cache = {
    (len(grid)-1, len(grid[0])-1): grid[len(grid)-1][len(grid[0])-1]
}

def r(x, y):
    if not (0 <= x < len(grid)) or not (0 <= y < len(grid[0])):
        return 201

    if (x, y) in cache:
        return cache[(x,y)]

    cache[(x,y)] = grid[x][y] + min(r(x+1, y), r(x, y+1))

    return cache[(x,y)]


"""


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        cache = {
            (len(grid)-1, len(grid[0])-1): grid[len(grid)-1][len(grid[0])-1]
        }

        def r(x, y):
            if not (0 <= x < len(grid)) or not (0 <= y < len(grid[0])):
                return 201

            if (x, y) in cache:
                return cache[(x,y)]

            cache[(x,y)] = grid[x][y] + min(r(x+1, y), r(x, y+1))

            return cache[(x,y)]

        return r(0, 0)