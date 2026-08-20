"""


- at each level we can take coin amount away

3, [1,2]
"Return the fewest number of coins" - we always go for the biggest ones possible?

cache = {}

track curr_amount, num_curr_coins=0
if curr_amount == 0:
    res = min(res, num_curr_coins)
    return num_curr_coins

if curr_amount in cache:
    return cache[curr_amount]

for coin in coins:
    if coin > amount:
        continue

    cache[curr_amount] = min(
        r(curr_amount-coin, num_curr_coins+1),
        cache[curr_amount]
    )

return cache[curr_amount]

    






"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        for i in coins:
            cache[i] = 1

        res = float('inf')

        def r(curr_amount, num_curr_coins):

            if curr_amount == 0:
                return num_curr_coins

            if curr_amount < 0:
                return float('inf')

            if curr_amount in cache:
                return num_curr_coins + cache[curr_amount]

            cache[curr_amount] = float('inf')

            for coin in coins:
                cache[curr_amount] = min(
                    r(curr_amount-coin, num_curr_coins+1),
                    cache[curr_amount]
                )

            return cache[curr_amount]

        res = r(amount, 0) 

        return res if res != float('inf') else -1