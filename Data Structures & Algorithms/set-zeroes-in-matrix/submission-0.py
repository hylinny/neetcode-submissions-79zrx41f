class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        height = len(matrix)
        width = len(matrix[0])
        zeroes = set()
        for i in range(height):
            for j in range(width):
                if matrix[i][j] == 0:
                    zeroes.add((i, j))
        for i, j in zeroes:
            up = down = i
            left = right = j
            while up >= 0:
                matrix[up][j] = 0
                up -= 1
            while down < height:
                matrix[down][j] = 0
                down += 1
            while left >= 0:
                matrix[i][left] = 0
                left -= 1
            while right < width:
                matrix[i][right] = 0
                right += 1

        
        