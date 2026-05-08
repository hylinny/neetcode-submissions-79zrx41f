class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # iterate from all borders with 'O', going into grids with 'O' and marking them with '#'
        # afterwards, do a one pass to change all remaining 'O's to 'X's and '#'s to 'O's
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def dfs(i, j):
            board[i][j] = '#'
            for dy, dx in directions:
                row, col = i + dy, j + dx
                if 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] == 'O':
                    dfs(row, col)
            
        
        for i in range(len(board)):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][len(board[0])-1] == 'O':
                dfs(i, len(board[0])-1)
        
        for j in range(len(board[0])):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[len(board)-1][j] == 'O':
                dfs(len(board)-1, j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'