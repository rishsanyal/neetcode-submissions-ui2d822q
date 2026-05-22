"""
We could pick a greedy path but let's see what the issues with that are

We can only go right on down.
We need to go from the end to the beginning to cache, right


grid = [
    [1,2,0],
    [5,4,2],
    [1,1,3]
]


[8,7,5],
[5,8,5],
[1,4,3]

res[x][y] = min(r(x-1, y), r(x, y+1))
cache the rest
"""

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        cache = {}
        cache[(len(grid)-1, len(grid[0])-1)] = grid[len(grid)-1][len(grid[0])-1]

        def r(x, y):
            if (x,y) in cache:
                return cache[(x,y)]

            if not  (0 <= x < len(grid)) or not (0 <= y < len(grid[0])): 
                return float('inf')

            res = min(r(x+1, y), r(x, y+1))

            cache[(x,y)] = grid[x][y] + res

            return cache[(x,y)]


        return r(0, 0)

            


        