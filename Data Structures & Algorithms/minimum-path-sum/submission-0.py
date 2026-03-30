class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = [[-1] * len(grid[0]) for _ in range(len(grid))]
        def solution(i, j):
            if i < 0 or j < 0:
                return float('inf')
            if i == 0 and j == 0:
                return grid[0][0]
            if memo[i][j] != -1:
                return memo[i][j]
            memo[i][j] = grid[i][j] + min(solution(i-1, j), solution(i, j-1))
            return memo[i][j]
        return solution(len(grid)-1, len(grid[0])-1)
        