"""
We need distinct integers, because of that we need to limit the options of of coins available

"""

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        cache = {}
        res = 0

        def r(curr_idx, curr_sum):
            if (curr_idx, curr_sum) in cache:
                return cache[(curr_idx, curr_sum)]

            if curr_sum == amount:
                return 1

            if curr_sum < 0 or curr_sum > amount:
                return 0

            ans = 0

            for i in range(curr_idx, len(coins)):
                ans += r(i, curr_sum+coins[i])

            cache[(curr_idx, curr_sum)] = ans

            return ans

        return r(0, 0)

        