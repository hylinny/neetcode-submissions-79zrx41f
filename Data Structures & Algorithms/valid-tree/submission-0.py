class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # input: edge list
        # check for tree: perform dfs. if visited, return not tree (false)
        adjacencylist = {i: [] for i in range(n)}
        for u, v in edges:
            adjacencylist[u].append(v)
            adjacencylist[v].append(u)
        
        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for neighbour in adjacencylist[node]:
                if neighbour == parent:
                    continue
                if not dfs(neighbour, node):
                    return False
            return True

        if not dfs(0, -1):
            return False
        
        return len(visited) == n
    
        