"""

- Bottom-right corner is the successful scenario
- Else is failure or need to compute
- we just need ot sum the number of successful paths

Edge cases:
- invalid values
- All 1's
- 

"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        cache = {}


        def r(x, y):
            if not (0 <= x < len(obstacleGrid)) or not (0 <= y < len(obstacleGrid[0])) or obstacleGrid[x][y] == 1:
                return 0

            if (x, y) in cache:
                return cache[(x, y)]

            if (x,y) == (len(obstacleGrid)-1, len(obstacleGrid[0])-1):
                return 1

            cache[(x, y)] = 0

            for (dx, dy) in [(0,1), (1, 0)]:
                cache[(x, y)] += r(x+dx, y+dy)

            return cache[(x, y)]

            
        return r(0, 0)