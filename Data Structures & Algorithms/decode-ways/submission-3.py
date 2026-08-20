"""

12
- 1 '2'
    - 2 ''
- 12 ''


We track the idx of the string

"""



class Solution:
    def numDecodings(self, s: str) -> int:

        char_tracker = {}

        for i in range(65, 65+26):
            char_tracker[str(i-65+1)] = chr(i)

        cache = {}
        res = 0

        def __helper(idx):

            res = 0

            if idx in cache:
                return cache[idx]
            
            if idx == len(s):
                return 1

            # if s[idx] not in char_tracker:
            #     return 0

            one_char = s[idx]
            two_char = s[idx:idx+2]

            if one_char in char_tracker:
                res += __helper(idx+1)

            if two_char in char_tracker:
                res += __helper(idx+2)

            cache[idx] = res

            return cache[idx]

        ans = __helper(0)

        return ans