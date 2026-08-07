class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        # build adjacency list
        adjList = defaultdict(list)
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        visited = set()
        def dfs(node, parent):
            visited.add(node)
            for neighbour in adjList[node]:
                if neighbour != parent and neighbour not in visited:
                    dfs(neighbour, node)
        
        dfs(0, 0)
        return len(visited) == n