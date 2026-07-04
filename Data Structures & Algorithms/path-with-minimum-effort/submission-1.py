class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        heap = []
        # change relaxation condition: take the max(edge weight, weight to current node
        row = len(heights)
        col = len(heights[0])
        heapq.heappush(heap, (0, 0, 0))
        minPath = {}
        minPath[(0, 0)] = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while heap:
            weight, r, c = heapq.heappop(heap)
            # relax neighbours
            for dy, dx in directions:
                newrow, newcol = dy + r, dx + c
                if 0 <= newrow < row and 0 <= newcol < col:
                    newEffort = max(abs(heights[newrow][newcol] - heights[r][c]), minPath[(r, c)])
                    if (newrow, newcol) not in minPath or minPath[(newrow, newcol)] > newEffort:
                        heapq.heappush(heap, (newEffort, newrow, newcol))
                        minPath[(newrow, newcol)] = newEffort

        return minPath[(row-1, col-1)]

