class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # iterate through all entries in the grid
            # if visited, skip, else increment islands and
        # perform bfs/dfs, and add all visited entries to visited

        def dfs(i, j):
            # need to check top down left right
            if (i, j) in visited:
                return
            if i < 0 or j < 0 or i >= height or j >= width:
                return
            if grid[i][j] == "0":
                return
            visited.add((i, j))
            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i-1, j)
            dfs(i, j-1)
            return 
        height = len(grid)
        width = len(grid[0])
        visited = set()
        islands = 0
        for i in range(height):
            for j in range(width):
                if (i, j) in visited:
                    continue
                if grid[i][j] == "0":
                    continue
                islands += 1
                dfs(i, j)
        return islands

        