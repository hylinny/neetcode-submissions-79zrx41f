class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # pacific: top left
        # atlantic: bottom right
        # input: 2d matrix of cells
        # output: 2d array of all possible grids
        # perform dfs, and mark all visitable cells with True
        # if cell value is lower than prev value
        # then, find the intersection and add it to output
        m = len(heights)
        n = len(heights[0])
        # starting from pacific/atlantic
        pacific, atlantic = set(), set()

        def dfs(i, j, visited, prev):
            if (i, j) in visited or i < 0 or j < 0 or i == m or j == n or prev > heights[i][j]:
                return
            visited.add((i, j))
            dfs(i+1, j, visited, heights[i][j])
            dfs(i-1, j, visited, heights[i][j])
            dfs(i, j+1, visited, heights[i][j])
            dfs(i, j-1, visited, heights[i][j])

        # pacific <-> atlantic iteration
        for i in range(m): # rows
            dfs(i, 0, pacific, float('-inf'))
            dfs(i, n-1, atlantic, float('-inf'))

        for i in range(n): # cols
            dfs(0, i, pacific, float('-inf'))
            dfs(m-1, i, atlantic, float('-inf'))
        
        output = []
        for i in range(m):
            for j in range(n):
                if (i, j) in pacific and (i, j) in atlantic:
                    output.append([i, j])
        return output




