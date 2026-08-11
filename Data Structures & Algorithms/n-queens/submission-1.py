"""
I love this problem

We need a tracker for rows, columns and positive diagonal and negative diagonal, positions=[]
we recurse by row
    for c in col

    base case is row == n, because we start from 0

"""




class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        rows, cols, pos_diag, neg_diag = set(), set(), set(), set()

        positions = []

        res = []

        def r(row_num):
            if row_num == n:
                res.append(positions[:])
                return True

            for c in range(n):
                if (row_num in rows) or (c in cols) or ((row_num+c) in pos_diag) or ((row_num-c) in neg_diag):
                    continue

                rows.add(row_num)
                cols.add(c)
                pos_diag.add((row_num+c))
                neg_diag.add((row_num-c))

                positions.append((row_num, c))

                r(row_num+1)

                positions.pop()

                rows.remove(row_num)
                cols.remove(c)
                pos_diag.remove((row_num+c))
                neg_diag.remove((row_num-c))

            return False

        r(0)

        final_res = []

        for position in res:
            temp = []
            for (_,c) in position:
                temp.append("."*(c) + "Q" + '.'*(n-c-1))

            final_res.append(temp)

        return final_res




