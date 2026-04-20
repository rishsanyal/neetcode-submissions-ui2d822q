class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW, COL = len(matrix), len(matrix[0])

        l, r = 0, (ROW*COL)-1

        while l <= r:
            mid = (l+r)//2

            row, col = mid // COL, mid % COL

            mid_num = matrix[row][col]

            if mid_num == target:
                return True
            elif mid_num < target:
                l = mid+1
            else:
                r = mid-1

        return False
