class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for operation in operations:
            if operation == '+':
                l, r = stack.pop(-1), stack.pop(-1)
                res = l + r
                stack.append(l)
                stack.append(r)
                stack.append(res)
            elif operation == 'D':
                prev = stack.pop(-1)
                stack.append(prev)
                stack.append(prev*2)
            elif operation == 'C':
                stack.pop(-1)
            else:
                stack.append(int(operation))

        print(stack)
        return sum(stack)