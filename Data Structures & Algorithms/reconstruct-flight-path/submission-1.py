class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # all tickets are used
        # originally departed from JFK, eulerian path
        # learn: hierholzer's algorithm on youtube
        adjList = defaultdict(list)
        tickets.sort(reverse=True)
        for u, v in tickets:
            adjList[u].append(v)
        toposort = []
        def dfs(node):
            while adjList[node]:
                nextNode = adjList[node].pop()
                dfs(nextNode)
            toposort.append(node)
        dfs("JFK")
        toposort.reverse()
        return toposort
        