"""
Use a deque to maintain the max number of a queue


the biggest number on the left
the smaller numbers on the right

if we see a big number, we start popping from the left until we can
if the number on the left has a smaller index than l, we popleft

[1,2,1,0,4,2,6]

d
1
2
2,1
2,1,0
4
4,2
6

"""

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque()
        res = []

        for (idx, num) in enumerate(nums):
            if not d or d[-1][0] >= num:
                d.append((num, idx))
            else:
                while d and d[-1][0] < num:
                    d.pop()

                d.append((num, idx))

            while d and d[0][1] < (idx-k):
                d.popleft()

            if idx >= (k-1):
                res.append(d[0][0])

        return res

            