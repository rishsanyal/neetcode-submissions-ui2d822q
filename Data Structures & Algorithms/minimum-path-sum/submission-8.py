"""
- if we reach the bottom right cell, we don't iterate forward
- we DO count the value of the starting cell
- We do include the value of the last one

- We need to indicate that going OOB isn't possible

- We could do top down
    - value + min(x+dx, y+dy)

"""



class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        cache = {}
        MAX_VAL = 201

        def r(x, y):
            if not (0 <= x < len(grid)) or not (0 <= y < len(grid[0])):
                return MAX_VAL
            
            if (x, y) in cache:
                return cache[(x, y)]

            if (x,y) == (len(grid)-1, len(grid[0])-1):
                return grid[len(grid)-1][len(grid[0])-1]

            cache[(x, y)] = grid[x][y]

            res = MAX_VAL

            for (dx, dy) in [(0, 1), (1, 0)]:
                res = min(res, r(x+dx, y+dy))

            cache[(x, y)] += res

            return cache[(x, y)]

        return r(0, 0)
                