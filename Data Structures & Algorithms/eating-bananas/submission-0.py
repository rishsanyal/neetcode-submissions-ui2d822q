class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        """
        There's 2 parts to this question
        1. Find the min speed of eating bananas
            - Binary Search (O(LgN))
        2. Validate the speed of eating bananas
        """

        def get_hours(inp):

            if inp == 0:
                return h+1
            res = 0
            for curr_pile in piles:
                res += math.ceil(curr_pile/inp)
            return res

        l, r = 0, max(piles)
        ans = max(piles)

        while l <= r:
            mid = (l+r)//2
            num_hours = get_hours(mid)

            print(num_hours)

            if num_hours <= h:
                ans = min(mid, ans)
                r = mid-1
            else:
                l = mid + 1

        return ans