"""

we track both indices
if char is equal we increase both indices
else we pick the max from (i+1, j), (i, j+1)

we track the longest subsequence at every step

when OOB, we return the subsequence length

  c r a b t
c 
a   
t 



"""



class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}

        def r(i, j):
            if not (0 <= i < len(text1)) or not (0 <= j < len(text2)):
                return 0

            if (i, j) in cache:
                return cache[(i, j)]

            cache[(i, j)] = 0

            if text1[i] == text2[j]:
                cache[(i, j)] = 1 + r(i+1, j+1)
            else:
                cache[(i, j)] = max(
                    r(i+1, j),
                    r(i, j+1),
                )

            return cache[(i, j)]

        return r(0, 0)