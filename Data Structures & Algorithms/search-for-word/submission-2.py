"""
We'll iterate through the graph
we have the word, we make a list of it

we go through the graph and if the word list is ever empty, we return False

For each cell, we have 4 options until the length of the word -> O(m*4^n)
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        word_list = [i for i in word]
        visited = set()

        neighbors = [
            [-1, 0],
            [0, -1],
            [1, 0],
            [0, 1]
        ]

        def r(x, y, word_list):
            if not word_list:
                return True

            if not (0 <= x < len(board)) or not (0 <= y < len(board[0])) or not (board[x][y] == word_list[0]) or (x,y) in visited:
                return False

            visited.add((x, y))

            for (nx, ny) in neighbors:
                ans = r(x+nx, y+ny, word_list[1:])
                if ans:
                    return True

            visited.remove((x, y))

            return False
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                res = r(i, j, word_list)
                if res:
                    return True

        return False