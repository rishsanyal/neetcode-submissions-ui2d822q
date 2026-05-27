"""
We need to track which path we're going on
We either have lt_sign = 0 for 

odd-even-odd
big-small-big - 0
small-big-small - 1

If we start out with a number, we reset teh sign based on the current 
start from 1 to len(arr)

if the sign is the same and previous, we continue
if the sign is different, we have to restart
BUT
what if the numbers are equal??
How do we handle that?
We assume the sign is the same if the numbers are different

[1,1,2]
"""

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1

        lt_sign = 0
        res = count = 0

        for idx in range(len(arr)-1):
            if arr[idx] < arr[idx+1]:
                if lt_sign == 0:
                    count += 1
                else:
                    count = 1
                lt_sign = 1
            elif arr[idx] > arr[idx+1]:
                if lt_sign == 1:
                    count += 1
                else:
                    count = 1

                lt_sign = 0
            else:
                count = 1
                lt_sign = 0


            res = max(res, count)

        return res

        


                

