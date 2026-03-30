class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(dict)
        for u, v, w in times:
            adjList[u][v] = w
        pq = [(0, k)]
        distances = {i: float('inf') for i in range(1, n+1)} # initialise all values to infinity
        distances[k] = 0
        while pq:
            distance, node = heapq.heappop(pq)
            if distance > distances[node]:
                continue
            for neighbour, weight in adjList[node].items():
                new_distance = distance + weight
                if new_distance < distances[neighbour]:
                    distances[neighbour] = new_distance
                    heapq.heappush(pq, (new_distance, neighbour))
        return max(distances.values()) if max(distances.values()) != float('inf') else -1
                