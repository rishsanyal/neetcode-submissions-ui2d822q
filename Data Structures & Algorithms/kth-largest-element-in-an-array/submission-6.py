"""
We pop it all in a max heap
pop k elements


[2,3,1,5,4]
[5,4,3,2,1] k = 2

sort and len(nums)-kth index
"""



class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []

        if k >= len(nums):
            return -1

        for num in nums:
            heapq.heappush_max(h, num)

        res = -1

        while k >= 0:
            res = heapq.heappop_max(h)
            k -= 1

        return res
