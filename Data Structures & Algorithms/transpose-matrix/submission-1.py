"""

mxn matrix ->


3x4
[
    [1,0,5],
    [2,4,3],
    [1,4,3],
    [3,5,2],
]

[
    [1,2,1,3],
    [0,4,4,5],
    [5,3,3,2]
]

We can't exchange everywhere, we could to create a new one

for c in col: (0, 3)
    for r in row: (0, 4)
        new_matrix[c][r] = matrix[r][c]

"""


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        ROW, COL = len(matrix), len(matrix[0])
        new_matrix = [[0] * ROW for _ in range(COL)]

        for c in range(COL):
            for r in range(ROW):
                new_matrix[c][r] = matrix[r][c]

        return new_matrix