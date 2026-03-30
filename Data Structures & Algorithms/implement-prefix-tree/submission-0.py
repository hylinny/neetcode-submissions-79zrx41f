class PrefixTree:

    def __init__(self):
        self.tree = {}

    def insert(self, word: str) -> None:
        i = 0 
        tree = self.tree
        while i < len(word):
            if word[i] not in tree:
                tree[word[i]] = {}
            tree = tree[word[i]]
            i += 1
        tree["#"] = ""


    def search(self, word: str) -> bool:
        # search for terminator
        tree = self.tree
        for c in word:
            if c not in tree:
                return False
            tree = tree[c]
        return "#" in tree
        

    def startsWith(self, prefix: str) -> bool:
        # search, return immediately once found
        tree = self.tree
        for c in prefix:
            if c not in tree:
                return False
            tree = tree[c]
        return True
        
        