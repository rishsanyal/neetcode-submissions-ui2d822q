"""

We can track leftmax and rightmax
but how do we know to add/remove
- if left max, right max is the same as the previous ones?

We track height, index

[0,2,0,3,1,0,1,3,2,1]
[0,2,2,3,3,3,3,3,3,3] left_max
[3,3,3,3,3,3,3,3,2,1] right_max
"""


class Solution:
    def trap(self, height: List[int]) -> int:

        left_max = []
        right_max = []

        curr_max = 0
        for i in range(len(height)):
            curr_max = max(height[i], curr_max)
            left_max.append(curr_max)

        curr_max = 0
        for i in range(len(height)-1, -1, -1):
            curr_max = max(height[i], curr_max)
            right_max.insert(0, curr_max)

        res = 0

        for i in range(len(height)):
            res += min(left_max[i], right_max[i]) - height[i]

        return res


        