class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:
        # obviously there must be only one queen per row and column
        # place the first queen on first row, then move to next row
        # helper function to check if the queen's col / diagonal 
        # already has a queen. if so don't recurse.
        output = []
        placed = [-1 for _ in range(n)]
        positiveDiag = set()
        negativeDiag = set()
        def solve(row):
            if row == n:
                return 1
            solutions = 0
            for i in range(n): # iterate through a column 
                if isValid(row, i):
                    placed[i] = row
                    positiveDiag.add(row+i)
                    negativeDiag.add(row-i)
                    solutions += solve(row + 1)
                    positiveDiag.remove(row+i)
                    negativeDiag.remove(row-i)
                    placed[i] = -1
            return solutions

        def isValid(row, col):
            # check col violation
            if placed[col] != -1:
                return False
            # check diag violation
            if row+col in positiveDiag or row-col in negativeDiag:
                return False
            return True

        return solve(0)