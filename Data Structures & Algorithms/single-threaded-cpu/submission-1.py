class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        t = []
        for i in range(len(tasks)):
            t.append([tasks[i][0], tasks[i][1], i])
        t.sort(key=lambda x: x[0])
        queue = deque()
        for task in t:
            queue.append(task)
        pq = []
        currentTime = 0
        order = []
        index = 0
        while pq or queue:
            while queue and currentTime >= queue[0][0]:
                task = queue.popleft()
                # order: processing time, index, enqueue time
                heapq.heappush(pq, (task[1], task[2], task[0]))
            if not pq:
                currentTime = queue[0][0]
            else:
                task = heapq.heappop(pq)
                currentTime += task[0]
                order.append(task[1])
        return order