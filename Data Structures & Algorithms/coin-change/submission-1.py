"""
on each level, we decrease the amount by the coin
cache -- amount, prev_coin - ?

(12, 0) = min((11, 1), (7, 1), (2, 1))

"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        coins.sort(reverse=True)
        cache = defaultdict(lambda: float('inf'))
        
        def r(curr_amt, num_coins):
            if curr_amt in cache:
                return cache[curr_amt]

            if curr_amt >= amount:
                if (curr_amt == amount):
                    cache[curr_amt] = num_coins
                    return cache[curr_amt]

                return float('inf')

            for c in coins:
                cache[curr_amt] = min(r(curr_amt+c, num_coins+1), cache[curr_amt])

            return cache[curr_amt]

        res = r(0, 0)

        return res if res != float('inf') else -1
                

