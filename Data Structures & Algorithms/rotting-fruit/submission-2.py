class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # do bfs, add rotten ones to queue
        # keep track of fresh fruits remaining so far
        # if fresh fruits hit 0, return bfs level
        # else, after bfs completes, if fresh fruits > 0, return -1
        queue = deque()
        fresh = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))
                    visited.add((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0
        
        minutes = 0
        while queue:
            minutes += 1
            n = len(queue)
            for _ in range(n):
                i, j = queue.popleft()
                for dy, dx in directions:
                    row, col = i + dy, j + dx
                    if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and (row, col) not in visited and grid[row][col] == 1:
                        queue.append((row, col))
                        visited.add((row, col))
                        fresh -= 1
            if fresh == 0:
                return minutes
        return -1
