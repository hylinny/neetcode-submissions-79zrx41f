class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def dfs(i, j):
            if i < 0 or j < 0 or i == m or j == n or (i, j) in visited or grid[i][j] == 0:
                return 0
            visited.add((i, j))
            return 1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1)
        
        maxArea = 0
        m = len(grid) # height
        n = len(grid[0])

        visited = set()

        for i in range(m):
            for j in range(n):
                if (i, j) not in visited:
                    area = dfs(i, j)
                    maxArea = max(maxArea, area)

        return maxArea
        