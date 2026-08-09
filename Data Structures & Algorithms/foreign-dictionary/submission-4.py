class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjList = {char: [] for word in words for char in word}
        for i in range(1, len(words)):
            word1 = words[i-1]
            word2 = words[i]
            j = 0
            while j < len(word1) and j < len(word2):
                if word1[j] != word2[j]:
                    adjList[word1[j]].append(word2[j])
                    break
                j += 1
            if j >= len(word2) and len(word1) != len(word2):
                return ""
    
        # perform topo sort + cycle detection
        visited = set()
        visiting = set()
        toposort = []

        def dfs(node):
            if node in visiting:
                return False
            if node in visited:
                return True
            visited.add(node)
            visiting.add(node)
            for neighbour in adjList[node]:
                if not dfs(neighbour):
                    return False
            visiting.remove(node)
            toposort.append(node)
            return True
        
        for node in adjList.keys():
            if not dfs(node):
                return ""
        toposort.reverse()
        return ''.join(toposort)




