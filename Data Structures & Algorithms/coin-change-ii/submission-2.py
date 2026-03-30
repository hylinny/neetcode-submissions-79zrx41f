class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # choose to take and stay or skip
        dp = {}
        def solve(i, cum):
            if (i, cum) in dp:
                return dp[(i, cum)]
            if cum == amount:
                return 1
            if cum > amount or i == len(coins):
                return 0
            dp[(i, cum)] = solve(i+1, cum) + solve(i, cum + coins[i])
            return dp[(i, cum)]
        return solve(0, 0)