class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        2 parts to this problem
            1. Search the least max_weight - N
            2. Validate that max_weight sends the packages in N days

            We want the least weight, in the number of days
            We care more about weight than days
        """

        def validate_weight(max_weight):
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
        ans = max(weights)

        while l < r:
            mid_weight = (l+r)//2
            possible = (validate_weight(mid_weight) <= days)
            
            if not possible:
                # go right
                l = mid_weight + 1
            else:
                # go left
                ans = min(ans, mid_weight)
                r = mid_weight - 1

        return l

