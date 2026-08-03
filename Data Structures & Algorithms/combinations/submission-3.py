"""

curr_list, curr_num

if len(curr_list) == k:
    append
    return

if curr_num == n+1:
    return

for i in range(curr_num+1, n):
    r(curr_list + [i], i)

r([curr_num+1], curr_num+1)

[], [1,2,3]
[1], [2,3]
[], [2,3]

[1,2], [3]
[1,3], []

[2], [3]
[], [3]

[2,3] []

[3]

"""



class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        

        res = []

        def r(curr_list, i):
            if len(curr_list) == k:
                res.append(curr_list[:])
                return

            if i == n+1:
                return

            r(curr_list + [i], i+1)
            r(curr_list, i+1)

        r([], 1)

        return res

