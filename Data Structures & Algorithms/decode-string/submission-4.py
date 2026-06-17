"""
Stack of stacks?
we have an int

Every time we see a new number, we start a stack?

abbbabbbc

every time we see
- bracket close, we pop from stack
- brack open, we add to stack
- if we pop from stack and the previous element is a str, we add to it

abbbabbb c

return .join


axb3[z]4[c]

axb, 3, z, 4, c
"""

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        new_entry = True

        for c in s:
            if c.isnumeric():
                # Was tracking a number previously
                if new_entry:
                    stack.append(c)
                else:
                    if stack and stack[-1].isnumeric():
                        stack[-1] += c
                    else:
                        stack.append(c)

                new_entry = False
            elif c == "[":
                new_entry = True

            elif c == "]":
                # pop 2 elements
                # make a string
                # then keep popping
                # if str: add to str
                # if num: break

                top_str, top_num = stack.pop(), stack.pop()
                top_str = top_str * int(top_num)

                if stack and stack[-1].isalpha():
                    stack[-1] += top_str
                else:
                    stack.append(top_str)

                new_entry = True
            else:
                if stack and stack[-1].isalpha():
                    stack[-1] += c
                else:
                    stack.append(c)

        return(stack[0])

            

        