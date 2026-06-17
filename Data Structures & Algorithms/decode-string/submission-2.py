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

        curr_str = ''
        tracking_num = False
        stack = []

        for c in s:
            if c.isnumeric():
                # Was tracking a number previously
                if tracking_num:
                    curr_str += c
                # was tracking a str
                else:
                    if curr_str:
                        stack.append(curr_str)

                    curr_str = c
                    tracking_num = True
            elif c == "[":
                if curr_str:
                    stack.append(curr_str)
                curr_str = ''
                tracking_num = False
            elif c == "]":
                # if curr_str:
                #     stack.append(curr_str)

                if stack and (stack[-1].isalpha()):
                    stack[-1] += curr_str
                else:
                    stack.append(curr_str)

                curr_str = ''
                tracking_num = False

                # pop 2 elements
                # make a string
                # then keep popping
                # if str: add to str
                # if num: break

                print(stack)

                top_str, top_num = stack.pop(), stack.pop()
                top_str = top_str * int(top_num)

                if stack and stack[-1].isalpha():
                    stack[-1] += top_str
                else:
                    stack.append(top_str)

                
                print(stack)
            else:
                if tracking_num:
                    if curr_str:
                        stack.append(curr_str)
                    curr_str = ''
                    tracking_num = False
                
                curr_str += c

        if curr_str:
            stack.append(curr_str)
            curr_str = ''

        return("".join(stack))

            

        