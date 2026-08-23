"""
we track each index

at each level, we either pick a character from s1 or s2
we're not matching it against s3's str at any point

We could compare it to s3
we have the index

"""

class Solution:
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False

        def r(i, j, curr_str):
            if i == len(s1) and j == len(s2):
                return curr_str == s3      # validate at the end

            res = False
            if i < len(s1):
                res = res or r(i+1, j, curr_str + s1[i])
            if j < len(s2):
                res = res or r(i, j+1, curr_str + s2[j])

            return res

        return r(0, 0, "")
                