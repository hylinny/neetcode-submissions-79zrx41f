class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)
        for u, v, time in times:
            adjList[u].append((v, time))

        minTimes = {} # minimum times
        pq = [(0, k)]
        while pq:
            minTime, node = heapq.heappop(pq)
            if node in minTimes:
                continue
            minTimes[node] = minTime
            for neighbour, time in adjList[node]:
                if neighbour not in minTimes:
                    heapq.heappush(pq, (minTime + time, neighbour))
        
        if len(minTimes) < n:
            return -1
        return max(minTimes.values())