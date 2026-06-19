"""

We have a res and a stack
we add to stack in decreasing/same order? - decreasing monotonic stack

at each point we compare the heights, 
    if curr area from current index to last index is lte the height, we pop and replace
    else, we add to the stack with the min height and the index from which we're tracking the area

[1,1,1,3,1,3]

we add to the stack in an increasing manner
we pop until we see a lesser or equal height
at which time we take the min index and the min height

we'll need to do a second pass too

1,0
3,5

curr_idx = 5

"""


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        for idx, val in enumerate(heights):
            if not heights:
                stack.append((val, idx))
                continue
            

            val_to_add, idx_to_add = val, idx

            while stack and stack[-1][0] >= val:
                prev_height, prev_idx = stack.pop()

                res = max(
                        res,
                        min(val, prev_height) * (idx-prev_idx)
                    )

                val_to_add, idx_to_add = val, prev_idx

            stack.append((val_to_add, idx_to_add))

        while stack:
            curr_height, curr_idx = stack.pop()

            res = max(
                res,
                curr_height * (len(heights)-curr_idx)
            )

        return res


