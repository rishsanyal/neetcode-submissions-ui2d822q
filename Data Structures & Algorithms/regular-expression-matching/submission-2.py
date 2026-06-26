"""
I see an exponential algo here

aa
.b

. matches the index against it
* matches 0 or more of the last element
.* matches everything

doing this in reverse is easier?

l, r = len(s)-1, len(p)-1

deal with first characters
s_char, p_char

if both alphabets: match and move on, if not match: False
if p == '.': move on
if p == '*': check index else we keep matching per remaining element


s = "nnn", p = "n*"

s_idx, p_idx
0, 0

"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        cache = {}
        
        def match(s_idx, p_idx):

            if s_idx >= len(s) and p_idx >= len(p):
                return True
            if p_idx >= len(p):
                return False

            if (s_idx, p_idx) in cache:
                return cache[(s_idx, p_idx)]

            match_flag =  s_idx < len(s) and ((s[s_idx] == p[p_idx]) or (p[p_idx] == '.'))

            if (p_idx + 1 < len(p)) and p[p_idx+1] == "*":
                match_flag = (match_flag and match(s_idx+1, p_idx)) or match(s_idx, p_idx+2)
            elif match_flag:
                match_flag = match(s_idx+1, p_idx+1)

            cache[(s_idx, p_idx)] = match_flag

            return cache[(s_idx, p_idx)]


            # if curr_p_char.isalpha():
            #     if curr_s_char == curr_p_char:
            #         return match(s_idx+1, p_idx+1)
            #     else:
            #         # todo: check if the next one's *
            #         if p_idx+1 < len(p) and p[p_idx+1] == '*':
            #             # TODO: handle case
            #             curr_res = match(s_idx+1, p_idx)
            #             return curr_res

            #         return False

            # if curr_p_char == '.':
            #     return match(s_idbx+1, p_idx+1)
            
            # if curr_p_char == '*':
            #     if p_idx < 1:
            #         return False

            #     prev_char = p[p_idx-1]

            #     # match prev_char and keep incrementing
            #     # can we do this recursively? not sure

            #     if prev_char == '.':
            #         return True
            #     elif prev_char.isalpha():
            #         while s_idx < len(s) and s[s_idx] == prev_char:
            #             curr_res = match(s_idx, p_idx+1)
            #             s_idx += 1

            #             if curr_res:
            #                 return True

        return match(0, 0)