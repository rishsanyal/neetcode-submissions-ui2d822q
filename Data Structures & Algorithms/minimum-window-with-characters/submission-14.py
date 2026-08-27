"""



Let's have 2 dictionaries
t_dict - counter
s_dict - DefaultDict

we have l, r, 0, 0

when the number of keys is the same, we iterate through them
if the count is different on any one, we continue

if the count on all is the same, we increase l untilwe hit a character in counter_t

go from there - r += 1
"""

"""
s="ODEBANC"
t="ABC"

t_dict = {A:1, B:1, C:1}

l, r = 0, 0

BEC
l, r = 0, 5

"""





class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ''

        res = ''
        res_len = len(s)

        s_ctr = defaultdict(int)
        t_ctr = Counter(t)

        l = r = 0

        match_status = True

        while r < len(s):
            curr_char = s[r]

            if curr_char in t_ctr:
                s_ctr[curr_char] += 1

                if match_status := len(s_ctr.keys()) == len(t_ctr.keys()):
                    for key, val in t_ctr.items():
                        if s_ctr[key] < val:
                            match_status = False

                    while match_status and l <= r:
                        if res_len >= (r - l + 1):
                            res = s[l:r+1]
                            res_len = r - l + 1

                        prev_char = s[l]

                        if s[l] in t_ctr and l < r:
                            s_ctr[s[l]] -= 1

                            if s_ctr[s[l]] <= 0:
                                s_ctr.pop(s[l])

                            match_status = s_ctr[s[l]] == t_ctr[s[l]]
                            
                        l += 1

            r += 1

        return res

                





        