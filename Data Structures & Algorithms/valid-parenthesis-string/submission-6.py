"""
we have 3 options

count open brackets

if c == '(': increase count by 1
if c == ')': decrease count by 1
else:
    we could do all

idx, count

"""

class Solution:
    def checkValidString(self, s: str) -> bool:
        cache = {}

        def r(idx=0, count=0):
            if idx == len(s):
                return (count == 0)

            if (idx, count) in cache:
                return cache[(idx, count)]

            if count < 0:
                cache[(idx, count)] = False
                return False

            curr_char = s[idx]

            if curr_char == '(':
                cache[(idx, count)] = r(idx+1, count+1)
            elif curr_char == ')':
                cache[(idx, count)] = r(idx+1, count-1)
            else:
                cache[(idx, count)] = r(idx+1, count-1) or r(idx+1, count+1) or r(idx+1, count)

            return cache[(idx, count)]

        return r()
        