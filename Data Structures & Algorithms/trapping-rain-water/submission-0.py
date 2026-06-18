"""

We need to get the highest right wall for the left wall

- we iterate and get the max at every point

[0,2,0,3,1,0,1,3,2,1]
max right - [3,3,3,3,3,3,3,3,2,1]
max left - [0,2,2,3,3,3,3,3,3,3]
min from both - [0,2,2,3,3,3,3,3,2,1]


[0,2,2,3,3,3,3,3,2,1]
[0,2,0,3,1,0,1,3,2,1]
[0,0,2,0,2,3,2,0,0,0] - 9
"""



class Solution:
    def trap(self, height: List[int]) -> int:

        # get max right
        max_right = []
        curr_max = 0

        for i in range(len(height)-1, -1, -1):
            curr_max = max(height[i], curr_max)
            max_right.insert(0, curr_max)

        
        curr_max = 0
        max_left = []

        for i in range(len(height)):
            curr_max = max(height[i], curr_max)
            max_left.append(curr_max)

        min_both = []

        for i in range(len(height)):
            min_both.append(
                min(max_right[i], max_left[i])
            )

        res = 0

        for i in range(len(height)):
            res += min_both[i] - height[i]
        
        return res