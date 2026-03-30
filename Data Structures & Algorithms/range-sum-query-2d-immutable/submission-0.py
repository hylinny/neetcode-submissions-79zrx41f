class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # compute the prefix sum of the grid defined by [0, 0] and current cell
        # to find sum of region, we just do [row2, col2] - [row2, col1-1] - [row1-1, col2] + [row1-1, col1-1]
        rows = len(matrix)
        cols = len(matrix[0])
        self.prefixSum = [[0] * (cols+1) for _ in range(rows+1)]
        for i in range(1, rows+1):
            rowSum = 0
            for j in range(1, cols+1):
                rowSum += matrix[i-1][j-1] # note that this is indexing into matrix
                self.prefixSum[i][j] = self.prefixSum[i-1][j] + rowSum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefixSum[row2+1][col2+1] - self.prefixSum[row2+1][col1] - self.prefixSum[row1][col2+1] + self.prefixSum[row1][col1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)