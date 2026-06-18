"""

We get a counter of T
We create a window of len(T) from s

- We start from the first common character
- we keep going until the count is 0
- we increase left until 0
- then keep increasing right until not 0

- We have 2 pointers l and r - 0,0 
- we have a counter dict for t
- we increase r until counter becomes empty
- when empty, we increase l


"""



class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ''

        counter_t = Counter(t)

        res = ''
        res_len = len(s)

        l, r = 0, 0

        while r < len(s):
            curr_char = s[r]

            if curr_char in counter_t:
                counter_t[curr_char] -= 1

                if counter_t[curr_char] == 0:
                    counter_t.pop(curr_char)

            while not counter_t and (l <= r):
                if res_len >= r-l+1:
                    res_len = r-l+1
                    res = s[l:r+1]

                prev_char = s[l]
                l += 1

                if (prev_char in t):
                    counter_t[prev_char] += 1

            r += 1

        return res
