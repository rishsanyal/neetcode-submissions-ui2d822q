"""


We use 2 heaps
- Max heap of small numbers
- Min heap of big numbers

On every push, we push onto max heap
when the difference in the length is more than 1
    we push from the max heap onto the min heap
in the end, if equal, pick the first element of both and average
of pick the max heap top


max_h, min_h
--------
[1], []
--------
[1], [2]
--------
[1], [2,3]
--------
[1], [2,3,4]
[2,1], [3,4]


we want to keep the smaller numbers in the max heap and bigger ones in min heap


"""


class MedianFinder:

    def __init__(self):
        self.max_h, self.min_h = [], []

    def addNum(self, num: int) -> None:

        if self.max_h and num <= self.max_h[0]:
            heapq.heappush_max(self.max_h, num)
        else:
            heapq.heappush(self.min_h, num)

        if len(self.max_h) - len(self.min_h) == 2:
            max_num = heapq.heappop_max(self.max_h)
            heapq.heappush(self.min_h, max_num)
        if len(self.min_h) - len(self.max_h) == 2:
            min_num = heapq.heappop(self.min_h)
            heapq.heappush_max(self.max_h, min_num)

        
    def findMedian(self) -> float:
        # print(self.max_h, self.min_h)

        res = 0
        if self.max_h and len(self.max_h) == len(self.min_h):
            res = (self.max_h[0] + self.min_h[0])/2
        elif len(self.max_h) > len(self.min_h):
            res = self.max_h[0]
        elif len(self.max_h) < len(self.min_h):
            res = self.min_h[0]
        

        return res
        
        
        