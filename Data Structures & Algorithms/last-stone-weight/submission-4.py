class Solution:
    import heapq

    def lastStoneWeight(self, stones: List[int]) -> int:
        h = stones

        heapq.heapify_max(h)

        while len(h) >= 2:
            stone1, stone2 = heapq.heappop_max(h), heapq.heappop_max(h)

            if stone1 == stone2:
                continue
            elif stone1 > stone2:
                heapq.heappush_max(h, stone1 - stone2)
            elif stone1 < stone2:
                heapq.heappush_max(h, stone2 - stone1)

        return h[0] if h else 0

