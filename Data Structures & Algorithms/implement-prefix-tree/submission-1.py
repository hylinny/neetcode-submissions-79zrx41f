class PrefixTree:

    def __init__(self):
        self.hashmap = {}

    def insert(self, word: str) -> None:
        p = self.hashmap
        for c in word:
            if c not in p:
                p[c] = {}
            p = p[c]
        p['.'] = {} # end indicator

    def search(self, word: str) -> bool:
        p = self.hashmap
        for c in word:
            if c not in p:
                return False
            p = p[c]
        return '.' in p
        
    def startsWith(self, prefix: str) -> bool:
        p = self.hashmap
        for c in prefix:
            if c not in p:
                return False
            p = p[c]
        return True
        
        