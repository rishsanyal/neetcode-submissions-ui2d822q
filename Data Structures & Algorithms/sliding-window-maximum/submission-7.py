"""
we have l, r = 0, k-1

maintain a max heap of size k
we inser (val, idx) in it

we start with a heap of the first k elements


we pop from the heap until the top is in the range l, r
we get the top of the heap
we append to the result
we slide the window, l+=1 r+=1
"""



class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        if len(nums) < k:
            return []

        import heapq

        res = []
        h = []
        l = 0

        for idx in range(len(nums)):
            heapq.heappush_max(h, (nums[idx], idx))

            if idx >= k-1:
                while h[0][1] <= idx - k:
                    heapq.heappop_max(h)
                res.append(h[0][0])

        return res
        