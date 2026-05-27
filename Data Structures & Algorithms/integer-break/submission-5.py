class Solution:
    def integerBreak(self, n: int) -> int:
        
        dp = {}

        def r(num):
            if num in dp:
                return dp[num]


            dp[num] = num
            for i in range(1, num):
                val = r(i) * r(num-i)
                dp[num] = max(dp[num], val)

            return dp[num]

        return r(n)