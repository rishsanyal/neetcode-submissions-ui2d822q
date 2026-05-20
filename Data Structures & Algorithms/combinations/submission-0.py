"""
base case, len of list == k OR len of remaining list < (n-k)
we have a list of 1..n
at each level, we either take a number or we don't

n = 3, k = 2

[], [1,2,3]
[1], [2,3]
[], [2,3]
[1,2], [3]
[2], [3]
[], [3]

"""

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def r(curr_list, inp_list):
            if len(curr_list) == k:
                res.append(curr_list)
                return

            if not inp_list:
                return

            # # check this
            # if curr_num > n:
            #     return

            r(curr_list, inp_list[1:])
            r(curr_list+[inp_list[0]], inp_list[1:])

            return

        r([], range(1,n+1))

        return res
        