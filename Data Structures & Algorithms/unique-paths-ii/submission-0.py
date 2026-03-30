class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo = [[-1] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        def solve(i, j):
            if i < 0 or j < 0:
                return 0
            # invalid state:
            if obstacleGrid[i][j] == 1:
                return 0
            if i == 0 and j == 0:
                return 1
            if memo[i][j] != -1:
                return memo[i][j]
            memo[i][j] = solve(i-1, j) + solve(i, j-1)
            return memo[i][j]
        return solve(len(obstacleGrid)-1, len(obstacleGrid[0])-1)
        