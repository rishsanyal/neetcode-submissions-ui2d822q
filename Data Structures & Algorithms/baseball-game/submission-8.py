class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == 'C':
                stack.pop(0)
            elif op == '+':
                num1, num2 = stack[0], stack[1]
                stack.insert(0, num1 + num2)
            elif op == 'D':
                num1 = stack[0]
                stack.insert(0, num1 * 2)
            else:
                stack.insert(0, int(op))

            print(stack)

        return sum(stack)
