# class Solution:
#     def minWindow(self, s: str, t: str) -> str:

#         if len(s) < len(t):
#             return ""
        
#         s_dict, t_dict = {}, Counter(t)
#         res_len = len(s)+10
#         res = ""

#         l = 0

#         for r in range(len(s)):
#             if s[r] in t_dict:
#                 if s[r] not in s_dict:
#                     s_dict[s[r]] = 0

#                 s_dict[s[r]] += 1
#                 match_status = len(s_dict.keys()) == len(t_dict.keys())

#                 if match_status:
#                     for key, val in t_dict.items():
#                         if s_dict[key] < val:
#                             match_status = False
#                             break

#                 while match_status and l < r:
#                     if res_len >= (r-l+1) or (not res):
#                         res_len = r-l+1
#                         res = s[l:r+1]

#                     if l < len(s) and s[l] in t_dict:
#                         s_dict[s[l]] -= 1

#                         if s_dict[s[l]] == 0:
#                             s_dict.pop(s[l])

#                         match_status = (s[l] in s_dict and s_dict[s[l]] >= t_dict[s[l]]) and len(s_dict.keys()) == len(t_dict.keys())

#                     l += 1

#         return res

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        s_dict, t_dict = defaultdict(int), Counter(t)
        res_len = len(s) + 1
        res = ""
        l = 0

        for r in range(len(s)):
            if s[r] in t_dict:
                s_dict[s[r]] += 1
                match_status = len(s_dict.keys()) == len(t_dict.keys())

                if match_status:
                    for key, val in t_dict.items():
                        if s_dict[key] < val:
                            match_status = False
                            break

                while match_status and l <= r:  # ← l <= r
                    if res_len >= (r - l + 1) or not res:
                        res_len = r - l + 1
                        res = s[l:r+1]

                    if s[l] in t_dict:
                        s_dict[s[l]] -= 1
                        if s_dict[s[l]] == 0:
                            s_dict.pop(s[l])
                        match_status = (
                            len(s_dict.keys()) == len(t_dict.keys()) and
                            all(s_dict[k] >= t_dict[k] for k in t_dict)
                        )
                    # ← if s[l] not in t_dict, match_status unchanged

                    l += 1  # ← always increment

        return res