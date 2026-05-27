"""

We can keep jumping but the max idex we go to cannot be 1
we don't update the max distance as we go on
we make one trip, reach the end and jump from there
we can jump between minJump and maxJump


we jump from min_jump+idx, max_jump+idx
check the index of the last 0 in there and make that our new origin

if the origin is same as previous origin we return False
if the new origin is gte len(s) we return True

s = "0010", minJump = 1, maxJump = 1 - False

"00110010" minJump = 2, maxJump = 4

"0000000001" minJump = 2, maxJump = 5
0 - 2 - 5

"""

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        origin = 0

        while origin < len(s):
            prev_origin = origin

            for new_idx in range(origin+minJump, origin+maxJump+1):
                if s[new_idx] == '0':
                    origin = max(origin, new_idx)

            if origin == prev_origin:
                return False
        
        return origin == len(s)-1

        