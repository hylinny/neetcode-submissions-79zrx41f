class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # brute force: iterate through each element,
        # try to expand outwards to check for square
        n = len(matrix)
        m = len(matrix[0])
        def checkSquare(i, j):
            k = 1
            maxSize = 1
            while True:
                row = i + k
                col = j + k
                if row == n or col == m:
                    break
                
                for r in range(i, row+1):
                    if matrix[r][col] == '0':
                        return maxSize
                
                for c in range(j, col+1):
                    if matrix[row][c] == '0':
                        return maxSize

                maxSize += 1
                k += 1
            return maxSize

        
        maximum = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '1':
                    maximum = max(maximum, checkSquare(i, j))
        return maximum * maximum