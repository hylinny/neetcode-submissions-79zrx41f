class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # pacific: top left
        # atlantic: bottom right
        # input: 2d matrix of cells
        # output: 2d array of all possible grids
        # dfs with backtracking. mark all possible cells with True
        # then, iterate and count number of True's
        # touch pacific: i == 0 or j == 0
        # touch atlantic: i == len(height) or j == len(width)
        m = len(heights)
        n = len(heights[0])
        visited = {}
        # -1 for unvisited, 0 for unreachable, 1 for reachable
        output = []

        def dfsAtlantic(i, j, prev):
            if i < 0 or j < 0 or i == m or j == n:
                return False
            if prev < heights[i][j]: # invalid traversal
                return False
            if i == m-1 or j == n-1:
                return True
            if (i, j) in visited:
                return False
            visited[(i, j)] = True
            return dfsAtlantic(i+1, j, heights[i][j]) or dfsAtlantic(i-1, j, heights[i][j]) or dfsAtlantic(i, j+1, heights[i][j]) or dfsAtlantic(i, j-1, heights[i][j])
            
        
        def dfsPacific(i, j, prev):
            if i == m or j == n or i < 0 or j < 0:
                return False
            if prev < heights[i][j]: # invalid traversal
                return False
            if i == 0 or j == 0:
                return True
            if (i, j) in visited:
                return False
            visited[(i, j)] = True
            return dfsPacific(i+1, j, heights[i][j]) or dfsPacific(i-1, j, heights[i][j]) or dfsPacific(i, j+1, heights[i][j]) or dfsPacific(i, j-1, heights[i][j])

        for i in range(m):
            for j in range(n):
                validCell = True
                validCell &= dfsAtlantic(i, j, float('inf'))
                visited = {}
                validCell &= dfsPacific(i, j, float('inf'))
                visited = {}
                if validCell:
                    output.append([i, j])
        return output


