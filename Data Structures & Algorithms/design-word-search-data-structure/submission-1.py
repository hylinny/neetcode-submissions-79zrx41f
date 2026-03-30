class WordDictionary:

    def __init__(self):
        self.trie = {}
        

    def addWord(self, word: str) -> None:
        trie = self.trie
        i = 0
        while i < len(word):
            if word[i] not in trie:
                trie[word[i]] = {}
            trie = trie[word[i]]
            i += 1
        trie["#"] = ""
        

    def search(self, word: str) -> bool:
        trie = self.trie
        def solve(i, trie):
            if i == len(word):
                return "#" in trie
            if word[i] == ".":
                for c in trie:
                    if c == "#":
                        continue
                    if solve(i+1, trie[c]):
                        return True
                return False
            elif word[i] in trie:
                return solve(i+1, trie[word[i]])
            else: # word not in trie
                return False
        return solve(0, trie)
        
