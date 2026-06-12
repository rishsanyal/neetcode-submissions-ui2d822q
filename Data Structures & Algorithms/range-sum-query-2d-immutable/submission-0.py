class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.tracker = [[0 for _ in range(len(matrix[0])+1)] for _ in range(len(matrix)+1)]

        for i in range(1, len(self.tracker)):
            row_sum = 0

            for j in range(1, len(self.tracker[0])):
                row_sum += matrix[i-1][j-1]
                above = self.tracker[i-1][j]
                self.tracker[i][j] = row_sum + above

        for i in self.tracker:
            print(i)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        return (
            self.tracker[row2+1][col2+1] - 
            self.tracker[row2+1][col1] - 
            self.tracker[row1][col2+1] + 
            self.tracker[row1][col1]
        )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)