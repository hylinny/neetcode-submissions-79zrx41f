class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # dfs traversal, enter if first letter matches
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        def dfs(i, j, index):
            if index == len(word):
                return True
            temp = board[i][j]
            board[i][j] = '#'
            for dy, dx in directions:
                row = dy + i
                col = dx + j
                if 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] == word[index]:
                    if dfs(row, col, index + 1):
                        return True
            board[i][j] = temp
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, 1):
                        return True
        return False
            