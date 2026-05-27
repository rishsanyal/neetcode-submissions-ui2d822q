"""
Why not use a max-heap?

[31,26,33,21,40]

[40,33,31,26,21]
[31,26,21,7]
[21,7,5]
[14,5]
[9]

151//2 ~ 75



"""

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total_sum = sum(stones)
        target = total_sum // 2

        cache = {}

        def r(idx, curr_sum):
            if curr_sum >= target or idx >= len(stones):
                return abs(curr_sum - (total_sum - curr_sum))

            if (idx, curr_sum) in cache:
                return cache[(idx, curr_sum)]

            cache[(idx, curr_sum)] = min(r(idx+1, curr_sum), r(idx+1, curr_sum + stones[idx]))

            return cache[(idx, curr_sum)]

        return r(0, 0)