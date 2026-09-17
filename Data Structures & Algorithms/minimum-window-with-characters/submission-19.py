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
                match_status = False

                if len(s_dict.keys()) == len(t_dict.keys()):
                    match_status = True
                    for key, val in t_dict.items():
                        if s_dict[key] < val:
                            match_status = False
                            break

                while match_status and l < r:
                    if res_len >= (r-l+1):
                        res_len = r-l+1
                        res = s[l:r+1]

                    if s[l] in t_dict:
                        s_dict[s[l]] -= 1

                        if s_dict[s[l]] == 0:
                            s_dict.pop(s[l])

                        match_status = (t_dict[s[l]] <= s_dict.get(s[l], -1)) and len(s_dict.keys()) == len(t_dict.keys())

                    l += 1

        return res