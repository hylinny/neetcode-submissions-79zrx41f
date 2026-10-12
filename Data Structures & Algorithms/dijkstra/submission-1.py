class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        # build adjacency list
        # initialise distances of infinity
        # initialize priority queue
        # push neighbours into priority queue if relaxed
        # pop -> true shortest path
        adjList = defaultdict(list)
        for u, v, w in edges:
            adjList[u].append((v, w))
        distances = {i: float('inf') for i in range(n)}
        pq = []
        heapq.heappush(pq, (0, src))
        distances[src] = 0
        while pq:
            w, node = heapq.heappop(pq)
            if w > distances[node]:
                continue
            for neighbour, weight in adjList[node]:
                nodeDist = distances[node]
                # relaxation condition
                if nodeDist + weight < distances[neighbour]:
                    distances[neighbour] = nodeDist + weight
                    heapq.heappush(pq, (nodeDist + weight, neighbour))
        for key, distance in distances.items():
            if distance == float('inf'):
                distances[key] = -1
        return distances