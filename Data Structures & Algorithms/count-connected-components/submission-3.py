class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        disjointSet = [i for i in range(n)]
        def find(u):
            if disjointSet[u] == u:
                return u
            disjointSet[u] = find(disjointSet[u])
            return disjointSet[u]
        def union(u, v):
            root1 = find(u)
            root2 = find(v)
            disjointSet[root1] = root2
        for u, v in edges:
            union(u, v)
        output = 0
        for i in range(len(disjointSet)):
            if disjointSet[i] == i:
                output += 1
        return output