class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # finish at most k projects (can be less)
        # invest capital and get profit for any i
        # capital must be <= w
        projects = []
        for i in range(len(profits)):
            projects.append((profits[i], capital[i]))
        projects.sort(key=lambda x: x[1]) # sort by capital ascending
        heap = [] # max-heap for profits
        i = 0 # pointer to track completable projects
        for _ in range(k):
            while i < len(projects) and projects[i][1] <= w:
                heapq.heappush(heap, -projects[i][0])
                i += 1
            if not heap:
                break
            profit = -heapq.heappop(heap)
            w += profit
        return w