class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        positionMap = {i: query for i, query in enumerate(queries)}
        queryMap = {}
        intervals.sort()
        queries.sort()
        heap = [] # (intervalPeriod, start, end)
        i = 0
        for query in queries:
            while i < len(intervals) and intervals[i][0] <= query:
                heapq.heappush(heap, (intervals[i][1] - intervals[i][0] + 1, intervals[i][0], intervals[i][1]))
                i += 1
            while heap and heap[0][2] < query:
                heapq.heappop(heap)
            if not heap:
                queryMap[query] = -1
            else:
                queryMap[query] = heap[0][0]
        output = []
        for i in range(len(queries)):
            output.append(queryMap[positionMap[i]])
        return output