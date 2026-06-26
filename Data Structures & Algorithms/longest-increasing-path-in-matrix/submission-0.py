"""
- We could do a BFS from every (x,y) point and cache the result with visited nodes

(0,0) - {}
(0,1) - {}
(0,2) - {1: set((1,2))}

We move in every direction until possible
- We have the distance from those cells too then

dfs(x, y, curr_dist=0, curr_path=set()):

    if x,y in cache:
        check for every set in the max path 
        if the len of curr_path is same for any
        else return 0 because curr path has already covered it

    dist = [
        (-1, 0),
        (0, -1),
        (1, 0),
        (0, 1),
    ]

    max_len, max_len_paths = []

    for new_x, new_y in dist:
        # check validity

        curr_len, curr_path = dfs(x+new_x, y+new_y, curr_dist+1, curr_path + set(x,y))





What if we only move 1 way? top and right? We can be sure there's no overlap, right? - Yes
    - BUT THAT'S NOT HOW THE GRID WORKS

    ans for this is 5 (1 - 2 - 3 - 4 - 8)

    1, 1, 1
    2, 3, 4
    8, 8, 8

    We should still be able to cache somehow - we need to track the paths


"""


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        cache = {}

        def dfs(x, y, prev_val):
            if not ((0 <= x < len(matrix)) and (0 <= y < len(matrix[0]))) or matrix[x][y] <= prev_val:
                return 0

            if (x,y) in cache:
                return cache[(x,y)]
            
            dist = [
                (-1, 0),
                (0, -1),
                (1, 0),
                (0, 1),
            ]

            max_len = 0

            for new_x, new_y in dist:
                curr_len = dfs(x+new_x, y+new_y, matrix[x][y])
                max_len = max(max_len, curr_len)

            cache[(x,y)] = 1 + max_len

            return cache[(x,y)]

        res = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = max(res, dfs(i, j, -1))

        return res









