"""
O(1) space is fine because the moment we find one we update the entire matrix the moment we see a 0
we also track the last visited row and col and visit after that

for r in row
    for c in col

        if col < last_visited:
            don't go

        if 0:
            set all of it
            set last visited col
            move on from col



"""


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        last_visited_col = -1
        last_visited_row = -1

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):

                if matrix[row][col] == 0:
                    # set row, col to 0

                    for zero_row in range(len(matrix)):
                        if matrix[zero_row][col] == 0:
                            continue

                        matrix[zero_row][col] = 'EMPTY'
                        # print(zero_row, col)

                    for zero_col in range(len(matrix[0])):
                        if matrix[row][zero_col] == 0:
                            continue
                            
                        matrix[row][zero_col] = 'EMPTY'
                        # print(row, zero_col)

                    # last_visited_col = col
                    # last_visited_row = row
                    continue
    
        print(matrix)

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 'EMPTY':
                    matrix[row][col] = 0

        

        return