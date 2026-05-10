class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # start with n disjoint sets
        # iterate through edges and add to sets
        # if an edge has the same parent root, it causes a cycle, return it
        n = max(max(i, j) for i, j in edges)
        sets = [i for i in range(n)]
        size = [1] * n

        def find(u):
            if sets[u] != u:
                sets[u] = find(sets[u])
            return sets[u]

        def union(u, v):
            root1 = find(u)
            root2 = find(v)
            if root1 == root2:
                return True
            if size[root1] > size[root2]:
                size[root1] += size[root2]
                sets[root2] = root1
            else:
                size[root2] += size[root1]
                sets[root1] = root2
            return False

        for u, v in edges:
            if union(u-1, v-1): # switch to 0-indexing
                return [u, v]
