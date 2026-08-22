"""

we track both indices
if char is equal we increase both indices
else we pick the max from (i+1, j), (i, j+1)

we track the longest subsequence at every step

when OOB, we return the subsequence length
"""



class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}

        def r(i, j, curr_len=0):

            if not (0 <= i < len(text1)) or not (0 <= j < len(text2)):
                return curr_len

            if (i, j) in cache:
                cache[(i, j)] = max(cache[(i, j)], curr_len)
                return cache[(i, j)]

            cache[(i, j)] = 0

            if text1[i] == text2[j]:
                cache[(i, j)] = r(i+1, j+1, curr_len+1)
            else:
                cache[(i, j)] = max(
                    r(i+1, j, curr_len),
                    r(i, j+1, curr_len),
                    r(i+1, j+1, curr_len)
                )

            return cache[(i, j)]

        return r(0, 0)