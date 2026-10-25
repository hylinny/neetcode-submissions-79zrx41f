class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        # find intersections between each route
        # route with source must reach route with target
        # build a map for reachable bus routes, hashmap from bus stop to routes
        hashmap = defaultdict(set)
        for i in range(len(routes)):
            for stop in routes[i]:
                hashmap[stop].add(i)
            routes[i] = set(routes[i])
        # do bfs starting at source stop until we reach target
        level = 0
        queue = deque()
        queue.append(source)
        visitedRoutes = set()
        visitedStops = set()
        while queue:
            level += 1
            n = len(queue)
            for i in range(n):
                stop = queue.popleft()
                routeSet = hashmap[stop]
                for route in routeSet:
                    if route not in visitedRoutes:
                        visitedRoutes.add(route)
                        if target in routes[route]:
                            return level
                        for stop in routes[route]:
                            if stop not in visitedStops:
                                visitedStops.add(stop)
                                queue.append(stop) 
        return -1