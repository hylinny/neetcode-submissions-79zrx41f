class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp: iterate through all coins, and recurse.
        memo = [[-1] * (amount+1) for _ in range(len(coins))]
        def solve(i, amount):
            if i >= len(coins) or amount < 0:
                return 0
            if amount == 0:
                return 1
            if memo[i][amount] != -1:
                return memo[i][amount]
            ways = solve(i, amount - coins[i]) # choose current coin
            ways += solve(i+1, amount) # skip current coin
            memo[i][amount] = ways
            return ways
        return solve(0, amount)
