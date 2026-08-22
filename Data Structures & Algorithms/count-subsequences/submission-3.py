"""

- We track both indices
- if one matches, we move to the next
- last case, both i and j == len(s) and len(t)

- if match - we do all three
- if not - we move only 2

cache (x, y)

"""



class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}


        def r(i, j):
            if i >= len(s) or j >= len(t):
                return j >= len(t)

            if (i,j) in cache:
                return cache[(i, j)]
            
            cache[(i, j)] = 0
            
            if s[i] == t[j]:
                cache[(i, j)] = r(i+1, j+1) + r(i+1, j)
            else:
                cache[(i, j)] = r(i+1, j)

            return cache[(i, j)]

        return r(0, 0)


            
        