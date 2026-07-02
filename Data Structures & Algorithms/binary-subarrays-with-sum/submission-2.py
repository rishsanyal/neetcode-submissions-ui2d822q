class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        cache = defaultdict(int)
        cache[0] = 1


        curr_sum = 0
        res = 0

        for num in nums:
            curr_sum += num
            res += cache[curr_sum - goal]

            cache[curr_sum] += 1

        return res