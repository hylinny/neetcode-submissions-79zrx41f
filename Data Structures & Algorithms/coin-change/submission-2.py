class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def solve(i, amt):
            if (i, amt) in dp:
                return dp[(i, amt)]
            if i == 0 and amt == 0:
                return 0
            if i == 0 and amt > 0:
                return float('inf')
            # choose to skip or take
            minCoins = float('inf')
            if amt - coins[i-1] >= 0:
                # take
                minCoins = min(minCoins, 1 + solve(i, amt - coins[i-1]))
            # skip
            minCoins = min(minCoins, solve(i-1, amt))
            dp[(i, amt)] = minCoins
            return minCoins
        ans = solve(len(coins), amount)
        return ans if ans != float('inf') else -1

