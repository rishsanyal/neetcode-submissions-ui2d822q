"""

We're given a set of coins
we have to get the total combinations to get an amount

we have to use backtracking since we have O(N) choices at every level

we can't go over the total amount

we track the current amount
for every option we add the current amount and go on
if we exceed the amount, we return

at each point we either skip a coin or pick it
"""

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        ans = 0

        cache = {}

        def r(idx, curr_sum):
            if curr_sum > amount:
                return 0
            
            if curr_sum == amount:
                return 1

            if (idx, curr_sum) in cache:
                return cache[(idx, curr_sum)]
            
            res = 0

            # We repeat the current coin
            res += r(idx, curr_sum + coins[idx])

            # We try new coins
            for i in range(idx+1, len(coins)):
                res += r(i, curr_sum + coins[i])

            cache[(idx, curr_sum)] = res

            return cache[(idx, curr_sum)]

        ans = 0

        ans += r(0, 0)
        
        return ans
            
