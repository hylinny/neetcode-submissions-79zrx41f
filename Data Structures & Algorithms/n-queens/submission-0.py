class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # obviously there must be only one queen per row and column
        # place the first queen on first row, then move to next row
        # helper function to check if the queen's col / diagonal 
        # already has a queen. if so don't recurse.
        output = []
        placed = [-1 for _ in range(n)]
        def solve(row, board):
            if row == n:
                output.append(board.copy())
                return
            for i in range(n): # iterate through a column 
                if isValid(row, i):
                    board.append("." * i + "Q" + "." * (n-i-1))
                    placed[i] = row
                    solve(row + 1, board)
                    board.pop()
                    placed[i] = -1

        def isValid(row, col):
            # check col violation
            if placed[col] != -1:
                return False
            # check diag violation
            for i in range(len(placed)):
                if placed[i] == -1:
                    continue
                dx = abs(placed[i] - row)
                dy = abs(i - col)
                if dx == dy:
                    return False
            return True

        solve(0, [])
        return output
