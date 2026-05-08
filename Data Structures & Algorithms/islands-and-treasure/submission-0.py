class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # do bfs from treasure chests
        # update inf cells to be lower if possible
        # if cell is -1, skip
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        queue = deque()
        def bfs(i, j):
            # stuff
            # print('bfs call')
            queue.append((i, j))
            visited = set([(i, j)])
            d = 0
            while queue:
                length = len(queue)
                for k in range(length):
                    i, j = queue.popleft()
                    # print(f"popped: {i}, {j}")
                    # print(f"d = {d}")
                    grid[i][j] = min(grid[i][j], d)
                    for dy, dx in directions:
                        row, col = i + dy, j + dx
                        if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and (row, col) not in visited and grid[row][col] != -1:
                            # valid row and col to traverse into
                            # print(f"valid neighbours: {row}, {col}")
                            visited.add((row, col))
                            queue.append((row, col))
                d += 1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    bfs(i, j)