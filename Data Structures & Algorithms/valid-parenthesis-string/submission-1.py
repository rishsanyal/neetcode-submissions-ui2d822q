"""
We could cache it by number of left parenthesis and right parenthesis
OR number of open brackets

if ( - we start an open backet
if ) - we end an oper bracket
if * - we have to do both?

How do we become greedy with it?
"""

class Solution:
    def checkValidString(self, s: str) -> bool:

        cache = {}
        
        def r(l, idx):
            if idx == len(s):
                return (l == 0)

            if l < 0:
                return False

            if (l, idx) in cache:
                return cache[(l, idx)]

            if s[idx] == '(':
                cache[(l, idx)] = r(l+1, idx+1)
            if s[idx] == ')':
                cache[(l, idx)] = r(l-1, idx+1)
            if s[idx] == '*':
                cache[(l, idx)] = r(l+1, idx+1) or r(l-1, idx+1) or r(l, idx+1)

            return cache[(l, idx)]

        return r(0, 0)