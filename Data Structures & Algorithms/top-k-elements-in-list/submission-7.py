"""
1. Use a heap counter
2. Use an ordered dict and update the count and pop from dict
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        for i in nums:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1

        print(counter)

        freq = [[] for _ in range(len(nums)+1)]

        for num, count in counter.items():
            freq[count].append(num)

        res = []

        for i in range(len(nums), -1, -1):
            while freq[i] and k:
                res.append(freq[i].pop())
                k -= 1

            if k == 0:
                break

        return res


