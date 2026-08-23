"""
we track each index

at each level, we either pick a character from s1 or s2
we're not matching it against s3's str at any point

"""

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        cache = {}


        def r(i, j, curr_str):
            if i >= len(s1) or j >= len(s2):
                return (curr_str == s3)

            if (i,j) in cache:
                return cache[(i, j)]

            cache[(i, j)] = r(i+1, j, curr_str+s1[i]) or r(i, j+1, curr_str+s2[j])

            return cache[(i, j)]

        return r(0, 0, '')

            

            