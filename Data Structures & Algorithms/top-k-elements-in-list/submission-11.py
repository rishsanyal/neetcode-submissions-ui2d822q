"""
Simple approach:
Counter to a heap

create an array of len(nums) of lists
counter and we populate accordingly
"""


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        c = Counter(nums)

        res = [[]]* (len(nums)+1)

        for num, pop in c.items():
            res[pop].append(num)

        tracker = []

        for idx in range(len(res)-1, -1, -1):
            if k <= 0:
                break

            while res[idx] and k > 0:
                tracker.append(res[idx].pop())

                k -= 1

        return tracker
