class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        We need a stack of temperatures and their indices.

        [22,21,23]

                0, 22
                1, 21
        

        we pop till we see a higher count
        then push onto the stack
        then we might need to do another pass too? - What if they're in decreasing order?

        We can track results with another list
        """

        results = [0] * len(temperatures)
        stack = []

        for idx, temperature in enumerate(temperatures):
            if stack and stack[-1][1] < temperature:
                while stack and stack[-1][1] < temperature:
                    prev_idx, _ = stack.pop()
                    results[prev_idx] = idx - prev_idx

            stack.append((idx, temperature))

        return results


        

        



