class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # node with two edges -> side length 2
        # one edge -> side length 3
        # three edges -> side length 1
        # four edges -> side length 0
        # perform dfs
        visited = set()
        m = len(grid)
        n = len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def dfs(i, j):
            visited.add((i, j))
            count = 0
            for dy, dx in directions:
                row = i + dy
                col = j + dx
                if row < 0 or col < 0 or row == m or col == n:
                    count += 1
                elif grid[row][col] == 0:
                    count += 1
                elif (row, col) not in visited:
                    count += dfs(row, col)
            return count
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return dfs(i, j)
        