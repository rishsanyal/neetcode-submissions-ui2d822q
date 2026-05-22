"""
Robot goes from top-left to bottom right
Can only move down or right 
1's are obstacles
"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        cache = {
            (len(obstacleGrid)-1, len(obstacleGrid[0])-1): 1
        }

        if (len(obstacleGrid) <= 1) and (len(obstacleGrid[0]) <= 1):
            return 0

        def r(x,y):
            if (x,y) in cache:
                return cache[(x, y)]

            if not (0 <= x < len(obstacleGrid)) or not (0 <= y < len(obstacleGrid[0])) or obstacleGrid[x][y]:
                return 0

            cache[(x, y)] = r(x+1, y) + r(x, y+1)

            return cache[(x, y)]

        return r(0, 0)

            