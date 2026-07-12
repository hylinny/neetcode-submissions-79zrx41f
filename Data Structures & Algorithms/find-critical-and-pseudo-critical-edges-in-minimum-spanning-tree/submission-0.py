class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        def kruskal(edges, initialConnection, skipEdge):
            unionMap = {i: i for i in range(n)}
            def find(node):
                if unionMap[node] == node:
                    return node
                unionMap[node] = find(unionMap[node])
                return unionMap[node]

            def union(node1, node2):
                root1 = find(node1)
                root2 = find(node2)
                unionMap[root1] = root2

            mstWeight = 0
            edgeCount = 0
            if initialConnection:
                union(initialConnection[1], initialConnection[2])
                mstWeight += initialConnection[0]
                edgeCount += 1
            for weight, u, v, index in edges:
                if skipEdge and index == skipEdge[3] or initialConnection and index == initialConnection[3]:
                    continue
                if find(u) == find(v):
                    continue
                union(u, v)
                mstWeight += weight
                edgeCount += 1
            return mstWeight if edgeCount == n-1 else -1

        edgeList = []
        for i in range(len(edges)):
            # weight, u, v, index
            edgeList.append([edges[i][2], edges[i][0], edges[i][1], i])

        edgeList.sort()

        mstWeight = kruskal(edgeList, [], [])

        critical = set()
        pseudocritical = set()

        for edge in edgeList:
            weight = kruskal(edgeList, [], edge)
            if weight != mstWeight:
                critical.add(edge[3])

        for edge in edgeList:
            weight = kruskal(edgeList, edge, [])
            if weight == mstWeight and edge[3] not in critical:
                pseudocritical.add(edge[3])
        
        return [list(critical), list(pseudocritical)]

