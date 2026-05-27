"""

We want to track the lte status to track count
if the sign is opposite the last one, we increase count
if the sign isn't opposite, then we restart count
if it's equal, we could just keep counting and the flag is opposite

small-big-small - 1
big-small-big - 0
"""

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        # tracks the expected relation between idx-1 and idx
        # should be true if idx-1 < idx
        lt_sign = True
        res = count = 0

        for i in range(1, len(arr)):
            if arr[i-1] < arr[i]:
                count += int(lt_sign)
                lt_sign = not lt_sign
            elif arr[i-1] > arr[i]:
                count += int(not lt_sign)
                lt_sign = not lt_sign
            else:
                count = 0
                lt_sign = True

            res = max(res, count)

        return res + 1



        