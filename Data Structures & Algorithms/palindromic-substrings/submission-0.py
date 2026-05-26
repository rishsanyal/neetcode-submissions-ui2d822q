"""
We could use the same where we keep going outward from one char and keep counting

O(N62)
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        n, res = 0, 0


        for i in range(len(s)):
            for j in range(2):
                l, r = i, i+j

                while (0 <= l < len(s)) and (0 <= r < len(s)):
                    if s[l] == s[r]:
                        res += 1

                        l -= 1
                        r += 1
                    else:
                         break

        return res







