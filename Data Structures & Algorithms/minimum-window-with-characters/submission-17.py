"""
s="ADOBECODEBANC"
t="ABC"
"""




class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        s_dict = {}
        t_dict = Counter(t)

        l = r = 0

        res = ''
        res_len = len(s)+1

        for r in range(len(s)):
            curr_char = s[r]

            if curr_char in t_dict:

                if curr_char not in s_dict:
                    s_dict[curr_char] = 0
                
                s_dict[curr_char] += 1

                if len(s_dict.keys()) == len(t_dict.keys()):
                    match_status = True
                    # check count
                    # s_dict can have more
                    for key, val in t_dict.items():
                        if s_dict[key] < val:
                            match_status = False
                            break

                    # We increase l and keep checking the keys
                    while match_status and len(s_dict.keys()) == len(t_dict.keys()):
                        # check res
                        if (not res) or ((r - l + 1) <= res_len):
                            res_len = r-l+1
                            res = s[l:r+1]

                        if l < len(s) and s[l] in s_dict:
                            s_dict[s[l]] -= 1

                            if s_dict[s[l]] <= 0:
                                s_dict.pop(s[l])

                            match_status = (s[l] in s_dict) and s_dict[s[l]] >= t_dict[s[l]]

                        l += 1

        # print(s_dict, l)

        return res