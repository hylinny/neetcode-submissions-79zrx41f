class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # recurrence: grab min of all 3 house colours.
        # if house color same as previous house colour, continue
        dp = [[-1] * 3 for _ in range(len(costs))]
        def solve(i, color):
            if i < 0:
                return 0
            if dp[i][color] != -1:
                return dp[i][color]
            minimum = float('inf')
            # at the current step, we need to take color
            for j in range(3):
                if color == j:
                    continue
                minimum = min(minimum, costs[i][j] + solve(i-1,j))
            dp[i][color] = minimum
            return dp[i][color]
        n = len(costs)-1
        return min(solve(n,0), solve(n,1), solve(n,2))
        