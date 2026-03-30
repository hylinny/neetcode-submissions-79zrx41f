class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        def solve(i, amt):
            if (i, amt) in dp:
                return dp[(i, amt)]
            if amt == amount:
                return 1
            if i == len(coins) or amt > amount:
                return 0
            # choose to skip current
            skip = solve(i+1, amt)
            # choose to take current
            take = solve(i, amt + coins[i])
            dp[(i, amt)] = skip + take
            return dp[(i, amt)]
        return solve(0, 0)