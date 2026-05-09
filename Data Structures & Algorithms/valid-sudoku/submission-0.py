class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        we can mantain 3 sets: row, column, grid

        Dicts
        - row_dict: row_num: set
        - col_dict: col_num: set
        - grid_dict: (row_num//3, col//3)
        
        populate them
            - check for unique entries
        check if the length is 9
        """

        row_dict = defaultdict(set)
        col_dict = defaultdict(set)
        grid_dict = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == '.':
                    continue

                if board[r][c] in row_dict[r]:
                    return False
                row_dict[r].add(board[r][c])

                if board[r][c] in col_dict[c]:
                    print("here")
                    return False
                col_dict[c].add(board[r][c])

                if board[r][c] in grid_dict[(r//3, c//3)]:
                    print("here")
                    return False
                grid_dict[(r//3, c//3)].add(board[r][c])

        return True
                