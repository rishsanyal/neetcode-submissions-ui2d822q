"""

  a b a b d
a 1 0 1 0 0
b 0 1 0 1 0
a 1 0 1 0 0
b 0 1 0 1 0
d 0 0 0 0 1

We could go through every index and compare as long as it can go
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        res_len = 0

        for i in range(len(s)):
            for j in range(2):
                l, r = i, i+j

                while (0 <= l < len(s)) and (0 <= r < len(s)):
                    if s[l] == s[r] and (r-l+1) > res_len:
                        res_len = (r-l+1)
                        res = s[l:r+1]

                    l -= 1
                    r += 1

        return res
        