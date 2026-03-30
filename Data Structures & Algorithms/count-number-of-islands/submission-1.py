class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs traversal
        visited = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def dfs(i, j):
            visited.add((i, j))
            for dy, dx in directions:
                row, col = dy + i, dx + j
                if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == '1' and (row, col) not in visited:
                    # valid cell
                    dfs(row, col)

        
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    if (i, j) not in visited:
                        dfs(i, j)
                        islands += 1
        return islands