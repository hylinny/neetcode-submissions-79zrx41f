class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # goal: maximise points
        # to gain points: pick one cell in each row
        # subtract the difference in column coordinates
        # between current row's cell and previous row's cell
        # at current row, we try picking from next row and
        # subtracting the difference in col coordinates.
        # take the maximum of this and recurse upwards
        dp = {}
        def solve(row, colIndex):
            if row == len(points):
                return 0
            if (row, colIndex) in dp:
                return dp[(row, colIndex)]
            maxPoints = 0
            for i in range(len(points[0])):
                p = points[row][colIndex] + solve(row+1, i) - abs(i - colIndex)
                maxPoints = max(maxPoints, p)
            dp[(row, colIndex)] = maxPoints
            return maxPoints
        return max(solve(0, i) for i in range(len(points[0])))

        