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
            nonlocal res
            res += 1

            # So we can popleft BABY!!
            q = deque([(x, y)])

            while q:
                curr_x, curr_y = q.popleft()

                if not (0 <= curr_x < len(grid)) or not (0 <= curr_y < len(grid[0])) or (grid[curr_x][curr_y] == "0"):
                    continue

                grid[curr_x][curr_y] = "0"

                for (dx, dy) in neighbors:
                    q.append((curr_x+dx, curr_y+dy))


        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "1":
                    traverse(x, y)
        
        return res          