class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Step 1: create a graph
        # Step 2: topo sort the graph
        # return reverse of toposort

        # iterate through the list and compare two elements character by character
        # for the first differing char encountered, draw an edge from right to left
        # continue until the end of the list
        # topo sort the graph
        if len(words) == 1:
            return words[0]

        adjacencylist = {}

        for word in words:
            for c in word:
                adjacencylist.setdefault(c, [])

        for i in range(len(words) - 1):
            firstword = words[i]
            secondword = words[i+1]
            for c in range(len(firstword)):
                if c == len(secondword):
                    return ""
                if firstword[c] != secondword[c]:
                    adjacencylist[secondword[c]].append(firstword[c])
                    break
            # otherwise, nothing is added
        
        visited = set()
        stack = []
        path = set()

        def dfs(node):
            if node in path:
                return False
            if node in visited:
                return True
            visited.add(node)
            path.add(node)
            for neighbor in adjacencylist[node]:
                if not dfs(neighbor):
                    return False
            path.remove(node)
            stack.append(node)
            return True

        for node in adjacencylist:
            if node in visited:
                continue
            if not dfs(node):
                return ""

        return ''.join(stack)
            



        