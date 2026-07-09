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
            pass

        def idea3(grid):
            pass

        return idea1(grid)
        
