class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adjList = defaultdict(list)
        for i in range(len(edges)):
            adjList[edges[i][0]].append((edges[i][1], succProb[i]))
            adjList[edges[i][1]].append((edges[i][0], succProb[i]))
        distances = {i: 0 for i in range(n)}
        distances[start_node] = 1
        pq = []
        heapq.heappush(pq, (1, start_node))
        while pq:
            probability, node = heapq.heappop(pq)
            if probability < distances[node]:
                continue
            for neighbour, edgeProb in adjList[node]:
                if probability * edgeProb > distances[neighbour]:
                    distances[neighbour] = probability * edgeProb
                    heapq.heappush(pq, (probability * edgeProb, neighbour))
        return distances[end_node]

