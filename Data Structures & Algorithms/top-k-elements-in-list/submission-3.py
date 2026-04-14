class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        """
        Use a heap by counter
        We have a dict counter and a heap

        We only have to maintain K elements right or atleast return K elements

        We can leverage the dictionary insertion order actually.

        We store in heap vs a dict, it's the same 
        We'll end up storing the entire count in the dict though
        Does a heap only store the top k elements?
        Yeah it does, but what if something builds up after k elements?
        """

        tracker = defaultdict(int)

        for num in nums:
            num_count = 0
            if num in tracker:
                num_count, _ = tracker.pop(num)
                num_count *= -1
            tracker[num] = (-1 * (num_count + 1), num)

        curr_list = list(tracker.values())
        heapq.heapify(curr_list)
        return [i for _,i in curr_list[:k]]
        