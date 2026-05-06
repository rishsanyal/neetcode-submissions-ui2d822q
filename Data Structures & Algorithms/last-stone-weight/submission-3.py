class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq

        """
        We create a max heap with stones

        if len(stones) >= 2: we pop 2 and compare
        elif len(stones) == 1: return
        else:
            return 0

        [2,3,6,2,4]

        [6,4,3,2,2]

        [3,2,2,2]

        [2,2,1]

        [1]        
        """
        heapq.heapify_max(stones)
        while len(stones) >= 2:
            x, y = heapq.heappop_max(stones), heapq.heappop_max(stones)
            heapq.heappush_max(stones, x-y)

        return stones[0] if stones else 0