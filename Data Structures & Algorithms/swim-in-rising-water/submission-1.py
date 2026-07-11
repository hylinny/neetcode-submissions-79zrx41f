class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # idea 1: ufds with pq
        # idea 2: bfs with binary search
        # idea 3: modified dijkstra's
        def idea1(grid):
            hashmap = {} # ufds
            n = len(grid)

            def find(node):
                if hashmap[node] == node:
                    return node
                hashmap[node] = find(hashmap[node])
                return hashmap[node]

            def union(node1, node2):
                root1 = find(node1)
                root2 = find(node2)
                hashmap[root1] = root2

            pq = []
            for i in range(n):
                for j in range(n):
                    # right and bottom neighbour
                    if j + 1 < n:
                        weightR = max(grid[i][j+1], grid[i][j])
                        heapq.heappush(pq, (weightR, (i, j), (i, j+1)))
                    if i + 1 < n:
                        weightD = max(grid[i+1][j], grid[i][j])
                        heapq.heappush(pq, (weightD, (i, j), (i+1, j)))
                    hashmap[(i, j)] = (i, j)
            
            while pq:
                weight, node1, node2 = heapq.heappop(pq)
                union(node1, node2)
                if find((0, 0)) == find((n-1, n-1)):
                    return weight
            return grid[0][0]

        def idea2(grid):
            n = len(grid)
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            def bfs(level):
                if grid[0][0] > level:
                    return False
                queue = deque()
                queue.append((0, 0))
                visited = set()
                visited.add((0, 0))
                while queue:
                    (x, y) = queue.popleft()
                    if x == n-1 and y == n-1:
                        return True
                    for dx, dy in directions:
                        newx, newy = x + dx, y + dy
                        if 0 <= newx < n and 0 <= newy < n and (newx, newy) not in visited and max(grid[newx][newy], grid[x][y]) <= level:
                            visited.add((newx, newy))
                            queue.append((newx, newy))
                return False


            right = max(max(row) for row in grid)
            left = min(min(row) for row in grid)
            while left <= right:
                mid = (right - left) // 2 + left
                isPossible = bfs(mid)
                if isPossible:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        def idea3(grid):
            pass

        return idea2(grid)
        
