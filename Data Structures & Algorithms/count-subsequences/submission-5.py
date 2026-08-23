"""

if character matches, we either increase t or disregard it
if t_idx >= len(t): return 1
if s_idx >= len(s): return 0

if s[0] == t[0]:
    c[0][0] = r(i+1, t) + r(i+1, t+1)
else:
    c[0][0] = r(i+1, t)

caat cat
0,0
    1,1
        2,2
            3,2 - 1
        2,1
            3,2 - 1


    1,0
        2,0
            3,0 - 0

"""


class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        cache = {}

        def r(s_idx, t_idx):
            if t_idx >= len(t):
                return 1

            if s_idx >= len(s):
                return 0

            if (s_idx, t_idx) in cache:
                return cache[(s_idx, t_idx)]

            cache[(s_idx, t_idx)] = r(s_idx+1, t_idx)

            if s[s_idx] == t[t_idx]:
                cache[(s_idx, t_idx)] += r(s_idx+1, t_idx+1)

            return cache[(s_idx, t_idx)]

        return r(0, 0)