class TrieNode:
    def __init__(self):
        self.trie = {}

    def addWord(self, word):
        i = 0
        trie = self.trie
        while i < len(word):
            if word[i] not in trie:
                trie[word[i]] = {}
            trie = trie[word[i]]
            i += 1
        trie["#"] = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # iterate through each word and do dfs on the grid

        trie = TrieNode()

        for word in words:
            trie.addWord(word)

        def dfs(i, j, trie):
            if i < 0 or j < 0 or i == m or j == n or (i, j) in visited or board[i][j] not in trie:
                return
            trie = trie[board[i][j]]
            if "#" in trie:
                output.add(trie["#"])
            visited.add((i, j))
            for x, y in directions:
                row = i + x
                col = j + y
                dfs(row, col, trie)
            visited.remove((i, j))
            

        m = len(board) #height
        n = len(board[0]) #width
        visited = set()
        output = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for i in range(m):
            for j in range(n):
                if board[i][j] in trie.trie:
                    dfs(i, j, trie.trie)

        return list(output)

        