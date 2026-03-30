class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def solution(i, isBuying):
            if i >= len(prices):
                return 0
            if (i, isBuying) in dp:
                return dp[(i, isBuying)]
            cooldown = solution(i+1, isBuying)
            if isBuying: # we can currently buy
                profit = solution(i+1, not isBuying) -  prices[i] # flip to sell
                dp[(i, isBuying)] = max(cooldown, profit)
            else: # we can currently sell
                profit = solution(i+2, not isBuying) + prices[i]
                dp[(i, isBuying)] = max(cooldown, profit)
            return dp[(i, isBuying)]
        return solution(0, True)