class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [n-1]

        adjList = defaultdict(list)
        edgeCount = defaultdict(int)
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
            edgeCount[u] += 1
            edgeCount[v] += 1
        
        visited = set()
        queue = deque()

        for node, neighbours in adjList.items():
            if len(neighbours) == 1:
                queue.append(node)
                visited.add(node)
        
        nodes = n
        while nodes > 2:
            frontier = len(queue)
            for i in range(frontier):
                node = queue.popleft()
                nodes -= 1
                for neighbour in adjList[node]:
                    edgeCount[neighbour] -= 1
                    if neighbour not in visited and edgeCount[neighbour] == 1:
                        # since tree, this should run at most once per source node
                        visited.add(neighbour)
                        queue.append(neighbour)
        
        return list(queue)
        

