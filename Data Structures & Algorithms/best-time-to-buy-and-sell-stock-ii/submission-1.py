class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # at current step, if we are buying, we can choose to
        # buy then flip to selling state, or skip current and stay at buying state
        # if we are selling, we can choose to sell then flip to buying,
        # or skip current and stay at selling state
        dp = {}
        def solve(i, isBuying):
            if (i, isBuying) in dp:
                return dp[(i, isBuying)]
            if i == len(prices):
                return 0
            profit = 0
            if isBuying:
                profit = max(solve(i+1, isBuying), -prices[i] + solve(i+1, not isBuying))
            else:
                profit = max(solve(i+1, isBuying), prices[i] + solve(i+1, not isBuying))
            dp[(i, isBuying)] = profit
            return profit
        return solve(0, True)