"""

The container's dependent on the min of the left wall and the right wall
- We track leftMax, rightMax -> 0, len(nums)-1
- whichever one's smaller, we increment/decrement
- On changing, we add the difference between the current height and the min to the result
"""



class Solution:
    def trap(self, height: List[int]) -> int:

        left, right = 0, len(height)-1
        leftMax, rightMax = height[left], height[right]
        res = 0

        while left < right:

            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                res += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                res += rightMax - height[right]


        return res