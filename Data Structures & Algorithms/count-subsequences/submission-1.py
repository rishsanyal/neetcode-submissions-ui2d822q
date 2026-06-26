"""
At each level we either select a character, or we don't

we have indices, s_index and t_index

base case when t_idx == len(t):
    return 1
when s_idx == len(s):
    return 0

when s[s_idx] == t[t_idx]:
    we do both
    r(s_idx+1, t_idx+1)
    r(s_idx+1, t_idx)
else:
    r(s_idx+1, t_idx)

"""

class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        cache = {}

        def r(s_idx, t_idx):

            if (s_idx, t_idx) in cache:
                return cache[(s_idx, t_idx)]

            if s_idx == len(s) and t_idx == len(t):
                return 1
            if t_idx == len(t):
                return 1
            if s_idx == len(s):
                return 0

            res = 0

            if s[s_idx] == t[t_idx]:
                res += r(s_idx+1, t_idx+1)
    
            res += r(s_idx+1, t_idx)

            cache[(s_idx, t_idx)] = res

            return cache[s_idx, t_idx]
        
        return r(0, 0)

            
        