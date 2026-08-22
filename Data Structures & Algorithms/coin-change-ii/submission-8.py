"""
Success means reaching amount - return 1

we need to track the indices possible since we only want distinct combinations
curr sum


"""



class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        res = 0
        cache = {}

        def r(allowed_idx, curr_amount):

            if curr_amount >= amount:
                return int(curr_amount == amount)

            if (allowed_idx, curr_amount) in cache:
                return cache[(allowed_idx, curr_amount)]

            cache[(allowed_idx, curr_amount)] = 0

            for i in range(allowed_idx, len(coins)):
                cache[(allowed_idx, curr_amount)] += r(i, curr_amount + coins[i])

            return cache[(allowed_idx, curr_amount)]

        return r(0, 0)