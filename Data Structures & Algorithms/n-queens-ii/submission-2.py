"""

- For each queen we need to track rows, cols, pos_diag, neg_diag
- we iterate by each row
    - for each column, we place a queen
    - recurse on the next row

"""


class Solution:
    def totalNQueens(self, n: int) -> int:
        
        rows, cols, pos_diag, neg_diag = set(), set(), set(), set()

        res = 0

        def r(row):
            nonlocal res

            if row == n:
                res += 1
                return

            for c in range(n):
                if (c in cols) or (row+c) in pos_diag or (row-c) in neg_diag:
                    continue

                cols.add(c)
                pos_diag.add(row+c)
                neg_diag.add(row-c)

                r(row+1)

                cols.remove(c)
                pos_diag.remove(row+c)
                neg_diag.remove(row-c)

            return

        r(0)

        return res