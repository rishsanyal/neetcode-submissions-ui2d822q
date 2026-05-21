class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4 != 0:
            return False

        sides = [0] * 4
        side_length = sum(matchsticks) // 4

        matchsticks.sort(reverse=True)

        def dfs(i):
            if i == len(matchsticks):
                return sides[0] == sides[1] == sides[2] == sides[3]

            for idx in range(4):
                if sides[idx] + matchsticks[i] <= side_length:
                    sides[idx] += matchsticks[i]
                    res = dfs(i+1)
                    if res:
                        return True
                    sides[idx] -= matchsticks[i]

            return False


        return dfs(0)