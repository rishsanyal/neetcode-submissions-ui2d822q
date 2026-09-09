"""
Simple approach:
Counter to a heap

create an array of len(nums) of lists
counter and we populate accordingly
"""


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        c = OrderedDict()

        for num in nums:
            curr_population = c.get(num, 0)

            c[num] = curr_population + 1

            c.move_to_end(num)

        res = []
        while c and (k > 0):
            key, val = c.popitem(last=True)

            res.append(key)

            k -= 1

        return res


