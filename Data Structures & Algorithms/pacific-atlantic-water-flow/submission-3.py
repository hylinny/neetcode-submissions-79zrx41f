class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # dfs from all pacific cells
        # dfs from all atlantic cells
        pacific = set()
        atlantic = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def dfs(i, j, visited):
            visited.add((i, j))
            for dy, dx in directions:
                row, col = i + dy, j + dx
                if 0 <= row < len(heights) and 0 <= col < len(heights[0]) and (row, col) not in visited and heights[i][j] <= heights[row][col]:
                    dfs(row, col, visited)
        for i in range(len(heights)):
            if (i, 0) not in pacific:
                dfs(i, 0, pacific)
            if (i, len(heights[0])-1) not in atlantic:
                dfs(i, len(heights[0])-1, atlantic)
        for j in range(len(heights[0])):
            if (0, j) not in pacific:
                dfs(0, j, pacific)
            if (len(heights)-1, j) not in atlantic:
                dfs(len(heights)-1, j, atlantic)

        output = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i, j) in pacific and (i, j) in atlantic:
                    output.append([i, j])
        return output
