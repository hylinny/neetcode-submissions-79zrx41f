class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        chosen = prices[0]
        maxProfit = 0
        for i in range(1, len(prices)):
            if prices[i] > chosen:
                maxProfit = max(maxProfit, prices[i] - chosen)
            else:
                chosen = prices[i]
        return maxProfit