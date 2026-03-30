class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # currently, decision to take left or right comes from 
        # max(stones won if left taken + left stones, stones won if right taken + right stones)
        # 2d dp to represent whose turn it is
        dp = [[-1] * len(piles) for _ in range(len(piles))]
        def solve(l, r, turn):
            if l > r:
                return 0
            if dp[l][r] != -1:
                return dp[l][r]
            takeLeft = solve(l+1, r, not turn)
            takeRight = solve(l, r-1, not turn)
            leftProfit = piles[l] if turn else 0
            rightProfit = piles[r] if turn else 0
            dp[l][r] = max(takeLeft + leftProfit, takeRight + rightProfit)
            return dp[l][r]
        # above function represents optimal solution for player
        total = sum(piles)
        alicePoints = solve(0, len(piles)-1, True)
        return total - alicePoints < alicePoints
            
        