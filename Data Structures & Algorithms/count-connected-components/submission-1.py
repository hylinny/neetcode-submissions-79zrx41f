class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = defaultdict(list)
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        connectedComponents = 0
        visited = set()
        def dfs(node):
            visited.add(node)
            for neighbour in adjList[node]:
                if neighbour not in visited:
                    dfs(neighbour)
        
        for i in range(n):
            if i not in visited:
                connectedComponents += 1
                dfs(i)

        return connectedComponents

        
