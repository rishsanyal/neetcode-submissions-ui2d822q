"""
Easy approach:
- Counter
- Heap
- Get top K elements

Run time - O(NlgN)
Space - O(N)


Better approach:
- Count Sort
- We create an empty list of len(n)
- This is a list of lists (since we can have multiple elements with the same count)
- We'll still need to maintain a counter

Run Time - O(N)
Space - O(N)
"""


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tracker = [[] for _ in range (len(nums)+1)]
        c = Counter(nums)

        for num, count in c.items():
            tracker[count].append(num)

        res = []
        idx = len(nums)

        while len(res) < k and idx >= 0:
            while len(res) < k and tracker[idx]:
                res.append(tracker[idx].pop())

            idx -= 1

        return res
            




