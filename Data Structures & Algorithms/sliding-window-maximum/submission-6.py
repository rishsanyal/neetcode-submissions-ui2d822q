"""
we need to track index and value

We have 2 pointers l and r, 0,0
we have a deque that holds the previous values

as we iterate through the input list -> using r as iterator -> while r < len(nums)
    - we pop from deque if current element (nums[r]) > last element of deque
        - while deque and deque[-1][val] < nums[r]: pop
    - we add nums[r] to the deque
    - while: we pop from left side if h[0][idx] < l
        - h.popleft
    - if r >= k-1, 
        - we add deque[-1][value] to result list
        - l += 1

- return res


[1,2,1,0,4,2,6], k = 3

d  l  r
[2] 0 1
[2, 1] 0, 2 - [2]
[2, 1, 0] 1, 3 - [2]

"""

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        d = deque() # idx, val
        l, r = 0, 0
        res = []

        while r < len(nums):
            while d and nums[r] > d[-1][1]:
                d.pop()

            d.append((r, nums[r]))

            while d[0][0] < l:
                d.popleft()

            if r >= k-1:
                res.append(d[0][-1])
                l += 1

            r += 1

        return res


            

