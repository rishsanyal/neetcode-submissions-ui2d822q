"""
We have to replace the land cells with the distance closest to a treasure chest

We start from treasure chests and do BFS to all reachable land cells
    - Problem: we'd iterate through the same block MULTIPLE times when we just need to visit each block once
    - we'd track all of the min a deque and use that


We could start from all land cells and do a bfs to treasure cells too
"""



class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # track all treasure chests in a deque
        q = deque()

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 0:
                    q.append((x, y, 0))

        neighbors = [
            (-1, 0),
            (0, -1),
            (1, 0),
            (0, 1)
        ]

        visited = set()

        while q:
            curr_x, curr_y, curr_count = q.popleft()

            if not (0 <= curr_x < len(grid)) or not (0 <= curr_y < len(grid[0])) or grid[curr_x][curr_y] == -1:
                continue

            if (curr_x, curr_y) in visited:
                continue

            visited.add((curr_x, curr_y))

            grid[curr_x][curr_y] = min(grid[curr_x][curr_y], curr_count)

            for (dx, dy) in neighbors:
                q.append((curr_x+dx, curr_y+dy, curr_count+1))


        return



            

            
