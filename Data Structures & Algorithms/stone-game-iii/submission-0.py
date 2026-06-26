"""
Looks like a DP problem

On each level, we can do one of three steps

player picks 1-3 
stone value could be negative TOO

highest score possible is all the positive numbers in the stoneValue
We can calculate only Alice's score

on every alice turn, we have idx
we pick up idx, idx+1, idx+2

track max score from those three

Could be a tie too

cache by index

What's the max score possible from the first 1-3 indices?
pick that for player

"""


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        
        highest_score = sum(stoneValue)
        cache = {}

        def dfs(idx, turn):
            if idx >= len(stoneValue):
                return 0

            res = 0

            res, num_piles = stoneValue[idx], 1

            if idx+1 < len(stoneValue) and stoneValue[idx] < (stoneValue[idx] + stoneValue[idx+1]):            
                res, num_piles = (stoneValue[idx] + stoneValue[idx+1]), 2

            if idx+2 < len(stoneValue) and (stoneValue[idx] + stoneValue[idx+1] + stoneValue[idx+2]) > (stoneValue[idx] + stoneValue[idx+1]):
                res, num_piles = (stoneValue[idx] + stoneValue[idx+1] + stoneValue[idx+2]), 3
            
            cache[(idx, turn)] = res

            dfs(idx+num_piles, not turn)

            return res

        dfs(0, True)

        print(cache, highest_score)

        if cache[(0, True)] == highest_score / 2:
            return "Tie"

        return "Alice" if (cache[(0, True)]) >= (highest_score/2) else "Bob"





        