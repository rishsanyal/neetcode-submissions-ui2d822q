"""
This should be a 2 pointer problem, right?

We have the t_counter, a counter dict for t
we track the result in a global variable, res

we have l = r = 0, tracking the  indices for s
we create an s_counter dict
We copy t_counter and decrement any character we see
once everything is 0, we compare the length against res and update res

we decrease the window by increasing l pointer until we see a character in t
we update the count in t_tracker

repeat


t_ctr = {x:1, y:1, z:1}

l = r = 0

s_ctr = {x:1, y:1, z:1}
r = 5
s_ctr = {x:1, z:1}
r = 6
s_ctr = {z:1}
r = 8
s_ctr = {}
l += 1 until 5

5:8+1 -> s[5:9]


"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t):
            return ""

        t_ctr = Counter(t)
        s_ctr = t_ctr.copy()

        l = r = 0
        res = s

        for (r, c) in enumerate(s):
            # exists in t
            if c in t_ctr:
                s_ctr[c] -= 1

                if s_ctr[c] == 0:
                    s_ctr.pop(c)

                while s_ctr == {}:
                    res = s[l:r+1] if (r - l + 1) < len(res) else res

                    if s[l] in t_ctr:
                        s_ctr[s[l]] += 1
                    
                    l += 1

                while s_ctr[c] < 0:
                    if s[l] in t_ctr:
                        s_ctr[s[l]] += 1
                    
                    l += 1

                # if l == len(s):
                #     break

        return res

                



        