"""
We maintain a not possible set
    - row
    - column
    - diagonals (x+y and x-y)

    for every point, we check if that point is in any of the visited sets
        if not: we place a queen there and continue

        we maintain a global result that we can join in while backtracking
"""

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        final_res = []

        rows, columns, pos_diag, neg_diag = set(), set(), set(), set()

        def r(x, res):
            if x >= n and len(res) == n:
                temp_res = [(["."] * n) for _ in range(n)]
                for q_x, q_y in res:
                    temp_res[q_x][q_y] = 'Q'

                for i in range(len(temp_res)):
                    temp_res[i] = ''.join(temp_res[i])

                final_res.append(temp_res)
                return
            
            for y in range(n):
                if (x not in rows) and (y not in columns) and ((x-y) not in neg_diag) and ((x+y) not in pos_diag):
                    res.add((x, y))

                    rows.add(x)
                    columns.add(y)
                    pos_diag.add(x+y)
                    neg_diag.add(x-y)

                    r(x+1, res)

                    res.remove((x, y))

                    rows.remove(x)
                    columns.remove(y)
                    pos_diag.remove(x+y)
                    neg_diag.remove(x-y)

        # for i in range(n):
        r(0, set())

        return final_res


        