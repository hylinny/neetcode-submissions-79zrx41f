class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[a] represents the minimum coins needed to make amount 'a'
        # We fill it with infinity, except for amount 0 which takes 0 coins
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        # recursive 'amt' increasing
        for a in range(1, amount + 1):
            # 'take or skip' choices
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
                    
        return dp[amount] if dp[amount] != float('inf') else -1

