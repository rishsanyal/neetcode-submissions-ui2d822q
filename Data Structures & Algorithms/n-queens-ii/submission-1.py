class Solution:
    def totalNQueens(self, n: int) -> int:
        final_res = 0

        rows, columns, pos_diag, neg_diag = set(), set(), set(), set()

        def r(x, res):
            nonlocal final_res

            if len(res) == n:
                final_res += 1
                return

            for y in range(n):
                if (x not in rows) and (y not in columns) and ((x+y) not in pos_diag) and ((x-y) not in neg_diag):
                    res.add((x, y))
                    rows.add(x)
                    columns.add(y)
                    pos_diag.add(x+y)
                    neg_diag.add(x-y)

                    r(x+1, res)

                    res.remove((x,y))
                    rows.remove(x)
                    columns.remove(y)
                    pos_diag.remove(x+y)
                    neg_diag.remove(x-y)


        r(0, set())

        return final_res

            
                    