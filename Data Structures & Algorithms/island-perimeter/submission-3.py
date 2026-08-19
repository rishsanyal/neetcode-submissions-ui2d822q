"""
For each block, we check the surrounding
if the neighbor is out of bounds, water - we add 1, else 0

when we visit the node, we mark it as water after

we don't need to spread from one island onwards
we can literally just iterate through all 
"""


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0

        diff = [
            (-1, 0),
            (0, -1),
            (1, 0),
            (0, 1)
        ]

        def __get_perimeter(x, y):
            perimeter = 0

            for dx, dy in diff:
                new_x, new_y = x+dx, y+dy

                if (not (0 <= new_x < len(grid))) or not (0 <= new_y < len(grid[0])) or grid[new_x][new_y] == 0:
                    perimeter += 1

            return perimeter

        for cx in range(len(grid)):
            for cy in range(len(grid[0])):
                if grid[cx][cy] == 1:
                    res += __get_perimeter(cx, cy)


        return res

