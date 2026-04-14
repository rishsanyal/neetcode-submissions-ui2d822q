class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for operation in operations:
            print(operation, stack)
            if operation == '+':
                res = stack[-1] + stack[-2]
                stack.append(res)
            elif operation == 'D':
                prev = stack[-1]
                stack.append(prev*2)
            elif operation == 'C':
                stack.pop()
            else:
                stack.append(int(operation))

        print(stack)
        return sum(stack)