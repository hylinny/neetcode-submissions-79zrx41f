class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        # check each row and column
        for i in range(n):
            rowset = set()
            columnset = set()
            boxset = set()
            for j in range(n):
                # checking rows
                if board[i][j] != ".":
                    if board[i][j] in rowset:
                        return False
                    rowset.add(board[i][j])
                
                # checking columns
                if board[j][i] != ".":
                    if board[j][i] in columnset:
                        return False
                    columnset.add(board[j][i])

                # indices for box
                boxrow = i//3 * 3 + j//3
                boxcol = i%3 * 3 + j%3
                if board[boxrow][boxcol] != ".":
                    if board[boxrow][boxcol] in boxset:
                        return False
                    boxset.add(board[boxrow][boxcol])
        return True
        # check each box
        # (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)
        # (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8)
        # mapping formula: (row/3*3 + col/3, row%3*3 + col%3)
        # 000111222000111222000111222, 012012012345345345678678678
