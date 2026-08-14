"""

Weird stack problem

we have a global res
if a smaller number comes, we push the curr h and idx to the stack?
if a greater or equal number comes, we pop the stack and track from there
    we keep popping from the stack with the smaller or equal value
    we track the smallest number while popping and keep going
    if no stack, we append and move on

when this is over, we just return the global result

7,1,7,2,2,4,5

we need to track min height, last applicable index, current index, curr_idx height

"""



class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        res = heights[0]
        stack = []


        for idx, h in enumerate(heights):
            idx_to_add = idx

            while stack and h <= stack[-1][0]:
                prev_h, prev_idx = stack.pop()

                res = max(
                    res,
                    prev_h*(idx - prev_idx)
                )

                idx_to_add = prev_idx

            stack.append((h, idx_to_add))
        
        while stack:
            curr_h, curr_idx = stack.pop()

            res = max(
                res,
                curr_h * (len(heights) - curr_idx)
            )

        return res