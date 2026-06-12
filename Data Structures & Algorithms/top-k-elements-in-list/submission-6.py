"""
1. Use a heap counter
2. Use an ordered dict and update the count and pop from dict
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = OrderedDict()

        for i in nums:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1

            counter.move_to_end(i)


        res = []

        for _ in range(k):
            res.append(counter.popitem()[0])

        return res