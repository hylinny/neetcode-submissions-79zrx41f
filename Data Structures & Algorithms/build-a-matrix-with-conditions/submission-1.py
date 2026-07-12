class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def toposort(edges):
            adjList = defaultdict(list)
            for u, v in edges:
                adjList[u].append(v)
            visited = set()
            visiting = set()
            topo = []
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
                topo.append(node)
                return True
                
            for i in range(1, k+1):
                if not dfs(i):
                    return []
            topo.reverse()
            return topo
        
        output = [[0] * k for _ in range(k)]
        rowList = toposort(rowConditions) # row toposort first
        colList = toposort(colConditions)
        if not rowList or not colList:
            return []
        rowMap = {rowList[i]: i for i in range(k)}
        colMap = {colList[i]: i for i in range(k)}
        for i in range(1, k+1):
            output[rowMap[i]][colMap[i]] = i
        return output