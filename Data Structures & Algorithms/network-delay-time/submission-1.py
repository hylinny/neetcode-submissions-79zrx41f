class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)
        for u, v, time in times:
            adjList[u].append((v, time))

        minTimes = {} # minimum times
        minTimes[k] = 0
        pq = [k]
        while pq:
            node = pq.pop()
            for neighbour, time in adjList[node]:
                if neighbour not in minTimes or neighbour in minTimes and minTimes[node] + time < minTimes[neighbour]:
                    # relax
                    newTime = minTimes[node] + time
                    minTimes[neighbour] = newTime
                    heapq.heappush(pq, neighbour)
        
        if len(minTimes) < n:
            return -1
        return max(minTimes.values())