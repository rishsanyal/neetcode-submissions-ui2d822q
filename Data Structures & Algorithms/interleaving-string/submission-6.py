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

        def r(idx1, idx2, curr_idx):
        # we could cache/track by s1, s2
            if len(s3) == curr_idx:
                return (idx1 == len(s) and idx2 == len(t))

            if (idx1, idx2) in cache:
                return cache[(idx1, idx2)]

            res = False

            if idx1 < len(s1) and s1[idx1] == s3[curr_idx]:
                res = r(idx1+1, idx2, curr_idx+1)
            
            if idx2 < len(s2) and s2[idx2] == s3[curr_idx]:
                res |= r(idx1, idx2+1, curr_idx+1)

            cache[(idx1, idx2)] = res

            return cache[(idx1, idx2)]

        return r(0, 0, 0)


