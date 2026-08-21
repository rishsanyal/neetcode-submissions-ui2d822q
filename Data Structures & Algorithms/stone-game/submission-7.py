"""

Easy way out - We cache turn l r
"""

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        cache = {}

        def dfs(turn, l, r, curr_sum):

            if l > r:
                return curr_sum

            if (turn, l, r) in cache:
                return cache[(turn, l, r)]

            cache[(turn, l, r)] = 0

            if turn:
                cache[(turn, l, r)] = max(
                    dfs(not turn, l+1, r, curr_sum+piles[l]),
                    dfs(not turn, l, r-1, curr_sum+piles[r]),
                )
            else:
                cache[(turn, l, r)] = max(
                    dfs(not turn, l+1, r, curr_sum),
                    dfs(not turn, l, r-1, curr_sum),
                )

            return cache[(turn, l, r)]

        return (dfs(True, 0, len(piles)-1, 0) >= len(piles)/2)
