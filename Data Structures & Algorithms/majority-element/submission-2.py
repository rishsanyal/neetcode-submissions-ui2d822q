"""
Not sure what the law here is called

We have a count and a number per element
if the number is the same, we continue
else: we reduce and if the count <= 0: we switch

5,1
5,2
5,1
1,1
1,2
1,1
5,1

Assuming a majority always exists
"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr_num, count = nums[0], 0

        for num in nums:
            if num == curr_num:
                count += 1
            else:
                count -= 1

                if count == 0:
                    curr_num = num
                    count = 1

        return curr_num
        