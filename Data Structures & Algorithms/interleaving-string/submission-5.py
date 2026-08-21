"""
At each level, we pick either s or t

we could cache/track by s1, s2
if len(s3) == len(curr_str) and s3 == curr_str:
    return 1

cache[(s1, len(s3)-s1]

if s1 == len(s1):
    return r(curr_str+t[s2+1])
elif s2 == len(s2):
    return r(curr_str+s[s1+1])
else:
    return r(curr_str+t[s2+1]) or r(curr_str+s[s1+1])

"""



class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        cache = {}

        s,t = s1, s2

        def r(idx1, idx2, curr_str):
        # we could cache/track by s1, s2
            if len(s3) == len(curr_str) and (idx1 == len(s) and idx2 == len(t)):
                return (s3 == curr_str)

            if (idx1 == len(s) and idx2 == len(t)):
                return False

            cache[(idx1, len(curr_str))] = 0

            if idx1 == len(s1):
                cache[(idx1, len(curr_str))] = r(idx1, idx2+1, curr_str+t[idx2])
            elif idx2 == len(s2):
                cache[(idx1, len(curr_str))] = r(idx1+1, idx2, curr_str+s[idx1])
            else:
                cache[(idx1, len(curr_str))] = r(idx1, idx2+1, curr_str+t[idx2]) or r(idx1+1, idx2, curr_str+s[idx1])

            return cache[(idx1, len(curr_str))]

        return r(0, 0, '')


