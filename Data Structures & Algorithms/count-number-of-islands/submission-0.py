"""
Question you lost google to


Count the numebr of islands
It's the connected 1's

We visit them in a BFS manner, because we need to identify bodies here
if we encounter a 1, we increase the island count and iterate through it's neighbors
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0

        neighbors = [
            (-1, 0),
            (0, -1),
            (0, 1),
            (1, 0)
        ]

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "0":
                    continue

                res += 1
                itr = deque([(r,c)])

                while itr:
                    curr_row, curr_col = itr.pop()

                    for dr,dc in neighbors:
                        new_r, new_c = curr_row+dr, curr_col+dc

                        if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]) \
                            and grid[new_r][new_c] == "1":
                            
                            itr.append((new_r, new_c))

                    grid[curr_row][curr_col] = "0"

        return res





    