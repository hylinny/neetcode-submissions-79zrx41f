class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # ways that we can include current coin: 12 - currentamount, rest of coins
        # ways that we can exclude current coin: 12, rest of coins
        memo = {}
        def function(coins, amount):
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]
            # amount > 0, recursive step
            minimumCoins = float('inf')
            for coin in coins:
                if amount - coin >= 0:
                    minimumCoins = min(
                        minimumCoins, 
                        1 + function(coins, amount - coin)
                    )
            memo[amount] = minimumCoins
            return minimumCoins
        minCoins = function(coins, amount)
        return -1 if minCoins == float('inf') else minCoins

                