"""
HINT: 2 Heaps of equal size

One Max heap and one Min heap


max_heap, min_heap, num
[], [], 1
[1], [], 2
[1,2], [], 3
[1,2], [3], 4
[1,2], [3,4], 5
[1,2,3], [4,5]

Max heap of smaller numbers and min heap of bigger numbers

we add to the min_heap
if len is equal, we pop from the min heap and populate the max_heap
max_heap should always have 0 or 1 greater elements

"""


class MedianFinder:
    # import heapq

    def __init__(self):
        # For smaller numbers
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if self.max_heap and num < self.max_heap[0]:
            heapq.heappush_max(self.max_heap, num)
        else:
            heapq.heappush(self.min_heap, num)

        if len(self.min_heap) > len(self.max_heap) + 1:
            num_to_pop = heapq.heappop(self.min_heap)
            heapq.heappush_max(self.max_heap, num_to_pop)
        elif len(self.max_heap) > len(self.min_heap) + 1:
            num_to_pop = heapq.heappop_max(self.max_heap)
            heapq.heappush(self.min_heap, num_to_pop)

        print(self.max_heap, self.min_heap, num)

        return


    def findMedian(self) -> float:
        result = 0

        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        elif len(self.max_heap) > len(self.min_heap):
            return self.max_heap[0]
        else:
            return (self.min_heap[0] + self.max_heap[0]) / 2
