class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # build adjacency list, then dfs to find max depth
        # store in hashmap
        depthmap = defaultdict(list)
        adjList = defaultdict(list)
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        visited = set()
        def dfs(node):
            if node in visited:
                return 0
            visited.add(node)
            maxDepth = 0
            for neighbour in adjList[node]:
                maxDepth = max(maxDepth, 1 + dfs(neighbour))
            return maxDepth
        
        for node in adjList:
            visited = set()
            depthmap[dfs(node)].append(node)

        for i in range(n+1):
            if len(depthmap[i]) > 0:
                return depthmap[i]

        return [0]