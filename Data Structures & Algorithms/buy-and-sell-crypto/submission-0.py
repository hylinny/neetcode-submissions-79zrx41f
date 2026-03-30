class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        minelement = float('inf')
        for num in prices:
            if num < minelement:
                minelement = num
            maxprofit = max(maxprofit, num - minelement)
        return maxprofit
            