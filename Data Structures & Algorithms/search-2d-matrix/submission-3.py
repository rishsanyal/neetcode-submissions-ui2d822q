"""
We could go an easy path and binary search when the target is between the start and end of a row

We could do 2 binary searches
One vertically - to find which row to search
One horizontally - to find the number
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS_LEN, COL_LEN = len(matrix[0]), len(matrix)

        def __vertical_search():
            l, r = 0, COL_LEN-1

            while l <= r:
                mid = (l+r)//2

                if matrix[mid][0] == target:
                    return mid
                elif matrix[mid][0] < target:
                    l = mid + 1
                else:
                    r = mid - 1

            return r

        def __horizontal_search(row_num):
            nums = matrix[row_num]

            l, r = 0, len(nums)-1

            while l <= r:
                mid = (l+r)//2

                if nums[mid] == target:
                    return True
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1

            return False

        row_num = __vertical_search()
        num_exists = __horizontal_search(row_num)

        return num_exists
