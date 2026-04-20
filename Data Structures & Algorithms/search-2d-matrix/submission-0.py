class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        - We could do binary search on every level if the number 
            is within range - O(m*lg(n))
        - We could do binary search on just the 0th index of everything too
        

        - We get the middle element by position
            - We check if that's eq
            - we increase/decrease col and row if necessary

        Split this into 2
        Binary search each row - to find if the number lies in the row
        then binary search all elements of that row
        """

        l, r = 0, len(matrix)-1
        mid = 0

        while l <= r:
            mid = (l+r) // 2

            if matrix[mid][0] <= target <= matrix[mid][len(matrix[0])-1]:
                break
            elif target <= matrix[mid][0]:
                r = mid - 1
            else:
                l = mid + 1

        l, r = 0, len(matrix[0])-1

        while l <= r:
            mid_num = (l+r) // 2

            if matrix[mid][mid_num] == target:
                return True
            elif matrix[mid][mid_num] <= target:
                r = mid_num - 1
            else:
                l = mid_num + 1
        
        return False
        