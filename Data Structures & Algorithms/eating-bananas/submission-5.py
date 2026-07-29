"""

Rate at which Koko can eat 0 - max(piles)
Given hours

Check if that number works
Number of hours for a pile = (pile // rate) + 1 if (pile % rate) else 0

"""

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def __check(inp):
            count = 0

            if inp == 0:
                return float('inf')

            for pile in piles:
                count += (pile // inp) + bool(pile % inp)

            return count

        res = 0
        l, r = 0, max(piles)

        while l <= r:
            mid = (l + r) // 2

            if __check(mid) > h:
                # Increase rate
                l = mid + 1
            else:
                # Go smaller
                r = mid - 1
                res = mid

        return res