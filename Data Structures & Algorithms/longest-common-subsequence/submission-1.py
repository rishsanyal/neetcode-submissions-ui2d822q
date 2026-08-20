"""

  c r a b t
c 1 1 1 1 1
a 1 1 2 2 2
t 0 0 0 0 3


"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        m = len(text1)
        n = len(text2)

        grid = [[0]*n for _ in range(m)]

        print(grid)

        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    grid[i][j] = 1

        for i in range(m):
            for j in range(n):
                if (0 <= (i-1) < m) and (0 <= (j-1) < n):
                    grid[i][j] += max(
                        grid[i-1][j],
                        grid[i][j-1]
                    )
                elif (0 <= (i-1) < m):
                    grid[i][j] += grid[i-1][j]
                elif (0 <= (j-1) < n):
                    grid[i][j] += grid[i][j-1]

        return grid[-1][-1]