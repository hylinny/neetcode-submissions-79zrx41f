class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)
        for u, v, time in times:
            adjList[u].append((v, time))

        minTimes = {i: float('inf') for i in range(1, n+1)}
        minTimes[k] = 0
        pq = [(0, k)]
        while pq:
            currentTime, node = heapq.heappop(pq)
            if currentTime > minTimes[node]: # stale node
                continue
            for neighbour, time in adjList[node]:
                if currentTime + time < minTimes[neighbour]:
                    # relax
                    newTime = currentTime + time
                    heapq.heappush(pq, (newTime, neighbour))
                    minTimes[neighbour] = newTime
        
        maxTime = max(minTimes.values())
        return maxTime if maxTime != float('inf') else -1