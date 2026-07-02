"""
0,0
0,1
1,1
1,0

We start with the outermost column and keep decreasing the allowed columns

l, r - 0, len(matrix[0])
up, down - 0, len(matrix)

while up <= down and l <= r:
    we go from left to right

    up to down

    right to left

    down to up

    change up, down, left and right


"""



class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l, r = 0, len(matrix[0])
        up, down = 0, len(matrix)

        res = []

        while l <= r and up <= down:
            for i in range(l, r):
                res.append(matrix[up][i])

            up += 1

            for j in range(up, down):
                res.append(matrix[j][r-1])

            r -= 1

            if not (l < r and up < down):
                break

            for i in range(r-1, l-1, -1):
                res.append(matrix[down-1][i])

            down -= 1

            for j in range(down-1, up-1, -1):
                res.append(matrix[j][l])

            l += 1


        return res






