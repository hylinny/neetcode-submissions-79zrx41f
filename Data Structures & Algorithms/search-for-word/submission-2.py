class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # iterate through grid dfs style
        # outside loop: if first letter found, enter dfs
        # dfs loop: create backtracking string, if string = word
        # then return true
        def dfs(i, j, wordIndex):
            if (i, j) in visited:
                return False
            if wordIndex == len(word)-1:
                return True
            visited.add((i, j))
            for x, y in directions:
                row = i + x
                col = j + y
                if row < 0 or col < 0 or row == m or col == n or board[row][col] != word[wordIndex+1]:
                    continue
                if dfs(row, col, wordIndex+1):
                    return True
            visited.remove((i, j))
            return False


        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set()
        
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False