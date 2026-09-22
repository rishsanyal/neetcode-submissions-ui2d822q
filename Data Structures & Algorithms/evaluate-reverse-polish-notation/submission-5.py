"""
We'd maintain a stack and every time we see an operation, we pop 2
The stack is invalid if
    we get an operation AND the len < 2
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for t in tokens:

            if t.isnumeric() or t[1:].isnumeric():
                stack.append(int(t))
            else:
                if len(stack) < 2:
                    return -1

                prev_num, next_num = stack.pop(), stack.pop()

                res = -1

                if t == '*':
                    res = int(prev_num) * int(next_num)

                if t == '+':
                    res = int(prev_num) + int(next_num)

                if t == '-':
                    res = int(next_num) - int(prev_num)

                if t == '/':
                    res = int(next_num)/int(prev_num)

                stack.append(res)

        return int(stack[-1])