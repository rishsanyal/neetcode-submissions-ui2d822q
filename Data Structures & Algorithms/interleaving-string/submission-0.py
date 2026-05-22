"""
We could use a 3-d matrix cache

we compare each index against s3
if there's a match, we add one and go on to next index of s1 and s2
if not match: we go to s1_idx+1, s2 and s1, s2_idx+1
"""

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        cache = {}

        def r(s1_idx, s2_idx, s3_idx):
            
            print(s1_idx, s2_idx, s3_idx)

            if s3_idx == len(s3):
                return True

            if not (0 <= s1_idx < len(s1)) and not (0 <= s2_idx < len(s2)):
                return False

            if (s1_idx, s2_idx) in cache:
                return cache[(s1_idx, s2_idx)]

            cache[(s1_idx, s2_idx)] = False

            if (0 <= s1_idx < len(s1)) and (0 <= s2_idx < len(s2)) and s1[s1_idx] == s2[s2_idx] == s3[s3_idx]:
                cache[(s1_idx, s2_idx)] =  r(s1_idx+1, s2_idx, s3_idx+1) or r(s1_idx, s2_idx+1,s3_idx+1)
            elif (0 <= s1_idx < len(s1)) and s1[s1_idx] == s3[s3_idx]:
                cache[(s1_idx, s2_idx)] = r(s1_idx+1, s2_idx, s3_idx+1)
            elif (0 <= s2_idx < len(s2)) and s2[s2_idx] == s3[s3_idx]:
                cache[(s1_idx, s2_idx)] = r(s1_idx, s2_idx+1, s3_idx+1)

            return cache[(s1_idx, s2_idx)]

        return r(0, 0, 0)