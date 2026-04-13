class Solution:


    import heapq
    from collections import Counter, defaultdict

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # We'll have a map for count
        # We'll have 2 pointers, and set them in order
        # a list of 2 elements
        
        # Create a heap with population as the key
        # might have duplicates, but that's fine

        result = []
        popn_map = Counter(nums)
        val_heap = []

        for i, val in popn_map.items():
            # Need a max heap
            # NOT A FUCKING MIN HEAP
            heapq.heappush(val_heap, (-1*val, i))

        while val_heap and len(result) < k:
            curr_val, curr_num = heapq.heappop(val_heap)
            result.append(curr_num)

        return result





        