class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t):
            return ""
        
        s_dict, t_dict = defaultdict(int), Counter(t)
        res_len = len(s)+1
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

                while match_status and l <= r:
                    if res_len >= (r-l+1) or (not res):
                        res_len = r-l+1
                        res = s[l:r+1]

                    if l < len(s) and s[l] in t_dict:
                        s_dict[s[l]] -= 1

                        if s_dict[s[l]] == 0:
                            s_dict.pop(s[l])

                        match_status = (s[l] in s_dict and s_dict[s[l]] >= t_dict[s[l]])

                    l += 1

        return res