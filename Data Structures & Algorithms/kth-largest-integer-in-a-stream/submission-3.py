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
        heapq.heapify_max(self.nums)

        temp = []

        while len(temp) < k and self.nums:
            temp.append(heapq.heappop_max(self.nums))

        self.nums, temp = temp, self.nums

        heapq.heapify(self.nums)
        
    def add(self, val: int) -> int:
        if len(self.nums) >= self.k:
            heapq.heappop(self.nums)
            
        heapq.heappush(self.nums, val)

        res = heapq.heappop(self.nums)
        heapq.heappush(self.nums, res)

        return res

        
