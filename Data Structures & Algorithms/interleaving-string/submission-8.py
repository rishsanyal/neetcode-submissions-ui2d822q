"""
we track each index

at each level, we either pick a character from s1 or s2
we're not matching it against s3's str at any point

We could compare it to s3
we have the index

"""

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        cache = {}

        def r(i, j):
            if i >= len(s1) and j >= len(s2):
                return True

            if (i, j) in cache:
                return cache[(i, j)]

            cache[(i, j)] = False

            if i < len(s1) and s1[i] == s3[i+j]:
                cache[(i, j)] = cache[(i, j)] or r(i+1, j)

            if j < len(s2) and s2[j] == s3[i+j]:
                cache[(i, j)] = cache[(i, j)] or r(i, j+1)

            return  cache[(i, j)]

        return r(0, 0)


            