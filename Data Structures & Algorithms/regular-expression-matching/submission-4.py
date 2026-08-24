"""

. is a match for ANY single character
* is a match of the previous element (0 or more times)

**?
.*?

we track both indices
if . we match 1 character
if * we match 0 or more characters
if character -> we match, if false, return false

terminal is both strings are done

def r(s_idx, p_idx):
    if s_idx == len(s) and p_idx == len(p):
        return True
    if s_idx == len(s) or p_idx == len(p):
        return False

    cache[(s_idx, p_idx)] = False

    if s[s_idx] == p[p_idx] or p[p_idx] == '.':
        cache[(s_idx, p_idx)] |= r(s_idx+1, p_idx+1)
    if p[p_idx] == '*':
        for i in range(p_idx, len(p)):
            cache[(s_idx, p_idx)] |= r(s_idx+1, i)

    return cache[(s_idx, p_idx)]


if * we go back one index
keep matching until valid
    
if prev_char:
    if s[s_idx] == prev_char:
        continue matching with prev_char
    else:
        we keep s_idx the same, but increase this 

"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}

        def r(s_idx, p_idx, prev_char=None):

            cache_key = (s_idx, p_idx, prev_char)

            if s_idx == len(s) and p_idx == len(p):
                return True
            if s_idx == len(s):
                return (prev_char and p_idx+2 == len(p))
            if p_idx == len(p):
                return False

            if cache_key in cache:
                return cache[cache_key]


            cache[cache_key] = False

            if prev_char:
                if (s[s_idx] == prev_char) or (prev_char == '.'):
                    cache[cache_key] |= r(s_idx+1, p_idx, prev_char)
                    cache[cache_key] |= r(s_idx, p_idx+2)
                else:
                    cache[cache_key] |= r(s_idx, p_idx+2)
            else:
                if s[s_idx] == p[p_idx] or p[p_idx] == '.':
                    cache[cache_key] |= r(s_idx+1, p_idx+1)
                if p[p_idx] == '*':
                    if p_idx == 0:
                        return False
                    
                    prev_char = p[p_idx-1]
                    cache[cache_key] |= r(s_idx-1, p_idx-1, prev_char)
                    

            return cache[cache_key]

        return r(0, 0)