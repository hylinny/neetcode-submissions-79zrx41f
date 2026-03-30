from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # find all rotten oranges and add it to the queue
        # keep track of maximum distance reached (i.e. when bfs terminates)
        # keep track of fresh count and time per bfs round
        # after visiting, change fresh to rotten

        minutes = 0
        fresh = 0
        queue = deque()
        m = len(grid) # height
        n = len(grid[0]) # width
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1 
        
        directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]
        # bfs
        while queue:
            length = len(queue)
            for i in range(length):
                cell = queue.popleft()
                for x, y in directions:
                    row = cell[0] + x
                    col = cell[1] + y
                    if row >= 0 and row < m and col >= 0 and col < n and grid[row][col] == 1:
                        queue.append((row, col))
                        grid[row][col] = 2
                        fresh -= 1
            minutes += 1
        return max(0, minutes-1) if fresh == 0 else -1
                


                
        