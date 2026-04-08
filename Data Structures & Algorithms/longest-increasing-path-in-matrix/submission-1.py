import sys
sys.setrecursionlimit(12000)

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # dfs approach
        # can start from any cell
        # store computed values
        dp = {}
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            path = 1
            for dy, dx in directions:
                row, col = i + dy, j + dx
                if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]) and matrix[row][col] > matrix[i][j]:
                    path = max(path, 1 + dfs(row, col))
            dp[(i, j)] = path
            return path

        
        path = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                path = max(path, dfs(i, j))
        return path
