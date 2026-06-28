class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # build a directed graph
        adjList = defaultdict(list)
        for (num, denom), value in zip(equations, values):
            adjList[num].append((denom, value))
            adjList[denom].append((num, 1 / value))

        visited = set()
        def dfs(num, denom):
            if num in visited:
                return -1
            visited.add(num)
            if num == denom:
                return 1
            for neighbour, value in adjList[num]:
                result = dfs(neighbour, denom)
                if result > 0:
                    return value * result
            return -1
        

        output = []
        for num, denom in queries:
            # bfs then multiply the values together along the path
            visited = set()
            if num in adjList and denom in adjList:
                output.append(dfs(num, denom))
            else:
                output.append(-1.0)

        return output
