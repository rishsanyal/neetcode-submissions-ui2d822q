class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = {}


        def dfs(i, turn):
            if i >= n:
                return 0

            if (i, turn) in dp:
                return dp[(i, turn)]

            res = float("-inf") if turn else float("inf")
            score: int = 0

            for j in range(i, min(i+3, n)):
                score += stoneValue[j]
                if turn:
                    res = max(res, score + dfs(j+1, False))
                else:
                    res = min(res, -score + dfs(j+1, True))

            dp[(i, turn)] = res

            return res

        result = dfs(0, True)

        if result == 0:
            return "Tie"

        return "Alice" if result > 0 else "Bob"
