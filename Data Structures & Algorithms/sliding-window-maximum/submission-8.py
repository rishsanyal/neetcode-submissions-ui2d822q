"""
We have a real tracker of the window k

we could have a MAX heap with the value and the index

[1,2,3,4,5,6,7]
- n*lg(n)

- Better Solution: I KNEW WE COULD USE A DEQUE!
"""



class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        h = []

        for (idx, num) in enumerate(nums):
            heapq.heappush_max(h, (num, idx))

            if idx < k-1:
                continue

            # check top of heap
            # pop from top of heap until within range
            while not ((idx-k+1) <= h[0][1] <= (idx+1)):
                # print(idx-k+1, h[0][1], idx+1, idx)
                heapq.heappop_max(h)

            # print(h)

            res.append(h[0][0])

        return res
            

            