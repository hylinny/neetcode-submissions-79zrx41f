class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # currently, decision to take left or right comes from 
        # max(stones won if left taken + left stones, stones won if right taken + right stones)
        # 2d dp to represent whose turn it is
        dp = [[-1] * len(piles) for _ in range(len(piles))]
        def solve(l, r, alice_turn):
            if l > r:
                return 0
            if dp[l][r] != -1:
                return dp[l][r]
            takeLeft = solve(l+1, r, not alice_turn)
            takeRight = solve(l, r-1, not alice_turn)
            if alice_turn:
                dp[l][r] = max(piles[l] + takeLeft,
                           piles[r] + takeRight)
            else:
                dp[l][r] = min(takeLeft,
                           takeRight)
            return dp[l][r]
        # above function represents optimal solution for player
        total = sum(piles)
        alicePoints = solve(0, len(piles)-1, True)
        return total - alicePoints < alicePoints
            
        