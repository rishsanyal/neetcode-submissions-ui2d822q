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

        h = []
        l = 0

        res = []

        for idx in range(len(nums)):
            val = nums[idx]
            r = l + k - 1

            while len(h) >=k and not (l <= h[0][1] <= r):
                # print('popping')
                heapq.heappop_max(h)

            if idx >= k:
                # print(h, l, r)
                res.append(h[0][0])
                l += 1

            heapq.heappush_max(h, (val, idx))

        return res + [h[0][0]]
        