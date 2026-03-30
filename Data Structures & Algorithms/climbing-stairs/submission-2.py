class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        def solve(i):
            if i == 0 or i == 1:
                return 1
            if i in dp:
                return dp[i]
            dp[i] = solve(i-1) + solve(i-2)
            return dp[i]
        return solve(n)