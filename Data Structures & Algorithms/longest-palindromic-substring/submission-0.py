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

        for idx, _ in enumerate(s):
            temp_len, temp_str = 0, ''
            # Odd case
            l, r = idx, idx
            while l <= r and l >= 0 and r < len(s):
                if s[l] == s[r]:
                    temp_len += 1

                    if res_len <= temp_len:
                        res_len = temp_len
                        res_str = s[l:r+1]

                l -= 1
                r += 1
            
            # even case
            l, r = idx, idx+1
            while l <= r and l >= 0 and r < len(s):
                if s[l] == s[r]:
                    temp_len += 1
                    temp_str = s[l] + temp_str + s[r]

                    if res_len <= temp_len:
                        res_len = temp_len
                        res_str = s[l:r+1]

                l -= 1
                r += 1

        return res_str        

        