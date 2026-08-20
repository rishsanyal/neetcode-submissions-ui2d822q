"""

  c r a b t
c 1 1 1 1 1
a 1 1 2 2 2
t 0 0 0 0 3


  b s b i n i n m
j 0 0 0 0 0 0 0 0
m 0 0 0 0 0 0 0 1
j 0 0 0 0 0 0 0 0
k 0 0 0 0 0 0 0 0
b 1 0 1 0 0 0 0 0
k 0 0 0 0 0 0 0 0
j 0 0 0 0 0 0 0 0
k 0 0 0 0 0 0 0 0
v 0 0 0 0 0 0 0 0

"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        m = len(text1)
        n = len(text2)

        cache = {}

        def r(i1, i2):
            if (i1, i2) in cache:
                return cache[(i1, i2)]

            if i1 >= len(text1) or i2 >= len(text2):
                return 0

            if text1[i1] == text2[i2]:
                cache[(i1, i2)] = 1 + r(i1+1, i2+1)
            else:
                cache[(i1, i2)] = max(
                    r(i1+1, i2),
                    r(i1, i2+1)
                )

            return cache[(i1, i2)]



        
        return r(0, 0)
