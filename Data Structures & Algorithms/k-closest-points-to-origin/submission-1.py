"""
- get distance
- put in a heap by distance and points

"""

import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(cx, cy):
            return math.sqrt((cx)**2 + (cy)**2)

        h = []
        res = []

        for (x, y) in points:
            heapq.heappush(h, (distance(x, y), (x, y)))


        while k > 0 and h:
            res.append(
                heapq.heappop(h)[1]
            )

            k -= 1

        return res

