"""
cache[(x, y)]

we stop in the case of 1: return 0

"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        cache = {}

        def r(x, y):
            if not (0 <= x < len(obstacleGrid)) or not (0 <= y < len(obstacleGrid[0])) or obstacleGrid[x][y] == 1:
                return 0

            if (x, y) in cache:
                return cache[(x, y)]

            if x == len(obstacleGrid)-1 and  y == len(obstacleGrid[0])-1:
                return 1

            cache[(x, y)] = r(x+1, y) + r(x, y+1)

            return cache[(x, y)]
        
        return r(0, 0)