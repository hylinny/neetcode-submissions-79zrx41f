class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # take stones from left to right
        # compute M down the recursion
        # grab max from i+1 - i+M, then return that + current stone value
        # 2d dp comes from length of piles and M
        dp = {}
        def solve(i, m, turn):
            if i == len(piles):
                return 0
            if (i, m, turn) in dp:
                return dp[(i, m, turn)]
            result = 0 if turn else float('inf')
            stones = 0
            for j in range(i, i+2*m):
                if j == len(piles):
                    break
                stones += piles[j]
                if turn:
                    result = max(stones + solve(j+1, max(m, j-i+1), not turn), result)
                else:
                    result = min(solve(j+1, max(m, j-i+1), not turn), result)
            dp[(i, m, turn)] = result
            return dp[(i, m, turn)]
        return solve(0, 1, True)


        