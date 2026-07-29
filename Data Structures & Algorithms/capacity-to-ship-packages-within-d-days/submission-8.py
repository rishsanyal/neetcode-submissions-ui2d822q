"""
We need to check the rate of packages shipped
"""


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def __check(max_weight):
            itr = 0
            days = 0
            curr_weight = 0

            while itr < len(weights):
                if (curr_weight + weights[itr]) > max_weight:
                    days += 1
                    curr_weight = weights[itr]
                elif (curr_weight + weights[itr]) < max_weight:
                    curr_weight += weights[itr]
                else:
                    days += 1
                    curr_weight = 0

                itr += 1

            if curr_weight > 0:
                days += 1

            return days



        l, r = max(weights), max(weights)*len(weights)

        res = 0

        while l <= r:
            mid = (l+r)//2

            if __check(mid) <= days:
                # Go smaller
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res