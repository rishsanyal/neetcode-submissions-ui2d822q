class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        We start from the 2 indices because if they're not at the edge or connected to the edge cells
         they're not going to be surrounded

        We start by tracking the edges and then do BFS from those cells.
        """

        edge_cells = deque()

        for r in range(len(board)):
            for c in range(len(board[0])):
                if r == 0 or c == 0 or r == len(board)-1 or c == len(board[0])-1:
                    edge_cells.append((r, c))

        while edge_cells:
            r, c = edge_cells.popleft()

            # OOB
            if not (0 <= r < len(board)) or not (0 <= c < len(board[0])):
                continue

            # Visited or invalid
            if board[r][c] in ("X", "V"):
                continue

            # mark visited
            board[r][c] = "V"

            # add neighbors

            for dr, dc in [(-1,0), (1, 0), (0, -1), (0, 1)]:
                edge_cells.append((r+dr, c+dc))

        print(board)

        # traverse in the end and re-mark the valid ones
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == "V":
                    board[r][c] = "O"
        
        print(board)
        return

