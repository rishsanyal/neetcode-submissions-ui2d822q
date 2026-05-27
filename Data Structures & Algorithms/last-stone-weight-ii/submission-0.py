"""
Why not use a max-heap?

[2,4,1,5,6,3]
[6,5,4,3,2,1]
[4,3,2,1,1]
[2,1,1,1]
[1,1,1]
[1]


[10,7,4,4,1]
[4,4,3,1]
[2]
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
