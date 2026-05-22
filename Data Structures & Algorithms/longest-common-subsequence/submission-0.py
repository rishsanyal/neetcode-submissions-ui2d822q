"""
We need to check how much of the shorter string does the longer string have?
in that order

c,a,t
c,r,a,b,t

if characters are equal -> we could either ignore it or move on

We either delete elements or we don't


we can start with 0
c, a, t
3, 2, 1

c, r, a, b, t
3, 2, 2, 1, 1

Our options are 
if equal - great
else: we check index - 1 for text1 and same for text2

compare at every step

create a cache -> {}


"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}
        text1_len, text2_len = 0, 0
        idx1, idx2 = 0, 0

        def r(i1, i2):
            if (i1, i2) in cache:
                return cache[(i1, i2)]

            if i1 >= len(text1) or i2 >= len(text2):
                return 0

            if text1[i1] == text2[i2]:
                cache[(i1, i2)] = 1 + r(i1+1, i2+1)
            else:
                cache[(i1, i2)] = max(r(i1+1, i2), r(i1, i2+1))

            return cache[(i1, i2)]

        return r(0, 0)