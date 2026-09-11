"""
Silly way, track father and if you reach edge, you backtrack

Better way, go through the edges, mark all of the O's and the O's connected to it as '1'

can we reuse BFS? We can give it the sign to change to

Longest way:
1. BFS to mark all edged ones as something else
2. BFS to mark the internal ones as something else

"""

class Solution:
    def solve(self, board: List[List[str]]) -> None:

        diff = [
            (-1, 0),
            (0, -1),
            (1, 0),
            (0, 1)
        ]

        def __dfs(x, y, new_char, old_char='O'):            
            if not (0 <= x < len(board)) or not (0 <= y < len(board[0])) or board[x][y] != old_char:
                return

            board[x][y] = new_char

            for (dx, dy) in diff:
                __dfs(x+dx, y+dy, new_char)

            return


        for i in range(0, len(board)):
            for j in range(0, len(board[0])):

                if (i in (0, len(board)-1)) or (j in (0, len(board[0])-1)):
                    if board[i][j] == 'O':
                        __dfs(i, j, 'L')

        for i in range(0, len(board)):
            for j in range(0, len(board[0])):

                if i in (0, len(board)-1) or j in (0, len(board[0])-1):
                    continue
                
                if board[i][j] == 'O':
                    __dfs(i, j, 'X')
        
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):

                if (i in (0, len(board)-1)) or (j in (0, len(board[0])-1)):
                    if board[i][j] == 'L':
                        __dfs(i, j, 'O', 'L')

        return 


        
