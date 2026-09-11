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

        def __bfs(x, y, new_char, old_char='O'):
            # board[x][y] = new_char
            q = deque([(x, y)])

            while q:
                new_x, new_y = q.popleft()  

                if not (0 <= new_x < len(board)) or not (0 <= new_y < len(board[0])) or board[new_x][new_y] != old_char:
                    continue

                board[new_x][new_y] = new_char

                for (dx, dy) in diff:
                    q.append(
                        (new_x + dx, new_y + dy)
                    )

            return


        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if (i in (0, len(board)-1)) or (j in (0, len(board[0])-1)):
                    __bfs(i, j, 'L')

        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                __bfs(i, j, 'X')
        
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                    if board[i][j] == 'L':
                        board[i][j] = 'O'

        return 


        
