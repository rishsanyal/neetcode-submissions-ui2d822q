"""
At each turn, we track which stone was picked

Alice, 1, 3 -> 1
Alice, 0, 2 -> 1



"""



class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        THRESHOLD = sum(piles) / 2
        cache = {}

        def dfs(turn, l, r):
            if l > r:
                return 0

            if (turn, l, r) in cache:
                return cache[(turn, l , r)]

            if turn:
                cache[(turn, l , r)] = max(
                    piles[l] + dfs(not turn, l+1, r),
                    piles[r] + dfs(not turn, l, r-1)
                )
            else:
                cache[(turn, l , r)] = max(
                    dfs(not turn, l+1, r),
                    dfs(not turn, l, r-1)
                )

            return cache[(turn, l , r)]

        return (dfs(True, 0, len(piles)-1) > THRESHOLD)

            

            
        