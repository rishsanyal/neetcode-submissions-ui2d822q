class KthLargest:
    """
    We maintain a heap of K elements
    on every insertion we insert in heap and if it's length == K+1 -> we pop

    but we want the Kth largest.
    We need to maintain a min heap and get the max at every point?

    do we just maintain a min heap of K points at every time?
    """

    def __init__(self, k: int, nums: List[int]):
        import heapq
        
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)

        while len(self.nums) > k:
            heapq.heappop(self.nums)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)


        return self.nums[0]

        
