"""
Why not use a max-heap?

[31,26,33,21,40]

[40,33,31,26,21]
[31,26,21,7]
[21,7,5]
[14,5]
[9]


"""

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while stones and len(stones) >= 2:
            stone1, stone2 = heapq.heappop_max(stones), heapq.heappop_max(stones)
            diff = stone1 - stone2

            if diff:
                heapq.heappush_max(stones, diff)

        if len(stones) == 1:
            return stones[0]

        return 0