"""
We need to return the perimeter of the island.

Perimeter is the number of cells that either have water or nothing around them
we add perimeter as we go on, for every cell.

Once a cell is visited, we mark it as visited, 
    either by changing it's value to -1 or tracking the index.

Tracking the index -> O(ij) memory if all of them are islands
Changing the value to -1 -> in place (if possible)

BFS/DFS - In this case BFS would be a better choice since we want to go wider?

Good question to ask (can we change this in place?)

For every x and y:
    we check neighbors, 
        if 0 or out of range add 1 to perimeter
        if 1 don't do anything
        mark as -1
"""

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0

        neighbors = [
            (-1, 0),
            (0, -1),
            (1, 0),
            (0, 1)
        ]

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0 or grid[r][c] == -1:
                    continue

                for dx, dy in neighbors:
                    curr_x = r + dx
                    curr_y = c + dy

                    # OOB or water
                    if not (0 <= curr_x < len(grid)) or not (0 <= curr_y < len(grid[0])) or grid[curr_x][curr_y] == 0:
                        res += 1

                grid[r][c] = -1

        return res