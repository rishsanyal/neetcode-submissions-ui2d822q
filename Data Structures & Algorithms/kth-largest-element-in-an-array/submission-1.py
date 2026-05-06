class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        we create a min heap and pop until the list == k and return the first element
        """

        import heapq
        
        h = [-1 * i for i in nums]
        heapq.heapify(h)
        count = 0
        res = None

        while k:
            res = heapq.heappop(h)
            k -= 1

        return -1*res