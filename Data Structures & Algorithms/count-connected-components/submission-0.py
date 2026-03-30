class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjacencylist = {i: [] for i in range(n)}
        for u, v in edges:
            adjacencylist[u].append(v)
            adjacencylist[v].append(u)

        visited = set()
        counter = 0

        def dfs(node):
            for neighbor in adjacencylist[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

        for i in range(n):
            if i in visited:
                continue
            visited.add(i)
            dfs(i)
            counter += 1

        return counter
        