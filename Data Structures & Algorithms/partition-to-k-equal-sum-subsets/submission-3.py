"""
We want to see if each partition can be equal to sum(nums) // 4

We create a list with k elements
we sort nums
we start recursing through the list 
    and keep checking if adding every element to the list helps
    We either add it to the current index OR we add it to the next element
"""

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)

        if total%k:
            return False

        partition_limit = total // k

        res = [0] * k
        # nums.sort(reverse=True)

        def r(idx):
            if idx == len(nums):
                return True

            for i in range(k):
                if nums[idx] + res[i] <= partition_limit:
                    res[i] += nums[idx]
                    if r(idx+1):
                        return True
                    res[i] -= nums[idx]

            return False

        return r(0)