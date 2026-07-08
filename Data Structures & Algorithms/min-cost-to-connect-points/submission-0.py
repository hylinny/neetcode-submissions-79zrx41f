class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # MST, kruskal's algo with union find
        # points identified by tuples
        # hashmap stores the disjoint sets, pointing to parent, root points to itself
        hashmap = {}
        for x, y in points:
            hashmap[(x, y)] = (x, y)
        
        def find(t):
            if hashmap[t] == t:
                return t
            hashmap[t] = find(hashmap[t])
            return hashmap[t]

        def union(t1, t2):
            root1 = find(t1)
            root2 = find(t2)
            hashmap[root1] = root2

        def manhattan(x1, x2, y1, y2):
            return abs(x1 - x2) + abs(y1 - y2)
        
        # construct edge list
        edges = []
        for x1, y1 in points:
            for x2, y2 in points:
                if x1 == x2 and y1 == y2:
                    continue
                distance = manhattan(x1, x2, y1, y2)
                edges.append([distance, (x1, y1), (x2, y2)])

        edges.sort()

        cost = 0

        n = len(points)
        i = 0
        for distance, p1, p2 in edges:
            if find(p1) == find(p2):
                continue
            union(p1, p2)
            cost += distance
            i += 1
            if i == n-1:
                break
        
        return cost

                
